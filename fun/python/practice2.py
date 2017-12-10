from Tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from time import *
from random import *

mixer.init()

root = Tk()
root.title("Texas Hold'em")
root.geometry("800x600")
root.configure(background="black")


class Game:
    def __init__(self):
        self.state=0
        #event width and height
        self.eventWidth=800
        self.eventHeight=600
        #create frame one
        self.image=Image.open("./card/window.jpg")
        self.imageCopy= self.image.copy()
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.background=Label(root,image=self.backgroundImage)
        self.background.pack(fill=BOTH, expand=YES)

        #create start button
        self.startButton=StartButton(self,"./card/start.jpg",0.39,0.85)

        #create music button
        self.musicButton=MusicButton(self,"./card/music.jpg",0.5,0.85)
        self.musicFlag=0

        #create quit button
        self.quitButton=QuitButton(self,"./card/quit.jpg",0.61,0.85)

        #resize frame one
        self.background.bind('<Configure>',self.resizeFrameOne)

        #computer hand
        self.computerHand=['JS','AH']
        #raw_input("Computer hand:").split()
        self.computerCard=[0,0]

        #back card
        self.backCard=[0,0,0,0,0,0,0]

        #board
        self.boardHand=['AC','2H','3D','4S','5H']
        #raw_input("board hand:").split()
        self.boardCard=[0,0,0,0,0]

        #player hand
        self.playerHand=['JS','KH']
        #raw_input("Player hand:").split()
        self.playerCard=[0,0]

        #money
        self.userMoney=40
        self.computerMoney=40
        self.tableMoney=0

    def resizeFrameOne(self,event):
        self.eventWidth=event.width
        self.eventHeight=event.height
        #resize background
        newWidth=event.width
        newHeight=event.height
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.backgroundImage=ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.backgroundImage)

        #resize start button
        self.startButton.resizeImage(event.width,event.height,0.08)

        #resize music button
        self.musicButton.resizeImage(event.width,event.height,0.08)

        #resize quit button
        self.quitButton.resizeImage(event.width,event.height,0.08)


    def resizeFrameTwo(self,event):
        self.eventWidth=event.width
        self.eventHeight=event.height
        #resize background
        newWidth=event.width
        newHeight=event.height
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.backgroundImage=ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.backgroundImage)

        #resize computer hand
        for i in xrange(2):
            self.computerCard[i].resizeImage(event.width,event.height,0.1,0.2)
            self.backCard[i].resizeImage(event.width,event.height,0.1,0.2)

        #resize board
        for i in xrange(5):
            self.boardCard[i].resizeImage(event.width,event.height,0.1,0.2)
            self.backCard[i+2].resizeImage(event.width,event.height,0.1,0.2)

        #resize player hand
        for i in xrange(2):
            self.playerCard[i].resizeImage(event.width,event.height,0.1,0.2)

        #resize music button
        self.musicButton.resizeImage(event.width,event.height,0.08)

        #resize quit button
        self.quitButton.resizeImage(event.width,event.height,0.08)

        #resize fold button
        self.foldButton.resizeImage(event.width,event.height,0.08)

        #resize user money label
        self.userMoneyLabel.resizeImage(event.width,event.height,0.08)

        #resize call button
        self.callButton.resizeImage(event.width,event.height,0.08)

        #resize Raise button
        self.raiseButton.resizeImage(event.width,event.height,0.08)

        #resize computer money label
        self.computerMoneyLabel.resizeImage(event.width,event.height,0.08)

        #resize table money label
        self.tableMoneyLabel.resizeImage(event.width,event.height,0.08)

        #resize action label
        self.action.resizeImage(event.width,event.height,0.08)


    def changeFrame(self):
        #destroy object in frame one
        self.background.destroy()
        self.startButton.button.destroy()
        self.musicButton.button.destroy()
        self.quitButton.button.destroy()

        #create frame two
        self.image=Image.open("./card/window2.jpg")
        self.imageCopy=self.image.copy()
        self.backgroundImage=ImageTk.PhotoImage(self.image)
        self.background=Label(root,image=self.backgroundImage)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>',self.resizeFrameTwo)

        #create computer hand
        for i in xrange(2):
            self.computerCard[i]=Card(self,"./card/"+self.computerHand[i]+".jpg",0.4+i*0.125,0.05)
            self.backCard[i]=Card(self,"./card/back.jpg",0.4+i*0.125,0.05)

        #create board
        for i in xrange(5):
            self.boardCard[i]=Card(self,"./card/"+self.boardHand[i]+".jpg",0.2+i*0.13,0.4)
            self.backCard[i+2]=Card(self,"./card/back.jpg",0.2+i*0.13,0.4)

        #create player hand
        for i in xrange(2):
            self.playerCard[i]=Card(self,"./card/"+self.playerHand[i]+".jpg",0.4+i*0.125,0.75)

        #create music button
        self.musicButton=MusicButton(self,"./card/music.jpg",0.8,0.94)

        #create quit button
        self.quitButton=QuitButton(self,"./card/quit.jpg",0.9,0.94)

        #create fold button
        self.foldButton=FoldButton(self,"./card/fold.jpg",0.8,0.84)

        #create call button
        self.callButton=CallButton(self,"./card/call.jpg",0.8,0.74)

        #create raise button
        self.raiseButton=RaiseButton(self,"./card/raise.jpg",0.9,0.74)

        #create user money label
        self.userMoneyLabel=MoneyLabel(self,"./card/"+str(self.userMoney)+".jpg",0.9,0.84)

        #create computer money label
        self.computerMoneyLabel=MoneyLabel(self,"./card/"+str(self.computerMoney)+".jpg",0.33,0.2)

        #create table money label
        self.tableMoneyLabel=MoneyLabel(self,"./card/"+str(self.tableMoney)+".jpg",0.12,0.55)

        #create action label
        self.action=ShowAction(self,"./card/state.jpg",0.48,0.64)

    def handleMusic(self):
        if self.musicFlag==-1:
            mixer.Channel(0).pause()
            self.musicFlag=1
        elif self.musicFlag==0:
            mixer.Channel(0).play(mixer.Sound('./card/001.ogg'),loops=-1)
            self.musicFlag=-1
        else:
            mixer.Channel(0).unpause()
            self.musicFlag=-1
    def updateByCall(self):
        self.state+=1

        if self.state!=5 and self.computerMoney!=0 and self.userMoney!=0:

            if self.state==1:
                ai=AI(self.computerHand,[])
            elif self.state==2:
                ai=AI(self.computerHand,self.boardHand[0:3])
            elif self.state==3:
                ai=AI(self.computerHand,self.boardHand[0:4])
            elif self.state==4:
                ai=AI(self.computerHand,self.boardHand)

            self.userMoney-=5
            self.tableMoney+=5
            #call
            if ai:
                self.computerMoney-=5
                self.tableMoney+=5
            else:
                self.state=-1
        self.updateMoneyLabel()
        self.handleRound()

    def updateByRaise(self):
        if self.userMoney>=10 and self.computerMoney>=10:
            self.state+=1
            if self.state!=5 and self.computerMoney!=0 and self.userMoney!=0:
                if self.state==1:
                    ai=AI(self.computerHand,[])
                elif self.state==2:
                    ai=AI(self.computerHand,self.boardHand[0:3])
                elif self.state==3:
                     ai=AI(self.computerHand,self.boardHand[0:4])
                elif self.state==4:
                     ai=AI(self.computerHand,self.boardHand)

                self.userMoney-=10
                self.tableMoney+=10
                #call
                if ai:
                    self.computerMoney-=10
                    self.tableMoney+=10
                else:
                    self.state=-1
            self.updateMoneyLabel()
            self.handleRound()
        else:
            self.updateByCall()

    def updateByFold(self):
        self.state+=1
        if self.state!=5 and self.computerMoney!=0 and self.userMoney!=0:
            self.state=-2
        self.updateMoneyLabel()
        self.handleRound()

    def updateMoneyLabel(self):
        #update user money label
        self.userMoneyLabel.label.destroy()
        self.userMoneyLabel=MoneyLabel(self,"./card/"+str(self.userMoney)+".jpg",0.9,0.84)
        self.userMoneyLabel.resizeImage(self.eventWidth,self.eventHeight,0.08)

        #update computer money label
        self.computerMoneyLabel.label.destroy()
        self.computerMoneyLabel=MoneyLabel(self,"./card/"+str(self.computerMoney)+".jpg",0.33,0.2)
        self.computerMoneyLabel.resizeImage(self.eventWidth,self.eventHeight,0.08)

        #update table money label
        self.tableMoneyLabel.label.destroy()
        self.tableMoneyLabel=MoneyLabel(self,"./card/"+str(self.tableMoney)+".jpg",0.12,0.55)
        self.tableMoneyLabel.resizeImage(self.eventWidth,self.eventHeight,0.08)

    def handleRound(self):
        if self.state==1:
            self.backCard[2].card.place_forget()
            self.backCard[3].card.place_forget()
            self.backCard[4].card.place_forget()
        elif self.state==2:
            self.backCard[5].card.place_forget()
        elif self.state==3:
            self.backCard[6].card.place_forget()
            self.backCard[0].card.place_forget()
            self.backCard[1].card.place_forget()
        elif self.state==-1:
            self.actionComputer=ShowAction(self,"./card/fold.jpg",0.48,0.28)
            self.actionComputer.resizeImage(self.eventWidth,self.eventHeight,0.08)
            self.userMoney+=self.tableMoney
            self.tableMoney=0
            self.action.action.destroy()
            self.action=ShowAction(self,"./card/win.jpg",0.48,0.64)
            self.action.resizeImage(self.eventWidth,self.eventHeight,0.08)
            self.state=4
        elif self.state==-2:
            self.computerMoney+=self.tableMoney
            self.tableMoney=0
            self.action.action.destroy()
            self.action=ShowAction(self,"./card/lose.jpg",0.48,0.64)
            self.action.resizeImage(self.eventWidth,self.eventHeight,0.08)
            self.state=4
        elif self.state==4:
            self.judgeGame()
        elif self.state==5:
            self.nextRound()
            self.changeFrame()
            self.state=0

    def judgeGame(self):
        win=randint(0,2)
        if win!=0:
            self.action.action.destroy()
            self.action=ShowAction(self,"./card/win.jpg",0.48,0.64)
            self.action.resizeImage(self.eventWidth,self.eventHeight,0.08)
            self.userMoney+=self.tableMoney
            self.tableMoney=0
        else:
            self.action.action.destroy()
            self.action=ShowAction(self,"./card/lose.jpg",0.48,0.64)
            self.action.resizeImage(self.eventWidth,self.eventHeight,0.08)
            self.computerMoney+=self.tableMoney
            self.tableMoney=0
        if self.computerMoney==0:
            print "WIN WIN WIN"
            self.computerMoney=40
            self.userMoney=40
        elif self.userMoney==0:
            print "LOSE LOSE LOSE"
            self.computerMoney=40
            self.userMoney=40

    def nextRound(self):
        #computer hand
        self.computerHand=['3S','4H']

        #board
        self.boardHand=['JC','KH','QD','QS','JH']

        #player hand
        self.playerHand=['2S','3H']


        #create computer hand
        for i in xrange(2):
            self.computerCard[i].card.destroy()


        #create board
        for i in xrange(5):
            self.boardCard[i].card.destroy()


        #create player hand
        for i in xrange(2):
            self.playerCard[i].card.destroy()




