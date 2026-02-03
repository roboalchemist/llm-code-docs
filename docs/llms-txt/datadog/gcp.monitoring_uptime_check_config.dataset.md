# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.monitoring_uptime_check_config.dataset.md

---
title: Uptime Check Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Uptime Check Configuration
---

# Uptime Check Configuration

Uptime Check Configuration in Google Cloud is used to monitor the availability and performance of applications or services. It regularly tests endpoints such as URLs, VMs, or load balancers from multiple geographic locations to ensure they are reachable and responsive. Results can trigger alerts when downtime or latency issues are detected.

```
gcp.monitoring_uptime_check_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| checker_type         | core | string        | The type of checkers to use to execute the Uptime check.                                                                                                                                                                                                                                                                                                                                                          |
| content_matchers     | core | json          | The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.                                                              |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | A human-friendly name for the Uptime check configuration. The display name should be unique within a Cloud Monitoring Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.                                                                                                                                                                                            |
| http_check           | core | json          | Contains information needed to make an HTTP or HTTPS check.                                                                                                                                                                                                                                                                                                                                                       |
| internal_checkers    | core | json          | The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig.                                                                                                                                                                                           |
| is_internal          | core | bool          | If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false.                                                                                                                               |
| labels               | core | array<string> |
| monitored_resource   | core | json          | The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: uptime_url, gce_instance, gae_app, aws_ec2_instance, aws_elb_load_balancer k8s_service servicedirectory_service cloud_run_revision                                                                                                 |
| name                 | core | string        | Identifier. A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response. |
| organization_id      | core | string        |
| parent               | core | string        |
| period               | core | string        | How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s.                                                                                                                                                                                                             |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_group       | core | json          | The group resource associated with the configuration.                                                                                                                                                                                                                                                                                                                                                             |
| resource_name        | core | string        |
| selected_regions     | core | array<string> | The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.                                                                                            |
| synthetic_monitor    | core | json          | Specifies a Synthetic Monitor to invoke.                                                                                                                                                                                                                                                                                                                                                                          |
| tags                 | core | hstore_csv    |
| tcp_check            | core | json          | Contains information needed to make a TCP check.                                                                                                                                                                                                                                                                                                                                                                  |
| timeout              | core | string        | The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.                                                                                                                                                                                                                                                                                                      |
| user_labels          | core | hstore        | User-supplied key/value data to be used for organizing and identifying the UptimeCheckConfig objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.                                                   |
| zone_id              | core | string        |
