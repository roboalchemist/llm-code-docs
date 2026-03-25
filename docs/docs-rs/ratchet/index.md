ratchet 1.2.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                ratchet-1.2.0
            
        
    

                
                

                    
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
                    ratchet 1.2.0
                    
                

                
                A cryptographicly secure pseudo random bytes stream

                
                    

                        
                        
- 
                                
                                 Crate
                            
                        

                        
                        
- 
                            
                                
                                 Source
                            
                        

                        
                        
- 
                            
                                
                                 Builds
                            
                        

                        
                        
- 
                            
                                
                                Feature flags
                            
                        
                    

                
            
    

        
            
                
                    

- Size
                            
- 
                                Source code size: 20.12 kB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Links
                        
- 
                                
                                    
                                    
                                        
                                            Dynisious/double-ratchet
                                        
                                        

                                         0
                                         0
                                         0

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                clear_on_drop ^0.2
                
                    *normal*
                    
                
            
        
  - 
                digest ^0.8
                
                    *normal*
                    
                
            
        
  - 
                hkdf ^0.8
                
                    *normal*
                    
                
            
        
  - 
                rand_core ^0.5
                
                    *normal*
                    
                
            
        
  - 
                serde ^1
                
                    *normal*
                    
                        *optional*
                    
                
            
        
  - 
                rand ^0.7
                
                    *dev*
                    
                
            
        
  - 
                serde_cbor ^0.11
                
                    *dev*
                    
                
            
        
  - 
                sha-1 ^0.8
                
                    *dev*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **1.2.0** (2020-03-11)
        
        
         
        
  - 
            **1.1.0** (2019-05-12)
        
        
         
        
  - 
            **1.0.1** (2019-05-12)
        
        
         
        
  - 
            **1.0.0** (2019-05-11)
        
        
         
        
  - 
            **0.1.2** (2019-05-04)
        
        
         
        
  - 
            **0.1.1** (2019-05-04)
        
        
         
        
  - 
            **0.1.0** (2019-05-04)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                ratchet-1.2.0 doesn't have any documentation.

Defines the [Ratchet] struct.

A [Ratchet] is a cryptographically secure pseudo random number generator.

use `--features serde` to provide serde implementations.

# Examples

```
use ratchet::typenum::consts;
use sha1::Sha1;
use rand_core::RngCore;

let mut ratchet = ratchet::Ratchet::<Sha1, consts::U100, consts::U5,>::default();
let mut bytes = [0; 1024];

ratchet.fill_bytes(&mut bytes,);

```

Author -- DMorgan

Last Moddified --- 2020-03-11