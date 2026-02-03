# Source: https://docs.datadoghq.com/security/default_rules/def-000-ay9.md

---
title: Private application load balancers should drop HTTP headers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Private application load balancers
  should drop HTTP headers
---

# Private application load balancers should drop HTTP headers
 
## Description{% #description %}

This control checks that private AWS Application Load Balancers (ALBs) are set to discard invalid HTTP headers. The control fails if the setting `routing.http.drop_invalid_header_fields.enabled` is false, and skips public-facing ALBs as those are covered in a separate finding. By default, ALBs do not drop invalid HTTP header values. Discarding these invalid headers is essential to prevent HTTP desynchronization attacks.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

To configure the load balancer to drop invalid header fields:

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
1. In the navigation pane, choose **Load balancers**.
1. Select an Application Load Balancer.
1. From **Actions**, choose **Edit attributes**.
1. Under **Drop Invalid Header Fields**, choose **Enable**.
1. Click **Save**.
