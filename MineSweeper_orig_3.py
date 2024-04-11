import random
def chooseSize():
    '''This function takes an input from user, 1 for Easy having 9x9 grids,
    2 for Medium having 16x16 grids and 3 for Expert where there will be 16x30 grids.

    If the User enters other than these three chices the function is called again
    showing message wrong input, try again and the function is called again

    This function returns a list of three integers where first one is height of the
    game and second one is the width of the game and the third is number of mines.'''
    try:
        mapSize=int(input('Enter your choice.\n1 for Easy(9x9).\n2 for Medium(16x16)\n3 for Expert(30x16).\n').strip())
        if mapSize==1:
            return([9,9,10])
        elif mapSize==2:
            return([16,16,40])
        elif mapSize==3:
            return(16,30,99)
        else:
            print('Invalid Size, Try again...')
            return(chooseSize())
    except ValueError:
        print('Invalid Size, Try again...')
        return(chooseSize())        

def getMap(mapcop):
    '''This function takes the board(mapcop) and prints the map in matrix form'''
    temp=['# |']
    temp.extend([i for i in range(w)])
    temp.append('| #')
    for i in temp:
        if temp.index(i)==0:
            print(i,end=' ')
        elif i==temp[-2]:
            print(i,end=' ')
        elif temp.index(i)<10:
            print(i,end='  ')
        else:
            print(i,end=' ')
    print('')
    for j in range(w+1):
        if j==0:
            print('- + -', end='')
        elif j==w:
            print(' + -', end='')
        else:
            print('  -', end='')
    print(' ')    
    for i in range(h):
        if i<10:
            print(str(i)+' | '+'  '.join(mapcop[i])+' | '+str(i))
        else:
            print(str(i)+'| '+'  '.join(mapcop[i])+' | '+str(i))
    for j in range(w+1):
        if j==0:
            print('- + -', end='')
        elif j==w:
            print(' + -', end='')
        else:
            print('  -', end='')
    print(' ')    
    for i in temp:
        if temp.index(i)==0:
            print(i,end=' ')
        elif i==temp[-2]:
            print(i,end=' ')
        elif temp.index(i)<10:
            print(i,end='  ')
        else:
            print(i,end=' ')
    print('\n')

def setMines(mineMap,h,w,mines):
    '''In this function the mines will be set randomly on all over the board,
    x here represents mine'''
    while mines!=0:
        x=random.randrange(0,h)
        y=random.randrange(0,w)
        if mineMap[x][y]=='+':
            mineMap[x][y]=u'\U00000238'
            mines-=1
    return(mineMap)

