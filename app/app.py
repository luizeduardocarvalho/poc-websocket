import os
import sqlite3
from services.Command import Command
from services.Command import CommandService
from services.Data import DataInitializer
from services.Data import DataController

from starlette.applications import Starlette
from starlette.websockets import WebSocketDisconnect
import json
import logging
import uvicorn

from datetime import datetime, timedelta
from json import dumps, load, loads

from flask import Flask, render_template, Response, request

app = Starlette()

websockets = {
    'web': {},
    'desktop': {},
}

async def receive_json(websocket):
    message = await websocket.receive_text()
    return json.loads(message)

@app.websocket_route('/ws')
async def websocket_endpoint(websocket):
    await websocket.accept()

    # "Authentication" message
    message = await receive_json(websocket)
    client_mode = message['client_mode']
    client_id = message['client_id']
    websockets[client_mode][client_id] = websocket

    # Get mirror mode to broadcast messages to the client on the other side
    mirror_mode = 'web' if client_mode == 'desktop' else 'desktop'

    client_string = f'{client_id}[{client_mode}]'
    print(f'Client connected: {client_string}')

    while (True):
        try:
            # Wait for a message from the client
            message = await receive_json(websocket)
            print(f'Message received from {client_string}: {message}')

            try:
                # Broadcast it to the mirror client
                await websockets[mirror_mode][client_id].send_text(
                    json.dumps(message)
                )
            except KeyError:
                print(
                    f'Client {client_id}[{mirror_mode}] not connected'
                )
        except WebSocketDisconnect:
            break

    del websockets[client_mode][client_id]
    await websocket.close()
    print(f'Client disconnected: {client_string}')


@app.route('/', methods=['GET'])
def index():
    """Return the index.html page"""
    return render_template('index.html')



if __name__ == '__main__':
    DataInitializer.initialize()
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host='0.0.0.0', port=port, debug=True)
    
    
