# FRLG Hexwriter in 7 Codes
## Preamble
Recently there has been efforts to simplify the writing of the hexwriter with the 'advent' of mail corruption.
This is one of those efforts.

## Prequisites
- Knowledge on how to perform mail corruption and grab ACE
- `BIC r0, r0, #0xFF` and `BX lr` written to Box 14's name, the name should like ` Foì`
    - This specific set-up does not require any bootstrap if you are writing box name codes only
    - Instructions on how to write this can be found [here](ExitCodes/FRLG_GrabACE_ShortExit.md)
- The exit code bootstrap.
    - This is technically not necessary for the box name codes and can be created after the creation of the hexwriter
    - This will allow the hexwriter to exit properly via `r0`
    - Instructions on how to create this can be found [here](ExitCodes/GrabACEBootstrap.md)


## Instructions
1. Activate the mail glitch
2. Write these words to their slot indicated by the arrow:
    - `LISTEN` → Word 3
    - `THICK FAT` → Word 5
    - `LIKELY TO` → Word 9
3. A bad egg should appear in Box 3, Slot 1, move this to Box 10, Slot 2.
4. Write and execute the following 7 box name codes, one after the other:
    ```
    ### CODE 1 ###
    Box  1: C C U n 2 M … o	[CCUn2M…o]
    Box  2: _ _ _ – H ? n _	[   –H?n ]
    Box  3: _ _ i Q ? n _ _	[  iQ?n  ]
    Box  4: _ N T ? n _ _ _	[ NT?n   ]
    Box  5: 6 F ! q t R … o	[6F!qtR…o]
    Box  6: _ _ _ , F ? n _	[   ,F?n ]
    Box  7: _ _ ♀ F w m _ _	[  ♀Fwm  ]
    Box  8: _ l R … o _ _ _	[ lR…o   ]
    Box  9: c U ? n ’ F w m	[cU?n’Fwm]
    Box 10: _ _ _ g G l o _	[   gGlo ]
    Box 11: _ _ g L R n _ _	[  gLRn  ]
    Box 12: _ a S R n _ _ _	[ aSRn   ]
    Box 13: 1 T R n – R ! s	[1TRn–R!s]

    ### CODE 2 ###
    Box  1: C C U n s R … o	[CCUnsR…o]
    Box  2: _ _ _ d F ? n _	[   dF?n ]
    Box  3: _ _ / Q w m _ _	[  /Qwm  ]
    Box  4: _ W M … o _ _ _	[ WM…o   ]
    Box  5: k J ? n W P ? n	[kJ?nWP?n]
    Box  6: _ _ _ “ F ? n _	[   “F?n ]
    Box  7: _ _ – R ! s _ _	[  –R!s  ]
    Box  8: _ P K … o _ _ _	[ PK…o   ]
    Box  9: t P ? n 0 Q ? n	[tP?n0Q?n]
    Box 10: _ _ _ G T ? n _	[   GT?n ]
    Box 11: _ _ – R ! s _ _	[  –R!s  ]
    Box 12: _ _ _ _ … _ _ _	[    …   ]
    Box 13: _ _ _ … _ _ _ _	[   …    ]

    ### CODE 3 ###
    Box  1: C C U n H K … o	[CCUnHK…o]
    Box  2: _ _ _ ” H ? n _	[   ”H?n ]
    Box  3: _ _ z R ? n _ _	[  zR?n  ]
    Box  4: _ J R ? n _ _ _	[ JR?n   ]
    Box  5: I F ! q z K … o	[IF!qzK…o]
    Box  6: _ _ _ 0 L ? n _	[   0L?n ]
    Box  7: _ _ Q P ? n _ _	[  QP?n  ]
    Box  8: _ – R ! s _ _ _	[ –R!s   ]
    Box  9: 1 H l o I M ? n	[1HloIM?n]
    Box 10: _ _ _ l P ? n _	[   lP?n ]
    Box 11: _ _ F H ? n _ _	[  FH?n  ]
    Box 12: _ – R ! s _ _ _	[ –R!s   ]
    Box 13: _ _ _ … _ _ _ _	[   …    ]

    ### CODE 4 ###
    Box  1: C C U n L I … o	[CCUnLI…o]
    Box  2: _ _ _ R M R n _	[   RMRn ]
    Box  3: _ _ Z Q R n _ _	[  ZQRn  ]
    Box  4: _ U F ! q _ _ _	[ UF!q   ]
    Box  5: G H … o t M ? n	[GH…otM?n]
    Box  6: _ _ _ . R ? n _	[   .R?n ]
    Box  7: _ _ C U ? n _ _	[  CU?n  ]
    Box  8: _ – R ! s _ _ _	[ –R!s   ]
    Box  9: N I l o Y M ? n	[NIloYM?n]
    Box 10: _ _ _ l P ? n _	[   lP?n ]
    Box 11: _ _ … H ? n _ _	[  …H?n  ]
    Box 12: _ – R ! s _ _ _	[ –R!s   ]
    Box 13: _ _ _ … _ _ _ _	[   …    ]

    ### CODE 5 ###
    Box  1: C C U n P K … o	[CCUnPK…o]
    Box  2: _ _ _ 6 P ? n _	[   6P?n ]
    Box  3: _ _ C S ? n _ _	[  CS?n  ]
    Box  4: _ G F ? n _ _ _	[ GF?n   ]
    Box  5: g F ! q , I l o	[gF!q,Ilo]
    Box  6: _ _ _ q M ? n _	[   qM?n ]
    Box  7: _ _ P P ? n _ _	[  PP?n  ]
    Box  8: _ F I ? n _ _ _	[ FI?n   ]
    Box  9: – R ! s X H … o	[–R!sXH…o]
    Box 10: _ _ _ 1 M ? n _	[   1M?n ]
    Box 11: _ _ x R ? n _ _	[  xR?n  ]
    Box 12: _ 0 R ? n _ _ _	[ 0R?n   ]
    Box 13: C U ? n – R ! s	[CU?n–R!s]

    ### CODE 6 ###
    Box  1: C C U n 4 J l o	[CCUn4Jlo]
    Box  2: _ _ _ 0 I ? n _	[   0I?n ]
    Box  3: _ _ k M ? n _ _	[  kM?n  ]
    Box  4: _ e P ? n _ _ _	[ eP?n   ]
    Box  5: s F ! q N I l o	[sF!qNIlo]
    Box  6: _ _ _ b M ? n _	[   bM?n ]
    Box  7: _ _ c R ? n _ _	[  cR?n  ]
    Box  8: _ 2 S ? n _ _ _	[ 2S?n   ]
    Box  9: H F ? n – R ! s	[HF?n–R!s]
    Box 10: _ _ _ l K … o _	[   lK…o ]
    Box 11: _ _ 1 L ? n _ _	[  1L?n  ]
    Box 12: _ E O ? n _ _ _	[ EO?n   ]
    Box 13: G S ? n – R ! s	[GS?n–R!s]

    ### CODE 7 ###
    Box  1: B C U n z L l o	[BCUnzLlo]
    Box  2: L R n y F R n _	[LRnyFRn ]
    Box  3: _ _ ‘ F ! q _ _	[  ‘F!q  ]
    Box  4: _ _ _ _ … _ _ _	[    …   ]
    Box  5: _ _ _ … _ _ _ _	[   …    ]
    Box  6: _ _ _ _ _ _ … _	[      … ]
    Box  7: _ _ _ _ _ … _ _	[     …  ]
    Box  8: _ _ _ _ … _ _ _	[    …   ]
    Box  9: _ _ _ … _ _ _ _	[   …    ]
    Box 10: _ _ _ _ _ _ … _	[      … ]
    Box 11: _ _ _ _ _ … _ _	[     …  ]
    Box 12: _ _ _ _ … _ _ _	[    …   ]
    Box 13: _ _ _ … _ _ _ _	[   …    ]

    ```