def numbers(mineMap,h,w):
    '''This function sets the numbers on the board i.e, the number of mines
    surrounding the coordinate'''
    if mineMap[0][0]!=u'\U00000238':                ##For Extreme cases, i.e, the corners
        count=0
        if mineMap[0][1]==u'\U00000238':
            count+=1
        if mineMap[1][1]==u'\U00000238':
            count+=1
        if mineMap[1][0]==u'\U00000238':
            count+=1
        mineMap[0][0]=str(count)
    if mineMap[0][w-1]!=u'\U00000238':
        count=0
        if mineMap[0][w-2]==u'\U00000238':
            count+=1
        if mineMap[1][w-2]==u'\U00000238':
            count+=1
        if mineMap[1][w-1]==u'\U00000238':
            count+=1
        mineMap[0][w-1]=str(count)
    if mineMap[h-1][0]!=u'\U00000238':
        count=0
        if mineMap[h-2][0]==u'\U00000238':
            count+=1
        if mineMap[h-2][1]==u'\U00000238':
            count+=1
        if mineMap[h-1][1]==u'\U00000238':
            count+=1
        mineMap[h-1][0]=str(count)
    if mineMap[h-1][h-1]!=u'\U00000238':
        count=0
        if mineMap[h-1][w-2]==u'\U00000238':
            count+=1
        if mineMap[h-2][w-2]==u'\U00000238':
            count+=1
        if mineMap[h-2][w-1]==u'\U00000238':
            count+=1
        mineMap[h-1][w-1]=str(count)
    for i in range(1,h-1):                          ##Now for edge cases excluding the corners
        if mineMap[i][0]!=u'\U00000238':            #Leftmost Column
            count=0
            if mineMap[i-1][0]==u'\U00000238':
                count+=1
            if mineMap[i-1][1]==u'\U00000238':
                count+=1
            if mineMap[i][1]==u'\U00000238':
                count+=1
            if mineMap[i+1][1]==u'\U00000238':
                count+=1
            if mineMap[i+1][0]==u'\U00000238':
                count+=1
            mineMap[i][0]=str(count)
        if mineMap[i][w-1]!=u'\U00000238':          #Rightmost column
            count=0
            if mineMap[i-1][w-1]==u'\U00000238':
                count+=1
            if mineMap[i-1][w-2]==u'\U00000238':
                count+=1
            if mineMap[i][w-2]==u'\U00000238':
                count+=1
            if mineMap[i+1][w-2]==u'\U00000238':
                count+=1
            if mineMap[i+1][w-1]==u'\U00000238':
                count+=1
            mineMap[i][w-1]=str(count)
    for i in range(1,w-1):
        if mineMap[0][i]!=u'\U00000238':            #Top row
            count=0
            if mineMap[0][i-1]==u'\U00000238':
                count+=1
            if mineMap[1][i-1]==u'\U00000238':
                count+=1
            if mineMap[1][i]==u'\U00000238':
                count+=1
            if mineMap[1][i+1]==u'\U00000238':
                count+=1
            if mineMap[0][i+1]==u'\U00000238':
                count+=1
            mineMap[0][i]=str(count)
        if mineMap[h-1][i]!=u'\U00000238':          #Bottom row
            count=0
            if mineMap[h-1][i-1]==u'\U00000238':
                count+=1
            if mineMap[h-2][i-1]==u'\U00000238':
                count+=1
            if mineMap[h-2][i]==u'\U00000238':
                count+=1
            if mineMap[h-2][i+1]==u'\U00000238':
                count+=1
            if mineMap[h-1][i+1]==u'\U00000238':
                count+=1
            mineMap[h-1][i]=str(count)
    for i in range(1,h-1):                          ##Now for ones touching 8 boxes
        for j in range(1,w-1):
            if mineMap[i][j]!=u'\U00000238':
                count=0
                for k in range(j-1,j+2):
                    if mineMap[i-1][k]==u'\U00000238':
                        count+=1
                    if mineMap[i+1][k]==u'\U00000238':
                        count+=1
                    if mineMap[i][k]==u'\U00000238' and k!=j:
                        count+=1
                mineMap[i][j]=str(count)
    return(mineMap)

