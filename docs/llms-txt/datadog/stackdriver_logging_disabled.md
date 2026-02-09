# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/stackdriver_logging_disabled.md

---
title: Stackdriver Logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Stackdriver Logging disabled
---

# Stackdriver Logging disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4c7ebcb2-eae2-461e-bc83-456ee2d4f694`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#logging_service)

### Description{% #description %}

Google Kubernetes Engine (GKE) clusters should have Stackdriver Logging enabled to ensure that logs from the cluster are collected and available for monitoring and auditing. Failing to set the `logging_service` attribute, or setting it to `"none"`, means critical cluster activity and security logs will not be captured, potentially leaving malicious or accidental changes undetected. For secure configuration, set `logging_service = "logging.googleapis.com/kubernetes"` or simply omit the attribute to use the default, as shown below:

```
resource "google_container_cluster" "secure" {
  name               = "example-cluster"
  location           = "us-central1-a"
  initial_node_count = 3
  logging_service    = "logging.googleapis.com/kubernetes"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "negative1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  logging_service = "logging.googleapis.com/kubernetes"

  timeouts {
    create = "30m"
    update = "40m"
  }
}

# Logging service defaults to Stackdriver, so it's okay to be undefined
resource "google_container_cluster" "negative2" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  
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
  logging_service = "none"

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_container_cluster" "positive2" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  logging_service = "logging.googleapis.com"

  timeouts {
    create = "30m"
    update = "40m"
  }
}
```
