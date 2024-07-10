# # # # # # # # # # # # # # # # #
# Convert Numbers to Characters #
# # # # # # # # # # # # # # # # #

japaneseTable = ("␣","あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ",
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

def get_number_from_array(num_array):
    num = 0
    for i in reversed(num_array):
        num = (num << 8) + i
    return num

def get_array_from_number(num, length):
    output = [num >> (8 * i) & 0xFF for i in range(length // 8)]
    return output

while True:
    try:
        wanted_bit_length = int(input("Bit length of number: "))
        if wanted_bit_length % 8:
            raise ValueError(wanted_bit_length)
        break
    except ValueError as err:
        print(f"{err.args} is not a valid input")

while True:
    try:
        endianness = input("Endianness of hexadecimal: ")
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
        input_value = int(input("Enter a hexadecimal number: "),16)
        break
    except ValueError as err:
        print(f"{err.args} is not a valid input")

raw_bytes = (list(reversed(get_array_from_number(input_value, wanted_bit_length))) 
             if little_endian_input else 
             get_array_from_number(input_value, wanted_bit_length))

output_base = [(get_characters(i))[0] for i in raw_bytes]
output_offset = [(get_characters(i))[1] for i in raw_bytes]

print(f'''\
Base:\t\
{' '.join([japaneseTable[i] for i in output_base])}\t\
({''.join([japaneseTable[i] for i in output_base])})
Offset:\t\
{' '.join([japaneseTable[i] for i in output_offset])}\t\
({''.join([japaneseTable[i] for i in output_offset])})

CodeGenerator Input:
{hex(get_number_from_array(output_base))}
{hex(get_number_from_array(output_offset))}

Raw Hex:
{get_number_from_array(list(reversed(output_base))):0{wanted_bit_length//4}X}
{get_number_from_array(list(reversed(output_offset))):0{wanted_bit_length//4}X}\
''')