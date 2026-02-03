# Source: https://docs.datadoghq.com/security/default_rules/def-000-0fh.md

---
title: API Gateway execution logging should be enabled for REST APIs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway execution logging should be
  enabled for REST APIs
---

# API Gateway execution logging should be enabled for REST APIs
 
## Description{% #description %}

This control evaluates whether execution logging is enabled for all stages of an Amazon API Gateway REST API. The control will pass only if the logging level has been configured for each API method within the API stage. The logging level must be set to either `ERROR` or `INFO`.

For API Gateway REST API stages, it's important to have appropriate logging enabled. Logging for these stages provides comprehensive records of the requests processed by API Gateway REST APIs. This includes details such as backend responses from API integrations, Lambda authorizer responses, and the requestId associated with AWS integration endpoints.

## Remediation{% #remediation %}

To learn how to configure execution logging for API Gateway REST APIs, refer to the [Set up CloudWatch API logging using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-using-console) section of the API Gateway Developer Guide documentation.
