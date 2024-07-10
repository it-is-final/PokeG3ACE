# Payload Writer

- Only needs modification of Boxes 6, 7, 8 and 9 once set up.
- A basic checksum for the current 8 bytes is set up.

## How to use

- Calculate the base and offset for the 8 bytes to write
- Figure out the offset in the Pokemon data

- Box 6 has first_four_bytes base data
- Box 7 has first_four_bytes offset data
- Box 8 has last_four_bytes base data
- Box 9 has last_four_bytes offset data and address offset

## Basic Boxnames

```text
Box  1: ル ば つ ぶ け は ざ 」	[ルばつぶけはざ」]
Box  2: _ け ッ ふ N _ l	[ けッふN l]
Box  3: つ の ぐ N サ の し G	[つのぐNサのしG]
Box  4: _ V ね ざ B _ l	[ VねざB l]
Box  5: さ 0 く タ し ぶ た ぃ	[さ0くタしぶたぃ]
Box  6: _ _ び あ あ あ あ	[  びああああ]
Box  7: ア ア い い い い	[アアいいいい]
Box  8: ア う う う う	[アうううう]
Box  9: え え え え ャ ゆ _ _	[ええええャゆ  ]
Box 10: ア ア ア	[アアア]
Box 11: ア ア y コ く く	[アアyコくく]
```
