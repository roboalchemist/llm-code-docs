# Source: https://docs.datadoghq.com/security/default_rules/def-000-ngl.md

---
title: >-
  API Gateway REST API stages should be configured to use SSL certificates for
  backend authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateway REST API stages should be
  configured to use SSL certificates for backend authentication
---

# API Gateway REST API stages should be configured to use SSL certificates for backend authentication
 
## Description{% #description %}

This control verifies whether SSL certificates are configured for Amazon API Gateway REST API stages. These certificates are used by backend systems to confirm that incoming requests originate from API Gateway.

To enable backend systems to authenticate that requests come from API Gateway, REST API stages in API Gateway should be configured with SSL certificates.

## Remediation{% #remediation %}

To learn how to configure SSL certificates for API Gateway REST APIs, refer to the [Generate and configure an SSL certificate for backend authentication](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html) section of the API Gateway Developer Guide documentation.
