# Source: https://docs.jit.io/docs/github-misconfiguration-detection.md

# CI/CD Security Checks

## Jit CI/CD Security Checks: What to know

* **Brief description:** Scan your GitHub environment to detect misconfigurations that could enable access to your codebase, which can lead to sensitive data exposure, intellectual property theft, and system compromise.
* **Scanning process:** Scanning takes place daily and documents findings in the [Backlog page](https://docs.jit.io/v5.0/docs/jit-backlog).
* **How to get started:** Jit IaC Security Scanning can be enabled by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **CI/CD Security**. Locate **Detect GitHub misconfigurations** and select **Activate**.
* **Based on Legitify and Chainbench:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For CI/CD Security Checks, Jit uses [Legitify](https://github.com/Legit-Labs/legitify) and [Chainbench](https://github.com/aquasecurity/chain-bench), which are maintained by Legit Security and Aqua Security, respectively.
* **Source Code Manager support**: Jit's CI/CD Security Checks are currently supported for GitHub environments.

***

## Checks and Permissions

Legitify and Chain Bench will execute the same checks that they are using in the GitHub Security Plan. The permissions required to run the checks are also identical.

Read more about the checks and permissions in the [GitHub Security Plan Documentation](https://docs.jit.io/docs/github-security-plan).