from typing import Union

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

'''
    Websocket endpoint that receives a websocket connection and receives text
'''
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # TODO Write text from client to database
            await websocket.send_text(f'Message text was: {data}')
    except WebSocketDisconnect:
        print('Client disconnected')
