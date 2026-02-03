# Source: https://docs.datadoghq.com/security/sensitive_data_scanner.md

---
title: Sensitive Data Scanner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Sensitive Data Scanner
---

# Sensitive Data Scanner

## Overview{% #overview %}

Sensitive data, such as credit card numbers, API keys, IP addresses, and personally identifiable information (PII) are often leaked unintentionally, which can expose your organization to security and compliance risks. Sensitive data can be found in your telemetry data, such as application logs, APM spans, RUM events, events from Event Management. It can also be unintentionally moved to cloud storage resources when engineering teams move their workloads to the cloud. Datadog's Sensitive Data Scanner can help prevent sensitive data leaks and limit non-compliance risks by discovering, classifying, and optionally redacting sensitive data.

**Note**: Datadog's tools and policies comply with PCI v4.0. For more information, see [PCI DSS Compliance](https://docs.datadoghq.com/data_security/pci_compliance/).

## Scan telemetry data{% #scan-telemetry-data %}

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/telemetry_data_issues.a481f2e95cd595163bd6b2e1dc1738db.png?auto=format"
   alt="Five different sensitive findings detected where two have critical priority, one has medium priority, and two are info." /%}

Sensitive Data Scanner can scan your data in the cloud or within your environment.

### In the Cloud{% #in-the-cloud %}

With Sensitive Data Scanner in the Cloud, you submit logs and events to the Datadog backend, so the data leaves your environment before it gets redacted. The logs and events are scanned and redacted in the Datadog backend during processing, so sensitive data is redacted before events are indexed and shown in the Datadog UI.

The data that can be scanned and redacted are:

- **Logs**: All structured and unstructured log content, including log message and attribute values
- **APM**: Span attribute values only
- **RUM**: Event attribute values only
- **Events**: Event attribute values only

Optionally, sampling rates can be set between 10% and 99% for each product. This helps manage costs when you first get started by reducing the amount of data that gets scanned for sensitive information.

For each [scanning rule](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/), one of the following actions can be applied to matched sensitive data:

