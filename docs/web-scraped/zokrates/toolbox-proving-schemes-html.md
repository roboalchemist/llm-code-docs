# Source: https://zokrates.github.io/toolbox/proving_schemes.html

Title: Proving schemes - ZoKrates

URL Source: https://zokrates.github.io/toolbox/proving_schemes.html

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

[Proving schemes ---------------](https://zokrates.github.io/toolbox/proving_schemes.html#proving-schemes)[Curves ------](https://zokrates.github.io/toolbox/proving_schemes.html#curves)
Proving schemes supported by ZoKrates require a pairing-friendly elliptic curve. The options are the following:

| Curve | CLI flag | Supported by Ethereum |
| --- | --- | --- |
| ALT_BN128 | `--curve bn128` | Yes ([EIP-196](https://eips.ethereum.org/EIPS/eip-196), [EIP-197](https://eips.ethereum.org/EIPS/eip-197)) |
| BLS12_381 | `--curve bls12_381` | No ([EIP-2537](https://eips.ethereum.org/EIPS/eip-2537)) |
| BLS12_377 | `--curve bls12_377` | No ([EIP-2539](https://eips.ethereum.org/EIPS/eip-2539)) |
| BW6_761 | `--curve bw6_761` | No ([EIP-3026](https://eips.ethereum.org/EIPS/eip-3026)) |

Default: `ALT_BN128`

When not using the default, the CLI flag has to be provided for the following commands:

*   `universal-setup`
*   `compile`
*   `export-verifier`
*   `verify`

[Schemes -------](https://zokrates.github.io/toolbox/proving_schemes.html#schemes)
ZoKrates supports different proving schemes. We identify the schemes by the reference to the paper that introduced them. Currently the options available are:

| Scheme | CLI flag | Curves | Universal |
| --- | --- | --- | --- |
| [G16](https://eprint.iacr.org/2016/260) | `--proving-scheme g16` | ALTBN_128, BLS12_381 | No |
| [GM17](https://eprint.iacr.org/2017/540) | `--proving-scheme gm17` | ALTBN_128, BLS12_381, BLS12_377, BW6_761 | No |
| [Marlin](https://eprint.iacr.org/2019/1047) | `--proving-scheme marlin` | ALTBN_128, BLS12_381, BLS12_377, BW6_761 | Yes |

All schemes have a circuit-specific setup phase called `setup`. Universal schemes also feature a preliminary, circuit-agnostic step called `universal-setup`. The advantage of universal schemes is that only the `universal-setup` step requires trust, so that it can be run a single time and reused trustlessly for many programs.

Default: `G16`, except for `universal-setup` for which the default is `Marlin`

When not using the default, the CLI flag has to be provided for the following commands:

*   `universal-setup`
*   `setup`
*   `export-verifier`
*   `generate-proof`
*   `verify`

[Supporting backends -------------------](https://zokrates.github.io/toolbox/proving_schemes.html#supporting-backends)
ZoKrates supports multiple backends. The options are the following:

| Backend | CLI flag | Proving schemes | Curves |
| --- | --- | --- | --- |
| Bellman | `--backend bellman` | G16 | ALTBN_128, BLS12_381 |
| Ark | `--backend ark` | G16, GM17, MARLIN | ALTBN_128, BLS12_381, BLS12_377, BW6_761 |

Default: `ark`

When not using the default, the CLI flag has to be provided for the following commands:

*   `universal-setup`
*   `setup`
*   `generate-proof`
*   `verify`

[G16 malleability ----------------](https://zokrates.github.io/toolbox/proving_schemes.html#g16-malleability)
When using G16, developers should pay attention to the fact that an attacker, seeing a valid proof, can very easily generate a different but still valid proof. Therefore, depending on the use case, making sure on chain that the same proof cannot be submitted twice may _not_ be enough to guarantee that attackers cannot replay proofs. Mechanisms to solve this issue include:

*   signed proofs
*   nullifiers
*   usage of an ethereum address as a public input to the program
*   usage of non-malleable schemes such as GM17

[](https://zokrates.github.io/toolbox/stdlib.html "Previous chapter")[](https://zokrates.github.io/toolbox/verification.html "Next chapter")

[](https://zokrates.github.io/toolbox/stdlib.html "Previous chapter")[](https://zokrates.github.io/toolbox/verification.html "Next chapter")
