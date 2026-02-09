# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning.md

---
title: Cloud Security Agentless Scanning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security > Cloud
  Security Agentless Scanning
---

# Cloud Security Agentless Scanning

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Agentless Scanning provides visibility into vulnerabilities that exist within your cloud infrastructure, without requiring you to install the Datadog Agent. Datadog recommends enabling Agentless Scanning as a first step to gain complete visibility into your cloud resources, and then installing the Datadog Agent on your core assets over time for deeper security and observability context.

## How it works{% #how-it-works %}

After [setting up Agentless scanning](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning#setup) for your resources, Datadog schedules automated scans in 12-hour intervals through [Remote Configuration](https://docs.datadoghq.com/remote_configuration). During a scan cycle, Agentless scanners gather Lambda code dependencies and create snapshots of your VM instances. With these snapshots, the Agentless scanners scan, generate, and transmit a list of packages to Datadog to check for vulnerabilities, along with Lambda code dependencies. When scans of a snapshot are completed, the snapshot is deleted. No confidential or private personal information is ever transmitted outside of your infrastructure.

If you have [Cloud Security Evaluation Filters](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters) configured, Agentless Scanning respects these filters and only scans resources that match the configured criteria.

The following diagram illustrates how Agentless Scanning works:

{% image
   source="https://datadog-docs.imgix.net/images/security/agentless_scanning/how_agentless_works.a42b95a0bfbd5a17886fb94d91545964.png?auto=format"
   alt="Diagram showing how Agentless scanning works" /%}

1. Datadog schedules a scan and sends which resources to scan through Remote Configuration.

**Note**: Scheduled scans ignore hosts that already have the Datadog Agent installed with Cloud Security enabled. Datadog schedules a continuous re-scanning of resources every 12 hours to provide up-to-date insights into potential vulnerabilities and weaknesses.

1. For Lambda functions, the scanners fetch the function's code.

1. The scanner creates snapshots of volumes used in running VM instances. These snapshots serve as the basis for conducting scans. Using the snapshots, or the code, the scanner generates a list of packages.

1. After the scan is complete, the list of packages and information related to collected hosts are transmitted to Datadog, with all other data remaining within your infrastructure. Snapshots created during the scan cycle are deleted.

1. Leveraging the collected package list along with Datadog's access to the Trivy vulnerabilities database, Datadog finds matching affected vulnerabilities in your resources and code.

**Notes**:

- The scanner operates as a separate VM instance within your infrastructure, ensuring minimal impact on existing systems and resources.
- For AWS, scanner instances automatically scale based on workload. When there are no resources to scan, scanners scale to zero to minimize cloud provider costs.
- The scanner securely collects a list of packages from your hosts without transmitting any confidential or private personal information outside your infrastructure.
- The scanner limits its use of the cloud provider API to prevent reaching any rate limit, and uses exponential backoff if needed.

## On-demand scanning{% #on-demand-scanning %}

By default, Agentless Scanning automatically scans your resources every 12 hours. You can also trigger an immediate scan of a specific resource (host, container, Lambda function, or S3 bucket) using the On-Demand Scanning API.

This is useful when you need to:

- Verify a vulnerability has been patched
- Get immediate results for newly deployed resources
- Validate security posture before production deployment

For more information, see the [On-Demand Scanning API documentation](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task).

## What data is sent to Datadog{% #what-data-is-sent-to-datadog %}

The Agentless scanner uses the OWASP [cycloneDX](https://cyclonedx.org/) format to transmit a list of packages to Datadog. No confidential or private personal information is ever transmitted outside of your infrastructure.

Datadog does **not** send:

- System and package configurations
- Encryption keys and certificates
- Logs and Audit Trails
- Sensitive business data

## Security considerations{% #security-considerations %}

Because the scanner instances grant [permissions](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/enable#prerequisites) to create and copy snapshots, and describe volumes, Datadog advises restricting access to these instances solely to administrative users.

To further mitigate this risk, Datadog implements the following security measures:

- The Datadog scanner operates *within* your infrastructure, ensuring that all data, including snapshots and list of packages, remain isolated and secure.
- All data transmission between the scanner and Datadog is encrypted using industry standard protocols (such as HTTPS) to ensure data confidentiality and integrity.
- The Datadog scanner operates under the principle of least privilege. This means that it is granted only the minimum permissions necessary to perform its intended functions effectively.
- Datadog carefully reviews and limits the permissions granted to the scanner to ensure that it can conduct scans without unnecessary access to sensitive data or resources.
- Unattended security updates are enabled on Datadog's scanner instances. This feature automates the process of installing critical security patches and updates without requiring manual intervention.
- The Datadog scanner instances are automatically rotated every 24 hours. This rotation ensures that the scanner instances are continually updated with the latest Ubuntu images.
- Access to the scanner instances is tightly controlled through the use of security groups. No inbound access to the scanner is allowed, restricting possibility to compromise the instance.
- No confidential or private personal information is ever transmitted outside of your infrastructure.

## Agentless Scanning with existing Agent installations{% #agentless-scanning-with-existing-agent-installations %}

When installed, the Datadog Agent offers real-time, deep visibility into risks and vulnerabilities that exist in your cloud workloads. It is recommended to fully install the Datadog Agent.

As a result, Agentless Scanning excludes resources from its scans that have the Datadog Agent installed and configured for [Vulnerability Management](https://app.datadoghq.com/security/csm/vm). In this way, Cloud Security offers complete visibility of your risk landscape without overriding the benefits received from installing the Datadog Agent with Vulnerability Management.

The following diagram illustrates how Agentless scanning works with existing Agent installations:

{% image
   source="https://datadog-docs.imgix.net/images/security/agentless_scanning/agentless_existing.2a666aebebb61ee648b034c5cfe2761c.png?auto=format"
   alt="Diagram showing how Agentless scanning works when the Agent is already installed with Cloud Security vulnerability management" /%}

## Cloud Storage scanning{% #cloud-storage-scanning %}

{% callout %}
##### Join the Preview!

Scanning support for Amazon S3 buckets and RDS instances in Preview. To enroll, click **Request Access**.

[Request Access](https://www.datadoghq.com/product-preview/data-security)
{% /callout %}

If you have [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner) enabled, you can catalog and classify sensitive data in your Amazon S3 buckets.

Sensitive Data Scanner scans for sensitive data by deploying [Agentless scanners](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning#setup) in your cloud environments. These scanning instances retrieve a list of all S3 buckets through [Remote Configuration](https://docs.datadoghq.com/remote_configuration), and have set instructions to scan text filesâsuch as CSVs and JSONs over time. Sensitive Data Scanner leverages its [entire rules library](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) to find matches. When a match is found, the location of the match is sent to Datadog by the scanning instance. Data stores and their files are only read in your environmentâno sensitive data is sent back to Datadog.

Along with displaying sensitive data matches, Sensitive Data Scanner surfaces any security issues detected by [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management) affecting the sensitive datastores. You can click any issue to continue triage and remediation within Cloud Security.

## Cloud service provider cost{% #cloud-service-provider-cost %}

When using Agentless Scanning, there are additional cloud provider costs for running scanners and analyzing your cloud environments.

Your cloud configuration affects your cloud provider costs. Typically, using the [recommended configuration](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/deployment_methods#recommended-configuration), these are in the range of $1 USD per scanned host per year. You should consult your cloud provider's information for exact amounts, which are subject to change without Datadog's involvement.

For large cloud workloads distributed across multiple regions, Datadog recommends setting up Agentless Scanning with Terraform to avoid cross-region networking.

## Further reading{% #further-reading %}

- [Read more about Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/vulnerabilities)
- [Set up Sensitive Data Scanner for Cloud Storage](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/cloud_storage)
