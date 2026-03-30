# Source: https://glitchtip.com/documentation/hosted-architecture

Title: GlitchTip

URL Source: https://glitchtip.com/documentation/hosted-architecture

Published Time: Thu, 12 Mar 2026 18:32:31 GMT

Markdown Content:
[Hosted GlitchTip: Architecture & Security Compliance](https://glitchtip.com/documentation/hosted-architecture#hosted-glitchtip-architecture-security-compliance)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

This document outlines the infrastructure, security controls, and data policies for the Hosted GlitchTip SaaS. Our architecture is designed to ensure data residency, transparency, and security, adhering to principles found in HIPAA, SOC II, and ISO 27001 frameworks.

[Core Infrastructure & Third-Party Processors](https://glitchtip.com/documentation/hosted-architecture#core-infrastructure-third-party-processors)
--------------------------------------------------------------------------------------------------------------------------------------------------

Burke Software functions as a data processor. We do not sell or share user data with third parties. We utilize a minimized set of industry-standard sub-processors:

*   Hosting (US): DigitalOcean NYC1 (New York, USA) - [https://app.glitchtip.com](https://app.glitchtip.com/)
*   Hosting (EU): DigitalOcean FRA1 (Frankfurt, Germany) - [https://eu.glitchtip.com](https://eu.glitchtip.com/)
*   Transactional Email: Mailgun (Data residency matches the server region: US or EU)
*   Analytics: Plausible (Privacy-focused, GDPR compliant, no cookies) runs solely on this marketing website [https://glitchtip.com](https://glitchtip.com/) and not on our GlitchTip hosted servers (ex: [https://app.glitchtip.com](https://app.glitchtip.com/))
*   Payments: Stripe (PCI-DSS Service Provider Level 1)

![Image 1](https://glitchtip.com/assets/glitchtip-saas.png)

[Security by Design](https://glitchtip.com/documentation/hosted-architecture#security-by-design)
------------------------------------------------------------------------------------------------

### [Data Isolation and Encryption](https://glitchtip.com/documentation/hosted-architecture#data-isolation-and-encryption)

*   Storage: User data is stored in managed Kubernetes (DOKS) PostgreSQL cluster, using CloudNativePG.
*   Network Isolation: The database cluster is isolated within a Private VPC (Virtual Private Cloud) and is accessible strictly via the Kubernetes cluster’s "Trusted Source" allowlist. It is not accessible via the public internet.
*   Encryption:
    *   In Transit: All data transmission requires TLS 1.2+ (HTTPS).
    *   At Rest: DigitalOcean Volumes Block Storage provides encryption at rest.

*   Secrets Management: Application credentials and keys are managed via Kubernetes Secrets and are never committed to version control.

### [Access Controls](https://glitchtip.com/documentation/hosted-architecture#access-controls)

*   Least Privilege: We operate on a strict principle of least privilege. Access to production infrastructure is restricted to the Principal Engineers at Burke Software.
*   Audit Trails: Infrastructure changes are managed via OpenTofu (Infrastructure as Code). All access requests and infrastructure changes are version-controlled and logged via GitLab.
*   Authentication: Administrative access to hosting environments requires Single Sign On (SSO) and hardware-backed Two-Factor Authentication (2FA/YubiKey).

### [Workstation Security](https://glitchtip.com/documentation/hosted-architecture#workstation-security)

*   Encryption: All employee workstations utilize Full Disk Encryption (e.g., LUKS) to prevent unauthorized data access in the event of theft or loss.
*   Auto-Lock: Workstations are configured to automatically lock after a short period of inactivity.
*   Endpoint Protection: Development machines are kept up-to-date with the latest security patches and utilize local firewall restrictions.

### [Application Security](https://glitchtip.com/documentation/hosted-architecture#application-security)

*   CSP & Headers: GlitchTip utilizes strict Content Security Policy (CSP), HSTS, and Secure Cookies.
*   Independent Rating: Mozilla Observatory rates app.glitchtip.com as "A+". [View Report](https://developer.mozilla.org/en-US/observatory/analyze?host=app.glitchtip.com).
*   Data Retention: Event data is automatically purged after 90 days.
*   Container Security: Docker images are built in isolated GitLab CI pipelines and hosted on GitLab Container Registry and [Docker Hub](https://hub.docker.com/r/glitchtip/glitchtip)).

[Disaster Recovery & Availability](https://glitchtip.com/documentation/hosted-architecture#disaster-recovery-availability)
--------------------------------------------------------------------------------------------------------------------------

Hosted GlitchTip relies on DigitalOcean’s Managed Kubernetes and Managed PostgreSQL for high availability.

*   Redundancy: Individual services (Kubernetes Pods) and Database Clusters are configured to self-heal.
*   Failover: In the event of a service interruption, our architecture ensures that the GlitchTip ingestion API fails closed; service interruptions on GlitchTip will not disrupt your application's core functionality.
*   Backups: Database snapshots are taken daily and retained for 7 days to ensure Recovery Point Objective (RPO) capabilities.
*   Status: Platform status is available at [DigitalOcean Status](https://status.digitalocean.com/).

### [Incident Response Targets](https://glitchtip.com/documentation/hosted-architecture#incident-response-targets)

While we utilize automated recovery for infrastructure, our internal targets for service-level incidents are:

*   Response Time Objective: 1 hour (during EST business hours) / Best Effort (off-hours).
*   Recovery Time Objective (RTO): 8 hours.

[Security Incident Response Policy](https://glitchtip.com/documentation/hosted-architecture#security-incident-response-policy)
------------------------------------------------------------------------------------------------------------------------------

Burke Software maintains a response policy to address potential security events. This policy is designed to align with the notification requirements of GDPR and HIPAA.

### [1. Detection and Analysis](https://glitchtip.com/documentation/hosted-architecture#1-detection-and-analysis)

Roles are divided into a Technical Lead (investigation/remediation) and a Compliance Lead (communication). A security incident is declared upon discovery by staff or notification via automated security alerts.

### [2. Containment and Eradication](https://glitchtip.com/documentation/hosted-architecture#2-containment-and-eradication)

Upon verification of an incident, the Technical Lead will:

*   Isolate affected Kubernetes Pods or services.
*   Rotate relevant API keys and secrets.
*   Preserve system logs for forensic analysis.

### [3. Notification](https://glitchtip.com/documentation/hosted-architecture#3-notification)

If a breach of customer data is confirmed, Burke Software will notify the affected customer's designated contact without undue delay and no later than 72 hours after discovery.

The notification will include:

*   A description of the breach.
*   The data types involved.
*   Mitigation steps taken.

### [4. Post-Incident Review](https://glitchtip.com/documentation/hosted-architecture#4-post-incident-review)

Following resolution, a root cause analysis is conducted to update policy and prevent recurrence. Documentation is retained for a minimum of six years.

[HIPAA Compliance](https://glitchtip.com/documentation/hosted-architecture#hipaa-compliance)
--------------------------------------------------------------------------------------------

Hosted GlitchTip's security controls (encryption, access logs, backup retention) are designed to align with the HIPAA Security Rule.

Standard Plans: Suitable for organizations that need HIPAA-aligned security controls but do not require a Business Associate Agreement (BAA).

Enterprise Plans: For organizations requiring a signed Business Associate Agreement (BAA), please contact [sales@glitchtip.com](mailto:sales@glitchtip.com).

[Vulnerability Disclosure](https://glitchtip.com/documentation/hosted-architecture#vulnerability-disclosure)
------------------------------------------------------------------------------------------------------------

We are committed to keeping GlitchTip secure.

*   Patch Management: We aim to update server and browser dependencies monthly.
*   Reporting: If you find a security vulnerability, please open a [private issue on GitLab](https://gitlab.com/glitchtip).
*   Note: Please do not report results of automated scanners (e.g., dependency bots) without manual verification. We do not offer a bug bounty program at this time.

For additional security questions or vendor risk assessment inquiries, please email [sales@glitchtip.com](mailto:sales@glitchtip.com).
