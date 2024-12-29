# Write `BX lr` to Box 14
This code enables the usage of longer box name codes through writing opcode `BX lr` to Box 14.
Codes making use of this version of the Box 14 setup do not require the use of an additional exit code bootstrap.

1. Write the following box names:
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
2. Execute the code

Control of the game should have been returned to you after execution, and Box 14 should now be named ` Foì`.
If control of the game has not been returned, that means you wrote the name of Box 14 wrong.
If the game crashes, make sure that you have written the code correctly, and that there are no invisible Pokemon in the execution area of your grab ACE Pokemon.

## Exiting for more complex payloads
For more complex payloads the must exit before the box names, use the exit code bootstrap [here](ace_notes/ExitCodes/GrabACEBootstrap.md).

## Explanation
The Box 14 name consists of two opcodes, they are the aforementioned `BX lr` and `BIC r0, r0, #0xFF`.

`BIC r0, r0, #0xFF` which is encoded as `✖_Fo` in the character set, with `✖` representing the string terminator.
This clears the lower 8 bits of `r0` which tells the game that the current task (in this case shifting Pokemon) has ended, otherwise the game will be stuck waiting for the signal that the task ended, and control never returned back to the player.
Older versions of this code did not use this opcode, instead using `ADCLT r12, r0, #0xFF` (`✖_?”`) which does nothing, and also forces code authors using the older setup to either append `MOVS r0, r0, #0x0` as the very last opcode before Box 14 or make users create a bootstrap that zeroes out `r0`

`BX lr` jumps the `pc` (program counter) back into the game's code handling the remainder of the shifting task.

## Acknowledgements
- E-Sh4rk for creating the [CodeGenerator](https://e-sh4rk.github.io/CodeGenerator)
- Sleipnir17 for creating the [short exit code setup code](https://e-sh4rk.github.io/EmeraldACE_web/doc/FRLG_Short_Exit_Codes_Guide.pdf) which this code is derived from
- merrp for the [Map Warp code](https://www.youtube.com/watch?v=yVhK4pLC9ac) which inspired the improvement to this code.