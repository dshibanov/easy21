# TODO:
# - make states.n, actions.n like in gym ai api
# - add tests


import random

class Easy21:
    def __init__(self, logging=False):    
        # hit = 1, stick = 0
        self.logging = logging
        self.reset()         
                    
    def draw_a_card(self, black_only=False):                        
        if black_only: 
            r = random.randint(1, 10)                
        else:
            r = random.randint(1, 10)*(-1 if random.random() < 1/3 else 1)
        if self.logging: print('C:', r)
        return r
    
    def state(self):
            return [self.dealer_sum, self.player_sum]
        
    def set_state(self, state):
        self.dealer_sum, self.player_sum = state[0], state[1]
        
    def draw(self):
        return self.player_sum == 21
    
    def goes_bust(self, summ):        
        if summ > 21 or summ < 1:            
            return True
        
    def dealer_hit(self):
        if self.dealer_sum < 17:
            return True
        return False
                
    def step(self, action): 
        
        state = self.state()
        if self.started == False:       
            self.reset()
            self.start()
            
            return state, action, 0
        else:
            if action == 1:
                if self.logging: print('hit')
                self.player_sum += self.draw_a_card()
                
                if self.draw():                    
                    if self.logging: print('R: draw')                    
                    self.started = False
                    return state, action, 0
                
                if self.goes_bust(self.player_sum):                    
                    if self.logging: print('R: dealer win')                    
                    self.started = False
                    return state, action, -1
                                
                return state, action, 0
            else:
                if self.logging: print('stick')
                while self.dealer_hit():
                    self.dealer_sum += self.draw_a_card()

                if self.goes_bust(self.dealer_sum) or self.dealer_sum < self.player_sum:                        
                    if self.logging: print('R: player win')
                    self.started = False
                    return state, action, 1
                
                if self.dealer_sum > self.player_sum:                    
                    if self.logging: print('R: dealer win')
                    self.started = False
                    return state, action, -1
                
                if self.dealer_sum == self.player_sum:
                    if self.logging: print('R: draw')                    
                    self.started = False
                    return state, action, 0
                                                    
                return state, action, 0

    def start(self):
        if self.logging: print('start a new game..')
        self.player_sum = self.draw_a_card(True)
        self.dealer_sum = self.draw_a_card(True)
        self.started = True
        
    def reset(self):
        if self.logging: print('reset')
        self.dealer_sum = 0
        self.player_sum = 0
        self.started = False
        return 0
