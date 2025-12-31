# Source: https://jam.dev/docs/company/security-privacy-and-compliance-policy.md

# Security, Privacy and Compliance Policy

Jam’s data privacy and security practices adhere to rigorous enterprise standards. Our infrastructure, data policies and internal corporate processes have been run through extensive security tests by third-party auditors.&#x20;

Our security policies are supported by quarterly vulnerability tests, and annual exercises as dictated by SOC 2 Type II requirements.

Read more about Jam's security practices and compliance measures below.

## SOC 2 Type II Compliance

Jam is SOC 2 Type II compliant. We are happy to share our SOC 2 Type 2 report with qualified customers. You can email <security@jam.dev> to request the report.

## Infrastructure

Jam uses Google Cloud Platform as the cloud provider to store data. For GCP, we use the Central US region. Jam uses Cloudflare for CDN. The Chrome extension is distributed through Google’s Chrome app store.

## Does Jam backup data?

Yes. Our data retention period depends on the frequency of the snapshots.

## Frequency Retention period

| Frequency | Retention period |
| --------- | ---------------- |
| Hourly    | 2 days           |
| Daily     | 7 days           |
| Weekly    | 4 weeks          |
| Monthly   | 12 months        |

## Encryption

Yes. Data is encrypted at rest (AES-256) and in transit (HTTPS/TLS).

## Securing our cloud environment

Access to our cloud services, source code, third-party tools etc. are secured with 2FA.

## What are Jam’s practices for reacting to security incidents?

We take security very seriously. We review security issues as soon as we learn about them. We let our users know if they are affected by any security incident.

## Has Jam deployed firewalls and intrusion detection and prevention systems in your environment?

Jam uses Cloudflare as a mechanism to prevent attacks on our environment, as well as have firewalls and controls within our GCP project. However it does not have an IDS or IPS running in our production network because the network is fully operated by GCP.

## How often is Jam performing vulnerability scans and penetration tests on your own infrastructure?

Jam is using GitHub to store our source code. GitHub provides a vulnerability feed of issues that become known in third party software dependencies used by our source code.

## Who should I reach out to if I have a security question about Jam?

If you notice a security issue or have a question or concern, you can reach out to us at <security@jam.dev> and we'll respond as soon as possible. Currently, Jam does not have a bug bounty program.

<br>
