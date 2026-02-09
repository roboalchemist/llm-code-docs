# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/network_policy_disabled.md

---
title: Network policy disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Network policy disabled
---

# Network policy disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `11e7550e-c4b6-472e-adff-c698f157cdd7`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster)

### Description{% #description %}

Kubernetes Engine clusters must have network policies enabled to restrict traffic between pods and control communication within the cluster. In Terraform, this requires setting `network_policy.enabled = true` and `addons_config.network_policy_config.disabled = false`, as shown below:

```
network_policy {
  enabled = true
}
addons_config {
  network_policy_config {
    disabled = false
  }
}
```

If these settings are not properly configured, unauthorized traffic between pods may be allowed, increasing the risk of lateral movement and potential compromise of sensitive applications or data within the cluster.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "negative1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  network_policy {
      enabled = true
  }
  addons_config {
    network_policy_config {
        disabled = false
    }
  }
  networking_mode = "VPC_NATIVE"

  timeouts {
    create = "30m"
    update = "40m"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
resource "google_container_cluster" "positive1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  network_policy {
      enabled = true
  }

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_container_cluster" "positive2" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  network_policy {
      enabled = true
  }

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_container_cluster" "positive3" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_container_cluster" "positive4" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  network_policy {
      enabled = true
  }
  addons_config {

  }

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_container_cluster" "positive5" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  network_policy {
      enabled = false
  }
  addons_config {
    network_policy_config {
        disabled = false
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_container_cluster" "positive6" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  network_policy {
      enabled = true
  }
  addons_config {
    network_policy_config {
        disabled = true
    }
  }

  timeouts {
    create = "30m"
    update = "40m"
  }
}
```
