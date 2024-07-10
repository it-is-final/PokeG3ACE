 All Thumb codes (unless stated other wise) use Box 9, Slot 27. All hexcode is written in big endian order.

## Change Nickname

This code does not call the nickname screen which allows renaming of Glitch Pokemon with problematic species names.

Replace * with wanted name
To terminate name early, simply press start to skip the rest of the slots.
Chars 0-7 are in Box 5, Chars 8-9 are in Box 4

```text
Box  1: ル ば か ぶ け は き ぶ	[ルばかぶけはきぶ]
Box  2: _ く タ か ぶ _ l _	[ くタかぶ l ]
Box  3: ぶ タ い ぶ く ゥ ミ び	[ぶタいぶくゥミび]
Box  4: _ ふ ぃ _ _ * *	[ ふぃ  **]
Box  5: * * * * * * * *		[********]
```

```arm-asm
MOV r1, pc
LDR r0, [pc, #0x24] ; r0 = 0x301C
SUB r1, r1, r0 ; r1 - r0 = address of Box 9,27 + 8
LDR r0, [pc, #0x28] ; r0=a
FILL 0x00FF, 2
STR r0, [r1] ; Sets chars 0-3
LDR r0, [pc, #0x24] ; r0=b
B #0x4 @ E000 ; Skip bad filler
FILL 0xFFFF, 2 ; bad filler (skipped)
STR r0, [r1, #0x4] ; Sets chars 4-7
LDR r0, [pc, #0x8] ; r0=0xFF000000+c
STRH r0, [r1, #0x8] ; Sets chars 8-9
BX LR
FILL 0x00FF, 2
; 0x0000301C
; c ; chars 8-9
FILL 0xFF00, 2
; a ; chars 0-3
; b ; chars 4-7

; Corresponding Hexcode
; 46 79 mov r1, pc
; 48 06 ldr r0, [pc, #0x24]
; 1A 09 sub r1, r1, r0
; 48 07 ldr r0, [pc, #0x28]
; 00 FF
; 60 08 str r0, [r1] ; Sets chars 0-3
; 48 06 ldr r0, [pc, #0x24] ; r0=b
; E0 00 b #0x4
; FF FF
; 60 48 str r0, [r1, #0x4]
; 48 02 ldr r0, [pc, #0x8]
; 81 08 strh r0, [r1, #0x8]
; 47 70 bx lr
; 00 FF
; 00 00 30 1C
; FF 00 XX XX
; XX XX XX XX
; XX XX XX XX
```

## Create EGG from Nothing

```text
Box  1: ル ば す ぶ け は こ ぶ	[ルばすぶけはこぶ]
Box  2: ア き ぼ ィ ね _ l	[アきぼィね l]
Box  3: か め ぼ ミ N ゥ け ぼ	[かめぼミNゥけぼ]
Box  4: ア こ ガ ィ ね _ l	[アこガィね l]
Box  5: ぶ ゥ ミ び $ $ _ _	[ぶゥミび$$  ]
Box  6: ア ア ア ￥ ￥ _ _	[アアア￥￥  ]
Box  7: ア ア つ ぃ _ _	[アアつぃ  ]
Box  8: ア _ ぞ _ _	[ア ぞ  ]
```

```arm-asm
mov r1, pc
ldr r0,[pc,52]
subs r1,r1,r0 ; Set r1 to address of Box 9, Slot 27
ldr r0,[pc, 40] ; Load YYyy
ldr r2,[pc, 28] ; Load ZZzz
adds r0,r0,r2 ; Calculate species number
b 4
movs r2, 0x6 ; isEgg = true, isSpecies = true
strb r2,[r1,1] ; Store isEgg and isSpecies flag
strh r0,[r1,0xE] ; Store species
ldr r2, [pc,36] ; Load substructure egg flag
strh r2, [r1,56] ; Store egg flag in substructure
b 4
adds r0, r0, r2 ; (species + 0x4000) = final checksum
strh r0,[r1,0xA] ; store final checksum, ignore upper 16 bits of final checksum
bx lr
```

