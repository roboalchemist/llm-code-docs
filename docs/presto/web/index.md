presto 0.1.1 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                presto-0.1.1
            
        
    

                
                

                    
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
                    presto 0.1.1
                    
                

                
                A simple TUI music player with Vim bindings

                
                    

                        
                        
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
                                Source code size: 301.09 kB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Links
                        
- 
                                
                                     Homepage
                                
                            
- 
                                
                                    
                                    
                                        
                                            mrs4ndman/presto
                                        
                                        

                                         8
                                         0
                                         0

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                async-io ^2.6.0
                
                    *normal*
                    
                
            
        
  - 
                config ^0.15.19
                
                    *normal*
                    
                
            
        
  - 
                crossterm ^0.29.0
                
                    *normal*
                    
                
            
        
  - 
                lofty ^0.23
                
                    *normal*
                    
                
            
        
  - 
                rand ^0.10
                
                    *normal*
                    
                
            
        
  - 
                ratatui ^0.30.0
                
                    *normal*
                    
                
            
        
  - 
                rodio ^0.21.1
                
                    *normal*
                    
                
            
        
  - 
                serde ^1
                
                    *normal*
                    
                
            
        
  - 
                toml ^0.9.12
                
                    *normal*
                    
                
            
        
  - 
                walkdir ^2.5.0
                
                    *normal*
                    
                
            
        
  - 
                zbus ^5.13.2
                
                    *normal*
                    
                
            
        
  - 
                zvariant ^5.9.2
                
                    *normal*
                    
                
            
        
  - 
                tempfile ^3
                
                    *dev*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.1.1** (2026-03-08)
        
        
         
        
  - 
            **0.1.0** (2026-02-13)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                        presto-0.1.1 is not a library.
                    

                
# presto

A simple music player TUI written in Rust, with Vim-like controls.

## Features

- Directory scan of common audio files (`mp3`, `flac`, `wav`, `ogg`)

- Keyboard-driven TUI with Vim-like controls

- `/` filter with word-by-word fuzzy matching

- `Ctrl+e` exits filter input without starting playback

- Right-sid panes for metadata and embedded lyrics (opened up with `K` / `gl`)

- Opt-in lyrics loading via config, with timed-line emphasis for synced lyrics

- MPRIS integration for `playerctl` / media keys

- Per-directory state persistence (selection, filter, shuffle, loop, volume, last track)

- Number-driven movement for `hjkl` skipping / navigation

## Getting started

- Dependencies:

  - `rodio` requirements

  - `libasound2-dev` (on Ubuntu-based at least)

### `crates.io`

- The version uploaded to `crates.io` is the one on the develop branch:

```
cargo install presto

```

### From source

- Build: `cargo build`

- Run: `cargo run -- [music_dir]`

  - If `music_dir` is omitted, it defaults to the current directory

## Docs

Visit the web version or start with
docs/README.md

## TODO:

Finished TODOs will migrate onto the changelog.

### Short-term

-  Enabling re-ordering / disabling some status sections

### Long-term

-  Listening stats (amount, usage, recent songs, etc.)

-  Theming

-  Cross-platform compatibility (config/state paths, media controls, audio backend support)

-  Server-client restructuring

## ↓ Current status ↓

[!CAUTION]
VERY LOUD, will try to record it next time with less volume

https://github.com/user-attachments/assets/34407dda-7599-4ec2-a0af-66889ef6251a