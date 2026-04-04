# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/sql_database_has_cross_db_ownership_chaining.md

---
title: SQL Server cross DB ownership chaining enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SQL Server cross DB ownership chaining enabled
---

# SQL Server cross DB ownership chaining enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b2d5f3c9-1e68-47a1-89b4-92f3a6d7e123`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_flags)

### Description{% #description %}

Cross-database ownership chaining allows users to access objects across databases without requiring separate permissions for each database, creating a potential privilege escalation vulnerability. When enabled, an attacker with access to one database might exploit ownership chains to gain unauthorized access to data in other linked databases, bypassing normal permission boundaries. To secure your SQL Server instance, configure the `cross db ownership chaining` database flag to `off` as shown in the following example:

```
settings {
  database_flags {
    name  = "cross db ownership chaining"
    value = "off"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_sql_database_instance" "good_example" {
  name             = "good-instance"
  database_version = "SQLSERVER_2019_STANDARD"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
    database_flags {
      name  = "cross db ownership chaining"
      value = "off" # â Compliant
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_sql_database_instance" "bad_example" {
  name             = "bad-instance"
  database_version = "SQLSERVER_2019_STANDARD"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
    database_flags {
      name  = "cross db ownership chaining"
      value = "on"
    }
  }
}
```
