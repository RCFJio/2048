
import random
import tkinter as tk







class game(tk.Frame):
    bg_color={
    '2': '#eee4da',
    '4': '#ede0c8',
    '8': '#edc850',
    '16': '#edc53f',
    '32': '#f67c5f',
    '64': '#f65e3b',
    '128': '#edcf72',
    '256': '#edcc61',
    '512': '#f2b179',
    '2048': '#edc22e'
    }
    
    color={
    '2': '#776e65',
    '4': '#f9f6f2',
    '8': '#f9f6f2',
    '16': '#f9f6f2',
    '32': '#f9f6f2',
    '64': '#f9f6f2',
    '128': '#f9f6f2',
    '256': '#f9f6f2',
    '512': '#776e65',
    '1024': '#f9f6f2',
    '2048': '#f9f6f2'
    }
         
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 game")
        self.maingrid=tk.Frame(self,bg="azure3",bd=3,width=600,height=600)
        self.maingrid.grid(pady=(100,0))
        self.makecells()
        self.gamestart()
        self.master.bind("<Left>",self.left)
        self.master.bind("<Right>",self.right)
        self.master.bind("<Up>",self.up)
        self.master.bind("<Down>",self.down)
    def makecells(self):
        self.cells=[]
        for i in range(4):
            row=[]
            for j in range(4):
                cell=tk.Frame(self.maingrid,bg="azure4",width=150,height=150)
                cell.grid(row=i,column=j,padx=5,pady=5)
                cellnum=tk.Label(self.maingrid,bg="azure4",font=("Ariel",20))
                cellnum.grid(row=i,column=j)
                celldata={"location":cell,"number":cellnum}
                row.append(celldata)
            self.cells.append(row)
        scoreframe=tk.Frame(self)
        scoreframe.place(relx=0.5,y=45,anchor='center')
        tk.Label(scoreframe,text="Score",font=("Ariel",20)).grid(row=0)
        self.slabel=tk.Label(scoreframe,text="0",font=("Ariel",20))
        self.slabel.grid(row=1)
    def gamestart(self):
        self.gmatrix=[[0]*4 for i in range(4)]
        r=random.randint(0,3)
        c=random.randint(0,3)
        self.gmatrix[r][c]=2
        self.cells[r][c]["location"].config(bg=game.bg_color["2"])
        self.cells[r][c]["number"].config(text="2",bg=game.bg_color["2"],fg=game.color["2"])
        while(self.gmatrix[r][c]!=0):
            r=random.randint(0,3)
            c=random.randint(0,3)
        self.gmatrix[r][c]=2
        self.cells[r][c]["location"].config(bg=game.bg_color["2"])
        self.cells[r][c]["number"].config(text="2",bg=game.bg_color["2"],fg=game.color["2"])
        self.score=0
    def stack(self):
        mat=[[0]*4 for i in range(4)]
        for i in range(4):
            position=0
            for j in range(4):
                if(self.gmatrix[i][j]!=0):
                    mat[i][position]=self.gmatrix[i][j]
                    position=position+1
        self.gmatrix=mat
    def comb(self):
        for i in range(4):
            for j in range(3):
                if(self.gmatrix[i][j]!=0 and self.gmatrix[i][j]==self.gmatrix[i][j+1]):
                    self.gmatrix[i][j]=self.gmatrix[i][j]*2
                    self.gmatrix[i][j+1]=0
                    self.score=self.score+self.gmatrix[i][j]
    def rev(self):
        mat=[]
        for i in range(4):
            mat.append([])
            for j in range(4):
                mat[i].append(self.gmatrix[i][3-j])
        self.gmatrix=mat
    def transpose(self):
        mat=[[0]*4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                mat[i][j]=self.gmatrix[j][i]
        self.gmatrix=mat
    def addcell(self):
        r=random.randint(0,3)
        c=random.randint(0,3)
        if(any(0 in row for row in self.gmatrix)):
            while(self.gmatrix[r][c]!=0):
                r=random.randint(0,3)
                c=random.randint(0,3)
            self.gmatrix[r][c]=random.choice([2,4])
        
    def updt(self):
        for i in range(4):
            for j in range(4):
                val=self.gmatrix[i][j]
                if(val==0):
                    self.cells[i][j]["location"].config(bg="azure4")
                    self.cells[i][j]["number"].config(text='',bg="azure4")
                else:
                    self.cells[i][j]["location"].config(bg=game.bg_color[str(val)])
                    self.cells[i][j]["number"].config(text=str(val),bg=game.bg_color[str(val)],fg=game.color[str(val)])
        self.slabel.configure(text=str(self.score))
        self.update_idletasks()
    
    def left(self,event):
        self.stack()
        self.comb()
        self.stack()
        self.addcell()
        self.updt()
        self.gover()
    
    def right(self,event):
        self.rev()
        self.stack()
        self.comb()
        self.stack()
        self.rev()
        self.addcell()
        self.updt()
        self.gover()
    
    def up(self,event):
        self.transpose()
        self.stack()
        self.comb()
        self.stack()
        self.transpose()
        self.addcell()
        self.updt()
        self.gover()

    def down(self,event):
        self.transpose()
        self.rev()
        self.stack()
        self.comb()
        self.stack()
        self.rev()
        self.transpose()
        self.addcell()
        self.updt()
        self.gover()
    
    def horizontal(self):
        for i in range(4):
            for j in range(3):
                if(self.gmatrix[i][j]==self.gmatrix[i][j+1]):
                    return True
        return False
    def vertical(self):
        for i in range(3):
            for j in range(4):
                if(self.gmatrix[i][j]==self.gmatrix[i+1][j]):
                    return True
        return False


    def gover(self):
        if(any(2048 in row for row in self.gmatrix)):
            goframe=tk.Frame(self.maingrid,borderwidth=2)
            goframe.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(goframe,text="you win").pack()
            
        elif(not any(0 in row for row in self.gmatrix) and not self.horizontal() and not self.vertical()):
            goframe=tk.Frame(self.maingrid,borderwidth=2)
            goframe.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(goframe,text="you loose").pack()

game().mainloop()




