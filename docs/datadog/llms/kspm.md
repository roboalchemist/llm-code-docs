# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/kspm.md

---
title: Kubernetes Security Posture Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Misconfigurations >
  Kubernetes Security Posture Management
---

# Kubernetes Security Posture Management

Kubernetes Security Posture Management (KSPM) for Cloud Security helps you proactively strengthen the security posture of your Kubernetes deployments by benchmarking your environment against established industry best practices, such as those defined by [CIS](https://www.cisecurity.org/cis-benchmarks), or your own custom detection policies.

## Setting up KSPM{% #setting-up-kspm %}

To take full advantage of KSPM, you must install both the Datadog Agent and cloud integrations. For detailed instructions, see the following articles:

- [Deploying Cloud Security on the Agent](https://docs.datadoghq.com/security/cloud_security_management/setup/agent/)
- [Deploying Cloud Security via Cloud Integrations](https://docs.datadoghq.com/security/cloud_security_management/setup/cloud_integrations/)

This allows Datadog to detect risks in your Kubernetes deployments for each of the following resource types:

| Resource Type                     | Install Method    | Framework        |
| --------------------------------- | ----------------- | ---------------- |
| `aws_eks_cluster`                 | Cloud integration | `cis-eks`        |
| `aws_eks_worker_node`             | Agent             | `cis-eks`        |
| `azure_aks_cluster`               | Cloud integration | `cis-aks`        |
| `azure_aks_worker_node`           | Agent             | `cis-aks`        |
| `gcp_kubernetes_engine_cluster`   | Cloud integration | `cis-gke`        |
| `gcp_kubernetes_engine_node_pool` | Cloud integration | `cis-gke`        |
| `gcp_gke_worker_node`             | Agent             | `cis-gke`        |
| `kubernetes_master_node`          | Agent             | `cis-kubernetes` |
| `kubernetes_worker_node`          | Agent             | `cis-kubernetes` |

## Monitor risk across Kubernetes deployments{% #monitor-risk-across-kubernetes-deployments %}

With KSPM, Datadog scans your environment for risks defined by more than 50+ out-of-the-box Kubernetes detection rules. When at least one case defined in a rule is matched over a given period of time, [a notification alert is sent](https://docs.datadoghq.com/security/misconfigurations/compliance_rules#set-notification-targets-for-compliance-rules), and a finding is generated in the [Misconfigurations explorer](https://app.datadoghq.com/security/compliance).

Each finding contains the context you need to identify the issue's impact, such as the full resource configuration, resource-level tags, and a map of the resource's relationships with other components of your infrastructure. After you understand the problem and its impact, you can start remediating the issue by [creating a Jira ticket](https://docs.datadoghq.com/security/cloud_security_management/review_remediate/jira) from within Cloud Security or by [executing a pre-defined workflow](https://docs.datadoghq.com/security/cloud_security_management/review_remediate/workflows).

**Note**: You can also use the [API to programmatically interact with findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-findings).

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/kspm_finding_1.d7e0c3972a053421b48b6507c3361f9b.png?auto=format"
   alt="The details panel for a medium severity finding for the EKS Cluster should have public access limited rule" /%}

## Assess your Kubernetes security posture against industry-standard frameworks{% #assess-your-kubernetes-security-posture-against-industry-standard-frameworks %}

Cloud Security provides a [security posture score](https://docs.datadoghq.com/security/cloud_security_management#track-your-organizations-health) that helps you understand your security and compliance status using a single metric. The score represents the percentage of your environment that satisfies all of your active out-of-the-box cloud and infrastructure detection rules. You can obtain the score for your entire organization, or for specific teams, accounts, and environments, including Kubernetes deployments.

For an in-depth explanation on how the security posture score works, see [Security posture score](https://docs.datadoghq.com/glossary/#security-posture-score).

### View security posture score for Kubernetes deployments{% #view-security-posture-score-for-kubernetes-deployments %}

To view the security posture score for your Kubernetes deployments, navigate to the [**Security** > **Compliance**](https://app.datadoghq.com/security/compliance/home) page and locate the CIS Kubernetes frameworks reports.

### View detailed reports for Kubernetes frameworks{% #view-detailed-reports-for-kubernetes-frameworks %}

Click a framework to view a detailed report that gives you insight into how you score against the framework's requirements and rules. On the framework page, you can download a copy of the report as a PDF or export it as a CSV.

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/kubernetes_posture_score_3.bef96cf6f2d85b7622e38b9c4e05a87b.png?auto=format"
   alt="The CIS Kubernetes compliance report page showing an overall posture score of 64 percent" /%}

## Create your own Kubernetes detection rules{% #create-your-own-kubernetes-detection-rules %}

In addition to the out-of-the-box detection rules, you can also create your own Kubernetes detection rules by cloning an existing rule or creating a new one from scratch. Rules are written in the [Rego policy language](https://www.openpolicyagent.org/docs/latest/policy-language/), a flexible Python-like language that serves as the industry standard for detection rules. For more information, see [Writing Custom Rules with Rego](https://docs.datadoghq.com/security/cloud_security_management/guide/writing_rego_rules/).

After you create the detection rule, you can customize its severity (`Critical`, `High`, `Medium`, `Low`, or `Info`) and [set alerts for real-time notifications](https://docs.datadoghq.com/security/misconfigurations/compliance_rules#set-notification-targets-for-compliance-rules) to notify you when a new finding is detected.

## Further reading{% #further-reading %}

- [Explore default Cloud Security Misconfigurations cloud configuration detection rules](https://docs.datadoghq.com/security/default_rules)
- [Create Custom Rules](https://docs.datadoghq.com/security/misconfigurations/custom_rules)
