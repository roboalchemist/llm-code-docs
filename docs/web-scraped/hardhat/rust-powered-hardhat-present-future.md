# Source: https://blog.nomic.foundation/rust-powered-hardhat-present-future/

Title: Rust-powered Hardhat: Present & Future

URL Source: https://blog.nomic.foundation/rust-powered-hardhat-present-future/

Published Time: 2024-08-19T15:51:33.000Z

Markdown Content:
In March, we released [Hardhat v2.21.0](https://github.com/NomicFoundation/hardhat/releases?q=v2.21.0&expanded=true&ref=blog.nomic.foundation), the first version powered by our brand new **E**thereum **D**evelopment **R**untime (EDR, for short) implemented in Rust. This was a significant change under the hood, representing the rewriting of Hardhat's largest and most complex component—its Ethereum simulation layer—in a new language. By design, this update didn’t affect the user experience beyond improving performance. In this post, we’ll explain why we built EDR, discuss its current status, and outline what’s coming next for the project.

Current Hardhat impact
----------------------

Migrating Hardhat to EDR was a significant undertaking, making stabilization our top priority post-release. We fixed every major bug and ensured that all community plugins continued to work as before. In terms of performance, our main goal was to avoid regressions, while also experimenting with some simple optimizations.

Most projects using the EDR release of Hardhat (or newer) saw at least a 2x increase in test running speed, with some experiencing up to a 10x improvement.

The EDR release also allowed us to overcome significant third-party architectural obstacles that had been preventing Hardhat from implementing tests in Solidity. More on this shortly.

Why build EDR?
--------------

EDR is a Rust-based tooling runtime implementation. The goal is to make it reusable by third-parties to accelerate the development of developer tools. It's part of the [Nomic Foundation long-term roadmap](https://blog.nomic.foundation/slang-rethnet-2ad465fd7880/) to improve Ethereum's developer experience by making tools easier to build. Our first step towards this vision was rewriting Hardhat Network and some of its dependencies in Rust, laying the foundations for EDR and allowing us to battle-test it through Hardhat's existing user base.

Hardhat Network, the runtime component of Hardhat, had observability capabilities that enable features like Solidity stack traces, `console.log` statements, and detailed information about reverted transactions. However, it was tightly coupled to Hardhat and Node.js. Migrating it to Rust allows those features to be available as a native library in any language, and in the browser through WASM. This decoupling means any improvements to runtime observability in Hardhat will benefit all future tools built on EDR. Additionally, migrating some dependencies and using [revm](https://github.com/bluealloy/revm?ref=blog.nomic.foundation) gave us more control over the stack, enabling us architecturally to start the development of Solidity tests and multi-chain support.

EDR is one side of this strategy, aiming to be a flexible, extensible, fast, and language-agnostic EVM local development runtime. The other half is our [Slang compiler](https://github.com/nomicfoundation/slang?ref=blog.nomic.foundation), which is also [making great progress](https://blog.nomic.foundation/how-to-write-your-own-solidity-linter-using-slang-356e7565ad1b/).

Coming next: Hardhat 3
----------------------

After stabilizing EDR, we shifted focus to enabling some key runtime features for our next major release: Hardhat 3. This version will involve a broad redesign and rewrite of the tool to address current and future ecosystem needs. Below are the the two key features we’re now working on.

### **OP Stack simulation support**

Developing on L2 networks like Optimism typically requires forking the network or developing locally in an "Ethereum mode" and hoping for the best in terms of your local code execution matching what will happen in production. We aim to improve this by enabling precise local simulations with behaviors specific to networks other than the Ethereum mainnet. Our initial focus will be on supporting [OP Stack](https://docs.optimism.io/stack/getting-started?ref=blog.nomic.foundation) networks, but we plan to add other types of chains in the future. Running local simulations in this mode will include features like L1 data fees or predeploys, resulting in a more precise and reliable development environment.

### Solidity tests

Solidity tests have been on the Hardhat roadmap for a long time, but limitations in our dependencies had been preventing us from implementing this feature. With EDR now in place, we can finally work towards offering Solidity tests. This will make a substantial part of the development process more streamlined and performant, while maintaining support for TypeScript-based tests for the more complex, integration-like testing scenarios that require a more expressive general-purpose language.

Looking ahead
-------------

EDR as Hardhat’s new runtime represents a fresh canvas to work on, with a much higher ceiling, and we have exciting plans lined up for after the release of Hardhat 3.

### Enhanced Portability with WASM

The current version is built on top of [N-API](https://nodejs.org/api/n-api.html?ref=blog.nomic.foundation) to enable usage from Node.js, but this approach has a big limitation: it prevents the use of EDR in the browser. To address this, we plan to transition to WebAssembly (WASM), which will provide the necessary portability without sacrificing performance. This will enable the community to build some cool browser-based tooling once done.

### Productizing the API

The EDR API is currently in beta for internal use within Hardhat. After Hardhat 3 is out we’ll work on improving it and stabilizing it to make it usable for external projects.

### Improved Solidity Debugging Experience

We’re on track to double down on enhancing the debugging experience further. Starting with improving stack traces and error messages, to then integrating Slang into EDR to allow for more precise step-by-step inspection of Solidity and EVM execution.

### Correct simulation of more L2 networks

While we’re starting with OP Stack, we’re hoping to add support for Arbitrum and zkSync, as well as providing a generalized path for other L2s to build plugins that add support on EDR.

Stay tuned
----------

We have a lot coming in the next year, and as usual, we’d love your feedback. Have you tried the Rust-powered version of Hardhat? Download the current version and [let us know if you run into any issues!](https://github.com/nomicfoundation/hardhat?ref=blog.nomic.foundation)

Follow [@HardhatHQ](https://twitter.com/HardhatHQ?ref=blog.nomic.foundation) and [@NomicFoundation](https://twitter.com/NomicFoundation?ref=blog.nomic.foundation) on X
