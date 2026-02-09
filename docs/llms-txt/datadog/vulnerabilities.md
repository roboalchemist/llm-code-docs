# Source: https://docs.datadoghq.com/security/cloud_security_management/troubleshooting/vulnerabilities.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities.md

---
title: Cloud Security Vulnerabilities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud Security > Cloud Security Vulnerabilities
---

# Cloud Security Vulnerabilities

## Overview{% #overview %}

Cloud Security Vulnerabilities helps you improve your security posture and achieve compliance, by continuously scanning container images, hosts, host images, and serverless functions for vulnerabilities, from CI/CD pipelines to live production. Leveraging runtime observability, it helps you prioritize and remediate exploitable vulnerabilities in your daily workflows, all in a single view, and without any dependencies on other Datadog products.

With Cloud Security Vulnerabilities, you can manage your cloud security management strategy, all in one place:

- Create a vulnerability management program, from CI/CD pipelines to production resources
- Pass compliance audits (such as SOC2, PCI, HIPAA, CIS, and FedRamp)
- Remediate emerging vulnerabilities (0-day CVEs)

**Note**: For vulnerability management in application libraries, see [Software Composition Analysis](https://docs.datadoghq.com/security/code_security/software_composition_analysis/). For application code, see [Code Security](https://docs.datadoghq.com/security/code_security/iast/).

## Key capabilities{% #key-capabilities %}

{% dl %}

{% dt %}
Deploy using Agentless or unified Datadog Agent
{% /dt %}

{% dd %}
Quickly scan your entire infrastructure for vulnerabilities, either using Agentless, or by using the unified Datadog Agent you already have deployed.
{% /dd %}

{% dt %}
Inventory cloud resources, in real-time
{% /dt %}

{% dd %}
Inventory container images, hosts, serverless functions, and all packages deployed in your infrastructure, in real time, and export your SBOM.
{% /dd %}

{% dt %}
Detect vulnerabilities continuously
{% /dt %}

{% dd %}
Scan recent updates and newly published CVEs, across running container images from hosts and registries, host, host images, and serverless, and identify vulnerable container image layers.
{% /dd %}

{% dt %}
Prioritize exploitable vulnerabilities, using runtime observability
{% /dt %}

{% dd %}
Leverage Datadog's security scoring, which is based on CVSS, by incorporating intel from CISA KEV, EPSS, and public exploit availability. With runtime observability, you can monitor production, exposure to attacks, sensitive data processing, and privileged access.
{% /dd %}

{% dt %}
Take advantage of guided remediation
{% /dt %}

{% dd %}
See which layers are impacted, get suggestions specific to each image, and action on your vulnerability lifecycle management.
{% /dd %}

{% dt %}
Implement automation and integrations
{% /dt %}

{% dd %}
Automate the creation of Jira tickets and implement SLAs. Use Datadog's public API to export vulnerabilities, coverage, and SBOMs.
{% /dd %}

{% dt %}
Explore reports
{% /dt %}

{% dd %}
View and monitor vulnerability data in your dashboards.
{% /dd %}

{% /dl %}

## Deployment methods{% #deployment-methods %}

Get started with Cloud Security Vulnerabilities and cover your infrastructure in minutes, using:

- [Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/)
- [Unified Datadog Agent](https://docs.datadoghq.com/security/cloud_security_management/setup/agent)

You can also use both deployment methods to use the unified Datadog Agent where you already have it deployed, and Agentless elsewhere.

After you've enabled it, Datadog starts scanning your resources continuously, and starts reporting prioritized vulnerabilities in your [Cloud Security Vulnerabilities Findings page](https://app.datadoghq.com/security/csm/vm) within an hour.

Use these tables to decide which solution to start with:

| Feature                                   | Agentless | Unified Datadog Agent     |
| ----------------------------------------- | --------- | ------------------------- |
| Time to deploy across your infrastructure | Minutes   | Hours to weeks            |
| Vulnerability prioritization              | Yes       | Yes, with runtime context |
| Vulnerability scanning frequency          | 12 hours  | Real-time                 |

| Vulnerability detection scope | Agentless                                                                                                     | Unified Datadog Agent          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Host and host image           | OS packages and app packages, mapped to image                                                                 | OS packages                    |
| Container image               | OS packages and app packages, mapped to image                                                                 | OS packages                    |
| Cloud provider                | AWS, [Azure (Preview)](https://www.datadoghq.com/product-preview/agentless-vulnerability-scanning-for-azure/) | AWS, Azure, GCP, on-prem, etc. |
| Operating system              | Linux                                                                                                         | Linux, Windows                 |
| Serverless                    | AWS Lambda, AWS ECS Fargate                                                                                   | Not applicable                 |
| Container registries          | Amazon ECR                                                                                                    | Not applicable                 |

For more information on compatibility, see [Cloud Security Vulnerabilities Hosts and Containers Compatibility](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/hosts_containers_compatibility). If you need any assistance, see the [troubleshooting guide](https://docs.datadoghq.com/security/cloud_security_management/troubleshooting/vulnerabilities/), or reach out to [support@datadoghq.com](mailto:support@datadoghq.com).

## Continuously detect, prioritize, and remediate exploitable vulnerabilities{% #continuously-detect-prioritize-and-remediate-exploitable-vulnerabilities %}

The [Cloud Security Vulnerabilities Findings page](https://app.datadoghq.com/security/csm/vm) helps you investigate vulnerabilities detected across your container images, host images, running hosts, and serverless functions using filtering and grouping capabilities.

Focus on exploitable vulnerabilities first, using the Datadog Severity Score, combining the base CVSS score with many risk factors, including sensitive data, environment sensitivity, exposure to attacks, exploit availability, or threat intelligence sources.

For vulnerabilities with available fixes, the Findings page provides guided remediation steps to assist Dev and Ops teams in resolving issues more quickly and effectively. You can also triage, mute, comment, and assign vulnerabilities to manage their lifecycle.

{% image
   source="https://datadog-docs.imgix.net/images/security/vulnerabilities/csm-vm-explorer-actionability-2.63a73c19e78e6a12bba978668a76fcc5.png?auto=format"
   alt="The Cloud Security Vulnerabilities Findings page displaying a vulnerability and the actions a user can take to remediate it" /%}

In [Container Images](https://app.datadoghq.com/container-images), you can trace vulnerabilities found in an image to specific layers, so you can pinpoint and remediate your security risks faster.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/containerimages/image_layer_vulnerabilities.c455c18e8e914ad25106700478a708a4.png?auto=format"
   alt="A list of vulnerabilities associated with each layer of an image" /%}

## Automation and Jira integration{% #automation-and-jira-integration %}

Make Cloud Security Vulnerabilities part of your daily workflow by setting up [security notification rules](https://app.datadoghq.com/security/configuration/notification-rules) and [automation pipelines (in Preview)](https://www.datadoghq.com/product-preview/security-automation-pipelines/):

- Get alerted upon detection of an exploitable vulnerability for your scope
- Automatically create Jira tickets
- Configure SLAs to remediate vulnerabilities

{% image
   source="https://datadog-docs.imgix.net/images/security/vulnerabilities/csm-notifications.39b7c5bc971ffcd9703d03f71c253c42.png?auto=format"
   alt="The notification rule setup screen" /%}

## Tracking and reporting{% #tracking-and-reporting %}

Use the out-of-the-box [Cloud Security Vulnerabilities dashboard](https://app.datadoghq.com/dash/integration/csm_vulnerabilities?fromUser=true&refresh_mode=sliding&from_ts=1733323465252&to_ts=1733928265252&live=true) to track and report progress to stakeholders. Clone and modify it as needed to fit your unique needs.

{% image
   source="https://datadog-docs.imgix.net/images/security/vulnerabilities/csm-vm-reporting.cd6456235aa1a41886c4fc3fba47eeb6.png?auto=format"
   alt="The Cloud Security Vulnerabilities dashboard" /%}

## Explore infrastructure packages{% #explore-infrastructure-packages %}

The [Infrastructure Packages Catalog](https://app.datadoghq.com/security/catalog/libraries) provides a real-time inventory of all packages across hosts, host images, and container images deployed in your infrastructure. It offers an interface you can use to investigate your SBOMs, enriched with vulnerability and runtime context.

Quickly assess the impact of a critical emerging vulnerability by searching for affected package versions and identifying all of the resources that use it.

{% image
   source="https://datadog-docs.imgix.net/images/security/vulnerabilities/csm_package_explorer_3.67da3ba7367ab11b52130b61e876538b.png?auto=format"
   alt="The inventory of packages deployed in the infrastructure with vulnerability context and pivot to resources using them" /%}

## Further reading{% #further-reading %}

- [Enable SBOM collection in Cloud Security Vulnerabilities](https://docs.datadoghq.com/infrastructure/containers/container_images/#enable-sbom-collection)
- [Setting up host vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/setup/csm_enterprise/?tab=aws#hosts)
- [Viewing Container Images](https://docs.datadoghq.com/infrastructure/containers/container_images)
- [Troubleshooting Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/troubleshooting/vulnerabilities)
- [Enhance your troubleshooting workflow with Container Images in Datadog Container Monitoring](https://www.datadoghq.com/blog/datadog-container-image-view/)
