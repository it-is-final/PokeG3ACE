/*
 * Thumb Hexwriter
 * r0 → exit routine
 * r1 → start of box names
 * r2 → box char
 * r3 → destination address
 * r4 → box char count
 * r5 → nibble count
 * r6 → accumulator 
 * r7 → byte count
 */

PUSH {r2-r7}
ADD r1, pc, #0x90
LDR r3, =0x2029000 ; @ pc + 0x38
CMP r12, r3
BCS pc + #0x2
LDR r3, =0x20242** ; party slot 3 @ pc + 0x30, 58 for Emerald, AC for FRLG
B pc + #0x0
MOV r3, r12
LDMIA r1!, {r4-r6} ; set r4, r5, r6 to be 0
BVC pc - #0x2 ; filler
LDRB r2, [r1, r4]
CMP r2, #0xFF
BEQ pc + #0x18
SUB r2, #0xB1
BCS pc + #0x0
ADD r2, #0x10
BPL pc + #0x0
LDRB r6, [r3, r7]
BMI pc + #0x2
LSL r6, r6, #0x4
ADD r6, r6, r2
LSR r7, r5, #0x1 ; Achieves similar effect to TST, if bit 0 is set, then carry gets set
BCC pc + #0x0 ; Skip store byte if bit 0 is not set
STRB r6, [r3, r7] ; previous LSR divides by 2, so r7 can be used
ADD r5, #0x1
ADD r4, #0x1
CMP r4, #0x7E
BMI pc - #0x26
POP {r2-r7}
BX r0