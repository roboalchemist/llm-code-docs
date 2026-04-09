asciinema 3.2.0 - Docs.rs

                    Docs.rs
                

    
-

                asciinema-3.2.0
            
        
    

                
                

                    
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

                    asciinema 3.2.0
                    
                

                
                Terminal session recorder, streamer, and player

                
                    

                        
                        
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
                                Source code size: 1.64 MB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Links

-

                                     Homepage

-

                                            asciinema/asciinema

                                         16980
                                         1011
                                         1

                                    
                            
                        
-

                                 crates.io
                            
                        

                        
- Dependencies

-

-
                anyhow ^1.0
                
                    *normal*
                    
                
            
        
-
                async-trait ^0.1
                
                    *normal*
                    
                
            
        
-
                avt ^0.17
                
                    *normal*
                    
                
            
        
-
                axum ^0.8
                
                    *normal*
                    
                
            
        
-
                bytes ^1.11
                
                    *normal*
                    
                
            
        
-
                clap ^4.0
                
                    *normal*
                    
                
            
        
-
                config ^0.15
                
                    *normal*
                    
                
            
        
-
                futures-util ^0.3
                
                    *normal*
                    
                
            
        
-
                nix ^0.30
                
                    *normal*
                    
                
            
        
-
                rand ^0.9
                
                    *normal*
                    
                
            
        
-
                reqwest ^0.12
                
                    *normal*
                    
                
            
        
-
                rgb ^0.8
                
                    *normal*
                    
                
            
        
-
                rust-embed ^8.8
                
                    *normal*
                    
                
            
        
-
                rustls ^0.23
                
                    *normal*
                    
                
            
        
-
                rustyline ^17.0
                
                    *normal*
                    
                
            
        
-
                serde ^1.0
                
                    *normal*
                    
                
            
        
-
                serde_json ^1.0
                
                    *normal*
                    
                
            
        
-
                signal-hook ^0.3
                
                    *normal*
                    
                
            
        
-
                signal-hook-tokio ^0.3
                
                    *normal*
                    
                
            
        
-
                tempfile ^3.23
                
                    *normal*
                    
                
            
        
-
                tokio ^1.40
                
                    *normal*
                    
                
            
        
-
                tokio-stream ^0.1
                
                    *normal*
                    
                
            
        
-
                tokio-tungstenite ^0.28
                
                    *normal*
                    
                
            
        
-
                tokio-util ^0.7
                
                    *normal*
                    
                
            
        
-
                tower-http ^0.6
                
                    *normal*
                    
                
            
        
-
                tracing ^0.1
                
                    *normal*
                    
                
            
        
-
                tracing-subscriber ^0.3.20
                
                    *normal*
                    
                
            
        
-
                url ^2.5
                
                    *normal*
                    
                
            
        
-
                uuid ^1.6
                
                    *normal*
                    
                
            
        
-
                which ^8.0
                
                    *normal*
                    
                
            
        
-
                clap ^4.0
                
                    *build*
                    
                
            
        
-
                clap_complete ^4.0
                
                    *build*
                    
                
            
        
-
                clap_mangen ^0.2
                
                    *build*
                    
                
            
        
-
                url ^2.5
                
                    *build*
                    
                
            
        
                                

                            
                        

                        
- Versions

-

-
            **3.2.0** (2026-03-01)
        
        
         
        
-
            **3.1.0** (2026-01-14)
        
        
         
        
-
            **3.0.1** (2025-10-24)
        
        
         
        
-
            **3.0.0** (2025-09-17)
        
        
         
        
-
            **3.0.0-rc.5** (2025-06-26)
        
        
         
        
-
            **3.0.0-rc.3** (2024-06-26)
        
        
         
        
-
            **3.0.0-rc.2** (2024-05-07)
        
        
         
        
-
            **3.0.0-rc.1** (2024-04-17)
        
        
         
        
-
            **3.0.0-beta.3** (2024-02-08)
        
        
         
        
-
            **3.0.0-beta.2** (2024-01-28)
        
        
         
        
