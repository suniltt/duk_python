# show_args.py
import sys

print("Script name:", sys.argv[0])
print("Number of arguments:", len(sys.argv) - 1)

for i, arg in enumerate(sys.argv):
    print(f"argv[{i}] = {arg!r}")