5. The bad egg is now ready to be used as the hexwriter.
Its hex data should be identical to the original version of the hexwriter.
Move this bad egg to Box 14, Slot 29 and execute ACE.
Most likely whatever is written in the box names would be interpreted as a bad egg, however if you want certainty that the hexwriter is working normally, write the following names and execute ACE.
```
Box  1: 00000000
Box  2: 00000000
Box  3: BDDCD5E6
Box  4: E0D9E7FF
Box  5: FFFF0002
Box  6: 00000000
Box  7: 00000000
Box  8: 01000000
Box  9: 01000000
Boxes 10-14: 00000000
```
A Bulbasaur named 'Charles' should appear in Box 14, Slot 28

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
In the very last code, I (thanks to the suggestion of Adrichu00) changed the immediate being subtracted from `#0x2F40` to `#0x2F00` which allows writing an `STR` instruction for that particular section without needing to use `ADC` or `LDRSB` to increment `r11`.

```
STR r12, [r11, r14, LSR #25]! ; encoded as `E7ABCCAE`
```
merrp is to be credited for using this trick to be able to increment `r11` using `STR` with what would be unwritable offsets thanks to the limitations of the European character set.
Since `r14` is always initially a ROM address where the most significant byte of the address is usually `0x8`, if the value is shifted right by 25 bits, it will become `0x4`.
This allows writing to the address stored in `r11` + `0x4` which is highly useful for the purposes of writing the hexwriter, as we do not need to waste more opcodes on writing half of each instruction then using `STRH` which takes up more space.
However for FireRed and LeafGreen, since we have access to mail corruption, and it so happens that some of the halfwords are writable as mail words, we can still use `STRH` for those instructions where half of it is already written by mail corruption.

