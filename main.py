"""
Example for run HTTPWebServer
"""
from HTTPWebServer.HTTPWebServer import HTTPWebServer

app = HTTPWebServer()

print(1)


@app.get('/')
async def home():
    return {'key': 1}


home()
