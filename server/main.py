from fastapi import FastAPI
from socketio import AsyncServer, ASGIApp
import random
from datetime import datetime


class User():
    def __init__(self,username,sid):
        self.username = username
        self.sid = sid
        self.color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

users = {str:User} #{sid:User}

app = FastAPI()
# to run the server -> uvicorn main:app --reload
# Create Socket.IO server
sio = AsyncServer(cors_allowed_origins='*',async_mode='asgi')
socketio_app = ASGIApp(sio)

app.mount("/socket.io/", socketio_app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@sio.on("connect")
async def connect(sid, env):
    print("Client Connected: "+" "+str(sid))
    users[sid] = User(env['HTTP_USERNAME'],str(sid))
    
@sio.on("disconnect")
async def disconnect(sid):
    print("Client Disconnected: "+" "+str(sid))
    users.pop(str(sid))
    
@sio.on("chat_message")
async def chat_message(sid, data):
    print("Message from client:", users[sid].username ," message:", data)
    c = datetime.now()
    current_time = c.strftime('%H:%M:%S')
    stamp = f"{current_time}:{data[0]}:"
    await sio.emit('chat_message', [users[sid].username, data, users[sid].color,stamp] ) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
