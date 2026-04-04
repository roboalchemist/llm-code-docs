# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/google_compute_network_using_firewall_rule_allows_port_range.md

---
title: Google Compute network using firewall rule that allows port range
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Compute network using firewall rule
  that allows port range
---

# Google Compute network using firewall rule that allows port range

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e6f61c37-106b-449f-a5bb-81bfcaceb8b4`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall#allow)

### Description{% #description %}

Allowing a port range in a Google Compute Network firewall rule, such as `ports = ["80", "8080", "1000-2000"]`, can expose unnecessary services and increase the attack surface of your cloud environment. Attackers may exploit any open ports within the specified range, leading to potential unauthorized access or compromise of resources. To reduce risk, firewall rules should restrict access to only required ports, as shown in the following configuration:

```
allow {
  protocol = "tcp"
  ports    = ["80", "8080"]
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
  name    = "test-firewall"
  network = google_compute_network.positive1.name

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "8080", "1000-2000"]
  }

  source_tags = ["web"]
}

resource "google_compute_network" "positive1" {
  name = "test-network"
}
```
