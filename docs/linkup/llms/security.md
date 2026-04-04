# Source: https://docs.linkup.so/pages/security-and-privacy/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Security

Linkup Technologies implements enterprise-grade security controls to protect our infrastructure, services, and client data. Our security program is designed to meet the stringent requirements of clients in highly regulated industries including financial services, consulting, and healthcare.

<Card title="Trust Center" icon="shield" href="https://trust.linkup.so/" horizontal>
  Visit Linkup's Trust Center
</Card>

​

## Certifications and compliance

* **SOC 2 Type II** certification validating security, availability, and confidentiality controls (report available upon request).

## Data encryption

* **In transit**: TLS 1.2+ for all API communications.
* **At rest**: AES-256 for any stored data.
* **Key management**: Enterprise key management services with strict access controls.

## Infrastructure security

* **Cloud infrastructure**: Hosted on enterprise-grade cloud platforms.
* **Network security**: VPC segregation, network segmentation via security groups and ACLs, multi-layer firewalls, DDoS protection, and no public database endpoints.
* **Hardening**: Baseline configurations, timely patching, and least-privilege service roles.

## Privileged access management

<Callout type="success" icon="check" title="RBAC + MFA">
  Privileged and administrative access requires multi‑factor authentication with strict role‑based access control.
</Callout>

<Callout type="success" icon="check" title="Monitored privileged access">
  All privileged access is logged, continuously monitored, and regularly reviewed.
</Callout>

<Callout type="success" icon="check" title="Least privilege & JIT">
  Access follows least‑privilege principles with just‑in‑time elevation where applicable.
</Callout>

## Vulnerability management and secure development

<Callout type="success" icon="check" title="Quarterly vulnerability scanning">
  Independent scans (Bastion Technologies) with tracked remediation.
</Callout>

<Callout type="success" icon="check" title="Annual penetration testing">
  Independent assessors validate controls and exploit paths.
</Callout>

<Callout type="success" icon="check" title="Continuous monitoring">
  Automated threat detection and alerting across infrastructure and apps.
</Callout>

<Callout type="success" icon="check" title="Remediation SLAs">
  Defined timelines by severity for fast, predictable fixes.
</Callout>

<Callout type="success" icon="check" title="Security‑by‑design SDLC">
  Design reviews, code scanning, dependency checks, and secure API patterns.
</Callout>

<Callout type="success" icon="check" title="Staff security training">
  Regular training to maintain security awareness and best practices.
</Callout>

## Malware and threat prevention (crawling safeguards)

<Callout type="success" icon="check" title="AI‑powered filtering">
  Blocks malware, phishing, and malicious sources before indexing or serving.
</Callout>

<Callout type="success" icon="check" title="Result curation safeguards">
  Ranking protects against sensitive and prohibited content exposure.
</Callout>

<Callout type="success" icon="check" title="Web filtering & DNS security">
  High‑risk sites are automatically blocked.
</Callout>

<Callout type="success" icon="check" title="Configurable domain exclusions">
  Control results via the <code>ExcludeDomains</code> API parameter.
</Callout>

<Callout type="success" icon="check" title="Ethical crawling standards">
  Respect for <code>robots.txt</code>; no circumvention of CAPTCHAs or access controls.
</Callout>

Enterprise customization available: We can accommodate custom breach notification timelines, tailored remediation SLAs, dedicated security reviews, and bespoke compliance reporting.


Built with [Mintlify](https://mintlify.com).