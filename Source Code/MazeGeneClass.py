# -*- coding:utf-8 -*-
import random as rand
from matplotlib import cm
from matplotlib import pyplot as plt
class MazeGenerator:
    def __init__(self,width,height,method):
        ###method: 1 kruscal    2 DFS    3 BFS
        ##初始化迷宫 全部为墙
        self.width = width
        self.height = height
        if(width%2==0 or height%2==0):
           # print('width and height must be odd.')
            return
        if(width<2 or height<2):
            self.maze=[['%' for i in range (width)] for i in range(height)]
            self.WriteMaze()
            return
        ###边框总为墙
        self.maze=[['%' for i in range(self.width)] for i in range(self.height)]
        if(method==1):
            self.kruscal()
        if(method==2):
            self.DFS()
        if(method==3):
            self.BFS()
        if(method==4):
            self.Recursive_Division()
            ##随机得到起点、终点
        while (1):
            self.startW, self.startH = rand.randint(1, (self.width - 1) // 2), rand.randint(1,(self.height - 1) // 2)
            self.targetW, self.targetH = rand.randint(self.startW + (self.width - 2) // 2, self.width - 2),rand.randint(self.startH + (self.height - 2) // 2, self.height - 2)
            if (self.maze[self.startH][self.startW] == ' ' and self.maze[self.targetH][self.targetW] == ' '):
                break
        self.maze[self.startH][self.startW] = 'P'
        self.maze[self.targetH][self.targetW] = 'G'
        self.WriteMaze()

    def kruscal(self):
        ###kruscal算法生成随机迷宫
        ###生成初始的点集
        row,col=(self.height-1)//2,(self.width-1)//2    ##points
        self.set_parent=[]
        set_count=row*col
        self.set_deep=[[1 for i in range(col)] for i in range(row)]
        for i in range(0,row):
            temp_row=[(0,0)]*col    ##初始parentset
            self.set_parent.append(temp_row)
        for i in range(0,row):
            for j in range(0,col):
                self.set_parent[i][j]=(i,j)
                self.maze[2*i+1][2*j+1]=' '
        n1=(self.width-3)*(self.height-1)//4
        n2=(self.height-3)*(self.width-1)//4
        wall_count=n1+n2
        wall_lists=[(0,0)]*wall_count    ###wall lists
        r,c=1,2
        ##create wall lists
        for i in range(0,n1):
            wall_lists[i]=(r,c)
            if(c<self.width-3):
                c+=2
            else:
                r += 2
                c = 2
        r,c=2,1
        for i in range(n1,wall_count):
            wall_lists[i]=(r,c)
            if(r<self.height-3):
                r+=2
            else:
                c += 2
                r = 2

        while(set_count>1):
            #随机选一个墙
            wall_index=rand.randint(0,wall_count-1)
            wall_row,wall_col=wall_lists[wall_index]
            del wall_lists[wall_index]
            wall_count-=1

            ##判断墙的方向  node1,node2为墙所连接的两个顶点
            if(wall_col%2==0):  #横向
                node1row,node1col=wall_row,wall_col-1
                node2row,node2col=wall_row,wall_col+1
            else:   #竖向
                node1row,node1col=wall_row-1,wall_col
                node2row,node2col=wall_row+1,wall_col

            ##将顶点坐标转换为set中对应的坐标
            set_node1_row,set_node1_col=(node1row-1)//2,(node1col-1)//2
            set_node2_row,set_node2_col=(node2row-1)//2,(node2col-1)//2
            #判断两个顶点是否在一个集合里
            if(self.connected(set_node1_row,set_node1_col,set_node2_row,set_node2_col)):
                continue
            else:
                self.union(set_node1_row,set_node1_col,set_node2_row,set_node2_col)
                self.maze[wall_row][wall_col]=' '
                set_count-=1

    def connected(self,x1,y1,x2,y2):  ##查询是否连通（在同一个集合中）
        return self.findp(x1,y1)==self.findp(x2,y2)

    def findp(self,x,y):  ##查询根节点
        if(self.set_parent[x][y]==(x,y)):
            a,b=x,y
        else:
            parent_row, parent_col = self.set_parent[x][y]
            a,b=self.findp(parent_row,parent_col)
        return a,b

    def union(self,x1,y1,x2,y2):   ##集合合并
        p1x,p1y=self.findp(x1,y1)
        p2x,p2y=self.findp(x2,y2)
        if(p1x==p2x and p1y==p2y):
            return
        if(self.set_deep[p1x][p1y]>self.set_deep[p2x][p2y]):
            self.set_parent[p2x][p2y]=(p1x,p1y)
        if(self.set_deep[p1x][p1y]<self.set_deep[p2x][p2y]):
            self.set_parent[p1x][p1y]=(p2x,p2y)
        if (self.set_deep[p1x][p1y] == self.set_deep[p2x][p2y]):
            self.set_parent[p1x][p1y] = (p2x, p2y)
            self.set_deep[p2x][p2y]+=1
    def DFS(self):
        ###初始的随机顶点的横纵坐标均为偶数
        stack = []
        cell_now_col=rand.randint(0,(self.width-3)//2)*2+1
        cell_now_row = rand.randint(0, (self.height - 3) //2) * 2+1
        self.maze[cell_now_row][cell_now_col]=' '
        stack.append((cell_now_row,cell_now_col))  ##初始点入栈
        while(len(stack)!=0):   #栈非空
            headrow,headcol=stack.pop()  #栈顶
            direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for i in range(0,4):
                temp=rand.randint(0,3-i)
                cell_next_row,cell_next_col=headrow+2*direction[temp][0],headcol+2*direction[temp][1]
                if(0<cell_next_row<self.height-1 and 0<cell_next_col<self.width-1 and self.maze[cell_next_row][cell_next_col]=='%'):
                    self.maze[headrow+direction[temp][0]][headcol+direction[temp][1]]=' '   ##中间的边打通
                    self.maze[cell_next_row][cell_next_col]=' '
                    stack.append((cell_next_row,cell_next_col))   #入栈
                del direction[temp]
        return

    def BFS(self):
        ###初始的随机顶点的横纵坐标均为偶数
        cell_now_col = rand.randint(0, (self.width - 3) // 2) * 2 + 1
        cell_now_row = rand.randint(0, (self.height - 3) // 2) * 2 + 1
        ##为了增加随机性，使用两个队列
        queue1 = []  ##高层  （较高一层，从该层出队）
        queue2 = []  ##低层  （较低一层，从该层入队）
        self.maze[cell_now_row][cell_now_col] = ' '
        queue1.append((cell_now_row, cell_now_col))  ##初始点入列
        while(len(queue1)!=0):
            index=rand.randint(0,len(queue1)-1)   #同一层随机出队
            headrow,headcol=queue1[index]         #出队顶点
            del queue1[index]   #从队列中删除该顶点
            direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            temp=rand.randint(0,3)
            for i in range(0, 4):
                temp = rand.randint(0, 3 - i)
                cell_next_row, cell_next_col = headrow + 2 * direction[temp][0], headcol + 2 * direction[temp][1]
                if (0 < cell_next_row < self.height - 1 and 0 < cell_next_col < self.width - 1 and
                        self.maze[cell_next_row][cell_next_col] == '%'):
                    self.maze[headrow + direction[temp][0]][headcol + direction[temp][1]] = ' '  ##中间的边打通
                    self.maze[cell_next_row][cell_next_col] = ' '
                    queue2.append((cell_next_row, cell_next_col))  # 入队
                del direction[temp]
            if(len(queue1)==0):
                queue1=queue2.copy()
                queue2=[]

    def Recursive_Division(self):
        for i in range(1,self.height-1):
            for j in range(1,self.width-1):
                 self.maze[i][j]=' '
        self.RD(1,1,self.height-2,self.width-2)

    def RD(self,startrow,startcol,endrow,endcol):   ###大的空间的参数
        ##在奇数行、奇数列产生walls
        ##如果行或列为1，即不可再分割，退出
        if(endrow<startrow+1 or endcol<startcol+1):
            return
        randrow=rand.randint(0,(endrow-startrow)//2-1)*2+1+startrow   #两个新建的墙的交点
        randcol=rand.randint(0,(endcol-startcol)//2-1)*2+1+startcol
        for i in range(startrow,endrow+1):
            self.maze[i][randcol]='%'
        for i in range(startcol,endcol+1):
            self.maze[randrow][i]='%'
        direction=[1,2,3,4]  ##随机选择开口的三个墙  （上，下，左，右）
        randwall=rand.randint(1,4)  ##被选中的不开口
        for i in range(0,4):
            j=direction[i]
            if(j==randwall):
                continue
            if(j==1):  #上
                selected_row = startrow+rand.randint(0, (randrow - 1-startrow)//2)*2
                self.maze[selected_row][randcol]=' '
            if(j==2):  #下
                selected_row =endrow-2* rand.randint(0,(endrow-randrow - 1)//2)
                self.maze[selected_row][randcol]=' '
            if(j==3):  #左
                selected_col =startcol+2* rand.randint(0, (randcol - 1-startcol)//2)
                self.maze[randrow][selected_col]=' '
            if(j==4):  #右
                selected_col =endcol-2*rand.randint(0, (endcol-randcol -1)//2)
                self.maze[randrow][selected_col]=' '
        self.RD(startrow, startcol, randrow - 1, randcol - 1)
        self.RD(startrow, randcol + 1, randrow - 1, endcol)
        self.RD(randrow + 1, startcol, endrow, randcol - 1)
        self.RD(randrow + 1, randcol + 1, endrow, endcol)
    def WriteMaze(self):
        fo=open("maze.txt","w")
        fo.write("")
        fo.close()
        fo=open("maze.txt","a")
        for i in range(0,self.height):
            for j in range(0,self.width):
                fo.write(str(self.maze[i][j]))
            fo.write('\n')
        self.show()
    def show(self):
        image=[[0 for i in range (self.width)] for i in range(self.height)]
        for i in range(0,self.height):
            for j in range(0,self.width):
                if(self.maze[i][j]!='%'):
                    image[i][j]=255
                if(self.maze[i][j]=='G' or self.maze[i][j]=='P'):
                    image[i][j]=120
        plt.imshow(image,cmap=cm.Greys_r,interpolation='none')
        plt.show()


if __name__ == "__main__":
   test=MazeGenerator(77,77,2)