From this, the codes are generally structured as the following:
```
SBC r11, pc, #0x2F40
MOVS r12, #{opcode_1} ?
STR r12, [r11, #{offset}]!
MOVS r12, #{opcode_2} ?
STR r12, [r11, r14, LSR #25]!
MOVS r12, #{opcode_3} ?
STR r12, [r11, r14, LSR #25]!
```
with some codes using different instructions due to either having a halfword already written with the mail corruption enabling us to use `STRH` and using `MOVS` with only half of the instruction as the immediate or having an unwritable offset.

## Mail corruption
The mail corruption allows directly writing halfwords that would have made the main code writing process longer.
With the mail written at the start of the process, here is the index of each word we wrote:
|Word|Index (hex)|
|-|-|
|`LISTEN`|0E00|
|`THICK FAT`|0402|
|`LIKELY TO`|1009|

## CodeGenerator Input
All of these codes have the following header
```
@@ exit = "Bootstrapped"
@@
```

If you see * in the writes section, that means part of it was already written by mail corruption
Assume opcodes without an @ are all written with an offset of +`0x4` relative to the previous opcode

### Code 1
```
SBC r11, pc, #0x2F40
MOVS r12, #0xE28F808A ?
STR r12, [r11, #0xA7]!
MOVS r12, #0xE8B8 ?
STRH r12, [r11, #0x6]!
MOVS r12, #0xE35C ?
STRH r12, [r11, #0x4]!
MOVS r12, #0x324FC066 ?
0xE7ABCCAE
```

Writes:
```
E28F808A @ 0x0+0xA7
E8B8****
E35C****
324FC066
```

### Code 2
```
SBC r11, pc, #0x2F40
MOVS r12, #0xE7D8 ?
STRH r12, [r11, #0xBA]!
MOVS r12, #0xE25110B1 ?
0xE7ABCCAE
MOVS r12, #0x32911010 ?
0xE7ABCCAE
```

Writes:
```
E7D8**** @ 0x12+0xA7+1
E25110B1
32911010
```


### Code 3
```
SBC r11, pc, #0x2F40
MOVS r12, #0x5081B20B ?
STR r12, [r11, #0xC3]!
MOVS r12, #0x459CB000 ?
0xE7ABCCAE
MOVS r12, #0xE31A0001 ?
0xE7ABCCAE
```

Writes:
```
5081B20B @ 0x1C+0xA7
459CB000
E31A0001
```


### Code 4
```
SBC r11, pc, #0x2F40
MOVS r12, #0x14CCB001 ?
STR r12, [r11, #0xCF]!
MOVS r12, #0x13A0B000 ?
0xE7ABCCAE
MOVS r12, #0xE35A0007 ?
0xE7ABCCAE
```

Writes:
```
14CCB001 @ 0x28+0xA7
13A0B000
E35A0007
```


### Code 5
```
SBC r11, pc, #0x2F40
MOVS r12, #0x328AA001 ?
STR r12, [r11, #0xDB]!
MOVS r12, #0x23A0A000 ?
0xE7ABCCAE
MOVS r12, #0x22899001 ?
0xE7ABCCAE
```

Writes:
```
328AA001 @ 0x34+0xA7
23A0A000
22899001
```


### Code 6
```
SBC r11, pc, #0x2F40
MOVS r12, #0xE2899001 ?
STR r12, [r11, #0xE7]!
MOVS r12, #0xE359007E ?
0xE7ABCCAE
MOVS r12, #0x424FF040 ?
0xE7ABCCAE
```

Writes:
```
E2899001 @ 0x40+0xA7
E359007E
424FF040
```


### Code 7
```
SBC r11, pc, #0x2F00
MVN r12, #0xEE00000
SBC r12, #0xFF00000
SBC r12, #0xED ; Change to #0xDF if you want to exit via `BX lr`, make sure to zero out `r0` before this!
STR r12, [r11, #0xB3]!
```

Writes:
```
E12FFF10 @ (0x4C+0xA7) - 0x40
```

## References and Acknowledgements
- [E-Sh4rk's original article for the hexwriter](https://e-sh4rk.github.io/ACE3/emerald/hex-writer/hex-writer/)
- [Adrichu00's method of writing the hexwriter](https://gist.github.com/Adrichu00/49433953af9d6fd7c1cd368d48c68778)
- RationalPsycho on the Glitch City Research Institute Discord for the glitched mail inputs
- merrp on the Glitch City Research Institute Discord for the `STR+4` opcode used in the codes.
