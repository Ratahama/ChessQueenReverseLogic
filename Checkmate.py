directions = {
    "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),
    "up-left": (-1, -1), "up-right": (-1, 1), "down-right": (1, 1), "down-left": (1, -1)
}
matrix = []
kingordinates = []
for i in range(8):
    row = input().split()
    matrix.append(row)
    if 'K' in row:
        column = row.index('K')
        kingordinates = [i, column]

queenordinates = []
for dir in directions.values():
    r = kingordinates[0] + dir[0]
    c = kingordinates[1] + dir[1]
    while 0 <= r < 8 and 0 <= c < 8:
        if matrix[r][c] == '.':
            r = r + dir[0]
            c = c + dir[1]
            continue
        elif matrix[r][c] == 'Q':
            queenordinates.append([r, c])
            break

if len(queenordinates) == 0:
    print("The king is safe!")

# [print(*x) for x in matrix]
[print(q) for q in queenordinates]
