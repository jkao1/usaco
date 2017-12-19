def place_cows(s):
    s = s.split('\n')
    num = int(s[0])
    cows = ['' for _ in range(num)]
    temp_places = [int(x) - 1 for x in s[1].split(' ')]
    places = temp_places[:]
    for n in range(num):
        places[temp_places[n]] = n
    cow_ids = s[2].split(' ')

    for _ in range(3):
        new_cow_ids = cow_ids[:]
        for i in range(num):
            new_cow_ids[places[i]] = cow_ids[i]
        cow_ids = new_cow_ids[:]
    return '\n'.join(cow_ids)

if __name__ == '__main__':
    fin = open('shuffle.in', 'r')
    fout = open('shuffle.out', 'w')
    fout.write(place_cows(fin.read()))
