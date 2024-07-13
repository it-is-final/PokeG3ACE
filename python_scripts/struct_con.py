# Convert Thumb Hexcode for CodeGenerator

from more_itertools import peekable
from itertools import cycle
import struct

# Test Input below

test_data = [0xb5ec, 0xc8ee, 0xa700, 0xc0c0, 0xd2ff, 0xd200, 0xbdec, 0xe000, 0x4679, 0x4800, 0x1a09, 0xa000,
                 0x51ff, 0xb000, 0x0100, 0x4770, 0xB000, 0xB000, 0xB000, 0xB000, 0xB000, 0xB000, 0xB000]

def get_codegen_input(hexcode):
    gen_output = ''
    hexcode_peek = peekable(hexcode)
    tex_term_pattern = (0x0, 0x0, 0xFF, 0x0, 0xFF00, 0x0, 0xFF0000, 0x0, 0xFF000000)
    for command, pattern in zip(hexcode_peek, cycle(tex_term_pattern)):
        match pattern:
            case 0x0:
                commands_int = command | ((next(hexcode_peek, 0)) << 0x10)
            case 0xFF:
                commands_int = ((command << 0x10) | 0xFF if (command & 0xFF != 0xFF)
                                else command | (next(hexcode_peek, 0) << 0x10))
            case 0xFF00:
                commands_int = (((command << 0x10) | 0xFF00) if (command & 0xFF00 != 0xFF00)
                                else command | (next(hexcode_peek, 0) << 0x10))
            case 0xFF0000:
                commands_int = ((command | 0xFF0000) if (hexcode_peek.peek(0) & 0xFF != 0xFF)
                                else command | (next(hexcode_peek, 0) << 0x10))
            case 0xFF000000:
                commands_int = ((command | 0xFF000000) if (hexcode_peek.peek(0) & 0xFF00 != 0xFF00)
                                else command | (next(hexcode_peek, 0) << 0x10))
        gen_output += f'{hex(commands_int)}'
        gen_output += '\n' if hexcode_peek.peek(None) is not None else ''
    return gen_output

def get_user_hexcode():
    hexcode = []
    print("Enter hexcode (Press Enter then ^D on Linux/Unix systems or Ctrl-Z on Windows systems)")
    while True:
        try:
            line = int(input(), 16) & 0xFFFF
        except ValueError as err:
            print(f"{err.args} is not hexcode, ignoring this line...")
        except EOFError:
            break
        else:
            hexcode.append(line)
    return hexcode


def get_hexcode_endianness():
    while True:
        try:
            endianness = input("Endianness of hexcode (default is \"big\"): ").strip() or "big"
            match endianness.lower():
                case "big":
                    return False
                case "little":
                    return True
                case _:
                    raise ValueError(endianness)
        except ValueError as err:
            print(f"{err.args} is not a valid input")

def get_array_from_instruction(raw_instruction, little_endian):
    format_param = '<H' if little_endian else '>H'
    # format_param += 'I' if _word else 'H'
    result = int.from_bytes(struct.pack(format_param, raw_instruction))
    return result

user_hexcode_input = test_data
little_endian = get_hexcode_endianness()
for i in user_hexcode_input:
    print(get_array_from_instruction(i, little_endian))

# print(get_codegen_input(user_hexcode))