def main_logic(userMap,mineMap,trigger,h,w):
    '''This function is called when the user clicks on a zero mine coordinate.
    this function uncovers the coordinates surrounding the zero coordinate but
    not F and ? coordinates

    Also it creates a list called Trigger of all the coordinates with zero in them as to check
    each one of them  until the list is empty'''
    while len(trigger)!=0:
        x,y=trigger[0][0],trigger[0][1]                                                     ##All four corners i.e, the extreme cases
        if x==0 and y==0:                                                                   
            if userMap[0][1]=='.' and userMap[0][1]!='F' and userMap[0][1]!='?':
                userMap[0][1]=mineMap[0][1]
                if userMap[0][1]=='0':
                    trigger.append([0,1])
            if userMap[1][0]=='.' and userMap[1][0]!='F' and userMap[1][0]!='?':
                userMap[1][0]=mineMap[1][0]
                if userMap[1][0]=='0':
                    trigger.append([1,0])
            if userMap[1][1]=='.' and userMap[1][1]!='F' and userMap[1][1]!='?':
                userMap[1][1]=mineMap[1][1]
                if userMap[1][1]=='0':
                    trigger.append([1,1])
        elif x==0 and y==w-1:
            if userMap[0][w-2]=='.' and userMap[0][w-2]!='F' and userMap[0][w-2]!='?':
                userMap[0][w-2]=mineMap[0][w-2]
                if userMap[0][w-2]=='0':
                    trigger.append([0,w-2])
            if userMap[1][w-2]=='.' and userMap[1][w-2]!='F' and userMap[1][w-2]!='?':
                userMap[1][w-2]=mineMap[1][w-2]
                if userMap[1][w-2]=='0':
                    trigger.append([1,w-2])
            if userMap[1][w-1]=='.' and userMap[1][w-1]!='F' and userMap[1][w-1]!='?':
                userMap[1][w-1]=mineMap[1][w-1]
                if userMap[1][w-1]=='0':
                    trigger.append([1,w-1])
        elif x==h-1 and y==0:
            if userMap[h-2][0]=='.' and userMap[h-2][0]!='F' and userMap[h-2][0]!='?':
                userMap[h-2][0]=mineMap[h-2][0]
                if userMap[h-2][0]=='0':
                    trigger.append([h-2,0])
            if userMap[h-2][1]=='.' and userMap[h-2][1]!='F' and userMap[h-2][1]!='?':
                userMap[h-2][1]=mineMap[h-2][1]
                if userMap[h-2][1]=='0':
                    trigger.append([h-2,1])
            if userMap[h-1][1]=='.' and userMap[h-1][1]!='F' and userMap[h-1][1]!='?':
                userMap[h-1][1]=mineMap[h-1][1]
                if userMap[h-1][1]=='0':
                    trigger.append([h-1,1])
        elif x==h-1 and y==w-1:
            if userMap[h-2][w-1]=='.' and userMap[h-2][w-1]!='F' and userMap[h-2][w-1]!='?':
                userMap[h-2][w-1]=mineMap[h-2][w-1]
                if userMap[h-2][w-1]=='0':
                    trigger.append([h-2,w-1])
            if userMap[h-2][w-2]=='.' and userMap[h-2][w-2]!='F' and userMap[h-2][w-2]!='?':
                userMap[h-2][w-2]=mineMap[h-2][w-2]
                if userMap[h-2][w-2]=='0':
                    trigger.append([h-2,w-2])
            if userMap[h-1][w-2]=='.' and userMap[h-1][w-2]!='F' and userMap[h-1][w-2]!='?':
                userMap[h-1][w-2]=mineMap[h-1][w-2]
                if userMap[h-1][w-2]=='0':
                    trigger.append([h-1,w-2])
        elif y==0:                                                                                  ##All four edges without the corners
            i=x                                                                                     #Rightmost column
            if mineMap[i][0]=='0':
                if userMap[i-1][0]=='.' and userMap[i-1][0]!='F' and userMap[i-1][0]!='?':
                    userMap[i-1][0]=mineMap[i-1][0]
                    if userMap[i-1][0]=='0':
                        trigger.append([i-1,0])
                if userMap[i-1][1]=='.' and userMap[i-1][1]!='F' and userMap[i-1][1]!='?':
                    userMap[i-1][1]=mineMap[i-1][1]
                    if userMap[i-1][1]=='0':
                        trigger.append([i-1,1])
                if userMap[i][1]=='.' and userMap[i][1]!='F' and userMap[i][1]!='?':
                    userMap[i][1]=mineMap[i][1]
                    if userMap[i][1]=='0':
                        trigger.append([i,1])
                if userMap[i+1][1]=='.' and userMap[i+1][1]!='F' and userMap[i+1][1]!='?':
                    userMap[i+1][1]=mineMap[i+1][1]
                    if userMap[i+1][1]=='0':
                        trigger.append([i+1,1])
                if userMap[i+1][0]=='.' and userMap[i+1][0]!='F' and userMap[i+1][0]!='?':
                    userMap[i+1][0]=mineMap[i+1][0]
                    if userMap[i+1][0]=='0':
                        trigger.append([i+1,0])
        elif y==w-1:                                                                                #Leftmost column
            i=x
            if mineMap[i][w-1]=='0':
                if userMap[i-1][w-1]=='.' and userMap[i-1][w-1]!='F' and userMap[i-1][w-1]!='?':
                    userMap[i-1][w-1]=mineMap[i-1][w-1]
                    if userMap[i-1][w-1]=='0':
                        trigger.append([i-1,w-1])
                if userMap[i-1][w-2]=='.' and userMap[i-1][w-2]!='F' and userMap[i-1][w-2]!='?':
                    userMap[i-1][w-2]=mineMap[i-1][w-2]
                    if userMap[i-1][w-2]=='0':
                        trigger.append([i-1,w-2])
                if userMap[i][w-2]=='.' and userMap[i][w-2]!='F' and userMap[i][w-2]!='?':
                    userMap[i][w-2]=mineMap[i][w-2]
                    if userMap[i][w-2]=='0':
                        trigger.append([i,w-2])
                if userMap[i+1][w-2]=='.' and userMap[i+1][w-2]!='F' and userMap[i+1][w-2]!='?':
                    userMap[i+1][w-2]=mineMap[i+1][w-2]
                    if userMap[i+1][w-2]=='0':
                        trigger.append([i+1,w-2])
                if userMap[i+1][w-1]=='.' and userMap[i+1][w-1]!='F' and userMap[i+1][w-1]!='?':
                    userMap[i+1][w-1]=mineMap[i+1][w-1]
                    if userMap[i+1][w-1]=='0':
                        trigger.append([i+1,w-1])
        elif x==0:                                                                                          #Top row
            i=y
            if mineMap[0][i]=='0':
                if userMap[0][i-1]=='.' and userMap[0][i-1]!='F' and userMap[0][i-1]!='?':
                    userMap[0][i-1]=mineMap[0][i-1]
                    if userMap[0][i-1]=='0':
                        trigger.append([0,i-1])
                if userMap[1][i-1]=='.' and userMap[1][i-1]!='F' and userMap[1][i-1]!='?':
                    userMap[1][i-1]=mineMap[1][i-1]
                    if userMap[1][i-1]=='0':
                        trigger.append([1,i-1])
                if userMap[1][i]=='.' and userMap[1][i]!='F' and userMap[1][i]!='?':
                    userMap[1][i]=mineMap[1][i]
                    if userMap[1][i]=='0':
                        trigger.append([1,i])
                if userMap[1][i+1]=='.' and userMap[1][i+1]!='F' and userMap[1][i+1]!='?':
                    userMap[1][i+1]=mineMap[1][i+1]
                    if userMap[1][i+1]=='0':
                        trigger.append([1,i+1])
                if userMap[0][i+1]=='.' and userMap[0][i+1]!='F' and userMap[0][i+1]!='?':
                    userMap[0][i+1]=mineMap[0][i+1]
                    if userMap[0][i+1]=='0':
                        trigger.append([0,i+1])
        elif x==h-1:                                                                                        #Bottom row
            i=y
            if mineMap[h-1][i]=='0':
                if userMap[h-1][i-1]=='.' and userMap[h-1][i-1]!='F' and userMap[h-1][i-1]!='?':
                    userMap[h-1][i-1]=mineMap[h-1][i-1]
                    if userMap[h-1][i-1]=='0':
                        trigger.append([h-1,i-1])
                if userMap[h-2][i-1]=='.' and userMap[h-2][i-1]!='F' and userMap[h-2][i-1]!='?':
                    userMap[h-2][i-1]=mineMap[h-2][i-1]
                    if userMap[h-2][i-1]=='0':
                        trigger.append([h-2,i-1])
                if userMap[h-2][i]=='.' and userMap[h-2][i]!='F' and userMap[h-2][i]!='?':
                    userMap[h-2][i]=mineMap[h-2][i]
                    if userMap[h-2][i]=='0':
                        trigger.append([h-2,i])
                if userMap[h-2][i+1]=='.' and userMap[h-2][i+1]!='F' and userMap[h-2][i+1]!='?':
                    userMap[h-2][i+1]=mineMap[h-2][i+1]
                    if userMap[h-2][i+1]=='0':
                        trigger.append([h-2,i+1])
                if userMap[h-1][i+1]=='.' and userMap[h-1][i+1]!='F' and userMap[h-1][i+1]!='?':
                    userMap[h-1][i+1]=mineMap[h-1][i+1]
                    if userMap[h-1][i+1]=='0':
                        trigger.append([h-1,i+1])
        else:                                                                                               ##Rest of the cases i.e, having 8 adjacent  Coordinates
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if userMap[i][j]=='.' and userMap[i][j]!='F' and userMap[i][j]!='?':
                        if i!=x or j!=y:
                            userMap[i][j]=mineMap[i][j]
                            if userMap[i][j]=='0':
                                trigger.append([i,j])
        trigger.pop(0)        
    return(userMap)

