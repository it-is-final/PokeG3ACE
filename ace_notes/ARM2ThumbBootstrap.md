# ARM → Thumb Bootstrap
This code generates a `?` in Box 10, Slot 19 with the nickname `Âî nÚ`.
This switches execution from ARM mode to Thumb mode which may be useful in very limited cicrumstances.

```
Box  1: 4 . U n 1 H l o	[4.Un1Hlo]
Box  2: _ ? ” 2 M ? n _	[ ?”2M?n ]
Box  3: ? ” N Q ? n _ _	[?”NQ?n  ]
Box  4: E l H ? n _ _ _	[ElH?n   ]
Box  5: _ F 9 q z L l o	[ F9qzLlo]
Box  6: L R n w F R n _	[LRnwFRn ]
Box  7: ? ” F 2 9 n _ _	[?”F29n  ]
Box  8: E _ F 9 q _ _ _	[E F9q   ]
Box  9: i R … o M U ? n	[iR…oMU?n]
Box 10: … … o , F P m _	[……o,FPm ]
Box 11: ? ” N S … o _ _	[?”NS…o  ]
Box 12: E ♀ F P m _ _ _	[E♀FPm   ]
Box 13: … “ P m ’ “ P m	[…“Pm’“Pm]
```

## Result
**Nickname Opcodes**:
```
E28F2003    ADD r2, pc, #0x3
E12FFF12    BX r2
```

**Pokemon Data**:
```
00 00 00 00 00 00 00 00
3E C0 8F E2 0F 00 00 EA
00 00 00 32 00 00 00 00
00 00 00 00 0F 00 00 00
0F 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
```

## CodeGenerator Input
```
@@ filler1 = 0xB2AC00FF
@@ filler2 = 0xB2ACFF00
@@ filler3 = 0xBFFF0000
%% E28F203F ADD r2, pc, #0x3
%% E12FFF12 BX r2
%% E01C B #0x3C
@@

SBC r10, pc, #0x2940
MOVS r12, #0xE28F2003 ?
STR r12, [r10]!
MVN r12, #0xEE00000
SBC r12, #0xFF00000
SBC r12, #0xEB ; r12 = E12FFF12 BX r2
ADC r10, r10, #0x3
STR r12, [r10]!
MOVS r12, #0xE01C ?
MOVS r11, #0xFF
STRH r12, [r10, #0x8]
MOVS r12, #0x3200
STRH r12, [r10, #0x6]
STRH r11, [r10, #0x10]
STRH r11, [r10, #0x14]
```