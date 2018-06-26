from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep


class ClientChannel(Channel):

    def Network(self, data):
        print(data)

    def Network_myaction(self, data):
        print("myaction:", data)


class Server(Server):
    channelClass = ClientChannel()

    def Connected(self, channel, addr):
        print("New connection: {}".format(channel))

        # When we receive a new connection
        # Check whether there is a game waiting in the queue
        if self.queue == None:

            # If there isn't someone queueing
            # Set the game ID for the player channel
            # Add a new game to the queue
            channel.gameID = self.gameIndex
            self.queue = Game(channel, self.gameIndex)

        else:

            # Set the game index for the currently connected channel
            channel.gameID = self.gameIndex

            # Set the second player channel
            self.queue.player_channels.append(channel)

            # Send a message to the clients that the game is starting
            for i in range(0, len(self.queue.player_channels)):
                self.queue.player_channels[i].Send(
                    {"action": "startgame", "player": i, "gameID": self.queue.gameID, "velocity": self.velocity})

            # Add the game to the end of the game list
            self.games.append(self.queue)

            # Empty the queue ready for the next connection
            self.queue = None

            # Increment the game index for the next game

            self.gameIndex += 1


if __name__ == "__main__":

    print("Server starting on LOCALHOST...")

    #Create a server
    s = Server()

    #Pump the server at regular intervals (check for new requests)
    while True:
        s.Pump()
        sleep(0.0001)