def main(shifts):
    shifts = [[int(x) - 1 for x in cow.split(' ')] for cow in shifts.split('\n')1:]
    ranges = [shifts[0]]
    for cow in shift[1:]:
        lo_place = 0
        shift_index = 0
        while cow[0]


if __name__ == '__main__':
    fin = open('lifeguards.in')
    main(fin.read())
    #fout = open('lifeguards.out', 'w')
    #fout.write(main(fin.read()))


def base(s):
    s = s.split('\n')
    num = int(s[0])
    s = [[int(x) - 1 for x in cow.split(' ')] for cow in s[1:]]

    time = [0 for _ in xrange(int(1e6))]
    for cow in s:
        for t in range(cow[0], cow[1]):
            time[t] += 1
    max_len = -1
    for cow in s:
        test = [1 if x > 0 else 0 for x in time]
        for t in range(cow[0], cow[1]):
            test[t] -= 1
        total = sum(test)
        if total > max_len:
            max_len = total
    print max_len
