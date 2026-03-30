# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter.md

# Phishing Reporter

This section describes in detail how to customize the add-in on the platform and deploy the Phishing Reporter add-in to users in Microsoft 365, Exchange, or Google Workspace platforms. This page also contains how to customize the Diagnostic Tool service and deploy it to the users to monitor the users' Phishing Reporter Outlook Add-in.&#x20;

## Shortcuts

* [Phishing Reporter Customization](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization)
* [Phishing Reporter Deployment](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment)
* [Diagnostic Tool Customization and Deployment](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/diagnostic-tool)

## FAQ

### How does the Phishing Reporter button work?

The Keepnet Phishing Reporter offers two methods for reporting a suspicious email:

1. It calls Keepnet's APIs to report the emails in a [fully encrypted and secure manner.](https://doc.keepnetlabs.com/resources/compliance#data-in-transit)
2. It sends a copy of the reported suspicious email to the SOC team. The "[Email Settings](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization#email-settings)" section provides customization options.

### How does the Phishing Reporter work with SOC Tools?

The Phishing Reporter from Keepnet works seamlessly with SOC tools to streamline and automate phishing analysis and incident response within organizations.

Keepnet offers native integration with several major SOC platforms, including IBM Resilient, IBM QRadar, Splunk Phantom, ArcSight, and SOAR tools. For further details, please contact us directly.

Keepnet also provides robust APIs that allow integration with any SOC tools or services. You can access the API documentation[ here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization) to learn how to utilize the [Incident Responder APIs.](https://api.keepnetlabs.com/docs/index.html)

### How does the Phishing Reporter label or identify reporting of duplicates?

Keepnet's "[cluster view](https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/incident-responder-dashboard#cluster-view)" feature effectively manages duplicates by organizing reported suspicious emails into clusters. This feature works in two primary ways:

1. **Clustering similar reported suspicious emails**: This method groups together emails that are alike in content or characteristics, helping to identify and manage duplicate reports.
2. **Clustering reporters with different reported suspicious emails**: This approach groups reporters based on the types of suspicious emails they report, even if the emails themselves are not identical. This helps in recognizing patterns or trends in the reporting behavior across different users or departments.

### Is there a feedback loop to the users on the result of the investigation?

Yes, Keepnet offers a feedback mechanism to inform users about the outcomes of their reported suspicious emails.

1. This is facilitated through the use of playbooks, which allow you to define the process for providing feedback to employees, the SOC team, or service providers. For instance, you can set up a playbook to send an email to your employees detailing the analysis results of a reported email or alert the SOC team about phishing or malicious activities flagged by your staff.
2. Additionally, Keepnet provides customizable notification templates to streamline the feedback process. These templates can be tailored to meet your organization’s specific needs, ensuring employees are appropriately informed about the status of suspicious emails they report.
3. Security admins can also manage feedback directly from the Incident Response dashboard. Admins can effectively update users on the reported incidents by selecting a notification template and adding a custom message.

### How can we seamlessly integrate with investigative tools to ensure efficient handling/management?

To seamlessly integrate with investigative tools for efficient handling and management of reported incidents, Keepnet offers several approaches:

1. Native Integrations:

[**Contact Keepnet**](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk): Begin by contacting us to learn about the native integrations we offer with various SOC tools and solutions. This will provide direct, built-in connections that facilitate smooth data flow and interactions.

2. Using Email Formats:

**Send Copies of Emails**: One of the simplest methods to integrate third-party solutions is to send a copy of the reported suspicious email in either .eml or .msg format. This can be configured in the "Email Settings" section, as detailed in our documentation[ here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization).

3. API Integration:

**Incident Responder APIs**: Utilize Keepnet's Incident Responder APIs to fetch reported email data. This data can then be processed or analyzed using other incident management systems. Our APIs provide flexibility to adapt and integrate with any external system, enhancing the overall response capability.

These methods ensure that you can tailor the integration process to meet your organization’s specific needs and existing infrastructure, enabling efficient management of phishing incidents.

<br>
