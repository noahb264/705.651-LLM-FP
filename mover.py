from abc import abstractmethod
import random

class Mover():

    @abstractmethod
    def get_next_move(self, current_lvl):
        pass

class RandomMover(Mover):

    def get_next_move(self, current_lvl):
        player = random.choice(["A", "B"])
        move = random.choice(["move right", "move left", "jump on right", "jump on left"])
        return {player: move}
    
class LlmMover(Mover):
    
    def get_next_move(self, current_lvl):
        pass
        

MOVERS = {
    "random": RandomMover
}