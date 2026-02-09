# Source: https://docs.datadoghq.com/security/default_rules/def-000-e0t.md

---
title: API Gateway stage REST API should have AWS X-Ray tracing enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway stage REST API should have
  AWS X-Ray tracing enabled
---

# API Gateway stage REST API should have AWS X-Ray tracing enabled
 
## Description{% #description %}

This check verifies if active tracing is enabled for AWS X-Ray on your Amazon API Gateway REST API stages. Active tracing allows for quicker identification of performance issues in your infrastructure, which could potentially impact API availability. It also provides real-time metrics on user requests flowing through your API Gateway operations and connected services.

## Remediation{% #remediation %}

For detailed instructions on how to enable X-Ray active tracing for API Gateway REST API operations, see [Amazon API Gateway active tracing support for AWS X-Ray in the AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-apigateway.html).
