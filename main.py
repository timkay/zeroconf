from zeroconf import ServiceBrowser, Zeroconf
import sys
import struct

class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        sys.stdout.write(' %s\t%d.%d.%d.%d\n' % (name, *struct.unpack('BBBB', info.address)))
        sys.stdout.flush()


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
