from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected", event)
        self.send({
            'type':'websocket.accept'
        })


    def websocket_receive(self, event):
        print("received", event)

    def websocket_disconnect(self, event):
        print("disconnected", event)

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

    async def websocket_receive(self, event):
        print("received", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
