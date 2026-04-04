# Source: https://docs.datadoghq.com/security.md

---
title: Datadog Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security
---

## Overview{% #overview %}

Bring speed and scale to your production security operations. Datadog Security delivers real-time threat detection, and continuous configuration audits across applications, hosts, containers, and cloud infrastructure. Coupled with the greater Datadog observability platform, Datadog Security brings unprecedented integration between security and operations aligned to your organization's shared goals.

Datadog Security includes:

- Cloud SIEM
- Code Security
- Cloud Security
- App and API Protection
- Workload Protection
- Sensitive Data Scanner

To learn more, check out the [30-second Product Guided Tour](https://www.datadoghq.com/guided-tour/security/).

## Cloud SIEM{% #cloud-siem %}

[Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem) (Security Information and Event Management) detects real-time threats to your application and infrastructure, like a targeted attack, an IP communicating with your systems which matches a threat intel list, or an insecure configuration. Cloud SIEM is powered by [Datadog Log Management](https://docs.datadoghq.com/logs/). With these areas combined, you can [automate remediation of threats detected by Datadog Cloud SIEM](https://www.datadoghq.com/blog/automated-vulnerability-remediation-datadog/) to speed up your threat-response workflow. Check out the dedicated [Guided Tour](https://www.datadoghq.com/guided-tour/security/cloud-siem/) to see more.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/cloud_siem_overview_2025.03fcaa2b666af25c9d72b24c9fe4aa52.png?auto=format"
   alt="The Cloud SIEM home page showing the Security Overview section with widgets for important signals, suspicious actors, impacted resources, threat intel, and signal trends" /%}

## Code Security{% #code-security %}

[Code Security](https://docs.datadoghq.com/security/code_security/) scans your first-party code and open source libraries used in your applications in both your repositories and running services, providing end-to-end visibility from development to production. It encompasses the following capabilities:

- [Static Code Analysis (SAST)](https://docs.datadoghq.com/security/code_security/static_analysis/) for identifying security and quality issues in your first-party code
- [Software Composition Analysis (SCA)](https://docs.datadoghq.com/security/code_security/software_composition_analysis/) for identifying open source dependencies in both your repositories and your services
- [Runtime Code Analysis (IAST)](https://docs.datadoghq.com/security/code_security/iast/) for identifying vulnerabilities in the first-party code within your services
- [Secret Scanning](https://docs.datadoghq.com/security/code_security/secret_scanning/) for identifying and validating leaked secrets (in Preview)

With IDE integrations, pull request comments, and CI/CD gates, Code Security helps teams implement DevSecOps throughout the organization:

- **Developers:** early vulnerability detection, code quality improvements, faster development as developers spend less time debugging and patching.
- **Security Administrators:** enhanced security posture, improved patch management in response to early vulnerability alerts, and compliance monitoring.
- **Site Reliability Engineers (SREs):** automated security checks throughout CI/CD workflow, security compliance, and system resilience. SAST reduces manual overhead for SREs and ensures that each release is thoroughly tested for vulnerabilities.

{% image
   source="https://datadog-docs.imgix.net/images/code_security/gitlab_integration_light.57c3526484e8f6b118d1baaf88676726.png?auto=format"
   alt="A SAST finding within a GitLab repository" /%}

## Cloud Security{% #cloud-security %}

[Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/) delivers real-time threat detection and continuous configuration audits across your entire cloud infrastructure, all in a unified view for seamless collaboration and faster remediation. Powered by observability data, security teams can determine the impact of a threat by tracing the full attack flow and identify the resource owner where a vulnerability was triggered.

Cloud Security includes [Workload Protection](https://docs.datadoghq.com/security/workload_protection/), [Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/), [Identity Risks](https://docs.datadoghq.com/security/cloud_security_management/identity_risks/), and [Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/). To learn more, check out the dedicated [Guided Tour](https://www.datadoghq.com/guided-tour/security/cloud-security-management/).

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/csm_overview_3.e072107660e4bc7aa938fa4f4ce879b9.png?auto=format"
   alt="The Security Inbox on the Cloud Security overview shows a list of prioritized security issues" /%}

To get started with Datadog Security, navigate to the [**Security** > **Setup**](https://app.datadoghq.com/security/configuration) page in Datadog, which has detailed information for single or multi-configuration, or follow the getting started sections below to learn more about each area of the platform.

## App and API Protection{% #app-and-api-protection %}

Datadog [App and API Protection (AAP)](https://docs.datadoghq.com/security/application_security/) provides observability into application-level attacks that aim to exploit code-level vulnerabilities, such as Server-Side-Request-Forgery (SSRF), SQL injection, Log4Shell, and Reflected Cross-Site-Scripting (XSS). AAP leverages [Datadog APM](https://docs.datadoghq.com/tracing/), the [Datadog Agent](https://docs.datadoghq.com/agent/), and in-app detection rules to detect threats in your application environment. Check out the product [Guided Tour](https://www.datadoghq.com/guided-tour/security/application-security-management/) to see more.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/app-sec-landing-page.c2f5121538f63fd687263ebf1b8a430f.png?auto=format"
   alt="A security signal panel in Datadog, which displays attack flows and flame graphs" /%}

## Workload Protection{% #workload-protection %}

[Workload Protection](https://docs.datadoghq.com/security/workload_protection/) monitors file, network, and process activity across your environment to detect real-time threats to your infrastructure. As part of the Datadog platform, you can combine the real-time threat detection of Workload Protection with metrics, logs, traces, and other telemetry to see the full context surrounding a potential attack on your workloads.

- Proactively block threats with [Active Protection](https://docs.datadoghq.com/security/workload_protection/guide/active-protection).
- Manage out-of-the-box and custom [detection rules](https://docs.datadoghq.com/security/workload_protection/workload_security_rules).
- Set up real-time [notifications](https://docs.datadoghq.com/security/notifications/).
- Investigate and remediate [security signals](https://docs.datadoghq.com/security/workload_protection/security_signals).

## Sensitive Data Scanner{% #sensitive-data-scanner %}

[Sensitive Data Scanner](https://docs.datadoghq.com/sensitive_data_scanner/) can help prevent sensitive data leaks and limit non-compliance risks by discovering, classifying, and optionally redacting sensitive data. It can scan for sensitive data in your telemetry data, such as application logs, APM spans, RUM events, and events from Event Management. It can also scan for sensitive information within your cloud storage resources.

After you [set up Sensitive Data Scanner](https://docs.datadoghq.com/sensitive_data_scanner/setup/), use the Findings page to see details of sensitive data findings that have been identified, so that you can triage, investigate, and remediate the findings.

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/sds_summary_20250203.d813af89f7cb6a5a0a676fd5488fe412.png?auto=format"
   alt="The summary page showing an overview of sensitive findings broken down by priority" /%}

## Further Reading{% #further-reading %}

- [Check out the latest Datadog Security releases! (App login required).](https://app.datadoghq.com/release-notes?category=Security%20%26%20Compliance)
- [See a Product Guided Tour](https://www.datadoghq.com/guided-tour/security/)
- [Begin detecting threats with Cloud SIEM](https://docs.datadoghq.com/getting_started/cloud_siem)
- [Start tracking misconfigurations with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/)
- [Uncover kernel-level threats with Workload Protection](https://docs.datadoghq.com/security/workload_protection/)
- [Read about security-related topics on Datadog's Security Labs blog](https://securitylabs.datadoghq.com/)
- [Join an interactive session to elevate your security and threat detection](https://dtdg.co/fe)
- [Elevate AWS threat detection with Stratus Red Team](https://www.datadoghq.com/blog/cyber-attack-simulation-with-stratus-red-team/)
- [Best practices for securing Kubernetes applications](https://www.datadoghq.com/blog/kubernetes-security-best-practices/)
- [Best practices for network perimeter security in cloud-native environments](https://www.datadoghq.com/blog/securing-cloud-native-infrastructure-network-perimeter/)
- [Best practices for data security in cloud-native infrastructure](https://www.datadoghq.com/blog/securing-data-in-cloud-native-infrastructure/)
- [Security-focused chaos engineering experiments for the cloud](https://www.datadoghq.com/blog/chaos-engineering-for-security/)
- [Datadog's approach to DevSecOps](https://www.datadoghq.com/blog/datadogs-approach-devsecops/)
- [Investigating a complex denial-of-service attack](https://www.datadoghq.com/blog/investigate-denial-of-service-attacks/)
- [Tips to optimize and secure Azure Functions](https://www.datadoghq.com/blog/optimize-and-secure-azure-functions/)
- [How we use Datadog for detection as code](https://www.datadoghq.com/blog/datadog-detection-as-code/)
- [Detect lateral movement in hybrid Azure environments](https://www.datadoghq.com/blog/lateral-movement-entra-id-azure/)
- [Identify the secrets that make your cloud environment more vulnerable to an attack](https://www.datadoghq.com/blog/secrets-management/)
- [Cloud security research and guide roundup: Infrastructure and access](https://www.datadoghq.com/blog/cloud-security-roundup-infrastructure-identity/)
- [Cloud security research and guide roundup: DevSecOps, threat detection, and AI](https://www.datadoghq.com/blog/cloud-security-roundup-devsecops-threat-detection-ai/)
- [Key metrics for measuring your organization's security posture](https://www.datadoghq.com/blog/key-security-metrics/)
- [Security and SRE: How Datadog's combined approach aims to tackle security and reliability challenges](https://www.datadoghq.com/blog/datadogs-approach-sre-security/)
- [2025 cloud security roundup: How attackers abused identities, supply chains, and AI](https://www.datadoghq.com/blog/cloud-security-roundup-2025)
- [Mitigation for Node.js denial-of-service vulnerability affecting Datadog APM](https://www.datadoghq.com/blog/nodejs-vulnerability-apm)
