# Write rules

Source: https://semgrep.dev/docs/writing-rules/overview

- [](/docs/)- [Write rules](/docs/writing-rules/overview)- Write rules for Semgrep Code- Overview**On this page- [Rule writing](/docs/tags/rule-writing)Write rules
Semgrep uses rules, which encapsulate pattern matching logic and data flow analysis, to scan your code for security issues, style violations, bugs, and more. In addition to rules available to you in the Semgrep Registry, you can write custom rules to determine what Semgrep detects in your repositories. You can write rules that:

- Automate code review comments.
- Identify secure coding violations.
- Scan configuration files.

See more use cases in [Rule ideas](/docs/writing-rules/rule-ideas).

## Get started[​](#get-started)
For an introduction to writing Semgrep rules, use the interactive, example-based [Semgrep rule tutorial](https://semgrep.dev/learn).

You can write rules in your terminal and run them with the Semgrep command line tool, or you can write and test using the [Semgrep Editor](https://semgrep.dev/editor).

For example, the following sample rule detects the use of `is` when comparing Python strings. `is` checks reference equality, not value equality, and can exhibit nondeterministic behavior.

## Next steps[​](#next-steps)
The following articles guide you through rule-writing basics and act as references:

- [Pattern syntax](/docs/writing-rules/pattern-syntax) describes what Semgrep patterns can do in detail and provides sample use cases.
- [Rule syntax](/docs/writing-rules/rule-syntax) describes Semgrep YAML rule files, which can have multiple patterns, detailed output messages, and autofixes. The syntax allows the composition of individual patterns with Boolean operators.
- [Contributing rules](/docs/contributing/contributing-to-semgrep-rules-repository) gives you an overview of how you can contribute to Semgrep Registry rules. This document also provides information about tests and metadata fields that you can use for your rules.

Need rule ideas? See [Rule ideas](/docs/writing-rules/rule-ideas) for everyday use cases and prompts to help you start writing rules from scratch.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Rule writing](/docs/tags/rule-writing)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/writing-rules/overview.md)Last updated on **Oct 15, 2025**