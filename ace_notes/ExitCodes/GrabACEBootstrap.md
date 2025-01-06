# Exit Code Bootstrap for FRLG grab ACE
The purpose of this bootstrap is to allow more complex ACE payloads such as the hexwriter, and the hexecutor to be able to exit out of execution and hand back control to the game.

## Prequisites
- Prior knowledge on activating mail corruption
- Prior knowledge on activating grab ACE

## How to create
### Method 1: Catch Random Pokemon
1. Catch any Pokemon and name it `␣␣␣C`
2. Place this Pokemon in Box 3, Slot 1
3. Write a glitched mail with the following contents:
    - Mail word 1 → GOTCHA
    - Mail word 2 → MARVEL SCALE
    - Mail word 3 → RUBY
    - Mail word 4 → I CHOOSE YOU
    - Mail word 5 → WANDERING
    - All other words should be left untouched
4. After writing the glitched mail, the Pokemon should have turned into a bad EGG, move this to Box 10, Slot 2
3. Write the following box names:
    ```
    Box  1: C . U n n F … o	[C.UnnF…o]
    Box  2: … l o 7 … P q _	[…lo7…Pq ]
    Box  3: _ _ 9 F P q _ _	[  9FPq  ]
    Box  4: _ ? … P q _ _ _	[ ?…Pq   ]
    Box  5: z ♀ l o k … Q n	[z♀lok…Qn]
    Box  6: ♀ Q n v F … o _	[♀QnvF…o ]
    Box  7: _ _ – F P q _ _	[  –FPq  ]
    Box  8: _ F G E n _ _ _	[ FGEn   ]
    Box  9: _ … ? q _ _ _ _	[ …?q    ]
    Box 10: _ _ _ _ _ _ … _	[      … ]
    Box 11: _ _ _ _ _ … _ _	[     …  ]
    Box 12: _ _ _ _ … _ _ _	[    …   ]
    Box 13: _ _ _ … _ _ _ _	[   …    ]
    Box 14: _ F o _ _ _ _ _	[ Fo     ]
    ```
4. Execute the code.

Box 14 should now be named `␣Foì` and the bad egg in Box 10, Slot 2 is now the exit code bootstrap.
To confirm, place the bad EGG in Box 3, Slot 1, and activate the mail glitch, the contents should be:
 ```
 ??? ???
 ??? ???
 WANDERING ???
 _______ _______
 _______
 ```

### Method 2: Empty Slot
1. Make sure Box 3, Slot 1 is empty, then write the following message to the glitched mail:
    - Mail word 1 → GOTCHA
    - Mail word 2 → MARVEL SCALE
    - Mail word 3 → RUBY
    - Mail word 5 → WANDERING 
    - All other words should be left untouched
2. A bad EGG should appear in Box 3, Slot 1, move it to Box 10, Slot 2 without using group selection.
3. Write the following box names:
    ```
    Box  1: C . U n n F … o	[C.UnnF…o]
    Box  2: … l o 7 … P q _	[…lo7…Pq ]
    Box  3: _ _ 9 F P q _ _	[  9FPq  ]
    Box  4: _ ? … P q _ _ _	[ ?…Pq   ]
    Box  5: v F … o – F P q	[vF…o–FPq]
    Box  6: _ _ _ / F P q _	[   /FPq ]
    Box  7: _ _ C F … o _ _	[  CF…o  ]
    Box  8: _ ” F P q _ _ _	[ ”FPq   ]
    Box  9: z ♀ l o k … Q n	[z♀lok…Qn]
    Box 10: ♀ Q n F F U n _	[♀QnFFUn ]
    Box 11: _ _ g … ? q _ _	[  g…?q  ]
    Box 12: _ _ _ _ … _ _ _	[    …   ]
    Box 13: _ _ _ … _ _ _ _	[   …    ]
    Box 14: _ F o _ _ _ _ _	[ Fo     ]
    ```
4. Execute the code.

Box 14 should now be named `␣Foì` and the bad egg in Box 10, Slot 2 is now the exit code bootstrap.
To confirm, place the bad EGG in Box 3, Slot 1, and activate the mail glitch, the contents should be:
```
??? ???
??? ???
WANDERING ???
??? ???
???
```

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
Through both mail corruption and that box name code we wrote, we have corrupted the PID/OTID of the Pokemon to become the following opcodes:
```
E24F0001 SUB r0, pc, #0x1
EA000011 B #0x4C
```

