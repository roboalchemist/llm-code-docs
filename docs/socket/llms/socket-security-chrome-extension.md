# Source: https://docs.socket.dev/docs/socket-security-chrome-extension.md

# Guide to Socket Chrome Extension

## Secure Your Supply Chain and Ship with Confidence

The [Socket Security browser extension](https://chromewebstore.google.com/detail/jbcobpbfgkhmjfpjjepkcocalmpkiaop) adds security metrics to your package pages and search results, protecting you from threats in open-source packages before you even install them.

<Callout icon="💡" theme="default">
  ### **Note:** While we call this the “Chrome extension,” it works in most Chromium-based browsers—including Google Chrome, Microsoft Edge, Brave, and others. You can install it from the Chrome Web Store just like you would in Chrome. Firefox is also supported directly.
</Callout>

<Image align="center" src="https://files.readme.io/7dab036-Screenshot_2024-08-14_at_20.33.41.png" />

## Why Use Socket Security?

At Socket, we want to make the web a safer place for developers.

Our completely revamped web extension helps you detect these threats in real-time and identify safe packages directly from your browser. It offers instant security metrics, identifying potential threats such as malware, typosquatting, and vulnerable dependencies.

We have also expanded support beyond npm to include PyPI, Go, and Maven package and search results.

### Example of an NPM Package with Socket Analysis

<Image align="center" src="https://files.readme.io/e358e17-Screenshot_2024-08-14_at_20.35.33.png" />

In this image, we see a package analysis page for the "browser" package version 0.2.6. The extension provides detailed security metrics including Supply Chain Security, Quality, Maintenance, Vulnerabilities, and License scores. It highlights specific issues such as floating dependencies, shell access, and critical dependency issues (e.g., CVEs). The package scores indicate overall risk and potential concerns that users need to address. This detailed insight helps developers make informed decisions about the security and reliability of their dependencies.

### Value to Your Business

* **Early Detection**: Socket can shorten the remediation time by detecting malicious packages hours or days before there is a CVE.
* **Comprehensive Coverage**: Socket uncovers malicious packages that would never be uncovered using SCA (CVE scanner) alone.
* **Continuous Protection**: Socket detects and blocks supply chain attacks before they strike, mitigating the worst consequences.

### Install the Socket GitHub App

Currently, the extension does not support manual scanning of webpages or viewing reports on potential vulnerabilities directly from the extension interface. The primary functionality is to provide real-time security metrics and alerts while browsing package pages. For more detailed analysis and reports, you would need to use the full Socket Security platform.

Want to defend your entire organization against open-source attacks? Install the Socket GitHub app at [Socket GitHub App](https://github.com/apps/socket-security) and get protected today!