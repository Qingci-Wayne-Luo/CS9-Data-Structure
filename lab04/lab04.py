#Lab04

from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    count = 1
    maze[startX][startY] = count
    s.push([startX, startY])
    goal = False

    while not goal:

        #go North first
        if maze[startX-1][startY] == ' ':
            count += 1
            startX -= 1
            startY = startY
            s.push([startX, startY])
            maze[startX][startY]=count

        #go West then
        elif maze[startX][startY-1] == ' ':
            count += 1
            startX = startX
            startY -= 1
            s.push([startX, startY])
            maze[startX][startY]=count

        #go South then
        elif maze[startX+1][startY] == ' ':
            count += 1
            startX += 1
            startY = startY
            s.push([startX, startY])
            maze[startX][startY]=count

        #go East last
        elif maze[startX][startY+1] == ' ':
            count += 1
            startX = startX
            startY += 1
            s.push([startX, startY])
            maze[startX][startY]=count

        #test if there is no way out
        elif maze[startX - 1][startY] == '+' \
                and maze[startX][startY - 1] == '+' \
                and maze[startX + 1][startY] == '+' \
                and maze[startX][startY + 1] == '+':
            return False

        elif maze[startX - 1][startY] == 'G' \
                or maze[startX][startY - 1] == 'G' \
                or maze[startX + 1][startY] == 'G' \
                or maze[startX][startY + 1] == 'G':
            goal = True

        else:
            if s.size()==0:
                return False
            else:
                #if this way is a deadend,
                #extract the number on the top of the stack
                startX = s.peek()[0]
                startY = s.peek()[1]
                s.pop()
        
    return goal
    


def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='',end='')
        print("|")
    return












        









    