-
            **3.0.0-beta.1** (2024-01-23)
        
        
         
        
-
            **3.0.0-alpha.8** (2024-01-22)
        
        
         
        
-
            **3.0.0-alpha.7** (2024-01-19)
        
        
         
        
-
            **3.0.0-alpha.6** (2024-01-10)
        
        
         
        
-
            **3.0.0-alpha.5** (2024-01-03)
        
        
         
        
-
            **3.0.0-alpha.4** (2023-12-28)
        
        
         
        
-
            **3.0.0-alpha.3** (2023-12-26)
        
        
         
        
-
            **3.0.0-alpha.2** (2023-12-23)
        
        
         
        
-
            **3.0.0-alpha.1** (2023-10-22)
        
                                

                            
                        

                        
                        
- Owners

-

                        asciinema-3.2.0 is not a library.

# asciinema

**asciinema** (aka asciinema CLI or asciinema recorder) is a command-line tool
for recording and live streaming terminal sessions.

Unlike typical *screen* recording software, which records visual output of a
screen into a heavyweight video files (`.mp4`, `.mov`), asciinema CLI runs
*inside a terminal*, capturing terminal session output into a lightweight
recording files in the
asciicast format (`.cast`),
or streaming it live to viewers in real-time.

The recordings can be replayed in a terminal, embedded on a web page with the
asciinema player, or published to
an asciinema server, such as
asciinema.org, for further sharing. Live streams allow
viewers to watch terminal sessions as they happen.

asciinema runs on GNU/Linux, macOS and FreeBSD.

Notable features:

- recording and replaying of sessions inside a terminal,

- local and remote live
streaming
of terminal sessions to multiple viewers in real-time,

- lightweight recording
format, which is highly
compressible (down to 15% of the original size e.g. with `zstd` or `gzip`),

- integration with asciinema
server, e.g.
asciinema.org, for easy recording hosting and live
streaming.

To record a session run this command in your shell:

```
asciinema rec demo.cast

```

To stream a session via built-in HTTP server run:

```
asciinema stream -l

```

To stream a session via a relay (asciinema server) run:

```
asciinema stream -r

```

Check out the Getting started
guide for installation and usage
overview.

## Building

Building asciinema from source requires the Rust
compiler (1.82 or later), and the Cargo package
manager. If they are not available via your
system package manager then use rustup.

To download the source code, build the asciinema binary, and install it in
`$HOME/.cargo/bin` in one go run:

```
cargo install --locked --git https://github.com/asciinema/asciinema

```

Then, ensure `$HOME/.cargo/bin` is in your shell's `$PATH`.

Alternatively, you can manually download the source code and build the asciinema
binary with:

```
git clone https://github.com/asciinema/asciinema
cd asciinema
cargo build --release

```

This produces the binary at `target/release/asciinema`. You can just copy the
binary to a directory in your `$PATH`.

To generate man pages and shell completion files, set `ASCIINEMA_GEN_DIR` to the
path where these artifacts should be stored. For example:

```
ASCIINEMA_GEN_DIR=/foo cargo build --release

```

The above command will build the binary and place the man pages in `/foo/man/`,
and the shell completion files in the `/foo/completion/` directory.

[!NOTE]
Windows is currently not supported. See #467.
You can try PowerSession instead.

## Development

All development happens on `develop` branch. This branch contains the current
generation (3.x) of the asciinema CLI, written in Rust.

The previous generation (2.x), written in Python, can be found in the `python`
branch.

If you wish to propose non-trivial code changes, please first reach out to the
team via forum,
Matrix or
IRC.

## Donations

Sustainability of asciinema development relies on donations and sponsorships.

If you like the project then consider becoming a
supporter or a corporate
sponsor.

asciinema is sponsored by:

- Brightbox

## Consulting

If you're interested in integration or customization of asciinema to suit your
needs, check asciinema consulting
services.

## License

© 2011 Marcin Kulik.

All code is licensed under the GPL, v3 or later. See LICENSE file
for details.
