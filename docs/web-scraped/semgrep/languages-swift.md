# Swift support

Source: https://semgrep.dev/docs/languages/swift

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages- Swift**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [swift](/docs/tags/swift)Swift support
tipSemgrep’s Swift coverage leverages framework-specific analysis capabilities that are not present in Semgrep Community Edition (CE). As a result, many framework specific Pro rules will **fail** to return findings if run on Semgrep CE. To ensure full security coverage, run: `semgrep login &amp;&amp; semgrep ci`.

## Semgrep Code analyses[​](#semgrep-code-analyses)

- Interprocedural analysis (cross-function)
- All analyses performed by [Semgrep Community Edition (CE)](#swift-support-in-semgrep-ce)

## Coverage[​](#coverage)
Semgrep aims to provide comprehensive and accurate detection of common OWASP Top 10 issues in source code. Semgrep uses **rules**, which are instructions based on which it detects patterns in code. These rules are usually organized in rulesets.

By default, Semgrep Code provides you with the [** `p/comment`](https://semgrep.dev/p/comment) and [** `p/default`](https://semgrep.dev/p/default) rulesets. These rulesets provide the most accurate and comprehensive coverage across Semgrep&#x27;s supported languages.

Some examples of rules include:

- [** CWE-477: Use of obsolete function. `ptrace` API is forbidden from iOS applications](https://semgrep.dev/orgs/-/editor/r/swift.lang.forbidden.forbidden-ios-api.swift-forbidden-ios-apis?editorMode=advanced)
- [** CWE-327: Use of a broken or risky cryptographic algorithm. Avoid MD2](https://semgrep.dev/orgs/-/editor/r/swift.commoncrypto.insecure-hashing-algorithm-md2.insecure-hashing-algorithm-md2?editorMode=advanced)

To view these rules, sign in to Semgrep AppSec Platform.

## Swift support in Semgrep Supply Chain[​](#swift-support-in-semgrep-supply-chain)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

### Supported package managers[​](#supported-package-managers)
Semgrep supports the following Swift package manager:

- SwiftPM

### Analyses and features[​](#analyses-and-features)
The following analyses and features are available for Swift:

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

License detectionSemgrep Supply Chain&#x27;s **license compliance** feature enables you to explicitly allow or disallow (block) a package&#x27;s use in your repository based on its license. For example, your company policy may disallow the use of packages with the Creative Commons Attribution-NonCommercial (CC-BY-NC) license.

SBOM generationSemgrep enables you to generate a software bill of materials (SBOM) to assess your third-party dependencies and comply with auditing procedures. Semgrep Supply Chain (SSC) can generate an SBOM for each repository you have added to Semgrep AppSec Platform.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [swift](/docs/tags/swift)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/languages/swift.md)Last updated on **Sep 30, 2025**