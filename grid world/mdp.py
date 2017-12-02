# -*- coding: utf-8 -*-

def _initialize(size):
    return {
        (x, y): 0 for x in range(size) for y in range(size)        
    }
        
class GridWorld(object):
    """Grid world is a MDP with
    - size * size states, and two
    terminal states:
        
        (0, 0)
        (size-1, size-1)
    
    - four actions:
    
        0  <--->  left
        1  <--->  right
        2  <--->  up
        3  <--->  down
        
    - two rewards:
        
        terminal states:    0
        noterminal states: -1
    
    :param size: size * size grids
    :param gamma: discount factor
    """

    def __init__(self, size, gamma):
        self.size = size
        self.gamma = gamma
    
    @property
    def states(self):
        return [
            (x, y) for x in range(self.size) for y in range(self.size)
        ]
        
    @property
    def actions(self):
        return [0, 1, 2, 3]
    
    @property
    def state_transition_table(self):
        table = {}
        
        for x in range(self.size):
            for y in range(self.size):
                for action in range(4):
                    sa = ((x, y), action)
                    table[sa] = _initialize(self.size)
                    if x > 0 and action == 0:
                        table[sa][(x-1, y)] = 1
                    elif x < self.size-1 and action == 1:
                        table[sa][(x+1, y)] = 1
                    elif y > 0 and action == 2:
                        table[sa][(x, y-1)] = 1
                    elif y < self.size-1 and action == 3:
                        table[sa][(x, y+1)] = 1
                    else:
                        table[sa][(x, y)] = 1
                        
        for action in range(4):
            table[((0, 0), action)] = _initialize(self.size)
            table[((0, 0), action)][(0, 0)] = 1
            table[((self.size-1, self.size-1), action)] = _initialize(self.size)
            table[((self.size-1, self.size-1), action)][(self.size-1, self.size-1)] = 1
            
        return table

    @property
    def reward_table(self):
        table = {}
        
        for x in range(self.size):
            for y in range(self.size):
                for action in range(4):
                    sa = ((x, y), action)
                    table[sa] = -1
                    
        for action in range(4):
            table[((0, 0), action)] = 0
            table[((self.size-1, self.size-1), action)] = 0
            
        return table