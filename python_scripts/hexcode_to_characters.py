# # # # # # # # # # # # # # # # # #
# ARM/Thumb Hexcode to Characters #
# # # # # # # # # # # # # # # # # #

nowrite_chars_present = False
ff_term_present = False

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
                 "…","『","』","「","」","♂","♀","✖","✖","✖","／","A","B","C","D","E",
                 "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
                 "V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k",
                 "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","✖",
                 "✖","✖","✖","✖","✖","✖","✖","✖","✖","✖","✖","✖","✖","✖","✖","✖")

def get_number_from_array(num_array):
    num = 0
    for i in reversed(num_array):
        num = (num << 8) + i
    return num

def get_array_from_number(num, length):
    output = [num >> (8 * i) & 0xFF for i in range(length // 8)]
    return output

def convert_hexcode(raw_data):
    output = (list(reversed(get_array_from_number(raw_data, wanted_bit_length))) 
    if little_endian_input else 
    get_array_from_number(raw_data, wanted_bit_length))
    return output

while True:
    try:
        cpu_mode = input("ARM or Thumb? (default is \"Thumb\")").strip() or "Thumb"
        match cpu_mode.lower():
            case "arm":
                wanted_bit_length = 32
            case "thumb":
                wanted_bit_length = 16
            case _:
                raise ValueError(cpu_mode)
        break
    except ValueError as err:
        print(f"{err.args} is not a valid input")

while True:
    try:
        endianness = input("Endianness of hexadecimal (default is \"big\"): ").strip() or "big"
        match endianness.lower():
            case "big":
                little_endian_input = False
                break
            case "little":
                little_endian_input = True
                break
            case _:
                raise ValueError(endianness)
    except ValueError as err:
        print(f"{err.args} is not a valid input")

while True:
    try:
        user_input = input("Enter hexcode (Press enter on empty input when done): ")
        if user_input:
            hexcode.append(int(user_input, 16))
        else:
            break
    except ValueError as err:
        print(f"{err.args} is not a valid input")

hex_byte_code = [convert_hexcode(i) for i in hexcode]
# [[japaneseTable[i] for i in i] for i in hex_byte_code]

char_code = ''
code_gen_input = ''
raw_hex_code = ''

for i in hex_byte_code:
    if any(j in range(0xEF, 0x100) for j in i) or any(j in range(0xB7, 0xBA) for j in i):
        nowrite_chars_present = True
    if 0xFF in i:
        ff_term_present = True
    char_code += ''.join([japaneseTable[j] for j in i]) + '\n'
    code_gen_input += f'{hex(get_number_from_array(i))}\n'
    raw_hex_code += f'{get_number_from_array(list(reversed(i))):0{wanted_bit_length//4}X}\n'

print(f'''\
{f"⚠️ Contains unwritable characters{chr(10)}" 
  if nowrite_chars_present else ""}\
{f"ℹ️ 0xFF is only usable when leaving spaces empty or when placing commands on the very start/end of a box name{chr(10)}" 
  if ff_term_present else ""}\
Box Name Codes:
{char_code}
CodeGenerator Input (should be rearranged for Thumb):
{code_gen_input}
Raw Hexcode
{raw_hex_code}\
''')
