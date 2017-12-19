fout = open('measurement.in', 'w')
out = ['100']
import random

names = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' ')


def random_delta():
    return random.randint(0, 101)
for i in range(100):
    out.append('%d %s %s' % (i, random.choice(names), random_delta()))

fout.write('\n'.join(out))
