from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio


class CodeExecutionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('type') == 'code':
            code = data['code']
            asyncio.create_task(self.execute_code(code))
        elif data.get('type') == 'input':
            user_input = data['input']

    async def execute_code(self, code):
        await self.send(text_data=json.dumps({
            'type': 'input_request',
            'message': 'Input is required'
        }))
