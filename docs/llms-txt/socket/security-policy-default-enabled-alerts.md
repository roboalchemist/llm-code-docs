# Source: https://docs.socket.dev/docs/security-policy-default-enabled-alerts.md

# Security Policy (Default Enabled Alerts)

These are the default set of Enabled Alerts

## Introduction

Socket's security policy is designed to help organizations manage and mitigate supply chain risks by automatically blocking or warning about potential threats. By default, Socket enables a set of alerts that are critical to maintaining the integrity and security of your codebase. These default alerts are carefully selected to minimize noise and ensure that only significant issues are brought to attention.

Customize alert actions in your organization’s security policy to block, monitor, warn, or ignore each alert type or set the action back to inherit from the default policy. Custom settings will override the default policy setting and stay in effect until you change them or remove all custom settings via the `Remove Custom Settings` button to the top right.

<Image align="center" src="https://files.readme.io/7963271f67e2572935848208c6a5d48ac79aafcbf27db57ff1dca70c8aaf579a-Screenshot_2024-08-27_at_4.22.53_PM.png" />

## Default Security Policy

Socket, by default, will show alerts that are likely not noise.

**Recommended for most teams**, balancing robust security measures with minimized disruption to developer workflows.

### Key Features:

* **Defend against supply chain risks**: Monitor and alert on potential risks to protect your projects from various supply chain attacks.
* **Block malicious dependencies**: Automatically block the use of known malicious dependencies to prevent them from entering your codebase.
* **Warn about critical CVEs, typosquats, protestware**: Provide warnings for critical vulnerabilities (CVEs), potential typosquatting attempts, and packages containing protestware, ensuring that developers are informed about potential threats without halting the development process.

### Default Security Policy Alert Actions

The table below outlines the alert types and their corresponding actions under the Default security policy:

| Alert Type                                                                      | Default |
| ------------------------------------------------------------------------------- | ------- |
| **[Known Malware](https://socket.dev/alerts/malware)**                          | 🚫      |
| **[Critical CVE](https://socket.dev/alerts/criticalCVE)**                       | ❗       |
| **[Possible Typosquat Attack](https://socket.dev/alerts/didYouMean)**           | ❗       |
| **[Protestware/Troll Package](https://socket.dev/alerts/troll)**                | ❗       |
| **[Git Dependency](https://socket.dev/alerts/gitDependency)**                   | ❗       |
| **[GitHub Dependency](https://socket.dev/alerts/gitHubDependency)**             | ❗       |
| **[HTTP Dependency](https://socket.dev/alerts/httpDependency)**                 | ❗       |
| **[Obfuscated File](https://socket.dev/alerts/obfuscatedFile)**                 | ❗       |
| **[High CVE](https://socket.dev/alerts/cve)**                                   | 👁️     |
| **[Medium CVE](https://socket.dev/alerts/mediumCVE)**                           | 👁️     |
| **[Low CVE](https://socket.dev/alerts/mildCVE)**                                | 👁️     |
| **[Telemetry](https://socket.dev/alerts/telemetry)**                            | 👁️     |
| **[Unpublished Package](https://socket.dev/alerts/unpublished)**                | 👁️     |
| **[Unstable Ownership](https://socket.dev/alerts/unstableOwnership)**           | 👁️     |
| **[Unpopular Package](https://socket.dev/alerts/unpopularPackage)**             | 👁️     |
| **[Deprecated](https://socket.dev/alerts/deprecated)**                          | 👁️     |
| **[Shrinkwrap](https://socket.dev/alerts/shrinkwrap)**                          | 👁️     |
| **[AI-Detected Potential Malware](https://socket.dev/alerts/gptMalware)**       | ➖       |
| **[Install Scripts](https://socket.dev/alerts/installScripts)**                 | ➖       |
| **[Unmaintained](https://socket.dev/alerts/unmaintained)**                      | ➖       |
| **[Potential Vulnerability](https://socket.dev/alerts/potentialVulnerability)** | ➖       |

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

*Note: all other supported alert types are set to be ignored in the three new policies and will have to be enabled explicitly.*

### Customizing Security Policies

Organizations can adjust these default settings to meet their specific needs using the Socket dashboard. For more granular per-repository settings, the `socket.yml` file can be used to customize the security policies.

See: [socket.yml](https://docs.socket.dev/docs/socket-yml).

### Conclusion

Maintaining the default set of enabled alerts ensures your codebase is protected against common and critical security risks. Customizing the alerts should be done with caution to avoid missing potential threats. For detailed instructions on customizing your security policies and managing alerts, contact the Socket Customer Success team.

For more information, visit the [Socket Documentation](https://docs.socket.dev/).