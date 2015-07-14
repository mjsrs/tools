import argparse

crc_table = [
    0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7,
    0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef
    ]


def calculateCrc(data, len):
    i = 0
    crc = 0
    for j in range(len):
        i = (crc >> 12) ^ (data[j] >> 4)
        crc = crc_table[i & 0x0F] ^ (crc << 4)
        i = (crc >> 12) ^ (data[j] >> 0)
        crc = crc_table[i & 0x0F] ^ (crc << 4)
    return (crc & 0xFFFF)


def auto_int(x):
    return int(x, 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate CRC")
    parser.add_argument('bytes', metavar='bytes', type=auto_int, nargs='+', help='bytes to calculate crc')
    args = parser.parse_args()
    output = calculateCrc(args.bytes, len(args.bytes))
    print "CRC: %s" % hex(output)
