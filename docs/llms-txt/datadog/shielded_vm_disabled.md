# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/shielded_vm_disabled.md

---
title: Shielded VM disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Shielded VM disabled
---

# Shielded VM disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1b44e234-3d73-41a8-9954-0b154135280e`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#shielded_instance_config)

### Description{% #description %}

Compute instances must be configured with Shielded VM enabled to provide enhanced security against rootkits and other persistent threats. This requires defining the `shielded_instance_config` block with all sub-attributesâ`enable_secure_boot`, `enable_vtpm`, and `enable_integrity_monitoring`âset to `true`. Failure to enable these features, as shown below, can leave virtual machines vulnerable to unauthorized modifications, tampering, or attacks that compromise the integrity and confidentiality of the system.

```
data "google_compute_instance" "appserver" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = true
      enable_vtpm = true
      enable_integrity_monitoring = true
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
data "google_compute_instance" "appserver" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = true
      enable_vtpm = true
      enable_integrity_monitoring = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
data "google_compute_instance" "appserver1" {
  name = "primary-application-server"
  zone = "us-central1-a"
}

data "google_compute_instance" "appserver2" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = true
      enable_vtpm = true
  }
}

data "google_compute_instance" "appserver3" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = true
      enable_integrity_monitoring = true
  }
}

data "google_compute_instance" "appserver4" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_vtpm = true
      enable_integrity_monitoring = true
  }
}

data "google_compute_instance" "appserver5" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = false
      enable_vtpm = true
      enable_integrity_monitoring = true
  }
}

data "google_compute_instance" "appserver6" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = true
      enable_vtpm = false
      enable_integrity_monitoring = true
  }
}

data "google_compute_instance" "appserver7" {
  name = "primary-application-server"
  zone = "us-central1-a"
  shielded_instance_config {
      enable_secure_boot = true
      enable_vtpm = true
      enable_integrity_monitoring = false
  }
}
```

```terraform
resource "google_compute_instance" "jumpbox" {
  name         = "${var.name}-jumpbox"
  machine_type = var.instance_type
  zone         = element(var.zones, 0)

  boot_disk {
    initialize_params {
      image = "${var.images_source}/${var.image_family}"
      size  = var.boot_disk_size
      type  = var.boot_disk_type
    }
  }

  network_interface {
    subnetwork = var.subnet
  }

  metadata = {}

  service_account {
    scopes = []
  }

  tags = ["public", "jumpbox"]
}

resource "google_compute_firewall" "jumpbox" {
  name    = "${var.name}-ssh-to-jumpbox"
  network = var.network

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_tags = ["appgate-gateway"]

  target_tags = ["jumpbox"]
}

resource "google_compute_firewall" "jumpbox_service" {
  name    = "${var.name}-jumpbox-service"
  network = var.network

  allow {
    protocol = "tcp"
    ports    = ["22", "80", "443"]
  }

  source_tags = ["jumpbox"]

  target_tags = ["jumpbox-service"]
}
```
