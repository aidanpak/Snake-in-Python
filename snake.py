from graphics import *
from random import *

snake_segment=[]
#this stores our snake as a list

class Snake():
    def __init__(self,length=1, color="red", x=400,y=400, direction=""):
        self.length=length
        self.color=color
        self.x=x
        self.y=y
        self.direction=direction
        self.segment_directionx=[]
        self.segment_directiony=[]
        self.segment_directionx_storage=[]
        self.segment_directiony_storage=[]
    def drawSnake(self,win):
        segment=Rectangle(Point(self.x+10,self.y+10), Point(self.x-10,self.y-10))
        segment.setFill('red')
        segment.draw(win)
        snake_segment.append(segment)
        self.segment_directionx.append(0)
        self.segment_directiony.append(0)
        self.segment_directionx_storage.append(0)
        self.segment_directiony_storage.append(0)
        return snake_segment

    # the four methods Up, Down, Left, and Right append the directions lists defined in __init__
    def Up(self,win):
        self.segment_directionx[0]= 0
        self.segment_directiony[0]= -20
        self.x=self.x+self.segment_directionx[0]
        self.y=self.y+self.segment_directiony[0]
        for i in range(0, len(snake_segment)):
            snake_segment[i].undraw()
            snake_segment[i].move(self.segment_directionx[i], self.segment_directiony[i])
            snake_segment[i].draw(win)
        for i in range(1, len(snake_segment)):
            self.segment_directionx_storage[i]= self.segment_directionx[i-1]
            self.segment_directiony_storage[i]= self.segment_directiony[i-1]
        for i in range(1, len(snake_segment)):
            self.segment_directionx[i]=self.segment_directionx_storage[i]
            self.segment_directiony[i]=self.segment_directiony_storage[i]
        return True

    def Down(self,win):
            self.segment_directionx[0]= 0
            self.segment_directiony[0]= 20
            self.x=self.x+self.segment_directionx[0]
            self.y=self.y+self.segment_directiony[0]
            for i in range(0, len(snake_segment)):
                snake_segment[i].undraw()
                snake_segment[i].move(self.segment_directionx[i], self.segment_directiony[i])
                snake_segment[i].draw(win)
            for i in range(1, len(snake_segment)):
                self.segment_directionx_storage[i]= self.segment_directionx[i-1]
                self.segment_directiony_storage[i]= self.segment_directiony[i-1]
            for i in range(1, len(snake_segment)):
                self.segment_directionx[i]=self.segment_directionx_storage[i]
                self.segment_directiony[i]=self.segment_directiony_storage[i]
            return True

    def Left(self,win):
            self.segment_directionx[0]= -20
            self.segment_directiony[0]= 0
            self.x=self.x+self.segment_directionx[0]
            self.y=self.y+self.segment_directiony[0]
            for i in range(0, len(snake_segment)):
                snake_segment[i].undraw()
                snake_segment[i].move(self.segment_directionx[i], self.segment_directiony[i])
                snake_segment[i].draw(win)
            for i in range(1, len(snake_segment)):
                self.segment_directionx_storage[i]= self.segment_directionx[i-1]
                self.segment_directiony_storage[i]= self.segment_directiony[i-1]
            for i in range(1, len(snake_segment)):
                self.segment_directionx[i]=self.segment_directionx_storage[i]
                self.segment_directiony[i]=self.segment_directiony_storage[i]
            return True

    def Right(self,win):
            self.segment_directionx[0]= 20
            self.segment_directiony[0]= 0
            self.x=self.x+self.segment_directionx[0]
            self.y=self.y+self.segment_directiony[0]
            for i in range(0, len(snake_segment)):
                snake_segment[i].undraw()
                snake_segment[i].move(self.segment_directionx[i], self.segment_directiony[i])
                snake_segment[i].draw(win)
            for i in range(1, len(snake_segment)):
                self.segment_directionx_storage[i]= self.segment_directionx[i-1]
                self.segment_directiony_storage[i]= self.segment_directiony[i-1]
            for i in range(1, len(snake_segment)):
                self.segment_directionx[i]=self.segment_directionx_storage[i]
                self.segment_directiony[i]=self.segment_directiony_storage[i]
            return True

    def moveSnake(self, key, win):
        if self.direction == 'Up':
            self.Up(win)
        elif self.direction == 'Down':
            self.Down(win)
        elif self.direction == 'Left':
            self.Left(win)
        elif self.direction == 'Right':
            self.Right(win)

    def getX(self):
        return (self.x)
    def getY(self):
        return (self.y)
        #end of class Snake

