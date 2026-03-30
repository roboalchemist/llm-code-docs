# Source: https://zokrates.github.io/toolbox/experimental.html

Title: Experimental - ZoKrates

URL Source: https://zokrates.github.io/toolbox/experimental.html

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

[Experimental features ---------------------](https://zokrates.github.io/toolbox/experimental.html#experimental-features)
ZoKrates supports some experimental features.

[Nova ----](https://zokrates.github.io/toolbox/experimental.html#nova)
ZoKrates supports the `nova` proof system using the `bellperson` backend. Nova is accessed with the subcommand `nova`.

[### API](https://zokrates.github.io/toolbox/experimental.html#api)
To use Nova, programs must have the following signature, for any types `State` and `StepInput`:

```
def main(public State state, private StepInput step_input) -> State
```

Then, using Nova lets the user prove many steps of this program, given an initial state.

For example:

```
def main(public field sum, private field element) -> field {
    return sum + element;
}
```

We compile this program using the Pallas curve:

```
zokrates compile -i sum.zok --curve pallas
```

Then we can prove three iterations as follows:

```
echo "\"0\"" > init.json
echo "[\"1\", \"7\", \"42\"]" > steps.json
zokrates nova prove
```

The proof created at `proof.json` proves the statement `0 + 1 + 7 + 42 == 50`.

We can extend it by running more steps, for example with the same intermediate inputs:

```
zokrates nova prove --continue
```

The proof updated at `proof.json` proves the statement `50 + (0 + 1 + 7 + 42) == 100`.

Once we're done, we compress the proof to a compressed snark:

```
zokrates nova compress
```

Finally, we can verify this proof

```
zokrates nova verify
```
[### Limitations](https://zokrates.github.io/toolbox/experimental.html#limitations)
*   The step circuit must be compiled with `--curve pallas`
*   The resulting recursive proof cannot currently be verified on the EVM

[](https://zokrates.github.io/toolbox/zokrates_js.html "Previous chapter")[](https://zokrates.github.io/examples/index.html "Next chapter")

[](https://zokrates.github.io/toolbox/zokrates_js.html "Previous chapter")[](https://zokrates.github.io/examples/index.html "Next chapter")
