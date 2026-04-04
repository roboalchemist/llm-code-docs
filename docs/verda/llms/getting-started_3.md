# Source: https://docs.verda.com/infrastructure-as-code/opentofu/getting-started.md

# Getting Started

OpenTofu is an open-source, Terraform-compatible Infrastructure as Code (IaC) tool. Verda supports OpenTofu as a **drop-in alternative to Terraform**, allowing you to manage Verda infrastructure using the same workflows, configuration language, and provider.

> **Beta notice**\
> OpenTofu support is currently in **beta**. Core functionality is stable, but interfaces and behavior may evolve. We recommend validating changes in non-production environments first.

***

#### What is OpenTofu?

OpenTofu is a community-driven fork of Terraform that maintains compatibility with existing Terraform configurations and providers. For Verda users, this means:

* The **same HCL syntax**
* The **same Verda provider**
* The **same resource definitions**
* The **same state and workflow concepts**

If you already use Terraform, you already know how to use OpenTofu.

***

#### When should I use OpenTofu?

You may choose OpenTofu if you:

* Prefer an open-source Terraform alternative
* Are migrating away from Terraform
* Want to standardize on OpenTofu across your infrastructure tooling

If you are already using Terraform successfully, switching to OpenTofu is optional.

***

#### What’s different from Terraform?

From a Verda perspective, very little.

* Resource schemas are identical
* Provider configuration is the same
* Infrastructure behavior is unchanged

The main difference is the CLI binary:

* `terraform` → `tofu`

Everything else remains familiar.

***

#### Prerequisites

Before getting started, make sure you have:

* An existing Verda account
* API credentials for authentication
* OpenTofu installed locally

Terraform users can reuse their existing configuration files.

***

#### Basic workflow

The OpenTofu workflow mirrors Terraform exactly:

1. Initialize the working directory
2. Review planned changes
3. Apply infrastructure changes
4. Manage state over time

Example commands:

```bash
tofu init
tofu plan
tofu apply
```

***

#### Next steps

* **Using the Verda Provider**\
  Learn how to configure and authenticate the Verda provider in OpenTofu.
* **Migration from Terraform**\
  Step-by-step guidance for moving existing Terraform projects to OpenTofu safely.

For resource definitions and examples, refer to the Terraform documentation sections — they apply equally to OpenTofu.
