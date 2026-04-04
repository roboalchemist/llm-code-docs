# Source: https://docs.jit.io/docs/require-mfa-for-scm.md

# Verify that MFA for Your GitHub Organization is Enabled

## Jit GitHub MFA Checks: Key things to know

* **Brief description:** Continuously scan your GitHub environment to ensure all users have MFA enabled. Multi-factor authentication adds an extra layer of security to your organization by ensuring that an attacker in possession of an employee password cannot gain access without a second factor, like a phone app or text.
* **Scanning process:** Jit automatically scans your GitHub environment every day and documents users missing MFA in the [Findings Page](https://dash.readme.com/project/jitsecurity/v5.0/docs/jit-findings).
* **How to get started:** Start by integrating Jit with GitHub. Then enable MFA Checks by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **Verify that MFA for your GitHub organization is enabled**. Hit **Activate**, which will kick off the scanning processes described above.
* **Based on github-mfa-checker:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For CI/CD Security Checks, Jit uses github-mfa-checker, which is maintained by Jit.
* **Source Code Manager support**: MFA checks are currently supported for GitHub.