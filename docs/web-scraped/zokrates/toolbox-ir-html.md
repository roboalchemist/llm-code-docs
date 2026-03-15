# Source: https://zokrates.github.io/toolbox/ir.html

Title: ZIR - ZoKrates

URL Source: https://zokrates.github.io/toolbox/ir.html

Markdown Content:
1.   [**1.** Introduction](https://zokrates.github.io/introduction.html)
2.   [**2.** Getting Started](https://zokrates.github.io/gettingstarted.html)
3.   [**3.** Language](https://zokrates.github.io/language/index.html)
4.       1.   [**3.1.** Variables](https://zokrates.github.io/language/variables.html)
    2.   [**3.2.** Types](https://zokrates.github.io/language/types.html)
    3.   [**3.3.** Operators](https://zokrates.github.io/language/operators.html)
    4.   [**3.4.** Control flow](https://zokrates.github.io/language/control_flow.html)
    5.   [**3.5.** Constants](https://zokrates.github.io/language/constants.html)
    6.   [**3.6.** Functions](https://zokrates.github.io/language/functions.html)
    7.   [**3.7.** Generics](https://zokrates.github.io/language/generics.html)
    8.   [**3.8.** Imports](https://zokrates.github.io/language/imports.html)
    9.   [**3.9.** Comments](https://zokrates.github.io/language/comments.html)
    10.   [**3.10.** Macros](https://zokrates.github.io/language/macros.html)
    11.   [**3.11.** Logging](https://zokrates.github.io/language/logging.html)
    12.   [**3.12.** Assembly](https://zokrates.github.io/language/assembly.html)

5.   [**4.** Toolbox](https://zokrates.github.io/toolbox/index.html)
6.       1.   [**4.1.** CLI](https://zokrates.github.io/toolbox/cli.html)
    2.   [**4.2.** Trusted Setup](https://zokrates.github.io/toolbox/trusted_setup.html)
    3.   [**4.3.** Standard Library](https://zokrates.github.io/toolbox/stdlib.html)
    4.   [**4.4.** Proving schemes](https://zokrates.github.io/toolbox/proving_schemes.html)
    5.   [**4.5.** Verification](https://zokrates.github.io/toolbox/verification.html)
    6.   [**4.6.** ZIR](https://zokrates.github.io/toolbox/ir.html)
    7.   [**4.7.** JSON ABI](https://zokrates.github.io/toolbox/abi.html)
    8.   [**4.8.** zokrates.js](https://zokrates.github.io/toolbox/zokrates_js.html)
    9.   [**4.9.** Experimental](https://zokrates.github.io/toolbox/experimental.html)

7.   [**5.** Examples](https://zokrates.github.io/examples/index.html)
8.       1.   [**5.1.** A SNARK Powered RNG](https://zokrates.github.io/examples/rng_tutorial.html)
    2.   [**5.2.** Proving knowledge of a hash preimage](https://zokrates.github.io/examples/sha256example.html)
    3.   [**5.3.** A ZK Magic Square in the browser](https://zokrates.github.io/examples/magic_square.html)

9.   [**6.** Testing](https://zokrates.github.io/testing.html)

[ZIR ---](https://zokrates.github.io/toolbox/ir.html#zir)
ZIR is the intermediate representation ZoKrates uses to represent programs. It is close to R1CS but still encapsulates witness generation.

**Note that ZIR is still in development and can change without notice.**

[Serialisation -------------](https://zokrates.github.io/toolbox/ir.html#serialisation)
ZIR programs are serialised with the following format:

| Fields | Length in bytes | Description |
| --- | --- | --- |
| Magic | 4 | `ZOK` in ASCII, right-padded by 0: `0x5a4f4b00` |
| Version | 4 | This format's version, as a big endian number: `0x00000001` |
| Field size | 4 | The first 4 bytes of `sha256(FIELD_MODULUS)`: `0xb4f7b5bd` for bn128 for example |
| Program | n | The [`bincode`](https://docs.rs/bincode/1.1.4/bincode/)-encoded program |
[Display -------](https://zokrates.github.io/toolbox/ir.html#display)
When generating R1CS constraints, very large numbers are often used, which can make reading ZIR hard for humans. To mitigate this, ZIR applies an isomorphism when displaying field elements: they are shown as members of the interval `[- (p - 1)/2, (p - 1)/2]`. In other words, the following mapping is used:

*   elements in `[0, (p - 1)/2]` map to themselves
*   elements in `[(p + 1)/2, p - 1]` map to themselves minus `p`

Therefore, instead of writing `p - 1` as:

```
21888242871839275222246405745257275088548364400416034343698204186575808495616
```

... in ZIR, we simply write:

```
-1
```
[](https://zokrates.github.io/toolbox/verification.html "Previous chapter")[](https://zokrates.github.io/toolbox/abi.html "Next chapter")

[](https://zokrates.github.io/toolbox/verification.html "Previous chapter")[](https://zokrates.github.io/toolbox/abi.html "Next chapter")
