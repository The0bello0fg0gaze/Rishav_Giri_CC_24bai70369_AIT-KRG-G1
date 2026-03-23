class horse():
    def __init__(self):
        self.board = [[0]*n for x in range(n)]
        self.out = [[0]*n for x in range(n)]
        self.found = False
        self.moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
 
    def nxt(self, h=0, pos=[0,0]):
        if h == n*n:
            self.out = [x[:] for x in self.board]
            return 0
        if not self.found:
            for i, j in self.moves:
                x, y = pos
                x += i
                y += j
                if x < n and y < n and x >= 0 and y >= 0 and self.board[x][y] == 0:
                    self.board[x][y] = h
                    self.nxt( h+1, [x,y])
                    self.board[x][y] = 0

n = 4
h = horse()
h.nxt(0,[0,0])
print(h.out)
