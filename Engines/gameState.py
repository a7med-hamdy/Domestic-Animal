class gameState():

    def __init__(self,powerups,score,bullets,players,enemies,difficulty,isExit,level,time):
        
        self.powerups=powerups
        self.bullets=bullets
        self.players=players
        self.enemies=enemies
        self.difficulty=difficulty
        self.level=level
        self.time=time
        self.Score=score
        self.isExit=isExit
