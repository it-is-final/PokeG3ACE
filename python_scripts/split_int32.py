# Convert Thumb Hexcode for CodeGenerator

# Test Input below

# hexcode_input = [0xb5ec, 0xc8ee, 0xa700, 0xc0c0, 0xd2ff, 0xd200, 0xbdec, 0xe000, 0x4679, 0x4800, 0x1a09, 0xa000, 
#                  0x51ff, 0xb000, 0x0100, 0x4770, 0xB000, 0xB000, 0xB000, 0xB000, 0xB000, 0xB000, 0xB000]

def split_int32(input_number):
    integer_high = input_number >> 0x10
    integer_low = input_number & 0xFFFF
    return (integer_low, integer_high)

def get_user_hexcode():
    hexcode = []
    print("Enter hexcode (Press Enter then ^D on Linux/Unix systems or Ctrl-Z on Windows systems)")
    while True:
        try:
            line = int(input(), 16) & 0xFFFFFFFF
        except ValueError as err:
            print(f"{err.args} is not hexcode, ignoring this line...")
        except EOFError:
            break
        else:
            hexcode.append(line)
    return hexcode

user_hexcode_input = get_user_hexcode()

instruction_array = []
for i in user_hexcode_input:
    instruction_array.extend(split_int32(i))

print('\n'.join([f'{i:04X}' for i in instruction_array]))
