# Source: https://docs.nexus.xyz/zkvm/development/sdk-quick-start.md

# SDK Quick Start

The Nexus SDK provides simple, misuse-resistant programmatic use of the Nexus zkVM.

{% stepper %}
{% step %}

### Install the Nexus zkVM

First, install Rust: <https://www.rust-lang.org/tools/install>. Next, install the RISC-V target:

{% code title="Install RISC-V target" %}

```bash
$ rustup target add riscv32i-unknown-none-elf
```

{% endcode %}

Then, install the Nexus zkVM:

{% code title="Install cargo-nexus (v0.3.4)" %}

```bash
$ rustup run nightly-2025-05-09 cargo install --git https://github.com/nexus-xyz/nexus-zkvm cargo-nexus --tag 'v0.3.6'
```

{% endcode %}

And verify the installation:

{% code title="Verify installation" %}

```bash
$ rustup run nightly-2025-05-09 cargo nexus --help
```

{% endcode %}

This should print the available CLI commands. At present, the `cargo nexus` CLI is minimal, providing just a `cargo nexus host` command to setup an SDK based project.
{% endstep %}

{% step %}

### Create a new Nexus host project

To use the zkVM programmatically, you need two programs: a guest program that runs on the zkVM, and a host program that operates the zkVM. Create the project with:

{% code title="Generate host project" %}

```bash
$ rustup run nightly-2025-05-09 cargo nexus host nexus-host
```

{% endcode %}

This will create a new Rust project directory with the following structure:

{% code title="Project structure" %}

```
./nexus-host
├── Cargo.lock
├── Cargo.toml
├── rust-toolchain.toml
└── src
    ├── main.rs
    └── guest
        ├── Cargo.toml
        ├── rust-toolchain.toml
        └── src
            └── main.rs
```

{% endcode %}

Here, `./src/main.rs` is the host program, while `./src/guest/src/main.rs` is the guest program.

Replace `./src/guest/src/main.rs` with this guest program (takes two integers, one public and one private, logs values, returns their product):

{% code title="src/guest/src/main.rs" %}

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

use nexus_rt::println;

#[nexus_rt::main]
#[nexus_rt::public_input(x)]
fn main(x: u32, y: u32) -> u32 {
    println!("Read public input:  {}", x);
    println!("Read private input: {}", y);

    x * y
}
```

{% endcode %}

Then replace `./src/main.rs` with this host program (compiles guest, invokes it with public input x = 5 and private input y = 3, reads output and logs, and verifies the proof):

{% code title="src/main.rs" %}

```rust
use nexus_sdk::{
    compile::{cargo::CargoPackager, Compile, Compiler},
    stwo::seq::Stwo,
    ByGuestCompilation, Local, Prover, Verifiable, Viewable,
};

const PACKAGE: &str = "guest";

fn main() {
    println!("Compiling guest program...");
    let mut prover_compiler = Compiler::<CargoPackager>::new(PACKAGE);
    let prover: Stwo<Local> =
        Stwo::compile(&mut prover_compiler).expect("failed to compile guest program");

    let elf = prover.elf.clone(); // save elf for use with test verification

    print!("Proving execution of vm... ");
    let (view, proof) = prover
        .prove_with_input::<u32, u32>(&3, &5)
        .expect("failed to prove program"); // x = 5, y = 3

    assert_eq!(view.exit_code().expect("failed to retrieve exit code"), nexus_sdk::KnownExitCodes::EXIT_SUCCESS as u32);

    let output: u32 = view
        .public_output::<u32>()
        .expect("failed to retrieve public output");
    assert_eq!(output, 15); // z = 15

    println!("output is {}!", output);
    println!(
        ">>>>> Logging\n{}<<<<<",
        view.logs().expect("failed to retrieve debug logs").join("")
    );

    print!("Verifying execution...");
    proof
        .verify_expected::<u32, u32>(
            &5,   // x = 5
            nexus_sdk::KnownExitCodes::EXIT_SUCCESS as u32,
            &15,  // z = 15
            &elf, // expected elf (program binary)
            &[],  // no associated data,
        )
        .expect("failed to verify proof");

    println!("  Succeeded!");
}
```

{% endcode %}

This host program compiles the guest, runs the zkVM with supplied inputs, retrieves output and logs, and verifies the proof of correct execution.
{% endstep %}

{% step %}

### Run your program

Run the host program (which executes and proves the guest program) with:

{% code title="Run host" %}

```bash
$ cargo run -r
```

{% endcode %}

You should see output similar to:

{% code title="Expected output" %}

```
Proving execution of vm... output is 15!
>>>>> Logging
Read public input:  5
Read private input: 3
<<<<<
Verifying execution...  Succeeded!
```

{% endcode %}

For more examples using the SDK with more complicated guest programs, see the walkthroughs for Gale-Shapley stable matching and the lambda calculus:

* <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
* <https://docs.nexus.xyz/zkvm/walkthroughs/lambdacalculus>
  {% endstep %}

{% step %}

### Run in legacy mode

In addition to the Stwo-based Nexus zkVM 3.0 prover, the SDK supports a legacy mode that uses the Nova, HyperNova, and (experimental) Jolt-based Nexus zkVM 2.0 machine. This machine uses a different runtime and requires additional host-side configuration due to public parameters and reference strings.

To use legacy mode, activate the appropriate feature for the `nexus-sdk` dependency in the host program: `legacy-nova`, `legacy-hypernova`, or `legacy-jolt`. Examples of using legacy mode to prove legacy guest programs are provided in the examples folder on GitHub:

* Legacy guest examples: <https://github.com/nexus-xyz/nexus-zkvm/tree/main/examples/legacy/src>
* SDK examples: <https://github.com/nexus-xyz/nexus-zkvm/tree/main/sdk/examples>

The legacy-mode code corresponds to the Nexus zkVM v0.2.4 release:

* <https://github.com/nexus-xyz/nexus-zkvm/tree/releases/0.2.4>
  {% endstep %}
  {% endstepper %}
