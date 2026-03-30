singularity 0.8.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                singularity-0.8.0
            
        
    

                
                

                    
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
                    singularity 0.8.0
                    
                

                
                CLI tool for pulling known malicious domains into one or more blackhole lists in various formats.

                
                    

                        
                        
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
                                
                                    
                                     Repository
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                anyhow ^1.0.52
                
                    *normal*
                    
                
            
        
  - 
                chrono ^0.4.19
                
                    *normal*
                    
                
            
        
  - 
                confy ^0.4.0
                
                    *normal*
                    
                
            
        
  - 
                fern ^0.6.0
                
                    *normal*
                    
                
            
        
  - 
                indicatif ^0.16.2
                
                    *normal*
                    
                
            
        
  - 
                log ^0.4.14
                
                    *normal*
                    
                
            
        
  - 
                num-format ^0.4.0
                
                    *normal*
                    
                
            
        
  - 
                regex ^1.5.4
                
                    *normal*
                    
                
            
        
  - 
                serde ^1.0.132
                
                    *normal*
                    
                
            
        
  - 
                structopt ^0.3.25
                
                    *normal*
                    
                
            
        
  - 
                tempfile ^3.2.0
                
                    *normal*
                    
                
            
        
  - 
                thiserror ^1.0.30
                
                    *normal*
                    
                
            
        
  - 
                ureq ^2.4.0
                
                    *normal*
                    
                
            
        
  - 
                url ^2.2.2
                
                    *normal*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.8.0** (2021-12-31)
        
        
         
        
  - 
            **0.7.0** (2021-02-19)
        
        
         
        
  - 
            **0.6.1** (2021-02-05)
        
        
         
        
  - 
            **0.6.0** (2020-11-15)
        
        
         
        
  - 
            **0.5.1** (2020-09-27)
        
        
         
        
  - 
            **0.5.0** (2020-09-20)
        
        
         
        
  - 
            **0.4.0** (2020-09-15)
        
        
         
        
  - 
            **0.3.0** (2020-09-15)
        
        
         
        
  - 
            **0.2.1** (2020-09-15)
        
        
         
        
  - 
            **0.2.0** (2020-09-14)
        
        
         
        
  - 
            **0.1.0** (2020-09-13)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                        singularity-0.8.0 is not a library.
                    

                
# Singularity

CLI tool for pulling known malicious domains into a blackhole list. Primarily meant to be used with PDNS Recursor. The tool can pull in blackholed domains from multiple adlist sources and output them into multiple places in various formats.

Accompanying blog post.

## Install

Requires a stable build of Rust, preferably the latest one. Minimum supported version: 1.52.0.

- From crates.io: `cargo install singularity`

- From source: `cargo install --path .`

## Usage

- Basic usage: `singularity`

### CLI options

All CLI options can be seen with the `--help` flag. The options are:

- `-v`, `--verbose`: enable additional debug output to stdout

- `-c`, `--config`: a custom configuration file to use instead of the default

- `-t`, `--timeout`: timeout in milliseconds to wait for each HTTP request to succeed (default: 1000)

### Configuration file

By default, the tool will use a confiuration file in the current system-dependent location. On Linux, this is `$HOME/.config/singularity/singularity.conf`. The file will be created if it doesn't exist and will contain empty values.

Complete example configuration file:

```
whitelist = ["my-cool-domain.com"]

[[adlist]]
source = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
format = "hosts"

[[adlist]]
source = "file:/absolute/path"
format = "domains"

[[adlist]]
source = "https://raw.githubusercontent.com/notracking/hosts-blocklists/master/dnsmasq/dnsmasq.blacklist.txt"
format = "dnsmasq"

[[output]]
type = "hosts"
destination = "/etc/powerdns/hosts"
blackhole_address = "0.0.0.0"
include = ["extra-hosts"]

[[output]]
type = "hosts"
destination = "/etc/hosts"
deduplicate = true

[[output]]
type = "pdns-lua"
destination = "/etc/powerdns/blackhole.lua"
blackhole_address = "::"
output_metric = true
metric_name = "blocked-queries"

```

#### `whitelist`

An array of domains you wish to not include in the final output. These are matched exactly, so `google.com` will match only `google.com`, but not any of its subdomains. The configuration option can be left out entirely for a default empty whitelist.

#### `adlist`

An array of objects describing adlist sources. They have two keys:

- `source`: URL to the source of the adlist. The URL scheme can be `http`, `https` or `file`. If it's a `file` URL, its path will be interpreted as an absolute filesystem path in the local system.

- `format`: the format the adlist's entries are in. This option can be omitted for the default `hosts` value. The value can be one of:

  - `hosts`: standard `/etc/hosts`-style entries; `0.0.0.0 malicious.domain`. It is assumed the address in each entry is the unspecfied `0.0.0.0` IP address. Entries that have a different IP address or have an IP address as the domain are ignored.

  - `domains`: each line is just a domain name: `malicious.domain`.

  - `dnsmasq`: each line is an `address` or `server` configuration line for dnsmasq; `address=/example.com/#`

Regardless of the source or format, any lines in an adlist beginning with a `#` are ignored and will not be included in the output.

### `output`

An array of objects describing where and how to output the blackholed domains. The type of each output is specified with the `type` key. The possible types are:

- `hosts`: output a standard hosts-format where each line is in the format of `<blackhole_address> <name>`. Other hosts-files can be included in the output by settings their paths in the `include` array option.

- `pdns-lua`: output a Lua script that can be used with the `lua-dns-script` configuration option in PDNS Recursor. The script will have each blackholed domain hardcoded into it. By using the `preresolve()` function, the script will respond to queries for the blackholed domains with either an `A`-record or an `AAAA`-record containing the `blackhole_address`. The type of the record depends on whether the `blackhole_address` is an IPv4- or an IPv6-address. By default, the script will output a metric called `blocked-queries` that is incremented every time the script responds to a blocked domain. It is accessible through the same means as every other Recursor metric. It can be disabled with the `output_metric` setting, and the metric's name can be customised with the `metric_name` setting. Both settings can be omitted for their default values.

Additional configuration for every type of output:

- `blackhole_address`: the address used in the blackhole responses

- `deduplicate`: remove duplicate entries in the output. Duplicate entries may appear when using multiple sources.