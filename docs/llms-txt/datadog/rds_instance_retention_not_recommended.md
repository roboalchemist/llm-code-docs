# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/rds_instance_retention_not_recommended.md

---
title: RDS instance retention period not recommended
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RDS instance retention period not recommended
---

# RDS instance retention period not recommended

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dc158941-28ce-481d-a7fa-dc80761edf46`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/db_instance#sql_collector_config_value)

### Description{% #description %}

`alicloud_db_instance` resources must have `sql_collector_status` set to `Enabled` and `sql_collector_config_value` set to `180` or greater. This rule flags resources that are missing either attribute, have `sql_collector_status` set to `Disabled`, or have `sql_collector_config_value` less than `180`. To remediate, set `sql_collector_status = Enabled` and `sql_collector_config_value = 180`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    sql_collector_status = "Enabled"
    sql_collector_config_value = 180
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    },{
        name = "log_connections"
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
    sql_collector_status = "Disabled"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    },{
        name = "log_connections"
        value = "ON"
    }]
}
```

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    sql_collector_status = "Enabled"
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    },{
        name = "log_connections"
        value = "ON"
    }]
}
```

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    sql_collector_status = "Enabled"
    sql_collector_config_value = 30
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    },{
        name = "log_connections"
        value = "ON"
    }]
}
```
