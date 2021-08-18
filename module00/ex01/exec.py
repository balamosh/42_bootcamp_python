import sys

str_in = ' '.join(sys.argv[1:])
str_out = str_in.swapcase()
str_out = str_out[::-1]
if str_out:
    print(str_out)
