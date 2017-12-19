def inside_rect(coord, rect):
    x, y = coord
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    if x1 <= x < x2 and y1 <= y < y2:
        return True

def p_matrix(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in A[::-1]  ]))

def main(s):
    s = s.split('\n')
    bill1 = [int(x) for x in s[0].split(' ')]
    bill2 = [int(x) for x in s[1].split(' ')]
    truck = [int(x) for x in s[2].split(' ')]

    ans = ( bill1[2] - bill1[0] ) * ( bill1[3] - bill1[1]) + ( bill2[2] - bill2[0] ) * ( bill2[3] - bill2[1])
    lox = truck[0]
    loy = truck[1]
    width = truck[2] - lox
    height = truck[3] - loy
    mat = [[0 for _ in xrange(width)] for _ in xrange(height)]
    for y in xrange(height):
        for x in xrange(width):
            for b in [bill1, bill2]:
                if inside_rect([x + lox, y + loy], b):
                    ans -= 1
    p_matrix(mat)
    return(str(ans))
    """
    xs = [l[0] for l in [bill1, bill2, truck]] + [l[2] for l in [bill1, bill2, truck]]
    ys = [l[1] for l in [bill1, bill2, truck]] + [l[3] for l in [bill1, bill2, truck]]
    lox = min(xs)
    width = max(xs) - lox
    loy = min(ys)
    height = max(ys) - loy

    mat = [[0 for _ in xrange(width)] for _ in xrange(height)]
    for y in xrange(height):
        for x in xrange(width):
            for r in [bill1, bill2, truck]:
                if inside_rect([x + lox, loy + y], r):
                    if r == truck and mat[y][x] > 0:
                        ans -= 1
                    else:
                        mat[y][x] += 1
    p_matrix(mat)
    return str(ans)
    """
if __name__ == '__main__':
    fin = open('billboard.in', 'r')
    fout = open('billboard.out', 'w')
    fout.write(main(fin.read()))
