# Source: https://docs.anchorbrowser.io/security.md

# Trust & Security

Anchor was engineered from the ground up to be the definitive secure browser solution, empowering developers to deploy to production with confidence. We provide the essential security backbone and advanced capabilities required to build the next generation of browser-based workloads.

This document outlines the security framework of Anchor Browser, covering:

* The reasons why leading enterprises build their solutions on Anchor Browser.
* An overview of our comprehensive Security Architecture.

For a detailed report on our compliance and security posture, please visit the [Anchor Trust Portal](https://trust.anchorbrowser.io/)

## Why Enterprise solutions are built on Anchor Browser

Anchor Browser is the result of deep security expertise from industry veterans, with our team hailing from leaders in cybersecurity such as SentinelOne, Noname Security (acquired by Akamai), and various specialized intelligence units. This collective experience has allowed us to embed robust security capabilities directly into the browser, giving our customers a distinct advantage in enterprise trust, security, and compliance.

### 1. Advanced Features for a More Secure End Solution

* **Complete Browser Isolation & Disposal**: Anchor creates a dedicated, isolated virtual machine (VM) for each browser instance. This VM is permanently terminated and erased upon session completion, ensuring that browsers are never reused and data remnants are eliminated.

* **Official Headful Browser Environments**: As the sole provider of secured and sandboxed environments using the official "Headful" browser operation mode, Anchor runs browsers as they were designed to be run. This ensures maximum stability and leverages the most rigorously tested and penetration-tested browser architecture.

* **Integrated Domain & Network Guardrails**: Anchor implements default network protections to shield customers from malicious websites. We also offer the ability to define granular whitelists of allowed domains, providing precise control over network access at the browser level.

* **Secure Authentication & Credential Management**: With Anchor, customers are never required to store credentials on our platform. Our browsers enable authenticated workflows using secure, encrypted, session-based authentication, eliminating the risks associated with stored credential-based logins.

* **Strict Tenant Isolation**: Anchor enforces rigorous logical isolation between all tenants. This architectural constraint guarantees the integrity and confidentiality of each customer's data.

* **Secure Peer-to-Peer File Transfers**: Secure Peer-to-Peer File Transfers: Uniquely, Anchor facilitates secure file downloads through a peer-to-peer mechanism. File downloads initiated in the browser are transferred directly to the customer's environment, meaning no file artifacts are ever created or stored on Anchor's infrastructure.

### 2. A Secure-by-Design Architecture

Anchor is built on a secure-by-design methodology. This principle ensures that the default configuration is always the most secure, significantly reducing the risk of misconfiguration errors and providing a foundation of trust from the moment you start.

### 3. Shared Responsibility Model

Our shared responsibility model clearly defines the security obligations of both Anchor and our customers. This well defined ownership perimeter approach ensures that all aspects of security are managed effectively, from the underlying infrastructure we secure to the applications you build on top of it.

### 4. Vetted and Audited Supply Chain

We maintain a rigorous security review and auditing process for our entire supply chain. Every component and third-party vendor is scrutinized to ensure they meet our high security standards, protecting our platform and our customers from upstream vulnerabilities.

## Product Architecture & Security Design

### Critical Security Controls

#### Storage of customer data

A core principle of Anchor Browser is minimizing data persistence. By design, we do not store customer data from within the browser sessions. Each browser instance runs in a dedicated, ephemeral virtual machine that is completely destroyed upon session termination. This means that any data accessed, generated, or downloaded during a session is either transferred directly to the customer's own environment via our secure peer-to-peer capability or is irretrievably deleted with the virtual machine. The only customer data we store is essential account and configuration information required for providing our service, such as user roles and network guardrail settings.

#### Confidentiality & Protection of Customer Data

We enforce strict measures to ensure the confidentiality and integrity of all customer data and platform interactions.

* Strict Tenant Isolation: Our architecture guarantees that each customer's browser instances are logically and physically isolated from one another. There is no possibility of cross-tenant data access.
* Ephemeral Environments: Browsers are never reused between sessions or customers. Every session starts with a pristine, isolated browser instance that is terminated and wiped clean after use, eliminating the risk of data leakage.
* Principle of Least Privilege: Access to all systems and data is governed by the principle of least privilege. Our employees are only granted the minimum level of access necessary to perform their job functions.

#### Data Encryption

Anchor employs robust encryption protocols to protect data at every stage.

* Encryption in Transit: All data transmitted between your local machine and the Anchor Browser instance, as well as any communication with our platform services, is encrypted using industry-standard TLS 1.2 or higher. We enforce the use of strong cipher suites to protect against eavesdropping and man-in-the-middle attacks.
* Encryption at Rest: While we minimize data storage, any essential configuration data or account information stored on our platform is encrypted at rest using AES-256, one of the strongest block ciphers available.

#### Reliability, Backup, and Business Continuity

Anchor is architected for high availability and resilience to ensure uninterrupted service.

* Redundant Architecture: Our infrastructure is deployed across multiple availability zones within our cloud provider's environment. This design protects against single-point-of-failure scenarios and ensures high uptime.
* Automated Backups: We perform regular, automated backups of critical platform configuration data. These backups are encrypted and stored securely, allowing for swift recovery in the unlikely event of a major disruption.
* Disaster Recovery: We maintain a comprehensive business continuity and disaster recovery plan that is regularly tested. This plan ensures that we can restore critical operations within a defined Recovery Time Objective (RTO).

#### Return of Customer Data

Given our ephemeral architecture, there is no session data to return. Any files downloaded during a session are transferred directly to your premises. As for your account and configuration data, you can request a copy of this information at any time during your service agreement. Upon termination of your contract, all associated account data will be permanently deleted from our systems in accordance with our data retention policy.

#### Certifications

Anchor is committed to meeting and exceeding industry standards for security and compliance. We have achieved key certifications that formally validate our security controls and demonstrate our commitment to protecting customer data:

* **SOC 2 Type II**: Anchor has achieved SOC 2 Type II compliance, demonstrating our commitment to security, availability, processing integrity, confidentiality, and privacy controls.
* **ISO 27001**: We are ISO 27001 certified, meeting the international standard for information security management systems.
* **HIPAA**: Anchor is HIPAA compliant, ensuring the protection of healthcare-related data and meeting the requirements of the Health Insurance Portability and Accountability Act.
* **GDPR**: We maintain GDPR compliance, protecting the privacy and data rights of European Union residents.

For the most up-to-date information on our certification status and detailed compliance reports, please visit the [Anchor Trust Portal](https://trust.anchorbrowser.io/).

<div style={{ display: 'flex', justifyContent: 'space-around', alignItems: 'center', gap: '2rem', margin: '2rem 0', flexWrap: 'wrap' }}>
  <img src="https://cdn.prod.website-files.com/64009032676f244c7bf002fd/678a6d6fc5825e05c17510b8_678a6d497673e6547fd00d40_aicpa-soc-logo-PNG.png" alt="SOC 2 Compliance" style={{ width: '90px', height: 'auto' }} />

  <img src="https://cms-assets.recognizeapp.com/wp-content/uploads/2022/05/06175813/ISO27001.png" alt="ISO 27001 Certification" style={{ width: '90px', height: 'auto' }} />

  <img src="https://i0.wp.com/beltlinehealth.com/wp-content/uploads/2022/02/hipaa_blue.png?fit=500%2C265&ssl=1" alt="HIPAA Compliance" style={{ width: '90px', height: 'auto' }} />

  <img src="https://www.loginradius.com/_next/static/media/gdpr-compliant.6f6aef57.webp" alt="GDPR Compliance" style={{ width: '90px', height: 'auto' }} />
</div>

#### Audits

Anchor engages independent, third-party auditors to conduct regular penetration tests and security assessments of our platform. These rigorous audits help us identify and remediate potential vulnerabilities, ensuring our defenses remain robust against emerging threats. A summary of our latest audit findings can be made available to customers upon request and under a Non-Disclosure Agreement (NDA).

#### Security Logs

We maintain detailed security logs to monitor for and investigate any suspicious activity.

* Audit Trails: We capture comprehensive audit logs of all administrative actions taken within the Anchor platform, such as changes to user permissions or security settings. Access to these logs is restricted to authorized personnel.
* Immutable Logging: Logs are stored in a secure, tamper-evident manner to ensure their integrity for forensic analysis and compliance purposes.

#### Personnel Practices

Our commitment to security extends to our internal team and practices.

* Security Training: We conduct mandatory security awareness training for all employees upon hiring and on an ongoing basis. This training covers data privacy, threat detection, and secure coding practices.
* Access Control: Access to our production environment is strictly controlled and limited to a small number of authorized engineers. We enforce multi-factor authentication (MFA) for all internal systems to add a critical layer of security.
