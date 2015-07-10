import socket


def main():
    """Scan the network for connected machines"""
    print "Starting scan"
    addr_range = "192.168.1.%d"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.settimeout(2.0)
    counter = 1
    for i in range(1, 254):
        try:
            ip = addr_range % i
            r = socket.gethostbyaddr(ip)
            print "%s: %s - %s" % (counter, r[2][0], r[0])
            counter += 1
        except socket.herror:
            pass

if __name__ == "__main__":
    main()
