ink 5.1.1 - Docs.rs

                    Docs.rs
                

    
-

                ink-5.1.1
            
        
    

                
                

                    
-
                        docs.rs

- About docs.rs
- Badges
- Builds
- Metadata
- Shorthand URLs
- Download
- Rustdoc JSON
- Build queue
- Privacy policy

-
                        Rust
                        

                            
  - Rust website

  - The Book

  - Standard Library API Reference

  - Rust by Example

  - The Cargo Guide

  - Clippy Documentation

#

                    ink 5.1.1
                    
                

                
                [ink!] Rust based eDSL for writing smart contracts for Substrate

                
                    

                        
                        
-

                                 Crate
                            
                        

                        
                        
-

                                 Source
                            
                        

                        
                        
-

                                 Builds
                            
                        

                        
                        
-

                                Feature flags
                            
                        
                    

                
            
    

        
            
                
                    

                            
                            
                            
- Coverage

- **92.19%**

                                **59** out of **64** items documented**11** out of **15** items with examples
- Size

-
                                Source code size: 190.93 kB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Ø build duration
-
                                    all releases: 2m 22s
                                        Average build duration of **successful** builds in releases after 2024-10-23.
                                        
                                    
                                
- Links

-

                                     Homepage

-

                                            use-ink/ink

                                         1462
                                         478
                                         154

                                    
                            
                        
-

                                 crates.io
                            
                        

                        
- Dependencies

-

-
                derive_more ^1.0.0
                
                    *normal*
                    
                
            
        
-
                ink_env =5.1.1
                
                    *normal*
                    
                
            
        
-
                ink_macro =5.1.1
                
                    *normal*
                    
                
            
        
-
                ink_metadata =5.1.1
                
                    *normal*
                    
                        *optional*
                    
                
            
        
-
                ink_prelude =5.1.1
                
                    *normal*
                    
                
            
        
-
                ink_primitives =5.1.1
                
                    *normal*
                    
                
            
        
-
                ink_storage =5.1.1
                
                    *normal*
                    
                
            
        
-
                pallet-contracts-uapi ^9.0.0
                
                    *normal*
                    
                
            
        
-
                parity-scale-codec ^3.6.9
                
                    *normal*
                    
                
            
        
-
                scale-info ^2.11
                
                    *normal*
                    
                        *optional*
                    
                
            
        
-
                staging-xcm ^11.0.0
                
                    *normal*
                    
                
            
        
-
                ink_ir =5.1.1
                
                    *dev*
                    
                
            
        
-
                ink_metadata =5.1.1
                
                    *dev*
                    
                
            
        
-
                trybuild ^1.0.101
                
                    *dev*
                    
                
            
        
                                

                            
                        

                        
- Versions

-

-
            **6.0.0-beta.1** (2025-11-13)
        
        
         
        
-
            **6.0.0-beta** (2025-10-29)
        
        
         
        
-
            **6.0.0-alpha** (2025-05-02)
        
        
         
        
-
            **5.1.1** (2024-12-04)
        
        
         
        
-
            **5.1.0** (2024-11-28)
        
        
         
        
-
            **5.0.0** (2024-03-11)
        
        
         
        
-
            **5.0.0-rc.3** (2024-03-08)
        
        
         
        
-
            **5.0.0-rc.2** (2024-02-28)
        
        
         
        
-
            **5.0.0-rc.1** (2024-02-09)
        
        
         
        
-
            **5.0.0-rc** (2023-11-30)
        
        
         
        
-
            **5.0.0-alpha** (2023-09-09)
        
        
         
        
-
            **4.3.0** (2023-08-24)
        
        
         
        
-
            **4.2.1** (2023-06-14)
        
        
         
        
-
            **4.2.0** (2023-04-20)
        
        
         
        
-
            **4.1.0** (2023-03-23)
        
        
         
        
-
            **4.0.1** (2023-02-27)
        
        
         
        
-
            **4.0.0** (2023-02-15)
        
        
         
        
-
            **4.0.0-rc** (2023-02-01)
        
        
         
        
-
            **4.0.0-beta.1** (2023-01-25)
        
        
         
        
-
            **4.0.0-beta** (2022-11-22)
        
        
         
        
-
            **4.0.0-alpha.3** (2022-09-21)
        
        
         
        
-
            **0.0.0** (2017-10-20)
        
                                

                            
                        

                        
                        
- Owners

-

                        docs.rs failed to build ink-5.1.1

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    
                        Visit the last successful build:
                        
                            ink-6.0.0-beta.1
                        
                    

    

