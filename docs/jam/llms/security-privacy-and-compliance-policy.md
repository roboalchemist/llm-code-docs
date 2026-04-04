# Source: https://jam.dev/docs/company/security-privacy-and-compliance-policy.md

# Security, Privacy and Compliance Policy

Jam’s data privacy and security practices adhere to rigorous enterprise standards. Our infrastructure, data policies and internal corporate processes have been run through extensive security tests by third-party auditors.&#x20;

Our security policies are supported by quarterly vulnerability tests, and annual exercises as dictated by SOC 2 Type 2 requirements.

Read more about Jam's security practices and compliance measures below.

## Privacy & Data Protection

### Where are Jam recordings stored?

Jam stores all recordings with Google Cloud Platform. Today, we are not able to redirect Jams to your chosen storage solution.

### Can we choose when Jam recordings are to be deleted?

Yes, Jam customers can specify a data deletion schedule for their workspace. Please contact us to implement your chosen schedule.

### Who has access to Jam recordings?

Jam provides [Access Controls](https://jam.dev/docs/administration/access-controls) so that you can control who can view your Jams. You can set global permissions so that only people with verified access to an email address with your company domain can view Jams. You can further narrow access to specific email addresses on a per Jam basis.

### How does Jam gather consent from end customers?

An end customer must proactively choose to begin recording and to submit their recording before any visual and browser data is stored by Jam. Both steps are forms of consent that the end user can decline at their discretion.

### How does Jam minimize the amount of sensitive information it collects?

Jam gathers visual screen recordings and data directly from the user’s browser. We also collect audio if the user opts into recording their voice alongside their screen. Jam has put protective measures in place to ensure users do not share or expose unnecessary sensitive data. Please refer to the following resources for deeper details:

* **Jam obfuscates sensitive data from network requests -** [learn more](https://jam.dev/docs/debug-a-jam/devtools/secrets)
* **Jam automatically blurs screen recordings** - [learn more](https://jam.dev/docs/jam-for-customer-support/advanced-data-protection-for-customer-support-jams-auto-blur)

### Can we tailor the automatic blurring feature to our business?

Yes, Jam gives our customers control over what data elements will be automatically blurred during recordings. [In this guide](https://jam.dev/docs/jam-for-customer-support/advanced-data-protection-for-customer-support-jams-auto-blur), we outline the data elements that are included in Jam’s default settings. It also includes instructions for how to choose data elements based on your own product context.

## Infrastructure & Data Management

### Infrastructure

Jam uses Google Cloud Platform as the cloud provider to store data. For GCP, we use the Central US region. Jam uses Cloudflare for CDN. The Chrome extension is distributed through Google’s Chrome app store.

### Does Jam backup data?

Yes. Our data retention period depends on the frequency of the snapshots.

#### Frequency Retention period

| Frequency | Retention period |
| --------- | ---------------- |
| Hourly    | 2 days           |
| Daily     | 7 days           |
| Weekly    | 4 weeks          |
| Monthly   | 12 months        |

## Security Measures

### Encryption

Yes. Data is encrypted at rest (AES-256) and in transit (HTTPS/TLS).

### Securing our cloud environment

Access to our cloud services, source code, third-party tools etc. are secured with 2FA.

### What are Jam’s practices for reacting to security incidents?

We take security very seriously. We review security issues as soon as we learn about them. We let our users know if they are affected by any security incident.

### Has Jam deployed firewalls and intrusion detection and prevention systems in your environment?

Jam uses Cloudflare as a mechanism to prevent attacks on our environment, as well as have firewalls and controls within our GCP project. However it does not have an IDS or IPS running in our production network because the network is fully operated by GCP.

### How often is Jam performing vulnerability scans and penetration tests on your own infrastructure?

Jam is using GitHub to store our source code. GitHub provides a vulnerability feed of issues that become known in third party software dependencies used by our source code.

## Compliance & Certifications

### SOC 2 Type 2 Compliance

Jam is SOC 2 Type 2 compliant. We are happy to share our SOC 2 Type 2 report with qualified customers. You can email <security@jam.dev> to request the report.

## Contact

### Who should I reach out to if I have a security question about Jam?

If you notice a security issue or have a question or concern, you can reach out to us at <security@jam.dev> and we'll respond as soon as possible. Currently, Jam does not have a bug bounty program.

<br>
