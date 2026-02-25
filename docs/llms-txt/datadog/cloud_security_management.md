# Source: https://docs.datadoghq.com/getting_started/security/cloud_security_management.md

# Source: https://docs.datadoghq.com/security/cloud_security_management.md

---
title: Cloud Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud Security
---

# Cloud Security

{% callout %}
##### Join an enablement webinar session

Learn how Datadog Cloud SIEM and Cloud Security elevate your organization's threat detection and investigation for dynamic, cloud-scale environments.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Security)
{% /callout %}

Datadog Cloud Security delivers deep visibility, continuous configuration audits, identity risk assessments, vulnerability detection, and real-time threat detection across your entire cloud infrastructureâall in a unified platform for seamless collaboration and faster remediation.

Security and DevOps teams can act on the shared context of observability and security data to quickly prioritize and remediate issues.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Agentless Scanning is not available in the selected site ().
{% /alert %}


{% /callout %}

Cloud Security leverages both the Datadog Agent and Agentless. It includes a variety of features you can enable to manage different facets of your organization's security:

- [**Misconfigurations**](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/): Tracks the security hygiene and compliance posture of your production environment, automates audit evidence collection, and enables you to remediate misconfigurations that leave your organization vulnerable to attacks.
- [**Identity Risks**](https://docs.datadoghq.com/security/cloud_security_management/identity_risks/): Provides in-depth visibility into your organization's AWS IAM, Azure, and GCP risks, and enables you to detect and resolve identity risks on an ongoing basis.
- [**Vulnerabilities**](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/): Continuously detect, prioritize, and remediate exploitable vulnerabilities in your container images, host images, and hosts running in your infrastructure.

Cloud Security also includes access to Datadog Security features, including:

- [Detection Rules](https://docs.datadoghq.com/security/detection_rules/)
- [Notifications](https://docs.datadoghq.com/security/notifications/)
- [Automation Pipelines](https://docs.datadoghq.com/security/automation_pipelines/)
- [Security Inbox](https://docs.datadoghq.com/security/security_inbox)
- [Audit Trail](https://docs.datadoghq.com/security/audit_trail/)
- [Security Research Feed](https://docs.datadoghq.com/security/research_feed)

{% callout %}
The new Cloud Security Summary shown below is in Preview. To get started, contact your Customer Success representative.
{% /callout %}

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/csm_overview_4.00fec4d033e3e684d19268f8724395b9.png?auto=format"
   alt="Cloud Security Summary in Datadog" /%}

{% alert level="info" %}
Collecting events using Cloud Security Management will affect your billing. For more information, see [Datadog Pricing](https://www.datadoghq.com/pricing/?product=cloud-security-management#products).
{% /alert %}

## Track your organization's health{% #track-your-organizations-health %}

Available for [Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/), the [security posture score](https://docs.datadoghq.com/glossary/#posture-score) helps you track your organization's overall health. The score represents the percentage of your environment that satisfies all of your active out-of-the-box cloud and infrastructure compliance rules.

Improve your organization's score by remediating misconfigurations, either by resolving the underlying issue or by muting the misconfiguration.

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/health_scores.111fd1f3759a72387217241edb949f5b.png?auto=format"
   alt="The posture score on the Cloud Security overview page tracks your organization's overall health" /%}

## Explore and remediate issues{% #explore-and-remediate-issues %}

For an overview of your Cloud Security and App and API Protection findings, sorted by importance, use the [Security Inbox](https://docs.datadoghq.com/security/security_inbox).

To get more detail, use [Findings](https://app.datadoghq.com/security/compliance) to review and remediate your organization's security findings concerning misconfigurations, vulnerabilities, and identity risks. View detailed information about a finding, including guidelines and remediation steps. [Send real-time notifications](https://docs.datadoghq.com/security/notifications/) when a threat is detected in your environment, and use tags to identify the owner of an impacted resource.

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/findings_page_2.25237b6e173a3ff6514d991aaff2e4a8.png?auto=format"
   alt="Cloud Security Findings page" /%}

## Investigate resources{% #investigate-resources %}

- Use the [Security Graph](https://docs.datadoghq.com/security/cloud_security_management/security_graph) to model your cloud environment as a relationship graph, so you can visualize and query the connections between your cloud resources. You can write queries to search for specific relationships between resources, such as publicly accessible EC2 instances that can access S3 buckets containing sensitive data, so you can proactively mitigate those infrastructure risks.
  {% image
     source="https://datadog-docs.imgix.net/images/security/csm/security_graph.33a02b53cfce68b34d33b51c2dcfb8d4.png?auto=format"
     alt="Security Graph displaying an example EC2 instance" /%}

- Use the [Resource Catalog](https://app.datadoghq.com/infrastructure/catalog) to view specific misconfigurations and threats that have been reported on the hosts and resources in your environments. For more information, see the [Resource Catalog](https://docs.datadoghq.com/infrastructure/resource_catalog) documentation.Important note for users on the following Datadog sites: app.ddog-gov.com:

Important alert (level: danger): Resource Catalog is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ().


  {% image
     source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/resource_catalog_infra_3.5b2108aaf6379e32ac67c54fcb638b49.png?auto=format"
     alt="Resource Catalog map view displaying host and cloud resources grouped by category and misconfigurations." /%}

- Use the [Cloudcraft Security Map](https://app.datadoghq.com/security/map) to visualize your resources and any misconfigurations, vulnerabilities, identity risks, or sensitive data associated with them. For more information on these overlays, see the [Cloudcraft overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/#security) documentation.

## Subscribe to weekly digest reports{% #subscribe-to-weekly-digest-reports %}

Receive a weekly summary of Cloud Security activity over the past week, including important new security issues discovered in the last seven days. Subscriptions to the weekly digest report are managed on a per user basis. To [subscribe to the weekly digest report](https://app.datadoghq.com/security/configuration/reports), you must have the `security_monitoring_signals_read` permission.

## Learn about emerging threats and vulnerabilities{% #learn-about-emerging-threats-and-vulnerabilities %}

Use the [Security Research Feed](https://app.datadoghq.com/security/feed) to stay current with the latest security developments, with content managed by Datadog's Security Research and Detection Engineering teams. For more information, see the [Security Research Feed](https://docs.datadoghq.com/security/research_feed) documentation.

## Next steps{% #next-steps %}

To get started with Cloud Security, navigate to the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page in Datadog, which has detailed steps on how to set up and configure Cloud Security. For more information, see [Setting Up Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/).

## Further reading{% #further-reading %}

- [Start tracking misconfigurations with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/)
- [Security Research Feed](https://docs.datadoghq.com/security/research_feed)
- [Elevate AWS threat detection with Stratus Red Team](https://www.datadoghq.com/blog/cyber-attack-simulation-with-stratus-red-team/)
- [Best practices for securing Kubernetes applications](https://www.datadoghq.com/blog/kubernetes-security-best-practices/)
- [Run Atomic Red Team detection tests in container environments with Datadog's Workload Security Evaluator](https://www.datadoghq.com/blog/workload-security-evaluator/)
- [Fix common cloud security risks with the Datadog Security Labs Ruleset](https://www.datadoghq.com/blog/security-labs-ruleset-launch/)
- [Best practices for application security in cloud-native environments](https://www.datadoghq.com/blog/securing-cloud-native-applications/)
- [Build sufficient security coverage for your cloud environment](https://www.datadoghq.com/blog/building-security-coverage-for-cloud-environments/)
- [Key learnings from the 2024 State of Cloud Security study](https://www.datadoghq.com/blog/cloud-security-study-learnings-2024/)
- [How Datadog Security Inbox prioritizes security risks](https://www.datadoghq.com/blog/security-inbox-prioritization/)
- [How we use Datadog for detection as code](https://www.datadoghq.com/blog/datadog-detection-as-code/)
- [Simplifying the shared responsibility model: How to meet your cloud security obligations](https://www.datadoghq.com/blog/shared-responsibility-model/)
- [Detect Amazon Bedrock misconfigurations with Datadog Cloud Security](https://www.datadoghq.com/blog/detect-bedrock-misconfigurations-cloud-security)
- [Trace exposure routes between resources with Datadog Cloud Security](https://www.datadoghq.com/blog/security-graph-attack-paths)
- [Scale compliance across global frameworks with Datadog Cloud Security](https://www.datadoghq.com/blog/datadog-cloud-security-compliance)
