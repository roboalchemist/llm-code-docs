# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/rds_instance_ssl_action_disabled.md

---
title: RDS instance SSL action disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RDS instance SSL action disabled
---

# RDS instance SSL action disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7a1ee8a9-71be-4b11-bb70-efb62d16863b`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/db_instance#ssl_action)

### Description{% #description %}

The `ssl_action` parameter must be set to `Open` for `alicloud_db_instance` resources. This rule flags instances where `ssl_action` is set to `Close` or is not defined. Setting `ssl_action = "Open"` enforces SSL/TLS for database connections; leaving it unset or set to `Close` may expose data in transit.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    ssl_action = "Update"
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
    ssl_action = "Open"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
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
    ssl_action = "Close"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    }]
}
```
