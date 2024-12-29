# Exit Code Bootstrap for FRLG grab ACE
The purpose of this bootstrap is to allow more complex ACE payloads such as the hexwriter, and the hexecutor to be able to exit out of execution and hand back control to the game.

## Prequisites
- Box 14 must have a `BX lr` opcode written to it, it should be named ` Foì`
    - Refer to the 'Restoring `BX lr` box name' section of this guide to get this box name.

## How to create
1. Write the following box names:
    ```
    Box  1: 4 . U n s K … o	[4.UnsK…o]
    Box  2: … … o v I ? n _	[……ovI?n ]
    Box  3: ? ” U N ? n _ _	[?”UN?n  ]
    Box  4: E _ F 9 q _ _ _	[E F9q   ]
    Box  5: F 2 9 n 7 K … o	[F29n7K…o]
    Box  6: H ? n V J ? n _	[H?nVJ?n ]
    Box  7: ? ” … “ P m _ _	[?”…“Pm  ]
    Box  8: E ’ “ P m _ _ _	[E’“Pm   ]
    Box  9: _ F 9 q , F f l	[ F9q,Ffl]
    Box 10: _ ? ” g K … o _	[ ?”gK…o ]
    Box 11: ? ” m H ? n _ _	[?”mH?n  ]
    Box 12: E i O ? n _ _ _	[EiO?n   ]
    Box 13: N G ? n _ F 9 q	[NG?n F9q]
    ```
2. Execute the code
    - This code should create a ? in Box 10, Slot 19
    - It should be named `Â  nÔ  v  `, and its OT should be blank

## Testing the bootstrap
1. Move the bootstrap to Box 13, Slot 9 or later
2. Write the following box names:
    ```
    Box  1: _ _ _ … _ _ _ _	[   …    ]
    Box  2: _ ? ” _ _ _ _ O	[ ?”    O]
    Box  3: … o	[…o]
    ```
    - `MOVS pc, #0x324` executes a `BX r0` instruction located somewhere in the BIOS
3. Execute the code
4. If it does not crash, that means the bootstrap is working

> [!IMPORTANT]
> This Pokemon does not have its hasSpecies flag set.
> Do not use group selection on this Pokemon, it will disappear!

## How to utilise the bootstrap
- Payloads that utilise the bootstrap must either never write to `r0`, or store the value of `r0` somewhere else (like another register) then write the value back to `r0` before exiting.
- Payloads should exit with `BX r0` which jumps to the code contained in the bootstrap which handles the exiting for you

## Restoring `BX lr` box name
In the rare case that you need to rename Box 14, here is the code to restore the `BX lr` name back:
```
Box  1: z ♀ l o k … Q n	[z♀lok…Qn]
Box  2: ♀ Q n n U U n _	[♀QnnUUn ]
Box  3: ? ” y ‘ ? q _ _	[?”y‘?q  ]
Box  4: E _ _ _ _ _ _ _	[E       ]
Box  5: _ _ _ … _ _ _ _	[   …    ]
Box  6: _ ? ” _ _ _ _ _	[ ?”     ]
Box  7: ? ” _ _ _ _ _ _	[?”      ]
Box  8: E _ _ _ _ _ _ _	[E       ]
Box  9: _ _ _ … _ _ _ _	[   …    ]
Box 10: _ ? ” _ _ _ _ _	[ ?”     ]
Box 11: ? ” _ _ _ _ _ _	[?”      ]
Box 12: E _ _ _ _ _ _ _	[E       ]
Box 13: _ _ _ … _ _ _ _	[   …    ]
Box 14: _ F o _ _ _ _ _	[ Fo     ]
```
More details on how it works can be found [here](FRLG_GrabACE_ShortExit.md).

## How it works
The nickname is the first bit of actual code to be executed in the bootstrap, the bytes correspond to the following opcodes:
```
E28F0003 ADD r0, pc, #0x3 ; sets bit 0 to 1 which will make `BX r0` execute this address in Thumb mode
EA00000F B #0x44
```

This stores the address of the bootstrap's OT in `r0` then jumps to the next box slot.
The OT contains Thumb code, the bytes of the OT correspond to the following opcodes:
```
4040 EOR r0, r0 ; zeroes out r0, tells game to the end the task of swapping
46F7 MOV pc, lr ; returns control to the game's code
```
This does the routine of handing control back to the game in a safe manner.

## CodeGenerator input
```
@@ filler1 = 0xB2AC00FF
@@ filler2 = 0xB2ACFF00
@@ filler3 = 0xBFFF0000
@@ exit = "Bootstrapped"
@@
SBC r10, pc, #0x2940 ; r11 = Box 10, Slot 19 + 9
MOVS r12, #0x39C00000
MOVS r11, #0xFF ; species = 0xFF
ADC r12, r12, #0xA8000003
ADC r12, r12, #0xCF0000 ; E28F0003 ADD r0, pc, #0x3
STR r12, [r10]! ; Store in characters 0-3 of nickname
ADC r10, r10, #0x3 ; r11 = Box 10, Slot 19 + 12
MOVS r12, #0x2A000000
ADC r12, #0xF000000F
ADC r12, #0xD0000000 ; EA00000F B #0xFF
; EA00000F & 0xFFFF = 0xF = Beedrill
STRH r11, [r10, #0x10] ; Store checksum
STRH r11, [r10, #0x14] ; Store species
STR r12, [r10]! ; Store in characters 4-7 of nickname
LDRH r12, [r10], #0x8 ; r11 = Box 10, Slot 19 + 20
; 4040 EOR r0, r0
; 46F7 MOV pc, lr
MOVS r12, #0x46F74040 ?
STR r12, [r10]! ; Store in OT characters 0-3
```

## Acknowledgements
- E-Sh4rk for creating the CodeGenerator, the `Create Pokemon from nothing (with exit code bootstrap)` code, and the `Certificate Exit Bootstrap` code which the exit code bootstrap codes is based off
- Sleipnir17 for creating the short exit code setup code which this code is derived from
- RETIRE for providing better methods to construct the Thumb code