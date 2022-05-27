import random
from ipaddress import IPv4Network


class IPv4RandomNetwork(IPv4Network):
  def __init__(self):
    IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(0,32)), strict=False)
List = []
while len(List) < 50:
    List.append(IPv4RandomNetwork)














