pmd 0.0.1 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                pmd-0.0.1
            
        
    

                
                

                    
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
                    pmd 0.0.1
                    
                

                
                Poor's man debugger, the most easy way to debug

                
                    

                        
                        
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
                                
                                    
                                    
                                        
                                            nkoporec/pmd
                                        
                                        

                                         0
                                         0
                                         0

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                axum ^0.6.2
                
                    *normal*
                    
                
            
        
  - 
                clap ^4.1.1
                
                    *normal*
                    
                
            
        
  - 
                crossterm ^0.25
                
                    *normal*
                    
                
            
        
  - 
                home ^0.5.4
                
                    *normal*
                    
                
            
        
  - 
                rust-embed ^6.4.2
                
                    *normal*
                    
                
            
        
  - 
                serde ^1.0.136
                
                    *normal*
                    
                
            
        
  - 
                serde_json ^1.0.91
                
                    *normal*
                    
                
            
        
  - 
                tokio ^1
                
                    *normal*
                    
                
            
        
  - 
                toml ^0.5.10
                
                    *normal*
                    
                
            
        
  - 
                tui ^0.19
                
                    *normal*
                    
                
            
        
  - 
                tui-tree-widget ^0.11.0
                
                    *normal*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.0.1** (2023-01-27)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                        pmd-0.0.1 is not a library.
                    

                
# Poor's man debugger

The most simple way to debug your code.

This is a simple TUI debugger, it starts a local server that accepts payloads from the adapters. Everything goes through HTTP requests, so it's very fast compared to other solutions.
You can think of it as a console.log(), but instead of the browser you use the terminal and it works with any language.

## Requirements

- PMD-adapter for your language installed in the project.

## Installation

You can install it via cargo.

- Install cargo (https://doc.rust-lang.org/cargo/)

- Run `cargo install pmd`

## Configuration

The default config is located at ~/.config/pmd/config.toml (for UNIX like systems) or ~/.pmd/config.toml (for Windows).

You can override the default config by passing a -c (--config) flag that points to the config.toml file.

### Keybindings

Keybindings are VIM-like. The `leader` key is set by default to `,` , but you can override this via config.

Debugger consists of three input states

- Normal

- Visual

- Inspection

### Normal

Normal mode enables you to scroll all the breakpoints and callstack data.

It has the following keybindings:

- `j` (or `Down arrow`) -> Move down the list

- `k` (or `Up arrow`) -> Move up the list

- `<leader> + h` -> Move to the left

- `<leader> + l` -> Move to the right

- `i` -> Set inspection mode, to inspect the dumped variables

- `v` -> Set visual mode and open the selected breakpoint/callstack in a popup for more details.

- `q` -> Quit

### Visual

Visual mode is meant to show additional data that are not present in normal mode for breakpoints/callstack.

It has the following keybindings:

- `q` -> Quit

- `ESC` -> Go to normal mode

### Inspection

Inspection mode enables you to inspect the tree-like data that were sent by the adapters.

It has the following keybindings:

- `j` (or `Down arrow`) -> Move down the tree

- `k` (or `Up arrow`) -> Move up the tree

- `h` -> Close the selected item

- `l` -> Expand selected item.

- `q` -> Quit

- `ESC` -> Go to normal mode

## Adapters

Adapters are language specific packages that sends the actual debug data to PMD via HTTP.

Currently supported

- PHP (https://github.com/nkoporec/pmd-php}

### Adapter API

An example API for an adapter

```
curl --request POST \
  --url http://localhost:6969/dump \
  --header 'Content-Type: application/json' \
  --data '{
        "timestamp": "3223232",
        "line": "6",
        "connector_type": "php",
        "filepath": "/home/project/drupal/web/index.php",
        "callstack": [
                {
                        "filepath": "/home/project/drupal/web/index.php",
                        "line": "10"
                }
        ],
        "payload": ""
}'

```

Types:

- timestamp -> String

- line -> String

- connector_type -> String

- filepath -> String

- callstack -> Array (where key is a line number (int), and value is a file path (string)

- payload -> JSON encoded string

## Security Vulnerabilities

For any security vulnarabilities please send an email to hey@nkoporec.com

## Credits

- nkoporec

- All Contributors

## License

The MIT License (MIT). Please see License File for more information.