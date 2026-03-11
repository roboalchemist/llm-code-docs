# Source: https://www.fastly.com/documentation/guides/compute/developer-guides/custom/

Title: Unofficial SDKs on the Compute platform | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/developer-guides/custom/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Developer guides](https://www.fastly.com/documentation/guides/compute/developer-guides/)

Because the Compute platform is powered by the [WebAssembly System Interface (WASI)](https://github.com/WebAssembly/WASI), you can write Compute programs in any WASI-supporting language. Though Fastly provides and recommends our official language SDKs, we welcome customers who want to bring their own build process.

**WARNING:** Follow the information on this page at your own risk. Because custom SDKs are not supported by Fastly, we cannot make guarantees about the safety and security of these solutions.

[](https://www.fastly.com/documentation/guides/compute/developer-guides/custom/#using-an-unofficial-sdk)Using an unofficial SDK
-------------------------------------------------------------------------------------------------------------------------------

When using a third-party SDK, you should follow the documentation provided by the maintainers. Here are some of the community-maintained SDKs that we know about:

| Language | Repository | Author |
| --- | --- | --- |
| **Zig** | [jedisct1/zigly](https://github.com/jedisct1/zigly) | [Frank Denis](https://twitter.com/jedisct1) |
| **Swift** | [AndrewBarba/swift-compute-runtime](https://github.com/AndrewBarba/swift-compute-runtime) | [Andrew Barba](https://twitter.com/andrew_barba) |
| **Ruby** | [kateinoigakukun/ruby-compute-runtime](https://github.com/kateinoigakukun/ruby-compute-runtime) | [Yuta Saito](https://twitter.com/kateinoigakukun) |
| **.NET** | [harmony7/dotnet-compute](https://github.com/harmony7/dotnet-compute) | [Katsuyuki Omuro](https://twitter.com/katsuyukiomuro) |

In addition the following SDKs have been published by Fastly in the past but are no longer supported:

| Language | SDK module | More info |
| --- | --- | --- |
| **AssemblyScript** | [@fastly/as-compute](https://www.npmjs.com/package/@fastly/as-compute) on npm | See [Using AssemblyScript](https://www.fastly.com/documentation/guides/compute/developer-guides/assemblyscript) |

Fastly does not provide support for, or any assurances about the merits of, any third-party tooling that you may use to build or deploy Compute programs.

[](https://www.fastly.com/documentation/guides/compute/developer-guides/custom/#building-your-own-sdk)Building your own SDK
---------------------------------------------------------------------------------------------------------------------------

To execute your Wasm applications on the Compute platform (and the local testing server), you need to use our Compute hostcalls, which are defined at [https://github.com/fastly/Viceroy/tree/main/wasm_abi/compute-at-edge-abi](https://github.com/fastly/Viceroy/tree/main/wasm_abi/compute-at-edge-abi). These `.witx` files define the functionality of the platform. Use them with your chosen language's WASI tooling to generate stubs or interfaces for your custom SDK to implement.

Once you have created interfaces for the WASI modules required for basic functionality (`fastly_http_req`, `fastly_http_body`) you should be able to create a Compute program that will respond to incoming requests.

When using one of our official SDKs, a program can be compiled with [fastly compute build](https://www.fastly.com/documentation/reference/cli/compute/build/). This will use the appropriate toolchain of your chosen language to produce a Wasm binary and then pack it with Fastly metadata into a package that can be uploaded to the Compute platform. When using your own build process, configure your compiler to produce a Wasm binary and then [fastly compute pack](https://www.fastly.com/documentation/reference/cli/compute/pack/) to package it with the Fastly metadata:

`$ fastly compute pack --wasm-binary bin/main.wasm✓ Initializing...✓ Copying wasm binary...✓ Copying manifest...✓ Creating .tar.gz file...`

The program can now be deployed using the standard [fastly compute deploy](https://www.fastly.com/documentation/reference/cli/compute/deploy/) command or can be tested locally using [fastly compute serve](https://www.fastly.com/documentation/reference/cli/compute/serve/).

[](https://www.fastly.com/documentation/guides/compute/developer-guides/custom/#publishing-your-sdk)Publishing your SDK
-----------------------------------------------------------------------------------------------------------------------

Assuming your dependencies' licenses allow for it, you are welcome to share your custom Compute SDK publicly. Be sure to make it clear that your SDK is not supported by Fastly, because it will be up to you to resolve any issues that your users may have.
