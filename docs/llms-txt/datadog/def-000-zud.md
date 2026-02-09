# Source: https://docs.datadoghq.com/security/default_rules/def-000-zud.md

---
title: API Gateway access logging should be enabled for V2 API stages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway access logging should be
  enabled for V2 API stages
---

# API Gateway access logging should be enabled for V2 API stages
 
## Description{% #description %}

This control evaluates whether access logging is enabled for a specific stage of an Amazon API Gateway V2 API.

For API Gateway API stages, it's important to have appropriate logging enabled. Logging for these stages provides comprehensive records of the requests processed by API Gateway APIs. This includes details such as backend responses from API integrations, Lambda authorizer responses, and the request ID associated with AWS integration endpoints.

## Remediation{% #remediation %}

To learn how to configure access logging for API Gateway APIs, refer to the [Set up CloudWatch API logging using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-using-console) section of the API Gateway Developer Guide documentation.
