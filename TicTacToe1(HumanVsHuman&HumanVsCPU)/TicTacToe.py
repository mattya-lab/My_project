# codeing=UTF8
import random

class TicTacToe():
    def __init__(self):
        self.table = [" " for x in range(10)]
        self.turn = None
        self.human = None
        self.cpu = None
        self.bestscore = -999

        
    def resetTable(self):
        self.table = [" " for x in range(10)]

    def getRandomFirst(self):
        self.turn = random.randrange(0, 2)
        if self.turn == 0:
            self.human = 0
            self.cpu = 1
        else :
            self.human = 1
            self.cpu = 0
     
    def printTable(self, bo):
        print('   |   |')
        print(' ' + bo[1] + ' | ' + bo[2] + ' | ' + bo[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + bo[4] + ' | ' + bo[5] + ' | ' + bo[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + bo[7] + ' | ' + bo[8] + ' | ' + bo[9])
        print('   |   |')
    
    def isTableFull(self, bo):
        if bo.count(' ') > 1:
            return False
        else:
            return True
    
    def isWinner(self, bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[6] == le and bo[3] == le) or
        (bo[7] == le and bo[5] == le and bo[3] == le) or 
        (bo[9] == le and bo[5] == le and bo[1] == le)) 

    def insertTable(self, letter, pos):
        self.table[pos] = letter

    def spaceIsFree(self, pos):
        return self.table[pos] == ' '
    
    def changeLetter(self):
        if self.turn % 2 == 0:
            return 'O'
        else :
            return 'X'

    def playerMove(self, letter):
        run = True
        while run:
            move = input('Please select a position to place an O (1-9): ')
            try:
                move  = int(move)
                if 0 < move and move < 10:
                    if self.spaceIsFree(move):
                        run = False
                        self.insertTable(letter, move)
                    else:
                        print('This postion is already occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')

    def playHumanVsHuman(self):
        print('Welcome to the Tic Tac Toe Game')
        while True:
            self.resetTable()
            self.getRandomFirst()  
            self.printTable(self.table)
            WinFlag = True
            while not self.isTableFull(self.table):
                for let in ['O', 'X']:
                    if self.isWinner(self.table, let):
                        if let == 'O':
                            print('O s win this time')
                            WinFlag = False
                        else :
                            print('X s win this time')
                            WinFlag = False

                if not WinFlag:
                    break

                letter = self.changeLetter()
                self.playerMove(letter)
                self.printTable(self.table)
                self.turn = self.turn + 1


    def minimax(self, bo, depth, isMaximizing, alpha, beta):

        if self.isWinner(bo, 'O'):
            return -10
        if self.isWinner(bo, 'X'):
            return 10
        if self.isTableFull(bo) or depth == 0:
            return 0 

        if isMaximizing :
            bestscore = -999
            for cell in range(1, 10):
                if bo[cell] == ' ':
                    bo[cell] = 'X' 
                    score = self.minimax(bo, depth - 1, False, alpha, beta)
                    bo[cell] = ' '
                    if score > bestscore:
                        bestscore = score
                    if bestscore > alpha:
                        alpha = bestscore
                    if beta <= alpha:
                        break
               
            return bestscore

        else :
            bestscore = 999
            for cell in range(1, 10):
                if bo[cell] == ' ':
                    bo[cell] = 'O'
                    score = self.minimax(bo, depth - 1, True, alpha, beta)
                    bo[cell] = ' '
                    if score < bestscore:
                        bestscore = score
                    if bestscore < beta:
                        beta = bestscore
                    if beta <= alpha:
                        break
            return bestscore

    def compMove(self, letter):
        bestscore = -999
        possibleMoves = [x for x, letter in enumerate(self.table) if letter == ' ' and x != 0]
        bestmove = 0
        bo = []
        for cell in range(10):
            bo.append(self.table[cell])

        for moves in possibleMoves:
            print('-------------' + str(moves) + "--------------" )
            bo[moves] = "X"
            score = self.minimax(bo, len(possibleMoves), False, -999, 999)
            bo[moves] = " "
            print(score)
            if score > bestscore:
                bestscore = score
                bestmove = moves
                
        print(str(bestmove) + " : " + str(bestscore))
        if bestmove != 0:
            self.insertTable(letter, bestmove)

    def playHumanVsCPU(self):
        print('Welcome to the Tic Tac Toe Game')
        while True:
            self.resetTable()
            self.getRandomFirst()
            self.printTable(self.table)

            WinFlag = True
            while not self.isTableFull(self.table):
                for let in['O', 'X']:
                    if self.isWinner(self.table, let):
                        if let == 'O':
                            print('O s win this time')
                            WinFlag = False
                        else :
                            print('X s win this time')
                            WinFlag = False

                if not WinFlag:
                    break

                if self.human == 0:
                    if self.turn % 2 == 0:
                        self.playerMove('O')
                    else:
                        self.compMove('X')
                else:
                    if self.turn % 2 == 0:
                        self.playerMove('O')
                    else :
                        self.compMove('X')
                
                self.printTable(self.table)
                self.turn = self.turn + 1

if __name__ == "__main__":
    tic = TicTacToe()
    #tic.playHumanVsHuman()
    tic.playHumanVsCPU()