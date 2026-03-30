# Source: https://render.com/docs/rust-toolchain.md

# Specifying a Rust Toolchain

By default, Render uses the latest stable Rust toolchain, but you can specify a different toolchain by adding a [file called `rust-toolchain`](https://rust-lang.github.io/rustup/overrides.html?#the-toolchain-file) at the root of your repo. It should contain a single line specifying the version. For example:

```text
nightly-2020-03-15
```

or

```text
beta
```

You can also use the `RUSTUP_TOOLCHAIN` environment variable and set the value to a valid version. The environment variables overrides the version in toolchain files.

> If you override the toolchain in your build command with `cargo +nightly...` the specified toolchain must already be installed. You can install new toolchains using `rustup` as part of your build command.

Learn more about [Rust toolchains](https://rust-lang.github.io/rustup/concepts/toolchains.html).