#addLength function adds a new segment to the snake for every target hit.
def addLength(snake,win):
    snake.x=snake.getX()
    snake.y=snake.getY()
    segment=snake_segment[0]
    newsegment=snake_segment[-1].clone()
    xdirection = snake.segment_directionx[-1]
    ydirection = snake.segment_directiony[-1]
    displacementx = xdirection * -1
    displacementy = ydirection * -1
    newsegment.move(displacementx, displacementy)
    snake_segment.append(newsegment)
    snake.segment_directionx.append(snake.segment_directionx[-1])
    snake.segment_directiony.append(snake.segment_directiony[-1])
    snake.segment_directionx_storage.append(0)
    snake.segment_directiony_storage.append(0)




def checkDeath(win,snake):
    x=snake.getX()
    y=snake.getY()
    if x<35 or x>765 or y<35 or y>765:
        endGame(win,snake)
        return True
        #this if statement determines if the snake runs out of the defined boundaries.
    for i in range(1, len(snake_segment)):
        if (snake_segment[0].getCenter().getX() == snake_segment[i].getCenter().getX()):
            if (snake_segment[0].getCenter().getY() == snake_segment[i].getCenter().getY()):
                endGame(win,snake)
                return True
                #this part of the checkDeath function determines if the snake hit itself which we defined as a death
    else:
        return False


#checkWin checks if the snake runs over the target and returns True.
def checkWin(snake,target,win):
    scenterx=snake.getX()
    scentery=snake.getY()
    tcenterx=target.getX()
    tcentery=target.getY()
    if scenterx==tcenterx and tcentery==scentery:
        addLength(snake, win)
        target.erase(win)
        return True
    else:
        return False


#Target class is randomly drawn in the window
class Target():
    def __init__(self):
        self.x=(randrange(2,38)*20)
        self.y=(randrange(2,38)*20)
    def drawTarget(self,win):
        target=Rectangle(Point(self.x+10,self.y+10), Point(self.x-10,self.y-10))
        target.setFill('green')
        target.draw(win)
    def getX(self):
        return (self.x)
    def getY(self):
        return (self.y)
    def erase(self, win):
        target=Rectangle(Point(self.x+10,self.y+10), Point(self.x-10,self.y-10))
        target.setFill('black')
        target.draw(win)
        #end of class Target()

#this draws the window of the already set background
def drawBoard(win):
    rectangle=Rectangle(Point(775,775), Point(25,25))
    rectangle.setFill("black")
    rectangle.draw(win)

#this function is run once checkDeath() == True. The user can then choose to quit or continue playing through the python shell.
def endGame(win,snake):
    text=Text(Point(400,200), "You lost!")
    text.setTextColor('yellow')
    text.draw(win)
    again=input('Do you want to play again? Type yes to play again  ')
    if again.lower()== 'yes':
        snake_segment[:]=[]
        win.close()
        main()
    else:
        win.close()

#waits for user input to start the game
def startGame(win):
    text=Text(Point(400,400),'Welcome to Snake! Press any key to start the game!')
    text.setTextColor('yellow')
    text.draw(win)
    key=win.getKey()
    text.undraw()
    return key

#the function sets up the target and actually runs the game.
def restart(win,snake):
    target=Target()
    target.drawTarget(win)
    while win.isOpen() and checkDeath(win,snake)==False and checkWin(snake,target,win)==False:
        key = win.checkKey()
        if (key != ""):
            snake.direction = key
        checkWin(snake,target,win)
        snake.moveSnake(key,win)
        checkDeath(win,snake)
        time.sleep(.1)


def main():
    win=GraphWin('Snake', 800, 800)
    win.setBackground("gray")
    drawBoard(win)
    startGame(win)
    snake=Snake()
    snake.drawSnake(win)
    x = 0
    while x==0:
        restart(win,snake)
    win.getMouse()


main()
