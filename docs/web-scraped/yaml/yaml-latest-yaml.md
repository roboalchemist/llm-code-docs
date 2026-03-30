# Source: https://docs.rs/yaml/latest/yaml/

Title: yaml 0.3.0 - Docs.rs

URL Source: https://docs.rs/yaml/latest/yaml/

Markdown Content:
docs.rs failed to build yaml-0.3.0 

 Please check the [build logs](https://docs.rs/crate/yaml/latest/builds) for more information. 

 See [Builds](https://docs.rs/about/builds) for ideas on how to fix a failed build, or [Metadata](https://docs.rs/about/metadata) for how to configure docs.rs builds. 

 If you believe this is docs.rs' fault, [open an issue](https://github.com/rust-lang/docs.rs/issues/new/choose).

libyaml-rust
------------

[![Image 1: libyaml-rust on Travis CI](https://travis-ci.org/kimhyunkang/libyaml-rust.svg?branch=master)](https://travis-ci.org/kimhyunkang/libyaml-rust)[![Image 2: yaml on crates.io](http://meritbadge.herokuapp.com/yaml)](https://crates.io/crates/yaml)

[LibYAML](http://pyyaml.org/wiki/LibYAML) bindings for [Rust](http://www.rust-lang.org/)

Dependencies
------------

*   LibYAML 0.1.4 or higher
*   Stable Rust (2015/2018 edition)

Usage
-----

Parse from memory

```
extern crate yaml;

use yaml::constructor::*;

yaml::parse_bytes_utf8("[1, 2, 3]".as_bytes()); // => Ok(vec![YamlSequence(~[YamlInteger(1), YamlInteger(2), YamlInteger(3)])])
```

Parse from Reader

```
extern crate yaml;

use std::io::BufReader;
use yaml::constructor::*;

let data = "[1, 2, 3]";
let mut reader = BufReader::new(data.as_bytes());

yaml::parse_io_utf8(&mut reader); // => Ok(vec![YamlSequence(~[YamlInteger(1), YamlInteger(2), YamlInteger(3)])])
```

Todo
----

In the order of what I want to do...

*    Emitter functions
*    Document iterator
*    UTF-16 support
*   Complete YAML 1.1 specs 
    *    Tag support
    *   [Timestamp type](http://yaml.org/type/timestamp.html)
    *   [Int parser](http://yaml.org/type/int.html)
    *   [Float parser](http://yaml.org/type/float.html)

*    Token functions
