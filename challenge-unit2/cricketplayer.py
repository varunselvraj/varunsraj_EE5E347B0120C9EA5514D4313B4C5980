# Parent class: Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Derived class 1: Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Derived class 2: Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Creating objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Calling play() method for each object
batsman.play()
bowler.play()