# Source: https://docs.socket.dev/docs/organization-alerts.md

# Organization Alerts

## Introduction

Socket's Organizational Alerts feature is designed to provide comprehensive security monitoring and alerting across all repositories within an organization. This powerful tool helps you identify and address potential security risks in real-time, ensuring your software supply chain remains secure.

## Overview of Organizational Alerts

Organizational Alerts in Socket provide a centralized view of security alerts detected across your organization's repositories. This feature is designed to help DevSecOps teams prioritize and manage security concerns efficiently, ensuring that critical vulnerabilities and risks are addressed promptly. This documentation will guide you through the features and functionalities of Organizational Alerts and how they can be leveraged to maintain a secure codebase.

<Image align="center" src="https://files.readme.io/10e058e23f6e31d9415b0853058156083b17191d160de7d9c4f198f288f20a76-Screenshot_2025-06-30_at_10.25.47_PM.png" />

## Accessing Organizational Alerts

To access Organizational Alerts, navigate to the 'Alerts' section in the Socket dashboard. Here, you will find a summary of the alerts detected across all repositories, categorized by severity.

## Features of Organizational Alerts

### Centralized Alert Management

Organizational Alerts aggregate security alerts from all repositories within your organization, providing a comprehensive overview of potential risks. This centralized view helps streamline the process of identifying and addressing security issues.

### [Triage and Prioritization](https://docs.socket.dev/docs/alert-actions-and-triage-functionality)

The alerts are categorized by severity—Critical, High, Medium, and Low—enabling your team to prioritize response efforts effectively. Critical alerts, such as known malware or critical CVEs, are highlighted to ensure immediate attention.

### Interactive Dashboard

The interactive dashboard displays a visual representation of alerts, making it easier to understand the distribution and severity of security issues across your repositories. You can filter alerts by repository, ecosystem, severity, category, type, and dependency to focus on specific areas of concern.

## How Organizational Alerts Help DevSecOps Teams

### Prioritizing Critical Issues

The ability to filter and categorize alerts by severity allows DevSecOps teams to focus on addressing the most critical security concerns first, such as known malware and critical CVEs. This ensures that the most significant risks are mitigated promptly.

### Enhancing Security Posture

By utilizing the Block action for high-confidence and severe issues, organizations can prevent potentially harmful code from being merged into the codebase. This proactive approach helps maintain a robust security posture.

### Streamlining Alert Management

The interactive dashboard and comprehensive alert management features streamline the process of identifying, triaging, and addressing security issues. This helps teams stay organized and ensures that no critical alerts are overlooked.

## Visual Representation of Organizational Alerts

<Image align="center" src="https://files.readme.io/dbca618d9f482cc8118e7bd03a27f657f530c24995479a6f2688d3f13337b88a-Screenshot_2025-07-01_at_12.38.35_AM.png" />

The dashboard provides a visual representation of the alerts detected within the default branch of your organization's repositories. You can customize your Security Policy to specify which alert types your organization should be notified about. Ignored alert types are hidden by default from the alert table view.

### Analytics

Socket's Analytics view provides high-level visibility into the state of your organization's software supply chain. It is especially useful for Security and Engineering leaders to understand trends, triage volume, and overall risk posture over time.

<Image align="center" src="https://files.readme.io/5c123f1746f29766b532c3f1dc1c97afb6fa06f835027d2741ecd0ec693d0bd2-Screenshot_2025-07-01_at_12.48.29_AM.png" />

This data helps you track improvement, spot regressions, and better allocate security and developer resources.

## Populating Organizational Alerts

Organizational Alerts are an essential feature for monitoring the security and integrity of your projects. When enabling Socket, it is important to note that scans for all repositories do not occur immediately. Socket currently does not initiate a scan until there is a commit or a pull request (PR) containing manifest files that Socket supports. For instance, if there is a PR where files like `package-lock.json`, `requirements.txt`, or other supported manifest files are present, a scan will automatically be performed.

To have results show up for the repositories, you need to make a new commit or PR with any supported manifest files. This action will trigger scans to be populated for the repositories.

Currently, Org Alerts are not populated unless a PR is merged into the default branch, which is configured in GitHub. Once this happens, it can take 15 minutes to an hour for the Org Alerts to populate.

*Please note the following conditions under which Organizational Alerts are populated:*

#### PR Merges into the Default Branch

Organizational Alerts will only populate once a pull request (PR) has been merged into the default branch. This ensures that alerts are relevant to the current state of your codebase.

#### Full Scan API Usage

Alternatively, Organizational Alerts can be populated using the Full Scan API. For this to happen, the scan must be marked with the parameters `make_default_branch` and `set_as_pending_head`. This approach allows for more immediate and comprehensive scanning results to be reflected in your Organizational Alerts.

By adhering to these conditions, you can ensure that your Organizational Alerts provide the most accurate and up-to-date information regarding the security status of your organization’s projects.

## Severity Categories

