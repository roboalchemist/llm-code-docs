# Semgrep Code overview

Source: https://semgrep.dev/docs/semgrep-code/overview

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Scan and triage- SAST (Code)- Overview**On this page- [Semgrep Code](/docs/tags/semgrep-code)Semgrep Code overview
Semgrep Code is a static application security testing (SAST) tool that detects security vulnerabilities in your first-party code.

You can use Semgrep Code to scan local repositories or integrate it into your CI/CD pipeline to automate the continuous scanning of your code.

## Rules[​](#rules)
Semgrep Code uses **rules**, which encapsulate pattern matching logic and data flow analysis, to scan your code for security issues, style violations, bugs, and more. Semgrep generates and reports **findings** to you whenever it finds code that matches the patterns defined by rules.

In addition to rules available in the [Registry](https://semgrep.dev/r), you can write custom rules to determine what Semgrep Code detects in your repositories. Whether you use pre-existing rules or write custom rules, knowing *which* rules Semgrep Code runs can help you understand how it detects security issues.

Semgrep Code is transparent; you can configure the rules it runs and inspect its syntax to understand how the finding was detected. You can also customize the content of a rule to improve the true positive rate of a rule or have Semgrep send a relevant message to developers.

## Findings[​](#findings)
Semgrep AppSec Platform displays Semgrep Code&#x27;s findings. Additionally, the platform allows you to:

- Triage findings
- Send alerts and notifications or create tickets to track findings identified by Semgrep Code
- Customize how Semgrep Code scans your repositories
- Manage your users and facilitate team collaboration in remediating security issues

## Semgrep Community Edition (CE) versus Semgrep Code analysis[​](#semgrep-community-edition-ce-versus-semgrep-code-analysis)
By default, Semgrep Code can analyze interactions beyond a single function but within a single file, a process known as **cross-function or interprocedural analysis**. This smaller scope of analysis makes it faster and easier to integrate into developer workflows.

Semgrep CE can only analyze interactions within a single function, known as intraprocedural or single-function analysis. However, this means that Semgrep CE is slightly faster than Semgrep Code. 

Semgrep Code also supports **[cross-file analysis](/docs/semgrep-code/semgrep-pro-engine-intro)** (interfile) analysis. These scans produce fewer false positives and more true positives, but take longer to complete.

## Enable Semgrep Code[​](#enable-semgrep-code)

- Sign in to [** Semgrep AppSec Platform](https://semgrep.dev/login).
- Go to **[Settings &gt; General &gt; Code](https://semgrep.dev/orgs/-/settings/general/code)**.
- Click the **** Code scans** toggle if it is not already enabled.

Subsequent scans now include Code scans.

### Run Semgrep Code scans with single-function analysis[​](#run-semgrep-code-scans-with-single-function-analysis)
In some cases, you may want to scan using Semgrep CE&#x27;s single-function analysis. To do this, edit your `semgrep ci` command in your CI provider&#x27;s configuration file with either the `--pro-languages` or `--oss-only` flags:

`# Preferred; includes support for all Semgrep Code languagessemgrep ci --pro-languages# Does not include all Semgrep Code language featuressemgrep ci --oss-only`
## Augment Semgrep Code with Semgrep Assistant[​](#augment-semgrep-code-with-semgrep-assistant)
[Semgrep Assistant](/docs/semgrep-assistant/overview) provides AI-powered security recommendations to help you review, triage, and remediate your Semgrep findings. More specifically, Assistant can:

- Provide [remediation advice](/docs/semgrep-assistant/overview#remediation) and autofixes, or suggested fixes, for Semgrep Code findings. This information is displayed in Semgrep AppSec Platform.
- Provide [remediation guidance](/docs/semgrep-assistant/overview#guidance) with step-by-step instructions on how to remediate the finding identified by Semgrep Code in every pull request or merge request comment Semgrep pushes.

Assistant supports the tailoring of its remediation guidance using [Memories](/docs/semgrep-assistant/overview#memories).

- [Tag your findings](/docs/semgrep-assistant/overview#component-tags) in Semgrep AppSec Platform to help identify high-priority issues.
- [Auto-triage findings](/docs/semgrep-assistant/overview#auto-triage) and suggest whether a finding can safely be ignored.
- [Filter out potential false positives](/docs/semgrep-assistant/overview#noise-filtering-beta) to help increase developer velocity.

## Next steps[​](#next-steps)

- [View your findings](/docs/semgrep-code/findings).
- Customize how Semgrep Code scans your repository by modifying the [default rules set](https://semgrep.dev/p/default) or [writing your own rules](/docs/semgrep-code/editor#write-a-new-rule-by-forking-an-existing-rule).
- Enable [autofix](/docs/writing-rules/autofix) so that Semgrep can push code suggestions to GitHub or GitLab to help your developers resolve findings.
- Enable [cross-file scanning](/docs/semgrep-code/semgrep-pro-engine-intro).

## Further reading[​](#further-reading)

- Read the [Trail of Bits Automated Testing Handbook](https://appsec.guide/) to learn about configuring and optimizing security tools, including Semgrep.
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-code/overview.md)Last updated on **Dec 10, 2025**