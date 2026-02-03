# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/sql_database_instance_does_not_have_skip_show_database.md

---
title: Ensure SQL database instance has skip show database flag
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Ensure SQL database instance has skip show
  database flag
---

# Ensure SQL database instance has skip show database flag

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a8b7c6d5-e4f3-2109-8a7b-6c5d4e3f2109`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance)

### Description{% #description %}

The absence of the `skip_show_database` flag, or its incorrect setting within a `google_sql_database_instance` resource, can allow users to view a list of all databases on a MySQL server instance, potentially exposing sensitive schema information to unauthorized individuals. This misconfiguration increases the risk of information disclosure and can aid attackers in reconnaissance activities by providing insight into database names and structures. To mitigate this risk, ensure the configuration includes `database_flags { name = "skip_show_database" value = "on" }`, as shown below:

```
resource "google_sql_database_instance" "good_example" {
  name             = "good-instance"
  database_version = "MYSQL_8"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
    database_flags {
      name  = "skip_show_database"
      value = "on"
    }
    database_flags {
      name  = "cross db ownership chaining"
      value = "on"
    }
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_sql_database_instance" "good_example" {
  name             = "good-instance"
  database_version = "MYSQL_8"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
    database_flags {
      name  = "skip_show_database"
      value = "on" # This flag is present as required
    }
    database_flags {
      name  = "cross db ownership chaining"
      value = "on"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_sql_database_instance" "bad_example" {
  name             = "bad-instance"
  database_version = "MYSQL_8"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
    database_flags {
      name  = "cross db ownership chaining"
      value = "on"
    }
  }
}

resource "google_sql_database_instance" "bad_example_2" {
  name             = "bad-instance"
  database_version = "MYSQL_8"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
    database_flags {
      name  = "skip_show_database"
      value = "off"
    }
  }
}

resource "google_sql_database_instance" "bad_example_3" {
  name             = "bad-instance"
  database_version = "MYSQL_8"
  region           = "us-central1"

  settings {
    tier = "db-custom-2-13312"
  }
}
```
