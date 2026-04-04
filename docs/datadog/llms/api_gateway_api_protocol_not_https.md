# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/api_gateway_api_protocol_not_https.md

---
title: API gateway API protocol not HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > API gateway API protocol not HTTPS
---

# API gateway API protocol not HTTPS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1bcdf9f0-b1aa-40a4-b8c6-cd7785836843`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/api_gateway_api#protocol)

### Description{% #description %}

API Gateway APIs must use `HTTPS`. This rule flags `alicloud_api_gateway_api` resources where `request_config.protocol` is not set to `HTTPS`. It supports both single and indexed forms of `request_config`, and reports the resource name and attribute location.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_api_gateway_group" "apiGroup" {
  name        = "ApiGatewayGroup"
  description = "description of the api group"
}

resource "alicloud_api_gateway_api" "apiGatewayApi" {
  name        = alicloud_api_gateway_group.apiGroup.name
  group_id    = alicloud_api_gateway_group.apiGroup.id
  description = "your description"
  auth_type   = "APP"
  force_nonce_check = false

  request_config {
    protocol = "HTTPS"
    method   = "GET"
    path     = "/test/path1"
    mode     = "MAPPING"
  }

  service_type = "HTTP"

  http_service_config {
    address   = "https://apigateway-backend.alicloudapi.com:8080"
    method    = "GET"
    path      = "/web/cloudapi"
    timeout   = 12
    aone_name = "cloudapi-openapi"
  }

  request_parameters {
    name         = "aaa"
    type         = "STRING"
    required     = "OPTIONAL"
    in           = "QUERY"
    in_service   = "QUERY"
    name_service = "testparams"
  }

  stage_names = [
    "RELEASE",
    "TEST",
  ]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_api_gateway_group" "apiGroup" {
  name        = "ApiGatewayGroup"
  description = "description of the api group"
}

resource "alicloud_api_gateway_api" "apiGatewayApi" {
  name        = alicloud_api_gateway_group.apiGroup.name
  group_id    = alicloud_api_gateway_group.apiGroup.id
  description = "your description"
  auth_type   = "APP"
  force_nonce_check = false

  request_config {
    protocol = "HTTP"
    method   = "GET"
    path     = "/test/path1"
    mode     = "MAPPING"
  }

  request_config {
    protocol = "HTTP"
    method   = "GET"
    path     = "/test/path2"
    mode     = "MAPPING"
  }

  service_type = "HTTP"

  http_service_config {
    address   = "http://apigateway-backend.alicloudapi.com:8080"
    method    = "GET"
    path      = "/web/cloudapi"
    timeout   = 12
    aone_name = "cloudapi-openapi"
  }

  request_parameters {
    name         = "aaa"
    type         = "STRING"
    required     = "OPTIONAL"
    in           = "QUERY"
    in_service   = "QUERY"
    name_service = "testparams"
  }

  stage_names = [
    "RELEASE",
    "TEST",
  ]
}
```

```terraform
resource "alicloud_api_gateway_group" "apiGroup" {
  name        = "ApiGatewayGroup"
  description = "description of the api group"
}

resource "alicloud_api_gateway_api" "apiGatewayApi" {
  name        = alicloud_api_gateway_group.apiGroup.name
  group_id    = alicloud_api_gateway_group.apiGroup.id
  description = "your description"
  auth_type   = "APP"
  force_nonce_check = false

  request_config {
    protocol = "HTTP"
    method   = "GET"
    path     = "/test/path1"
    mode     = "MAPPING"
  }

  service_type = "HTTP"

  http_service_config {
    address   = "http://apigateway-backend.alicloudapi.com:8080"
    method    = "GET"
    path      = "/web/cloudapi"
    timeout   = 12
    aone_name = "cloudapi-openapi"
  }

  request_parameters {
    name         = "aaa"
    type         = "STRING"
    required     = "OPTIONAL"
    in           = "QUERY"
    in_service   = "QUERY"
    name_service = "testparams"
  }

  stage_names = [
    "RELEASE",
    "TEST",
  ]
}
```
