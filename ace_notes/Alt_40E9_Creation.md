# Non-shiny 0x40E9 generation code
This code allows obtaining non-shiny 0x40E9 in one 0x611 execution without needing DOTS.

## Instructions
Make sure Box 10, Slot 19 is empty before executing this code.
Write and execute the following code:
```
Box  1: 5 C U n n R … o	[5CUnnR…o]
Box  2: P R o 7 9 … o _	[PRo79…o ]
Box  3: _ _ C 2 w m _ _	[  C2wm  ] (replace 'C' with 'E' if using inaccurate emulator)
Box  4: _ B F w m _ _ _	[ BFwm   ]
Box  5: F R l o v F ? n	[FRlovF?n]
Box  6: _ _ _ / F Q m _	[   /FQm ]
Box  7: _ _ D F Q m _ _	[  DFQm  ]
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
After this, you should save and soft reset to facilitate the creation of the Thumb→ARM bootstrap.

## Technical details
The following is the the hexadecimal of this box name code along with their corresponding instructions:
```
E2CFBAD6    SBC R11, PC, #0x2980 ; R11 = Box 10, Slot 19 - 0x3* (7 on console and accurate emulators, 9 on inaccurate emulators)
E3B0CCE2    MOVS R12, #0xE200
E3CCCAFF    BIC R12, R12, #0xFF000 ; R12 = 0x200, hasSpecies set
E3B0AAA8    MOVS R10, #0xA8000 ; R10 & 0xFFFF = 0x8000, non-shiny SID for TID 0 and PID 0
0000FF00    ; filler
E1EBA3B*    STRH R10, [R11, #0x3*]! ; * = D for console and accurate emulators, F for inaccurate emulators, store SID
00FF0000    ; filler
E1EBC0BC    STRH R12, [R11, #0xC]! ; store hasSpecies flag
FF000000    ; filler
E3E0CCC0    MVN R12, #0xC000 ; R12 = 0xFFFF3FFF
E2ACC0EA    ADC R12, R12, #0xEA ; R12 = 0xFFFF40E9
000000FF    ; filler
E1CBC0BA    STRH R12, [R11, #0xA] ; Store checksum
0000FF00    ; filler
E1CBC0BE    STRH R12, [R11, #0xE] ; Store species
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
