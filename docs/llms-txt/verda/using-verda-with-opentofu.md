# Source: https://docs.verda.com/infrastructure-as-code/opentofu/using-verda-with-opentofu.md

# Using Verda with OpenTofu

Verda provides an official Infrastructure as Code (IaC) provider that can be used with **OpenTofu** to provision and manage Verda resources declaratively.

The Verda provider for OpenTofu is **identical to the Terraform provider**. It uses the same schemas, resources, authentication methods, and lifecycle behavior. If you already use Verda with Terraform, you can switch to OpenTofu without changing your existing configuration.

***

#### What this page covers

* How Verda works with OpenTofu
* Declaring and configuring the Verda provider
* Authentication behavior
* Compatibility with Terraform
* State and lifecycle considerations

***

#### Provider compatibility

The Verda provider is fully compatible with OpenTofu:

* ✅ Same provider source (`verda-cloud/verda`)
* ✅ Same resource and data source schemas
* ✅ Same authentication methods
* ✅ Same lifecycle and state behavior

In most cases, migrating to OpenTofu only requires replacing the Terraform CLI with OpenTofu. No changes to Verda resources or configuration are needed.

***

#### Declaring the provider

Declare the Verda provider in your OpenTofu configuration using the standard `required_providers` block:

```hcl
terraform {
  required_providers {
    verda = {
      source  = "verda-cloud/verda"
      version = "~> 1.0"
    }
  }
}
```

Then configure the provider:

```hcl
provider "verda" {}
```

No OpenTofu-specific configuration is required.

***

#### Authentication

Authentication works exactly the same way in OpenTofu as it does in Terraform.

The Verda provider supports the following authentication methods:

* Environment variables
* CLI-based authentication
* Explicit provider configuration (when applicable)

Refer to the **Terraform Authentication** documentation for full details, as the behavior is identical when using OpenTofu.

***

#### Using Verda resources

All Verda resources behave the same way in OpenTofu as they do in Terraform, including:

* Compute instances
* Storage volumes
* Containers and serverless jobs
* Networking and related infrastructure

Example:

```hcl
resource "verda_volume" "data" {
  name        = "training-data"
  size_gb    = 500
  description = "Dataset volume"
}
```

***

#### State and lifecycle behavior

* OpenTofu state files are compatible with existing Terraform state files
* Lifecycle rules such as `prevent_destroy` and `ignore_changes` behave the same
* Importing existing Verda resources works identically

For more details, see **Importing Existing Resources**.

***

#### Summary

Using Verda with OpenTofu provides the same experience as using Verda with Terraform, while allowing you to adopt OpenTofu as your IaC engine. Existing Verda users can migrate with minimal effort and no changes to their infrastructure definitions.
