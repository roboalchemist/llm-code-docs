# Source: https://docs.socket.dev/docs/vanta-integration.md

# Vanta integration

This guide explains how to integrate Socket with Vanta to enhance your organization’s security and compliance efforts.

## Introduction

### What is Vanta?

Vanta is a platform that automates security monitoring and compliance for businesses, helping them to prepare for audits and maintain certifications such as SOC 2, ISO 27001, HIPAA, and more. It simplifies the process of proving your organization's security posture to customers and auditors.

### How Socket Helps with SOC 2 and Other Certifications

Socket provides a developer-first security platform that prevents vulnerable and malicious open source dependencies from infiltrating your software supply chain. It assists with:

* **SOC 2 Compliance**: By ensuring that all dependencies are secure, Socket supports the security and availability principles required for SOC 2.
* **ISO 27001**: Helps maintain the integrity and confidentiality of information by managing software vulnerabilities.
* **HIPAA**: Ensures that software dependencies do not introduce risks to sensitive health information.

### Why Is an Integration Between the Tools Beneficial?

Integrating Socket with Vanta enhances your organization's security and compliance efforts by:

* Automatically synchronizing security alerts from Socket to Vanta, ensuring all potential issues are tracked in one place.
* Simplifying the audit process by maintaining a consistent and comprehensive view of your security posture.
* Reducing manual effort in managing compliance tasks, allowing your team to focus on development and other high-priority activities.

## How to Enable It

### Integrate from the Settings Page

1. **Navigate to the Settings Page**: Go to the [Socket Dashboard](https://socket.dev/dashboard/).
2. **Set Up the Integration**:
   * Find the Vanta integration option under the "Integrations" section.
   * Follow the prompts to authorize the connection between Socket and Vanta.
3. **Synchronization**:
   * Once the link is set up, all Organization Alerts will be synchronized to your Vanta instance.
   * Alerts will respect your [Security Policy](https://docs.socket.dev/docs/enabled-issues), ensuring only relevant issues are reported.

## How the Integration Works

1. **Authorization via OAuth**\
   To enable the integration, you will connect your Vanta instance to Socket using OAuth. Upon completion, Socket will store a refresh token in your organization settings for ongoing communication with Vanta.

`⚠️ Important Caveat: Vanta often revokes these tokens. Tokens may be invalidated due to:`

* No new scan results within a 24-hour window (including weekends),
* High alert volume,
* Other undocumented reasons.

If this happens, the integration may appear broken. The recommended fix is to `re-authorize` the integration via the Socket dashboard.

2. **What Gets Synced**
   * Alerts: Whenever Socket scans the default branch (triggered via GitHub webhook events, not the GitHub API), it stores all alerts internally and sends the current snapshot to Vanta every 45 minutes.
   * Membership Info: Socket also sends organization membership data and repository metadata from the Socket database (not from GitHub APIs) to keep Vanta aligned.
   * Alerts are sent based on your Security Policy ( `Block` , `Warn`, and `Monitor`). Alerts marked as `Ignore` in Socket will not be synced to Vanta.

## Next Steps

* **Enjoy spending less time manually syncing findings into Vanta!**: From now on, Socket and Vanta dashboards will automatically be synchronized and alerts marked as `Ignore` in Socket will not synchronize over to Vanta.
* **Review Security Policies**: Make sure your [Security Policy](https://docs.socket.dev/docs/enabled-issues)  is up-to-date to avoid unnecessary alerts and ensure compliance with the latest standards.
* **Prepare for Audits**: Use the integrated system to streamline your audit preparations, ensuring all security measures are documented and up-to-date.

By integrating Socket with Vanta, you can enhance your security posture, streamline compliance processes, and maintain a clear and consistent view of your software supply chain's security.