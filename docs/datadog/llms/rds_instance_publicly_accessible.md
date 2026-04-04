# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/rds_instance_publicly_accessible.md

---
title: RDS DB instance publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RDS DB instance publicly accessible
---

# RDS DB instance publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1b4565c0-4877-49ac-ab03-adebbccd42ae`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/db_instance#security_ips)

### Description{% #description %}

`0.0.0.0` or `0.0.0.0/0` should not be included in the `security_ips` list. This rule flags `alicloud_db_instance` resources whose `security_ips` contain these public addresses. Allowing them grants public network access to the database instance and may expose it to the internet.

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
    }]
}
```

```terraform
resource "alicloud_db_instance" "default" {
    engine = "MySQL"
    engine_version = "5.6"
    db_instance_class = "rds.mysql.t1.small"
    db_instance_storage = "10"
    security_ips = [
        "10.23.12.24"
        ]
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
    security_ips = [
        "0.0.0.0/0",
        "10.23.12.24/24"
        ]
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
    security_ips = [
        "0.0.0.0",
        "10.23.12.24/24"
        ]
    parameters = [{
        name = "innodb_large_prefix"
        value = "ON"
    },{
        name = "connect_timeout"
        value = "50"
    }]
}
```
