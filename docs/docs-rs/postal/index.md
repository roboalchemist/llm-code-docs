postal 0.2.6 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                postal-0.2.6
            
        
    

                
                

                    
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
                    postal 0.2.6
                    
                

                
                FFI bindings and safe interface to libpostal

                
                    

                        
                        
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
                                
                                     Homepage
                                
                            
- 
                                
                                    
                                    
                                        
                                            pnordahl/rust-postal
                                        
                                        

                                         33
                                         10
                                         0

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                parking_lot ^0.12.0
                
                    *normal*
                    
                
            
        
  - 
                criterion ^0.2
                
                    *dev*
                    
                
            
        
  - 
                bindgen ^0.68
                
                    *build*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.2.6** (2023-09-26)
        
        
         
        
  - 
            **0.2.5** (2022-09-10)
        
        
         
        
  - 
            **0.2.4** (2020-07-15)
        
        
         
        
  - 
            **0.2.3** (2019-08-15)
        
        
         
        
  - 
            **0.2.2** (2019-08-01)
        
        
         
        
  - 
            **0.2.1** (2019-07-30)
        
        
         
        
  - 
            **0.2.0** (2019-07-12)
        
        
         
        
  - 
            **0.1.0** (2019-07-09)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                    
                        docs.rs failed to build postal-0.2.6
                        

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    
# rust-postal

Bindings to the libpostal street address parsing/normalization C library.

This library provides rust-lang/rust-bindgen generated Rust <-> C bindings, and puts an ergonomic and safe Rust API on top of them.

This crate requires Rust 1.60 or newer.

## Installation

Follow the README instructions at openvenues/libpostal to install the shared library for your platform. Currently, the compiled object is dynamically linked when your project runs - static linkage could be supported in the future.

Add `postal` to your `Cargo.toml`:

Add this to your Cargo.toml:

```
[dependencies]
postal = "0.2"

```

Next, add this to your crate:

```
extern crate postal;

```

## Usage example (expand_address)

*Note*: `libpostal` is not threadsafe. As a result, do not create more than one `postal::Context` per process. `Context::expand_address` and `Context::parse_address` do internal locking, and are safe to call concurrently.

This is an example of using the `expand_address` API:

```
extern crate postal;
use postal::{Context, InitOptions, ExpandAddressOptions};

// initialize a context to work with
let mut ctx = Context::new();

// enable address expansion for this context
ctx.init(InitOptions{expand_address: true}).unwrap();

// these options are safe to persist and reuse between calls to `expand_address`
let mut opts = ExpandAddressOptions::new();

// (optional) set languages; this can improve runtime performance significantly, approximately 30% in benchmarks
opts.set_languages(vec!["en"].as_slice());

// expand a single address into a `postal::Expansions` iterator
let exps = ctx.expand_address(
	"1234 Cherry Ln, Podunk TX", &mut opts)
	.unwrap();
for e in exps {
	dbg!(e);
}

```

This is how you might use the `parse_address` API:

```
extern crate postal;
use postal::{Context, InitOptions, ParseAddressOptions};

// initialize a context to work with
let mut ctx = Context::new();

// enable address parsing for this context
ctx.init(InitOptions{parse_address: true}).unwrap();

// these options are safe to persist and reuse between calls to `parse_address`.
// Note: `language` and `country` are technically options that libpostal will accept
// for purposes of parsing addresses, but it ignores them at present.
let mut opts = ParseAddressOptions::new();

// parse a single address into a `postal::Components` iterator
let comps = ctx.parse_address(
	"1234 Cherry Ln, Podunk TX", &mut opts)
	.unwrap();
for c in comps {
	dbg!(c);
}

```

*For more examples and usage, please refer to the tests or benchmarks.*

## Development setup

This will build `bindgen` bindings, run the tests, and run the benchmarks.

```
cargo build
cargo test -- --nocapture --test-threads 1
cargo bench

```

Note: `--test-threads 1` is required due to the single-threaded nature of `libpostal`.

## Release History

- 

0.2.6

  - Update bindgen and parking_lot, replace deprecated rustfmt_bindings with formatter for bindgen

- 

0.2.2

  - Resolve locking issue due to unbound Mutex guard.

- 

0.2.1

  - Make Component fields public.

- 

0.2.0

  - Added `parse_address` support.

- 

0.1.0

  - Initial release.

## Meta

Distributed under the MIT license. See `LICENSE` for more information.

## Contributing

- Fork it (https://github.com/pnordahl/rust-postal/fork)

- Create your feature branch (`git checkout -b feature/fooBar`)

- Commit your changes (`git commit -am 'Add some fooBar'`)

- Push to the branch (`git push origin feature/fooBar`)

- Create a new Pull Request