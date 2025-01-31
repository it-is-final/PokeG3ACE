# Non-shiny 0x40E9 generation code
This code allows obtaining non-shiny 0x40E9 in one 0x611 execution without needing DOTS.

## Instructions
Make sure Box 10, Slot 19 is empty before executing this code.
Write and execute the following code:
```
Box  1: 5 C U n n R … o	[5CUnnR…o]
Box  2: P R o / J Q m _	[PRo/JQm ] (change '/' to 'B' on inaccurate emulator)
Box  3: _ _ N P … o _ _	[  NP…o  ]
Box  4: _ C I w m _ _ _	[ CIwm   ] (change 'C' to 'E' on inaccurate emulator)
Box  5: F R l o v F ? n	[FRlovF?n]
Box  6: _ _ _ ♀ G Q m _	[   ♀GQm ]
Box  7: _ _ / G Q m _ _	[  /GQm  ]
Box  8: _ F G E n _ _ _	[ FGEn   ]
Box  9: z … l o z ♀ Q o	[z…loz♀Qo]
Box 10: ♀ Q n _ … ? q _	[♀Qn …?q ]
Box 11: _ _ h T – n _ _	[  hT–n  ]
Box 12: _ Y N ? n _ _ _	[ YN?n   ]
Box 13: F N R o b _ ? n	[FNRob ?n]
Box 14: _ _ _ _ _ _ … _	[      … ]
```

A decamark should appear in Box 10, Slot 19.
Its species name should be ` ÓàÉ LvLv`, and it should be female and level 100.

## Technical details
The following is the the hexadecimal of this box name code along with their corresponding instructions:
```
E2CFBAD6    SBC R11, PC, #0x2980 ; R11 = Box 10, Slot 19 - 0x3* (7 on console and accurate emulators, 9 on inaccurate emulators)
E3B0CCE2    MOVS R12, #0xE200
E3CCCAFF    BIC R12, R12, #0xFF000 ; R12 = 200, hasSpecies set
E1CBC4B*    STRH R12, [R11, #0x4*] ; * = A for console and accurate emulators, C for inaccurate emulators, store hasSpecies
0000FF00    ; filler
E3B0CAC8    MOVS R12, #0xC8000 ; SID to make 0x40E9 non-shiny
00FF0000    ; filler
E1EBC3B*    STRH R12, [R11, #0x3*] ; * = D for console and accurate emulators, F for inaccurate emulators, store SID
FF000000    ; filler
E3E0CCC0    MVN R12, #0xC000 ; R12 = 0xFFFF3FFF
E2ACC0EA    ADC R12, R12, #0xEA ; R12 = 0xFFFF40E9
000000FF    ; filler
E1CBC1B6    STRH R12, [R11, #0x16] ; Store checksum
0000FF00    ; filler
E1CBC1BA    STRH R12, [R11, #0x1A] ; Store species
00FF0000    ; filler
E2BFC1C0    ADCS R12, PC, #0x30 ; R12 = address of Box 14 name
FF000000    ; filler
E3E0B0EE    MVN R11, #0xEE
E3CBB6EE    BIC R11, R11, #0xEE00000
E2CBB6FF    SBC R11, R11, #0xFF00000 ; R11 = 0xE12FFF10 (BX R0)
E5ACB000    STR R12, [R11, #0x0]! ; Store BX R0 opcode in Box 14 name
0000FF00    ; filler
E2AECEDC    ADC R12, LR, #0xDC0 ; LR = 0x080069E7
00FF0000    ; filler
E2ACC8D3    ADC R12, R12, #0xD30000
FF000000    ; filler
E3CCC8C0    BIC R12, R12, #0xC00000
E2AC00D6    ADC R0, R12, #0xD6 ; R0 = SetCB2WhiteOut
000000FF    ; filler
B0000000    ; becomes BX R0 (0xE12FFF10)
```
