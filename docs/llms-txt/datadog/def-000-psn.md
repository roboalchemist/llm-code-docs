# Source: https://docs.datadoghq.com/security/default_rules/def-000-psn.md

---
title: Scout Suite user agent observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Scout Suite user agent observed
---

# Scout Suite user agent observed
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526) 
## Goal{% #goal %}

Detect when the [Scout Suite](https://github.com/nccgroup/ScoutSuite) user agent is observed.

## Strategy{% #strategy %}

This rule monitors cloud audit logs with the user agent `ScoutSuite`. Scout Suite is an open source multi-cloud security-auditing tool, which enables security posture assessment of cloud environments. Using the APIs exposed by cloud providers, Scout Suite gathers configuration data for manual inspection and highlights risk areas. While this tool may be used legitimately by an organization to assess their security posture it can also be used by attackers as a means of discovery once they have gained unauthorized access to your cloud environment.

The following cloud providers are currently supported by Scout Suite:

- Amazon Web Services
- Microsoft Azure
- Google Cloud Platform
- Alibaba Cloud (alpha)
- Oracle Cloud Infrastructure (alpha)
- Kubernetes clusters on a cloud provider (alpha)

## Triage and response{% #triage-and-response %}

1. Determine if your organization is using the Scout Suite tool to assess its security posture.
1. If it is, consider adding a suppression for the Scout Suite's identity or IP address. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the results of the triage indicate that this tool is not used by your organization, begin your company's incident response process and an investigation.
   - If appropriate, disable or rotate the affected credential/identity.
   - Investigate any actions taken by the identity.
