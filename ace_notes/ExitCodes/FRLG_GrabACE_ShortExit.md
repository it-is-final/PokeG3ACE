# Grab ACE Box 14 Exit Code
This exit code enables the usage of longer box name codes through writing the grab ACE exit code to box 14.
Box name codes making use of this version of the Box 14 exit code do not require the use of an additional exit code bootstrap.

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

Box 14 should be named `␣Foì`.

If the game crashes or softlocks it may have been caused by the following:
- Box names are written wrong
- There are Pokémon (visible or not) after the entrypoint of your glitch Pokémon (for $351, it is Box 13, Slot 8)
    - Move them to a box slot before the entrypoint
    - For invisible Pokémon: use group selection or move them before the entrypoint if they do not disappear

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