def uncover(x,y,choice,mineMap,userMap,h,w):
    '''This function returns responses codes, In this function
    the user can whether put or remove flags or ? on the coordinates
    or click on the coordiante to unveil it'''
    try:
        trigger=[]
        if choice=='f':
            if userMap[x][y]!='.' and userMap[x][y]!='F' and userMap[x][y]!='?':
                return (1)
            elif userMap[x][y]=='F':
                userMap[x][y]='.'
                return('FR')
            userMap[x][y]='F'
            return('FS')
        elif choice=='?':
            if userMap[x][y]!='.' and userMap[x][y]!='?' and userMap[x][y]!='F':
                return (1)
            elif userMap[x][y]=='F':
                userMap[x][y]='?'
                return('FR?S')
            elif userMap[x][y]=='?':
                userMap[x][y]='.'
                return('?R')
            userMap[x][y]='?'
            return('?S')
        elif choice=='c':
            if userMap[x][y]!='.':
                if userMap[x][y]=='F':
                    return('remF')
                elif userMap[x][y]=='?':
                    return('rem?')
                return (1)
            elif mineMap[x][y]==u'\U00000238':
                userMap[x][y]=u'\U00000238'
                return(2)
            else:
                userMap[x][y]=mineMap[x][y]
                if userMap[x][y]=='0':
                    trigger.append([x,y])
                    userMap=main_logic(userMap,mineMap,trigger,h,w)
                return(3)
    except IndexError:
        return(4)
    
