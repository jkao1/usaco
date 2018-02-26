def main(s):
    s = s.split('\n')
    trail_length, num_stops, rf, rb = [int(x) for x in s[0].split(' ')]

    stops = s[1:]
    for i in range(num_stops):
        x = stops[i].split(' ')
        stops[i] = [int(x[0]), int(x[1])]

    output = 0

    layover = 0

    for i in range(num_stops):
        stop = stops[i]
        if i == 0:
            meters_passed = stop[0]
        else:
            meters_passed = stop[0] - stops[i-1][0]
        time_dif = (rf - rb) * meters_passed - layover

        best_time = (0, 0)

        if i < num_stops - 1:
            next_stop = stops[i + 1]
            possible_times = []
            for t in range(time_dif + 1):
                dist_between = next_stop[0] - stop[0]
                possible_times.append([t, t*stop[1] + next_stop[1] * ((rf - rb) * dist_between + time_dif - t)])

            for time in possible_times:
                if time[1] > best_time[1]:
                    best_time = time

            output += stop[1] * best_time[0] + next_stop[1] * (time_dif - best_time[0])

            layover = time_dif - best_time[0]
        else:
            if time_dif < layover:
                output += stop[1] * layover
            else:
                output += stop[1] * (time_dif - layover)

    return str(output)

if __name__ == '__main__':
    fin = open('reststops.in', 'r')
    fout = open('reststops.out', 'w')
    fout.write(main(fin.read()))