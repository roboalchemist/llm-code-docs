# Source: https://docs.startree.ai/getstarted/deployment/security_certifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Security and Compliance

> StarTree Cloud ships with enterprise grade security and has industry-leading certifications such as SOC2 and HIPAA.

At StarTree, we are deeply committed to protecting customer and internal data. This commitment encompasses robust **security measures** for devices, networks, and systems, as well as strict adherence to **regulatory compliance** to ensure data integrity and trust.

## Security

StarTree has implemented features in the following areas to protect data.

### Authentication and Authorization

* Controlled access on all company assets, using the principle of least privilege
* Strong password requirements
* Dedicated customer instances with controlled access

### Encryption

* AES disk encryption for data at rest
* SSL/TLS for data encryption in transit
* Support for encryption options in AWS S3, Google Cloud Storage (GCS), and Amazon Elastic Block Storage (EBS)

### Networking

* Antivirus
* Anti-malware
* Endpoint detection and response (EDR) solutions
* Monitoring, including for file integrity
* Intrusion detection
* Firewalls

### Audit Trails and Data Loss Prevention

* Logging
* Offsite backups
* Regular updates to operating system and application software
* Testing and peer review and approval prior to pushing changes to production

Your real-time analytics data is stored in your Apache Pinot cluster. Depending on your account, this could be running
in StarTree Cloud or in your own cloud account for BYOC deployments.

Configuration details and access management secrets are stored in secure locations. Sensitive data is encrypted.

StarTree Cloud security features include:

* Authentication via OIDC compatible Identity Providers
* Authorization via fine-grained Role Based Access Control (RBAC) policies
* Encryption in transit via TLS 1.2+
* Encryption at rest: All stored data (including logs and metadata) is encrypted using industry-standard AES-256 encryption.

## Compliance

StarTree Cloud has achieved the following certifications:

* SOC2 Type 2
* ISO 27001
* HIPAA readiness

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/getstarted/images/compliance.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=c74d1f270ae5b9d000b47dd20b8cd490" alt="Compliance Pn" width="510" height="360" data-path="getstarted/images/compliance.png" />

For more details, see: [https://startree.ai/security-compliance](https://startree.ai/security-compliance)

Built with [Mintlify](https://mintlify.com).
