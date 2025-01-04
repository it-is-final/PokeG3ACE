# Exit Code Bootstrap for Japanese FRLG grab ACE

The purpose of this bootstrap is to provide more complex ACE payloads with a way to exit safely and hand back control to the game.

## Prequisites
- Prior knowledge on activating grab ACE

## How to create

1. Write the following box names
    ```
    Box  1: か ぶ く 0 ほ O ほ F	[かぶく0ほOほF]
    Box  2: む こ ふ え ぃ _ l	[むこふえぃ l]
    Box  3: か F ぞ ぞ _ C _ _	[かFぞぞ C  ]
    Box  4: _ 」 ぢ い い _ _ _	[ 」ぢいい   ]
    Box  5: い ッ あ ぃ み l _ _	[いッあぃみl  ]
    Box  6: _ あ い ぞ ぞ _ C _	[ あいぞぞ C ]
    ```
2. Execute ACE

A `?` should appear in party slot 3 with the nickname of `いッあぃみ` and its OT should be `ぞぞ C`.
That should be your exit code bootstrap, move it to Box 14, Slot 1.

## Testing the bootstrap

1. Write the following box names
    ```
    Box  1: _ び _ _ _ _ _ _	[ び      ]
    ```
2. Execute ACE

If the game did not crash, that means the bootstrap is working properly.