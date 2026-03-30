# Source: https://docs.socket.dev/docs/threat-feed.md

# Threat Feed

## Introduction

The Socket Threat Feed is an essential feature designed to help you stay informed about the latest malware detected across various open-source packages. This tool allows organizations to identify zero-day software supply chain attacks swiftly, often within seconds of publication. By leveraging the Threat Feed, you can better protect your organization from emerging threats, ensuring your software dependencies remain secure.

### Accessing the Threat Feed

To access the Threat Feed, navigate to the 'Threat Feed' section in the Socket dashboard. This section provides a comprehensive overview of recent threats detected in packages across different ecosystems.

<Image align="center" src="https://files.readme.io/f54623e-Screenshot_2024-06-26_at_12.01.42_PM.png" />

### Understanding the Threat Feed

The Threat Feed displays key information about each detected threat, including:

* **Ecosystem**: The package ecosystem where the threat was detected (e.g., npm, PyPI, Maven).
* **Name**: The name of the package containing the threat.
* **Version**: The specific version of the package where the threat was identified.
* **Artifact**: The artifact type associated with the package (e.g., jar, tar-gz).
* **Threats**: The number of threats detected within the package.
* **Last Threat Detected At**: The timestamp indicating when the threat was last detected.

<Image align="center" src="https://files.readme.io/1a94a3d-Screenshot_2024-06-26_at_12.02.49_PM.png" />

### Threat Details

The Threat Listing section in the Threat Feed provides a detailed breakdown of each threat. By clicking on a specific package, you can view detailed information about the detected threats, including:

* **Threat Description**: An AI-generated description of the threat, providing insights into the nature and potential impact of the issue.
* **Found At**: The timestamp indicating when the threat was first detected.
* **Location**: The specific location within the package where the threat was identified.

This detailed information helps you quickly understand the severity and potential impact of each threat, allowing for timely and effective responses.

### File Explorer

By clicking on a Threat Location, you can view detailed information about the detected threats, including source code:

<Image align="center" src="https://files.readme.io/4e873a5-Screenshot_2024-06-26_at_12.08.15_PM.png" />

### How to Use the Threat Feed

* **Monitor Regularly**: Regularly check the Threat Feed to stay updated on new and emerging threats.
* **Prioritize by Severity**: Use the severity ratings provided to prioritize response efforts. Focus on addressing critical and high-severity threats first.
* **Investigate and Mitigate**: Investigate the details of each detected threat to understand its impact on your software. Take appropriate actions to mitigate the risks, such as updating or replacing affected packages.
* **Update Security Policies**: Based on the threats identified, update your organization's security policies to block, warn, monitor, or ignore specific types of issues.

### Conclusion

The Threat Feed is a powerful tool within the Socket dashboard that enables you to stay ahead of potential security risks in your software supply chain. By regularly monitoring the Threat Feed and taking appropriate actions, you can significantly enhance your organization's security posture.

For more information and best practices on using the Threat Feed, visit our [blog post](https://socket.dev/blog/socket-introduces-new-dashboard-threat-feed) and the [Socket documentation](https://docs.socket.dev/).

### Additional Resources

* **Getting Started with Socket**: [Getting Started](https://docs.socket.dev/docs/getting-started)
* **Socket for GitHub**: [Socket for GitHub](https://docs.socket.dev/docs/socket-for-github)
* **Socket CLI**: [Socket CLI](https://docs.socket.dev/docs/socket-cli)
* **Socket API**: [Socket API](https://docs.socket.dev/reference/introduction-to-socket-api)