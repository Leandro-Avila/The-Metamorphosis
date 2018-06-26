from PodSixNet.Connection import connection
from PodSixNet.Connection import ConnectionListener
from time import sleep

# connect to the server - optionally pass hostname and port like: ("mccormick.cx", 31425)


class OnlineGame(ConnectionListener):

    # Constructor
    def __init__(self):
        # Initialize the gameID and player ID
        self.gameID = None
        self.player = None

        # Connect to the server
        self.Connect()

        # Set running to false
        self.running = False

        # While the game isn't running pump the server
        print('cliente iniciado')
        while not self.running:
            # Pump the server
            self.Pump()
            connection.Pump()
            sleep(0.01)

    def Network_startgame(self, data):
        # Get the game ID and player number from the data
        self.gameID = data['gameID']
        self.player = data['player']

        # Set the game to running so that we enter the update loop
        self.running = True
        self.Send({"action": "myaction", "blah": 123, "things": [3, 4, 3, 4, 7]})


class MyPlayerListener(ConnectionListener):

    def Network_numplayers(data):
        # update gui element displaying the number of currently connected players
        print(data['players'])


if __name__ == "__main__":

    #Create the game object
    og = OnlineGame()

    #Every tick update the game
    while True:
        og.update()