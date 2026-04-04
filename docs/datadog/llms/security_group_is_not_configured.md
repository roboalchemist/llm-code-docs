# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/security_group_is_not_configured.md

---
title: Security group is not configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security group is not configured
---

# Security group is not configured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5c822443-e1ea-46b8-84eb-758ec602e844`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://www.terraform.io/docs/providers/azure/r/virtual_network.html)

### Description{% #description %}

Network Security Groups (NSGs) in Azure provide filtering of network traffic to and from Azure resources within an Azure virtual network. When a subnet is not configured with an NSG, it lacks essential security controls that filter inbound and outbound traffic, potentially exposing resources to unauthorized access and network-based attacks.

A properly secured virtual network requires the `security_group` attribute to be defined with a valid NSG reference in each subnet configuration. Without this protection, workloads running in these subnets may be accessible from unwanted network sources, increasing the attack surface.

Secure example:

```terraform
subnet {
  name           = "subnet1"
  address_prefix = "10.1.2.0/25"
  security_group = "securitygroup-name"
}
```

Vulnerable example:

```terraform
subnet {
  name           = "subnet1"
  address_prefix = "10.1.2.0/25"
  // Missing security_group attribute
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "azure_virtual_network" "negative1" {
  name          = "test-network"
  address_space = ["10.1.2.0/24"]
  location      = "West US"

  subnet {
    name           = "subnet1"
    address_prefix = "10.1.2.0/25"
    security_group = "a"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
resource "azure_virtual_network" "positive1" {
  name          = "test-network"
  address_space = ["10.1.2.0/24"]
  location      = "West US"

  subnet {
    name           = "subnet1"
    address_prefix = "10.1.2.0/25"
  }
}

resource "azure_virtual_network" "positive2" {
  name          = "test-network"
  address_space = ["10.1.2.0/24"]
  location      = "West US"

  subnet {
    name           = "subnet1"
    address_prefix = "10.1.2.0/25"
    security_group = ""
  }
}
```