ink! is an eDSL to write smart contracts in Rust for blockchains built on the Substrate framework. ink! contracts are compiled to WebAssembly.

Guided Tutorial for Beginners  •  
ink! Documentation Portal  •  
Developer Documentation

More relevant links:

- Substrate Stack Exchange ‒ Forum for getting your ink! questions answered

- `cargo-contract` ‒ CLI tool for ink! contracts

- Contracts UI ‒ Frontend for contract instantiation and interaction

- Substrate Contracts Node ‒ Simple Substrate blockchain which includes smart contract functionality

- Awesome ink! - A curated list of awesome projects for Polkadot's ink!

- We post announcements on Matrix and Discord (in the
`ink_smart-contracts` channel).

## Table of Contents

- Table of Contents

- Play with It

- Usage

- Hello, World! ‒ The Flipper

- Examples

- How it Works

- ink! Macros & Attributes Overview

  - Entry Point

  - Trait Definitions

  - Off-chain Testing

- Developer Documentation

- Community Badges

  - Normal Design

  - Flat Design

- Contributing

- License

## Play with It

The best way to start is to check out the Getting Started
page in our documentation.

If you want to have a local setup you can use our `substrate-contracts-node` for a quickstart.
It's a simple Substrate blockchain which includes the Substrate module for smart contract functionality ‒ the `contracts` pallet (see How it Works for more).

We also have a live testnet named "Contracts" on Rococo. Rococo is a Substrate based
parachain which supports ink! smart contracts. For further instructions on using this
testnet, follow the instructions in
our documentation.

The Contracts UI can be used to instantiate your
contract to a chain and interact with it.

## Usage

A prerequisite for compiling smart contracts is to have Rust and Cargo installed. Here's an installation guide.

We recommend installing `cargo-contract` as well.
It's a CLI tool which helps set up and manage WebAssembly smart contracts written with ink!:

```
cargo install cargo-contract --force

```

Use the `--force` to ensure you are updated to the most recent `cargo-contract` version.

In order to initialize a new ink! project you can use:

```
cargo contract new flipper

```

This will create a folder `flipper` in your work directory.
The folder contains a scaffold `Cargo.toml` and a `lib.rs`, which both contain the necessary building blocks for using ink!.

The `lib.rs` contains our hello world contract ‒ the `Flipper`, which we explain in the next section.

In order to build the contract just execute this command in the `flipper` folder:

```
cargo contract build

```

As a result you'll get a `target/flipper.wasm` file, a `flipper.json` file and a `<contract-name>.contract` file in the `target` folder of your contract.
The `.contract` file combines the Wasm and metadata into one file and needs to be used when instantiating the contract.

## Hello, World! ‒ The Flipper

The `Flipper` contract is a simple contract containing only a single `bool` value.

It provides methods to:

- flip its value from `true` to `false` (and vice versa) and

- return the current state.

Below you can see the code using ink!.

```
#[ink::contract]
mod flipper {
    /// The storage of the flipper contract.
    #[ink(storage)]
    pub struct Flipper {
        /// The single `bool` value.
        value: bool,
    }

    impl Flipper {
        /// Instantiates a new Flipper contract and initializes
        /// `value` to `init_value`.
        #[ink(constructor)]
        pub fn new(init_value: bool) -> Self {
            Self {
                value: init_value,
            }
        }

        /// Flips `value` from `true` to `false` or vice versa.
        #[ink(message)]
        pub fn flip(&mut self) {
            self.value = !self.value;
        }

        /// Returns the current state of `value`.
        #[ink(message)]
        pub fn get(&self) -> bool {
            self.value
        }
    }

    /// Simply execute `cargo test` in order to test your contract
    /// using the below unit tests.
    #[cfg(test)]
    mod tests {
        use super::*;

        #[ink::test]
        fn it_works() {
            let mut flipper = Flipper::new(false);
            assert_eq!(flipper.get(), false);
            flipper.flip();
            assert_eq!(flipper.get(), true);
        }
    }
}

```

The `flipper/src/lib.rs`
file in our examples folder contains exactly this code. Run `cargo contract build` to build your
first ink! smart contract.

## Examples

In the `examples` repository you'll find a number of examples written in ink!.

Some of the most interesting ones:

- `basic_contract_ref` ‒ Implements cross-contract calling.

- `trait-erc20` ‒ Defines a trait for `Erc20` contracts and implements it.

- `erc721` ‒ An exemplary implementation of `Erc721` NFT tokens.

- `dns` ‒  A simple `DomainNameService` smart contract.

- …and more, just rummage through the folder 🙃.

To build a single example navigate to the root of the example and run:

