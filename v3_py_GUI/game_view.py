import PySimpleGUI as sg
from minesweeper import pointMatrix
from minesweeper import Minesweeper
import time

class gameScreen:
    def __init__(self, difficulty):
        if(difficulty=='easy'):
            dif = 1
        elif(difficulty=='intermediate'):
            dif = 2
        elif(difficulty=='expert'):
            dif = 3
        self.game = Minesweeper(dif)
        print("Matrix: ",self.game.x,"x",self.game.y)
        #layout
        layout = [
            [sg.Text("Game Minesweeper: "+difficulty)]
        ]
        matrix_game = []
        line = []
        string_but = 1
        for i in range(self.game.x):
            for j in range(self.game.y):
                print(string_but," ", end="")
                line+= [sg.Button("", key=str(string_but), size=(3,0), pad=(0,0))]
                string_but += 1
            matrix_game+=[line]
            print("")
            line = []
        layout+=matrix_game
        #window
        self.window = sg.Window("Minesweeper - Game").layout(layout)

    def play(self):
        #data
        self.window.finalize()
        self.game.printaCampo(1)
        while(1):
            button, self.data = self.window.Read()
            option = 1
            row = 0
            column = 0
            b_num = int(button)
            print("BUTTON: ",b_num)
            while(b_num>self.game.y):
                row=row+1
                b_num=b_num-self.game.y
            column=b_num-1
            print("Coordinate: ", row, ",", column)
            situation = self.game.decisaoJogador(row, column, option)
            self.unlock_button(button,row,column,option)
            if(situation==1):
                self.window.finalize()
                time.sleep(3)
                return 1
            elif(situation==2):
                self.window.finalize()
                time.sleep(3)
                return 2

    def unlock_button(self, button, row, column, option):
        if(option==1):
            if(self.game.matrix[row][column].mine==False):
                if(self.game.matrix[row][column].mines_around!=-1):
                    self.window.FindElement(button).Update(str(self.game.matrix[row][column].mines_around))
                else:
                    self.window.FindElement(button).Update("0")
                    self.cleanZerosView()
                    print("*Zeros Cleaned*")
            elif(self.game.matrix[row][column].mine==True):
                self.window.FindElement(button).Update("*")
        elif(option==2):
            self.window.FindElement(button).Update("B")

    def cleanZerosView(self):
        cont = 1
        while(cont<=((self.game.x)*(self.game.y))):
            but_num=cont
            row = 0
            column = 0
            while(but_num>self.game.y):
                row=row+1
                but_num=but_num-self.game.y
            column=but_num-1
            if(self.game.matrix[row][column].unlocked==True):
                if(self.game.matrix[row][column].mines_around==-1):
                    self.window.FindElement(str(cont)).Update("0")
                else:
                    self.window.FindElement(str(cont)).Update(str(self.game.matrix[row][column].mines_around))
            cont+=1
            

    def close(self):
        self.window.close()

class resultScreen:
    def __init__(self, won):
        if(won==1):
            layout = [
                [sg.Text("You WON!")],
                [sg.Quit()]
            ]
        elif(won==2):
            layout = [
                [sg.Text("You loose.")],
                [sg.Quit()]
            ]
        self.window = sg.Window("Result of the Game").layout(layout)
        self.window.finalize()
        self.button, self.data = self.window.Read()
        
    def close(self):
        self.window.close()