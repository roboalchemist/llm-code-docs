# Source: https://hardhat.org

Title: Hardhat 3

URL Source: https://hardhat.org/

Published Time: Thu, 12 Mar 2026 10:58:25 GMT

Markdown Content:
Hardhat 3
===============
[< < < < < Please complete the 2026 Solidity Survey! > > > > >](https://solidity.survey-research.net/solidity-survey)[![Image 1: Hardhat](https://hardhat.org/images/hardhat-logo.svg)![Image 2: Hardhat](https://hardhat.org/images/hardhat-logo-dark.svg)](https://hardhat.org/)
*   [documentation](https://hardhat.org/docs/getting-started)
    *   [Hardhat 3](https://hardhat.org/docs/getting-started)
    *   [Hardhat Ignition](https://hardhat.org/ignition/docs/getting-started)
    *   [Hardhat VSCode](https://hardhat.org/hardhat-vscode)

*   [plugins](https://hardhat.org/plugins)
*   [hardhat 2](https://hardhat.org/hardhat2)

[](https://github.com/NomicFoundation/hardhat)[](https://twitter.com/HardhatHQ)[](https://hardhat.org/discord)

![Image 3: theme-switcher](https://hardhat.org/images/theme-switcher.svg)![Image 4: theme-switcher](https://hardhat.org/images/theme-switcher-dark.svg)

**Hardhat 3:** Rust-powered Solidity tests
Ethereum development environment for professionals
==================================================

[Get started](https://hardhat.org/docs/getting-started)

Ready to use out of the box
---------------------------

Hardhat includes everything you need for Solidity smart contract development. Testing, deployment, code coverage, code verification, and more.

![Image 5](https://hardhat.org/_astro/hero.2vvt1DZz.webp)

![Image 6](https://hardhat.org/_astro/heroDark.BhpR2ioz.webp)

Why hardhat?
------------

### Run Solidity tests on a Rust-powered runtime

Deploy your contracts, run Solidity tests, and debug your code on Hardhat's new runtime written in Rust for outstanding performance.

[Learn more about writing Solidity tests](https://hardhat.org/docs/guides/testing/using-solidity)

### Clear errors and Solidity stack traces

When transactions revert, Hardhat shows actionable errors like "Non-payable function was called with value 1," alongside detailed Solidity stack traces to pinpoint exactly where and why your code fails.

[Learn more about debugging](https://hardhat.org/docs/reference/edr-simulated-networks#developer-focused-features)

![Image 7: Feature card picture](https://hardhat.org/images/feature-cards/SolidityDebuggerImageSm.svg)

![Image 8: Feature card picture](https://hardhat.org/images/feature-cards/SolidityDebuggerImageDarkSm.svg)

### Comprehensive testing approach

Write unit tests in Solidity for speed and conciseness, integration tests in TypeScript for expressiveness and complexity, or fuzzing tests to push the edges. Decide on a case by case basis.

[Learn more about testing](https://hardhat.org/docs/guides/testing)

### Multi-chain ready: Optimism's OP Stack and Base simulation support

Manage multiple networks at the same time and confidently deploy on OP Stack knowing your code was tested on an accurate simulation.

[Learn more about multichain support](https://hardhat.org/docs/explanations/multichain-support)

![Image 9: Feature card picture](https://hardhat.org/images/feature-cards/ComprehensiveTestingImageSm.svg)

![Image 10: Feature card picture](https://hardhat.org/images/feature-cards/ComprehensiveTestingImageDarkSm.svg)

### Simple and reliable deployments

Define your contract instances, their operations, and Hardhat Ignition will drive the complex details and parallelize execution.

[Get started with Hardhat Ignition](https://hardhat.org/docs/guides/deployment/using-ignition)

### Plugin ecosystem

Extend Hardhat with a composable ecosystem of plugins that add functionality and integrate your existing tools into a smooth workflow.

[Explore the plugin ecosystem](https://hardhat.org/docs/plugins/official-plugins)

![Image 11: Feature card picture](https://hardhat.org/images/feature-cards/SimpleDeploymentsImageSm.svg)

![Image 12: Feature card picture](https://hardhat.org/images/feature-cards/SimpleDeploymentsImageDarkSm.svg)

### TypeScript extensibility

A tooling platform designed to be extended, Hardhat has all the utilities you need to address your project-specific needs. Change anything you like. Even entire built-in tasks, or just parts of them.

[Learn more about extending Hardhat](https://hardhat.org/docs/guides/writing-tasks)

### For teams and projects of any scale

From single hacker quickly iterating on a proof of concept to full blown engineering organization dealing with ad-hoc needs at scale, Hardhat adapts as your needs change

[Get started with Hardhat plugins](https://hardhat.org/docs/plugin-development)

![Image 13: Feature card picture](https://hardhat.org/images/feature-cards/PluginEcosystemImageSm.png)

![Image 14: Feature card picture](https://hardhat.org/images/feature-cards/PluginEcosystemImageDarkSm.png)

![Image 15: Feature card picture](https://hardhat.org/images/feature-cards/SolidityDebuggerImageMd.svg)

![Image 16: Feature card picture](https://hardhat.org/images/feature-cards/SolidityDebuggerImageDarkMd.svg)

![Image 17: Feature card picture](https://hardhat.org/images/feature-cards/ComprehensiveTestingImageMd.svg)

![Image 18: Feature card picture](https://hardhat.org/images/feature-cards/ComprehensiveTestingImageDarkMd.svg)

![Image 19: Feature card picture](https://hardhat.org/images/feature-cards/SimpleDeploymentsImageMd.svg)

![Image 20: Feature card picture](https://hardhat.org/images/feature-cards/SimpleDeploymentsImageDarkMd.svg)

![Image 21: Feature card picture](https://hardhat.org/images/feature-cards/PluginEcosystemImageMd.png)

![Image 22: Feature card picture](https://hardhat.org/images/feature-cards/PluginEcosystemImageDarkMd.png)

Flexible. Extensible. Fast.

Build your software your way—without limitations.

What's new in Hardhat
---------------------

![Image 23: Hardhat v3.1.12](https://hardhat.org/_astro/Hardhat-news.DA4JGr4h.svg)

 Today 

### Hardhat v3.1.12

This release adds support for function gas snapshots and snapshot cheatcodes in Solidity tests through the new `--snapshot` and `--snapshot-check` flags, along with minor improvements for plugins and an update to EDR.

[Learn more](https://github.com/NomicFoundation/hardhat/releases/tag/hardhat%403.1.12)

 6 days ago 

### Hardhat v3.1.11

This release improves the DX of the Viem and Ethers plugins with better autocomplete, improves the errors printed when a contract can't be compiled with the configured compilers, upgrades EDR, and many minor improvements and fixes. EDR RELATED BREAKING CHANGE: Memory capture used to be enabled by default on geth, but has since been flipped (see ethereum/go-ethereum#23558) and is now disabled by default. We have followed suit and disabled it by default as well. If you were relying on memory capture, you will need to explicitly enable it by setting the enableMemory option to true in your tracer configuration.

[Learn more](https://github.com/NomicFoundation/hardhat/releases/tag/hardhat%403.1.11)

 2 weeks ago 

### Hardhat v3.1.10

This release contains many improvements and bug fixes, including a cleaner display of test coverage reports (`--coverage`) and support for inline actions in tasks.

[Learn more](https://github.com/NomicFoundation/hardhat/releases/tag/hardhat%403.1.10)

What's new in Hardhat
---------------------

[](https://blog.nomic.foundation/solidity-vs-typescript-tests-how-to-choose-and-combine-in-hardhat-3/)

![Image 24: Solidity vs. TypeScript tests: How to choose and combine in Hardhat 3](https://blog.nomic.foundation/content/images/2025/10/Hardhat-Gosht-Post-Banner-V2.png)

### Solidity vs. TypeScript tests: How to choose and combine in Hardhat 3

Testing is central to Ethereum smart contract development, as bugs and vulnerabilities can lead to catastrophic losses. Most projects tests contracts either in TypeScript or Solidity. With Hardhat 3, you don’t have to choose between writing all your tests in Solidity or in TypeScript — both are first-class options, they can be combined, and each brings their unique strengths. The key is knowing where each approach fits best, and how they complement one another. Solidity Tests Writing tests d

[](https://blog.nomic.foundation/rust-powered-hardhat-present-future/)

![Image 25: Rust-powered Hardhat: Present & Future](https://blog.nomic.foundation/content/images/2024/08/EDR-announcement-blogpost-image.png)

### Rust-powered Hardhat: Present & Future

In March, we released Hardhat v2.21.0, the first version powered by our brand new Ethereum Development Runtime (EDR, for short) implemented in Rust. This was a significant change under the hood, representing the rewriting of Hardhat's largest and most complex component—its Ethereum simulation layer—in a new language. By design, this update didn’t affect the user experience beyond improving performance. In this post, we’ll explain why we built EDR, discuss its current status, and outline what’s c

[](https://blog.nomic.foundation/secure-deployments-with-hardhat-ignition-and-ledger-hardware-wallets-028080159e77/)

![Image 26: Secure deployments with Hardhat Ignition and Ledger hardware wallets](https://blog.nomic.foundation/content/images/max/1200/1-jtudwgpzwc8p9xpfrnya3a.jpg)

### Secure deployments with Hardhat Ignition and Ledger hardware wallets

As you may know, we recently introduced Hardhat Ignition, a declarative system for deploying smart contracts on Ethereum, which aims to…

Tell me about new product features as they come out
---------------------------------------------------

##### Built by

![Image 27: Nomic Foundation](https://hardhat.org/_astro/nomic-foundation-logo.BjNjHHvQ_Z17TxzU.svg)

![Image 28: Nomic Foundation](https://hardhat.org/_astro/nomic-foundation-logo-dark.BvbyFhmX_Z17TxzU.svg)

##### Copyright 2026 Nomic Foundation | [Privacy Policy](https://hardhat.org/privacy-policy.html)

### Cookie Policy

We use cookies to improve your experience on our website. [Read More](https://hardhat.org/privacy-policy.html)

Reject all Accept all
