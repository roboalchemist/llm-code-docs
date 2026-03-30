# Source: https://docs.datadoghq.com/security/default_rules/def-000-isv.md

---
title: Log entries should have log sinks configured for exporting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Log entries should have log sinks
  configured for exporting
---

# Log entries should have log sinks configured for exporting

## Description{% #description %}

It is recommended to create a sink that will export copies of all log entries. This can help aggregate logs from multiple projects and export them to a Security Information and Event Management (SIEM).

## Rationale{% #rationale %}

Log entries are held in Cloud Logging. To aggregate logs, export them to a SIEM. To keep them longer, it is recommended to set up a log sink. To export logs, create a filter that selects the log entries to export, and then choose a destination, such as Cloud Storage, BigQuery, or Cloud Pub/Sub, to which to export them. The filter and destination are held in an object called a sink. To ensure all log entries are exported to sinks, ensure that there is no filter configured for a sink. Sinks can be created in projects, organizations, folders, and billing accounts.

**Note:**

1. A sink created by these commands, exports logs to storage buckets. However, sinks can be configured to export logs to BigQuery, or Cloud Pub/Sub, or a `Custom Destination`.
1. While creating a sink, do not use the sink option `--log-filter` to ensure the sink exports all log entries.
1. A sink can be created at a folder or organization level that collects the logs of all the projects underneath, bypassing the option `--include-children` in the `gcloud` command.

### Impact{% #impact %}

There are no costs or limitations in Cloud Logging for exporting logs, but the destinations to which the logs are exported charge for storing or transmitting the log data.

### Default value{% #default-value %}

By default, there are no sinks configured.

## Finding notes{% #finding-notes %}

Currently findings are only audited at the project level. Folder and Organization level log sinks will be audited in the near future. Due to this, a `fail` finding may be generated if the log sink is configured at the folder or organization level. In this case the rule may be muted to ensure accurate Cloud Security Misconfiguration scoring.

### Manual audits may be performed using{% #manual-audits-may-be-performed-using %}

1. Go to `Logs Router` by visiting [https://console.cloud.google.com/logs/router](https://console.cloud.google.com/logs/router).
1. For every sink, click the 3-dot button for Menu options and select `View sink details`.
1. Ensure there is at least one sink with an `empty` Inclusion filter.
1. Additionally, ensure that the resource configured as `Destination` exists.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Logs Router page by visiting [https://console.cloud.google.com/logs/router](https://console.cloud.google.com/logs/router).
1. Click **CREATE SINK**.
1. Fill out the fields for the Sink details sections.
1. Select **Cloud Logging bucket** in the Select sink destination dropdown menu.
1. Select a log bucket in the Sink destination drop down menu.
1. If an inclusion filter is not provided for this sink, all ingested logs will be routed to the destination provided above. This may result in higher than expected resource usage.
1. Click **Create Sink**.

### From the command line{% #from-the-command-line %}

1. To create a sink to export all log entries in a Google Cloud Storage bucket:
   ```
   gcloud logging sinks create <sink-name>
   storage.googleapis.com/DESTINATION_BUCKET_NAME
   ```
1. Sinks can be created for a folder or organization, which will include all projects.
   ```
   gcloud logging sinks create <sink-name>
   storage.googleapis.com/DESTINATION_BUCKET_NAME --include-children -- folder=FOLDER_ID | --organization=ORGANIZATION_ID
   ```

## References{% #references %}

1. [https://cloud.google.com/logging/docs/reference/tools/gcloud-logging](https://cloud.google.com/logging/docs/reference/tools/gcloud-logging)
1. [https://cloud.google.com/logging/quotas](https://cloud.google.com/logging/quotas)
1. [https://cloud.google.com/logging/docs/routing/overview](https://cloud.google.com/logging/docs/routing/overview)
1. [https://cloud.google.com/logging/docs/export/using_exported_logs](https://cloud.google.com/logging/docs/export/using_exported_logs)
1. [https://cloud.google.com/logging/docs/export/configure_export_v2](https://cloud.google.com/logging/docs/export/configure_export_v2)
1. [https://cloud.google.com/logging/docs/export/aggregated_exports](https://cloud.google.com/logging/docs/export/aggregated_exports)
1. [https://cloud.google.com/sdk/gcloud/reference/beta/logging/sinks/list](https://cloud.google.com/sdk/gcloud/reference/beta/logging/sinks/list)
