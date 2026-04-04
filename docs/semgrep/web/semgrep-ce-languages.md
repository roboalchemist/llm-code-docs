# Supported languages for Semgrep Community Edition (CE)

Source: https://semgrep.dev/docs/semgrep-ce-languages

- [](/docs/)- Semgrep Community Edition- Supported languages**On this page- [Semgrep CE](/docs/tags/semgrep-ce)- [Semgrep Code](/docs/tags/semgrep-code)Supported languages for Semgrep Community Edition (CE)
This document provides information about supported languages for Semgrep Code and Semgrep CE.

## Semgrep Code and CE[​](#semgrep-code-and-ce)
Semgrep CE is a fast, lightweight program analysis tool that can help you detect bugs in your code. It makes use of Semgrep&#x27;s LGPL 2.1 open source engine. These languages are supported by the Semgrep community, at best effort.

Semgrep Code is a static application security testing (SAST) solution designed to detect complex security vulnerabilities. It makes use of proprietary Semgrep analyses, such as cross-file (interfile) dataflow analysis and framework specific analyses, in addition to Semgrep CE. This results in a [**higher true positive rate than Semgrep CE**](/docs/semgrep-pro-vs-oss). Semgrep Code provides the highest quality support by the Semgrep team: reported issues are resolved promptly.

Use either tool to scan local code or integrate it into your CI/CD pipeline to automate the continuous scanning of your repositories.

**Languages****🚀 Semgrep Code:** [Free for small teams](https://semgrep.dev/pricing)**Semgrep CE**C / C++**Generally available**
• Cross-file dataflow analysis
• 150+ Pro rules  Community supported 
• Limited to single-function analysis
• Community rules C#**Generally available **
• Cross-file dataflow analysis
• Supports up to C# 13
• 170+ Pro rules  Community supported 
• Limited to single-function analysis
• Community rules 
• Supports up to C# 7.0Go**Generally available**
• Cross-file dataflow analysis
• 80+ Pro rules  Community supported 
• Limited to single-function analysis
• Community rules Java**Generally available**
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 190+ Pro rules JavaScript**Generally available**
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 250+ Pro rulesKotlin**Generally available **
• Cross-file dataflow analysis
• 60+ Pro rules[Python](/docs/languages/python)**Generally available**
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 710+ Pro rules
• See [Python-specific support details](/docs/languages/python)Typescript**Generally available **
• Cross-file dataflow analysis
• Framework-specific control flow analysis
• 230+ Pro rulesRuby**Generally available **
• Cross-function dataflow analysis
• 40+ Pro rulesRust**Generally available **
• Cross-function dataflow analysis
• 40+ Pro rulesJSX**Generally available **
• Cross-function dataflow analysis
• 70+ Pro rulesPHP**Generally available **
• Cross-function dataflow analysis
• 50+ Pro rulesScala**Generally available **
• Cross-function dataflow analysis
• Community rulesSwift**Generally available **
• Cross-function dataflow analysis
• 60+ Pro rulesTerraform**Generally available**
• Cross-function dataflow analysis
• Community rulesGeneric**Generally available **Community supportedJSON**Generally available **APEX**Beta**Not availableElixir**Beta**Click to view experimental languages.
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

## Language maturity definitions[​](#language-maturity-definitions)
Semgrep Code languages can be classified into four maturity levels:

- Generally available (GA)
- Beta
- Experimental
- Community supported*

*Community supported languages meet the parse rate and syntax requirements of **Experimental** languages. Users can still access community rules or write their own rules.

**Feature****GA****Beta****Experimental****Community supported**SupportHighest quality support by the Semgrep team. Reported issues are resolved promptly.Supported by the Semgrep team. Reported issues are fixed after GA languages.There are limitations to this language&#x27;s functionality. Reported issues are tracked and prioritized with best effort.These languages are supported by the Semgrep community. While Semgrep may develop rules or engine updates for these languages, they are not prioritized.Parse Rate99%+95%+90%+Number of Pro rules10+5+0+. Query the [Registry](https://semgrep.dev/r) to see if any rules exist for your language.Semgrep syntaxRegex, equivalence, deep expression operators, types and typing. All features supported in Beta.Complete metavariable support, metavariable equality. All features supported in Experimental.Syntax, ellipsis operator, basic metavariable functionality.Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep CE](/docs/tags/semgrep-ce)- [Semgrep Code](/docs/tags/semgrep-code)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-ce-languages.md)Last updated on **Sep 17, 2025**