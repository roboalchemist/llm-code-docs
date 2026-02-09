# Source: https://docs.datadoghq.com/security/default_rules/def-000-uad.md

---
title: API Gateway execution logging should be enabled for WebSocket APIs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway execution logging should be
  enabled for WebSocket APIs
---

# API Gateway execution logging should be enabled for WebSocket APIs
 
## Description{% #description %}

This control evaluates whether execution logging is enabled for all stages of an Amazon API Gateway WebSocket API. The control will pass only if the following conditions are true.

- The logging level must be set to either `ERROR` or `INFO` in `default_route_settings`.
- If per-route logging has been configured in `route_settings`, the logging level for every route must also be set to either `ERROR` or `INFO`.

For API Gateway WebSocket API stages, it's important to have appropriate logging enabled. Logging for these stages provides comprehensive records of the requests processed by API Gateway WebSocket APIs. This includes details such as backend responses from API integrations, Lambda authorizer responses, and the requestId associated with AWS integration endpoints.

## Remediation{% #remediation %}

To learn how to configure execution logging for API Gateway WebSocket APIs, refer to the [Set up CloudWatch API logging using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-using-console) section of the API Gateway Developer Guide documentation.
