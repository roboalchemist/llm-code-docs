# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/outdated_gke_version.md

---
title: Outdated GKE version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Outdated GKE version
---

# Outdated GKE version

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `128df7ec-f185-48bc-8913-ce756a3ccb85`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#master_version)

### Description{% #description %}

Running outdated versions of Google Kubernetes Engine (GKE) exposes clusters to unpatched security vulnerabilities and known exploits that attackers can leverage to compromise workloads or gain unauthorized access. Terraform configurations should specify the `min_master_version` and `node_version` attributes with values such as `"latest"` or a supported, up-to-date release to ensure that the cluster automatically receives important security patches. For example, a secure configuration might look like the following:

```
resource "google_container_cluster" "example" {
  min_master_version = "latest"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "negative1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }

  min_master_version = "latest"
}

#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "negative2" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }

  min_master_version = "1.25"
}

#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "negative3" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }

  min_master_version = "1.25"
  node_version = "1.25"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "positive1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }

  min_master_version = "1.24"
}

#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "positive2" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }


  node_version = "1.24"
}
```
