# Source: https://docs.datadoghq.com/security/workload_protection/inventory/hosts_and_containers.md

---
title: Hosts and Containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Workload Protection > Coverage and Posture
  Management > Hosts and Containers
---

# Hosts and Containers

The [Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts) view in Datadog Workload Protection **Inventory** provides a unified view of host-level agent deployment, configuration health, and security feature status.

The **Hosts and Containers** view shows the hostname of all active Agents running directly on hosts or as containers. This includes hosts with Workload Protection enabled or disabled.

**Hosts and Containers** enables DevSecOps teams to:

- Verify that protections are properly deployed and running across environments, including:
  - [Workload Protection](https://docs.datadoghq.com/security/workload_protection/)
  - [CSM Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/)
  - [Container Vulnerability Scanning](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/)
  - [Host Vulnerability Scanning](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/)
- Identify which hosts and containers are running old versions of the Agent
- Access remediation guidance for missing protections

## Use cases{% #use-cases %}

The [Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts) inventory supports several common DevSecOps use cases.

### Assess coverage status{% #assess-coverage-status %}

To identify hosts where runtime threat detection is not configured:

1. In [Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts), set the following facets to **false**:

   - **Workload Protection Enabled**
   - **Misconfigurations Enabled**
   - **Hosts VM Enabled**
   - **Containers VM Enabled**

The hosts and containers missing one or more of these features are shown with an orange icon. This list flags coverage gaps that expose the workload to undetected process, file, or network-level threats.

1. For remediation guidance, hover over the icon for a feature and click **Configure**.

{% alert level="info" %}
Filter by Containers VM Enabled: true to ensure scanning is also applied to container workloads running inside a VM context.
{% /alert %}

### Validate Agent health{% #validate-agent-health %}

To validate Agent health:

1. In the **Agent Version** column, look for older versions identified with yellow labels.

Yellow labels indicate versions that might not support all security features.

1. Click a version label (for example, 7.69.1), and select **Filter by agent\_version:[number]**. This isolates all hosts running that version.

1. Outside of [Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts), check each Agent host for upgrade readiness and [schedule upgrades accordingly](https://docs.datadoghq.com/agent/guide/upgrade_agent_fleet_automation).

### Detect misconfigurations{% #detect-misconfigurations %}

Hosts without CSM Misconfigurations enabled can't surface IAM, logging, or encryption misconfigurations. Misconfiguration checks are critical for CIS Benchmarks and NIST-aligned cloud security posture management.

To check whether posture checks are enabled for a host:

1. In [Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts), set the **Misconfigurations Enabled** facet to **false**.

The hosts and containers without CSM Misconfigurations enabled are indicated by an orange icon.

1. For remediation guidance, hover over the **CSM Misconfigurations** icon and click **Configure**.

See Cloud Security Vulnerabilities [deployment methods](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/).

### Cluster-level tracking{% #cluster-level-tracking %}

The **Cluster Name** column links hosts to logical infrastructure boundaries like Kubernetes clusters. Filter on a cluster by clicking its name and selecting **Filter by cluster\_name:[name]**.

Filtering on a cluster confirms whether protections are applied uniformly. This ensures protections are applied consistently across environments and regions.

### Prioritize response{% #prioritize-response %}

[Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts) supports investigations and incident triage. Use the feature icon panel to spot protection gaps.

Typically, hosts missing critical features like **Workload Protection** or **Host/Container Vulnerability Scanning** are triaged first.

Hover over a feature icon and click **Configure** to see remediation steps for all feature gaps. This enables triage without context switching.

### Compliance evidence{% #compliance-evidence %}

[Hosts and Containers](https://app.datadoghq.com/security/workload-protection/inventory/hosts) provides a live audit view for workload security posture. Filters such as **Workload Protection Enabled** and **Agent Version** demonstrate control coverage for frameworks such as SOC 2, PCI DSS, or FedRAMP.
