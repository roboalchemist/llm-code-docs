# Scala support

Source: https://semgrep.dev/docs/languages/scala

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages- Scala**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [scala](/docs/tags/scala)Scala support
tipSemgrep’s Scala coverage leverages framework-specific analysis capabilities that are not present in Semgrep Community Edition (CE). As a result, many framework specific Pro rules will **fail** to return findings if run on Semgrep CE. To ensure full security coverage, run: `semgrep login &amp;&amp; semgrep ci`.

## Semgrep Code analyses[​](#semgrep-code-analyses)

- Interprocedural analysis (cross-function)
- All analyses performed by [Semgrep Community Edition (CE)](#scala-support-in-semgrep-ce)

## Coverage[​](#coverage)
Semgrep aims to provide comprehensive and accurate detection of common OWASP Top 10 issues in source code. Semgrep uses **rules**, which are instructions based on which it detects patterns in code. These rules are usually organized in rulesets.

By default, Semgrep Code provides you with the [** `p/comment`](https://semgrep.dev/p/comment) and [** `p/default`](https://semgrep.dev/p/default) rulesets. These rulesets provide the most accurate and comprehensive coverage across Semgrep&#x27;s supported languages.

Some examples of rules include:

- [** CWE-89: SQL injection. Avoid using unsanitized user input when generating SQL strings](https://semgrep.dev/playground/r/scala.play.security.tainted-slick-sqli.tainted-slick-sqli?editorMode=advanced)
- [** CWE-78: OS command injection. Sanitize variables that are used in external processes.](https://semgrep.dev/playground/r/scala.lang.security.audit.dangerous-seq-run.dangerous-seq-run)

## Scala support in Semgrep Supply Chain[​](#scala-support-in-semgrep-supply-chain)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

### Supported package managers[​](#supported-package-managers)
Semgrep supports the following Scala package manager:

- Maven

### Analyses and features[​](#analyses-and-features)
The following analyses and features are available for Scala:

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

License detectionSemgrep Supply Chain&#x27;s **license compliance** feature enables you to explicitly allow or disallow (block) a package&#x27;s use in your repository based on its license. For example, your company policy may disallow the use of packages with the Creative Commons Attribution-NonCommercial (CC-BY-NC) license.

SBOM generationSemgrep enables you to generate a software bill of materials (SBOM) to assess your third-party dependencies and comply with auditing procedures. Semgrep Supply Chain (SSC) can generate an SBOM for each repository you have added to Semgrep AppSec Platform.

## Scala support in Semgrep CE[​](#scala-support-in-semgrep-ce)
Semgrep CE is a fast, lightweight program analysis tool that can help you detect bugs in your code. It makes use of Semgrep&#x27;s LGPL 2.1 open source engine.

### Analyses[​](#analyses)

- Single-file, cross-function constant propagation
- Single-function taint analysis
- Semantic analysis

### Coverage[​](#coverage)
tip
- Check the `license` of a rule to ensure it meets your licensing requirements. See [Licensing](/docs/licensing) for more details.

The Semgrep Registry provides the following Scala rule sets:

tk

- [** `p/default`](https://semgrep.dev/p/default)
- [** `p/scala`](https://semgrep.dev/p/scala)

Sample usage:

`semgrep scan --config p/scala`Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [scala](/docs/tags/scala)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/languages/scala.md)Last updated on **Sep 30, 2025**