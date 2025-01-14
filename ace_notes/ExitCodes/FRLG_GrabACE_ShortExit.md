# Write `BX lr` to Box 14
This code enables the usage of longer box name codes through writing opcode `BX lr` to Box 14.
Codes making use of this version of the Box 14 setup do not require the use of an additional exit code bootstrap.

1. Write the following box names:
    ```
    Box  1: z ♀ l o k … Q n	[z♀lok…Qn]
    Box  2: ♀ Q n n U U n _	[♀QnnUUn ]
    Box  3: _ _ y ‘ ? q _ _	[  y‘?q  ]
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
    Box 14: _ F o _ _ _ _ _	[ Fo     ]
    ```
2. Execute the code

Control of the game should have been returned to you after execution, and Box 14 should now be named ` Foì`.
If control of the game has not been returned, that means you wrote the name of Box 14 wrong.
If the game crashes, make sure that you have written the code correctly, and that there are no invisible Pokémon in the execution area of your grab ACE Pokemon.

## Exiting for more complex payloads
For more complex payloads the must exit before the box names, use the exit code bootstrap [here](GrabACEBootstrap.md).

## Explanation
This code writes the grab ACE exit code to the name of box 14.
The grab ACE exit is composed of two parts, one that clears at least part of `r0` and a branch to the return address stored `LR`.

Shifting two box Pokemon is considered a task by the game which seems to store its status in `r0`.
By clearing at least the least significant byte of `r0`, a task finish is signalled which will be handled when the processor branches to the return address.
If a task is not signalled as ‘finished’, the code at the return address will eventually branch back into the glitched task callback, causing the game to appear softlocked.
Signalling this will skip the branch back into the glitched callback and allow the shift Pokémon task to finish properly.

The box 14 exit code is composed of these two instructions:
- `BIC r0, r0, #0xFF` (`($FF)␣Fo`) clears part of `r0`, specifically its least significant byte.
- `BX lr` (`ì`) performs a branch to the return address.

As the essential parts of the exit code is present in box 14’s name, no extra bootstrap is needed for box name codes to exit properly.

Older versions of the box 14 exit code used either another Pokémon with code that cleared `r0` or have box name codes place an instruction that cleared `r0` at the end, as `($FF)␣Fo` was not written in box 14 for those exit codes.

However more complex payloads that need to exit before the `PC` reaches the box names cannot use this box 14 exit code, thus requiring an exit code bootstrap of some kind to be able to exit properly.

## Acknowledgements
- E-Sh4rk for creating the [CodeGenerator](https://e-sh4rk.github.io/CodeGenerator)
- Sleipnir17 for creating the [short exit code setup code](https://e-sh4rk.github.io/EmeraldACE_web/doc/FRLG_Short_Exit_Codes_Guide.pdf) which this code is derived from
- merrp for the [Map Warp code](https://www.youtube.com/watch?v=yVhK4pLC9ac) which inspired the improvement to this code.
