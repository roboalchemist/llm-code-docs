# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/sql_db_instance_backup_disabled.md

---
title: SQL DB instance backup disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SQL DB instance backup disabled
---

# SQL DB instance backup disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `cf3c7631-cd1e-42f3-8801-a561214a6e79`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance)

### Description{% #description %}

This check verifies whether automated backups are enabled for all Google Cloud SQL database instances by ensuring the `backup_configuration` block has the `enabled = true` attribute. If automated backups are disabled or the `backup_configuration` block is missing, databases are at risk of unrecoverable data loss in the event of accidental deletion, corruption, or other failures. When automated backups are disabled, the configuration appears as follows:

```
settings {
    backup_configuration {
        enabled = false
    }
}
```

To mitigate this risk, ensure backups are enabled using the following configuration:

```
settings {
    backup_configuration {
        enabled = true
    }
}
```

This ensures that point-in-time recovery is possible and critical business data can be restored when needed.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_sql_database_instance" "negative1" {
    name             = "master-instance"
    database_version = "POSTGRES_11"
    region           = "us-central1"

    settings {
        backup_configuration{
            enabled = true
        }
    }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_sql_database_instance" "positive1" {
    name             = "master-instance"
    database_version = "POSTGRES_11"
    region           = "us-central1"

    settings {
        tier = "db-f1-micro"
    }
}

resource "google_sql_database_instance" "positive2" {
    name             = "master-instance"
    database_version = "POSTGRES_11"
    region           = "us-central1"

    settings {
        tier = "db-f1-micro"
        backup_configuration{
            binary_log_enabled = true
        }
    }
}

resource "google_sql_database_instance" "positive3" {
    name             = "master-instance"
    database_version = "POSTGRES_11"
    region           = "us-central1"

    settings {
        backup_configuration{
            enabled = false
        }
    }
}
```
