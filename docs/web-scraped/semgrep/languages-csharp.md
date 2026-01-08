# C# support

Source: https://semgrep.dev/docs/languages/csharp

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages- C#**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [c](/docs/tags/c)C# support
tipSemgrep’s C# coverage leverages framework-specific analysis capabilities that are not present in Semgrep Community Edition (CE). As a result, many framework specific Pro rules will **fail** to return findings if run on Semgrep CE. To ensure full security coverage, run: `semgrep login &amp;&amp; semgrep ci`.

## Semgrep Code analyses[​](#semgrep-code-analyses)

- Interfile analysis (cross-file)
- Interprocedural analysis (cross-function)
- All analyses performed by [Semgrep Community Edition (CE)](#c-support-in-semgrep-ce)

## Coverage[​](#coverage)
Semgrep aims to provide comprehensive and accurate detection of common OWASP Top 10 issues in source code. Semgrep uses **rules**, which are instructions based on which it detects patterns in code. These rules are usually organized in rulesets.

By default, Semgrep Code provides you with the [** `p/comment`](https://semgrep.dev/p/comment) and [** `p/default`](https://semgrep.dev/p/default) rulesets. These rulesets provide the most accurate and comprehensive coverage across Semgrep&#x27;s supported languages.

Some examples of rules include:

- [** CWE-89: SQL injection. Don&#x27;t use formatted strings in SQL statements; prefer prepared statements](https://semgrep.dev/playground/r/csharp.lang.security.sqli.csharp-sqli.csharp-sqli?editorMode=advanced)
- [** CWE-90: LDAP injection. Avoid LDAP queries constructed dynamically on user-controlled input](https://semgrep.dev/playground/r/csharp.dotnet.security.audit.ldap-injection.ldap-injection?editorMode=advanced)
- [** CWE-347: Improper verification of cryptographic signature. Use signed security tokens](https://semgrep.dev/playground/r/csharp.lang.security.cryptography.unsigned-security-token.unsigned-security-token?editorMode=advanced)

## C# support in Semgrep Supply Chain[​](#c-support-in-semgrep-supply-chain)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

### Supported package managers[​](#supported-package-managers)
Semgrep supports the following C# package manager:

- NuGet

### Analyses and features[​](#analyses-and-features)
The following analyses and features are available for C#:

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

License detectionSemgrep Supply Chain&#x27;s **license compliance** feature enables you to explicitly allow or disallow (block) a package&#x27;s use in your repository based on its license. For example, your company policy may disallow the use of packages with the Creative Commons Attribution-NonCommercial (CC-BY-NC) license. Semgrep can help enforce this restriction.

Malicious dependency detectionSemgrep is able to detect malicious dependencies in your projects and in pull requests (PRs) or merge requests (MRs).

SBOM generationSemgrep enables you to generate a software bill of materials (SBOM) to assess your third-party dependencies and comply with auditing procedures. Semgrep Supply Chain (SSC) can generate an SBOM for each repository you have added to Semgrep AppSec Platform.

No need for lockfilesC# projects can be scanned **without** the need for lockfiles. See [Scan a project without lockfiles (beta)](/docs/semgrep-supply-chain/getting-started#scan-a-project-without-lockfiles-beta).

## C# support in Semgrep CE[​](#c-support-in-semgrep-ce)
Semgrep CE is a fast, lightweight program analysis tool that can help you detect bugs in your code. It makes use of Semgrep&#x27;s LGPL 2.1 open source engine.

### Analyses[​](#analyses)

- Single-file, cross-function constant propagation
- Single-function taint analysis
- Semantic analysis

### Coverage[​](#coverage)
tip
- Check the `license` of a rule to ensure it meets your licensing requirements. See [Licensing](/docs/licensing) for more details.

The Semgrep Registry provides the following  C# rule sets:

- [** `p/default`](https://semgrep.dev/p/default)
- [** `p/csharp`](https://semgrep.dev/p/csharp)
- [** `p/gitlab`](https://semgrep.dev/p/gitlab)

Sample usage:

`semgrep scan --config p/csharp`Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [c](/docs/tags/c)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/languages/csharp.md)Last updated on **Sep 30, 2025**