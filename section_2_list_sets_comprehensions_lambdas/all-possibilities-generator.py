def list_comprehensions(x, y, z, n):
    saida = []
    [[[saida.append([elemento_x, elemento_y, elemento_z]) for elemento_z in range(z+1) if elemento_x + elemento_y + elemento_z != n] for elemento_y in range(y+1)] for elemento_x in range(x+1)]
    print(saida)


if __name__ == '__main__':
    list_comprehensions(1, 1, 1, 2)

"""
given three integers x,y and z representing the dimensions of a cuboid along with an integer .
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where
the sum of i, j, k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z .
"""