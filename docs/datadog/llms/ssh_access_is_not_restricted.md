# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/ssh_access_is_not_restricted.md

---
title: SSH access is not restricted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SSH access is not restricted
---

# SSH access is not restricted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c4dcdcdf-10dd-4bf4-b4a0-8f6239e6aaa0`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall)

### Description{% #description %}

Allowing SSH access (TCP port 22) from the internet (such as setting `source_ranges = ["0.0.0.0/0"]` in a `google_compute_firewall` resource) exposes virtual machine instances to potential unauthorized access and brute-force attacks, violating the principle of least privilege. Attackers scanning public IP ranges can exploit this misconfiguration to gain direct access to your systems, increasing the risk of compromise. A secure configuration should restrict SSH access to trusted IP addresses or private networks, as shown below:

```
resource "google_compute_firewall" "secure_example" {
  name    = "restricted-ssh"
  network = google_compute_network.default.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
  source_ranges = ["203.0.113.0/24"] // Replace with trusted IP range
  source_tags = ["admin"]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_firewall" "negative1" {
  name    = "test-firewall"
  network = google_compute_network.default.name

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "8080", "1000-2000"]
  }

  source_tags = ["web"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_firewall" "positive1" {
  name    = "test-firewall"
  network = google_compute_network.default.name
  direction = "INGRESS"
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["22", "80", "3389", "8080", "1000-2000"]
  }

  source_tags = ["web"]
}

resource "google_compute_firewall" "positive2" {
  name    = "test-firewall"
  network = google_compute_network.default.name

  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "8080", "1000-2000","21-3390"]
  }

  source_tags = ["web"]
}

resource "google_compute_firewall" "positive3" {
  name    = "test-firewall"
  network = google_compute_network.default.name

  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "all"
  }

  source_tags = ["web"]
}
```
