def zm(n):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n[1] for _ in range(n[0])]
    for i in range(n[0] * n[1]):
        arr[x][y] = str (i % 10)
        nx, ny = x+dx, y+dy
        if 0 <= nx < n[0] and 0 <= ny < n[1] and not (arr[nx][ny]):
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            nx, ny = x+dx, y+dy
            if 0 <= nx < n[0] and 0 <= ny < n[1] and not (arr[nx][ny]):
                x, y = nx, ny
            else:
                dx, dy = -dy, dx
                x, y = x+dx, y+dy
    for x in list(zip(*arr)):
        print(*x)

zm(eval(input()))
