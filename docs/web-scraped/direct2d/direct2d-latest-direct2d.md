# Source: https://docs.rs/direct2d/latest/direct2d/

Title: direct2d 0.2.0 - Docs.rs

URL Source: https://docs.rs/direct2d/latest/direct2d/

Markdown Content:
direct2d 0.2.0 - Docs.rs
===============

[Docs.rs](https://docs.rs/)
*   [direct2d-0.2.0](https://docs.rs/crate/direct2d/latest "A safe abstraction for drawing with Direct2D")

*   [docs.rs](https://docs.rs/direct2d/latest/direct2d/#)
    *   [About docs.rs](https://docs.rs/about)
    *   [Badges](https://docs.rs/about/badges)
    *   [Builds](https://docs.rs/about/builds)
    *   [Metadata](https://docs.rs/about/metadata)
    *   [Shorthand URLs](https://docs.rs/about/redirections)
    *   [Download](https://docs.rs/about/download)
    *   [Rustdoc JSON](https://docs.rs/about/rustdoc-json)
    *   [Build queue](https://docs.rs/releases/queue)
    *   [Privacy policy](https://foundation.rust-lang.org/policies/privacy-policy/#docs.rs)

*   [Rust](https://docs.rs/direct2d/latest/direct2d/#)
    *   [Rust website](https://www.rust-lang.org/)
    *   [The Book](https://doc.rust-lang.org/book/)
    *   [Standard Library API Reference](https://doc.rust-lang.org/std/)
    *   [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
    *   [The Cargo Guide](https://doc.rust-lang.org/cargo/guide/)
    *   [Clippy Documentation](https://doc.rust-lang.org/nightly/clippy)

direct2d 0.2.0
==============

A safe abstraction for drawing with Direct2D

*   [Crate](https://docs.rs/crate/direct2d/latest)
*   [Source](https://docs.rs/crate/direct2d/latest/source/)
*   [Builds](https://docs.rs/crate/direct2d/latest/builds)
*   [Feature flags](https://docs.rs/crate/direct2d/latest/features)

*   Links
*   [Connicpu/direct2d-rs 34 10 2](https://github.com/Connicpu/direct2d-rs)
*   [crates.io](https://crates.io/crates/direct2d "See direct2d on crates.io")
*   Dependencies
*   
    *   [directwrite ^0.1.3 _normal_](https://docs.rs/crate/directwrite/^0.1.3)
    *   [dxgi ^0.1.6 _normal_](https://docs.rs/crate/dxgi/^0.1.6)
    *   [either ^1.5.0 _normal_](https://docs.rs/crate/either/^1.5.0)
    *   [winapi ^0.3.5 _normal_](https://docs.rs/crate/winapi/^0.3.5)
    *   [wio ^0.2 _normal_](https://docs.rs/crate/wio/^0.2)
    *   [direct3d11 ^0.1.3 _dev_](https://docs.rs/crate/direct3d11/^0.1.3)
    *   [image ^0.18.0 _dev_](https://docs.rs/crate/image/^0.18.0)
    *   [lazy_static ^1.0 _dev_](https://docs.rs/crate/lazy_static/^1.0)
    *   [rand ^0.4 _dev_](https://docs.rs/crate/rand/^0.4)

*   Versions
*   
    *   [**0.3.0-alpha1** (2019-02-24)](https://docs.rs/crate/direct2d/0.3.0-alpha1)
    *   [**0.2.0** (2018-10-23)](https://docs.rs/crate/direct2d/0.2.0)
    *   [**0.1.4** (2018-09-26)](https://docs.rs/crate/direct2d/0.1.4)
    *   [**0.1.3** (2018-09-12)](https://docs.rs/crate/direct2d/0.1.3)
    *   [**0.1.2** (2018-04-27)](https://docs.rs/crate/direct2d/0.1.2)
    *   [**0.1.1** (2018-04-26)](https://docs.rs/crate/direct2d/0.1.1)
    *   [**0.1.0** (2018-04-25)](https://docs.rs/crate/direct2d/0.1.0)
    *   [**0.0.9** (2018-03-17)](https://docs.rs/crate/direct2d/0.0.9)
    *   [**0.0.8** (2018-03-16)](https://docs.rs/crate/direct2d/0.0.8)
    *   [**0.0.6** (2017-04-16)](https://docs.rs/crate/direct2d/0.0.6)
    *   [**0.0.5** (2016-02-24)](https://docs.rs/crate/direct2d/0.0.5 "docs.rs failed to build direct2d-0.0.5")
    *   [**0.0.4** (2016-01-10)](https://docs.rs/crate/direct2d/0.0.4 "docs.rs failed to build direct2d-0.0.4")
    *   [**0.0.3** (2016-01-09)](https://docs.rs/crate/direct2d/0.0.3 "docs.rs failed to build direct2d-0.0.3")
    *   [**0.0.2** (2015-12-13)](https://docs.rs/crate/direct2d/0.0.2 "docs.rs failed to build direct2d-0.0.2")
    *   [**0.0.1** (2015-12-12)](https://docs.rs/crate/direct2d/0.0.1 "docs.rs failed to build direct2d-0.0.1")

*   Owners
*   [![Image 1: Connicpu](https://avatars.githubusercontent.com/u/967877?v=4)](https://crates.io/users/Connicpu)

direct2d-0.2.0 doesn't have any documentation.

Safe abstractions for drawing on Windows using Direct2D

Example
-------

```
extern crate direct2d;

use direct2d::{DeviceContext, RenderTarget};
use direct2d::brush::SolidColorBrush;
use direct2d::image::Bitmap;

fn draw(context: &mut DeviceContext, target: &Bitmap) {
    let brush = SolidColorBrush::create(&context)
        .with_color(0xFF_7F_7F)
        .build().unwrap();

    context.begin_draw();
    context.set_target(target);
    context.clear(0xFF_FF_FF);
    
    context.draw_line((10.0, 10.0), (20.0, 20.0), &brush, 2.0, None);
    context.draw_line((10.0, 20.0), (20.0, 10.0), &brush, 2.0, None);

    match context.end_draw() {
        Ok(_) => {/* cool */},
        Err(_) => panic!("Uh oh, rendering failed!"),
    }
}
```
