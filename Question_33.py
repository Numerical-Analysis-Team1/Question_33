def createMatrix(matrix, size, val):
    if val == 0:
        matrix = [[0 for i in range(size)] for j in range(size)]
    elif val == 1:
        matrix = [[int(i == j) for i in range(size)] for j in range(size)]
    return matrix


def calcDet(matrix):
    size = len(matrix)
    det = 0
    if size == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    minor = createMatrix(matrix, size - 1, 0)
    for k in range(len(matrix)):
        i, j = 0, 0
        while i < size:
            if i != k:
                minor[j] = matrix[i][1:]
                j += 1
            i += 1
        det += matrix[k][0] * ((-1) ** k) * calcDet(minor)
    return det


def invertMatrix(matrix):
    determinant = calcDet(matrix)
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant], matrix[0][0] / determinant]

    inverse = []
    for i in range(len(matrix)):
        inverseRow = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            inverseRow.append(((-1) ** (i + j)) * calcDet(minor))
        inverse.append(inverseRow)
    inverse = list(map(list, zip(*inverse)))
    for i in range(len(inverse)):
        for j in range(len(inverse)):
            inverse[i][j] = inverse[i][j] / determinant
    return inverse


def Mul_matrix(a, b):
    temp = [0 for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            temp[i] += a[i][j] * b[j]
    return temp


def Polynomial_Method(tab, xf):
    result, b = 0, [tab[i][1] for i in range(len(tab))]
    poly = Mul_matrix(invertMatrix(Polynomial_creation(tab)), b)
    for i in range(len(poly)):
        result += poly[i] * (xf ** i)
    return result


def Polynomial_creation(tab):
    for i in range(len(tab)):
        tab[i].insert(0, 1)
    return [[tab[i][1] ** j for j in range(len(tab))] for i in range(len(tab))]


def Nevil_Method(tab, xf):
    def Nevil_P(m, n):
        if m == n:
            return tab[m][1]
        else:
            Px = ((xf - tab[m][0]) * Nevil_P(m + 1, n) - (xf - tab[n][0]) * Nevil_P(m, n - 1)) / (
                    tab[n][0] - tab[m][0])
            return Px

    return Nevil_P(0, len(tab) - 1)


def driver(tab, xf):
    print("*****Nevil_Method*****")
    print("F({0}) = {1}".format(xf, Nevil_Method(tab, xf)))
    print("\n*****Polynomial Method*****")
    print("F({0}) = {1}".format(xf, Polynomial_Method(tab, xf)))


m_tab = [[0.35, -213.5991], [0.4, -204.4416], [0.55, -194.9375], [0.65, -185.0256], [0.7, -174.6711], [0.85, -163.8656],
         [0.9, -152.6271]]
point = 0.75

driver(m_tab, point)
