import telnetlib
import time

"""
hostmgr list
flags
C - Connected
D - DHCP Lease
L - Lock the lease
"""

HOST = "192.168.1.254"
USER = "sumeo"
PASS = "bfd,10ng"


class meo:

    def __init__(self):
        self.host = HOST
        self.user = USER
        self._pass = PASS
        self.tn = None

    def connect(self):
        print "meo telnet client - connecting to %s with user %s" % (HOST, USER)
        self.tn = telnetlib.Telnet(self.host)
        self.tn.read_until("Username :")
        self.tn.write("%s\n\r" % self.user)
        self.tn.read_until("Password :")
        self.tn.write("%s\n\r" % self._pass)

    def disconnect(self):
        self.tn.write("exit\n\r")
        print "meo telnet client - exit"

    def getHostmgrList(self):
        print "running hostmgr list"
        print "-" * 80
        devices = []
        self.connect()
        # hostmgr list
        self.tn.write("hostmgr list\n\r")
        self.disconnect()
        data = self.tn.read_all()
        info_start = data.find("hostmgr list")
        rows = data[info_start+12:].splitlines()
        for row in rows[3:len(rows)-1]:
            _row = row.split()
            device = {'mac': _row[0], 'ip': _row[1], 'flags': _row[2], 'type': _row[3], 'intf': _row[4], 'hw': _row[5], 'hostname': _row[6]}
            devices.append(device)
        print "Devices Found: ", len(devices)
        print "-" * 80
        for device in devices:
            print device

    def getArpList(self):
        print "running ip arplist"
        print "-" * 80
        devices = []
        self.connect()
        # ip arplist
        self.tn.write("ip arplist\n\r")
        self.disconnect()
        data = self.tn.read_all()
        info_start = data.find("ip arplist")
        rows = data[info_start+10:].splitlines()
        for row in rows[2:len(rows)-1]:
            _row = row.split()
            device = {'intf': _row[1], 'ip': _row[2], 'hwaddr': _row[3], 'type': _row[4]}
            devices.append(device)
        for device in devices:
            print device
        return devices

    def deleteArpCache(self):
        print "deleting arp cache"
        print "-" * 80
        devices = self.getArpList()
        self.connect()
        for device in devices:
            print "deleting device %s" % device['ip']
            delete_cmd = "ip arpdelete intf=%s ip=%s hwaddr=%s \n\r" % (device['intf'], device['ip'], device['hwaddr'])
            print delete_cmd
            self.tn.write(delete_cmd)
        self.disconnect()


if __name__ == "__main__":
    tn = meo()
    tn.deleteArpCache()
    print "waiting for 20 seconds..."
    time.sleep(20)
    tn.getHostmgrList()
    tn.getArpList()
