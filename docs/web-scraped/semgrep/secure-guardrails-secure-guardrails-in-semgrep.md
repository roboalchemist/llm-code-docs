# Secure guardrails in Semgrep

Source: https://semgrep.dev/docs/secure-guardrails/secure-guardrails-in-semgrep

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Set up and deploy scans- Secure guardrails**On this page- [Secure guardrails](/docs/tags/secure-guardrails)Secure guardrails in Semgrep
Secure guardrails guide **developers** towards fixing security issues in the early stages of development. By deploying secure guardrails, you can:

- Prevent issues from merging into production or default branches. This improves security posture and reduces the growth of the vulnerability backlog.
- Reduce the time and cost to address issues—the earlier a vulnerability is detected, the faster it is to fix.

The deployment of secure guardrails maximizes the impact of early detection by providing **specific** and **actionable** remediation guidance to developers. Customization enables you to set the **amount of alerts** that developers receive.

This document defines secure guardrails and presents an overview of the guardrail deployment process in Semgrep.

***Figure**. Secure guardrails maximize the potential impact of early detection by  providing tailored remediation guidance to developers. (Chart for illustration purposes only.)*

Secure guardrails consist of:

ContentThe content that identifies, explains, and provides remediation guidance for the security issue, such as the Semgrep rule and Semgrep Assistant (AI) remediation guidance.

Semgrep uses **rules**, which are instructions that detect patterns in your code, such as security issues, bugs, and more. Semgrep generates and reports **findings** to you whenever it finds code that matches the patterns defined by rules.

Semgrep rules also include a **message** that guides remediation and provides other metadata about the vulnerability, such as its OWASP category, which are presented to the developer. Further improvements to this guidance are made through Semgrep Assistant.

