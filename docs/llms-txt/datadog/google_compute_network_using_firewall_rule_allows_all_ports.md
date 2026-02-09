# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/google_compute_network_using_firewall_rule_allows_all_ports.md

---
title: Google Compute network using firewall rule that allows all ports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Compute network using firewall rule
  that allows all ports
---

# Google Compute network using firewall rule that allows all ports

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `22ef1d26-80f8-4a6c-8c15-f35aab3cac78`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall#allow)

### Description{% #description %}

Allowing a Google Compute Network firewall rule to permit traffic on all TCP ports (using `ports = ["0-65535"]`) exposes instances to a broad range of attacks and unauthorized access, increasing the risk of exploitation across unused and potentially vulnerable services. By not restricting allowed ports to only those necessaryâsuch as `ports = ["80", "8080"]` for web servicesâthe configuration creates a large attack surface. To minimize security risks, firewall rules should define only the specific protocols and ports required for service functionality.

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
  name    = "test-firewall"
  network = google_compute_network.positive1.name

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }

  source_tags = ["web"]
}

resource "google_compute_network" "positive1" {
  name = "test-network"
}
```
