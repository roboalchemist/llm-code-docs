# Source: https://docs.datadoghq.com/security/code_security/static_analysis/ai_enhanced_sast.md

---
title: AI-Enhanced Static Code Analysis
description: Automate security decision-making across the entire static analysis lifecycle
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) >
  AI-Enhanced Static Code Analysis
---

# AI-Enhanced Static Code Analysis

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Static Code Analysis (SAST) uses AI to help automate detection, validation, and remediation across the vulnerability management lifecycle. This page provides an overview of these features.

## Summary of AI features in SAST{% #summary-of-ai-features-in-sast %}

| Step of vulnerability management lifecycle | Feature                                                                                                | Trigger Point | Impact                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------- | ----------------------------------------------- |
| Detection                                  | Malicious PR protection: Detect potentially malicious changes or suspicious diffs                      | At PR time    | Flags PRs introducing novel risky code          |
| Validation                                 | False positive filtering: Deprioritize low-likelihood findings                                         | After scan    | Reduce noise, allow focus on actual issues      |
| Remediation                                | Batched remediation: Generate suggested fixes (and optionally PRs) for one or multiple vulnerabilities | After scan    | Reduces developer effort, accelerates fix cycle |

## Detection{% #detection %}

{% callout %}
##### Join the Preview!

Malicious PR protection is in Preview and supports GitHub repositories only. Click **Request Access** and complete the form.

