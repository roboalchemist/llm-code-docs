# Supported languages

Source: https://semgrep.dev/docs/supported-languages

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages**On this page- [Deployment](/docs/tags/deployment)Supported languages
This document provides information about supported languages and language maturity definitions for the following products:

- **Semgrep Code (SAST)** - a static application security testing (SAST) solution designed to detect complex security vulnerabilities.
- **Semgrep Supply Chain (SCA)** - a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

Semgrep Code and Semgrep Supply Chain are free for [small teams](https://semgrep.dev/pricing).

## Language maturity summary[​](#language-maturity-summary)
The following table lists all **Generally available (GA)** and **Beta** languages for Semgrep Code and Semgrep Supply Chain.

Languages are arranged by feature completeness from most to least. **Cross-file (interfile)** analysis for Semgrep Code and **reachability** analysis for Semgrep Supply Chain are the most advanced analyses that Semgrep provides; see [Feature definitions](#feature-definitions) for more details.

**Languages****Semgrep Code**Supports 35+ languages**Semgrep Supply Chain**Supports 14 languages[C#](/docs/languages/csharp)**Generally available**
• Cross-file dataflow analysis
• Supports up to C# 13
• 170+ Pro rules **Generally available**
• Reachability analysis
• Can detect open source licenses
• Can detect malicious dependencies[Go](/docs/languages/go)**Generally available**
• Cross-file dataflow analysis
• 80+ Pro rules **Generally available**
• Reachability analysis
• Can detect open source licenses
• Can detect malicious dependencies[Java](/docs/languages/java)**Generally available**
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 190+ Pro rules **Generally available**
• Reachability analysis
• Can detect open source licenses[JavaScript](/docs/languages/javascript)**Generally available**
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 250+ Pro rules**Generally available**
• Reachability analysis
• Can detect open source licenses
• Can detect malicious dependencies[Kotlin](/docs/languages/kotlin)**Generally available **
• Cross-file dataflow analysis
• 60+ Pro rules**Generally available**
• Reachability analysis
• Can detect open source licenses[Python](/docs/languages/python)**Generally available**
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 710+ Pro rules
• See [Python-specific support details](/docs/languages/python)**Generally available**
• Reachability analysis
• Can detect open source licenses
• Can detect malicious dependenciesTypescript**Generally available **
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 230+ Pro rules**Generally available**
• Reachability analysis
• Can detect malicious dependencies
• Can detect open source licensesC / C++**Generally available**
• Cross-file dataflow analysis
• 150+ Pro rules N/aJSX**Generally available **
• Cross-function dataflow analysis
• 70+ Pro rules**Generally available**
• Reachability analysis
• Can detect open source licenses[Ruby](/docs/languages/ruby)**Generally available **
• Cross-function dataflow analysis
• 40+ Pro rules**Generally available**
• Reachability analysis
• Can detect open source licenses
• Can detect malicious dependencies[Scala](/docs/languages/scala)**Generally available **
• Cross-function dataflow analysis
• Community rules**Generally available**
• Reachability analysis
• Can detect open source licenses[Swift](/docs/languages/swift)**Generally available **
• Cross-function dataflow analysis
• 60+ Pro rules**Generally available**
• Reachability analysis
• Can detect open source licensesRust**Generally available **
• Cross-function dataflow analysis
• 40+ Pro rules**Beta**
• Can detect open source licenses
• Can detect malicious dependenciesPHP**Generally available **
• Cross-function dataflow analysis
• 50+ Pro rules**Generally available**
• Reachability analysis
• Can detect open source licensesTerraform**Generally available**
• Cross-function dataflow analysis
• Community rulesN/aGeneric**Generally available **N/aJSON**Generally available **N/aElixir**Beta****Beta**APEX**Beta**--Dart**Experimental****Beta**
Click to view experimental languages for Semgrep Code.
- Bash
- Cairo
- Circom
- Clojure
- Dockerfile
- Hack
- HTML
- Jsonnet
- Julia
- Lisp
- Lua
- Move on Aptos
- Move on Sui
- OCaml
- R
- Scheme
- Solidity
- YAML
- XML

### Language maturity levels[​](#language-maturity-levels)
#### Semgrep Code[​](#semgrep-code)
Semgrep Code languages can be classified into four maturity levels:

- Generally available (GA)
- Beta
- Experimental
- Community supported*

*Community supported languages meet the parse rate and syntax requirements of **Experimental** languages. Users can still access community rules or write their own rules.

Click to view table of definitions.**Feature****GA****Beta****Experimental****Community supported**SupportHighest quality support by the Semgrep team. Reported issues are resolved promptly.Supported by the Semgrep team. Reported issues are fixed after GA languages.There are limitations to this language&#x27;s functionality. Reported issues are tracked and prioritized with best effort.These languages are supported by the Semgrep community. While Semgrep may develop rules or engine updates for these languages, they are not prioritized.Parse Rate99%+95%+90%+Number of Pro rules10+5+0+. Query the [Registry](https://semgrep.dev/r) to see if any rules exist for your language.Semgrep syntaxRegex, equivalence, deep expression operators, types and typing. All features supported in Beta.Complete metavariable support, metavariable equality. All features supported in Experimental.Syntax, ellipsis operator, basic metavariable functionality.
#### Semgrep Supply Chain[​](#semgrep-supply-chain)
Semgrep Supply Chain has two language maturity levels:

- Generally available
- Beta

Click to view table of definitions.**Feature****Generally available****Beta**Number of reachability rulesAs defined by [CVE coverage](#cve-coverage).All critical severity CVEs from [supported sources](#supported-sources) starting 2022 onwards, for packages used by customers with an active, paid subscription.Semgrep, Inc. rule-writing supportQuickly support CVE coverage with reachability analysis for all critical and high vulnerabilities based on the latest [security advisories](https://nvd.nist.gov/vuln).Coverage for CVEs but without reachability analysis.Semgrep Community Edition (CE) [language support](/supported-languages#semgrep-oss-language-support)Semgrep CE support is GA.Semgrep CE support is at least Beta.
### Feature definitions[​](#feature-definitions)
Cross-file dataflow analysisCross-file analysis (also known as **interfile analysis**) takes into account how information flows between files. In particular, cross-file analysis includes **cross-file taint analysis**, which tracks unsanitized variables flowing from a source to a sink through arbitrarily many files. Other analyses performed across files include constant propagation and type inference.

Cross-file analysis is usually used in contrast to intrafile, or per-file analysis, where each file is analyzed as a standalone block of code.

Languages with cross-file support also include cross-function support.

Cross-function dataflow analysisCross-function analysis means that interactions between functions are taken into account. This improves taint analysis, which tracks unsanitized variables flowing from a source to a sink through arbitrarily many functions.

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

See [Overview of Semgrep Supply Chain](/docs/semgrep-supply-chain/overview) to learn how Semgrep leverages its code-scanning and rule syntax capabilities to provide high-signal rules that determine a finding&#x27;s reachability. This assists security engineers in remediation and triage processes.

tipSee [Language maturity levels](#language-maturity-levels) to learn which features define GA or beta language support.

## Semgrep Supply Chain feature support[​](#semgrep-supply-chain-feature-support)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies. It can also:

- Generate a software bill of materials (SBOM) that provides a complete inventory of your open source components
- Query for information about your dependencies
- Support the enforcement of your business&#x27; open source package licensing requirements
- Detect malicious dependencies (this feature is currently in invite-only beta; please contact [Semgrep Support](/docs/support) for more information)

For projects with lockfiles, Semgrep parses lockfiles for dependencies, then scans your codebase for reachable findings based on the lockfiles. For a lockfile to be scanned by Semgrep Supply Chain, it must have one of the supported lockfile names.

For some languages, a lockfile or manifest file is parsed to determine [transitivity](/docs/semgrep-supply-chain/glossary#transitive-or-indirect-dependency). See [Transitive dependencies and reachability analysis](/docs/semgrep-supply-chain/overview#transitive-dependencies-and-reachability-analysis) for more information.

Additionally, Semgrep offers beta support for the scanning of projects written in the following languages **without lockfiles**:

- C#
- Java
- Kotlin
- Python
- Ruby

### Package manager support[​](#package-manager-support)
The following table lists all Semgrep-supported package managers for each language. Languages  with **reachability** support are listed first.

LanguageSupported package managersManifest file or lockfileC#NuGet`packages.lock.json`GoGo modules (`go mod`)`go.mod`JavaGradle`gradle.lockfile`MavenMaven-generated dependency tree (See [Setting up SSC scans for Apache Maven](/docs/semgrep-supply-chain/setup-maven/) for instructions.)JavaScript or TypeScriptnpm`package-lock.json`Yarn`yarn.lock`pnpm`pnpm-lock.yaml`KotlinGradle`gradle.lockfile`MavenMaven-generated dependency tree (See [Setting up SSC scans for Apache Maven](/docs/semgrep-supply-chain/setup-maven/) for instructions.)PythonpipAny of the following: - `*requirement*.txt` or `*requirement*.pip`- Any manifest file in a requirements folder, such as `**/requirements/*.txt` or `**/requirements/*.pip` The file must be generated automatically and have values set to exact versions (pinned dependencies).pip-toolsPipenv`Pipfile.lock`Poetry`poetry.lock`uv`uv.lock`RubyRubyGems`Gemfile.lock`ScalaMavenMaven-generated dependency tree (See [Setting up SSC scans for Apache Maven](/docs/semgrep-supply-chain/setup-maven/) for instructions.)SwiftSwiftPM`Package.swift` file and Swift-generated `Package.resolved` file. (See [Swift documentation ](https://www.swift.org/documentation/package-manager/) for instructions.)RustCargo*`cargo.lock`DartPub`pubspec.lock`ElixirHex`mix.lock`PHPComposer`composer.lock`
******Supply Chain does not analyze the transitivity of packages for these language and manifest file or lockfile combinations. All dependencies are listed as **No Reachability Analysis.***

### Feature support[​](#feature-support)
The following table lists all Supply Chain features for each language. Languages with **reachability** support are listed first.

LanguageReachability(see [CVE coverage](#cve-coverage))[Scan without lockfiles (beta)](/docs/semgrep-supply-chain/getting-started#scan-a-project-without-lockfiles-beta)License detectionMalicious dependencydetectionC#✅✅✅✅Go✅--✅✅Java✅✅✅--JavaScript or TypeScript✅--✅✅Kotlin✅✅✅--Python✅✅✅ For PyPi only✅Ruby✅--✅✅Scala✅--✅--Swift✅--✅†--PHP✅--✅--RustNo reachability analysis. However, Semgrep can compare a package&#x27;s version against a list of versions with known vulnerabilities.--✅✅Dart------Elixir------
***†**License detection for new packages is asynchronous and processed after the initial scan. Policies aren&#x27;t applied on first detection, but are enforced in subsequent scans.*

#### CVE coverage[​](#cve-coverage)
For customers with an active paid subscription, Semgrep’s reachability analysis covers all **critical and high severity** CVEs from [supported sources](#supported-sources) starting in 2017 across all supported languages.

##### Supported sources[​](#supported-sources)

- [** Reviewed GitHub Security Advisories](https://github.com/advisories?query=type%3Areviewed)
- [** Electron release notes](https://releases.electronjs.org/releases/stable)

### Feature and product maturity levels[​](#feature-and-product-maturity-levels)
The detailed specifications previously provided apply only to language support. Language maturity levels differ from feature and product maturity levels.

## More information[​](#more-information)
Visit the cheat sheet generation script and associated semgrep-core test files to learn more about each feature:

- [Generation script](https://github.com/semgrep/semgrep/blob/develop/scripts/generate_cheatsheet.py)
- [`semgrep-core` test files](https://github.com/semgrep/semgrep/tree/develop/tests)
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Deployment](/docs/tags/deployment)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/supported-languages.md)Last updated on **Jan 7, 2026**