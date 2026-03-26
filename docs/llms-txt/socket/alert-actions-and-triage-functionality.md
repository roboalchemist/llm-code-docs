# Source: https://docs.socket.dev/docs/alert-actions-and-triage-functionality.md

# Alert Actions and Triage Functionality

## Introduction

Welcome to the guide on triaging alerts and configuring security policies with Socket. Efficient alert triaging and robust security policies are crucial for maintaining a secure codebase. In this documentation, we'll explore how to manage alerts effectively, ensuring critical issues are addressed promptly while minimizing alert fatigue.

For a practical demonstration of these features, watch our demo video on Triaging Alerts & Security Policy Configuration. This video provides step-by-step instructions and showcases real-world scenarios to help you get the most out of Socket's alert management capabilities.

<Embed url="https://www.youtube.com/watch?v=kG9DYixhuRc" title="Socket Demo Video Triaging Alerts & Security Policy Configuration" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/kG9DYixhuRc/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=kG9DYixhuRc" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FkG9DYixhuRc%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DkG9DYixhuRc%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FkG9DYixhuRc%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

### Accessing Security Policy

1. Navigate to the '[Security Policy](https://docs.socket.dev/docs/security-policy-default-enabled-alerts)' page from the left-hand menu.
2. On the Security Policy page, you can see various alert types categorized by severity: Block, Warn, Monitor, and Ignore.

### Example Security Policy Configuration

It's important to configure your security policy to meet your organization's specific requirements. Here's an example configuration:

* **Block**: Known Malware, Critical CVE
* **Warn**: Install Scripts, AI Detected Security Risk
* **Monitor**: Network Access, Medium CVE
* **Ignore**: Low CVE, Non-existent Author

## Alert Actions

| Alert Action | Shows up in Dashboard | Developers see it (e.g., GitHub comment, CLI prints a warning) | Developers blocked (GitHub PR fails, CLI errors) |
| ------------ | --------------------- | -------------------------------------------------------------- | ------------------------------------------------ |
| Block        | ✅                     | ✅                                                              | ✅                                                |
| Warn         | ✅                     | ✅                                                              | ❌                                                |
| Monitor      | ✅                     | ❌                                                              | ❌                                                |
| Ignore       | ❌                     | ❌                                                              | ❌                                                |

### Legend

* **🚫 Block**: This action will fail the Socket CI/CD check, preventing the merge or deployment process until the issue is resolved. All related alerts will appear in the dashboard, developers will be notified, and further actions will be blocked.
* **❗ Warn**: This action indicates a potential issue that should be reviewed. It will appear in the dashboard and notify developers through comments or warnings, but it will not block the development process.
* **👁️ Monitor**: This action is used for tracking alerts that require monitoring over time. Alerts will be visible in the dashboard, but no notifications will be sent to developers, and it won't block any processes.
* **➖ Ignore**: This action is set for low-priority alerts or informational notifications. The alerts will not show up in the dashboard, and there will be no notifications or blocks applied.

## Triaging Alerts

### How It Works

When a [security alert](https://docs.socket.dev/docs/organization-alerts) is generated, the initial action is determined by the security policy settings. However, users can override this action for specific alerts to allow for flexible and context-specific responses. This helps reduce alert fatigue while prioritizing the mitigation of critical and high supply chain risks in your codebase.

### Common Use Cases

1. **Dismissing Alerts**:
   * Reasons for dismissal include:
     * A fix has already been started.
     * No bandwidth to fix this.
     * Risk is tolerable to the project.
     * Vulnerable code is not actually used.
   * Example: Dismissing an alert after confirming that the vulnerable code path is not exercised in your application.

2. **Upgrading Alert Severity**:
   * Example: An Install Script alert initially set to Monitor can be elevated to Block after evaluation.

### Steps to Triage an Alert

1. **Identify the Alert**: Locate the alert in the Socket dashboard.
2. **Select an Action**: Choose to Block, Warn, Monitor, or Ignore based on the specific context.

## Conclusion

Effective alert triage and security policy configuration ensure that security issues are addressed promptly and appropriately. By leveraging Socket's capabilities, teams can maintain robust security postures while minimizing disruption to development workflows.

For step-by-step instructions, check out the [quick start guide](https://docs.socket.dev/docs/getting-started).