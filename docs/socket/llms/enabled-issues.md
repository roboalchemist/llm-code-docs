# Source: https://docs.socket.dev/docs/enabled-issues.md

# Customizable Security Policies

Socket has [introduced](https://socket.dev/blog/announcing-new-default-security-policies) three new customizable default security policies to provide greater flexibility in managing dependency security: **Low Noise**, **Default**, and **Higher Noise**.

These policies leverage Socket's four alert actions—**Block**, **Warn**, **Monitor**, and **Ignore**—allowing teams to tailor their security measures according to their specific needs.

![](https://files.readme.io/bf393839223f8057ddd59611be9b5c0e010f69265b08b7d57232a5b30c2e6696-image.png)

## New Security Policies

### 1. Low Noise (Traditional SCA)

* **Focus:** CVEs and malicious dependencies.
* **Actions:**
  * **Block** known malicious dependencies.
  * **Warn** developers about critical CVEs.
  * **Monitor** all other CVEs.

### 2. Default (Recommended for Most Teams)

* **Focus:** Balances robust security with minimized disruption.
* **Actions:**
  * **Block** known malicious dependencies.
  * **Warn** for critical CVEs, potential typosquats, and protestware.
  * **Monitor** a wider range of potential issues.

### 3. Higher Noise (For More Engaged Teams)

* **Focus:** Designed for teams with active security vetting.
* **Actions:**
  * **Block** dependencies with critical CVEs or malicious intent.
  * **Warn** developers for a wider range of potential issues.
  * **Monitor** extensive quality and maintenance issues.

## Policy Configurations

* **Inherit:** Adopts actions specified in the chosen policy (Low Noise, Default, Higher Noise), allowing for automatic updates with policy changes.
* **Explicit Setting:** Remains constant regardless of policy changes, offering tailored customization.

## Detailed Breakdown of Default Alert Actions

The table below outlines the alert types and their corresponding actions under each security policy:

| Alert Type                                                                  | Low Noise (SCA) | Default | Higher Noise |
| --------------------------------------------------------------------------- | --------------- | ------- | ------------ |
| [Known Malware](https://socket.dev/alerts/malware)                          | 🚫              | 🚫      | 🚫           |
| [Critical CVE](https://socket.dev/alerts/criticalCVE)                       | ❗               | ❗       | 🚫           |
| [Git Dependency](https://socket.dev/alerts/gitDependency)                   | ➖               | ❗       | 🚫           |
| [GitHub Dependency](https://socket.dev/alerts/gitHubDependency)             | ➖               | ❗       | 🚫           |
| [HTTP Dependency](https://socket.dev/alerts/httpDependency)                 | ➖               | ❗       | 🚫           |
| [Possible Typosquat Attack](https://socket.dev/alerts/didYouMean)           | ➖               | ❗       | ❗            |
| [Protestware/Troll Package](https://socket.dev/alerts/troll)                | ➖               | ❗       | ❗            |
| [Obfuscated File](https://socket.dev/alerts/obfuscatedFile)                 | ➖               | ❗       | ❗            |
| [Telemetry](https://socket.dev/alerts/telemetry)                            | ➖               | 👁️     | ❗            |
| [Unpublished Package](https://socket.dev/alerts/unpublished)                | ➖               | 👁️     | ❗            |
| [Unpopular Package](https://socket.dev/alerts/unpopularPackage)             | ➖               | 👁️     | ❗            |
| [Unstable Ownership](https://socket.dev/alerts/unstableOwnership)           | ➖               | 👁️     | ❗            |
| [Deprecated](https://socket.dev/alerts/deprecated)                          | ➖               | 👁️     | ❗            |
| [Shrinkwrap](https://socket.dev/alerts/shrinkwrap)                          | ➖               | 👁️     | ❗            |
| [High CVE](https://socket.dev/alerts/cve)                                   | 👁️             | 👁️     | ❗            |
| [Medium CVE](https://socket.dev/alerts/mediumCVE)                           | 👁️             | 👁️     | 👁️          |
| [Low CVE](https://socket.dev/alerts/mildCVE)                                | 👁️             | 👁️     | 👁️          |
| [Install Scripts](https://socket.dev/alerts/installScripts)                 | ➖               | ➖       | 👁️          |
| [Unmaintained](https://socket.dev/alerts/unmaintained)                      | ➖               | ➖       | 👁️          |
| [Potential Vulnerability](https://socket.dev/alerts/potentialVulnerability) | ➖               | ➖       | 👁️          |
| [AI-Detected Potential Malware](https://socket.dev/alerts/gptMalware)       | ➖               | ➖       | 👁️          |

## Alert Actions

| Alert Action | Shows up in Dashboard | Developers see it (e.g., GitHub comment, CLI prints a warning) | Developers blocked (GitHub PR fails, CLI errors) |
| ------------ | --------------------- | -------------------------------------------------------------- | ------------------------------------------------ |
| Block 🚫     | ✅                     | ✅                                                              | ✅                                                |
| Warn ❗       | ✅                     | ✅                                                              | ❌                                                |
| Monitor 👁️  | ✅                     | ❌                                                              | ❌                                                |
| Ignore ➖     | ❌                     | ❌                                                              | ❌                                                |

### Legend

* **Block 🚫**: This action will fail the Socket CI/CD check, preventing the merge or deployment process until the issue is resolved. All related alerts will appear in the dashboard, developers will be notified, and further actions will be blocked.
* **Warn ❗**: This action indicates a potential issue that should be reviewed. It will appear in the dashboard and notify developers through comments or warnings, but it will not block the development process.
* **Monitor 👁️**: This action is used for tracking alerts that require monitoring over time. Alerts will be visible in the dashboard, but no notifications will be sent to developers, and it won't block any processes.
* **Ignore ➖**: This action is set for low-priority alerts or informational notifications. The alerts will not show up in the dashboard, and there will be no notifications or blocks applied.

*Note: all other of our supported alert types are set to be ignored in the three new policies and will have to be enabled explicitly.*

## Changes in the New Default Policy

* **CVE Handling:** Increased visibility for critical to low CVEs.
* **Supply Chain Risks:** Adjusted alert actions to minimize unnecessary disruptions.
* **Quality and Maintenance:** Expanded monitoring for potential issues like deprecated or unmaintained packages.

## Action Steps for Organizations

1. **Review Changes:** Understand how the new default policy affects your organization.
2. **Lock In Preferences:** Set explicit actions for critical alerts to maintain current settings.
3. **Switch Between Policies:** Choose between Low Noise, Default, or Higher Noise based on your team’s needs.

## Transition to New Policies

* **Transition Period (*August 14 - August 28, 2024*):** Organizations can review changes and lock in existing settings if needed.
* **New Policies Take Effect (*August 28, 2024*):** Automatic update to the new default policy, with options to switch between the three new policies.

Socket’s update is designed to enhance security measures while providing flexibility and reducing alert fatigue. If you have any questions or need assistance, please reach out to Socket support.

For more detailed information on the Socket API and alert actions, visit the [Socket Documentation](https://docs.socket.dev/reference/introduction-to-socket-api).