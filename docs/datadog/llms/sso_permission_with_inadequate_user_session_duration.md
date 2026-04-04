# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sso_permission_with_inadequate_user_session_duration.md

---
title: SSO permission with inadequate user session duration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SSO permission with inadequate user session
  duration
---

# SSO permission with inadequate user session duration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ce9dfce0-5fc8-433b-944a-3b16153111a8`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssoadmin_permission_set)

### Description{% #description %}

Single Sign-On (SSO) permission sets should restrict user session durations to a maximum of one hour to reduce the window of opportunity for unauthorized access and session hijacking. Allowing longer session durations by setting the `session_duration` attribute to values such as `"PT2H"` or `"PT1H1M"` in the `aws_ssoadmin_permission_set` resource increases the risk of attackers leveraging stale or stolen sessions. Configuring session durations to `session_duration = "PT1H"`, or omitting the duration in the configuration enforces this security best practice and helps limit potential exposure.

```
resource "aws_ssoadmin_permission_set" "example" {
  name             = "Example"
  instance_arn     = tolist(data.aws_ssoadmin_instances.example.arns)[0]
  relay_state      = "https://s3.console.aws.amazon.com/s3/home?region=us-east-1//"
  session_duration = "PT1H"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ssoadmin_permission_set" "example" {
  name             = "Example"
  description      = "An example"
  instance_arn     = tolist(data.aws_ssoadmin_instances.example.arns)[0]
  relay_state      = "https://s3.console.aws.amazon.com/s3/home?region=us-east-1#"
  session_duration = "PT1H"
}

resource "aws_ssoadmin_permission_set" "example2" {
  name             = "Example"
  description      = "An example"
  instance_arn     = tolist(data.aws_ssoadmin_instances.example.arns)[0]
  relay_state      = "https://s3.console.aws.amazon.com/s3/home?region=us-east-1#"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ssoadmin_permission_set" "example3" {
  name             = "Example"
  description      = "An example"
  instance_arn     = tolist(data.aws_ssoadmin_instances.example.arns)[0]
  relay_state      = "https://s3.console.aws.amazon.com/s3/home?region=us-east-1#"
  session_duration = "PT1H1M"
}

resource "aws_ssoadmin_permission_set" "example4" {
  name             = "Example"
  description      = "An example"
  instance_arn     = tolist(data.aws_ssoadmin_instances.example.arns)[0]
  relay_state      = "https://s3.console.aws.amazon.com/s3/home?region=us-east-1#"
  session_duration = "PT2H"
}
```
