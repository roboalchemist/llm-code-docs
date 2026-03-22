# Source: https://docs.verda.com/infrastructure-as-code/terraform/provider-configuration.md

# Provider Configuration

The Verda Terraform provider supports a minimal default configuration and optional advanced settings. In most cases, the default configuration is sufficient, and Terraform will work out of the box once authentication is set up.

***

## Basic configuration (recommended)

The simplest and recommended provider configuration looks like this:

```hcl
provider "verda" {}
```

With this configuration, the provider automatically reads authentication credentials from environment variables.

This approach is ideal for:

* Local development
* CI/CD pipelines
* Keeping credentials out of version control

***

### Authentication parameters

The provider supports the following authentication parameters:

| Parameter       | Description             |
| --------------- | ----------------------- |
| `client_id`     | Verda API Client ID     |
| `client_secret` | Verda API Client Secret |

These values can be supplied via:

* Environment variables (recommended)
* Terraform variables
* Directly in the provider block

Example using Terraform variables:

```hcl
provider "verda" {
  client_id     = var.verda_client_id
  client_secret = var.verda_client_secret
}
```

***

#### Environment variables

When using environment variables, Terraform automatically passes them to the provider:

```bash
export VERDA_CLIENT_ID="your-client-id"
export VERDA_CLIENT_SECRET="your-client-secret"
```

No additional provider configuration is required.

***

#### Multiple provider configurations

If you need to manage multiple Verda accounts or environments (for example, staging and production), you can define multiple provider instances using aliases:

```hcl
provider "verda" {
  alias = "staging"
}

provider "verda" {
  alias = "production"
}
```

Then reference the provider in resources:

```hcl
resource "verda_instance" "example" {
  provider = verda.staging
  # resource configuration
}
```

***

#### Version pinning

It is recommended to pin the provider version to avoid unexpected breaking changes:

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

Update the version constraint as new provider versions are released.

***

#### Common issues

* **Authentication errors**\
  Ensure `VERDA_CLIENT_ID` and `VERDA_CLIENT_SECRET` are set and accessible to Terraform.
* **Provider not found**\
  Verify the provider source matches the registry you are using.
* **Unexpected behavior after upgrade**\
  Review the provider changelog and consider tightening version constraints.

***

#### Next steps

Once the provider is configured, you can start managing Verda resources:

* **Compute** – GPU instances, SSH keys, and startup scripts
* **Storage** – Persistent volumes
* **Containers** – Containers, serverless jobs, and registry credentials
