e = int(input(""))
for i in range(e):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = sum(a)
    if s >= a and (s-a)%x == 0:
        print("YES ",end="")
    else:
        print("NO ",end="")
