import sys
name = "jacob"
grade = "A+"

name_b = name.encode('UTF-8')
grade_b = grade.encode('UTF-8')

sys.stdout.buffer.write(name_b + b'\x00'*5 + grade_b)