This stores the address of the bootstrap's nickname in `r0` then jumps to the next box slot.
Since bit 0 of `r0` is set to 1, that means that when the `BX r0` instruction is executed, the code in the nickname is run in Thumb mode.
From mail corruption, and the specific nickname we gave the Pokemon earlier, the nickname becomes the following Thumb opcodes:
```
2000 MOV r0, #0x0 ; zeroes out r0, tells game to the end the task of swapping
BD00 POP pc ; returns control to the game's code
```
This does the routine of handing control back to the game in a safe manner.

## Technical details
### Method 1
The nickname `␣␣␣C` populates the partial nickname with a Thumb opcode `POP pc` (`BD00`), this reduces the need to write out the payload via grab ACE.

The mail words have the following indexes:
|Word|Index (hex)|
|-|-|
|GOTCHA|201|
|MARVEL SCALE|44F|
|RUBY|211|
|I CHOOSE YOU|200|
|WANDERING|2000|

'WANDERING' forms the other half of our Thumb payload that `BX r0` will jump into, where its index perfectly matches with `MOV r0, #0x0`.
The rest of the words will partially form each ARM opcode that constitutes the PID/OTID with their most significant bytes being overwritten by the box name code.

Below is the input fed into E-Sh4rk's CodeGenerator to produce the box name code
```
@@
SBC r10, pc, #0x2F40 ; Box 10, Slot 2 - 0xA7
MOVS r12, #0xE2
MVN r11, #0xFF ; the least significant byte of r11 is 0
STRB r11, [r10, #0xA8]
STRB r12, [r10, #0xAA]
STRB r11, [r10, #0xAC]
MVN r11, #0xEE00000
SBC r11, #0xDF
SBC r11, #0xFF00000 ; r11 = E12FFF1E BX lr
MOVS r12, #0xEA
STRB r12, [r10, #0xAE]
ADCS r12, pc, #0x30 ; r12 = address of box 14 name
STR r11, [r12]! ; Store BX lr opcode in Box 14 name
0
0
0
0
0
0
BIC r0, r0, #0xFF
```

### Method 2
The explanation for the mail words will not be repeated here as its largely the same as method 1, with only the omission of mail word 4 as the difference.
This omission is because the empty box slot is all just 0 meaning we do not need to fill in a word for mail word 4 as that just places a 0, and its upper byte is getting overwritten anyway.

The box name code writes `0xBD` to the upper byte of the second halfword of the nickname to account for the lack of a nickname to do that for us, and also manually set the hasSpecies flag for that slot since it started off as technically 'no Pokemon'.

Below is the CodeGenerator input:
```
@@
SBC r10, pc, #0x2F40 ; Box 10, Slot 2 - 0xA7
MOVS r12, #0xE2
MVN r11, #0xFF ; the least significant byte of r11 is 0
STRB r11, [r10, #0xA8]
STRB r12, [r10, #0xAA]
STRB r11, [r10, #0xAC]
MOVS r12, #0xEA
STRB r12, [r10, #0xAE]
STRB r12, [r10, #0xBA] ; Sets hasSpecies
MOVS r12, #0xBD
STRB r12, [r10, #0xB2]
MVN r11, #0xEE00000
SBC r11, #0xDF
SBC r11, #0xFF00000 ; r11 = E12FFF1E BX lr
SBC r12, pc, #0xC0 ; r12 = address of box 14 name
STR r11, [r12, #0xDB]! ; Store BX lr opcode in Box 14 name
0
0
BIC r0, r0, #0xFF
```

## Acknowledgements
- E-Sh4rk for creating the CodeGenerator, the `Create Pokemon from nothing (with exit code bootstrap)` code, and the `Certificate Exit Bootstrap` code which the exit code bootstrap codes is based off
- Sleipnir17 for creating the short exit code setup code which this code is derived from
- RETIRE for providing better methods to construct the Thumb code
- RationalPsycho on the Glitch City Research Institute for suggesting the use of mail to simplify the writing process
