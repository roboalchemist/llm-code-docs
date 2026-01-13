# Semgrep for developers

Source: https://semgrep.dev/docs/for-developers/overview

- [](/docs/)- [For developers](/docs/for-developers/overview)- Overview**On this page- [Guides for developers](/docs/tags/guides-for-developers)Semgrep for developers
This guide is for developers who are using Semgrep in a team or organizational setting.

Use Semgrep to:

- Triage security issues
- Follow best practices set by your organization
- Automate code reviews among your peers
- Lint your code

This document provides an overview of how developers work with Semgrep to resolve the issues it detects.

Developer and AppSec rolesIf you are a developer responsible for your **own** security program in personal projects, see the [Quickstart](/docs/getting-started/quickstart) and [Core deployment](/docs/deployment/core-deployment) documentation.

## Semgrep AppSec Platform[​](#semgrep-appsec-platform)
Semgrep AppSec Platform, or simply **Semgrep**, is a software suite for implementing and tracking security programs.

**AppSec engineers** use Semgrep to detect, triage, and remediate findings across an entire organization&#x27;s codebases.

**Developers** primarily interact with Semgrep when Semgrep scans a project, then notifies users of issues in their code. Issues detected by Semgrep are called **findings**. The pattern-matching logic by which Semgrep detects a finding is encapsulated in a **rule**. Semgrep performs various static analyses to detect bugs, vulnerabilities in dependencies, and leaked secrets.

## How developers use Semgrep[​](#how-developers-use-semgrep)
Your interactions with Semgrep vary depending on your organization&#x27;s deployment of it.

Semgrep is almost always integrated into your CI and source code manager (SCM) and automatically runs on every pull request or merge request you open. These scans are **diff-aware** and only affect the scope of your PR, which keeps the scan speed fast. Your security engineer may configure Semgrep to display PR or MR comments about certain **blocking** or **non-blocking** findings to you, which you can resolve or ignore from within your SCM.

***Figure**. A PR comment detecting a hardcoded secret.*

It is less frequent, but still common, for developers to run Semgrep as part of their day-to-day coding workflow in the following environments:

- IDEs (VS Code and IntelliJ)
- CLI, including `pre-commit`

Your AppSec team is likely to have guidelines about Semgrep scans in these environments.

Noise in your pull requests or merge requests?Your security engineers are in full control of what findings are displayed to you. If you notice a high rate of false positives, tell your security engineers so that they can tune your scans.

## Semgrep findings in your PR or MR[​](#semgrep-findings-in-your-pr-or-mr)
Semgrep findings are typically posted in your PR or MR. The following image displays the parts of a Semgrep PR comment in GitHub; this example appears in a similar form in GitLab and other SCMs:

***Figure**. An example of a PR comment with various sections annotated.*

A - Block indicatorThis appears if a finding fails the CI job. Organizations typically block PRs or MRs with failed jobs.B - Finding descriptionA human-written description always appears in a PR or MR comment, describing why your code is flagged. **References** may also be included to help you learn more about the finding.C - Dataflow graphSome Code findings have a dataflow graph, which indicates that the finding was detected through [taint analysis](/docs/writing-rules/glossary#taint-analysis). The dataflow graph provides the lines of code identifying sources, sinks, and traces of unsanitized data flowing through your program. You can click the links on the boxes to take you to the lines of code.D - Resolution or remediation sectionVarious options are provided to help your resolve the finding. Depending on the [type of finding](#type-of-findings-by-resolution), resolution options may vary.E - Ignore instructionsClick to view instructions about how to ignore the finding by replying to the comment.
### Type of findings by resolution[​](#type-of-findings-by-resolution)
Code findingThis type of finding is typically resolved by refactoring your code. This finding typically catches bugs, security issues, or violations of best practices.Dependency findingSemgrep found that you&#x27;re using a vulnerable version of a dependency. It can also detect if you&#x27;re using the vulnerable function or code of the dependency.License findingSemgrep has found that you&#x27;re using a dependency with a **license** that may violate the guidelines set by your organization.Secrets findingSemgrep has detected a leaked secret. Rotate the secret to resolve this finding.

***Figure**. Summary of findings by resolution, assuming that the finding is a true positive.*

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Guides for developers](/docs/tags/guides-for-developers)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/for-developers/developer-overview.md)Last updated on **Jan 16, 2025**