<!-- Source: https://docs.verda.com/infrastructure-as-code/terraform/authentication.md -->

# Authentication

Terraform authenticates with Verda using OAuth2 credentials. All API requests made by the Verda Terraform provider are authorized using a **Client ID** and **Client Secret** associated with your Verda account.

***

## Required credentials

To authenticate, you need:

* **Client ID**
* **Client Secret**

These credentials are generated in the Verda dashboard and grant Terraform permission to manage your resources.

***

## Recommended: environment variables

The recommended way to provide credentials is via environment variables.

Set the following variables in your shell:

```bash
export VERDA_CLIENT_ID="your-client-id"
export VERDA_CLIENT_SECRET="your-client-secret"
```

Then configure the provider with an empty block:

```hcl
provider "verda" {}
```

This approach keeps sensitive credentials out of your Terraform configuration files and works well for local development and CI/CD pipelines.

***

## Provider configuration (alternative)

You can also configure credentials directly in the provider block:

```hcl
provider "verda" {
  client_id     = "your-client-id"
  client_secret = "your-client-secret"
}
```

> This method is **not recommended** for production use, as it risks committing secrets to version control.

***

## Using Terraform variables

If you prefer using Terraform variables, define them as sensitive:

```hcl
variable "verda_client_id" {
  type      = string
  sensitive = true
}

variable "verda_client_secret" {
  type      = string
  sensitive = true
}
```

Then reference them in the provider configuration:

```hcl
provider "verda" {
  client_id     = var.verda_client_id
  client_secret = var.verda_client_secret
}
```

Values can be supplied via `terraform.tfvars`, environment variables, or a secrets manager.

***

## CI/CD considerations

When running Terraform in CI/CD:

* Store credentials in your CI secret manager
* Inject them as environment variables at runtime
* Avoid printing sensitive values in logs

Terraform automatically masks sensitive variables, but extra care should still be taken when debugging pipelines.

***

## Troubleshooting authentication

If authentication fails:

* Verify that `VERDA_CLIENT_ID` and `VERDA_CLIENT_SECRET` are set
* Confirm the credentials are valid and not expired
* Ensure your environment variables are available to the Terraform process

Authentication errors typically appear during `terraform init` or `terraform plan`.

***

## Next steps

Once authentication is configured, continue with:

* **Provider Configuration** – advanced provider settings
* **Compute** – provisioning GPU instances and related resources
* **Storage** – managing persistent volumes
