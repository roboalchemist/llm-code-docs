# Source: https://zokrates.github.io/toolbox/zokrates_js.html

Title: zokrates.js - ZoKrates

URL Source: https://zokrates.github.io/toolbox/zokrates_js.html

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

[zokrates.js -----------](https://zokrates.github.io/toolbox/zokrates_js.html#zokratesjs)
JavaScript bindings for [ZoKrates](https://github.com/Zokrates/ZoKrates).

```
npm install zokrates-js
```
[Importing ---------](https://zokrates.github.io/toolbox/zokrates_js.html#importing)[#### ES modules](https://zokrates.github.io/toolbox/zokrates_js.html#es-modules)
```
import { initialize } from "zokrates-js";
```
[#### CommonJS](https://zokrates.github.io/toolbox/zokrates_js.html#commonjs)
```
let { initialize } = await import("zokrates-js");
```
[#### CDN](https://zokrates.github.io/toolbox/zokrates_js.html#cdn)
```
<script src="https://unpkg.com/zokrates-js@latest/umd.min.js"></script>
<script>
  zokrates.initialize().then((zokratesProvider) => {
    /* ... */
  });
</script>
```
[Example -------](https://zokrates.github.io/toolbox/zokrates_js.html#example)
```
initialize().then((zokratesProvider) => {
  const source = "def main(private field a) -> field { return a * a; }";

  // compilation
  const artifacts = zokratesProvider.compile(source);

  // computation
  const { witness, output } = zokratesProvider.computeWitness(artifacts, ["2"]);

  // run setup
  const keypair = zokratesProvider.setup(artifacts.program);

  // generate proof
  const proof = zokratesProvider.generateProof(
    artifacts.program,
    witness,
    keypair.pk
  );

  // export solidity verifier
  const verifier = zokratesProvider.exportSolidityVerifier(keypair.vk);

  // or verify off-chain
  const isVerified = zokratesProvider.verify(keypair.vk, proof);
});
```
[API ---](https://zokrates.github.io/toolbox/zokrates_js.html#api)[##### initialize()](https://zokrates.github.io/toolbox/zokrates_js.html#initialize)
Returns an initialized `ZoKratesProvider` as a promise.

```
initialize().then((zokratesProvider) => {
  // call api functions here
});
```

Returns: `Promise<ZoKratesProvider>`

[##### withOptions(options)](https://zokrates.github.io/toolbox/zokrates_js.html#withoptionsoptions)
Returns a `ZoKratesProvider` configured with given options.

```
initialize().then((defaultProvider) => {
  let zokratesProvider = defaultProvider.withOptions({
    backend: "ark",
    curve: "bls12_381",
    scheme: "g16",
  });
  // ...
});
```

Options:

*   `backend` - Backend (options: `ark` | `bellman`, default: `ark`)
*   `curve` - Elliptic curve (options: `bn128` | `bls12_381` | `bls12_377` | `bw6_761`, default: `bn128`)
*   `scheme` - Proving scheme (options: `g16` | `gm17` | `marlin`, default: `g16`)

Returns: `ZoKratesProvider`

[##### compile(source[, options])](https://zokrates.github.io/toolbox/zokrates_js.html#compilesource-options)
Compiles source code into ZoKrates internal representation of arithmetic circuits.

Parameters:

*   `source` - Source code to compile
*   `options` - Compilation options

Returns: `CompilationArtifacts`

**Examples:**

Compilation:

```
const artifacts = zokratesProvider.compile("def main() { return; }");
```

Compilation with custom options:

```
const source = "...";
const options = {
  location: "main.zok", // location of the root module
  resolveCallback: (currentLocation, importLocation) => {
    console.log(currentLocation + " is importing " + importLocation);
    return {
      source: "def main() { return; }",
      location: importLocation,
    };
  },
};
const artifacts = zokratesProvider.compile(source, options);
```

**Note:** The `resolveCallback` function is used to resolve dependencies. This callback receives the current module location and the import location of the module which is being imported. The callback must synchronously return either an error, `null` or a valid `ResolverResult` object like shown in the example above. A simple file system resolver in a node environment can be implemented as follows:

```
import fs from "fs";
import path from "path";

const fileSystemResolver = (from, to) => {
  const location = path.resolve(path.dirname(path.resolve(from)), to);
  const source = fs.readFileSync(location).toString();
  return { source, location };
};
```
[##### computeWitness(artifacts, args[, options])](https://zokrates.github.io/toolbox/zokrates_js.html#computewitnessartifacts-args-options)
Computes a valid assignment of the variables, which include the results of the computation.

Parameters:

*   `artifacts` - Compilation artifacts
*   `args` - Array of arguments (eg. `["1", "2", true]`)
*   `options` - Computation options

Returns: `ComputationResult`

**Example:**

```
const code = "def main(private field a) -> field { return a * a; }";
const artifacts = zokratesProvider.compile(code);

const { witness, output } = zokratesProvider.computeWitness(artifacts, ["2"]);

console.log(witness); // Resulting witness which can be used to generate a proof
console.log(output); // Computation output: "4"
```
[##### setup(program[, entropy])](https://zokrates.github.io/toolbox/zokrates_js.html#setupprogram-entropy)
Generates a trusted setup for the compiled program.

Parameters:

*   `program` - Compiled program
*   `entropy` - User provided randomness (optional)

Returns: `SetupKeypair`

[##### universalSetup(size[, entropy])](https://zokrates.github.io/toolbox/zokrates_js.html#universalsetupsize-entropy)
Performs the universal phase of a trusted setup. Only available for the `marlin` scheme.

Parameters:

*   `size` - Size of the trusted setup passed as an exponent. For example, `8` for `2**8`.
*   `entropy` - User provided randomness (optional)

Returns: `Uint8Array`

[##### setupWithSrs(srs, program)](https://zokrates.github.io/toolbox/zokrates_js.html#setupwithsrssrs-program)
Generates a trusted setup with universal public parameters for the compiled program. Only available for `marlin` scheme.

Parameters:

*   `srs` - Universal public parameters from the universal setup phase
*   `program` - Compiled program

Returns: `SetupKeypair`

[##### generateProof(program, witness, provingKey[, entropy])](https://zokrates.github.io/toolbox/zokrates_js.html#generateproofprogram-witness-provingkey-entropy)
Generates a proof for a computation of the compiled program.

Parameters:

*   `program` - Compiled program
*   `witness` - Witness (valid assignment of the variables) from the computation result
*   `provingKey` - Proving key from the setup keypair
*   `entropy` - User provided randomness (optional)

Returns: `Proof`

[##### verify(verificationKey, proof)](https://zokrates.github.io/toolbox/zokrates_js.html#verifyverificationkey-proof)
Verifies the generated proof.

Parameters:

*   `verificationKey` - Verification key from the setup keypair
*   `proof` - Generated proof

Returns: `boolean`

[##### exportSolidityVerifier(verificationKey)](https://zokrates.github.io/toolbox/zokrates_js.html#exportsolidityverifierverificationkey)
Generates a Solidity contract which contains the generated verification key and a public function to verify proofs of computation of the compiled program.

Parameters:

*   `verificationKey` - Verification key from the setup keypair

Returns: `string`

[##### utils.formatProof(proof)](https://zokrates.github.io/toolbox/zokrates_js.html#utilsformatproofproof)
Formats the proof into an array of field elements that are compatible as input to the generated solidity contract

Parameters:

*   `proof` - Generated proof

Returns: `array`

[](https://zokrates.github.io/toolbox/abi.html "Previous chapter")[](https://zokrates.github.io/toolbox/experimental.html "Next chapter")

[](https://zokrates.github.io/toolbox/abi.html "Previous chapter")[](https://zokrates.github.io/toolbox/experimental.html "Next chapter")
