# Semgrep docs

Source: https://semgrep.dev/docs/

- [](/docs/)- Docs home[*](https://semgrep.dev)Semgrep docs
##### Find bugs and reachable dependency vulnerabilities in code. Enforce your code standards on every commit.
### Scan with Semgrep AppSec Platform
Deploy static application security testing (SAST), software composition analysis (SCA), and secrets scans from one platform.

[###### Get startedRun your first Semgrep scan.**

](/docs/getting-started/quickstart-managed-scans)[###### Deploy SemgrepDeploy Semgrep to your organization quickly and at scale.

](/docs/deployment/core-deployment)[###### Triage and remediateTriage and remediate findings; fine-tune guardrails for developers.

](/docs/semgrep-code/triage-remediation)[###### Write rulesEnforce your organization’s coding standards with custom rules.

](/docs/writing-rules/overview)
### Supported languages
ProductLanguagesSemgrep Code**Generally available (GA)**C and C++ • C# • Generic • Go • Java • JavaScript • JSON • Kotlin • Python • TypeScript • Ruby • Rust • JSX • PHP • Scala • Swift • Terraform **Beta**APEX • Elixir**Experimental**Bash • Cairo • Circom • Clojure • Dart • Dockerfile • Hack • HTML • Jsonnet • Julia • Lisp • Lua • Move on Aptos • Move on Sui • OCaml• R • Scheme • Solidity • YAML • XMLSemgrep Supply Chain**Generally available reachability**C# • Go • Java • JavaScript and TypeScript • Kotlin • PHP • Python • Ruby • Scala • Swift **Languages without support for reachability analysis**Dart • Elixir • RustSemgrep SecretsLanguage-agnostic; can detect 630+ types of credentials or keys.
See the [Supported languages](/docs/supported-languages#language-maturity-summary) documentation for more details.

### November 2025 release notes summary

- **Cortex** and **Sysdig** integrations are now generally available. Semgrep now uses deployment status and, for Cortex, internet-exposure data from these CNAPP providers to better prioritize findings.
- Malicious dependency detection is now generally available. Semgrep detects malicious packages, including malware, typosquatting, and credential-stealing dependencies, using over 80,000 rules.
- Assistant now automatically analyzes **all new Critical and High-severity findings** with **Medium or High confidence** in full scans, removing the previous 10-issue limit.
- The **Settings &gt; General** tab now displays all Semgrep product settings on a single page.

[See the latest release notes *](/docs/release-notes)

[** Subscribe to RSS feed ](https://semgrep.dev/docs/release-notes/rss.xml)Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/index.md)Last updated on Dec 9, 2025**