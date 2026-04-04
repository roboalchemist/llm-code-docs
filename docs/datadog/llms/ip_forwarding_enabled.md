# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/ip_forwarding_enabled.md

---
title: IP forwarding enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IP forwarding enabled
---

# IP forwarding enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f34c0c25-47b4-41eb-9c79-249b4dd47b89`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance)

### Description{% #description %}

This check ensures that the `can_ip_forward` attribute for Google Compute Engine instances is set to `false`, which prevents instances from forwarding packets not addressed to them. If `can_ip_forward` is set to `true`, as shown below, the instance could be misused as a routing or proxy device, increasing the risk of data exfiltration or man-in-the-middle attacks:

```
resource "google_compute_instance" "appserver" {
  name           = "primary-application-server"
  machine_type   = "e2-medium"
  can_ip_forward = true
  ...
}
```

To mitigate this risk, configure the attribute as `false`:

```
resource "google_compute_instance" "appserver" {
  name           = "primary-application-server"
  machine_type   = "e2-medium"
  can_ip_forward = false
  ...
}
```

Disabling IP forwarding hardens network boundaries and reduces the attack surface of the cloud environment.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_instance" "appserver" {
  name           = "primary-application-server"
  machine_type   = "e2-medium"
  can_ip_forward = false

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_instance" "appserver" {
  name           = "primary-application-server"
  machine_type   = "e2-medium"
  can_ip_forward = true

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
  }
}
```
