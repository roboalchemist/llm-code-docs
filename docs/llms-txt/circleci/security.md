# Source: https://circleci.com/security.md

# Your security is our priority

At CircleCI, our top concern is protecting our users’ intellectual property and sensitive secrets such as keys, tokens, and credentials.

## Compliance and authorizations

CircleCI takes the security of your applications seriously. We partner with the top security organizations to ensure that your projects are built, deployed, and maintained securely.

FedRAMP tailored

First CI/CD tool to meet the rigorous security and privacy [NIST](https://www.nist.gov/)\-standards of [FedRAMP](https://www.fedramp.gov/)

SOC 2 Type II compliant

[SOC 2 Type II compliance](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/serviceorganization-smanagement.html) is a component of the American Institute of CPAs (AICPA)’s Service Organization Control reporting platform

## Product security features

Get the compliance, security, and [audit logging](https://circleci.com/docs/security/#audit-logs) features that you need. Choose our cloud-hosted service with the option to use CircleCI compute and self-hosted runners, or run your own instance of CircleCI entirely on your own infrastructure.

### Source code security

Communication with your VCS to access source code is always encrypted over the wire using SSH and/or HTTPS.

### Config policies

Enforce organizational compliance and standardization across projects.

### Environment variables (secrets)

Protect secrets and other sensitive data in CircleCI using environment variables.

### OpenID Connect

CircleCI supports authentication via OpenID Connect at the job level. Using OIDC, pipelines can authenticate to systems like Vault, AWS and GCP without distributing secrets.

### Restricted contexts

Restricted contexts allow encrypted storage and sharing of environment variables across multiple projects while limiting access to certain user groups or at the project level.

### Audit logging

Use audit logs to monitor anomalies, assist in forensics, and demonstrate compliance.

### Runtime isolation

CircleCI runs all builds in isolated sandboxes that are destroyed after each use.

### Console output and artifacts

Encryption is employed over the wire using SSH and/or HTTPS for both console output and artifacts. Both are only available to those with read access to your repository.

### Two-factor authentication

CircleCI inherits 2FA authentication established in your third-party VCS provider.

### Compliance & certifications

| Current compliance & certifications |  |
| :-- | --- |
| SOC 2 Type II compliant | SOC 2 Type II provides CircleCI with an opportunity to meet (and exceed) industry standards and gives our customer organization’s access to industry-recognized, standardized reports that they can compare across services in our space. Achieving SOC 2 Type II compliance means that CircleCI has put in place and follows the procedures and security policies necessary to reduce risks, and that their processes can be requested and audited.  **Learn more about SOC 2 Type II at** [https://www.aicpa.org/](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/soclogosinfo.html). |
| FedRAMP tailored | Our FedRAMP Tailored designation demonstrates that CircleCI meets US government data security standards and is authorized for use within US government agencies.  **Learn more about the FedRAMP certification at** <https://www.fedramp.gov/>. |
| Data privacy frameworks | The certification ensures that CircleCI meets all data transfer security standards for the United States, the EU, the UK (and Gibraltar) and Switzerland under the EU-U.S. Data Privacy Framework, the UK Extension to the EU-U.S. Data Privacy Framework, and the Swiss-U.S. Data Privacy Framework as set forth by the U.S. Department of Commerce.  **Learn more about the Data Privacy Framework at** <https://www.dataprivacyframework.gov/>. |
| PCI compliance | CircleCI leverages the PCI compliance of Stripe. |

### Business practices

| Personnel & Processors |  |
| :-- | --- |
| Background checks | All CircleCI employees and contractors must pass a background check and sign confidentiality agreements. |
| Employee security awareness | CircleCI mandates that new employees attend classes covering security best practices. |
| Engineer security education | Engineers are required to attend an additional technical security workshop. |
| Policies | CircleCI maintains various security policies which are maintained and communicated by our security management team. |
| Partner management | CircleCI requires all partners and third-party vendors to fill out a security questionnaire. Those which handle PII are also required to sign a Data Processing Addendum. |

| Security incident response |  |
| :-- | --- |
| Response team | CircleCI maintains a dedicated Incident Response Team. |
| Response policy + plan | CircleCI maintains an Incident Response Policy and Runbook to facilitate decision making during critical situations. |
| Communication | Network and security incidents are published at <https://status.circleci.com/>. *At our discretion, based on the nature of a security incident, we may contact customers directly and/or publish security alert information to <https://circleci.com/blog/> in addition to (or in lieu of) posting to our general status page.* |

### Physical security

| Offices security |  |
| :-- | --- |
| Headquarters security | CircleCI headquarters employs 24-hour door personnel and badge access is required at all hours. Visitors are required to sign in and be escorted at all times. |
| Remote offices security | CircleCI’s remote offices in Denver, Japan, and London implement similar physical security controls to the San Francisco headquarters. |

| Fleet security |  |
| :-- | --- |
| Linux fleet security | CircleCI uses Amazon and Google Cloud Platform for its computing. Both vendors are industry leaders in security and privacy. |
| macOS fleet security | CircleCI operates macOS fleets housed at three data centers, located in Milwaukee, Las Vegas, and Atlanta. No CircleCI employee has physical access to the machines and all administration is done remotely. Data center engineers are the only people with access to provisioning machines, updating or deprovisioning machines. Federal regulators completed a full-day onsite audit in 2022 to assess the security, availability and integrity of the facility. Additionally, a penetration test was performed in late 2022 to identify and resolve any potential threats to the platform. Extensive badging, access logging, and other security controls are in place, all of which have been audited and approved under SOC 2 Type II compliance programs at CircleCI or the data center provider. |

### Network & data security

| Network security |  |
| :-- | --- |
| Vulnerability scanning | CircleCI implements a Docker-centric vulnerability scanning tool in its software development CI/CD process. Patching timelines for CircleCI’s cloud service are: - Critical – 14 days - High – 14 days - Medium – 30 days - Low – 30 days  Monthly scans are submitted to federal authorities as part of ongoing FedRAMP compliance. |
| Internal systems auditing | CircleCI maintains a formal Audit Policy governing application events, system events, hardware events, and physical access. This includes the what, when, and where of the event, its source, its object, its outcome, and the person associated with it. |
| Architecture | CircleCI’s architecture consists of multiple layers of data security including a DMZ, bastion hosts, and firewalls. |
| Global distribution | CircleCI’s Site Reliability, Support and Engineering teams are globally distributed for 24/7/365 coverage. |
| Build isolation | CircleCI runs all builds in isolated sandboxes that are destroyed after each use. |

| Data security |  |
| :-- | --- |
| Traffic encryption | All data in transit is encrypted via TLS and SSH. |
| Environment variable encryption | Environment variables are encrypted at rest and in transit, and injected into the runtime environment at the start of a job. All sensitive secrets such as keys, tokens, and other credentials should be stored as environment variables within CircleCI. |
| Source code encryption | Source code is always encrypted via TLS and SSH in transit, but is not encrypted at rest. Source code at rest is secured behind multiple layers of architecture security such as DMZ, bastion hosts, and firewalls. |
| Data backup | CircleCI maintains a Data Backup and Snapshot Policy that requires restoration capabilities within common industry timelines. |

### Application security

| Secure development |  |
| :-- | --- |
| Secure coding | The Software Development Lifecycle Policy dictates delivery, review and merge processes to minimize rollbacks, downtime, design flaws and security incidents. |
| Site reliability | CircleCI employs a team of Site Reliability Engineers ensuring that the CircleCI application security layers are consistently maintained. |

| Application-level security |  |
| :-- | --- |
| OWASP Top 10 | CircleCI’s web application is designed to withstand OWASP Top 10 matters such as injections, broken authentication and session management, cross-site scripting (XSS), insecure direct object references, missing function level access control, cross-site request forgery (CSRF), unvalidated redirects and forwards. |
| Application penetration testing | Third-party penetration testers are hired annually to test the CircleCI application, network, infrastructure, and new products for vulnerabilities. Coverage ranges from OWASP Top 10 to threat modeling of new product features. |

## Have a security concern about CircleCI?

### Finding serious security issues

If you find any of the following issues, please contact us with relevant details including steps to reproduce or a proof-of-concept.

*   Injection vulnerabilities
*   Authentication or session problems
*   Improper access to sensitive data
*   Broken access controls
*   Cross-site scripting
*   Anything from the OWASP Top 10 Project
*   Email spoofing, SPF, DKIM, and DMARC errors

### Protect our users’ data

Upon discovering a vulnerability, we ask that you:

*   Inform us as soon as possible, contact our security team by email at [security@circleci.com](mailto:security@circleci.com)
    *   If you are reporting a sensitive issue, please encrypt your message using our security team’s GPG key (ID: `0x4013DDA7`, fingerprint: `3CD2 A48F 2071 61C0 B9B7 1AE2 6170 15B8 4013 DDA7`)
*   Test against fake data and accounts, not our users’ private data (please ask if you’d like a free account to work on this)
*   Work with us to close the vulnerability before disclosing it to others

[Email security@circleci.com](mailto:security@circleci.com) 

### CircleCI does not have a bounty program

We do not offer bug bounties for discovered vulnerabilities. We hope that if you discover vulnerabilities in the course of your work that you share them with us so we can improve the health of the internet ecosystem.

### Reports we do not act on

*   Credentials in a 3rd party’s `.circleci/config.yml`

## Learn more

[Integrate CircleCI with HashiCorp Vault using OIDC](https://circleci.com/blog/oidc-with-vault/)

[Security best practices for CI/CD](https://circleci.com/blog/security-best-practices-for-ci-cd/)

[Vulnerability management and DevSecOps with CI/CD](https://circleci.com/resources/devsecops-ebook/)