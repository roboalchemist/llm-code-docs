# Source: https://docs.datadoghq.com/security/default_rules/def-000-n0m.md

---
title: CloudFront distributions should be configured for origin failover
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distributions should be
  configured for origin failover
---

# CloudFront distributions should be configured for origin failover
 
## Description{% #description %}

This assessment verifies if an Amazon CloudFront distribution has been set up with an origin grouping that contains at least two origins.

Using CloudFront origin failover has the potential to enhance system reliability. In the event that the primary origin is inaccessible or returns certain HTTP response status codes, origin failover automatically redirects traffic to a secondary origin.

## Remediation{% #remediation %}

For instructions on setting up origin failover for a CloudFront distribution, refer to [Creating an origin group](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html#concept_origin_groups.creating) in the Amazon CloudFront Developer Guide.
