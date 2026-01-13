# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_anycast_ip_list.dataset.md

---
title: CloudFront Anycast IP List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Anycast IP List
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_anycast_ip_list.dataset/index.html
---

# CloudFront Anycast IP List

Provides a list of Anycast IP addresses used by Amazon CloudFront. These IPs represent the global entry points for CloudFront's content delivery network, allowing clients to connect to the nearest edge location for improved performance and availability. This resource helps identify the current set of Anycast IPs that CloudFront advertises.

```
aws.cloudfront_anycast_ip_list
```

## Fields

| Title           | ID   | Type   | Data Type                                                                     | Description |
| --------------- | ---- | ------ | ----------------------------------------------------------------------------- | ----------- |
| _key            | core | string |
| account_id      | core | string |
| anycast_ip_list | core | json   | The Anycast static IP list details.                                           |
| e_tag           | core | string | The version identifier for the current version of the Anycast static IP list. |
| tags            | core | hstore |