class ShowAction:
    def __init__(self,parant,path,x,y):
        #create action label
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.actionImage=ImageTk.PhotoImage(self.image)
        self.action=Label(self.parant.background,image=self.actionImage)
        self.action.place(relx=x,rely=y)

        #action width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter action
        self.action.bind('<Enter>',self.inLabel)
        #leave action
        self.action.bind('<Leave>',self.outLabel)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.actionImage=ImageTk.PhotoImage(self.image)
        self.action.configure(image=self.actionImage)

    def inLabel(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outLabel(self,event):
        self.resizeImage(self.width,self.height,0.08)



class StartButton:
    def __init__(self,parant,path,x,y):
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.buttonImage=ImageTk.PhotoImage(self.image)
        #change frame one to two
        self.button=Button(self.parant.background,image=self.buttonImage,command=parant.changeFrame)
        self.button.place(relx=x,rely=y,anchor=CENTER)


        #button width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter start button
        self.button.bind('<Enter>',self.inButton)
        #leave start button
        self.button.bind('<Leave>',self.outButton)

    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)

        self.buttonImage=ImageTk.PhotoImage(self.image)
        self.button.configure(image=self.buttonImage)

    def inButton(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outButton(self,event):
        self.resizeImage(self.width,self.height,0.08)

class MusicButton:
    def __init__(self,parant,path,x,y):
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.buttonImage=ImageTk.PhotoImage(self.image)

        #play or stop music
        self.button=Button(self.parant.background,image=self.buttonImage,command=parant.handleMusic)
        self.button.place(relx=x,rely=y,anchor=CENTER)

        #button width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter music button
        self.button.bind('<Enter>',self.inButton)
        #leave music button
        self.button.bind('<Leave>',self.outButton)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.buttonImage=ImageTk.PhotoImage(self.image)
        self.button.configure(image=self.buttonImage)

    def inButton(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outButton(self,event):
        self.resizeImage(self.width,self.height,0.08)

class QuitButton:
    def __init__(self,parant,path,x,y):
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.buttonImage=ImageTk.PhotoImage(self.image)

        #quit
        self.button=Button(self.parant.background,image=self.buttonImage,command=root.quit)
        self.button.place(relx=x,rely=y,anchor=CENTER)

        #button width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter quit button
        self.button.bind('<Enter>',self.inButton)
        #leave quit button
        self.button.bind('<Leave>',self.outButton)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.buttonImage=ImageTk.PhotoImage(self.image)
        self.button.configure(image=self.buttonImage)

    def inButton(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outButton(self,event):
        self.resizeImage(self.width,self.height,0.08)

class Card:
    def __init__(self,parant,path,x,y):

        #create card
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.cardImage=ImageTk.PhotoImage(self.image)
        self.card=Label(self.parant.background,image=self.cardImage)
        self.card.place(relx=x,rely=y)

        #card width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter card
        self.card.bind('<Enter>',self.inLabel)
        #leave card
        self.card.bind('<Leave>',self.outLabel)


    def resizeImage(self,width,height,scaleX,scaleY):
        self.width=width
        self.height=height
        newWidth=int(width*scaleX)
        newHeight=int(height*scaleY)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.cardImage=ImageTk.PhotoImage(self.image)
        self.card.configure(image=self.cardImage)

    def inLabel(self,event):
        self.resizeImage(self.width,self.height,0.12,0.22)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outLabel(self,event):
        self.resizeImage(self.width,self.height,0.1,0.2)

class FoldButton:
    def __init__(self,parant,path,x,y):
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.buttonImage=ImageTk.PhotoImage(self.image)

        #fold command
        self.button=Button(self.parant.background,image=self.buttonImage,command=parant.updateByFold)
        self.button.place(relx=x,rely=y,anchor=CENTER)

        #button width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter quit button
        self.button.bind('<Enter>',self.inButton)
        #leave quit button
        self.button.bind('<Leave>',self.outButton)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.buttonImage=ImageTk.PhotoImage(self.image)
        self.button.configure(image=self.buttonImage)

    def inButton(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outButton(self,event):
        self.resizeImage(self.width,self.height,0.08)

class CallButton:
    def __init__(self,parant,path,x,y):
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.buttonImage=ImageTk.PhotoImage(self.image)

        #call command
        self.button=Button(self.parant.background,image=self.buttonImage,command=parant.updateByCall)
        self.button.place(relx=x,rely=y,anchor=CENTER)

        #button width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter quit button
        self.button.bind('<Enter>',self.inButton)
        #leave quit button
        self.button.bind('<Leave>',self.outButton)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.buttonImage=ImageTk.PhotoImage(self.image)
        self.button.configure(image=self.buttonImage)

    def inButton(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outButton(self,event):
        self.resizeImage(self.width,self.height,0.08)

class RaiseButton:
    def __init__(self,parant,path,x,y):
        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.buttonImage=ImageTk.PhotoImage(self.image)

        #raise command
        self.button=Button(self.parant.background,image=self.buttonImage,command=parant.updateByRaise)
        self.button.place(relx=x,rely=y,anchor=CENTER)

        #button width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter quit button
        self.button.bind('<Enter>',self.inButton)
        #leave quit button
        self.button.bind('<Leave>',self.outButton)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.buttonImage=ImageTk.PhotoImage(self.image)
        self.button.configure(image=self.buttonImage)

    def inButton(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outButton(self,event):
        self.resizeImage(self.width,self.height,0.08)

class MoneyLabel:
    def __init__(self,parant,path,x,y):

        self.parant=parant
        self.image=Image.open(path)
        self.imageCopy=self.image.copy()
        self.labelImage=ImageTk.PhotoImage(self.image)

        #money command
        self.label=Label(self.parant.background,image=self.labelImage)
        self.label.place(relx=x,rely=y,anchor=CENTER)

        #lable width and height
        self.width=parant.eventWidth
        self.height=parant.eventHeight
        #enter quit label
        self.label.bind('<Enter>',self.inLabel)
        #leave quit label
        self.label.bind('<Leave>',self.outLabel)


    def resizeImage(self,width,height,scale):
        self.width=width
        self.height=height
        newWidth=int(width*scale)
        newHeight=int(height*scale)
        self.image=self.imageCopy.resize((newWidth,newHeight),Image.ANTIALIAS)
        self.labelImage=ImageTk.PhotoImage(self.image)
        self.label.configure(image=self.labelImage)

    def inLabel(self,event):
        self.resizeImage(self.width,self.height,0.1)
        mixer.Channel(1).play(mixer.Sound('./card/002.ogg'))
    def outLabel(self,event):
        self.resizeImage(self.width,self.height,0.08)

def AI(a,b):
    # print a,b
    x,y = numberized(b,a)
    if y[0][0] == y[1][0] and y[0][0] >= x[1][0] and len(x) == 3:
        if random() < 0.85:
            return True
    # compare total value
    if y[0][0] + y[1][0] >= x[1][0] + x[randint(0,len(x)-1)][0]:
        if random() < 0.6:
            return True
    # compare color
    colourList = [y[0][1], y[1][1]]
    for i in range(len(x)):
        colourList += [x[i][1]]
    colourList.sort()
    for i in range(len(colourList)):
        if i+2 < len(colourList) and colourList[i] == colourList[i+1] == colourList[i+2]:
            if random() < 0.55:
                return True
        if i+3 < len(colourList) and colourList[i] == colourList[i+1] == colourList[i+2] == colourList[i+3]:
            if random() < 0.67:
                return True
        if i+4 < len(colourList) and colourList[i] == colourList[i+1] == colourList[i+2] == colourList[i+3] == colourList[i+4]:
            return True
    # compare bot and table
    for i in range(len(y)):
        for j in range(len(x)):
            if y[i][0] == x[j][0] and y[i][0] >= x[randint(0,len(x)-1)][0]:
                if random() < 0.85:
                    return True
    return False

def numberized(tableCard, aiCard):
        number = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        shape = ['S','H','C','D']
        tCard =[]
        aCard = []
        tCard = progress(tableCard,number,shape)
        aCard = progress(aiCard,number,shape)
        return tCard,aCard

def progress(card,number,shape):
        Card = []
        for a in range(len(card)) :
                for b in range(len(card[a])):
                        if b==0:
                                x = number.index(card[a][b])
                        elif b==1:
                                y = shape.index(card[a][b])
                Card.append([x,y])
        return Card


def main():

    game=Game()


    root.mainloop()

if __name__=='__main__':
    main()
