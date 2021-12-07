# converts binary.txt (decimal representation) > hex .txt
# does not work with break files (for example, 8 characters per row)
# use 8bit_to_all_bits first if file contains separate rows
# for example: 01000110 outputs 4f

data1 = open('data.txt', 'r')
data2 = open("hex_" + data1.name, 'w')

# () specifies number of decimal characters used, remove number to run whole file
file = data1.read()

decimal_representation = int(file, base=2)
hexadecimal_string = hex(decimal_representation)

# removes first two characters (0x) of output and writes to file
data2.write(hexadecimal_string[2:])

data1.close()
data2.close()
