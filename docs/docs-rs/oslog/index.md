oslog 0.2.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                oslog-0.2.0
            
        
    

                
                

                    
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
                    oslog 0.2.0
                    
                

                
                A minimal safe wrapper around Apple's Logging system

                
                    

                        
                        
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
                                
                                    
                                    
                                        
                                            steven-joruk/oslog
                                        
                                        

                                         44
                                         12
                                         2

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                dashmap ^5.1.0
                
                    *normal*
                    
                
            
        
  - 
                log ^0.4.14
                
                    *normal*
                    
                
            
        
  - 
                cc ^1.0.73
                
                    *build*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.2.0** (2022-02-17)
        
        
         
        
  - 
            **0.1.0** (2021-02-16)
        
        
         
        
  - 
            **0.0.4** (2021-02-16)
        
        
         
        
  - 
            **0.0.3** (2020-06-19)
        
        
         
        
  - 
            **0.0.2** (2020-06-18)
        
        
         
        
  - 
            **0.0.1** (2020-05-14)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                    
                        docs.rs failed to build oslog-0.2.0
                        

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    

A minimal wrapper around Apple's unified logging system.

By default support for the log crate is provided, but if
you would prefer just to use the lower level bindings you can disable the
default features.

When making use of targets (`info!(target: "t", "m");`), you should be aware
that a new log is allocated and stored in a map for the lifetime of the program.
I expect log allocations are extremely small, but haven't attempted to verify
it.

## Logging example

This is behind the `logger` feature flag and is enabled by default.

```
fn main() {
    OsLogger::new("com.example.test")
        .level_filter(LevelFilter::Debug)
        .category_level_filter("Settings", LevelFilter::Trace)
        .init()
        .unwrap();

    // Maps to OS_LOG_TYPE_DEBUG
    trace!(target: "Settings", "Trace");

    // Maps to OS_LOG_TYPE_INFO
    debug!("Debug");

    // Maps to OS_LOG_TYPE_DEFAULT
    info!(target: "Parsing", "Info");

    // Maps to OS_LOG_TYPE_ERROR
    warn!("Warn");

    // Maps to OS_LOG_TYPE_FAULT
    error!("Error");
}

```

## Missing features

- Activities

- Tracing

- Native support for line numbers and file names.