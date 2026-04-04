# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/rds_instance_log_duration_disabled.md

---
title: RDS instance log duration disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RDS instance log duration disabled
---

# RDS instance log duration disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a597e05a-c065-44e7-9cc8-742f572a504a`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/db_instance#parameters)

### Description{% #description %}

The `log_duration` parameter must be defined in the `parameters` array of `alicloud_db_instance` resources and set to `ON`.If `log_duration` exists and is set to `OFF`, the rule reports an `IncorrectValue` issue and suggests replacing `OFF` with `ON`.If the `parameters` array or the `log_duration` parameter is missing, the rule reports a `MissingAttribute` issue and suggests adding `parameters = [{ name = "log_duration" value = "ON" }]`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    },{
        name = "log_duration"
        value = "ON"
    }]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    }]
}
```

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
}
```

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    },{
        name = "log_duration"
        value = "OFF"
    }]
}
```
