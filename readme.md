# Running Server Client

Create an app on Heroku and execute the following commands:
* heroku login
* heroku container:login
* heroku container:push web -\<heroku-app-name\>
* heroku container:release web -\<heroku-app-name\>

# Running Desktop Client
* python desktop.py <client-name>

**NOTE: Change the app name inside the desktop and web code**

### Web
const socket = new WebSocket("ws://**\<app-url\>**/ws");

### Desktop
asyncio.get_event_loop().run_until_complete(
        handler('ws://**\<app-url\>**/ws', sys.argv[1])
    )


