# Source: https://docs.nexus.xyz/zkvm/overview/the-nexus-zkvm.md

# The Nexus zkVM

![](https://3435725530-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLJ85JA3XlaU4USdPDSkb%2Fuploads%2FSiQoM7hcMaTD6C7qrMpo%2Fnexus-github_network_zkvm.png?alt=media\&token=987b3462-8464-43fa-af1d-08b42b39c23e)

The Nexus zero-knowledge virtual machine is a modular, extensible, prover-optimized, fully-specified zkVM written in Rust, focused on performance and security. [Nexus zkVM v0.3.6](https://github.com/nexus-xyz/nexus-zkvm/releases/tag/v0.3.6) is the current stable release, implementing the [Nexus zkVM 3.0 machine](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).

## What is the Nexus zkVM?

Nexus zkVM is a [zero-knowledge virtual machine](https://docs.nexus.xyz/zkvm/overview/zkvm-overview) that enables developers to generate succinct proofs for any computation, demonstrating that a program executed every instruction and accessed memory correctly to produce a given output. Built with Rust and focused on performance and security, it provides a robust foundation for building applications.

## Proving Computation

The Nexus zkVM can generate proofs for any computation. For example, given a Rust program that calculates the Fibonacci sequence:

{% code title="fib.rs" %}

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]

use nexus_rt::println;

fn fib(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib(n - 1) + fib(n - 2),
    }
}

#[nexus_rt::main]
fn main() {
    let n = 7;
    let result = fib(n);
    assert_eq!(result, 13);
    println!("fib({}) = {}", n, result);
}
```

{% endcode %}

the zkVM can generate a succinct, efficiently verifiable proof of its correct execution. To get started with the Nexus zkVM, check out the [Getting Started](https://docs.nexus.xyz/zkvm/development/getting-started) page.

{% hint style="warning" %}
The Nexus zkVM is in an experimental stage and is not currently recommended for production use.
{% endhint %}

## Key Features

### Security First

* The Nexus zkVM provides fully-specified cryptographic components with careful analysis of security and performance.
* The system includes no code obfuscation, no proprietary components, and no closed-source code.
* Source-available transparency ensures complete auditability for all users.

### Performance Optimized

* The prover-optimized architecture enables efficient proof generation across diverse workloads.
* Sensible defaults are configured to work out of the box without complex setup requirements.

### Developer Friendly

* Developers can write programs with execution proven to be correct.
* A comprehensive SDK and tooling ecosystem supports rapid development and deployment.
* Extensive documentation and examples guide users through implementation details.

### Extensible & Modular

* The system supports new languages, new precompiles, and new provers as the state-of-the-art advances.
* Configurable components prevent vendor lock-in and allow customization for specific use cases.
* Source-available code and consistent development by the Nexus zkVM team ensure long-term reliability.

## The Nexus Ethos: Assurance through Open Science

We believe a zkVM must provide an efficient proving mechanism without compromising on security and correctness. A zkVM cannot provide transparency without being transparent itself. Every component of a zkVM should be powered by fully and publicly specified cryptographic components, with careful analysis of security and performance. The Nexus zkVM features no code obfuscation, no proprietary components, and no closed-source code.

## Modular and Extensible Architecture

Built with a modular architecture at its core, the Nexus zkVM features independently optimized components that integrate smoothly. The system ships with carefully chosen defaults for the prover and memory model, allowing developers to start building immediately while maintaining confidence in both security and performance across diverse applications.

Extensibility is a fundamental design principle of the Nexus zkVM. The codebase and active development by the Nexus team ensures continuous evolution, supporting emerging languages, advanced precompiles, and cutting-edge proving systems as the field progresses—all without locking developers into proprietary solutions.

## Use Cases

The Nexus zkVM enables a wide range of applications:

* **Verifiable Computation**: Prove correct execution of any program
* **Privacy-Preserving Applications**: Compute on sensitive data without revealing it
* **Blockchain Scaling**: Generate proofs for off-chain computation
* **Compliance & Auditing**: Provide cryptographic guarantees for regulatory requirements
* **Trustless Systems**: Build applications that don’t require trusted intermediaries

## Getting Started

{% stepper %}
{% step %}

### Quick Start Guide

Get up and running in minutes: <https://docs.nexus.xyz/zkvm/proving/overview>
{% endstep %}

{% step %}

### SDK Documentation

Comprehensive API reference: <https://docs.nexus.xyz/zkvm/proving/sdk>
{% endstep %}

{% step %}

### Architecture Overview

Understand how it works: <https://docs.nexus.xyz/zkvm/architecture>
{% endstep %}

{% step %}

### Example Walkthroughs

Learn through practical examples: <https://docs.nexus.xyz/zkvm/walkthroughs/galeshapley>
{% endstep %}
{% endstepper %}

***

*Experience the future of verifiable computation with Nexus zkVM - where transparency meets performance.*
