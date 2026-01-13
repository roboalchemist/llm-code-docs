# Java support

Source: https://semgrep.dev/docs/languages/java

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages- Java**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [java](/docs/tags/java)Java support
tipSemgrep’s Java coverage leverages framework-specific analysis capabilities that are not present in Semgrep Community Edition (CE). As a result, many framework specific Pro rules will **fail** to return findings if run on Semgrep CE. To ensure full security coverage, run: `semgrep login &amp;&amp; semgrep ci`.

## Semgrep Code analyses[​](#semgrep-code-analyses)

- [Language-specific analysis](/docs/semgrep-code/java)
- Interfile analysis (cross-file)
- Interprocedural analysis (cross-function)
- All analyses performed by [Semgrep Community Edition (CE)](#java-support-in-semgrep-ce)

## Coverage[​](#coverage)
Semgrep aims to provide comprehensive and accurate detection of common OWASP Top 10 issues in source code. Semgrep uses **rules**, which are instructions based on which it detects patterns in code. These rules are usually organized in rulesets.

By default, Semgrep Code provides you with the [** `p/comment`](https://semgrep.dev/p/comment) and [** `p/default`](https://semgrep.dev/p/default) rulesets. These rulesets provide the most accurate and comprehensive coverage across Semgrep&#x27;s supported languages.

Some examples of rules include:

- [** CWE-327: Use of a broken or risky cryptographic algorithm. Don&#x27;t use the `none` algorithm](https://semgrep.dev/playground/r/java.java-jwt.security.jwt-none-alg.java-jwt-none-alg?editorMode=advanced)
- [** CWE-78: OS command injection. Sanitize your variables before using them as input to a `java.lang.Runtime` call](https://semgrep.dev/playground/r/java.lang.security.audit.command-injection-formatted-runtime-call.command-injection-formatted-runtime-call?editorMode=advanced)

## Java support in Semgrep Supply Chain[​](#java-support-in-semgrep-supply-chain)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

### Supported package managers[​](#supported-package-managers)
Semgrep supports the following Java package managers:

- Gradle
- Maven

### Analyses and features[​](#analyses-and-features)
The following analyses and features are available for Java:

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

License detectionSemgrep Supply Chain&#x27;s **license compliance** feature enables you to explicitly allow or disallow (block) a package&#x27;s use in your repository based on its license. For example, your company policy may disallow the use of packages with the Creative Commons Attribution-NonCommercial (CC-BY-NC) license.

SBOM generationSemgrep enables you to generate a software bill of materials (SBOM) to assess your third-party dependencies and comply with auditing procedures. Semgrep Supply Chain (SSC) can generate an SBOM for each repository you have added to Semgrep AppSec Platform.

No need for lockfilesJava projects can be scanned **without** the need for lockfiles. See [Scan a project without lockfiles (beta)](/docs/semgrep-supply-chain/getting-started#scan-a-project-without-lockfiles-beta).

## Java support in Semgrep CE[​](#java-support-in-semgrep-ce)
Semgrep CE is a fast, lightweight program analysis tool that can help you detect bugs in your code. It makes use of Semgrep&#x27;s LGPL 2.1 open source engine.

### Analyses[​](#analyses)

- Single-file, cross-function constant propagation
- Single-function taint analysis
- Semantic analysis

### Coverage[​](#coverage)
tip
- Check the `license` of a rule to ensure it meets your licensing requirements. See [Licensing](/docs/licensing) for more details.

The Semgrep Registry provides the following Java rulesets:

- [** `p/default`](https://semgrep.dev/p/default)
- [** `p/java`](https://semgrep.dev/p/java)
- [** `p/findsecbugs`](https://semgrep.dev/p/findsecbugs)

Sample usage:

`semgrep scan --config p/java`Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [java](/docs/tags/java)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/languages/java.md)Last updated on **Sep 30, 2025**