- **Redact**: Replace the entire matched data with a single token that you choose, such as `[sensitive_data]`.
- **Partially redact**: Replace a specific portion of all matching values.
- **Hash**: Replace the entire matched data with a non-reversible unique identifier.
- **Mask** (available for logs only): Obfuscate all matching values. Users with the `Data Scanner Unmask` permission can de-obfuscate (unmask) and view this data in Datadog. See [Mask action](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data/?tab=logs#mask-action) for more information.

**Note**: When scanning sampled data, you will not be able to select actions that obfuscate the data it scans.

To use Sensitive Data Scanner, set up a scanning group to define what data to scan and then set up scanning rules to determine what sensitive information to match within the data. For scanning rules you can:

- Add predefined scanning rules from Datadog's [Scanning Rule Library](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/). These rules detect common patterns such as email addresses, credit card numbers, API keys, authorization tokens, network and device information, and more.
- [Create your own rules using regex patterns](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules/).

See [Set Up Sensitive Data Scanner for Telemetry Data](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data/) for setup details.

### In your environment{% #in-your-environment %}

Use [Observability Pipelines](https://docs.datadoghq.com/observability_pipelines/) to collect and process your logs within your environment, and then route the data to their downstream integrations. When you set up a pipeline in Observability Pipelines, add the [Sensitive Data Scanner processor](https://docs.datadoghq.com/observability_pipelines/processors/sensitive_data_scanner) to redact sensitive data in your logs before they leave your premises. You can add predefined scanning rules from the Rule Library, such as email addresses, credit card numbers, API keys, authorization tokens, IP addresses, and more. You can also create your own rules using regex patterns.

See [Set Up Pipelines](https://docs.datadoghq.com/observability_pipelines/configuration/set_up_pipelines/) for more information.

## Scan cloud storage{% #scan-cloud-storage %}

{% callout %}
##### Join the Preview!

Scanning support for Amazon S3 buckets and RDS instances is in Preview. To enroll, click **Request Access**.

[Request Access](https://www.datadoghq.com/product-preview/data-security)
{% /callout %}

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/cloud_storage_issues.208a58fa3bb42b256d1484182c05510c.png?auto=format"
   alt="The Findings page's datastore section with three Amazon S3 findings" /%}

If you have Sensitive Data Scanner enabled, you can catalog and classify sensitive data in your Amazon S3 buckets. **Note**: Sensitive Data Scanner does not redact sensitive data in your cloud storage resources.

Sensitive Data Scanner scans for sensitive data by deploying [Agentless scanners](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning) in your cloud environments. These scanning instances retrieve a list of all S3 buckets through [Remote Configuration](https://docs.datadoghq.com/remote_configuration), and have set instructions to scan text filesâsuch as CSVs and JSONs over time.

Sensitive Data Scanner leverages its [entire rules library](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) to find matches. When a match is found, the location of the match is sent to Datadog by the scanning instance. **Note**: Data stores and their files are only read in your environmentâno sensitive data that was scanned is sent back to Datadog.

Along with displaying sensitive data matches, Sensitive Data Scanner surfaces any security issues detected by [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management) affecting the sensitive data stores. You can click any issue to continue triage and remediation within Cloud Security.

See [Set up Sensitive Data Scanner for Cloud Storage](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/cloud_storage/) for setup details.

## Investigate sensitive data findings{% #investigate-sensitive-data-findings %}

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/findings_20251014.0e5b31c352b7904297ad52541050f41d.png?auto=format"
   alt="The Findings page showing an overview of sensitive findings broken down by priority" /%}

Use the [Findings page](https://app.datadoghq.com/organization-settings/sensitive-data-scanner) to see details of sensitive data findings identified by your scanning rules. These details include:

- The specific scanning rule that detected the matches, so that you can determine which rules to modify as needed.
- The scanning group in which the finding has occurred, so that you can determine the blast radius of any leaks.
- The number of events associated with the finding to help you gauge its scope and severity.
- A graph of the events associated with the finding to help you pinpoint when a finding started and see how it has progressed.
- Related cases created for the finding.

See [Investigate Sensitive Data Findings](https://docs.datadoghq.com/security/sensitive_data_scanner/guide/investigate_sensitive_data_findings/) for more information on triaging sensitive data using the Findings page.

## Review sensitive data trends{% #review-sensitive-data-trends %}

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/sdslight.577d50b373d738e1e85044ccb6c8d15a.png?auto=format"
   alt="Sensitive Data Scanner Overview dashboard" /%}

When Sensitive Data Scanner is enabled, an [out-of-the-box dashboard](https://app.datadoghq.com/dash/integration/sensitive_data_scanner) summarizing sensitive data findings is automatically installed in your account. To access this dashboard, navigate to **Dashboards** > **Dashboards List** and search for "Sensitive Data Scanner Overview".

## Further reading{% #further-reading %}

- [Set up Sensitive Data Scanner for Telemetry Data](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data)
- [Set up Sensitive Data Scanner for Cloud Storage](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/cloud_storage)
- [CoTerm: Monitor terminal sessions and sensitive activities on local and remote systems](https://docs.datadoghq.com/coterm)
- [Reducing data related risks](https://docs.datadoghq.com/data_security/)
- [Discover, triage, and remediate sensitive data issues at scale with Sensitive Data Scanner](https://www.datadoghq.com/blog/scaling-sensitive-data-scanner/)
- [Build a modern data compliance strategy with Datadog's Sensitive Data Scanner](https://www.datadoghq.com/blog/sensitive-data-scanner/)
- [Best practices for sensitive data management](https://www.datadoghq.com/blog/sensitive-data-management-best-practices/)
- [Discover sensitive data in your cloud data stores with Data Security](https://www.datadoghq.com/blog/data-security/)
- [How companies subject to HIPAA requirements manage sensitive data with Datadog](https://www.datadoghq.com/blog/hipaa-compliance-sensitive-data-scanner/)
- [How financial services companies discover, classify, and manage sensitive data with Datadog](https://www.datadoghq.com/blog/sds-dlp-for-financial-service-companies/)
- [How insurance companies discover, classify, and act on sensitive data risks with Datadog](https://www.datadoghq.com/blog/sds-for-insurance-companies/)
- [Gain visibility into Strands Agents workflows with Datadog LLM Observability](https://www.datadoghq.com/blog/llm-aws-strands)
- [Simplify log collection and aggregation for MSSPs with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-mssp)
- [Scale compliance across global frameworks with Datadog Cloud Security](https://www.datadoghq.com/blog/datadog-cloud-security-compliance)