$ = (ZZ)(zz)
￥  = (YY)(yy)

## Port of 'Change PRNG seed and freeze' code

```text
Box  1: く ぶ か む あ タ く ぶ	[くぶかむあタくぶ]
Box  2: _ い む あ ミ _ l	[ いむあミ l]
Box  3: き ぶ く べ こ ぼ グ ね	[きぶくべこぼグね]
; Use べ from the blue layer
Box  4: _ あ タ ミ び	[ あタミび]
Box  5: ゾ わ い い ベ ら _ う	[ゾわいいベら う]
; Use べ from the red layer
Box  6: _ _ _ l コ _ う _	[   lコ う ]
	Box  7: ア ア * ° § @ _ _	[アア*°§@  ]
index of *=VV; index of °=vv; index of §=UU; index of @=uu
Box  8: ア * ° § @ _ _ _	[ア*°§@   ]
index of *=ZZ; index of °=zz; index of §=WW; index of @=ww
```

```arm-asm
LDR r0, [pc, #0x18] ; r0 = gBattleTypeFlags (0x02022c90)
MOV r1, #0x6 ; bit 24,21,20,19,18,17,16 or 1 (LE) of gBattleTypeFlags must be activated
STR r1, [r0]
LDR r0 [pc, #0x20] ; r0 = inBattle (0x03002799)
FILL 0x00FF, 2
MOV r0, #0x2 ; bit 1 of inBattle must be activated (but preferably not bit 0 and 2)
STRB r1, [r0]
B #0x4
FILL 0xFFFF, 2
LDR r0, [pc, #0x1C] ; r0 = PRNG state (0x03005AE0)
LDR r1, [pc, #0x20] ; r1 = uuUUvvVV
LDR r2, [pc, #0x28] ; r2 = wwWWzzZZ
ADD r1, r1, r2 ; r1 + r2 = xxXXyyYY
FILL 0x00FF, 2
STR r1, [r0] ; 6001
BX LR ; 4770
FILL 0xFFFFFFFF, 4
; 0x02022c90
; 0x03002799
FILL 0x000000FF, 4
; 0x03005AE0
FILL 0x5151FF00, 4
; uuUUvvVV
FILL 0x51FF0000, 4
; wwWWzzZZ

; Corresponding Hexcode
; 48 08 LDR r0, [pc, #0x18]
; 21 06 MOV r1, #0x6
; 60 01 STR r1, [r0]
; 48 08 LDR r0 [pc, #0x20]
; 00 FF
; 21 02 MOV r0, #0x2
; 70 01 STRB r1, [r0]
; E0 00 B #0x4
; FF FF
; 48 07 LDR r0, [pc, #0x1C]
; 49 08 LDR r1, [pc, #0x20]
; 4A 0A LDR r2, [pc, #0x28]
; 18 89 ADD r1, r1, r2
; 00 FF
; 60 01 STR r1, [r0]
; 47 70 BX LR
; FF FF FF FF
; 02 02 2C 90
; 03 00 27 99
; 00 00 00 FF
; 03 00 5A E0
; 51 51 FF 00
; XX XX XX XX
; 51 FF 00 00
; XX XX XX XX
```

## Complex Nicknames
After discovering STMIA and LDMIA can probably reduce the number of opcodes for storing and loading, I tried it out with this code which is horribly bloated. I got this cursed piece of Thumb code to show for it.

```text
Box  1: け ッ く べ だ は ふ N	[けッくべだはふN]
Box  2: _ つ の リ N _ l	[ つのリN l]
Box  3: 3 の と G ふ N ひ の	[3のとGふNひの]
Box  4: _ さ ィ ミ び	[ さィミび]
Box  5: ぞ ぃ _ _ * * * *	[ぞぃ  ****]
Box  6: _ _ _ + + + + _	[   $$$$ ]
Box  7: _ _ * * * * _ _	[  ****  ]
Box  8: _ + + + + _ _ _	[ $$$$   ]
Box  9: * * _ あ + + _ あ	[** あ$$ あ]
```

