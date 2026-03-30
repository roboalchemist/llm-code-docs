# Source: https://docs.jit.io/docs/require-mfa-for-cloud-providers.md

# Verify that AWS Users Have Enabled MFA

## Jit AWS MFA Checks: Key things to know

* **Brief description:** Continuously scan your AWS environment to ensure all users have MFA enabled. Multi-factor authentication adds an extra layer of security to your organization by ensuring that an attacker in possession of an employee password cannot gain access without a second factor, like a phone app or text. This check ensures that you have MFA enabled for all users.
* **Scanning process**: Jit automatically scans your cloud environment every day and documents users missing MFA in the [Findings Page](https://dash.readme.com/project/jitsecurity/v5.0/docs/jit-findings).
* **How to get started:** Start by integrating Jit with AWS. Then enable MFA Checks by navigating to **ASPM → Security Plans** (left menu) → **Jit Max Security Plan** → **Verify that users of your AWS accounts have enabled MFA**. Hit **Activate**, which will kick off the scanning processes described above
* **AWS integration**: Learn how to set up Jit's integration with AWS [here](https://docs.jit.io/docs/integrating-with-aws).