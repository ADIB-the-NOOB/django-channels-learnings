import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from .models import Message
from channels.db import database_sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the room name from the URL.
        self.room_name = 'chat_room'
        self.messages = await self.get_messages()
        # Add the current user to the room group.
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        # Send a welcome message to the user.
        await self.accept()

        await self.send(text_data=json.dumps({
            'message': 'Hello there!',
            'Previous_messages': self.messages 
        }))

        # Accept the connection.
    
    @database_sync_to_async
    def get_messages(self):
        return list(Message.objects.all().values('message'))

    async def disconnect(self, close_code):
        # Remove the current user from the room group.
        await self.channel_layer.group_discard(self.room_name, self.channel_name)


    async def receive(self, text_data):
        # Get the message from the JSON data.
        message = json.loads(text_data)['message']
        created_message = await self.save_message(message)
    
        # Send the message to all users in the room group.
        await self.channel_layer.group_send(self.room_name, {
            'type': 'chat_message',
            'message': message,
          })


    async def chat_message(self, event):
        # Get the message from the event data.
        message = event['message']

        # Send the message to the client.
        await self.send(text_data=json.dumps({
            'message': message,
        }))

    @database_sync_to_async
    def save_message(self, message):
        return Message.objects.create(message=message)
    


