openfhe 0.2.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                openfhe-0.2.0
            
        
    

                
                

                    
- 
                        docs.rs
                        

  -  About docs.rs
  -  Badges
  -  Builds
  -  Metadata
  -  Shorthand URLs
  -  Download
  -  Rustdoc JSON
  -  Build queue
  -  Privacy policy
                        

                    
                

                

- 
                        Rust
                        

                            
  - Rust website
                            
  - The Book

                            
  - Standard Library API Reference

                            
  - Rust by Example

                            
  - The Cargo Guide

                            
  - Clippy Documentation
                        

                    
                

                
                
                    
                        
                    

                    
                    
                    
                
            
        
    

    
    
        
            
                

                
                
# 
                    openfhe 0.2.0
                    
                

                
                Rust package of the OpenFHE Fully Homomorphic Encryption Library.

                
                    

                        
                        
- 
                                
                                 Crate
                            
                        

                        
                        
- 
                            
                                
                                 Source
                            
                        

                        
                        
- 
                            
                                
                                 Builds
                            
                        

                        
                        
- 
                            
                                
                                Feature flags
                            
                        
                    

                
            
    

        
            
                
                    

- Links
                        
- 
                                
                                     Documentation
                                
                            
- 
                                
                                    
                                    
                                        
                                            fairmath/openfhe-rs
                                        
                                        

                                         55
                                         12
                                         7

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                cxx ^1.0
                
                    *normal*
                    
                
            
        
  - 
                cxx-build ^1.0
                
                    *build*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.2.8** (2024-06-26)
        
        
         
        
  - 
            **0.2.0** (2024-06-26)
        
        
         
        
  - 
            **0.1.8** (2024-06-21)
        
        
         
        
  - 
            **0.1.7** (2024-06-19)
        
        
         
        
  - 
            **0.1.6** (2024-06-16)
        
        
         
        
  - 
            **0.1.5** (2024-06-12)
        
        
         
        
  - 
            **0.1.4** (2024-05-18)
        
        
         
        
  - 
            **0.1.3** (2024-05-17)
        
        
         
        
  - 
            **0.1.2** (2024-05-16)
        
        
         
        
  - 
            **0.1.1** (2024-05-14)
        
        
         
        
  - 
            **0.1.0** (2024-05-14)
        
        
         
        
  - 
            **0.0.0** (2024-03-18)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                                    
                                
                    

                
            

            
                
                    
                        docs.rs failed to build openfhe-0.2.0
                        

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    
# About OpenFHE-rs

☀️ *OpenFHE-rs is a joint project by FairMath & OpenFHE.*

---

🔔 *Keep in mind that the library is WIP and may contain some unpolished interfaces. If you encounter any issues or have any suggestions, feel free to ping us on our Discord server or open a new issue in the GitHub repository.*

---

OpenFHE-rs is a Rust interface for the OpenFHE library, which is renowned for its comprehensive suite of Fully Homomorphic Encryption (FHE) schemes,
all implemented in C++.
By providing a Rust wrapper for OpenFHE, we aim to make these advanced FHE capabilities easily accessible to Rust developers.

Whether you're developing secure data processing applications or privacy-focused tools, OpenFHE-rs enables you to leverage the powerful encryption technologies of OpenFHE seamlessly within your Rust projects.

# Installation

To use OpenFHE-rs, you'll need to install several dependencies and follow the installation steps for both the core OpenFHE library and the Rust crate.

## Prerequisites

Ensure you have the following dependencies installed:

- `CMake >= 3.5.1`

- `G++ >= 11.4`

- `Rust >= 1.78`

- `Git`

## Installation process

### Core OpenFHE library installation

To build and install the OpenFHE library, follow the steps below or refer to OpenFHE's installation documentation.

- Clone the repository

```
git clone https://github.com/openfheorg/openfhe-development.git
cd openfhe-development

```

- Configure CMake

```
cmake -B ./build -DBUILD_SHARED=ON .

```

- Build and install the C++ OpenFHE library

```
make -C ./build -j$(nproc)
make -C ./build install

```

- Update the cache for the linker

```
sudo ldconfig

```

## Configuring your project to use the crate

To use the OpenFHE crate in your Rust project, add it as a dependency from crates.io:

```
cargo add openfhe

```

You also need to add a small piece of code for the core dependencies' configuration in your `build.rs` file:

```
fn main
{
    // linking openFHE
    println!("cargo::rustc-link-arg=-L/usr/local/lib");
    println!("cargo::rustc-link-arg=-lOPENFHEpke");
    println!("cargo::rustc-link-arg=-lOPENFHEbinfhe");
    println!("cargo::rustc-link-arg=-lOPENFHEcore");
    // linking OpenMP
    println!("cargo::rustc-link-arg=-fopenmp");
    // necessary to avoid LD_LIBRARY_PATH
    println!("cargo::rustc-link-arg=-Wl,-rpath=/usr/local/lib");
}

```

To build and run a complete working example, go to the crate_usage directory
(assuming that the OpenFHE library is already installed),

- Build the application

```
cargo build

```

- Run

```
cargo run

```

# Custom crate installation from the source

You can adjust the installation process by building the crate manually.
In that case, you need to clone the Fair Math's openfhe-rs repo to your local machine and build it:

- Clone the repository

```
git clone https://github.com/fairmath/openfhe-rs.git
cd openfhe-rs

```

- Build the library

```
cargo build

```

- Run tests

```
cargo test -- --test-threads=1

```

- Run the examples

```
cargo run --example function_evaluation
cargo run --example polynomial_evaluation
cargo run --example simple_integers
cargo run --example simple_real_numbers

```

# Contributing

Contributions are always welcome!
If you find bugs, have feature requests, or want to contribute code, please open an issue or pull request on the GitHub repository.

# License

`OpenFHE-rs` is licensed under the **BSD 2-Clause License**.
See the LICENSE file for more details.