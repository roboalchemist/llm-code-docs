# Source: https://docs.datadoghq.com/account_management/guide/hourly-usage-migration.md

---
title: Migrating from the V1 Hourly Usage APIs to V2
description: >-
  Learn how to migrate from V1 hourly usage endpoints to the consolidated V2 API
  with product families, JSON:API format, pagination, and multi-organization
  support.
breadcrumbs: >-
  Docs > Account Management > Account Management Guides > Migrating from the V1
  Hourly Usage APIs to V2
source_url: https://docs.datadoghq.com/guide/hourly-usage-migration/index.html
---

# Migrating from the V1 Hourly Usage APIs to V2

## Summary{% #summary %}

On February 1, 2025, the individual hourly usage by product endpoints will be deprecated in favor of the v2 [hourly usage by product family API](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family).

Users of the v1 APIs should recognize familiar concepts in the consolidated v2 hourly usage API, just represented in a slightly different format.

The most notable differences between the v1 API and the v2 API are that the v2 API:

- Consolidates all products to one endpoint
- Follows the JSON:API standard
- Is paginated
- Can return data for multiple organizations and regions per request

Each difference is discussed in further detail in the following sections.

## Consolidated Product Families{% #consolidated-product-families %}

The v2 API introduces the concepts of product family and usage type. Product families are groupings of one or more usage types. Usage types are usage measurements for a given organization and time period. The `all` product family retrieves the usage for all product families or you can filter by specific product families.

This list below shows how the product families and usage types map to the v1 hourly usage endpoints. Usage type and datapoint are the same, except where explicitly noted:

{% dl %}

{% dt %}
ENDPOINT | PRODUCT FAMILY
{% /dt %}

{% dt %}
`<base_url>/api/v1/usage/hosts` | infra_hosts
{% /dt %}

{% dd %}
`agent_host_count`
{% /dd %}

{% dd %}
`alibaba_host_count`
{% /dd %}

{% dd %}
`apm_azure_app_service_host_count`
{% /dd %}

{% dd %}
`apm_host_count`
{% /dd %}

{% dd %}
`aws_host_count`
{% /dd %}

{% dd %}
`azure_host_count`
{% /dd %}

{% dd %}
`container_count`
{% /dd %}

{% dd %}
`gcp_host_count`
{% /dd %}

{% dd %}
`heroku_host_count`
{% /dd %}

{% dd %}
`host_count`
{% /dd %}

{% dd %}
`infra_azure_app_service`
{% /dd %}

{% dd %}
`opentelemetry_host_count`
{% /dd %}

{% dd %}
`vsphere_host_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/logs` | logs
{% /dt %}

{% dd %}
`billable_ingested_bytes`
{% /dd %}

{% dd %}
`indexed_events_count`
{% /dd %}

{% dd %}
`ingested_events_bytes`
{% /dd %}

{% dd %}
`logs_live_indexed_count`
{% /dd %}

{% dd %}
`logs_live_ingested_bytes`
{% /dd %}

{% dd %}
`logs_rehydrated_indexed_count`
{% /dd %}

{% dd %}
`logs_rehydrated_ingested_bytes`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/timeseries` | timeseries
{% /dt %}

{% dd %}
`num_custom_input_timeseries`
{% /dd %}

{% dd %}
`num_custom_output_timeseries`
{% /dd %}

{% dd %}
`num_custom_timeseries`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/indexed-spans` | indexed_spans
{% /dt %}

{% dd %}
`indexed_events_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/synthetics`
{% /dt %}

{% dd %}
Deprecated. See synthetics_api and synthetics_browser for synthetics usage
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/synthetics_api` | synthetics_api
{% /dt %}

{% dd %}
`check_calls_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/synthetics_browser` | synthetics_browser
{% /dt %}

{% dd %}
`browser_check_calls_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/fargate` | fargate
{% /dt %}

{% dd %}
`avg_profiled_fargate_tasks`
{% /dd %}

{% dd %}
`tasks_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/aws_lambda` | serverless
{% /dt %}

{% dd %}
`func_count`
{% /dd %}

{% dd %}
`invocations_sum`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/rum_sessions` | rum
{% /dt %}

