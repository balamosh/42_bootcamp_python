import sys

# Check args
if len(sys.argv) < 2:
    sys.exit()
elif len(sys.argv) != 2:
    sys.exit("ERROR")

# Read 1st argument
str_in = sys.argv[1]

# Try converting to int
try:
    n = int(str_in)
except ValueError:
    sys.exit("ERROR")

# Print
if n == 0:
    print("I'm Zero.")
elif n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
