import pokemonTypes


pokedex = {'Charizard':[8,6,7],'Gyrados':[7.5,7,8],'Pikachu':[5,7,7],'Steelix':[4,9.5,5.5],'Zapdos':[7,8,9.5],'Mewtwo':[8,7,7]}

class Player:

    def __init__(self,name,team,money):

        self.name = name
        self.team = team
        self.money = money
        self.isBattling = False
        self.teamAlive = True
        self.firstPokemon = self.team[0]
        self.currentPokemon = self.firstPokemon

    def enterBattle(self,opponent):

        while(self.teamAlive and opponent.teamAlive):

            action = input("Enter f for fight, c for change pokemon, r run")

            if(action == "f"):

                moveNumber = int(input("Enter 1,2,3,4, or 5 to go back"))

                self.currentPokemon.useMove(moveNumber,opponent)

            elif(action == "c"):

                pass
            elif(action == "r"):

                pass










class Move:

    def __init__(self,name,damage,usesLeft,type,noTarget,effect):
        self.damage = damage
        self.effect = effect
        self.name = name
        self.usesLeft = usesLeft
        self.type = type
        self.noTarget = noTarget

class Pokemon:

    def __init__(self,hp,level,moves,a,d,s,teachableMoves):
        self.hp = hp
        self.level = level
        self.moves = moves
        self.attack = a
        self.defense = d
        self.speed = s

        self.teachableMoves = teachableMoves

    def isAlive(self):
        if(self.hp <= 0):
            return False
        return True

    def learn(self, move, moveNumber):
        if(self.teachableMoves.contains(move)):
            self.moves[moveNumber-1] = move

        else:
            print("This pokemon cannot learn " + move.name)


    def useMove(self,moveNumber,target):
        if(moveNumber <= 4 and moveNumber >= 1):
            if(not(self.moves[moveNumber-1].noTarget)):
                target.hp -= self.moves[moveNumber-1].damage
                self.moves[moveNumber - 1].usesLeft -1

            else:
                if(self.moves[moveNumber-1].effect[0] == 'attack'):
                    self.attack += self.moves[moveNumber-1].effect[1]
                    self.moves[moveNumber - 1].usesLeft - 1
                elif(self.moves[moveNumber-1].effect[0] == 'defense'):
                    self.defense += self.moves[moveNumber-1].effect[1]
                    self.moves[moveNumber - 1].usesLeft - 1
                elif(self.moves[moveNumber-1].effect[0] == 'speed'):
                    self.speed += self.moves[moveNumber-1].effect[1]
                    self.moves[moveNumber - 1].usesLeft - 1
                else:
                    print("move is encoded incorrect. Need to select attack,defense, or speed as the effect type")

        else:
            print("Please enter a move number between 1 and 4")



tackle = Move("Tackle", 5, 30, "Normal",False,None)
flameThrower = Move("Flame Thrower", 20, 15, "Fire",False,None)
waterGun = Move("Water Gun", 10, 30,"water",False,None)
growl = Move("Growl",0,30,"normal",True,['attack',2])
kick = Move("Kick", 7, 40, "fighting",False,None)
rockThrow = Move("Rock Throw", 9,"ground",False,None)



charmander = Pokemon(40,8,[flameThrower,growl,tackle,kick],5,4,4,None)