[Request Access](https://www.datadoghq.com/product-preview/malicious-pr-protection/)
{% /callout %}

Malicious PR protection uses LLMs to detect and prevent malicious code changes at scale. By scanning pull requests (PRs) submitted to the default branches of your repositories to detect potentially malicious intent, this functionality helps you to:

- Secure code changes from both internal and external contributors
- Scale your code reviews as the volume of AI-assisted code changes increases
- Embed code security into your security incident response workflows

### Detection coverage{% #detection-coverage %}

Malicious code changes come in many different forms. Datadog SAST covers attack vectors such as:

- Malicious code injection
- Attempted secret exfiltration
- Pushing of malicious packages
- CI workflow compromise

Examples include the [tj-actions/changed-files breach (March 2025)](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) and [obfuscation of malicious code in npm packages (September 2025)](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem). Read more in the blog post [here](https://www.datadoghq.com/blog/engineering/malicious-pull-requests/).

### Search and filter results{% #search-and-filter-results %}

Detections from Datadog SAST on potentially malicious PRs can be found in [Security Signals](https://app.datadoghq.com/security) from the rule ID `def-000-wnp`.

There are two potential verdicts: `malicious` and `benign`. They can be filtered for using:

- `@malicious_pr_protection.scan.verdict:malicious`
- `@malicious_pr_protection.scan.verdict:benign`.

Signals can be triaged directly in Datadog (assign, create a case, or declare an incident), or routed externally using [Datadog Workflow Automation](https://docs.datadoghq.com/actions/workflows/).

## Validation and triage{% #validation-and-triage %}

### False positive filtering{% #false-positive-filtering %}

For a subset of SAST vulnerabilities, [Bits AI](https://docs.datadoghq.com/bits_ai/) reviews the context of the finding and assess whether it is more likely to be a true or false positive, along with a short explanation of the reasoning.

To narrow down your initial list for triage, in [Vulnerabilities](https://app.datadoghq.com/security/code-security/sast), select **Filter out false positives**. This option uses the `-bitsAssessment:"False Positive"` query.

Each finding includes a section with an explanation of the assessment. You can provide Bits AI with feedback on its assessment using a thumbs up ð or thumbs down ð.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/static_analysis/false_positive_filtering_sast_side_panel_higher_res_png.34cd8b7d9ddc445ffdd70c4dff065277.png?auto=format"
   alt="Visual indicator of a false positive assessment in SAST side panel" /%}



{% collapsible-section open=null #id-for-anchoring %}
#### Supported CWEs

False positive filtering is supported for the following CWEs:

- [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)

- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html)

- [CWE-90: LDAP Injection](https://cwe.mitre.org/data/definitions/90.html)

- [CWE-22: Path Traversal](https://cwe.mitre.org/data/definitions/22.html)

- [CWE-501: Trust Boundary Violation](https://cwe.mitre.org/data/definitions/501.html)

- [CWE-79: Cross-site Scripting](https://cwe.mitre.org/data/definitions/79.html)

- [CWE-614: Insecure Cookie](https://cwe.mitre.org/data/definitions/614.html)

- [CWE-327: Broken or Risky Cryptographic Algorithm](https://cwe.mitre.org/data/definitions/327.html)

- [CWE-643: XPath Injection](https://cwe.mitre.org/data/definitions/643.html)

- [CWE-94: Code Injection](https://cwe.mitre.org/data/definitions/94.html)

- [CWE-284: Improper Access Control](https://cwe.mitre.org/data/definitions/284.html)

- [CWE-502: Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)

{% /collapsible-section %}

## Remediation{% #remediation %}

{% callout %}
##### Join the Preview!

AI-suggested remediation for SAST is powered by the Bits AI Dev Agent and is in Preview. To sign up, click **Request Access** and complete the form.

[Request Access](http://datadoghq.com/product-preview/bits-ai-dev-agent)
{% /callout %}

Datadog SAST uses the [Bits AI Dev Agent](https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent) to generate single and bulk remediations for vulnerabilities.

### Fix a single vulnerability{% #fix-a-single-vulnerability %}

For each SAST vulnerability, open the side panel to see a pre-generated fix under the **Remediation** section. For other findings (such as code quality), you can click the **Fix with Bits** button to generate a fix.

From each remediation, you can modify the fix suggested by Bits AI directly in the session view, or click **Create a pull request** to apply the remediation back to your source code repository.

### Fix multiple vulnerabilities in batches with campaigns{% #fix-multiple-vulnerabilities-in-batches-with-campaigns %}

Datadog SAST saves time by replacing the filing of individual pull requests to fix vulnerabilities with bulk-remediation **campaigns** that can fix multiple vulnerabilities at once.

A **campaign** is how teams in Datadog operationalize remediation at scale. Creating a campaign tells Datadog to generate remediations for a certain subset of vulnerabilities in your codebase. Each campaign can also automatically create pull requests to apply fixes for all vulnerabilities in the scope of the campaign.

A campaign defines the following:

| Section                 | Description                                 | Options                                                                                                                                                                                                                                                                                            |
| ----------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Repositories**        | Define which repo(s) and paths to scan      | - Set the GitHub repo URL.- Use **Paths** to limit rule scanning to certain directories or files.                                                                                                                                                                                                  |
| **Rule**                | Choose which SAST rule to apply             | - Select a rule from the dropdown.- View description, code example, and number of matches.- Click **Show More** to see remediation steps.                                                                                                                                                          |
| **Session Management**  | Controls how PRs are grouped and submitted  | - **Create one PR per**:â¢ `Repository`: One PR for all findings in the repoâ¢ `File`: One PR per file with findingsâ¢ `Finding`: One PR per finding (most granular)- **Allow [n] open PRs at a time**: Prevents too many PRs at once- **Limit [n] findings per PR**: Prevents creating too-large PRs |
| **Custom Instructions** | Customizes how the AI proposes remediations | - **Custom Instructions**: Guide the AI on how to tweak fixes (for example, `Update CHANGELOG.md with a summary of changes`, `Start all PR titles with [autofix]`).                                                                                                                                |

#### Campaign in progress{% #campaign-in-progress %}

After you click **Create Campaign**, [Bits AI Dev Agent](https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent) does the following:

1. Loads SAST findings for the selected repo(s), path(s), and rule.
1. Generates patches for each group of findings.
1. Creates PRs according to your session rules. **Note**: Automatic PR creation is *opt-in* through [Settings](https://app.datadoghq.com/code/settings).
1. Lets you review, edit, and merge fixes by interacting directly with the Agent.

The campaign page shows real findings that Bits AI is actively remediating and how many have been remediated or are pending so your security and development teams can track progress made toward remediating vulnerabilities.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/static_analysis/campaigner-hero-image.125faebd3695c46c7cf75148a58c4a31.png?auto=format"
   alt="Campaigns page in Bits AI Dev Agent" /%}



You can click a session to view the code changes in more detail and chat with the [Bits AI Dev Agent](https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent) to ask for changes.

#### Session details{% #session-details %}

A remediation session shows the full lifecycle of an AI-generated fix. It includes the original security finding, a proposed code change, an explanation of how and why the AI made the fix, and if enabled, CI results from applying the patch.

Session details make each remediation transparent, reviewable, and auditable, helping you safely adopt AI in your secure development workflow.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/static_analysis/single-session-sql-injection-fix-light-png.f475a05b24289a8722d0eb0578d183a3.png?auto=format"
   alt="An image of a concluded session with Bits AI Dev Agent where remediations have been generated" /%}

Session details include the following:

- Header: Identifies the campaign, time of session creation, and affected branch, file, or PR.
- Title: Summarizes the remediation goal based on the vulnerability being fixed.
- Session metadata: Indicates whether the session is a part of a campaign, the AI model used, and related PR metadata.
- Right panel:
  - Suggested code change: Displays a diff of the vulnerable code and the AI-generated patch.
  - **Create/View Pull Request**: Creates a GitHub PR to apply the remediation, or opens an existing linked GitHub PR for you to review or merge the proposed changes.
- Left panel displays the chat message history, for example:
  - Prompt for remediation: Asks for remediation(s) and explains the triggered rule, the security risk, and why the original code is unsafe.
  - Task list: Shows exactly how the AI read the code, understood the context, chose its approach, and applied the fix. This is helpful for auditability, compliance, and trust. You can confirm that the AI isn't rewriting code blindly, but applying defensible and explainable patterns.
  - CI logs from GitHub: Describes whether the AI-generated patch breaks anything downstream, and includes full error logs. This helps you validate that a fix is not only secure but also safe to deploy, without needing to leave the platform.
  - Summary: Recaps the impact of the fix and provides next steps or guidance if tests failed or PR needs to be rebased.
  - **Bits AI chat field**: Lets you interactively refine the fix or ask the AI follow-up questions. This makes remediation collaborative and tunable, giving security engineers and developers control without needing to write the patch themselves.

## Further reading{% #further-reading %}

- [Log processing pipelines](https://docs.datadoghq.com/logs/processing/pipelines)
- [Using LLMs to filter out false positives from static code analysis](https://www.datadoghq.com/blog/using-llms-to-filter-out-false-positives)
