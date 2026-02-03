# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/certificate_has_expired.md

---
title: Certificate has expired
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Certificate has expired
---

# Certificate has expired

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c3831315-5ae6-4fa8-b458-3d4d5ab7a3f6`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_rest_api)

### Description{% #description %}

Expired SSL/TLS certificates should be removed from cloud resources to prevent the risk of exposing users to insecure or untrusted connections. When a resource, such as an AWS API Gateway custom domain, is configured with an expired certificate (for example, `certificate_body = file("expiredCertificate.pem")`), clients attempting to access the API will receive security warnings, and automated clients may reject the connection entirely. This vulnerability undermines the integrity and trust of the service, potentially leading to denial of service, data interception, or man-in-the-middle attacks. Regularly updating and ensuring only valid certificates are used helps maintain secure encrypted communications between clients and services.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
- name: upload a self-signed certificate2
  community.aws.aws_acm:
    certificate: "{{ lookup('file', 'validCertificate.pem' ) }}"
    privateKey: "{{ lookup('file', 'key.pem' ) }}"
    name_tag: my_cert
    region: ap-southeast-2
```

```terraform
resource "aws_api_gateway_domain_name" "example" {
  certificate_body = file("validCertificate.pem")
  domain_name     = "api.example.com"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
- name: upload a self-signed certificate
  community.aws.aws_acm:
    certificate: "{{ lookup('file', 'expiredCertificate.pem' ) }}"
    privateKey: "{{ lookup('file', 'key.pem' ) }}"
    name_tag: my_cert
    region: ap-southeast-2
```

```terraform
resource "aws_api_gateway_domain_name" "example2" {
  certificate_body = file("expiredCertificate.pem")
  domain_name     = "api.example.com"
}
```
