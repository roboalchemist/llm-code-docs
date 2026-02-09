# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/pubsub_topic_is_public.md

---
title: Pub/Sub Topics are anonymously or publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Pub/Sub Topics are anonymously or publicly
  accessible
---

# Pub/Sub Topics are anonymously or publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7sdj7dsj8-f348-4f95-845c-1090e41a615c`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_topic_iam)

### Description{% #description %}

Google Cloud Pub/Sub Topics should not be configured to allow public access by assigning IAM roles to the special principals `allUsers` or `allAuthenticatedUsers`. Granting roles to these principals makes the topic accessible to anyone on the internet or to any authenticated Google user, exposing your data to unauthorized access or misuse. For example:

```
resource "google_pubsub_topic_iam_member" "bad_example" {
  topic  = "example-topic"
  member = "allUsers"
  role   = "roles/pubsub.publisher"
}
```

To prevent this, restrict the `member` attribute to specific users or service accounts, as shown below:

```
resource "google_pubsub_topic_iam_member" "good_example" {
  topic  = "example-topic"
  member = "user:someone@example.com"
  role   = "roles/pubsub.publisher"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# IAM Binding compliant
resource "google_pubsub_topic_iam_binding" "good_example_binding" {
  topic   = "example-topic"
  members = ["user:someone@example.com", "group:admins@example.com"] # â No public principals
  role    = "roles/pubsub.subscriber"
}
```

```terraform
# IAM Member compliant
resource "google_pubsub_topic_iam_member" "good_example_member" {
  topic  = "example-topic"
  member = "user:someone@example.com" # â Non-public principal
  role   = "roles/pubsub.publisher"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# IAM Member violation
resource "google_pubsub_topic_iam_member" "bad_example_member" {
  topic  = "example-topic"
  member = "allUsers" # â Public principal
  role   = "roles/pubsub.publisher"
}

# IAM Binding violation
resource "google_pubsub_topic_iam_binding" "bad_example_binding" {
  topic   = "example-topic"
  members = ["allAuthenticatedUsers", "user:someone@example.com"] # â Contains public principal
  role    = "roles/pubsub.subscriber"
}
```
