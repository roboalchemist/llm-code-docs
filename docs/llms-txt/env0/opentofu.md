# Source: https://docs.envzero.com/guides/community-and-resources/community-and-open-source/opentofu.md

# Source: https://docs.envzero.com/guides/admin-guide/templates/opentofu.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenTofu

> Configure and deploy OpenTofu templates with env zero as an open-source Terraform alternative

OpenTofu is an open-source fork of Terraform that provides a robust Infrastructure-as-Code (IaC) solution. It maintains compatibility with Terraform while offering additional features and community-driven development.

## OpenTofu in env zero

env zero provides full support for OpenTofu deployments, allowing you to manage your infrastructure using OpenTofu's declarative configuration language. OpenTofu is the default Terraform binary in env zero, providing a reliable and open-source alternative to Terraform.

## Configuration options

### OpenTofu version selection

You can specify which version of OpenTofu to use in your template configuration:

1. Navigate to your template settings
2. Open the **Advanced** settings section
3. Select your preferred OpenTofu version from the dropdown

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/envzero-b61043c8/images/guides/admin-guide/templates/opentofu-version-selection.png" alt="OpenTofu version selection in Advanced settings" />
</Frame>

### Working directory

Configure the working directory where your OpenTofu configuration files are located:

* **Root directory**: Use the repository root (default)
* **Subdirectory**: Specify a path relative to the repository root

<Info>
  If your OpenTofu files are in a subdirectory, specify the path in the **Working Directory** field under **Advanced** settings.
</Info>

## OpenTofu-specific features

### State management

OpenTofu uses the same state management concepts as Terraform:

* **Local state**: Stored temporarily during deployment
* **Remote state**: Recommended for production environments
* **State locking**: Prevents concurrent modifications

<Warning>
  **State persistence**

  env zero stores the local state between deployments by default. For production environments, configure a remote backend in your OpenTofu configuration to ensure state persistence and team collaboration.
</Warning>

### Variable handling

OpenTofu supports multiple variable input methods:

* **Environment variables**: Set in env zero's variable management
* **Variable files**: `.tfvars` files in your repository
* **Command-line variables**: Passed via `-var` flags
* **Variable precedence**: Command-line > environment > variable files

### Provider configuration

Configure OpenTofu providers in your configuration files:

```hcl main.tf theme={null}
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
```

## Deployment workflow

env zero follows OpenTofu's standard deployment workflow:

1. **Initialize**: `tofu init` - Download providers and modules
2. **Plan**: `tofu plan` - Generate execution plan
3. **Apply**: `tofu apply` - Execute the planned changes
4. **Destroy**: `tofu destroy` - Remove resources (when needed)

### Plan and apply process

The plan step generates a detailed execution plan showing what changes will be made. The apply step uses this plan to make the actual changes to your infrastructure.

<Info>
  env zero stores plan files between the plan and apply steps to ensure consistency and allow for review and approval workflows.
</Info>

## Best practices

### Remote backend configuration

Configure a remote backend for state management:

```hcl backend.tf theme={null}
terraform {
  backend "s3" {
    bucket         = "your-terraform-state-bucket"
    key            = "path/to/your/state.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

### Module usage

Organize your infrastructure using OpenTofu modules:

```hcl main.tf theme={null}
module "vpc" {
  source = "./modules/vpc"
  
  vpc_cidr = "10.0.0.0/16"
  environment = var.environment
}
```

### Variable management

Use consistent variable naming and types:

```hcl variables.tf theme={null}
variable "environment" {
  description = "Environment name"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

## Troubleshooting

### Common issues

**Provider version conflicts**

* Ensure provider versions are compatible with your OpenTofu version
* Check the [OpenTofu provider compatibility matrix](https://opentofu.org/docs/language/providers/)

**State file issues**

* Use remote backends for production environments
* Enable state locking to prevent concurrent modifications
* Regularly backup your state files

**Variable resolution**

* Check variable precedence order
* Verify environment variables are set correctly in env zero
* Use `tofu console` to debug variable values

### Debugging deployments

Enable detailed logging by setting the `TF_LOG` environment variable:

* `TF_LOG=DEBUG` - Most verbose logging
* `TF_LOG=INFO` - Standard information level
* `TF_LOG=WARN` - Warning and error messages only

<Info>
  Set the `TF_LOG` environment variable in your template's environment variables section for detailed OpenTofu execution logs.
</Info>

## Migration from Terraform

OpenTofu maintains compatibility with Terraform configurations:

1. **Configuration files**: No changes required to `.tf` files
2. **State files**: Compatible with Terraform state format
3. **Providers**: Use the same provider ecosystem
4. **Modules**: Existing Terraform modules work without modification

<Check>
  Your existing Terraform configurations will work with OpenTofu without any modifications.
</Check>

## Additional resources

* [OpenTofu Documentation](https://opentofu.org/docs/)
* [OpenTofu GitHub Repository](https://github.com/opentofu/opentofu)
* [Provider Registry](https://registry.opentofu.org/)
* [Migration Guide from Terraform](https://opentofu.org/docs/intro/terraform/)

Built with [Mintlify](https://mintlify.com).
