image = [list("....######......."),
         list("....#....#......."),
         list("....#..#####....."),
         list("....####...#....."),
         list(".......#...####.."),
         list(".......#......#.."),
         list(".......########.."),
         list(".................")]

def print_image():
    for line in image:
        print("".join(line))

def floodfill(row, col, c):
    if row < 0 or row > len(image) - 1 or col < 0 or col > len(image[0]) - 1:
        return
    if image[row][col] != '.':
        return
    image[row][col] = c
    floodfill(row-1, col, c)
    floodfill(row+1, col, c)
    floodfill(row, col-1, c)
    floodfill(row, col+1, c)


floodfill(5, 8, '*')
floodfill(5, 3, '$')
print_image()