```arm-asm
ADD r0, pc, #0x24
LDR r1, [pc, #0x20] ; r1 = 0x3040
SUB r1, r0, r1 ; r1 = Box 9, Slot 27
LDMIA r0!, {r2, r3, r4} ; Load first four characters of nickname
FILL 0x00FF, 2
ADD r2, r2, r4
LDMIA r0!, {r3, r4, r5, r6} ; Load next four characters of nickname
B #4
FILL 0xFFFF, 2
ADD r4, r4, r6
STMIA r1!, {r2, r4} ; Store first 8 characters of nickname
LDMIA r0!, {r2, r3, r4} ; Load next two characters of nickname
ADD r3, r3, r4
FILL 0x00FF, 2
STRH r3, [r1]
BX LR

; Corresponding Hexcode
; A0 09
; 49 08
; 1A 41
; C8 1C
; 00 FF
; 19 12
; C8 78
; E0 00
; FF FF
; 19 A4
; C1 14
; C8 1C
; 19 1B
; 00 FF
; 80 0B
; 47 70
; FF FF FF FF
; 00 00 XX XX
; XX XX XX XX
; 51 51 51 FF
; XX XX XX XX
; 51 51 FF 00
; XX XX XX XX
; 51 FF 00 00
; XX XX XX XX
; FF 00 00 00
; 01 00 XX XX
; 01 00 XX XX
```

## Create NOP Bad Egg

```
Box  1: ル ば さ ぶ け は か ッ	[ルばさぶけはかッ]
Box  2: _ え 」 お ぼ _ l	[ え」おぼ l]
Box  3: さ k え B え ぶ ぶ ェ	[さkえBえぶぶェ]
Box  4: _ か ぶ _ び F ば	[ かぶ びFば]
Box  5: り _ _ あ _ c _ _	[り  あ c  ]
Box  6: _ _ _ ャ ゆ _ _ _	[   ャゆ   ]
Box  7: _ _ ゆ ヲ て く _ _	[  ゆヲてく  ]
```

```
MOV r1, pc
LDR r0, =0x2584 @ pc, #0x2C
SUB r1, r1, r0 ; r1-r0 = Box 11, Slot 1
ADD r0, pc, #0x18
PUSH {r2}
LDR r2, =0x01000028 @ pc, #0x14 ; Setting up parameters for SWI
B pc
SWI #0xB ; Call CpuSet with parameters described in r0, r1, r2
POP {r2}
LDR r0, =0xD700 @ pc, #0x10
STRH r0, [r1, #0x12] ; Replace potentially dangerous 47C0 opcode with D700 in misc/lang flags
LDR r0, =0x08137D25 @ pc, #0x18
BX r0 ; Uses certifcate exit to ensure a safe Bad EGG is created (no 50/50 chance of D700 being missing)
.halfword 0x49C0 ; Informal NOP, means MOV r8, r8
.word 0x01000028 ; Fill address in r1 with halfword described in r0 for 0x28 words
.word 0x0000D700 ; BVC pc, safest opcode I can think of that does not corrupt anything
.word 0x00002584
.word 0x08137D25

; 4679 MOV r1, pc
; 480B LDR r0, [pc, #0x2C]
; 1A09 SUB r1, r1, r0
; A006 ADD r0, pc, #0x18
; 00FF
; B404 PUSH {r2}
; 4A05 LDR r2, [pc, #0x14]
; E000 B pc
; FFFF
; DF0B SWI #0xB
; BC04 POP {r2}
; 4804 LDR r0, [pc, #0x10]
; 8248 STRH r0, [r1, #0x12]
; 00FF
; 4806 LDR r0, [pc, #0x18]
; 4700 BX r0
; 46C0
; FFFF
; 0028
; 0100
; D700
; 0000
; 00FF
; 0000
; 2584
; 0000
; FF00
; 0000
; 7D25
; 0813
```
