# Source: https://docs.datadoghq.com/security/default_rules/def-000-vq1.md

---
title: API Gateway REST API cache data should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway REST API cache data should
  be encrypted at rest
---

# API Gateway REST API cache data should be encrypted at rest

## Description{% #description %}

This control evaluates whether execution logging is enabled for all stages of an Amazon API Gateway REST API. The control passes only if the logging level has been configured for each API method within the API stage. The logging level must be set to either `ERROR` or `INFO`.

For API Gateway REST API stages, it's important to have appropriate logging enabled. Logging for these stages provides comprehensive records of the requests processed by API Gateway REST APIs. This includes details such as backend responses from API integrations, Lambda authorizer responses, and the request ID associated with AWS integration endpoints.

## Remediation{% #remediation %}

To learn how to configure execution logging for API Gateway REST APIs, refer to the [Set up CloudWatch API logging using the API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-using-console) section of the API Gateway Developer Guide documentation.
