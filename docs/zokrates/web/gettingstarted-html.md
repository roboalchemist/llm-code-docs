# Source: https://zokrates.github.io/gettingstarted.html

Title: Getting Started - ZoKrates

URL Source: https://zokrates.github.io/gettingstarted.html

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

ZoKrates
--------

[](https://zokrates.github.io/print.html "Print this book")

[Getting Started ---------------](https://zokrates.github.io/gettingstarted.html#getting-started)[Installation ------------](https://zokrates.github.io/gettingstarted.html#installation)[### Online IDEs](https://zokrates.github.io/gettingstarted.html#online-ides)
To get a feel of the language, try the [ZoKrates playgound](https://play.zokrat.es/).

To experiment with creating SNARKs and verifying them in the EVM, check out the ZoKrates plugin in the [Remix online IDE](https://remix.ethereum.org/).

[### One-line installation](https://zokrates.github.io/gettingstarted.html#one-line-installation)
We provide one-line installation for Linux, MacOS and FreeBSD:

```
curl -LSfs get.zokrat.es | sh
```
[### From source](https://zokrates.github.io/gettingstarted.html#from-source)
You can build ZoKrates from [source](https://github.com/ZoKrates/ZoKrates/) with the following commands:

```
git clone https://github.com/ZoKrates/ZoKrates
cd ZoKrates
export ZOKRATES_STDLIB=$PWD/zokrates_stdlib/stdlib
cargo build -p zokrates_cli --release
cd target/release
```
[### Docker](https://zokrates.github.io/gettingstarted.html#docker)
ZoKrates is available on Dockerhub.

```
docker run -ti zokrates/zokrates /bin/bash
```

From there on, you can use the `zokrates` CLI.

[Hello ZoKrates! ---------------](https://zokrates.github.io/gettingstarted.html#hello-zokrates)
First, create the text-file `root.zok` and implement your program. In this example, we will prove knowledge of the square root `a` of a number `b`:

```
def main(private field a, field b) {
    assert(a * a == b);
    return;
}
```

Some observations:

*   The keyword `field` is the basic type we use, which is an element of a given prime field.
*   The keyword `private` signals that we do not want to reveal this input, but still prove that we know its value.

Then run the different phases of the protocol:

```
# compile
zokrates compile -i root.zok
# perform the setup phase
zokrates setup
# execute the program
zokrates compute-witness -a 337 113569
# generate a proof of computation
zokrates generate-proof
# export a solidity verifier
zokrates export-verifier
# or verify natively
zokrates verify
```

The CLI commands are explained in more detail in the [CLI reference](https://zokrates.github.io/toolbox/cli.html).

[](https://zokrates.github.io/introduction.html "Previous chapter")[](https://zokrates.github.io/language/index.html "Next chapter")

[](https://zokrates.github.io/introduction.html "Previous chapter")[](https://zokrates.github.io/language/index.html "Next chapter")
