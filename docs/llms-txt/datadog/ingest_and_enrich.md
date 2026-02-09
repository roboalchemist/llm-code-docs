# Source: https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich.md

---
title: Ingest and Enrich
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Ingest and Enrich
---

# Ingest and Enrich

## Overview{% #overview %}

Cloud SIEM detection rules analyze logs and security data to generate security signals when threats are detected. After you have enabled Cloud SIEM, configure Datadog to ingest and enrich logs from sources that you want to monitor.

## Ingest security data{% #ingest-security-data %}

The easiest way to send data to Datadog is by using [Content Packs](https://docs.datadoghq.com/security/cloud_siem/content_packs/), which are integrations specifically designed for Cloud SIEM. Each content pack contains instructions on how to configure the integration to ingest those logs and provides information on what is included, such as:

- Detections rules
- Out-of-the-box interactive dashboards
- Parsers
- SOAR workflows

[Content packs](https://docs.datadoghq.com/security/cloud_siem/content_packs/) are available for many popular security technologies.

If you have custom logs or have a data source not listed on Cloud SIEM's [Content Pack](https://app.datadoghq.com/security/siem/content-packs) page, check whether the integration is available in Datadog's extensive [integration library](https://docs.datadoghq.com/integrations/). If it isn't available, you can send those logs as [custom logs](https://docs.datadoghq.com/logs/log_collection/) to Cloud SIEM for analysis.

## Enrich logs{% #enrich-logs %}

### Threat intelligence{% #threat-intelligence %}

Datadog provides built-in [Threat Intelligence](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-sources) for Cloud SIEM logs and also supports enriching and searching using threat intelligence indicators of compromise (IoCs) stored in Datadog reference tables. See [Bring Your Own Threat Intelligence](https://docs.datadoghq.com/security/cloud_siem/threat_intelligence#bring-your-own-threat-intelligence) for more information.

### Open Cybersecurity Framework (OCSF){% #open-cybersecurity-framework-ocsf %}

[Open Cybersecurity Framework (OCSF)](https://docs.datadoghq.com/security/cloud_siem/open_cybersecurity_schema_framework) is integrated directly into Cloud SIEM, so incoming security logs are automatically enriched with OCSF-compliant attributes through out-of-the-box pipelines.

## Further reading{% #further-reading %}

- [Getting Started with Cloud SIEM](https://docs.datadoghq.com/getting_started/security/cloud_siem/)
- [Best practices for monitoring AWS CloudTrail logs](https://www.datadoghq.com/blog/monitoring-cloudtrail-logs/)
- [Best practices for monitoring authentication logs](https://www.datadoghq.com/blog/how-to-monitor-authentication-logs/)
- [Normalize your data with the OCSF Common Data Model in Datadog Cloud SIEM](https://www.datadoghq.com/blog/ocsf-common-data-model//)