```
cargo contract build

```

You should now have an `<name>.contract` file in the `target` folder of the contract.

For information on how to upload this file to a chain, please have a look at the Play with It section or our smart contracts workshop.

## How it Works

- Substrate's Framework for Runtime Aggregation of Modularized Entities (FRAME)
contains a module  which implements an API for typical functions smart contracts need (storage,querying information about accounts, …).
This module is called the `contracts` pallet,

- The `contracts` pallet requires smart contracts to be uploaded to the blockchain as a Wasm blob.

- ink! is a smart contract language which targets the API exposed by `contracts`.
Hence ink! contracts are compiled to Wasm.

- When executing `cargo contract build` an additional file `<contract-name>.json` is created.
It contains information about e.g. what methods the contract provides for others to call.

## ink! Macros & Attributes Overview

### Entry Point

In a module annotated with `#[ink::contract]` these attributes are available:

Attribute
Where Applicable
Description

`#[ink(storage)]`
On `struct` definitions.
Defines the ink! storage struct. There can only be one ink! storage definition per contract.

`#[ink(message)]`
Applicable to methods.
Flags a method for the ink! storage struct as message making it available to the API for calling the contract.

`#[ink(constructor)]`
Applicable to method.
Flags a method for the ink! storage struct as constructor making it available to the API for instantiating the contract.

`#[ink(event)]`
On `struct` definitions.
Defines an ink! event. A contract can define multiple such ink! events.

`#[ink(anonymous)]`
Applicable to ink! events.
Tells the ink! codegen to treat the ink! event as anonymous which omits the event signature as topic upon emitting. Very similar to anonymous events in Solidity.

`#[ink(signature_topic = _)]`
Applicable to ink! events.
Specifies custom signature topic of the event that allows to use manually specify shared event definition.

`#[ink(topic)]`
Applicable on ink! event field.
Tells the ink! codegen to provide a topic hash for the given field. Every ink! event can only have a limited number of such topic fields. Similar semantics as to indexed event arguments in Solidity.

`#[ink(payable)]`
Applicable to ink! messages.
Allows receiving value as part of the call of the ink! message. ink! constructors are implicitly payable.

`#[ink(selector = S:u32)]`
Applicable to ink! messages and ink! constructors.
Specifies a concrete dispatch selector for the flagged entity. This allows a contract author to precisely control the selectors of their APIs making it possible to rename their API without breakage.

`#[ink(selector = _)]`
Applicable to ink! messages.
Specifies a fallback message that is invoked if no other ink! message matches a selector.

`#[ink(namespace = N:string)]`
Applicable to ink! trait implementation blocks.
Changes the resulting selectors of all the ink! messages and ink! constructors within the trait implementation. Allows to disambiguate between trait implementations with overlapping message or constructor names. Use only with great care and consideration!

`#[ink(impl)]`
Applicable to ink! implementation blocks.
Tells the ink! codegen that some implementation block shall be granted access to ink! internals even without it containing any ink! messages or ink! constructors.

See here for a more detailed description of those and also for details on the `#[ink::contract]` macro.

### Trait Definitions

Use `#[ink::trait_definition]` to define your very own trait definitions that are then implementable by ink! smart contracts.
See e.g. the `examples/trait-erc20` contract on how to utilize it or the documentation for details.

### Off-chain Testing

The `#[ink::test]` procedural macro enables off-chain testing. See e.g. the `examples/erc20` contract on how to utilize those or the documentation for details.

## Developer Documentation

We have a very comprehensive documentation portal,
but if you are looking for the crate level documentation itself, then these are
the relevant links:

Crate
Docs
Description

`ink`

Language features exposed by ink!. See here for a detailed description of attributes which you can use in an `#[ink::contract]`.

`ink_storage`

Data structures available in ink!.

`ink_env`

Low-level interface for interacting with the smart contract Wasm executor. Contains the off-chain testing API as well.

`ink_prelude`

Common API for no_std and std to access alloc crate types.

## Community Badges

### Normal Design

```
[![Built with ink!](https://raw.githubusercontent.com/use-ink/ink/master/.images/badge.svg)](https://github.com/use-ink/ink)

```

### Flat Design

```
[![Built with ink!](https://raw.githubusercontent.com/use-ink/ink/master/.images/badge_flat.svg)](https://github.com/use-ink/ink)

```

## Contributing

Visit our contribution guidelines for more information.

Use the scripts provided under `scripts/check-*` directory in order to run checks on either the workspace or all examples. Please do this before pushing work in a PR.

## License

The entire code within this repository is licensed under the Apache License 2.0.
