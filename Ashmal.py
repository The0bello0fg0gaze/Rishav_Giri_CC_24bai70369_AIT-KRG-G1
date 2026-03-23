import sys
import time
def Ashmal(words):
    out = words[0]
    for x in words[1:]:
        if out != x:
            if out > x:
                out = x + out 
            else:
                out += x
        else:
            out += x
    return out
n = int(input())
for x in range(n):
    l = int(sys.stdin.readline())
    words = sys.stdin.readline().split()
    out = Ashmal(words)
    print(out)
