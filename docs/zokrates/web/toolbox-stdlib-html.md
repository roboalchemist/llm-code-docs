# Source: https://zokrates.github.io/toolbox/stdlib.html

Title: Standard Library - ZoKrates

URL Source: https://zokrates.github.io/toolbox/stdlib.html

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

[Standard library ----------------](https://zokrates.github.io/toolbox/stdlib.html#standard-library)
ZoKrates comes with a number of reusable components in the form of a Standard Library. In order to import it as described in the [imports](https://zokrates.github.io/language/imports.html) section, the `$ZOKRATES_STDLIB` environment variable must be set to the `stdlib` folder.

The full ZoKrates Standard Library can be found [here](https://github.com/Zokrates/ZoKrates/tree/latest/zokrates_stdlib/stdlib).

[### Hashes](https://zokrates.github.io/toolbox/stdlib.html#hashes)[#### SHA256](https://zokrates.github.io/toolbox/stdlib.html#sha256)
We provide an implementation of the SHA256 function from the SHA-2 family of secure hash functions [1](https://zokrates.github.io/toolbox/stdlib.html#1). The hash functions of the SHA-2 family are considered to be pseudorandom.

SHA256 is available in Ethereum as a pre-compiled contract and thus a hash function that is cheap to evaluate in the EVM. However, the implementation inside a circuit is comparatively expensive, as it is defined for binary in- and outputs and heavily relies on bit manipulation.

[#### Pedersen Hashes](https://zokrates.github.io/toolbox/stdlib.html#pedersen-hashes)
The pedersen hash function is inspired by a commitment scheme published by Pedersen [2](https://zokrates.github.io/toolbox/stdlib.html#2). This hash function’s security is based on the discrete logarithm problem. Pedersen-hashes cannot be assumed to be pseudorandom and should therefore not be used where a hash function serves as a random oracle.

In the EVM, operations on the BabyJubJub curve are not natively supported. Therefore, Pedersen hashes are expensive to evaluate on-chain and should be avoided.

By definition, the Pedersen hash function has a fixed-length binary input and outputs a group element, i.e., a point on the BabyJubJub elliptic curve in our case.

[#### MiMC](https://zokrates.github.io/toolbox/stdlib.html#mimc)
The MiMC hash function was designed by using the MiMC-Feistel permutation [3](https://zokrates.github.io/toolbox/stdlib.html#3) over a prime field in a sponge construction [4](https://zokrates.github.io/toolbox/stdlib.html#4) to arrive at a secure and efficiently provable hash function. The construction is based on established hash function design principles from symmetric cryptography but is still novel and should thus be used cautiously. MiMC hashes are considered to be pseudorandom.

Due to its native use of prime field arithmetics, MiMC hash functions are efficient in circuits. At the same time, they can be evaluated by the EVM with comparatively little overhead.

The MiMC hash function maps from field elements to field elements; applying the function to its output again does not introduce overhead for packing/unpacking.

[### Elliptic curve cryptography](https://zokrates.github.io/toolbox/stdlib.html#elliptic-curve-cryptography)
Thanks to the existence of BabyJubJub, an efficient elliptic curve embedded in ALT_BN128, we provide tools to perform elliptic curve operations such as:

*   Point operations
*   Proving knowledge of a private EdDSA key
*   Proving validity of an EdDSA signature

Check out this [python repository](https://github.com/Zokrates/pycrypto) for tooling, for example to generate EdDSA signatures to then check in a SNARK.

[### Utils](https://zokrates.github.io/toolbox/stdlib.html#utils)[#### Packing / Unpacking](https://zokrates.github.io/toolbox/stdlib.html#packing--unpacking)
As some operations require their input to be provided in the form of bits, we provide tools to convert back and forth between field elements and their bit representations.

[#### Casts](https://zokrates.github.io/toolbox/stdlib.html#casts)
Helpers to convert between types representing binary data.

[#### Multiplexer](https://zokrates.github.io/toolbox/stdlib.html#multiplexer)
Optimised tools to branch inside circuits.

1
P. FIPS. “180-4 FEDERAL INFORMATION PROCESSING STANDARDS PUBLICA- TION”. In: Secure Hash Standard (SHS), National Institute of Standards and Technology (2012).

2
T. P. Pedersen. “Non-interactive and information-theoretic secure verifiable secret shar- ing”. In: Annual International Cryptology Conference. Springer. 1991, pp. 129–140.

3
M. Albrecht, L. Grassi, C. Rechberger, A. Roy, and T. Tiessen. “MiMC: Efficient en- cryption and cryptographic hashing with minimal multiplicative complexity”. In: In- ternational Conference on the Theory and Application of Cryptology and Information Security. Springer. 2016, pp. 191–219.

4
G. Bertoni, J. Daemen, M. Peeters, and G. Van Assche. “On the indifferentiability of the sponge construction”. In: Annual International Conference on the Theory and Applica- tions of Cryptographic Techniques. Springer. 2008, pp. 181–197.

[](https://zokrates.github.io/toolbox/trusted_setup.html "Previous chapter")[](https://zokrates.github.io/toolbox/proving_schemes.html "Next chapter")

[](https://zokrates.github.io/toolbox/trusted_setup.html "Previous chapter")[](https://zokrates.github.io/toolbox/proving_schemes.html "Next chapter")