InterfaceThe developer-native **interface** where the developer can see the content and triage or remediate the finding, such as Visual Studio Code (VS Code), pre-commit on CLI, or GitHub pull request comments. See [all supported interfaces](#support-for-developer-interfaces-pre-build).

***Figure**. Semgrep products provide the content of the guardrail, namely its rules and suggested remediations. The [Semgrep web app](https://semgrep.dev/login) provides the means to configure and deploy guardrails: what rules to deploy as well as where and how to alert developers.*

## Qualities of secure guardrails[​](#qualities-of-secure-guardrails)
### Speed[​](#speed)
Scans must be quick to successfully integrate into developer workflows without slowing them down.

The following table lists the speed of a Semgrep scan in relation to the environment the scan is run in:

InterfaceScope of scanAnalysisTypical speedIDE (per keystroke and on save)Current fileSingle-function, single-fileIn a few secondsCLI on commit (through [`pre-commit`](https://pre-commit.com/))Files staged for commit (cross-function, single-file analysis)Cross-function, single-fileUnder 5 minutesPR or MR commentsAll committed files and changes in the PR or MRCross-function, single-file analysisUnder 5 minutes
### Support for developer interfaces (pre-build)[​](#support-for-developer-interfaces-pre-build)
Guardrails should be able to provide remediation guidance and means to triage findings or give feedback within developer interfaces.

Semgrep supports the following interfaces:

InterfaceSupported providers and appsTriage and remediation actionsIDEs[Visual Studio Code (VS Code)](https://marketplace.visualstudio.com/items?itemName=Semgrep.semgrep)- Receive human-written remediation guidance.
- Ignore or apply a [1-click autofix](/docs/writing-rules/autofix), if it is available, to findings individually.[IntelliJ-based IDEs](https://plugins.jetbrains.com/plugin/22622-semgrep)PR or MR comments[All GitHub plans](/docs/semgrep-appsec-platform/github-pr-comments)- Receive human-written and Semgrep Assistant remediation guidance*; you can customize the confidence level at which the AI leaves a comment.
- Ignore or apply a [1-click autofix](/docs/writing-rules/autofix), if it is available, to findings individually.[All GitLab plans](/docs/semgrep-appsec-platform/gitlab-mr-comments)[All Bitbucket plans](/docs/category/bitbucket-pr-comments)[Azure Devops Cloud](/docs/semgrep-appsec-platform/azure-pr-comments)CLI through `pre-commit`Most terminal emulator apps- Receive human-written remediation guidance.
- Ignore or apply [a 1-click autofix](/docs/writing-rules/autofix), if it is available, to findings individually.
**To receive Assistant guidance, check that your source code manager (SCM) is supported: [list of supported source code managers (SCMs)](/docs/semgrep-assistant/overview#support-and-availability).*

***Figure**. Remediation message provided in VS Code. The message appears when a user hovers over findings, which are marked with squiggly lines. Developers can click the **Quick Fix** button to either ignore the finding or, if the rule provides an autofix, apply the fix.*

***Figure**. A PR comment detecting a hardcoded secret.*

### Customizability[​](#customizability)
Every organization has its own secure coding practices. Customizability ensures that the tool can adapt to the unique needs of an organization.

Semgrep provides customizability through:

- Custom rules - You can create custom rules and deploy them as guardrails. Learn more about Semgrep rule structure in [the next section](#remediation-guidance).
- Assistant Memories - this feature allows you to add and save additional context when Semgrep Assistant provides remediation. For example, you can provide organization-specific public keys, which Semgrep Assistant remembers.

***Figure**. A form on a finding&#x27;s details page where you can enter additional instructions or context.*

### Remediation guidance[​](#remediation-guidance)
Remediation guidance can come in three forms:

- The rule&#x27;s `message`
- AI-generated remediation guidance through Semgrep Assistant
- The rule&#x27;s `fix`

Much of the remediation guidance originates from the rule itself, which is also used to generate Semgrep Assistant&#x27;s advice (if Assistant is enabled). Learning the basic Semgrep rule structure can help you:

- Customize remediation through your organization-specific rules.

Writing your own rules provides you with a means to tailor Semgrep to your organization with or without Assistant.

- Write and deploy guardrails of your own.

The following example illustrates a basic Semgrep rule.

***Figure**. A simple Semgrep rule that illustrates the common fields or keys used to create guardrails. Scroll through the **Rule** pane to view all the fields used to define the rule.*

Click to view a line-by-line explanation of each field in the sample rule.`rules:  # The name of the rule (required):  - id: fix-and-message-demo-copy    # The language of the target code (required):    languages:      - python    # How severe the impact of the finding is (required):    severity: HIGH    # Description and advice that appears in the IDE,    # PR or MR comment, or CLI (required):    message: &gt;-      You&#x27;re using an unsafe function.      Prefer safe_function() if possible.    # The matching logic of the rule (required):    pattern: unsafe_function(...)    # A substitution that resolves the finding (optional).    fix: safe_function(...)    # Metadata is optional but helpful to AI-generated remediation.    metadata:      # A category that describes the rule. Typically security:      category: security      # Confidence of the rule to detect true positives:      confidence: HIGH      # How likely an attacker can exploit the issue:      likelihood: HIGH      # Indicates how much damage a vulnerability can cause:      impact: HIGH      # A sub-type under category. Typically vuln, audit, or secure default:      subcategory:        - vuln`
#### The rule `message`[​](#the-rule-message)
This description explains **why** the finding was generated and outlines **general advice** on resolving the issue. Messages notify developers in all interfaces where you&#x27;ve deployed a guardrail.

#### AI-generated remediation guidance and code suggestions (Semgrep Assistant)[​](#ai-generated-remediation-guidance-and-code-suggestions-semgrep-assistant)
This is a tailored, **step-by-step** outline of what a developer must change to fix the insecure code.
The guidance makes use of the Semgrep rule, AI&#x27;s understanding of code, and a prompt tree that incorporates inputs such as:

- Prior triage decisions
- Custom instructions
- Broader context of the file

***Figure**. AI-generated guidance. Developers are able to commit the suggestion directly.*

info
- Within developer-native interfaces, Semgrep Assistant only appears in PR or MR comments. Assistant guidance does not appear in the IDE or `pre-commit`.
- You can adjust when the guidance is shown to developers based on the level of confidence in the guidance.

#### The rule&#x27;s human-written autofix (`fix`)[​](#the-rules-human-written-autofix-fix)
Sometimes a rule can resolve a finding by replacing, for example, an insecure function with a secure one. These rules make use of Semgrep&#x27;s [autofix](/docs/writing-rules/autofix) feature, which enables rule-writers to provide a human-written fix.

Semgrep Assistant does **not** provide a code snippet suggestion when a human-written fix is provided in the rule.

## Deploy secure guardrails[​](#deploy-secure-guardrails)
### Prerequisites[​](#prerequisites)
#### For AppSec engineers[​](#for-appsec-engineers)

- You have completed a [Semgrep core deployment](/docs/deployment/core-deployment).
- Your [Policies](https://semgrep.dev/orgs/-/policies) page should have at least one rule.

#### For developers[​](#for-developers)

- You must have a Semgrep account.
- You must have joined your Semgrep organization.
- To use Semgrep with your IDE, you must install the extension for the IDE and sign in to Semgrep through the extension.
- To use Semgrep with `pre-commit`, you must install and set up `pre-commit`, then sign in to Semgrep through the CLI.

Rules can be **configured on a per-product, per-interface basis** to notify developers when a finding from that rule is detected. The customization enables you to manage the amount of notifications a developer may receive. The following table describes how to deploy guardrails for each product and interface:

InterfaceSemgrep CodeSemgrep SecretsSemgrep Supply ChainIDETo notify developers of findings from a rule, add the rule to your Policies.Coming soonPR or MR commentsTo notify developers, a rule must be in Comment mode; you can configure your Policies to include only **high confidence, high severity rules**.Developers receive comments about any **reachable vulnerability of high or critical severity.**CLI through `pre-commit`To notify developers of findings from a rule, add the rule to your Policies.Developers are notified of **all** findings by default.

***Figure**. **Policies page &gt; Code tab**. Rules should be in either Comment or Block mode to leave a PR or MR comment.*

## Next steps[​](#next-steps)

- Learn about [secure defaults and their implementation in Semgrep](/docs/secure-guardrails/secure-defaults).
- Create custom rules that you can [deploy as guardrails](/docs/secure-guardrails/custom-guardrails-rules).
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Secure guardrails](/docs/tags/secure-guardrails)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/secure-guardrails/overview.md)Last updated on **Oct 21, 2025**