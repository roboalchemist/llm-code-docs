# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/emr_without_vpc.md

---
title: EMR without VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EMR without VPC
---

# EMR without VPC

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2b3c8a6d-9856-43e6-ab1d-d651094f03b4`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/emr_cluster#subnet_id)

### Description{% #description %}

This check ensures that Amazon Elastic MapReduce (EMR) clusters are deployed within a Virtual Private Cloud (VPC) by specifying a `subnet_id` in the Terraform resource. Launching EMR clusters without associating them to a VPC, as shown by omitting the `subnet_id` attribute in the `aws_emr_cluster` resource, exposes the cluster to public networks and increases the risk of unauthorized access or data compromise. By deploying EMR clusters in a VPC, network access control can be properly enforced through security groups and network ACLs, limiting exposure to only trusted sources. Failure to launch EMR clusters inside a VPC can lead to serious security vulnerabilities, including unauthorized data access, data exfiltration, or service disruption.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_emr_cluster" "negative1" {
  name          = "emr-test-arn"
  release_label = "emr-4.6.0"
  subnet_id = aws_subnet.main.id
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_emr_cluster" "positive1" {
  name          = "emr-test-arn"
  release_label = "emr-4.6.0"
}
```
