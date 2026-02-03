# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkmanagement_connectivity_test.dataset.md

---
title: Connectivity Test
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connectivity Test
---

# Connectivity Test

Connectivity Test in Google Cloud is a Network Intelligence Center tool that verifies and diagnoses network connectivity between two endpoints. It simulates packet flow across your Google Cloud and hybrid networks, identifying configuration or routing issues. This helps ensure that network paths are correctly set up and that traffic can reach its intended destination securely and efficiently.

```
gcp.networkmanagement_connectivity_test
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| --------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| ancestors                   | core | array<string> |
| bypass_firewall_checks      | core | bool          | Whether the analysis should skip firewall checking. Default value is false.                                                                                                                                                                                                                                                                                                                         |
| create_time                 | core | timestamp     | Output only. The time the test was created.                                                                                                                                                                                                                                                                                                                                                         |
| datadog_display_name        | core | string        |
| description                 | core | string        | The user-supplied description of the Connectivity Test. Maximum of 512 characters.                                                                                                                                                                                                                                                                                                                  |
| destination                 | core | json          | Required. Destination specification of the Connectivity Test. You can use a combination of destination IP address, URI of a supported endpoint, project ID, or VPC network to identify the destination location. Reachability analysis proceeds even if the destination location is ambiguous. However, the test result might include endpoints or use a destination that you don't intend to test. |
| gcp_display_name            | core | string        | Output only. The display name of a Connectivity Test.                                                                                                                                                                                                                                                                                                                                               |
| gcp_source                  | core | json          | Required. Source specification of the Connectivity Test. You can use a combination of source IP address, URI of a supported endpoint, project ID, or VPC network to identify the source location. Reachability analysis might proceed even if the source location is ambiguous. However, the test result might include endpoints or use a source that you don't intend to test.                     |
| labels                      | core | array<string> | Resource labels to represent user-provided metadata.                                                                                                                                                                                                                                                                                                                                                |
| name                        | core | string        | Identifier. Unique name of the resource using the form: `projects/{project_id}/locations/global/connectivityTests/{test_id}`                                                                                                                                                                                                                                                                        |
| organization_id             | core | string        |
| parent                      | core | string        |
| probing_details             | core | json          | Output only. The probing details of this test from the latest run, present for applicable tests only. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.                                                                                                                                                              |
| project_id                  | core | string        |
| project_number              | core | string        |
| protocol                    | core | string        | IP Protocol of the test. When not provided, "TCP" is assumed.                                                                                                                                                                                                                                                                                                                                       |
| reachability_details        | core | json          | Output only. The reachability details of this test from the latest run. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.                                                                                                                                                                                            |
| region_id                   | core | string        |
| related_projects            | core | array<string> | Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries.                                                                                                                                                                                                                                                           |
| resource_name               | core | string        |
| return_reachability_details | core | json          | Output only. The reachability details of this test from the latest run for the return path. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.                                                                                                                                                                        |
| round_trip                  | core | bool          | Whether run analysis for the return path from destination to source. Default value is false.                                                                                                                                                                                                                                                                                                        |
| tags                        | core | hstore_csv    |
| update_time                 | core | timestamp     | Output only. The time the test's configuration was updated.                                                                                                                                                                                                                                                                                                                                         |
| zone_id                     | core | string        |
