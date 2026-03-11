# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/remote-state-data-source.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote State Data Source

> Use terraform_remote_state data source to read outputs from env zero-managed remote state across stacks

Terraform allows you to utilize the remote state as a data source.  This is particularly useful for retrieving dependent information from a parent resource.

env zero's remote state can be used with [Terraform Remote State Data Source](https://developer.hashicorp.com/terraform/language/state/remote-state-data).

```hcl  theme={null}
data "terraform_remote_state" "example" {
  backend = "remote"

  config = {
    hostname     = "backend.api.env0.com"
    organization = "[ORGANIZATION_ID]"
    workspaces = {
      name = "[WORKSPACE_NAME]"
    }
  }
}
```

<Info>
  **The WORKSPACE\_NAME is unique per organization.**
</Info>

Here's an example of how its used:

```hcl  theme={null}
provider "aws" {
  region = "us-west-2"
}

data "terraform_remote_state" "vpc" {
  backend = "remote"

  config = {
    hostname     = "backend.api.env0.com"
    organization = "aaaaaaaa-bbbb-cccc-dddd-8f43fe49db92"
    workspaces = {
      name = "acme-fitness-agent-vpc"
    }
  }
}

output "vpc_id" {
  value = data.terraform_remote_state.vpc.outputs.vpc_id
}
```

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).
