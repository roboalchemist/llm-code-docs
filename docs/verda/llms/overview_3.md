# Source: https://docs.verda.com/infrastructure-as-code/overview.md

# Overview

## Quick links

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref">Target</th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td>Terraform</td><td><a href="terraform">terraform</a></td><td data-object-fit="fill"><a href="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FHXMQNm8Hj6sJCa9rN7Bj%2Fterraform-icon.svg?alt=media&#x26;token=4b39aa5c-05ed-4c40-b9ea-94090aa4c24a">https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FHXMQNm8Hj6sJCa9rN7Bj%2Fterraform-icon.svg?alt=media&#x26;token=4b39aa5c-05ed-4c40-b9ea-94090aa4c24a</a></td></tr><tr><td>OpenTofu</td><td><a href="opentofu">opentofu</a></td><td data-object-fit="contain"><a href="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FlkazC31AaRtzih95OFuM%2FLogo_of_OpenTofu.svg.png?alt=media&#x26;token=f45e8901-507b-4be9-a604-8b6f31fc6302">https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FlkazC31AaRtzih95OFuM%2FLogo_of_OpenTofu.svg.png?alt=media&#x26;token=f45e8901-507b-4be9-a604-8b6f31fc6302</a></td></tr></tbody></table>

## Supported Provisioners

* **Terraform**: Officially supported via the Verda Cloud registry. The provider is compatible with Terraform 1.x.
* **OpenTofu**: An open‑source fork of Terraform. The Verda provider works seamlessly with OpenTofu; you can source it directly from the OpenTofu registry if you prefer.

To use the provider, specify one of these sources in your configuration:

```hcl
# From Terraform Registry (works in OpenTofu as well)
terraform {
  required_providers {
    verda = {
      source  = "verda-cloud/verda"
      version = "~> 1.0"
    }
  }
}

# Or, explicitly from OpenTofu Registry
terraform {
  required_providers {
    verda = {
      source  = "registry.opentofu.org/verda-cloud/verda"
      version = "~> 1.0"
    }
  }
}

```

Replace the `version` constraint with the latest provider version available in the registry.

## What You’ll Find Here

* **Terraform** – guidance on installing the provider, authenticating with your Verda account, configuring providers, and using modules. Subsections cover compute resources (instances, SSH keys, startup scripts), storage (volumes), container workloads (deployments, serverless jobs, registry credentials), and how to import existing resources.
* **OpenTofu** – a brief overview of OpenTofu, instructions on using the Verda provider via the OpenTofu registry, and notes on migrating existing Terraform configurations to OpenTofu if desired.

## Prerequisites

* A Verda account with API access and an API token.
* Terraform 1.0 or newer, or OpenTofu 1.6 or newer installed on your local machine.
* Basic familiarity with HCL (HashiCorp Configuration Language).

This overview acts as the landing page for the infrastructure‑as‑code documentation. Use the navigation sidebar to dive into the specific topics that matter to you, such as provisioning GPU instances, managing volumes, or deploying containers.
