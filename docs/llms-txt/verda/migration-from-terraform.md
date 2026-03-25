# Source: https://docs.verda.com/infrastructure-as-code/opentofu/migration-from-terraform.md

# Migration from Terraform

OpenTofu is a community-driven fork of Terraform that preserves full compatibility with existing Terraform configurations and providers.\
For Verda users, migrating from Terraform to OpenTofu is intentionally straightforward and low-risk.

In most cases, **no changes to your Verda resources or configuration files are required**.

***

## What stays the same

When migrating from Terraform to OpenTofu, the following remain unchanged:

* ✅ **Verda provider source and version**
* ✅ **Resource and data source definitions**
* ✅ **State file format**
* ✅ **Authentication mechanisms**
* ✅ **Lifecycle behavior and planning logic**

If you are already using the Verda provider with Terraform, you can continue using the same `.tf` files with OpenTofu.

***

## What changes

The primary change is replacing the Terraform CLI with the OpenTofu CLI.

| Terraform          | OpenTofu      |
| ------------------ | ------------- |
| `terraform init`   | `tofu init`   |
| `terraform plan`   | `tofu plan`   |
| `terraform apply`  | `tofu apply`  |
| `terraform import` | `tofu import` |

All commands behave the same way unless explicitly documented otherwise by OpenTofu.

***

## Step-by-step migration

### 1. Install OpenTofu

Install OpenTofu using your preferred package manager or from the official OpenTofu releases.

Ensure the `tofu` binary is available in your PATH.

***

### 2. Use your existing Terraform configuration

No changes are required to your existing Verda configuration:

```hcl
terraform {
  required_providers {
    verda = {
      source  = "verda-cloud/verda"
      version = "~> 1.0"
    }
  }
}

provider "verda" {}
```

The `terraform {}` block is still used and remains valid in OpenTofu.

***

### 3. Initialize with OpenTofu

From your existing project directory:

```bash
tofu init
```

This will:

* Reuse your existing provider configuration
* Read your current state file
* Download compatible provider binaries

***

### 4. Verify the plan

Always run a plan before applying changes:

```bash
tofu plan
```

If the migration is successful, the plan should show **no changes**.

***

### 5. Apply as usual

Once verified, continue managing your infrastructure with:

```bash
tofu apply
```

***

## State compatibility

* OpenTofu can read existing Terraform state files without modification
* Remote backends (e.g. S3-compatible storage) continue to work as before
* State locking and concurrency behavior remains unchanged

No state migration step is required.

***

## Importing existing resources

Importing resources into OpenTofu works exactly the same way as in Terraform:

```bash
tofu import verda_compute_instance.example <instance-id>
```

For more details, see **Importing Existing Resources**.

***

## Rollback considerations

If needed, you can switch back to Terraform by:

* Reinstalling the Terraform CLI
* Using the same configuration and state files

No irreversible changes are introduced by OpenTofu.

***

## Summary

* Migration from Terraform to OpenTofu is **safe and minimal**
* Verda configurations and providers work without changes
* Only the CLI command changes (`terraform` → `tofu`)
* Existing state and infrastructure are preserved

This makes OpenTofu a drop-in replacement for Terraform when managing Verda infrastructure.
