<!-- Source: https://docs.verda.com/infrastructure-as-code/terraform/containers-containers.md -->

# Containers – Containers

Use Terraform to provision and manage container workloads on Verda. Containers let you run services, batch workloads, and inference applications without managing virtual machines directly.

In Verda, containers are defined as standalone resources and fully managed by the platform. Terraform allows you to describe container configuration declaratively, enabling repeatable deployments, safe updates, and easy teardown.

***

## What this page covers

* Creating containers with Terraform
* Configuring container images and runtime resources
* Managing environment variables and execution settings
* Understanding container lifecycle and updates
* Importing existing containers into Terraform state

***

## Basic example

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

resource "verda_container" "example" {
  name  = "api-service"
  image = "ghcr.io/example/my-api:1.2.0"

  cpu    = 2
  memory = 4096

  env = {
    ENVIRONMENT = "production"
    LOG_LEVEL   = "info"
  }
}

output "container_id" {
  value = verda_container.example.id
}
```

***

## Key concepts

### Container identity

* The `name` field is a human-readable identifier.
* Always reference containers using the Terraform-managed `id` when integrating with other resources or automation.

***

### Container images

Containers are created from OCI-compatible images (Docker images).

**Best practices:**

* Use immutable image tags (for example `1.2.0` instead of `latest`)
* Store images in a trusted container registry
* Version images alongside your Terraform configuration

If your registry requires authentication, configure registry credentials separately (see **Containers – Registry Credentials**).

***

### Resource configuration

Containers typically support configuration for:

* CPU allocation
* Memory limits
* Optional GPU resources (if supported by the container type)

Choose resource values carefully:

* Under-provisioning can cause performance issues
* Over-provisioning increases cost unnecessarily

***

### Environment variables

Environment variables let you configure application behavior at runtime without rebuilding images.

Example:

```hcl
env = {
  API_KEY = var.api_key
  MODE    = "production"
}
```

For sensitive values, use Terraform variables or a secrets manager instead of hardcoding values.

***

## Updating containers safely

Most configuration changes—such as updating the image, CPU, memory, or environment variables—require **recreating the container**.

To reduce risk:

* Test changes in non-production environments first
* Use pinned image versions
* Always review `terraform plan` before applying changes

***

## Importing an existing container

If a container already exists in Verda, you can import it into Terraform state:

```bash
terraform import verda_container.example <container-id>
```

After importing, run:

```bash
terraform plan
```

Update your Terraform configuration until the plan shows no changes.

***

## Troubleshooting

**Container fails to start**\
Verify that the image exists and is accessible, and that CPU and memory limits are sufficient.

**Unexpected container recreation**\
Changes to image tags, CPU, memory, or environment variables typically force replacement.

**Image pull errors**\
Ensure registry credentials are configured correctly and accessible to Verda.
