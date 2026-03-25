# Source: https://docs.nexus.xyz/zkvm/walkthroughs/use-case-program-execution.md

# Use Case: Program Execution

### Introduction

*As this walkthrough describes a more advanced use case for the zkVM, we recommend reviewing both the* [SDK Quick Start](https://docs.nexus.xyz/zkvm/development/sdk-quick-start) *and the simpler* [Stable Matching](https://docs.nexus.xyz/zkvm/walkthroughs/use-case-stable-matching) *walkthrough first.*

By definition, a zkVM is designed to prove the correctness of a program’s execution. However, a more advanced use case arises when the **program to be proven** is not the code running directly in the zkVM, but is instead provided **as input** to the zkVM.

In this case, the zkVM executes an **interpreter** as its guest program, which then reads, interprets, and runs the input program inside the zkVM. This effectively allows the zkVM to generate a proof for the execution of arbitrary, dynamically supplied programs.

Consider the following guest program in which `program_to_be_proven` is nested inside as input to the zkVM:

```rust
fn digest(program: &ElfFile) -> Vec<u8> { ... }

fn rv32i_interpret(program: &ElfFile) -> Vec<u8> { ... }

#[nexus_rt::main]
#[nexus_rt::private_input(program_to_be_proven)]
#[nexus_rt::public_input(program_digest)]
fn main(program_to_be_proven: ElfFile, program_digest: Vec<u8>) -> Vec<u8> {
    assert_eq!(digest(&program_to_be_proven), &program_digest);

    nexus_rt::print!("Program digest {} validated, executing program... ", program_digest);

    let output = rv32i_interpret(&program_to_be_proven);

    nexus_rt::println!("completed.");

    output
}
```

At first glance, this pattern may seem redundant—why not just run `program_to_be_proven` directly as the guest program? However, this level of **indirection** unlocks powerful capabilities that significantly expand the utility of the zkVM.

#### Enabling Private Program Execution

The first benefit, illustrated by the example above, is the ability to treat the **program to be proven** as a **private input**. This allows the zkVM to prove the execution of programs **without revealing their source**, making it possible to build **private smart contracts** on-chain, among other use cases.

By comparing the program’s digest to a **public input**, verifiers can still check meaningful properties such as:

* Consistency of the private program across multiple invocations.
* Conformance to a known, audited version without exposing implementation details.

This digest check enables **trust minimization** while preserving **privacy**.

#### Generalization Across Programs with a Single zkVM Binary

A second, more technical benefit is that this structure enables the zkVM to handle a wide range of programs through a **single, fixed guest binary** — the interpreter.

With careful planning around memory constraints (e.g. stack, heap, and output size bounds), this pattern allows:

* The proving key and public parameters can be shared and reused across many programs, which simplifies definitions for [non-transparent provers which may require per-program setup](https://blog.nexus.xyz/the-murky-proof-system-waters-part-ii/).
* Deployment pipelines for applications and smart contracts verifying zkVM proofs on-chain can be simplified significantly.
* Systems using non-transparent proving systems can be managed more easily, even though they often require per-program setup (note: the `Stwo` prover used here is transparent).

This approach decouples the proving circuit from individual guest programs, significantly improving **composability** and **maintainability**.

### The Lambda Calculus Model

Instead of working through this design at the full complexity of the RISC-V32i instruction set, this walkthrough uses a simpler computational model: the [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus). The example demonstrates the core concept with a minimal interpreter implemented as a guest program inside the zkVM.

***

### Implementation

To start, follow the [SDK Quick Start](https://docs.nexus.xyz/zkvm/development/sdk-quick-start). After installing the zkVM, initialize the host and guest programs:

```bash
$ cargo nexus host lambda_calculus
```

Begin by creating a shared library for the guest and host program, located within the guest program crate.

#### Shared Library

The first part of the library defines terms in the calculus:

lambda\_calculus/src/guest/src/common.rs

```rust
#![cfg_attr(no_std)]

extern crate alloc;

use alloc::boxed::Box;
use core::fmt::{Debug, Display};
use serde::{Serialize, Deserialize};

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord, Serialize, Deserialize)]
#[repr(transparent)]
pub struct DeBruijnIndex(usize);

impl From<usize> for DeBruijnIndex {
    fn from(value: usize) -> Self {
        Self(value)
    }
}

impl Display for DeBruijnIndex {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        write!(f, "{}", self.0)
    }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
enum Term<R> {
    Var(DeBruijnIndex),
    Lambda(R),
    Apply(R, R),
}

impl<R: Display> Display for Term<R> {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            Term::Var(v) => write!(f, "{v}"),
            Term::Lambda(t) => {
                write!(f, "(\\")?;
                write!(f, "{t}")?;
                write!(f, ")")
            }
            Term::Apply(t1, t2) => {
                write!(f, "(")?;
                write!(f, "{t1}")?;
                write!(f, " ")?;
                write!(f, "{t2}")?;
                write!(f, ")")
            }
        }
    }
}
```

This defines an enum `Term` for possible term kinds: indexed `Var`, `Lambda`, and `Apply`, and includes trait implementations for construction and debugging. Next, full expressions and evaluation routines:

lambda\_calculus/src/guest/src/common.rs

```rust
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Expr(Term<Box<Self>>);

impl Display for Expr {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl PartialEq for Expr {
    fn eq(&self, other: &Self) -> bool {
        self.clone().eval().structural_eq(&other.clone().eval())
    }
}

impl Eq for Expr {}

impl Expr {
    pub fn var<T: Into<DeBruijnIndex>>(binding: T) -> Self {
        Self(Term::Var(binding.into()))
    }

    pub fn lambda<T: Into<Box<Self>>>(inner: T) -> Self {
        Self(Term::Lambda(inner.into()))
    }

    pub fn apply<T1, T2>(left: T1, right: T2) -> Self
    where
        T1: Into<Box<Self>>,
        T2: Into<Box<Self>>,
    {
        Self(Term::Apply(left.into(), right.into()))
    }

    pub fn identity() -> Self {
        Self::lambda(Self::var(0))
    }

    pub fn omega() -> Self {
        let expr = Self::lambda(Self::apply(Self::var(0), Self::var(0)));
        Self::apply(expr.clone(), expr)
    }

    pub fn step(&self) -> Self {
        fn subst(body: Expr, arg: Expr, depth: usize) -> Expr {
            match body.0 {
                Term::Var(i) => {
                    if i.0 == depth {
                        arg
                    } else {
                        Expr::var(i)
                    }
                }
                Term::Lambda(e) => subst(*e, arg, depth + 1),
                Term::Apply(e1, e2) => {
                    Expr::apply(subst(*e1, arg.clone(), depth), subst(*e2, arg, depth))
                }
            }
        }

        // attempt beta reduction
        if let Term::Apply(e1, e2) = &self.0 {
            if let Term::Lambda(e) = &e1.0 {
                return subst(*e.clone(), *e2.clone(), 0);
            }
        }

        self.clone()
    }

    pub fn structural_eq(&self, other: &Self) -> bool {
        match (&self.0, &other.0) {
            (Term::Var(i), Term::Var(j)) => *i == *j,
            (Term::Lambda(e), Term::Lambda(f)) => e.structural_eq(f),
            (Term::Apply(e1, e2), Term::Apply(f1, f2)) => {
                e1.structural_eq(f1) && e2.structural_eq(f2)
            }
            _ => false,
        }
    }

    pub fn eval(self) -> Self {
        let mut curr = self;
        loop {
            let next = curr.step();
            if next.structural_eq(&curr) {
                return curr.clone();
            } else {
                curr = next;
            }
        }
    }
}
```

This provides `step` and `eval` routines to reduce expressions into stable forms.

To make the common library work across both host and guest:

* Update the guest crate to depend on `serde` (used for serialization/deserialization of `Expr`):

lambda\_calculus/src/guest/Cargo.toml

```toml
...

[dependencies]
nexus-rt = { git = "https://github.com/nexus-xyz/nexus-zkvm.git", tag = "0.3.0", version = "0.3.0" }
postcard = { version = "1.1.1", default-features = false, features = ["alloc"] }
serde = { version = "1.0", default-features = false, features = ["derive"] }

...
```

* Export the common code as a Rust library:

lambda\_calculus/src/guest/src/lib.rs

```rust
#![no_std]

pub mod common;
pub use common::*;
```

* Make the library visible to the host program:

lambda\_calculus/Cargo.toml

```toml
...

[dependencies]
nexus-sdk = { git = "https://github.com/nexus-xyz/nexus-zkvm.git", tag = "0.3.0", version = "0.3.0" }
guest = { path = "./src/guest" }

...
```

#### Guest Program

As an `Expr` is a program in the lambda calculus, implement a simple interpreter (here omitting hash-based checking):

lambda\_calculus/src/guest/src/main.rs

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

use guest::Expr;

#[nexus_rt::main]
#[nexus_rt::private_input(program_to_be_proven)]
fn main(program_to_be_proven: Expr) -> Expr {
    program_to_be_proven.eval()
}
```

#### Host Program

Create a host program that compiles the guest, provides a private program as input, and produces a proof of its execution:

lambda\_calculus/src/main.rs

```rust
use nexus_sdk::{
    compile::{cargo::CargoPackager, Compile, Compiler},
    stwo::seq::Stwo,
    ByGuestCompilation, Local, Prover, Viewable,
};

use guest::Expr;

const PACKAGE: &str = "guest";

fn main() {
    println!("Compiling guest program...");
    let mut prover_compiler = Compiler::<CargoPackager>::new(PACKAGE);
    let prover: Stwo<Local> =
        Stwo::compile(&mut prover_compiler).expect("failed to compile guest program");

    let program_to_be_proven = Expr::apply(Expr::identity(), Expr::var(42));

    println!("Proving execution of vm...");
    let (view, proof) = prover.prove_with_input::<Expr, ()>(
        &program_to_be_proven,
        (),
    ).expect("failed to prove program");

    assert_eq!(view.exit_code().expect("failed to retrieve exit code"), nexus_sdk::KnownExitCodes::ExitSuccess as u32);

    let output = view.public_output::<Expr>().expect("failed to retrieve public output");

    println!("Reduced expression: {}", output);
}
```

### Verification

Verification does not require access to the private program. A verifier can recompile the guest program and verify the proof against the expected outputs:

```rust
println!("Verifier recompiling guest program...");
let mut verifier_compiler = Compiler::<CargoPackager>::new(PACKAGE);
let path = verifier_compiler.build().expect("failed to (re)compile guest program");

print!("Verifying execution...");
proof.verify_expected_from_program_path::<&str, (), Expr>(
  &(),                                           // at view.public_input
  nexus_sdk::KnownExitCodes::ExitSuccess as u32, // at view.exit_code
  &output,                                       // at view.public_output
  &path,                                         // path to program binary
  &[]                                            // no associated data,
).expect("failed to verify proof");
```

This demonstrates using the zkVM to prove the correctness of executing a private program.

### Conclusion

This walkthrough demonstrates how the Nexus zkVM can be applied to fundamental computational models, illustrating versatility beyond practical applications. The implementation proves correct execution of lambda calculus programs while keeping program logic private.

Key achievements:

1. A shared library architecture enabling code reuse between guest and host programs.
2. A clean abstraction for lambda calculus expressions with evaluation semantics.
3. A zkVM-based interpreter that generates proofs for program execution.
4. A verification system that confirms correctness without exposing the original program.

This example shows that zkVMs can handle abstract computational models, not just concrete algorithms, and that privacy-preserving verification principles generalize across domains. The approach transforms program execution from “trust the interpreter” to “verify the computation,” providing mathematical assurance that programs are evaluated correctly according to their formal semantics.

Links for further reading:

* Use Case: Stable Matching: <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
* The Complete Specification: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>
