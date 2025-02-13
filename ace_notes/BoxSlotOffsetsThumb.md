# Box slot offsets
Since Thumb cannot substract an offset from the `pc` in one opcode, this document simply lists every box slot with their offsets without regard for whether they are actually writable in the character set.
Thumb codes either write to a party slot where they are unaffected by ASLR or do the following sequence of opcodes (note that `r0` and `r1` can be substituted for other registers but they are used most in Sleipnir17's codes)
```
MOV r1, pc ; can be substituted with ADD r1, pc, #0x0
LDR r0, [pc, #nn] ; loads the offset into r0
SUB r1, r1, r0
```
All of these offsets all land on the first byte of the PID given that `MOV r1, pc` or `ADD r1, pc, #0x0` is the very first instruction in the box name code.

|   Box |   Slot | Offset   |
|-------|--------|----------|
|     1 |      1 | 0x8344   |
|     1 |      2 | 0x82F4   |
|     1 |      3 | 0x82A4   |
|     1 |      4 | 0x8254   |
|     1 |      5 | 0x8204   |
|     1 |      6 | 0x81B4   |
|     1 |      7 | 0x8164   |
|     1 |      8 | 0x8114   |
|     1 |      9 | 0x80C4   |
|     1 |     10 | 0x8074   |
|     1 |     11 | 0x8024   |
|     1 |     12 | 0x7FD4   |
|     1 |     13 | 0x7F84   |
|     1 |     14 | 0x7F34   |
|     1 |     15 | 0x7EE4   |
|     1 |     16 | 0x7E94   |
|     1 |     17 | 0x7E44   |
|     1 |     18 | 0x7DF4   |
|     1 |     19 | 0x7DA4   |
|     1 |     20 | 0x7D54   |
|     1 |     21 | 0x7D04   |
|     1 |     22 | 0x7CB4   |
|     1 |     23 | 0x7C64   |
|     1 |     24 | 0x7C14   |
|     1 |     25 | 0x7BC4   |
|     1 |     26 | 0x7B74   |
|     1 |     27 | 0x7B24   |
|     1 |     28 | 0x7AD4   |
|     1 |     29 | 0x7A84   |
|     1 |     30 | 0x7A34   |
|     2 |      1 | 0x79E4   |
|     2 |      2 | 0x7994   |
|     2 |      3 | 0x7944   |
|     2 |      4 | 0x78F4   |
|     2 |      5 | 0x78A4   |
|     2 |      6 | 0x7854   |
|     2 |      7 | 0x7804   |
|     2 |      8 | 0x77B4   |
|     2 |      9 | 0x7764   |
|     2 |     10 | 0x7714   |
|     2 |     11 | 0x76C4   |
|     2 |     12 | 0x7674   |
|     2 |     13 | 0x7624   |
|     2 |     14 | 0x75D4   |
|     2 |     15 | 0x7584   |
|     2 |     16 | 0x7534   |
|     2 |     17 | 0x74E4   |
|     2 |     18 | 0x7494   |
|     2 |     19 | 0x7444   |
|     2 |     20 | 0x73F4   |
|     2 |     21 | 0x73A4   |
|     2 |     22 | 0x7354   |
|     2 |     23 | 0x7304   |
|     2 |     24 | 0x72B4   |
|     2 |     25 | 0x7264   |
|     2 |     26 | 0x7214   |
|     2 |     27 | 0x71C4   |
|     2 |     28 | 0x7174   |
|     2 |     29 | 0x7124   |
|     2 |     30 | 0x70D4   |
|     3 |      1 | 0x7084   |
|     3 |      2 | 0x7034   |
|     3 |      3 | 0x6FE4   |
|     3 |      4 | 0x6F94   |
|     3 |      5 | 0x6F44   |
|     3 |      6 | 0x6EF4   |
|     3 |      7 | 0x6EA4   |
|     3 |      8 | 0x6E54   |
|     3 |      9 | 0x6E04   |
|     3 |     10 | 0x6DB4   |
|     3 |     11 | 0x6D64   |
|     3 |     12 | 0x6D14   |
|     3 |     13 | 0x6CC4   |
|     3 |     14 | 0x6C74   |
|     3 |     15 | 0x6C24   |
|     3 |     16 | 0x6BD4   |
|     3 |     17 | 0x6B84   |
|     3 |     18 | 0x6B34   |
|     3 |     19 | 0x6AE4   |
|     3 |     20 | 0x6A94   |
|     3 |     21 | 0x6A44   |
|     3 |     22 | 0x69F4   |
|     3 |     23 | 0x69A4   |
|     3 |     24 | 0x6954   |
|     3 |     25 | 0x6904   |
|     3 |     26 | 0x68B4   |
|     3 |     27 | 0x6864   |
|     3 |     28 | 0x6814   |
|     3 |     29 | 0x67C4   |
|     3 |     30 | 0x6774   |
|     4 |      1 | 0x6724   |
|     4 |      2 | 0x66D4   |
|     4 |      3 | 0x6684   |
|     4 |      4 | 0x6634   |
|     4 |      5 | 0x65E4   |
|     4 |      6 | 0x6594   |
|     4 |      7 | 0x6544   |
|     4 |      8 | 0x64F4   |
|     4 |      9 | 0x64A4   |
|     4 |     10 | 0x6454   |
|     4 |     11 | 0x6404   |
|     4 |     12 | 0x63B4   |
|     4 |     13 | 0x6364   |
|     4 |     14 | 0x6314   |
|     4 |     15 | 0x62C4   |
|     4 |     16 | 0x6274   |
|     4 |     17 | 0x6224   |
|     4 |     18 | 0x61D4   |
|     4 |     19 | 0x6184   |
|     4 |     20 | 0x6134   |
|     4 |     21 | 0x60E4   |
|     4 |     22 | 0x6094   |
|     4 |     23 | 0x6044   |
|     4 |     24 | 0x5FF4   |
|     4 |     25 | 0x5FA4   |
|     4 |     26 | 0x5F54   |
|     4 |     27 | 0x5F04   |
|     4 |     28 | 0x5EB4   |
|     4 |     29 | 0x5E64   |
|     4 |     30 | 0x5E14   |
|     5 |      1 | 0x5DC4   |
|     5 |      2 | 0x5D74   |
|     5 |      3 | 0x5D24   |
|     5 |      4 | 0x5CD4   |
|     5 |      5 | 0x5C84   |
|     5 |      6 | 0x5C34   |
|     5 |      7 | 0x5BE4   |
|     5 |      8 | 0x5B94   |
|     5 |      9 | 0x5B44   |
|     5 |     10 | 0x5AF4   |
|     5 |     11 | 0x5AA4   |
|     5 |     12 | 0x5A54   |
|     5 |     13 | 0x5A04   |
|     5 |     14 | 0x59B4   |
|     5 |     15 | 0x5964   |
|     5 |     16 | 0x5914   |
|     5 |     17 | 0x58C4   |
|     5 |     18 | 0x5874   |
|     5 |     19 | 0x5824   |
|     5 |     20 | 0x57D4   |
|     5 |     21 | 0x5784   |
|     5 |     22 | 0x5734   |
|     5 |     23 | 0x56E4   |
|     5 |     24 | 0x5694   |
|     5 |     25 | 0x5644   |
|     5 |     26 | 0x55F4   |
|     5 |     27 | 0x55A4   |
|     5 |     28 | 0x5554   |
|     5 |     29 | 0x5504   |
|     5 |     30 | 0x54B4   |
|     6 |      1 | 0x5464   |
|     6 |      2 | 0x5414   |
|     6 |      3 | 0x53C4   |
|     6 |      4 | 0x5374   |
|     6 |      5 | 0x5324   |
|     6 |      6 | 0x52D4   |
|     6 |      7 | 0x5284   |
|     6 |      8 | 0x5234   |
|     6 |      9 | 0x51E4   |
|     6 |     10 | 0x5194   |
|     6 |     11 | 0x5144   |
|     6 |     12 | 0x50F4   |
|     6 |     13 | 0x50A4   |
|     6 |     14 | 0x5054   |
|     6 |     15 | 0x5004   |
|     6 |     16 | 0x4FB4   |
|     6 |     17 | 0x4F64   |
|     6 |     18 | 0x4F14   |
|     6 |     19 | 0x4EC4   |
|     6 |     20 | 0x4E74   |
|     6 |     21 | 0x4E24   |
|     6 |     22 | 0x4DD4   |
|     6 |     23 | 0x4D84   |
|     6 |     24 | 0x4D34   |
|     6 |     25 | 0x4CE4   |
|     6 |     26 | 0x4C94   |
|     6 |     27 | 0x4C44   |
|     6 |     28 | 0x4BF4   |
|     6 |     29 | 0x4BA4   |
|     6 |     30 | 0x4B54   |
|     7 |      1 | 0x4B04   |
|     7 |      2 | 0x4AB4   |
|     7 |      3 | 0x4A64   |
|     7 |      4 | 0x4A14   |
|     7 |      5 | 0x49C4   |
|     7 |      6 | 0x4974   |
|     7 |      7 | 0x4924   |
|     7 |      8 | 0x48D4   |
|     7 |      9 | 0x4884   |
|     7 |     10 | 0x4834   |
|     7 |     11 | 0x47E4   |
|     7 |     12 | 0x4794   |
|     7 |     13 | 0x4744   |
|     7 |     14 | 0x46F4   |
|     7 |     15 | 0x46A4   |
|     7 |     16 | 0x4654   |
|     7 |     17 | 0x4604   |
|     7 |     18 | 0x45B4   |
|     7 |     19 | 0x4564   |
|     7 |     20 | 0x4514   |
|     7 |     21 | 0x44C4   |
|     7 |     22 | 0x4474   |
|     7 |     23 | 0x4424   |
|     7 |     24 | 0x43D4   |
|     7 |     25 | 0x4384   |
|     7 |     26 | 0x4334   |
|     7 |     27 | 0x42E4   |
|     7 |     28 | 0x4294   |
|     7 |     29 | 0x4244   |
|     7 |     30 | 0x41F4   |
|     8 |      1 | 0x41A4   |
|     8 |      2 | 0x4154   |
|     8 |      3 | 0x4104   |
|     8 |      4 | 0x40B4   |
|     8 |      5 | 0x4064   |
|     8 |      6 | 0x4014   |
|     8 |      7 | 0x3FC4   |
|     8 |      8 | 0x3F74   |
|     8 |      9 | 0x3F24   |
|     8 |     10 | 0x3ED4   |
|     8 |     11 | 0x3E84   |
|     8 |     12 | 0x3E34   |
|     8 |     13 | 0x3DE4   |
|     8 |     14 | 0x3D94   |
|     8 |     15 | 0x3D44   |
|     8 |     16 | 0x3CF4   |
|     8 |     17 | 0x3CA4   |
|     8 |     18 | 0x3C54   |
|     8 |     19 | 0x3C04   |
|     8 |     20 | 0x3BB4   |
|     8 |     21 | 0x3B64   |
|     8 |     22 | 0x3B14   |
|     8 |     23 | 0x3AC4   |
|     8 |     24 | 0x3A74   |
|     8 |     25 | 0x3A24   |
|     8 |     26 | 0x39D4   |
|     8 |     27 | 0x3984   |
|     8 |     28 | 0x3934   |
|     8 |     29 | 0x38E4   |
|     8 |     30 | 0x3894   |
|     9 |      1 | 0x3844   |
|     9 |      2 | 0x37F4   |
|     9 |      3 | 0x37A4   |
|     9 |      4 | 0x3754   |
|     9 |      5 | 0x3704   |
|     9 |      6 | 0x36B4   |
|     9 |      7 | 0x3664   |
|     9 |      8 | 0x3614   |
|     9 |      9 | 0x35C4   |
|     9 |     10 | 0x3574   |
|     9 |     11 | 0x3524   |
|     9 |     12 | 0x34D4   |
|     9 |     13 | 0x3484   |
|     9 |     14 | 0x3434   |
|     9 |     15 | 0x33E4   |
|     9 |     16 | 0x3394   |
|     9 |     17 | 0x3344   |
|     9 |     18 | 0x32F4   |
|     9 |     19 | 0x32A4   |
|     9 |     20 | 0x3254   |
|     9 |     21 | 0x3204   |
|     9 |     22 | 0x31B4   |
|     9 |     23 | 0x3164   |
|     9 |     24 | 0x3114   |
|     9 |     25 | 0x30C4   |
|     9 |     26 | 0x3074   |
|     9 |     27 | 0x3024   |
|     9 |     28 | 0x2FD4   |
|     9 |     29 | 0x2F84   |
|     9 |     30 | 0x2F34   |
|    10 |      1 | 0x2EE4   |
|    10 |      2 | 0x2E94   |
|    10 |      3 | 0x2E44   |
|    10 |      4 | 0x2DF4   |
|    10 |      5 | 0x2DA4   |
|    10 |      6 | 0x2D54   |
|    10 |      7 | 0x2D04   |
|    10 |      8 | 0x2CB4   |
|    10 |      9 | 0x2C64   |
|    10 |     10 | 0x2C14   |
|    10 |     11 | 0x2BC4   |
|    10 |     12 | 0x2B74   |
|    10 |     13 | 0x2B24   |
|    10 |     14 | 0x2AD4   |
|    10 |     15 | 0x2A84   |
|    10 |     16 | 0x2A34   |
|    10 |     17 | 0x29E4   |
|    10 |     18 | 0x2994   |
|    10 |     19 | 0x2944   |
|    10 |     20 | 0x28F4   |
|    10 |     21 | 0x28A4   |
|    10 |     22 | 0x2854   |
|    10 |     23 | 0x2804   |
|    10 |     24 | 0x27B4   |
|    10 |     25 | 0x2764   |
|    10 |     26 | 0x2714   |
|    10 |     27 | 0x26C4   |
|    10 |     28 | 0x2674   |
|    10 |     29 | 0x2624   |
|    10 |     30 | 0x25D4   |
|    11 |      1 | 0x2584   |
|    11 |      2 | 0x2534   |
|    11 |      3 | 0x24E4   |
|    11 |      4 | 0x2494   |
|    11 |      5 | 0x2444   |
|    11 |      6 | 0x23F4   |
|    11 |      7 | 0x23A4   |
|    11 |      8 | 0x2354   |
|    11 |      9 | 0x2304   |
|    11 |     10 | 0x22B4   |
|    11 |     11 | 0x2264   |
|    11 |     12 | 0x2214   |
|    11 |     13 | 0x21C4   |
|    11 |     14 | 0x2174   |
|    11 |     15 | 0x2124   |
|    11 |     16 | 0x20D4   |
|    11 |     17 | 0x2084   |
|    11 |     18 | 0x2034   |
|    11 |     19 | 0x1FE4   |
|    11 |     20 | 0x1F94   |
|    11 |     21 | 0x1F44   |
|    11 |     22 | 0x1EF4   |
|    11 |     23 | 0x1EA4   |
|    11 |     24 | 0x1E54   |
|    11 |     25 | 0x1E04   |
|    11 |     26 | 0x1DB4   |
|    11 |     27 | 0x1D64   |
|    11 |     28 | 0x1D14   |
|    11 |     29 | 0x1CC4   |
|    11 |     30 | 0x1C74   |
|    12 |      1 | 0x1C24   |
|    12 |      2 | 0x1BD4   |
|    12 |      3 | 0x1B84   |
|    12 |      4 | 0x1B34   |
|    12 |      5 | 0x1AE4   |
|    12 |      6 | 0x1A94   |
|    12 |      7 | 0x1A44   |
|    12 |      8 | 0x19F4   |
|    12 |      9 | 0x19A4   |
|    12 |     10 | 0x1954   |
|    12 |     11 | 0x1904   |
|    12 |     12 | 0x18B4   |
|    12 |     13 | 0x1864   |
|    12 |     14 | 0x1814   |
|    12 |     15 | 0x17C4   |
|    12 |     16 | 0x1774   |
|    12 |     17 | 0x1724   |
|    12 |     18 | 0x16D4   |
|    12 |     19 | 0x1684   |
|    12 |     20 | 0x1634   |
|    12 |     21 | 0x15E4   |
|    12 |     22 | 0x1594   |
|    12 |     23 | 0x1544   |
|    12 |     24 | 0x14F4   |
|    12 |     25 | 0x14A4   |
|    12 |     26 | 0x1454   |
|    12 |     27 | 0x1404   |
|    12 |     28 | 0x13B4   |
|    12 |     29 | 0x1364   |
|    12 |     30 | 0x1314   |
|    13 |      1 | 0x12C4   |
|    13 |      2 | 0x1274   |
|    13 |      3 | 0x1224   |
|    13 |      4 | 0x11D4   |
|    13 |      5 | 0x1184   |
|    13 |      6 | 0x1134   |
|    13 |      7 | 0x10E4   |
|    13 |      8 | 0x1094   |
|    13 |      9 | 0x1044   |
|    13 |     10 | 0xFF4    |
|    13 |     11 | 0xFA4    |
|    13 |     12 | 0xF54    |
|    13 |     13 | 0xF04    |
|    13 |     14 | 0xEB4    |
|    13 |     15 | 0xE64    |
|    13 |     16 | 0xE14    |
|    13 |     17 | 0xDC4    |
|    13 |     18 | 0xD74    |
|    13 |     19 | 0xD24    |
|    13 |     20 | 0xCD4    |
|    13 |     21 | 0xC84    |
|    13 |     22 | 0xC34    |
|    13 |     23 | 0xBE4    |
|    13 |     24 | 0xB94    |
|    13 |     25 | 0xB44    |
|    13 |     26 | 0xAF4    |
|    13 |     27 | 0xAA4    |
|    13 |     28 | 0xA54    |
|    13 |     29 | 0xA04    |
|    13 |     30 | 0x9B4    |
|    14 |      1 | 0x964    |
|    14 |      2 | 0x914    |
|    14 |      3 | 0x8C4    |
|    14 |      4 | 0x874    |
|    14 |      5 | 0x824    |
|    14 |      6 | 0x7D4    |
|    14 |      7 | 0x784    |
|    14 |      8 | 0x734    |
|    14 |      9 | 0x6E4    |
|    14 |     10 | 0x694    |
|    14 |     11 | 0x644    |
|    14 |     12 | 0x5F4    |
|    14 |     13 | 0x5A4    |
|    14 |     14 | 0x554    |
|    14 |     15 | 0x504    |
|    14 |     16 | 0x4B4    |
|    14 |     17 | 0x464    |
|    14 |     18 | 0x414    |
|    14 |     19 | 0x3C4    |
|    14 |     20 | 0x374    |
|    14 |     21 | 0x324    |
|    14 |     22 | 0x2D4    |
|    14 |     23 | 0x284    |
|    14 |     24 | 0x234    |
|    14 |     25 | 0x1E4    |
|    14 |     26 | 0x194    |
|    14 |     27 | 0x144    |
|    14 |     28 | 0xF4     |
|    14 |     29 | 0xA4     |
|    14 |     30 | 0x54     |
