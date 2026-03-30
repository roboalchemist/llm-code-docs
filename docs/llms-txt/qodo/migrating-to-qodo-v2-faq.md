# Source: https://docs.qodo.ai/qodo-documentation/code-review/migrating-to-qodo-v2/migrating-to-qodo-v2-faq.md

# Migrating to Qodo v2 FAQ

Qodo v2 introduces a unified platform architecture that expands and restructures capabilities previously available in Qodo v1. As the platform evolves across v2.x releases, features may be enhanced, consolidated, or redesigned to support a more scalable and integrated experience.\
\
This guide focuses on feature mappings, deprecations, and required migration guidance for existing functionality. For new capabilities introduced in Qodo 2.x that did not exist in Qodo v1, refer to the [What's New](https://docs.qodo.ai/qodo-documentation/whats-new).

### General

<details>

<summary>Where is Qodo v2 currently available?</summary>

Supported SCM: GitHub.\
Supported Plans: All plans.\
Supported deployment types: Single-tenant, Multi-tenant and On Premises.

</details>

<details>

<summary>What’s changed in Qodo v2?</summary>

Qodo v2 introduces a unified platform architecture. The table below maps current platform capabilities to their equivalents in Qodo v1.

Items are ordered by the most recent update.

| Qodo v2 Feature           | Qodo v1 Equivalent                 | Version | Status | Change Summary                                                                                                                    | Supported SCM | Required Action |
| ------------------------- | ---------------------------------- | ------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| Qodo Rules System         | Best Practices / Custom Compliance | v2.1    | Beta   | The separate review flows have been unified under PR code review, with best practices and compliance handled by the Rules System. | GitHub        | Onboard         |
| Agentic Review Experience | PR-Merge                           | v2.0    | Beta   | Replaced with: `/agentic_review`, `/agent_describe`, `/invoke_reviews`                                                            | GitHub        |                 |

</details>

<details>

<summary>What onboarding is required for Qodo v2, and what does it involve?</summary>

Yes. Migrating to Qodo v2 requires updating your repository configuration to enable the new review commands.\
Onboarding is designed to be incremental and safe. You can test the new review experience alongside your existing configuration before rolling it out across your organization.

The onboarding process includes:

* Updating repository configuration to enable the new review commands
* Optionally testing the new experience manually in pull requests
* Enabling the new configuration on a pilot repository
* Rolling out configuration at the organization level
* Removing previous review commands to prevent duplicate feedback

For detailed, step-by-step instructions, see [Migrating to Qodo v2](https://docs.qodo.ai/qodo-documentation/code-review/migrating-to-qodo-v2).

</details>

<details>

<summary>What Qodo v1 features and functionality have been deprecated?</summary>

| Qodo v1 Feature       | Deprecated in Version | Change Summary                                    |
| --------------------- | --------------------- | ------------------------------------------------- |
| `/improve` command    | v2.1                  | Unified under PR review through the Rules System. |
| `/compliance` command | v2.1                  | Unified under PR review through the Rules System. |

</details>

### Code Review Experience Q\&A

<details>

<summary>Do I need to change my Git workflow?</summary>

No. Qodo remains fully embedded in your pull request workflow. The review experience is enhanced, but your development process does not need to change.

</details>

<details>

<summary>What has improved in the PR review experience in Qodo v2?</summary>

Review feedback is now unified and structured:

* Issues are grouped by priority (e.g., Action Required, Remediation Recommended, Other).
* Findings include clear explanations and direct references to code.
* Reviews include agent-assisted fix prompts.
* Compliance and code suggestions are no longer separate outputs.

</details>

<details>

<summary>What is the primary change between Qodo v1 and Qodo v2?</summary>

In Qodo v2, review is coordinated by a multi-agent system that:

* Uses specialized review agents to evaluate pull requests from multiple perspectives.
* Evaluates changes using repository context, pull request history, and organizational standards.
* Consolidates findings into a single prioritized review.
* Applies organizational standards through the Rule System.

</details>

<details>

<summary>How is feedback structured differently in Qodo v2?</summary>

| Qodo v1                                                  | Qodo v2                                          |
| -------------------------------------------------------- | ------------------------------------------------ |
| Compliance presented as checklist-style outputs.         | Compliance integrated into prioritized findings. |
| Code suggestions appeared as separate advisory comments. | Suggestions integrated into contextual findings. |
| Findings not prioritized.                                | Issues ranked by impact and severity.            |
| Limited explanation of issues                            | Clear reasoning and resolution guidance provided |

</details>

<details>

<summary>Will reviews look different in my pull requests?</summary>

Yes. In Qodo v2 you will notice:

* No separate Compliance or Code Suggestions sections.
* A more coordinated and prioritized review flow.
* Clearer explanations tied directly to code.
* Emoji acknowledgment (👀) when invoking agent commands.

</details>

### Rule System Q\&A

<details>

<summary>What is the Rule System?</summary>

The Rule System is a core component of the Qodo v2 review experience that:

* Captures your organization’s standards.
* Applies them consistently during pull request reviews.
* Surfaces findings as structured rule violations.

When rules are not supported in a given environment, Qodo uses Qodo v1 review logic.

</details>

<details>

<summary>How can I generate additional suggested rules from past pull request discussions?</summary>

Qodo can analyze historical pull request discussions in a repository to identify recurring review patterns and generate additional suggested rules.

To trigger this analysis manually, add the following command to a pull request comment in any repository you want Qodo to analyze:

```
/scan_repo_discussions
```

This command scans prior pull request discussions to detect new patterns and expand rule coverage. After triggering the command, return to the Qodo portal. Within 5–10 minutes, newly generated rule suggestions should appear for review.

Rule discovery is currently in Beta. Automatic, continuous discovery will be available in a future release.

</details>
