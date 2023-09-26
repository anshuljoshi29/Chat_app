from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("connected")


    
    def websocket_recieve(self,event):
        print("recieved")
    

    
    def websocket_connect(self,event):
        print("disconnected")