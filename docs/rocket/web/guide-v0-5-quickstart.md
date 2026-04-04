# Source: https://rocket.rs/guide/v0.5/quickstart/

Title: Quickstart - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.5/quickstart/

Markdown Content:
Quickstart - Rocket Web Framework
===============

![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

[Rocket Homepage](https://rocket.rs/)- [x] [overview](https://rocket.rs/overview/)[guide](https://rocket.rs/guide/v0.5/)[faq](https://rocket.rs/guide/v0.5/faq/#faq)[news](https://rocket.rs/news/)[docs](https://api.rocket.rs/v0.5/rocket/)[![Image 7: GitHub octocat](https://rocket.rs/images/github-mark-white.svg)](https://github.com/rwf2/Rocket/tree/v0.5.1)

[Guide](https://rocket.rs/guide/v0.5/)
======================================

v0.5

[v0.4](https://rocket.rs/guide/v0.4/)[v0.3](https://rocket.rs/guide/v0.3/)[master](https://rocket.rs/guide/master/)

#### The ins and outs of Rocket, in detail

* [Introduction](https://rocket.rs/guide/v0.5/introduction/#introduction)

* [Upgrading](https://rocket.rs/guide/v0.5/upgrading/#upgrading)

* [Quickstart](https://rocket.rs/guide/v0.5/quickstart/#quickstart)
  * [Running Examples](https://rocket.rs/guide/v0.5/quickstart/#running-examples)

* [Getting Started](https://rocket.rs/guide/v0.5/getting-started/#getting-started)

* [Overview](https://rocket.rs/guide/v0.5/overview/#overview)

* [Requests](https://rocket.rs/guide/v0.5/requests/#requests)

* [Responses](https://rocket.rs/guide/v0.5/responses/#responses)

* [State](https://rocket.rs/guide/v0.5/state/#state)

* [Fairings](https://rocket.rs/guide/v0.5/fairings/#fairings)

* [Testing](https://rocket.rs/guide/v0.5/testing/#testing)

* [Configuration](https://rocket.rs/guide/v0.5/configuration/#configuration)

* [Deploying](https://rocket.rs/guide/v0.5/deploying/#deploying)

* [Pastebin Tutorial](https://rocket.rs/guide/v0.5/pastebin/#pastebin-tutorial)

* [Conclusion](https://rocket.rs/guide/v0.5/conclusion/#conclusion)

* [FAQ](https://rocket.rs/guide/v0.5/faq/#faq)

[](https://rocket.rs/guide/v0.5/quickstart/#quickstart "anchor")Quickstart
==========================================================================

Before you can start writing a Rocket application, you'll need to install the Rust toolchain. We recommend using [rustup](https://rustup.rs/). If you don't have Rust installed and would like extra guidance doing so, see [Getting Started](https://rocket.rs/guide/v0.5/getting-started/).

[](https://rocket.rs/guide/v0.5/quickstart/#running-examples "anchor")Running Examples
--------------------------------------------------------------------------------------

The absolute fastest way to start experimenting with Rocket is to clone the Rocket repository and run the included examples in the `examples/` directory. For instance, the following set of commands runs the `hello` example:

1
2
3
4
5 git clone https://github.com/rwf2/Rocket cd Rocket git checkout v0.5 cd examples/hello cargo run

There are numerous examples in the `examples/` directory. They can all be run with `cargo run`.

The examples' `Cargo.toml` files will point to the locally cloned `rocket` libraries. When copying the examples for your own use, you should modify the `Cargo.toml` files as explained in the [Getting Started](https://rocket.rs/guide/v0.5/getting-started/) guide.

* * *

[◄ Upgrading](https://rocket.rs/guide/v0.5/upgrading/)

[](https://rocket.rs/guide/v0.5/upgrading/)

[](https://rocket.rs/guide/v0.5/upgrading/)[Getting Started ►](https://rocket.rs/guide/v0.5/getting-started/)

* * *

[© 2016-2025 Sergio Benitez](https://sergio.bz/)

![Image 8: Small Rocket Logo](https://rocket.rs/images/logo-small.svg)

[BACK TO TOP Δ](https://rocket.rs/guide/v0.5/quickstart/#)

![Image 9: cloud](https://rocket.rs/images/cloud-0.png)![Image 10: cloud](https://rocket.rs/images/cloud-1.png)![Image 11: cloud](https://rocket.rs/images/cloud-2.png)
