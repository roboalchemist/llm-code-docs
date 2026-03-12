# Source: https://swc.rs/

Title: Rust-based platform for the Web

URL Source: https://swc.rs/

Markdown Content:
Rust-based platform for the Web
===============
[Skip to Content](https://swc.rs/#nextra-skip-nav)[![Image 1](https://swc.rs/logo.png)SWC Speedy Web Compiler](https://swc.rs/)

[Docs](https://swc.rs/docs/getting-started)[Playground](https://swc.rs/playground)[Blog](https://swc.rs/blog/perf-swc-vs-babel)

[](https://github.com/swc-project/swc)[](https://discord.gg/GnHbXTdZz6)
*   Docs

    *   [Getting Started](https://swc.rs/docs/getting-started)
    *   Usage

        *   [@swc/cli](https://swc.rs/docs/usage/cli)
        *   [@swc/core](https://swc.rs/docs/usage/core)
        *   [@swc/wasm](https://swc.rs/docs/usage/wasm)
        *   [@swc/jest](https://swc.rs/docs/usage/jest)
        *   [swc-loader](https://swc.rs/docs/usage/swc-loader)
        *   [@swc/html](https://swc.rs/docs/usage/html)
        *   [Bundling](https://swc.rs/docs/usage/bundling)

    *   Configuration

        *   [.swcrc](https://swc.rs/docs/configuration/swcrc)
        *   [Compilation](https://swc.rs/docs/configuration/compilation)
        *   [Supported Browsers](https://swc.rs/docs/configuration/supported-browsers)
        *   [Modules](https://swc.rs/docs/configuration/modules)
        *   [Minification](https://swc.rs/docs/configuration/minification)
        *   [Bundling](https://swc.rs/docs/configuration/bundling)

    *   Plugin

        *   [Selecting swc_core](https://swc.rs/docs/plugin/selecting-swc-core)
        *   ECMAScript

            *   [Getting started](https://swc.rs/docs/plugin/ecmascript/getting-started)
            *   [Cheatsheet](https://swc.rs/docs/plugin/ecmascript/cheatsheet)
            *   [Compatibility](https://swc.rs/docs/plugin/ecmascript/compatibility)

        *   [Publishing](https://swc.rs/docs/plugin/publishing)

    *   Contributing

        *   Commons

            *   [String Management](https://swc.rs/docs/contributing/commons/string-management)

        *   ECMAScript Commons

            *   [Variable Management](https://swc.rs/docs/contributing/es-commons/variable-management)

        *   ECMAScript Minifier

            *   [Profiling](https://swc.rs/docs/contributing/es-minifier/profiling)
            *   [Debugging Next.js App](https://swc.rs/docs/contributing/es-minifier/debugging-nextjs-app)
            *   [Debugging size difference between SWC and Terser](https://swc.rs/docs/contributing/es-minifier/debugging-size)

    *   [The Team](https://swc.rs/docs/team)
    *   [Roadmap](https://swc.rs/docs/roadmap)
    *   [Sponsors](https://swc.rs/docs/sponsors)
    *   [Customers](https://swc.rs/docs/customers)
    *   [Benchmarks](https://swc.rs/docs/benchmarks)
    *   API References

        *   [@swc/wasm-typescript](https://swc.rs/docs/references/wasm-typescript)

    *   [Migrating from Babel](https://swc.rs/docs/migrating-from-babel)
    *   [@swc-node vs @swc](https://swc.rs/docs/swc-node-vs-swc)
    *   [Migrating from tsc](https://swc.rs/docs/migrating-from-tsc)

*   Playground

    *   [Try SWC](https://swc.rs/playground)

*   Blog

    *   [Performance Comparison of SWC and Babel](https://swc.rs/blog/perf-swc-vs-babel)
    *   [Introducing SWC 1.0](https://swc.rs/blog/swc-1)

Light

Light

On This Page

*   [Overview](https://swc.rs/#overview)
*   [Download prebuilt binaries](https://swc.rs/#download-prebuilt-binaries)
*   [Transpile JavaScript file and emit to stdout](https://swc.rs/#transpile-javascript-file-and-emit-to-stdout)
*   [Features](https://swc.rs/#features)
*   [Community](https://swc.rs/#community)

[Question? Give us feedback](https://github.com/swc-project/website/issues/new?title=Feedback%20for%20%E2%80%9CRust-based%20platform%20for%20the%20Web%E2%80%9D&labels=feedback)[Edit this page](https://github.com/swc-project/website/tree/main/apps/website/content/index.mdx)Scroll to top

SWC
===

Rust-based platform for the Web

SWC is an extensible Rust-based platform for the next generation of fast developer tools. It’s used by tools like Next.js, Parcel, and Deno, as well as companies like Vercel, ByteDance, Tencent, Shopify, Trip.com, and [more](https://swc.rs/docs/customers).

SWC can be used for both compilation and bundling. For compilation, it takes JavaScript / TypeScript files using modern JavaScript features and outputs valid code that is supported by all major browsers.

🏎

SWC is **20x faster than Babel** on a single thread and **70x faster** on four cores.

[Get Started](https://swc.rs/docs/getting-started) · [Playground](https://swc.rs/playground) · [Blog](https://swc.rs/blog/perf-swc-vs-babel) · [Rustdocs](https://rustdoc.swc.rs/swc/) · [GitHub Repository](https://github.com/swc-project/swc) · [Donate](https://opencollective.com/swc)

Overview[](https://swc.rs/#overview)
------------------------------------

SWC can be downloaded and used as a pre-built binary, or built from source. Currently, the following binaries are provided:

*   Mac (Apple Silicon)
*   Mac (x64)
*   Linux (x86_64)
*   Linux (aarch64)
*   Linux (armv7)
*   Alpine Linux (also install `@swc/core-linux-musl`)
*   Android (aarch64)
*   Windows (win32-x64)
*   Windows (ia32)

#### Download prebuilt binaries[](https://swc.rs/#download-prebuilt-binaries)

pnpm npm yarn

### pnpm

`pnpm add -D @swc/cli @swc/core`

### npm

`npm i -D @swc/cli @swc/core`

### yarn

`yarn add -D @swc/cli @swc/core`

#### Transpile JavaScript file and emit to stdout[](https://swc.rs/#transpile-javascript-file-and-emit-to-stdout)

`npx swc ./file.js`

Features[](https://swc.rs/#features)
------------------------------------

SWC is designed to be extensible. Currently, there is support for:

*   Compilation
*   Minification
*   Transforming with WebAssembly
*   Usage inside webpack and Rspack (`swc-loader`)
*   Improving Jest performance (`@swc/jest`)
*   Custom Plugins

[Learn more](https://swc.rs/docs/getting-started).

Community[](https://swc.rs/#community)
--------------------------------------

![Image 2: stars](https://badgen.net/github/stars/swc-project/swc)

![Image 3: downloads](https://badgen.net/npm/dw/@swc/core?label=downloads%20(@swc/core))

![Image 4: downloads](https://badgen.net/npm/dw/@swc/helpers?label=downloads%20(3rd%20party))

SWC is created by [kdy1](https://github.com/kdy1). Follow [@kdy1dev](https://twitter.com/kdy1dev) on Twitter for future project updates.

Feel free to join the [discussions on GitHub](https://github.com/swc-project/swc/discussions)!

Last updated on April 11, 2025

[Powered by](https://vercel.com/?utm_source=swc)
