# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/google_compute_network_using_default_firewall_rule.md

---
title: Google Compute network using default firewall rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Compute network using default firewall
  rule
---

# Google Compute network using default firewall rule

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `40abce54-95b1-478c-8e5f-ea0bf0bb0e33`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall#name)

### Description{% #description %}

Google Compute Network resources should avoid using the default firewall rule, as it typically allows overly permissive access to network resources and does not restrict traffic according to least-privilege principles. If left unaddressed, using the default firewall may expose internal resources to unauthorized external access, increasing the risk of lateral movement or compromise within a project. Instead, firewall rules should be defined explicitly with restricted protocols, source ranges, and tags, as shown below:

```
resource "google_compute_firewall" "secure_example" {
  name    = "restricted-firewall"
  network = google_compute_network.secure_example.name

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["203.0.113.0/24"]
}

resource "google_compute_network" "secure_example" {
  name = "test-network"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_firewall" "negative1" {
  name    = "test-firewall"
  network = google_compute_network.negative1.name

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "8080"]
  }

  source_tags = ["web"]
}

resource "google_compute_network" "negative1" {
  name = "test-network"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_firewall" "positive1" {
  name    = "default"
  network = google_compute_network.positive1.name
}

resource "google_compute_network" "positive1" {
  name = "test-network"
}
```
