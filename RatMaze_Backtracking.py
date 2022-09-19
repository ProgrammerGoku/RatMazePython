n=4
def isValid(init_mat,x,y):
  if(0<=x<=n-1 and 0<=y<=n-1):
    if(init_mat[x][y]==0):
      return False
    else:
      return True
  return False

def RatMaze(init_mat,x,y,sol):
  if(x==n-1 and y==n-1):
    sol[x][y]=1
    return sol
  if(isValid(init_mat,x,y)):
    sol[x][y]=1
    if(RatMaze(init_mat,x+1,y,sol)):
      return True
    if(RatMaze(init_mat,x,y+1,sol)):
      return True
    sol[x][y]=0
    return False
    
  




sol=[[0 for i in range(4)] for i in range(4)]
sol[0][0]=1
maze=[[1,0,0,0],
      [1,1,0,1],
      [0,1,0,0],
      [1,1,1,1]]

a=RatMaze(maze,0,0,sol)


