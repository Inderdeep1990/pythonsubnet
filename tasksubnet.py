
import math
class Network:
    
	def __init__(self, ip_addresss, binary):
        self.net_addr = []
        self.copy_addr = []
        self.binary = binary
        ip_addresss = ip_addresss.split(".")
        ad = "1"*binary + "0"*(32-binary)
        octet = [ad[0:8], ad[8:16], ad[16:24], ad[24:32]]
 
        for p in range(len(ip_addresss)):
            a = int(ip_addresss[p])
            b = int(octet[p], 2)
            self.net_addr.append(a&b)
        print ("Network Address:", self.net_addr)
 
    def subnet(self, count):
        d = int(math.log(count, 2))
        target = self.binary + d
         
        ad = "1"*target + "0"*(32-target)
        octet = [ad[0:8], ad[8:16], ad[16:24], ad[24:32]
        move = math.ceil( target / 8.0 )
        host = (move*8) - target
        jump = 2**hoste
        self.copy_addr = copy.deepcopy(self.net_addr)
        for i in range(count):
            

