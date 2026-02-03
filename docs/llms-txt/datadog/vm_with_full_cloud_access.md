# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/vm_with_full_cloud_access.md

---
title: VM with full cloud access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > VM with full cloud access
---

# VM with full cloud access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `bc280331-27b9-4acb-a010-018e8098aa5d`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#scopes)

### Description{% #description %}

If a Google Compute Engine VM instance is configured to use the default service account with `cloud-platform` scope (full access to all Cloud APIs), any process running on that instance can interact with all enabled Google Cloud services in the project, significantly increasing the risk of privilege escalation or unintended data exposure. For example, the following configuration is insecure:

```
service_account {
  scopes = ["userinfo-email", "compute-ro", "storage-ro", "cloud-platform"]
}
```

To limit permissions and reduce the attack surface, the service account should only be granted the minimum set of scopes necessary, such as:

```
service_account {
  scopes = ["userinfo-email", "compute-ro", "storage-ro"]
}
```

Leaving excessive permissions unaddressed can allow attackers or compromised applications to gain broad and unnecessary access across your cloud environment.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_instance" "negative1" {
  name         = "test"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro"]
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_instance" "positive1" {
  name         = "test"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro", "cloud-platform"]
  }
}
```
