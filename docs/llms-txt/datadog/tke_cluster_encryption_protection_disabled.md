# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/tke_cluster_encryption_protection_disabled.md

---
title: Beta - TKE cluster encryption protection disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - TKE cluster encryption protection
  disabled
---

# Beta - TKE cluster encryption protection disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3ed47402-e322-465f-a0f0-8681135a17b0`

**Cloud Provider:** TencentCloud

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/kubernetes_encryption_protection)

### Description{% #description %}

A `TKE` cluster should have `tencentcloud_kubernetes_encryption_protection` enabled. This rule verifies that each `tencentcloud_kubernetes_cluster` has a corresponding `tencentcloud_kubernetes_encryption_protection` resource whose `cluster_id` references the cluster. If no matching `tencentcloud_kubernetes_encryption_protection` is found, the rule reports a `MissingAttribute` issue.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
data "tencentcloud_vpc_subnets" "vpc" {
  is_default        = true
  availability_zone = "ap-guangzhou-3"
}

resource "tencentcloud_kubernetes_cluster" "has_encryption_protection" {
  vpc_id                  = data.tencentcloud_vpc_subnets.vpc.instance_list.0.vpc_id
  cluster_cidr            = "10.32.0.0/16"
  cluster_max_pod_num     = 32
  cluster_name            = "tf_example_cluster"
  cluster_desc            = "a tf example cluster for the kms test"
  cluster_max_service_num = 32
  cluster_deploy_type     = "MANAGED_CLUSTER"
}


resource "tencentcloud_kms_key" "example" {
  alias       = "tf-example-kms-key"
  description = "example of kms key instance"
  key_usage   = "ENCRYPT_DECRYPT"
  is_enabled  = true
}

resource "tencentcloud_kubernetes_encryption_protection" "example" {
  cluster_id = tencentcloud_kubernetes_cluster.has_encryption_protection.id
  kms_configuration {
    key_id     = tencentcloud_kms_key.example.id
    kms_region = "ap-guangzhou"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
data "tencentcloud_vpc_subnets" "vpc" {
  is_default        = true
  availability_zone = "ap-guangzhou-3"
}

resource "tencentcloud_kubernetes_cluster" "none_encryption_protection" {
  vpc_id                  = data.tencentcloud_vpc_subnets.vpc.instance_list.0.vpc_id
  cluster_cidr            = "10.32.0.0/16"
  cluster_max_pod_num     = 32
  cluster_name            = "tf_example_cluster"
  cluster_desc            = "a tf example cluster for the kms test"
  cluster_max_service_num = 32
  cluster_deploy_type     = "MANAGED_CLUSTER"
}
```
