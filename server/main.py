from fastapi import FastAPI
from socketio import AsyncServer, ASGIApp


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
    print("New Client Connected to This id :"+" "+str(sid))
    
@sio.on("disconnect")
async def disconnect(sid):
    print("Client Disconnected: "+" "+str(sid))
    
@sio.on("chat_message")
async def chat_message(sid, data):
    print("Message from client:", data)
    await sio.emit('chat_message', data) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
