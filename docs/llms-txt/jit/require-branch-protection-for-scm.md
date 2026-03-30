# Source: https://docs.jit.io/docs/require-branch-protection-for-scm.md

# GitHub Branch Protection Verification

## GitHub Branch Protection Verification: What to know

* **Brief description:** Branch protection is an important GitHub feature that enables you to protect git branches from unauthorized modifications. This security check verifies that GitHub Branch protection is functioning as intended.
* **Scanning process:** Scanning takes place daily and documents findings in the [Backlog page](https://docs.jit.io/v5.0/docs/jit-backlog).
* **How to get started:** Jit IaC Security Scanning can be enabled by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **CI/CD Security**. Locate **Verify that GitHub Branch Protection is properly configured** and select **Activate**.
* **Based on Branch Protection Checker:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For CI/CD Security Checks, Jit uses Branch Protection Checker, which is maintained by Jit.
* **Source Code Manager support**: GitHub Branch Protection Verification is currently supported for GitHub environments.
* Currently Branch Protection only works with classic branch protection and not rulesets.

***

## Configuration

* **Configure Classic Branch Protection** — Select the **"Add classic branch protection rule"** classic branch protection and not the suggested "Add branch ruleset״
* **Required number of approvals** — When enabled, Jit checks if pull requests targeting the default branch require this number of approvals before they can be merged.
* **Require status checks** — When enabled, Jit checks if these status checks must pass before pull requests can be merged to the default branch.

![](https://files.readme.io/375337f-Screen_Shot_2022-09-13_at_14.05.42.png "Screen Shot 2022-09-13 at 14.05.42.png")

> 📘 Recommended configuration
>
> Jit strongly recommends all users use this requirement to validate branch protection rules requiring passage of the *Jit Security* status check before merging.

## Remediation

Jit provides repository-level remediation scripts for the following branch protection misconfigurations:

| Finding type               | What will Jit do?                                     | Why should you fix it?                                                                                                                  |
| :------------------------- | :---------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong number of approvals. | Create a script that updates the number of approvals. | Setting the number of approvals that must pass is necessary to safeguard the quality of your code without creating new security issues. |
| Missing checks.            | Create a script that updates required checks.         | Setting the required checks that must pass is necessary to safeguard the quality of your code without creating new security issues.     |

From the *Branch Protection* GitHub action, download the script and run it from a local environment with the **${github\_username}:${github\_pat}** as an argument, where:

* **${github\_username}** is your GitHub username.
* **${github\_pat}** is your personal access token.

> 📘 Note
>
> The personal access token requires full control permissions on your repositories.