# Hexwriter in 7 Codes
## Preamble
Recently there has been efforts to simplify the writing of the hexadecimal writer (hexwriter) with the 'advent' of mail corruption.
This is one of those efforts.

While these codes can be executed on FRLG grab ACE, keep in mind that this guide is written with Emerald in mind (check the FRLG version’s prequisites beforehand).

## Prequisites
- Game Boy Advance console or a highly-accurate emulator (like mGBA 0.9.0+)
   - These codes do not work if the `PC` register is aligned, e.g. executing ACE through an inaccurate emulator
   - Ancient Thumb → ARM bootstraps are also included, the standard bootstrap setup can be found [here](https://e-sh4rk.github.io/ACE3/emerald/getting-started/stable-ace/#thumb-arm-bootstrap-for-the-english-french-and-italian-versions-only)
- A stable ACE Pokémon, with its Thumb → ARM bootstrap if required
- An exit code bootstrap, with box 14 named `␣␣␣Œ`
    - Instructions on how to create this can be found [here](https://e-sh4rk.github.io/ACE3/emerald/getting-started/exit-code/)


## Instructions 
Before starting the writing of the hexwriter, make sure that Box 10, Slot 2 is empty.
Saves and resets are allowed during this process, as there is no risk of save corruption.
Viewing Box 10 is allowed during this process.

Write and execute the following 7 box name codes, one after the other:
```
### CODE 1 ###
Box  1: C C U n 2 M … o	[CCUn2M…o]
Box  2: _ _ _ – H ? n _	[   –H?n ]
Box  3: _ _ i Q ? n _ _	[  iQ?n  ]
Box  4: _ N T ? n _ _ _	[ NT?n   ]
Box  5: 6 F ! q z M … o	[6F!qzM…o]
Box  6: _ _ _ q J ? n _	[   qJ?n ]
Box  7: _ _ l T ? n _ _	[  lT?n  ]
Box  8: _ – R ! s _ _ _	[ –R!s   ]
Box  9: N I l o c M ? n	[NIlocM?n]
Box 10: _ _ _ e U ? n _	[   eU?n ]
Box 11: _ _ 1 F ? n _ _	[  1F?n  ]
Box 12: _ – R ! s _ _ _	[ –R!s   ]
Box 13: _ _ _ … _ _ _ _	[   …    ]

### CODE 2 ###
Box  1: C C U n g G l o	[CCUngGlo]
Box  2: _ _ _ g L R n _	[   gLRn ]
Box  3: _ _ a S R n _ _	[  aSRn  ]
Box  4: _ 1 T R n _ _ _	[ 1TRn   ]
Box  5: ‘ F ! q 0 K l o	[‘F!q0Klo]
Box  6: _ _ _ 0 H ? n _	[   0H?n ]
Box  7: _ _ l P ? n _ _	[  lP?n  ]
Box  8: _ 0 P ? n _ _ _	[ 0P?n   ]
Box  9: – R ! s W M … o	[–R!sWM…o]
Box 10: _ _ _ k J ? n _	[   kJ?n ]
Box 11: _ _ W P ? n _ _	[  WP?n  ]
Box 12: _ “ F ? n _ _ _	[ “F?n   ]
Box 13: – R ! s _ _ _ _	[–R!s    ]

### CODE 3 ###
Box  1: C C U n P K … o	[CCUnPK…o]
Box  2: _ _ _ t P ? n _	[   tP?n ]
Box  3: _ _ 0 Q ? n _ _	[  0Q?n  ]
Box  4: _ G T ? n _ _ _	[ GT?n   ]
Box  5: E F ! q H K … o	[EF!qHK…o]
Box  6: _ _ _ ” H ? n _	[   ”H?n ]
Box  7: _ _ z R ? n _ _	[  zR?n  ]
Box  8: _ J R ? n _ _ _	[ JR?n   ]
Box  9: – R ! s z K … o	[–R!szK…o]
Box 10: _ _ _ 0 L ? n _	[   0L?n ]
Box 11: _ _ Q P ? n _ _	[  QP?n  ]
Box 12: _ – R ! s _ _ _	[ –R!s   ]
Box 13: _ _ _ … _ _ _ _	[   …    ]

### CODE 4 ###
Box  1: C C U n 1 H l o	[CCUn1Hlo]
Box  2: _ _ _ I M ? n _	[   IM?n ]
Box  3: _ _ l P ? n _ _	[  lP?n  ]
Box  4: _ F H ? n _ _ _	[ FH?n   ]
Box  5: Q F ! q L I … o	[QF!qLI…o]
Box  6: _ _ _ R M R n _	[   RMRn ]
Box  7: _ _ Z Q R n _ _	[  ZQRn  ]
Box  8: _ – R ! s _ _ _	[ –R!s   ]
Box  9: G H … o t M ? n	[GH…otM?n]
Box 10: _ _ _ . R ? n _	[   .R?n ]
Box 11: _ _ C U ? n _ _	[  CU?n  ]
Box 12: _ – R ! s _ _ _	[ –R!s   ]
Box 13: _ _ _ … _ _ _ _	[   …    ]

### CODE 5 ###
Box  1: C C U n N I l o	[CCUnNIlo]
Box  2: _ _ _ Y M ? n _	[   YM?n ]
Box  3: _ _ l P ? n _ _	[  lP?n  ]
Box  4: _ … H ? n _ _ _	[ …H?n   ]
Box  5: c F ! q P K … o	[cF!qPK…o]
Box  6: _ _ _ 6 P ? n _	[   6P?n ]
Box  7: _ _ C S ? n _ _	[  CS?n  ]
Box  8: _ G F ? n _ _ _	[ GF?n   ]
Box  9: – R ! s , I l o	[–R!s,Ilo]
Box 10: _ _ _ q M ? n _	[   qM?n ]
Box 11: _ _ P P ? n _ _	[  PP?n  ]
Box 12: _ F I ? n _ _ _	[ FI?n   ]
Box 13: – R ! s _ _ _ _	[–R!s    ]

### CODE 6 ###
Box  1: C C U n X H … o	[CCUnXH…o]
Box  2: _ _ _ 1 M ? n _	[   1M?n ]
Box  3: _ _ x R ? n _ _	[  xR?n  ]
Box  4: _ 0 R ? n _ _ _	[ 0R?n   ]
Box  5: C U ? n o F ! q	[CU?noF!q]
Box  6: _ _ _ 4 J l o _	[   4Jlo ]
Box  7: _ _ 0 I ? n _ _	[  0I?n  ]
Box  8: _ k M ? n _ _ _	[ kM?n   ]
Box  9: e P ? n – R ! s	[eP?n–R!s]
Box 10: _ _ _ _ _ _ … _	[      … ]
Box 11: _ _ _ _ _ … _ _	[     …  ]
Box 12: _ _ _ _ … _ _ _	[    …   ]
Box 13: _ _ _ … _ _ _ _	[   …    ]

### CODE 7 ###
Box  1: C C U n N I l o	[CCUnNIlo]
Box  2: _ _ _ b M ? n _	[   bM?n ]
Box  3: _ _ c R ? n _ _	[  cR?n  ]
Box  4: _ 2 S ? n _ _ _	[ 2S?n   ]
Box  5: H F ? n w F ! q	[HF?nwF!q]
Box  6: _ _ _ l K … o _	[   lK…o ]
Box  7: _ _ 1 L ? n _ _	[  1L?n  ]
Box  8: _ E O ? n _ _ _	[ EO?n   ]
Box  9: G S ? n – R ! s	[GS?n–R!s]
Box 10: _ _ _ m F l o _	[   mFlo ]
Box 11: _ _ y L R o _ _	[  yLRo  ]
Box 12: _ m H R o _ _ _	[ mHRo   ]
Box 13: – R ! s _ _ _ _	[–R!s    ]
```

The bad egg is now ready to be used as the hexwriter.
Its hex data should be identical to the original version of the hexwriter.
Move this bad egg to Box 14, Slot 29 and execute ACE.
Most likely whatever is written in the box names would be interpreted as a bad egg, however if you want certainty that the hexwriter is working properly, write the following names and execute ACE.
```
Box  1: 00000000
Box  2: 00000000
Box  3: C6E9D7DF
Box  4: EDFFFFFF
Box  5: FFFF0002
Box  6: 00000000
Box  7: 00000000
Box  8: 71000000
Box  9: 71000000
Boxes 10-14: 00000000
```
A shiny Chansey named 'Lucky' should appear in Box 14, Slot 28.

If you want to know what the hex data for the hexwriter is supposed to be, it is the following:
```
8A808FE2
000EB8E8
02045CE3
66C04F32
0910D8E7
B11051E2
10109132
0BB28150
00B09C45
01001AE3
01B0CC14
00B0A013
07005AE3
01A08A32
00A0A023
01908922
019089E2
7E0059E3
40F04F42
10FF2FE1
```

## Troubleshooting
If the hexwriter is not working as expected, please refer to [this troubleshooting guide](https://e-sh4rk.github.io/ACE3/emerald/hex-writer/hex-writer/#appendix-in-case-of-failure) for the hexwriter.

## How these codes work
```
SBC r11, pc, #0x2F40
```
This subtracts `0x2F40` from the `pc` register, and due to the instruction being `SBC` and the carry flag is unset, it also subtracts an extra `0x1` from the result.
Since it is expected that the code will be executed using `0x351` where it executes in ARM mode with the `pc` register's bit 1 set to `1`, the result assigned to `r11` will be `0xA7` (167) bytes before the PID of Box 10, Slot 2.
I have chosen an offset of `0xA7` as that it and (most) later offsets are writable using the European character set which allows storing using `STR r12, [r11, {offset}]!` and for the most part remove the need to waste an opcode incrementing `r11`.
It also allowed `STRB` to be usable for writing part of the hexwriter as that is encoded similarly to `STR`.

```
STR r12, [r11, r14, LSR #25]! ; encoded as `E7ABCCAE`
```
merrp is to be credited for using this trick to be able to increment `r11` using `STR` with what would be unwritable offsets thanks to the limitations of the European character set.
Since `r14` is always initially a ROM address where the most significant byte of the address is usually `0x8`, if the value is shifted right by 25 bits, it will become `0x4`.
This allows writing to the address stored in `r11` + `0x4` which is highly useful for the purposes of writing the hexwriter, as we do not need to waste more opcodes on writing half of each instruction then using `STRH` which takes up more space.

### Box name codes
Below are the inputs to E-Sh4rk's CodeGenerator for each box name code along with the exact bytes that each code writes, and their starting offsets

#### Code 1
Starting offset: 0x0 + 0xA7 = 0xA7
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0xE28F808A ?
STR r12, [r11, #0xA7]!
MOVS r12, #0xE8B80E00 ?
0xE7ABCCAE
MOVS r12, #0xE35C0402 ?
0xE7ABCCAE
```

Writes:
```
8A 80 8F E2
00 0E B8 E8
02 04 5C E3
```

#### Code 2
Starting offset: 0xC + 0xA7 = 0xB3
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0x324FC066 ?
STR r12, [r11, #0xB3]!
MOVS r12, #0xE7D81009 ?
0xE7ABCCAE
MOVS r12, #0xE25110B1 ?
0xE7ABCCAE
```

Writes:
```
66 C0 4F 32
09 10 D8 E7
B1 10 51 E2
```

#### Code 3
Starting offset: 0x18 + 0xA7 = 0xBF
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0x32911010 ?
STR r12, [r11, #0xBF]!
MOVS r12, #0x5081B20B ?
0xE7ABCCAE
MOVS r12, #0x459CB000 ?
0xE7ABCCAE
```

Writes:
```
10 10 91 32
0B B2 81 50
00 B0 9C 45
```

#### Code 4
Starting offset: 0x24 + 0xA7 = 0xCB
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0xE31A0001 ?
STR r12, [r11, #0xCB]!
MOVS r12, #0x14CCB001 ?
0xE7ABCCAE
MOVS r12, #0x13A0B000 ?
0xE7ABCCAE
```

Writes:
```
01 00 1A E3
01 B0 CC 14
00 B0 A0 13
```

#### Code 5
Starting offset: 0x30 + 0xA7 = 0xD7
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0xE35A0007 ?
STR r12, [r11, #0xD7]!
MOVS r12, #0x328AA001 ?
0xE7ABCCAE
MOVS r12, #0x23A0A000 ?
0xE7ABCCAE
```

Writes:
```
07 00 5A E3
01 A0 8A 32
00 A0 A0 23
```

#### Code 6
Starting offset: 0x3C + 0xA7 = 0xE3
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0x22899001 ?
STR r12, [r11, #0xE3]!
MOVS r12, #0xE2899001 ?
0xE7ABCCAE
```

Writes:
```
01 90 89 22
01 90 89 E2
```

#### Code 7
Starting offset: 0x44 + 0xA7 = 0xE3
```
@@ exit = "Bootstrapped"
@@
SBC r11, pc, #0x2F40
MOVS r12, #0xE359007E ?
STR r12, [r11, #0xEB]!
MOVS r12, #0x424FF040 ?
0xE7ABCCAE
; MOVS r12, #0xE12FFF10 ?
MVN r12, #0xE1
BIC r12, #0xED00000
BIC r12, #0x1000000E ; r12 = E12FFF10 BX r0
0xE7ABCCAE
```

Writes:
```
7E 00 59 E3
40 F0 4F 42
10 FF 2F E1
```

## References and Acknowledgements
- [E-Sh4rk's original article for the hexwriter](https://e-sh4rk.github.io/ACE3/emerald/hex-writer/hex-writer/)
- [Adrichu00's method of writing the hexwriter](https://gist.github.com/Adrichu00/49433953af9d6fd7c1cd368d48c68778)
- RationalPsycho on the Glitch City Research Institute Discord for the glitched mail inputs
- merrp on the Glitch City Research Institute Discord for the `STR+4` opcode used in the codes.
