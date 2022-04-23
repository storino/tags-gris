#!usr/bin/env python3.8

from pwn import *
p = remote("35.184.230.50",3000)
p.sendline("esoj_12312312")
print(p.recvline())
