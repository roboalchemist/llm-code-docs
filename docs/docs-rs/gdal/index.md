gdal 0.19.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                gdal-0.19.0
            
        
    

                
                

                    
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
                    gdal 0.19.0
                    
                

                
                GDAL bindings for Rust

                
                    

                        
                        
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
                                Source code size: 713.15 kB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Ø build duration
- 
                                    all releases: 36s
                                        Average build duration of **successful** builds in releases after 2024-10-23.
                                        
                                    
                                
- Links
                        
- 
                                
                                    
                                    
                                        
                                            georust/gdal
                                        
                                        

                                         434
                                         107
                                         45

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                bitflags ^2.10
                
                    *normal*
                    
                
            
        
  - 
                chrono ^0.4.26
                
                    *normal*
                    
                
            
        
  - 
                gdal-src ^0.3
                
                    *normal*
                    
                        *optional*
                    
                
            
        
  - 
                gdal-sys ^0.12
                
                    *normal*
                    
                
            
        
  - 
                geo-types ^0.7.18
                
                    *normal*
                    
                
            
        
  - 
                ndarray ^0.17
                
                    *normal*
                    
                        *optional*
                    
                
            
        
  - 
                thiserror ^2.0
                
                    *normal*
                    
                
            
        
  - 
                arrow-array ^57.1
                
                    *dev*
                    
                
            
        
  - 
                tempfile ^3.8
                
                    *dev*
                    
                
            
        
  - 
                semver ^1.0
                
                    *build*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **0.19.0** (2025-12-23)
        
        
         
        
  - 
            **0.18.0** (2025-03-28)
        
        
         
        
  - 
            **0.17.1** (2024-09-22)
        
        
         
        
  - 
            **0.17.0** (2024-07-26)
        
        
         
        
  - 
            **0.16.0** (2023-08-24)
        
        
         
        
  - 
            **0.15.0** (2023-06-02)
        
        
         
        
  - 
            **0.14.0** (2022-11-10)
        
        
         
        
  - 
            **0.13.0** (2022-09-02)
        
        
         
        
  - 
            **0.12.0** (2022-01-19)
        
        
         
        
  - 
            **0.11.0** (2021-11-10)
        
        
         
        
  - 
            **0.10.0** (2021-10-08)
        
        
         
        
  - 
            **0.9.0** (2021-08-06)
        
        
         
        
  - 
            **0.8.0** (2021-04-27)
        
        
         
        
  - 
            **0.7.2** (2021-01-05)
        
        
         
        
  - 
            **0.7.1** (2021-01-03)
        
        
         
        
  - 
            **0.7.0** (2020-12-19)
        
        
         
        
  - 
            **0.6.0** (2020-02-02)
        
        
         
        
  - 
            **0.5.0** (2019-01-03)
        
        
         
        
  - 
            **0.4.0** (2018-05-27)
        
        
         
        
  - 
            **0.3.0** (2017-10-08)
        
        
         
        
  - 
            **0.2.1** (2016-05-28)
        
        
         
        
  - 
            **0.2.0** (2016-05-09)
        
        
         
        
  - 
            **0.1.1** (2016-01-03)
        
        
         
        
  - 
            **0.1.0** (2015-07-12)
        
        
         
        
  - 
            **0.0.1** (2015-01-21)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                                    
                                
                    

                
            

            
                
                    
                        docs.rs failed to build gdal-0.19.0
                        

                        Please check the
                        build logs for more information.
                        

                        See Builds for ideas on how to fix a failed build,
                        or Metadata for how to configure docs.rs builds.
                        

                        If you believe this is docs.rs' fault, open an issue.
                    
                        Visit the last successful build:
                        
                            gdal-0.18.0
                        
                    
# GDAL

GDAL is a translator and processing library for various raster and vector geospatial data formats.

This crate provides safe, idiomatic Rust bindings for GDAL.

## Capabilities

GDAL is an incredibly powerful library. For a general understanding of its capabilities, a good place to get started is the GDAL User-oriented documentation. These features include:

- Opening raster and vector file formats for reading/writing

- Translating between file formats

- Reading and writing metadata in raster and vector datasets

- Accessing raster bands and their metadata

- Reading and writing geospatial coordinate system and projection values

- Warping (resampling and re-projecting) between coordinate systems

## Documentation

This crate's API documentation is hosted on docs.rs.

The Rust documentation is currently a work in progress, and may not cover requisite details on parameter semantics, value interpretation, etc.
Therefore, the authoritative documentation is that of GDAL in the form of its C and C++ APIs.
The former is technically what this crate calls, but the latter is usually more clear and better documented.

## Usage

This crate provides high-level, idiomatic Rust bindings for GDAL.
To do that, it uses `gdal-sys` internally, a low-level interface to the GDAL C library, which is generated using `bindgen`.
Using the `gdal-sys` crate directly is normally not needed, but it can be useful in order to call APIs that have not yet been exposed in `gdal`.

## Version support

As a general rule, only GDAL versions in Ubuntu LTS-1 (previous LTS version, that is, GDAL 3.4 in 22.04 at this moment) and newer are supported.
`gdal-sys` might support earlier versions using the `bindgen` feature flag, but `gdal` does not.

Building this crate assumes a compatible version of GDAL is installed with the corresponding header files and shared libraries.
This repository includes pre-generated bindings for GDAL 3.4 through 3.11 (see the `gdal-sys/prebuilt-bindings` directory).
If you're compiling against another version of GDAL, you can enable the `bindgen` feature flag to have the bindings generated on the fly.

## Community

This crate is part of the expansive (and expanding!) `georust` organization. Come join our discussions on Discord!

## Contributing

This crate continues to evolve, and PRs are always welcome. Make sure you are comfortable with the Code of Conduct and License before submitting a PR.

## License

This library is released under the MIT license