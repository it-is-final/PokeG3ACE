# # # # # # # # # # # # # # # # #
# Convert Numbers to Characters #
# # # # # # # # # # # # # # # # #

japanese_char_table = ("␣","あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ",
                 "た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま",
                 "み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん","ぁ",
                 "ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ",
                 "ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ",
                 "っ","ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ",
                 "タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ",
                 "ミ","ム","メ","モ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン","ァ",
                 "ィ","ゥ","ェ","ォ","ャ","ュ","ョ","ガ","ギ","グ","ゲ","ゴ","ザ","ジ","ズ","ゼ",
                 "ゾ","ダ","ヂ","ヅ","デ","ド","バ","ビ","ブ","ベ","ボ","パ","ピ","プ","ペ","ポ",
                 "ッ","0","1","2","3","4","5","6","7","8","9","！","？","。","ー","・",
                 "…","『","』","「","」","♂","♀","","","","／","A","B","C","D","E",
                 "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
                 "V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k",
                 "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","",
                 "","","","","","","","","","","","","","","","")

def get_characters(byte):
    byte = byte & 0xFF
    if byte >= 0xB7 and byte < 0xBA:
        byte_base = 0xB6
        byte_offset = byte - 0xB6
    elif byte >= 0xEF and byte < 0x100:
        byte_base = 0xEE
        byte_offset = byte - 0xEE
    else:
        byte_base = byte
        byte_offset = 0
    return (byte_base, byte_offset)

def get_bit_length():
    while True:
        try:
            bit_length = int(input("Bit length of number: "))
            if bit_length % 8:
                raise ValueError(bit_length)
        except ValueError as err:
            print(f"{err.args} is not a valid input")
        else:
            return bit_length

def get_hexcode_endianness():
    while True:
        try:
            endianness = input("Endianness of hexadecimal (default is \"big\"): ").strip() or "big"
            match endianness.lower():
                case "big":
                    return "big"
                case "little":
                    return "little"
                case _:
                    raise ValueError(endianness)
        except ValueError as err:
            print(f"{err.args} is not a valid input")

def get_hex_from_input():
    while True:
        try:
            input_value = int(input("Enter a hexadecimal number: "),16)
        except ValueError as err:
            print(f"{err.args} is not a valid input")
        else:
            return input_value

def convert_result_to_char(result, char_table, spaces):
    spacer = ' ' if spaces else ''
    char_string = spacer.join([char_table[i] for i in reversed(result)])
    return char_string

result_base = bytearray()
result_offset = bytearray()

number_length = get_bit_length()
number = get_hex_from_input()
endianness = get_hexcode_endianness()

raw_bytes = number.to_bytes(length=(number_length // 8),byteorder=endianness,signed=False)

for i in raw_bytes:
    result_base.extend(get_characters(i)[0].to_bytes(1,signed=False))
    result_offset.extend(get_characters(i)[1].to_bytes(1,signed=False))

char_base_1 = convert_result_to_char(result_base, japanese_char_table, spaces=True)
char_base_2 = convert_result_to_char(result_base, japanese_char_table, spaces=False)
char_offset_1 = convert_result_to_char(result_offset, japanese_char_table, spaces=True)
char_offset_2 = convert_result_to_char(result_offset, japanese_char_table, spaces=False)

code_gen_input_base = hex(int.from_bytes(result_base,'big',signed=False))
code_gen_input_offset = hex(int.from_bytes(result_offset,'big',signed=False))

raw_hex_base = ' '.join('{:02X}'.format(i) for i in reversed(result_base))
raw_hex_offset = ' '.join('{:02X}'.format(i) for i in reversed(result_offset))

print(f'''\
Base:\t\
{char_base_1}\t\
({char_base_1})
Offset:\t\
{char_offset_1}\t\
({char_offset_2})

CodeGenerator Input:
{code_gen_input_base}
{code_gen_input_offset}

Raw Hex:
{raw_hex_base}
{raw_hex_offset}\
''')
