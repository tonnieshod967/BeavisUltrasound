import sys
import struct

if len(sys.argv) != 3:
    print ("Usage: %s infile outfile" % sys.argv[0])
    quit()
inf = open(sys.argv[1], 'rb')
ind = inf.read()
inf.close()

of = open(sys.argv[2], 'wb')
for i in range(int(len(ind) / 2)):
    b = (ind[i*2] << 8) | ind[i*2+1]
    bo = 0
    for j in range(16):
        bo |= ((b >> j) & 1) << (15 - j)
    of.write(struct.pack('<BB', bo >> 8, bo & 0xff))
of.close()



