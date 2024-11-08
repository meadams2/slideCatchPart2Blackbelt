"""Marianne Adams
CS120 Slide Catch Blackbelt
Addition of a "Win" and a "Lose"""

import simpleGE, pygame, random

class Wednesday(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Wednesday.png")
        self.setSize (75, 75)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Leaf(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("FallLeaf.png")
        self.setSize(40, 40)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = 0
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Apple(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Apple.png")
        self.setSize(20, 20)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
    
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = 0
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
    
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("FallScene.png")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.score = 0
        
        self.wednesday = Wednesday(self)
        
        self.leaves = []
        for i in range(10):
            self.leaves.append(Leaf(self))
        
        self.apples = []
        for i in range(3):
            self.apples.append(Apple(self))
        
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.sprites = [self.wednesday,
                        self.leaves,
                        self.apples,
                        self.lblScore,
                        self.lblTime]
    def process(self):
        for leaf in self.leaves:
            if self.wednesday.collidesWith(leaf):
                leaf.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
        for apple in self.apples:
            if self.wednesday.collidesWith(apple):
                apple.reset()
                self.score -= 1
                self.lblScore.text = f"Score: {self.score}"
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft(): .2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            if self.score >= 10:
                self.level = "Win"
            else:
                self.level = "Lose"
            print(f"{self.level}")
            self.stop()
            

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()