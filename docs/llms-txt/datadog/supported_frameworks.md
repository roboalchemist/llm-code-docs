# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks/supported_frameworks.md

---
title: Supported Frameworks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Misconfigurations >
  Manage Your Security Compliance Posture > Supported Frameworks
---

# Supported Frameworks

Cloud Security Misconfigurations comes with more than 1,000 out-of-the-box compliance rules that evaluate the configuration of your cloud resources and identify potential misconfigurations. Each [compliance rule](https://docs.datadoghq.com/security_monitoring/default_rules/) maps to one or more controls within the following compliance standards and industry benchmarks.

{% alert level="info" %}
In Cloud Security, rules with the **infrastructure** label are applicable to Agent installations.
{% /alert %}

| Framework                                                                                                                                       | Supported Versions             | Framework Tag                       | Rule Type                |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------- | ------------------------ |
| [AICPA SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)                                          | 2017 TSC w/ rev POF - 2022     | `soc-2`                             | Cloud                    |
| [Australia APRA CPS 234](https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf)                                  | 2019                           | `cps234`                            | Cloud                    |
| [Australia ASD Essential 8](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight)                        | 2024                           | `essential8`                        | Cloud                    |
| [AWS Foundational Security Best Practices](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html)                         | v1.0.0                         | `aws-fsbp`                          | Cloud                    |
| [Brazil LGPD](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/outros-documentos-e-publicacoes-institucionais/lgpd-en-lei-no-13-709-capa.pdf) | 2018                           | `lgpd`                              | Cloud                    |
| [California CCPA/CPRA](https://oag.ca.gov/privacy/ccpa)                                                                                         | Nov 2022                       | `ccpa`                              | Cloud                    |
| [CIS AlmaLinux 9](https://www.cisecurity.org/benchmark/almalinuxos_linux)                                                                       | v2.0.0                         | `cis-almalinux9`                    | Infrastructure           |
| [CIS Amazon Linux 2023](https://www.cisecurity.org/benchmark/amazon_linux)                                                                      | v1.0.0                         | `cis-al2023`                        | Infrastructure           |
| [CIS Amazon Linux 2](https://www.cisecurity.org/benchmark/amazon_linux)                                                                         | v3.0.0                         | `cis-amzn2`                         | Infrastructure           |
| [CIS AWS Foundations Benchmark*](https://www.cisecurity.org/benchmark/amazon_web_services/)                                                     | v5.0.0, v4.0.0, v3.0.0, v1.5.0 | `cis-aws`                           | Cloud                    |
| [CIS Azure Foundations Benchmark](https://www.cisecurity.org/benchmark/azure)                                                                   | v4.0.0, v2.0.0                 | `cis-azure`                         | Cloud                    |
| [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)                                                                             | v1.2                           | `cis-docker`                        | Infrastructure           |
| [CIS GCP Foundations Benchmark](https://www.cisecurity.org/benchmark/google_cloud_computing_platform)                                           | v3.0.0                         | `cis-gcp`                           | Cloud                    |
| [CIS GKE](https://www.cisecurity.org/benchmark/kubernetes)                                                                                      | v1.6.0                         | `cis-gke`                           | Cloud                    |
| [CIS Kubernetes (AKS) Benchmark**](https://www.cisecurity.org/benchmark/kubernetes/)                                                            | v1.4.0                         | `cis-aks`                           | Cloud and Infrastructure |
| [CIS Kubernetes (EKS) Benchmark**](https://www.cisecurity.org/benchmark/kubernetes/)                                                            | v1.7.0, v1.4.0                 | `cis-eks`                           | Cloud and Infrastructure |
| [CIS Kubernetes Benchmark**](https://www.cisecurity.org/benchmark/kubernetes/)                                                                  | v1.9.0                         | `cis-kubernetes`                    | Infrastructure           |
| [CIS Red Hat Linux 7](https://www.cisecurity.org/benchmark/red_hat_linux)                                                                       | v3.1.1                         | `cis-rhel7`                         | Infrastructure           |
| [CIS Red Hat Linux 8](https://www.cisecurity.org/benchmark/red_hat_linux)                                                                       | v3.0.0                         | `cis-rhel8`                         | Infrastructure           |
| [CIS Red Hat Linux 9](https://www.cisecurity.org/benchmark/red_hat_linux)                                                                       | v2.0.0                         | `cis-rhel9`                         | Infrastructure           |
| [CIS Ubuntu 20.04](https://www.cisecurity.org/benchmark/ubuntu_linux)                                                                           | v1.0.0                         | `cis-ubuntu2004`                    | Infrastructure           |
| [CIS Ubuntu 22.04](https://www.cisecurity.org/benchmark/ubuntu_linux)                                                                           | v2.0.0                         | `cis-ubuntu2204`                    | Infrastructure           |
| [CIS Ubuntu 24.04](https://www.cisecurity.org/benchmark/ubuntu_linux)                                                                           | v1.0.0                         | `cis-ubuntu2404`                    | Infrastructure           |
| [CMMC](https://dowcio.war.gov/CMMC/About/)                                                                                                      | v2.0                           | `cmmc-level-2`                      | Cloud                    |
| [Digital Operational Resilience Act (DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)                             | C(2024) 1532                   | `dora`                              | Cloud                    |
| [Essential Cloud Security Controls](https://www.datadoghq.com/blog/essential-cloud-security-controls-ruleset-v2/)                               | v2                             | `essential-cloud-security-controls` | Cloud                    |
| [EU Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)                                               | 2024                           | `cyber-resilience-act`              | Cloud                    |
| [FedRAMP High](https://www.fedramp.gov/) (Preview)                                                                                              | v5                             | `fedramp-high`                      | Cloud                    |
| [FedRAMP Moderate](https://www.fedramp.gov/) (Preview)                                                                                          | v5                             | `fedramp-moderate`                  | Cloud                    |
| [FedRAMP Low](https://www.fedramp.gov/) (Preview)                                                                                               | v5                             | `fedramp-low`                       | Cloud                    |
| [GDPR](https://gdpr.eu/)                                                                                                                        | 2016/679                       | `gdpr`                              | Cloud                    |
| [HIPAA](https://www.hhs.gov/hipaa/index.html)                                                                                                   | 800-66-r2                      | `hipaa`                             | Cloud                    |
| [ISO/IEC 27001](https://www.iso.org/isoiec-27001-information-security.html)                                                                     | 2022, 2013                     | `iso-27001`                         | Cloud                    |
| [NIS2 Directive (EU)](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)                                                         | 2022/2555                      | `nis2`                              | Cloud                    |
| [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final)                                                                             | v2                             | `nist-800-171`                      | Cloud                    |
| [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)                                                                               | v5                             | `nist-800-53`                       | Cloud                    |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)                                                      | v1.0                           | `nist-ai-rmf`                       | Cloud                    |
| [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework/framework)                                                                   | v2.0, v1.1                     | `nist-csf`                          | Cloud                    |
| [PCI DSS](https://www.pcisecuritystandards.org/document_library)                                                                                | v4.0                           | `pci-dss`                           | Cloud                    |
| [UK Cyber Essentials](https://www.ncsc.gov.uk/cyberessentials/overview)                                                                         | 2024                           | `cyber-essentials`                  | Cloud                    |
| [Singapore MAS TRM](https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines)                                         | 2021                           | `mas-trm`                           | Cloud                    |

\*To pass the Monitoring Section of the [CIS AWS Foundations benchmark](https://www.cisecurity.org/benchmark/amazon_web_services/), you **must** enable [Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/) and forward [CloudTrail logs to Datadog](https://docs.datadoghq.com/integrations/amazon_cloudtrail/).

\**Some [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/) compliance rules only apply to self-hosted Kubernetes clusters.

**Notes**:

- Cloud Security Misconfigurations provides visibility into whether your resources are configured in accordance with certain compliance rules. These rules address various regulatory frameworks, benchmarks, and standards (Security Posture Frameworks). Cloud Security Misconfigurations does not provide an assessment of your actual compliance with any Security Posture Framework, and the compliance rules may not address all configuration settings that are relevant to a given framework. Datadog recommends that you use Cloud Security Misconfigurations in consultation with your legal counsel or compliance experts.
- The compliance rules for the CIS benchmarks follow the CIS automated recommendations. If you're obtaining CIS certification, Datadog recommends also reviewing the manual recommendations as part of your overall security assessment.
- Datadog also provides Essential Cloud Security Controls, a set of recommendations developed by Datadog internal security experts. Based on common cloud security risks observed by Datadog, this ruleset aims to help users that are new to cloud security remediate high-impact misconfigurations across their cloud environments.

## Further reading{% #further-reading %}

- [Getting started with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cspm/setup)
- [Explore default Cloud Security Misconfigurations cloud configuration compliance rules](https://docs.datadoghq.com/security/default_rules)
- [Search and explore misconfigurations](https://docs.datadoghq.com/security/cspm/findings)
- [Datadog Security extends compliance and threat protection capabilities for Google Cloud](https://www.datadoghq.com/blog/datadog-security-google-cloud/)
