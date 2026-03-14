# Source: https://docs.gitguardian.com/platform/security-data-privacy/privacy-mode.md

# Privacy mode

> Explains how to enable privacy mode to control whether raw secret values are stored by GitGuardian.

Protecting sensitive information from unauthorized access is crucial for maintaining data privacy.

The privacy mode enables you to control sensitive information's visibility, preventing unauthorized viewing and aligning with privacy-by-design principles.

### What sensitive information can be obfuscated?

To enable you to use GitGuardian in the best possible conditions, you can choose to show or hide sensitive information at any time from the application.

The obfuscated sensitive information are:

- The secrets themselves with [their multiple matches](../../secrets-detection/secrets-detection-engine/quick_start#detecting-secrets-with-multiples-matches-and-multi-line-secrets).
- The honeytokens and the IP addresses that triggered the honeytokens.

### How to use the privacy mode?

- You can activate or deactivate this mode from the top navigation bar.
- When activated, all the workspace's secrets are obfuscated. It is not possible to deactivate the privacy mode for a single secret.
- This mode is a setting available to every user, regardless of their access level or workspace plan.

![privacy mode](/img/platform/security-data-privacy/privacy-mode.png)

> Please note that its activation does not affect other users in the same workspace.