{% dd %}
See [RUM Migration Guide for full mapping instructions.](https://docs.datadoghq.com/account_management/guide/relevant-usage-migration/#rum)
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/network_hosts` | network_hosts
{% /dt %}

{% dd %}
`host_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/network_flows` | network_flows
{% /dt %}

{% dd %}
`indexed_events_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/logs-by-retention` | indexed_logs
{% /dt %}

{% dd %}
**Note:** The usage type and datapoint are separate for this URL, because the retention value is included in the usage type.
{% /dd %}

{% dd %}
**Usage Type:** `logs_indexed_events_<retention>_count` **Datapoint:** `indexed_events_count`
{% /dd %}

{% dd %}
**Usage Type:** `logs_live_indexed_events_<retention>_count` **Datapoint:** `live_indexed_events_count`
{% /dd %}

{% dd %}
**Usage Type:** `logs_rehydrated_indexed_events_<retention>_count` **Datapoint:** `rehydrated_indexed_events_count`
{% /dd %}

{% dd %}
**Usage Type:** In `usage_type`, replace `<retention>` with one of : `3_day`, `7_day`, `15_day`, `30_day`, `45_day`, `60_day`, `90_day`, `180_day`, `365_day`, `custom` **Datapoint:** `retention`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/analyzed_logs` | analyzed_logs
{% /dt %}

{% dd %}
`analyzed_logs`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/snmp` | snmp
{% /dt %}

{% dd %}
`snmp_devices`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/profiling` | profiling
{% /dt %}

{% dd %}
`host_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/ingested-spans` | ingested_spans
{% /dt %}

{% dd %}
`ingested_events_bytes`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/incident-management` | incident_management
{% /dt %}

{% dd %}
`monthly_active_users`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/iot` | iot
{% /dt %}

{% dd %}
`iot_device_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/cspm` | cspm
{% /dt %}

{% dd %}
`aas_host_count`
{% /dd %}

{% dd %}
`azure_host_count`
{% /dd %}

{% dd %}
`compliance_host_count`
{% /dd %}

{% dd %}
`container_count`
{% /dd %}

{% dd %}
`host_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/cws` | cws
{% /dt %}

{% dd %}
`cws_container_count`
{% /dd %}

{% dd %}
`cws_host_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/dbm` | dbm
{% /dt %}

{% dd %}
`dbm_host_count`
{% /dd %}

{% dd %}
`dbm_queries_count`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/sds` | sds
{% /dt %}

{% dd %}
`logs_scanned_bytes`
{% /dd %}

{% dd %}
`total_scanned_bytes`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/ci-app` | ci_app
{% /dt %}

{% dd %}
`ci_pipeline_indexed_spans`
{% /dd %}

{% dd %}
`ci_test_indexed_spans`
{% /dd %}

{% dd %}
`ci_visibility_pipeline_committers`
{% /dd %}

{% dd %}
`ci_visibility_test_committers`
{% /dd %}

{% dt %}
`<base_url>/api/v1/usage/online-archive` | online_archive
{% /dt %}

{% dd %}
`online_archive_events_count`
{% /dd %}

{% dt %}
`<base_url>/api/v2/usage/lambda_traced_invocations` | lambda_traced_invocations
{% /dt %}

{% dd %}
`lambda_traced_invocations_count`
{% /dd %}

{% dt %}
`<base_url>/api/v2/usage/application_security` | application_security
{% /dt %}

{% dd %}
`app_sec_host_count`
{% /dd %}

{% dt %}
`<base_url>/api/v2/usage/observability_pipelines` | observability_pipelines
{% /dt %}

{% dd %}
`observability_pipelines_bytes_processed`
{% /dd %}

{% /dl %}

## JSON:API Compliant Format{% #jsonapi-compliant-format %}

Response bodies and parameter names conform to the [JSON:API specification](https://jsonapi.org/format/). All data available in the v1 APIs is still available. See the example below of the mapping from the v1 hosts API to the v2 hourly usage API.

### V1 API: Get hourly usage for hosts and containers{% #v1-api-get-hourly-usage-for-hosts-and-containers %}

#### Request{% #request %}

`https://api.datadoghq.com/api/v1/usage/hosts?start_hr=2022-06-01T00&end_hr=2022-06-01T01`

##### Notes{% #notes %}

- Product is an element of the path `hosts`.
- Time bounds are controlled by the parameters `start_hr` and `end_hr`.

#### Response{% #response %}

```json
{
  "usage": [
    {
      "agent_host_count": 1,
      "alibaba_host_count": 2,
      "apm_azure_app_service_host_count": 3,
      "apm_host_count": 4,
      "aws_host_count": 5,
      "azure_host_count": 6,
      "container_count": 7,
      "gcp_host_count": 8,
      "heroku_host_count": 9,
      "host_count": 10,
      "infra_azure_app_service": 11,
      "opentelemetry_host_count": 12,
      "vsphere_host_count": 13,
      "hour": "2022-06-01T00",
      "org_name": "Customer Inc",
      "public_id": "abc123"
    }
  ]
}
```

##### Notes{% #notes-1 %}

- Usage for each hour is represented as an object in the usage array.
- Usage types are keys in the object, and measured usage for those usage types are the corresponding values.
- Hour, organization name, and public ID are also fields in the object.

### V2 API: Get hourly usage by product family{% #v2-api-get-hourly-usage-by-product-family %}

#### Request{% #request-1 %}

`https://api.datadoghq.com/api/v2/usage/hourly_usage?filter[timestamp][start]=2022-06-01T00&filter[timestamp][end]=2022-06-01T01&filter[product_families]=infra_hosts`

##### Notes{% #notes-2 %}

- Product is passed as a query parameter `filter[product_families]=infra_hosts`.
- Time bounds are controlled by the parameters `filter[timestamp][start]` and `filter[timestamp][end]`.

#### Response{% #response-1 %}

```json
{
  "data": [
    {
      "attributes": {
        "org_name": "Customer Inc",
        "public_id": "abc123",
        "timestamp": "2022-06-01T00:00:00+00:00",
        "region": "us",
        "measurements": [
          {
            "usage_type": "agent_host_count",
            "value": 1
          },
          {
            "usage_type": "alibaba_host_count",
            "value": 2
          },
          {
            "usage_type": "apm_azure_app_service_host_count",
            "value": 3
          },
          {
            "usage_type": "apm_host_count",
            "value": 4
          },
          {
            "usage_type": "aws_host_count",
            "value": 5
          },
          {
            "usage_type": "azure_host_count",
            "value": 6
          },
          {
            "usage_type": "container_count",
            "value": 7
          },
          {
            "usage_type": "gcp_host_count",
            "value": 8
          },
          {
            "usage_type": "heroku_host_count",
            "value": 9
          },
          {
            "usage_type": "host_count",
            "value": 10
          },
          {
            "usage_type": "infra_azure_app_service",
            "value": 11
          },
          {
            "usage_type": "opentelemetry_host_count",
            "value": 12
          },
          {
            "usage_type": "vsphere_host_count",
            "value": 13
          }
        ],
        "product_family": "infra_hosts"
      },
      "type": "usage_timeseries",
      "id": "ec3e0318b98d15c2ae8125e8bda0ff487cd08d80b120fb340c9322ee16f28629"
    }
  ]
}
```

#### Notes{% #notes-3 %}

- Objects in the data array represent hourly usage, for each product and each organization.
  - V1 APIs did not support multiple products or multiple organizations per request.
- Usage measurements are represented in the nested `measurements` array.
- Usage measurement objects have the fields `usage_type` and `value`.
- `hour`, `org_name`, and `public_id` are also fields in the `attributes` object.

## Pagination{% #pagination %}

The v2 hourly usage API is paginated. Responses are limited to 500 pages, with a page containing usage data for one product family, for one hour, for one organization. Pagination allows the API to support other features such as multiple products per request, multiple organizations per request, and unlimited time ranges.

If a result has more pages, the record ID of the next page is returned in the field `meta.pagination.next_record_id`. Clients should then pass that id in the parameter `pagination[next_record_id]`. There are no more pages to retrieve when the `meta.pagination.next_record_id` field is not set.

### Code example{% #code-example %}

```
response := GetHourlyUsage(start_time, end_time, product_families)
cursor := response.metadata.pagination.next_record_id
WHILE cursor != null BEGIN
sleep(5 seconds)  # Avoid running into rate limit
response := GetHourlyUsage(start_time, end_time, product_families, next_record_id=cursor)
cursor := response.metadata.pagination.next_record_id
END
```

## Multi-organization responses{% #multi-organization-responses %}

The v2 API supports retrieving usage data for all of your child organizations in all regions in one request. Use the parameter `filter[include_descendants]` to request data for child organizations.

### Further Reading{% #further-reading %}

- [Plan and Usage Settings](https://docs.datadoghq.com/account_management/plan_and_usage/)
