# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_hosted_zone.dataset.md

---
title: "Route\_53 Hosted Zone"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Hosted Zone"
---

# Route 53 Hosted Zone

A Route 53 Hosted Zone is a container for DNS records that define how traffic is routed for a domain and its subdomains. It represents the authoritative DNS configuration for a domain, allowing you to manage records such as A, CNAME, MX, and others. Hosted zones can be public, for domains accessible on the internet, or private, for domains used within an Amazon VPC.

```
aws.route53_hosted_zone
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                        | Description |
| ------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| caller_reference          | core | string     | The value that you specified for CallerReference when you created the hosted zone.                                                                                                                                                                                               |
| config                    | core | json       | A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don't appear in the response.                                                                      |
| delegation_set            | core | json       | A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.                                                                                                                                                                                        |
| dnssec                    | core | json       |
| hosted_zone_arn           | core | string     |
| id                        | core | string     | The ID that Amazon Route 53 assigned to the hosted zone when you created it.                                                                                                                                                                                                     |
| linked_service            | core | json       | If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Route 53.                                                                                       |
| name                      | core | string     | The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar. For information about how to specify characters other than a-z, 0-9, and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone. |
| resource_record_set_count | core | int64      | The number of resource record sets in the hosted zone.                                                                                                                                                                                                                           |
| tags                      | core | hstore_csv |
| vpcs                      | core | json       | A complex type that contains information about the VPCs that are associated with the specified hosted zone.                                                                                                                                                                      |