def enterGame(mineMap,userMap,mines,h,w):
    '''It is the function where the choices are made and the coordinate
    on which the choosen operation would be performed and gives acknowledgement
    to the user about what happened'''
    #this is the position to display the map once in a game by using "getMap(mineMap)"
    print('Lets Begin')
    flag=mines
    while (True):
        print('Flags left :'+str(flag))
        getMap(userMap)
        choice=input('Enter f to put or remove flag, ? for Uncertain Flag or c to click : ')
        if choice.isupper():
            choice=choice.lower()
        if choice!='f' and choice!='?' and choice!='c':
            print('Wrong Entry, Please select again')
            continue
        try:
            x,y=input('Enter the postion on which you want to click, give coordinates : ').strip().split()
            x,y=int(x),int(y)
        except ValueError:
            print('Enter again. A number then space then number')
            continue
        x,y=int(x),int(y)
        res_code=uncover(x,y,choice,mineMap,userMap,h,w)
        print('---------------------------------------------------------------------------')
        if res_code==1:
            print('Already Uncovered')
        elif res_code==2:
            getMap(userMap)
            print('Mine was set off, Game Over!, Better Luck next time')
            break
        elif res_code==3:
            print('Nice choice')
        elif res_code==4:
            print('Index out of range, 0<=row<={0:d} and 0<=column<={1:d}, Try again within limits'.format(h-1,w-1))
        elif res_code=='FS':
            print('Flag Set')
            flag-=1
        elif res_code=='FR':
            print('Flag Removed')
            flag+=1
        elif res_code=='FR?S':
            print('Flag removed, ? set')
            flag+=1
        elif res_code=='?S':
            print('? Set')
        elif res_code=='?R':
            print('? Removed')
        elif res_code=='remF':
            print('Already a flag here, remove it then try again')
        elif res_code=='rem?':
            print('Already a ? here, remove it then try Removed')
        count=0
        for i in userMap:
            for j in i:
                if j!='.' and j!='F' and j!='?':
                    count+=1
        if count>=(h*w)-mines:
            getMap(mineMap)
            print('========================You Won========================')
            break
'''This is the main body where the user starts a game and after
one completion chooses whether to play again or quit'''
while True:
    mapSize=chooseSize()                                    #This line calls the function chooseSize in which user will choose to play in one of three difficulties
    h,w,mines=mapSize[0],mapSize[1],mapSize[2]
    mineMap=[['+' for x in range(w)] for y in range(h)]     #Initializing the minefield with all zeros.
    mineMap=setMines(mineMap,h,w,mines)                     #Set mines randomly on the board
    mineMap=numbers(mineMap,h,w)                            #Get the number on the board
    userMap=[['.' for x in range(w)] for y in range(h)]
    enterGame(mineMap,userMap,mines,h,w)                    #Start the game
    new_game=input('Enter p to play again or any other key to exit: ')
    if new_game.isupper():
        new_game=new_game.lower()
    if new_game=='p':
        continue
    print('========================Goodbye========================')
    break
