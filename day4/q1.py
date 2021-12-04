class Board:
    def __init__(self, data):
        self.position = {}
        self.playBoard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0],
            "diagonal" : [0,0]
        }
        self.picked = []

        self.loadBoard(data)
        self.won = False

    
    def loadBoard(self,data):       
        for i in range(5):            
            for j in range(5):
                choice = int(data[i][j])
                self.playBoard[i][j] = choice
                self.position[choice] = (i,j)
    
    def updateBoard(self, val):
        #print (self.position)
        try:
            x,y = self.position[val]
            self.playBoard[x][y] = 'X'
            self.updateBingo(x,y)
            self.picked.append(val)
        except KeyError:
            return
        
    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1
        
        if x==y==2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x==y:
            self.bingo["diagonal"][0] += 1
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1
    
    def checkBingo(self):
        #OMG, I DID NOT read you can't win on a diagonal
        #return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]
        
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] 

    def displayBoard(self):
        for i in range(5):
            for j in self.playBoard[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print()


    def sumBoard(self):
        total = 0
        for i in range(5):
            for j in self.playBoard[i]:
                if j!='X':                   
                    total += int(j)

        return total
           


class Game:
    def __init__(self):
        self.cards = []
        self.pulled = []
        self.winner = -1
    
    def displayGame(self):
        #print ("Pulled:"+str(self.pulled))
        print ("============")
        for card in self.cards:            
            card.displayBoard()
            print ()

    def pick(self,index):
        #print ("Pick: "+self.pulled[index])
        for card in self.cards:            
            card.updateBoard(int(self.pulled[index]))


    def checkBingo(self):     
        for i in range(len(self.cards)):
            if self.cards[i].checkBingo():
                # we have a winner
                self.winner = i
                return True
        return False

    def play(self):
        for i in range(len(self.pulled)):
            self.pick(i)
            #self.displayGame()
            if self.checkBingo():
                print ("Winner is "+str(self.winner))
                self.cards[self.winner].displayBoard()
                boardsum = self.cards[self.winner].sumBoard()
                print (f"{boardsum=}")
                print ("last pull="+self.pulled[i])
                result = int(boardsum) * int(self.pulled[i])
                print (f"{result=}")
                
                return

    def numWinners(self):
        total = 0
        for card in self.cards:
            if card.won:
                total += 1        
        return (total)
            
            

    def lastToWin(self):
        last_win = 0
        for i in range(len(self.pulled)):
            self.pick(i)
            for j in range(len(self.cards)):
                if not self.cards[j].won and self.cards[j].checkBingo():
                    self.cards[j].won = True
                    last_win = j

                    
            #print ("Cards: "+str(len(self.cards)))
            #print ("Winners: "+str(self.numWinners()))
            if len(self.cards) - self.numWinners() == 0:
                self.cards[last_win].displayBoard()
                boardsum = self.cards[last_win].sumBoard()
                print (f"{boardsum=}")
                print ("last pull="+self.pulled[i])
                result = int(boardsum) * int(self.pulled[i])
                print (f"{result=}")
                return

    def loadGame(self,file_name):
        with open(file_name, 'r') as data_file:
            data = []
            for index, line in enumerate(data_file):
                line = line.strip()
            
                if index == 0:
                    self.pulled = line.split(",")            
                    continue

                if line == '' and index != 1:
                    card = Board(data)            
                    data = []
                    self.cards.append(card)
                
                            
                if line != '':
                    values = line.split()
                    data.append(values)
                
            card = Board(data)             
            self.cards.append(card)

                
# main
fname = 'data.txt'

bingo = Game()
bingo.loadGame(fname)
print ("Part 1")
bingo.play()

print ("\nPart 2")
bingo2 = Game()
bingo2.loadGame(fname)
bingo2.lastToWin()
