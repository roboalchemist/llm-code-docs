# Source: https://esbuild.github.io/faq/

Title: esbuild - FAQ

URL Source: https://esbuild.github.io/faq/

Published Time: Thu, 12 Mar 2026 19:14:25 GMT

Markdown Content:
esbuild - FAQ
===============

[](javascript:void 0)

[esbuild](https://esbuild.github.io/)
*   [Try in the browser](https://esbuild.github.io/try/)
*   [Getting Started](https://esbuild.github.io/getting-started/)
    *   [Install esbuild](https://esbuild.github.io/getting-started/#install-esbuild)
    *   [Your first bundle](https://esbuild.github.io/getting-started/#your-first-bundle)
    *   [Build scripts](https://esbuild.github.io/getting-started/#build-scripts)
    *   [Bundling for the browser](https://esbuild.github.io/getting-started/#bundling-for-the-browser)
    *   [Bundling for node](https://esbuild.github.io/getting-started/#bundling-for-node)
    *   [Simultaneous platforms](https://esbuild.github.io/getting-started/#simultaneous-platforms)
    *   [Using Yarn Plug'n'Play](https://esbuild.github.io/getting-started/#yarn-pnp)
    *   [Additional npm flags](https://esbuild.github.io/getting-started/#additional-npm-flags)
    *   [Other ways to install](https://esbuild.github.io/getting-started/#other-ways-to-install)

*   [API](https://esbuild.github.io/api/)
    *   [Overview](https://esbuild.github.io/api/#overview)
    *   [General options](https://esbuild.github.io/api/#general-options)
    *   [Input](https://esbuild.github.io/api/#input)
    *   [Output contents](https://esbuild.github.io/api/#output-contents)
    *   [Output location](https://esbuild.github.io/api/#output-location)
    *   [Path resolution](https://esbuild.github.io/api/#path-resolution)
    *   [Transformation](https://esbuild.github.io/api/#transformation)
    *   [Optimization](https://esbuild.github.io/api/#optimization)
    *   [Source maps](https://esbuild.github.io/api/#source-maps)
    *   [Build metadata](https://esbuild.github.io/api/#build-metadata)
    *   [Logging](https://esbuild.github.io/api/#logging)

*   [Content Types](https://esbuild.github.io/content-types/)
    *   [JavaScript](https://esbuild.github.io/content-types/#javascript)
    *   [TypeScript](https://esbuild.github.io/content-types/#typescript)
    *   [JSX](https://esbuild.github.io/content-types/#jsx)
    *   [JSON](https://esbuild.github.io/content-types/#json)
    *   [CSS](https://esbuild.github.io/content-types/#css)
    *   [Text](https://esbuild.github.io/content-types/#text)
    *   [Binary](https://esbuild.github.io/content-types/#binary)
    *   [Base64](https://esbuild.github.io/content-types/#base64)
    *   [Data URL](https://esbuild.github.io/content-types/#data-url)
    *   [External file](https://esbuild.github.io/content-types/#external-file)
    *   [Empty file](https://esbuild.github.io/content-types/#empty-file)

*   [Plugins](https://esbuild.github.io/plugins/)
    *   [Finding plugins](https://esbuild.github.io/plugins/#finding-plugins)
    *   [Using plugins](https://esbuild.github.io/plugins/#using-plugins)
    *   [Concepts](https://esbuild.github.io/plugins/#concepts)
    *   [On-resolve callbacks](https://esbuild.github.io/plugins/#on-resolve)
    *   [On-load callbacks](https://esbuild.github.io/plugins/#on-load)
    *   [On-start callbacks](https://esbuild.github.io/plugins/#on-start)
    *   [On-end callbacks](https://esbuild.github.io/plugins/#on-end)
    *   [On-dispose callbacks](https://esbuild.github.io/plugins/#on-dispose)
    *   [Accessing build options](https://esbuild.github.io/plugins/#build-options)
    *   [Resolving paths](https://esbuild.github.io/plugins/#resolve)
    *   [Example plugins](https://esbuild.github.io/plugins/#example-plugins)
    *   [Plugin API limitations](https://esbuild.github.io/plugins/#plugin-api-limitations)

*   [FAQ](https://esbuild.github.io/faq/)
    *   [Why is esbuild fast?](https://esbuild.github.io/faq/#why-is-esbuild-fast)
    *   [Benchmark details](https://esbuild.github.io/faq/#benchmark-details)
    *   [Upcoming roadmap](https://esbuild.github.io/faq/#upcoming-roadmap)
    *   [Production readiness](https://esbuild.github.io/faq/#production-readiness)
    *   [Anti-virus software](https://esbuild.github.io/faq/#anti-virus-software)
    *   [Outdated version of Go](https://esbuild.github.io/faq/#old-go-version)
    *   [Minified newlines](https://esbuild.github.io/faq/#minified-newlines)
    *   [Avoiding name collisions](https://esbuild.github.io/faq/#top-level-name-collisions)
    *   [Strict mode](https://esbuild.github.io/faq/#strict-mode)
    *   [Top-level `var`](https://esbuild.github.io/faq/#top-level-var)

*   [Bundle Size Analyzer](https://esbuild.github.io/analyze/)

[](https://github.com/evanw/esbuild)[](javascript:void 0)

FAQ
===

This is a collection of common questions about esbuild. You can also ask questions on the [GitHub issue tracker](https://github.com/evanw/esbuild/issues).

*   [Why is esbuild fast?](https://esbuild.github.io/faq/#why-is-esbuild-fast)
*   [Benchmark details](https://esbuild.github.io/faq/#benchmark-details)
*   [Upcoming roadmap](https://esbuild.github.io/faq/#upcoming-roadmap)
*   [Production readiness](https://esbuild.github.io/faq/#production-readiness)
*   [Anti-virus software](https://esbuild.github.io/faq/#anti-virus-software)
*   [Outdated version of Go](https://esbuild.github.io/faq/#old-go-version)
*   [Minified newlines](https://esbuild.github.io/faq/#minified-newlines)
*   [Avoiding name collisions](https://esbuild.github.io/faq/#top-level-name-collisions)
*   [Strict mode](https://esbuild.github.io/faq/#strict-mode)
*   [Top-level `var`](https://esbuild.github.io/faq/#top-level-var)

[#](https://esbuild.github.io/faq/#why-is-esbuild-fast)Why is esbuild fast?
---------------------------------------------------------------------------

Several reasons:

*   It's written in [Go](https://go.dev/) and compiles to native code.

Most other bundlers are written in JavaScript, but a command-line application is a worst-case performance situation for a JIT-compiled language. Every time you run your bundler, the JavaScript VM is seeing your bundler's code for the first time without any optimization hints. While esbuild is busy parsing your JavaScript, node is busy parsing your bundler's JavaScript. By the time node has finished parsing your bundler's code, esbuild might have already exited and your bundler hasn't even started bundling yet.

In addition, Go is designed from the core for parallelism while JavaScript is not. Go has shared memory between threads while JavaScript has to serialize data between threads. Both Go and JavaScript have parallel garbage collectors, but Go's heap is shared between all threads while JavaScript has a separate heap per JavaScript thread. This seems to cut the amount of parallelism that's possible with JavaScript worker threads in half [according to my testing](https://github.com/evanw/esbuild/issues/111#issuecomment-719910381), presumably since half of your CPU cores are busy collecting garbage for the other half.

*   Parallelism is used heavily.

The algorithms inside esbuild are carefully designed to fully saturate all available CPU cores when possible. There are roughly three phases: parsing, linking, and code generation. Parsing and code generation are most of the work and are fully parallelizable (linking is an inherently serial task for the most part). Since all threads share memory, work can easily be shared when bundling different entry points that import the same JavaScript libraries. Most modern computers have many cores so parallelism is a big win.

*   Everything in esbuild is written from scratch.

There are a lot of performance benefits with writing everything yourself instead of using 3rd-party libraries. You can have performance in mind from the beginning, you can make sure everything uses consistent data structures to avoid expensive conversions, and you can make wide architectural changes whenever necessary. The drawback is of course that it's a lot of work.

For example, many bundlers use the official TypeScript compiler as a parser. But it was built to serve the goals of the TypeScript compiler team and they do not have performance as a top priority. Their code makes pretty heavy use of [megamorphic object shapes](https://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html) and unnecessary [dynamic property accesses](https://github.com/microsoft/TypeScript/issues/39247) (both well-known JavaScript speed bumps). And the TypeScript parser appears to still run the type checker even when type checking is disabled. None of these are an issue with esbuild's custom TypeScript parser.

*   Memory is used efficiently.

Compilers are ideally mostly O(n) complexity in the length of the input. So if you are processing a lot of data, memory access speed is likely going to heavily affect performance. The fewer passes you have to make over your data (and also the fewer different representations you need to transform your data into), the faster your compiler will go.

For example, esbuild only touches the whole JavaScript AST three times:

    1.   A pass for lexing, parsing, scope setup, and declaring symbols
    2.   A pass for binding symbols, minifying syntax, JSX/TS to JS, and ESNext-to-ES2015
    3.   A pass for minifying identifiers, minifying whitespace, generating code, and generating source maps

This maximizes reuse of AST data while it's still hot in the CPU cache. Other bundlers do these steps in separate passes instead of interleaving them. They may also convert between data representations to glue multiple libraries together (e.g. string→TS→JS→string, then string→JS→older JS→string, then string→JS→minified JS→string) which uses more memory and slows things down.

Another benefit of Go is that it can store things compactly in memory, which enables it to use less memory and fit more in the CPU cache. All object fields have types and fields are packed tightly together so e.g. several boolean flags only take one byte each. Go also has value semantics and can embed one object directly in another so it comes "for free" without another allocation. JavaScript doesn't have these features and also has other drawbacks such as JIT overhead (e.g. hidden class slots) and inefficient representations (e.g. non-integer numbers are heap-allocated with pointers).

Each one of these factors is only a somewhat significant speedup, but together they can result in a bundler that is multiple orders of magnitude faster than other bundlers commonly in use today.

[#](https://esbuild.github.io/faq/#benchmark-details)Benchmark details
----------------------------------------------------------------------

Here are the details about each benchmark:

JavaScript benchmark

[esbuild](https://esbuild.github.io/)

0.39s

[parcel 2](https://parceljs.org/)

14.91s

[rollup 4](https://rollupjs.org/) + [terser](https://terser.org/)

34.10s

[webpack 5](https://webpack.js.org/)

41.21s

0s

10s

20s

30s

40s

This benchmark approximates a large JavaScript codebase by duplicating the [three.js](https://github.com/mrdoob/three.js) library 10 times and building a single bundle from scratch, without any caches. The benchmark can be run with `make bench-three` in the [esbuild repo](https://github.com/evanw/esbuild).

| Bundler | Time | Relative slowdown | Absolute speed | Output size |
| --- | --- | --- | --- | --- |
| esbuild | 0.39s | 1x | 1403.7 kloc/s | 5.80mb |
| parcel 2 | 14.91s | 38x | 36.7 kloc/s | 5.78mb |
| rollup 4 + terser | 34.10s | 87x | 16.1 kloc/s | 5.82mb |
| webpack 5 | 41.21s | 106x | 13.3 kloc/s | 5.84mb |

Each time reported is the best of three runs. I'm running esbuild with `--bundle --minify --sourcemap`. I used the [`@rollup/plugin-terser`](https://github.com/rollup/plugins/tree/master/packages/terser) plugin because Rollup itself doesn't support minification. Webpack 5 uses `--mode=production --devtool=sourcemap`. Parcel 2 uses the default options. Absolute speed is based on the total line count including comments and blank lines, which is currently 547,441. The tests were done on a 6-core 2019 MacBook Pro with 16gb of RAM and with [macOS Spotlight](https://en.wikipedia.org/wiki/Spotlight_(software)) disabled.

TypeScript benchmark

[esbuild](https://esbuild.github.io/)

0.10s

[parcel 2](https://parceljs.org/)

6.91s

[webpack 5](https://webpack.js.org/)

16.69s

0s

5s

10s

15s

This benchmark uses the old [Rome](https://github.com/rome/tools) code base (prior to their Rust rewrite) to approximate a large TypeScript codebase. All code must be combined into a single minified bundle with source maps and the resulting bundle must work correctly. The benchmark can be run with `make bench-rome` in the [esbuild repo](https://github.com/evanw/esbuild).

| Bundler | Time | Relative slowdown | Absolute speed | Output size |
| --- | --- | --- | --- | --- |
| esbuild | 0.10s | 1x | 1318.4 kloc/s | 0.97mb |
| parcel 2 | 6.91ѕ | 69x | 16.1 kloc/s | 0.96mb |
| webpack 5 | 16.69ѕ | 167x | 8.3 kloc/s | 1.27mb |

Each time reported is the best of three runs. I'm running esbuild with `--bundle --minify --sourcemap --platform=node`. Webpack 5 uses [`ts-loader`](https://github.com/TypeStrong/ts-loader) with `transpileOnly: true` and `--mode=production --devtool=sourcemap`. Parcel 2 uses `"engines": "node"` in `package.json`. Absolute speed is based on the total line count including comments and blank lines, which is currently 131,836. The tests were done on a 6-core 2019 MacBook Pro with 16gb of RAM and with [macOS Spotlight](https://en.wikipedia.org/wiki/Spotlight_(software)) disabled.

The results don't include Rollup because I couldn't get it to work for reasons relating to TypeScript compilation. I tried [`@rollup/plugin-typescript`](https://github.com/rollup/plugins/tree/master/packages/typescript) but you can't disable type checking, and I tried [`@rollup/plugin-sucrase`](https://github.com/rollup/plugins/tree/master/packages/sucrase) but there's no way to provide a `tsconfig.json` file (which is required for correct path resolution).

[#](https://esbuild.github.io/faq/#upcoming-roadmap)Upcoming roadmap
--------------------------------------------------------------------

These features are already in progress and are first priority:

*   Code splitting ([#16](https://github.com/evanw/esbuild/issues/16), [docs](https://esbuild.github.io/api/#splitting))

These are potential future features but may not happen or may happen to a more limited extent:

*   HTML content type ([#31](https://github.com/evanw/esbuild/issues/31))

After that point, I will consider esbuild to be relatively complete. I'm planning for esbuild to reach a mostly stable state and then stop accumulating more features. This will involve saying "no" to requests for adding major features to esbuild itself. I don't think esbuild should become an all-in-one solution for all frontend needs. In particular, I want to avoid the pain and problems of the "webpack config" model where the underlying tool is too flexible and usability suffers.

For example, I am _not_ planning to include these features in esbuild's core itself:

*   Support for other frontend languages (e.g. [Elm](https://elm-lang.org/), [Svelte](https://svelte.dev/), [Vue](https://vuejs.org/), [Angular](https://angular.io/))
*   TypeScript type checking (just run `tsc` separately)
*   An API for custom AST manipulation
*   Hot-module reloading
*   Module federation

I hope that the extensibility points I'm adding to esbuild ([plugins](https://esbuild.github.io/plugins/) and the [API](https://esbuild.github.io/api/)) will make esbuild useful to include as part of more customized build workflows, but I'm not intending or expecting these extensibility points to cover all use cases. If you have very custom requirements then you should be using other tools. I also hope esbuild inspires other build tools to dramatically improve performance by overhauling their implementations so that everyone can benefit, not just those that use esbuild.

I am planning to continue to maintain everything in esbuild's existing scope even after esbuild reaches stability. This means implementing support for newly-released JavaScript and TypeScript syntax features, for example.

[#](https://esbuild.github.io/faq/#production-readiness)Production readiness
----------------------------------------------------------------------------

This project has not yet hit version 1.0.0 and is still in active development. That said, it is far beyond the alpha stage and is pretty stable. I think of it as a late-stage beta. For some early-adopters that means it's good enough to use for real things. Some other people think this means esbuild isn't ready yet. This section doesn't try to convince you either way. It just tries to give you enough information so you can decide for yourself whether you want to use esbuild as your bundler.

Some data points:

*   **Used by other projects**
The API is already being used as a library within many other developer tools. For example, [Vite](https://vitejs.dev/) is using esbuild to transform TypeScript into JavaScript and [Amazon CDK](https://aws.amazon.com/cdk/) (Cloud Development Kit) and [Phoenix](https://www.phoenixframework.org/) are using esbuild to bundle code.

*   **API stability**
Even though esbuild's version is not yet 1.0.0, effort is still made to keep the API stable. Patch versions are intended for backwards-compatible changes and minor versions are intended for backwards-incompatible changes. If you plan to use esbuild for something real, you should either pin the exact version (maximum safety) or pin the major and minor versions (only accept backwards-compatible upgrades).

*   **Only one main developer**
This tool is primarily built by [me](https://github.com/evanw). For some people this is fine, but for others this means esbuild is not a suitable tool for their organization. That's ok with me. I'm building esbuild because I find it fun to build and because it's the tool I'd want to use. I'm sharing it with the world because there are others that want to use it too, because the feedback makes the tool itself better, and because I think it will inspire the ecosystem to make better tools.

*   **Not always open to scope expansion**
I'm not planning on including major features that I'm not interested in building and/or maintaining. I also want to limit the project's scope so it doesn't get too complex and unwieldy, both from an architectural perspective, a testing and correctness perspective, and from a usability perspective. Think of esbuild as a "linker" for the web. It knows how to transform and bundle JavaScript and CSS. But the details of how your source code ends up as plain JavaScript or CSS may need to be 3rd-party code.

I'm hoping that [plugins](https://esbuild.github.io/plugins/) will allow the community to add major features (e.g. WebAssembly import) without needing to contribute to esbuild itself. However, not everything is exposed in the plugin API and it may be the case that it's not possible to add a particular feature to esbuild that you may want to add. This is intentional; esbuild is not meant to be an all-in-one solution for all frontend needs.

[#](https://esbuild.github.io/faq/#anti-virus-software)Anti-virus software
--------------------------------------------------------------------------

Since esbuild is written in native code, anti-virus software can sometimes incorrectly flag it as a virus. _This does not mean esbuild is a virus._ I do not publish malicious code and I take supply chain security very seriously.

Virtually all of esbuild's code is first-party code except for [one dependency](https://github.com/evanw/esbuild/blob/main/go.mod) on Google's set of supplemental Go packages. My development work is done on different machine that is isolated from the one I use to publish builds. I have done additional work to ensure that esbuild's published builds are completely reproducible and after every release, published builds are [automatically compared](https://github.com/evanw/esbuild/blob/main/.github/workflows/validate.yml) to ones locally-built in an unrelated environment to ensure that they are bitwise identical (i.e. that the Go compiler itself has not been compromised). You can also build esbuild from source yourself and compare your build artifacts to the published ones to independently verify this.

Having to deal with false-positives is an unfortunate reality of using anti-virus software. Here are some possible workarounds if your anti-virus won't let you use esbuild:

*   Ignore your anti-virus software and remove esbuild from quarantine
*   Report the specific esbuild native executable as a false-positive to your anti-virus software vendor
*   Use [`esbuild-wasm`](https://esbuild.github.io/getting-started/#wasm) instead of `esbuild` to bypass your anti-virus software (which likely won't flag WebAssembly files the same way it flags native executables)
*   Use another build tool instead of esbuild

[#](https://esbuild.github.io/faq/#old-go-version)Outdated version of Go
------------------------------------------------------------------------

If you use an automated dependency vulnerability scanner, you may get a report that the version of the Go compiler that esbuild uses and/or the version of `golang.org/x/sys` (esbuild's only dependency) is outdated. These reports are benign and should be ignored.

This happens because esbuild's code is deliberately intended to be compilable with Go 1.13. Later versions of Go have dropped support for certain older platforms that I want esbuild to be able to run on (e.g. older versions of macOS). While esbuild's published binaries are compiled with a much newer version of the Go compiler (and therefore don't work on older versions of macOS), you are currently still able to compile the latest version of esbuild for yourself with Go 1.13 and use it on older versions of macOS because esbuild's code can still be compiled with Go as far back as 1.13.

People and/or automated tools sometimes see the `go 1.13` line in [`go.mod`](https://github.com/evanw/esbuild/blob/main/go.mod) and complain that esbuild's published binaries are built with Go 1.13, which is a really old version of Go. However, that's not true. That line in `go.mod` only specifies the minimum compiler version. It has nothing to do with the version of Go that esbuild's published binaries are built with, which is a much newer version of Go. [Please read the documentation.](https://go.dev/ref/mod#go-mod-file-go)

People also sometimes want esbuild to update the `golang.org/x/sys` dependency because there is a known vulnerability in the version that esbuild uses (specifically [GO-2022-0493](https://pkg.go.dev/vuln/GO-2022-0493) about the `Faccessat` function). The problem that prevents esbuild from updating to a newer version of the `golang.org/x/sys` dependency is that newer versions have started using the `unsafe.Slice` function, which was first introduced in Go 1.17 (and therefore doesn't compile in older versions of Go). However, this vulnerability report is irrelevant because a) esbuild doesn't ever call that function in the first place and b) esbuild is a build tool, not a sandbox, and esbuild's file system access is not security-sensitive.

I'm not going to drop compatibility with older platforms and prevent some people from being able to use esbuild just to work around irrelevant vulnerability reports. Please ignore any reports about the issues described above.

[#](https://esbuild.github.io/faq/#minified-newlines)Minified newlines
----------------------------------------------------------------------

People are sometimes surprised that esbuild's minifier typically changes the character escape sequence `\n` within JavaScript strings into a newline character in a template literal. But this is intentional. **This is not a bug with esbuild**. The job of a minifier is to generate as compact an output as possible that's equivalent to the input. The character escape sequence `\n` is two bytes long while a newline character is one byte long.

For example, this code is 21 bytes long:

var text="a\nb\nc\n";
While this code is 18 bytes long:

var text=`a b c `;
So the second code is fully minified while the first one isn't. Minifying code does not mean putting it all on one line. Instead, minifying code means generating equivalent code that uses as few bytes as possible. In JavaScript, an untagged template literal is equivalent to a string literal, so esbuild is doing the correct thing here.

[#](https://esbuild.github.io/faq/#top-level-name-collisions)Avoiding name collisions
-------------------------------------------------------------------------------------

Top-level variables in an entry point module should never end up in the global scope when running esbuild's output in a browser. If that happens, it means you did not follow [esbuild's documentation about output formats](https://esbuild.github.io/api/#format) and are using esbuild incorrectly. **This is not a bug with esbuild.**

Specifically, you must do either one of the following when running esbuild's output in a browser:

1.   `--format=iife` with `<script src="...">`
If you are running your code in the global scope, then you should be using `--format=iife`. This causes esbuild's output to wrap your code so that top-level variables are declared in a nested scope.

2.   `--format=esm` with `<script src="..." type="module">`
If you are using `--format=esm`, then you must run your code as a module. This causes the browser to wrap your code so that top-level variables are declared in a nested scope.

Using `--format=esm` with `<script src="...">` will break your code in subtle and confusing ways (omitting `type="module"` means that all top-level variables will end up in the global scope, which will then collide with top-level variables that have the same name in other JavaScript files).

[#](https://esbuild.github.io/faq/#strict-mode)Strict mode
----------------------------------------------------------

JavaScript contains a feature called [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) which alters how JavaScript code runs. If a JavaScript file and/or function starts with a `"use strict";` statement, the code in that scope and all nested scopes runs in strict mode:

function usesStrictMode() {
 "use strict";
  return this;
}

function doesNotUseStrictMode() {
  return this;
}

console.log(
  usesStrictMode(),
  doesNotUseStrictMode(),
)
The strict mode feature is complicated and error-prone for many reasons:

*   It does not compose well because there is no way to turn it off for a nested scope. For example, it's unclear what the above code will print. The first function will definitely return `undefined` because `this` is always defaults to `undefined` when calling a strict mode function. But the second function may either return `undefined` or the global object depending on whether or not the scope surrounding this code snippet is in strict mode.

*   Strict mode can be affected by your choice of JavaScript module format. CommonJS modules (files that reference `module` and/or `exports`) are only in strict mode if they start with a `"use strict";` directive. However, ECMAScript modules (files that use the `import` and `export` keywords) are always in strict mode regardless of whether or not the `"use strict";` directive is present.

*   The TypeScript compiler automatically inserts a `"use strict";` directive for you if you enable the [`strict`](https://www.typescriptlang.org/tsconfig/#strict) or [`alwaysStrict`](https://www.typescriptlang.org/tsconfig/#alwaysStrict) options in your `tsconfig.json` file. This isn't necessarily obvious because the `strict` option is typically associated with type checking, not changing run-time behavior. Because esbuild emulates these TypeScript settings, esbuild will also insert `"use strict";` in these cases.

*   When esbuild bundles multiple modules into a single file, some of the modules that shouldn't be run in strict mode may end up being run in strict mode anyway. This can happen when the output format is an ECMAScript module (implicit strict mode) or when the entry point is in strict mode (either with an explicit directive or implicit strict mode from `tsconfig.json`). This is because bundling places the dependencies in nested scopes and because JavaScript doesn't have a way to turn strict mode back off in a nested scope.

There isn't really a general solution to these problems because of how the strict mode feature was designed. Hopefully this information can help you diagnose and work around any compatibility problems that come up.

[#](https://esbuild.github.io/faq/#top-level-var)Top-level `var`
----------------------------------------------------------------

People are sometimes surprised that esbuild sometimes rewrites top-level `let`, `const`, and `class` declarations as `var` declarations instead. This is done for a few reasons:

*   **For correctness**
Bundling sometimes needs to lazily-initialize a module. For example, this happens when you call `require()` or `import()` using the path of a module within the bundle. Doing this involves separating the declaration and initialization of top-level symbols by moving the initialization into a closure. So for example `class` statements are rewritten as an assignment of a class expression to a variable. Keeping the declarations out of the lazy-initialization closure is important for performance, since it means other modules can reference them directly instead by name instead of indirectly via a slower property access.

Another case where this is needed is when transforming top-level `using` declarations. This involves wrapping the entire module body in a `try` block, which also involves separating the declaration and initialization of top-level symbols. Top-level symbols may need to be exported, which means they cannot be declared within the `try` block.

In both of these cases esbuild will fail with a build error if the source code contains a mutation of a `const` symbol, so it's not possible for esbuild's rewriting of top-level `const` into `var` to result in the mutation of a constant.

Due to esbuild's current architecture, the part of esbuild that does this transformation (the parser) cannot know whether the current module will end up being lazily initialized or not. The information for this decision may only be discovered later on in the build, or may even change in future incremental builds that reuse the same AST (per-file ASTs are transformed once during parsing and then cached and reused across incremental builds). So this transformation is always done when bundling is active.

*   **For performance**
Multiple JavaScript VMs have had and continue to have performance issues with TDZ (i.e. "temporal dead zone") checks. These checks validate that a let, or const, or class symbol isn't used before it's initialized. Here are two issues with well-known VMs:

    *    V8: [https://bugs.chromium.org/p/v8/issues/detail?id=13723](https://bugs.chromium.org/p/v8/issues/detail?id=13723) (10% slowdown) 
    *    JavaScriptCore: [https://bugs.webkit.org/show_bug.cgi?id=199866](https://bugs.webkit.org/show_bug.cgi?id=199866) (1,000% slowdown!) 

JavaScriptCore had a severe performance issue as their TDZ implementation had time complexity that was quadratic in the number of variables needing TDZ checks in the same scope (with the top-level scope typically being the worst offender). V8 has ongoing issues with TDZ checks being present throughout the code their JIT generates even when they have already been checked earlier in the same function or when the function in question has already been run (so the checks have already happened).

In JavaScript, `let`, `const`, and `class` declarations all introduce TDZ checks while `var` declarations do not. Since bundling typically merges many modules into a single very large top-level scope, the performance impact of these TDZ checks can be pretty severe. Converting top-level `let`, `const`, and `class` declarations into `var` helps automatically make your code faster.

Note that esbuild doesn't preserve top-level TDZ side effects because modules may need to be lazily initialized (as described above), which means separating declaration from initialization. TDZ checks for top-level symbols could hypothetically still be supported by generating extra code that checks before each use of a top-level symbol and throws if it hasn't been initialized yet (effectively manually implementing what a real JavaScript VM would do). However, this seems like an excessive overhead for both code size and run time, and does not seem like something that a production-oriented bundler should do.