Organizational [Alerts](https://docs.socket.dev/docs/package-issues) are categorized into four severity levels to help you prioritize response efforts:

* **Critical**: Immediate action required to prevent significant security risks.
* **High**: Prompt attention required for potential serious issues.
* **Medium**: Regular monitoring recommended for known issues.
* **Low**: Informational alerts that do not require immediate action.

## Managing Alerts

Socket provides various [alert actions ](https://docs.socket.dev/docs/security-policy-defaults)to manage alerts effectively. These actions include: Block, Warn, Monitor, and Ignore.

* **Block 🚫**: Immediately block the package from use. Critical alerts like known malware and potential typo squats should be blocked to prevent security breaches.
* **Warn ⚠️**: Notify the team to review the package. High-risk alerts like telemetry and protestware are flagged for review.
* **Monitor 👁️**: Track the package over time without immediate action. Medium risk alerts such as environment variable access and filesystem access are monitored for changes.
* **Ignore ❌**: Ignore the alert if it is deemed low priority or informational.

## Example Alerts and Actions

These actions allow you to tailor the handling of each alert type according to its severity and impact on your project.

### Block 🚫

| **Alert**            | **Category**      | **Severity** | **Action**                          | **Link**                                             |
| -------------------- | ----------------- | ------------ | ----------------------------------- | ---------------------------------------------------- |
| Known Malware        | Supply Chain Risk | Critical     | Block immediately. Notify the team. | [Learn more](https://socket.dev/npm/issue/malware)   |
| Potential Typo Squat | Supply Chain Risk | Critical     | Verify and block. Notify the team.  | [Learn more](https://socket.dev/npm/issue/typosquat) |

### Warn ⚠️

| **Alert**   | **Category**      | **Severity** | **Action**                             | **Link**                                               |
| ----------- | ----------------- | ------------ | -------------------------------------- | ------------------------------------------------------ |
| Telemetry   | Supply Chain Risk | High         | Review data tracking. Notify the team. | [Learn more](https://socket.dev/npm/issue/telemetry)   |
| Protestware | Supply Chain Risk | High         | Examine and replace if necessary.      | [Learn more](https://socket.dev/npm/issue/protestware) |

### Monitor 👁️

| **Alert**                   | **Category**      | **Severity** | **Action**                     | **Link**                                                     |
| --------------------------- | ----------------- | ------------ | ------------------------------ | ------------------------------------------------------------ |
| Environment Variable Access | Supply Chain Risk | Medium       | Monitor and ensure safe usage. | [Learn more](https://socket.dev/npm/issue/env-access)        |
| Filesystem Access           | Supply Chain Risk | Medium       | Monitor for unusual activity.  | [Learn more](https://socket.dev/npm/issue/filesystem-access) |

### Ignore ❌

| **Alert**           | **Category**      | **Severity** | **Action**                     | **Link**                                                       |
| ------------------- | ----------------- | ------------ | ------------------------------ | -------------------------------------------------------------- |
| Non-existent Author | Supply Chain Risk | Medium       | Investigate and monitor usage. | [Learn more](https://socket.dev/npm/issue/non-existent-author) |
| Minified Code       | Quality           | Low          | Review source if possible.     | [Learn more](https://socket.dev/npm/issue/minified-code)       |

## Customizing Security Policies

Organizations can customize their [security policies](https://docs.socket.dev/docs/security-policy-default-enabled-alerts) to tailor alert actions according to their specific needs. This can be done through the dashboard for granular control at the repository level.

### Using the Dashboard

To customize your security policy using the dashboard:

1. Navigate to the 'Security Policy' section.
2. Select the alerts you wish to modify.
3. Choose the desired action (Block, Warn, Monitor, Ignore).

## Example of a Socket Dependency Overview Comment

This is an example of a Socket Dependency Overview comment. The dependency overview comments appear where there is either a new dependency, an updated dependency that adds new capabilities, or there are removed dependencies. This type of comment is an informational type to provide additional insight into what your dependencies are adding in. For example, you might want to look at why a simple parser might be adding in network or shell capabilities when you aren't expecting it. You can follow the links for the capabilities and we try to highlight right in the code where this detection was. Socket's goal is to do the scanning and evaluation of the packages for you so that you don't need to read every line of code for direct or transitive dependencies.

<Image align="center" src="https://files.readme.io/606b7ca0f7bcca09fb234859d399617e6faa70875ab49bc7e6e9387af72a152f-Screenshot_2025-07-01_at_12.39.53_AM.png" />

<Image align="center" src="https://files.readme.io/82adc2c-Screenshot_2024-07-08_at_6.23.56_PM.png" />

## Example of a Socket Security Issue Comment

This screenshot is of a Socket Security Issue comment. When there are items that the Security Team has added to the Warn or Block security policies within Socket it will trigger these types of comments. Warn Alerts will comment on the PR but will not fail the Socket Security: Pull Request Alerts check. Block Alerts will comment on the PR and WILL fail the Socket Github check. If there are branch protection rules configured for the repository that either all checks must pass or specifically the Socket Pull Request Alert then the merge would be blocked. If this branch protection rule is not configured then it is possible to still merge.

<Image align="center" src="https://files.readme.io/12637dd9fd6e8c5158e056ef98096afc0db65eb56864c6337d6cbf7c6d4cb906-Screenshot_2025-07-01_at_12.40.38_AM.png" />

## Conclusion

Socket's [Organizational Alerts](https://socket.dev/blog/enhanced-alert-actions-and-triage-functionality) provide a robust framework for securing your software supply chain. By leveraging the power of real-time alerts, severity-based categorization, and customizable security policies, you can proactively manage risks and ensure the integrity of your codebase.

For more detailed information, visit the [Socket Blog on Organizational Alerts](https://socket.dev/blog/introducing-organization-alerts).

***

This documentation is designed to help you navigate and utilize Socket's Organizational Alerts effectively. Should you have any further questions or need assistance, please feel free to contact our support team.