import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(
            text_data=json.dumps({
                'message': 'Hello From Django ASGI Server!!'
            })
        )

    def receive(self,  text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)