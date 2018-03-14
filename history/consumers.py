from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from core.auth_mixins import channel_login_required
from history.models import Message, Room


class ChatConsumer(WebsocketConsumer):
    @channel_login_required
    def connect(self):
        self.room_name = 'first_room'
        self.room_group_name = 'chat-%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    @channel_login_required
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    @channel_login_required
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'message': message,
                    'user': self.scope['user'].username
                }
            }
        )

        room = Room.objects.filter(title=self.room_name).first()
        if room is None:
            raise ValueError(f'Room {self.room_name} does not exist')

        Message.objects.create(user=self.scope['user'], room=room, text=message)

    @channel_login_required
    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
