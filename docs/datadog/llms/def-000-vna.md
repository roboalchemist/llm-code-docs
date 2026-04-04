# Source: https://docs.datadoghq.com/security/default_rules/def-000-vna.md

---
title: API Gateway routes should specify an authorization type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway routes should specify an
  authorization type
---

# API Gateway routes should specify an authorization type

## Description{% #description %}

This control verifies whether Amazon API Gateway routes are configured with an authorization mechanism. The control fails if an API Gateway route lacks any form of authorization.

API Gateway offers several methods for managing and restricting access to your APIs. By setting an authorization type, you can ensure that only authorized users or systems can access your API.

## Remediation{% #remediation %}

To learn how to configure authorization for HTTP APIs, review the [Controlling and managing access to an HTTP API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control.html) section in the API Gateway Developer Guide. To configure authorization for WebSocket APIs, review the [Controlling and managing access to a WebSocket API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-control-access.html) section in the API Gateway Developer Guide.
