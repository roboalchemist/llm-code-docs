<!-- Source: https://docs.verda.com/infrastructure-as-code/terraform/compute-instances.md -->

# Compute – Instances

Use Terraform to provision and manage Verda compute instances (CPU or GPU) declaratively. Instances are suitable for long-running workloads such as training jobs, interactive development, or services that require dedicated compute capacity.

***

## What this page covers

* Creating a compute instance with Terraform
* Common configuration options (instance type, image, disk, access)
* Managing instance lifecycle safely
* Importing existing instances into Terraform state

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

resource "verda_instance" "example" {
  name          = "training-01"
  instance_type = "gpu-a100-80gb"   # example
  image         = "ubuntu-22.04"    # example

  # Optional: root disk size (if supported by your instance type)
  # disk_size_gb = 200

  # Optional: attach SSH keys managed by Terraform
  # ssh_key_ids = [verda_ssh_key.main.id]

  # Optional: run a startup script on first boot
  # startup_script = file("${path.module}/startup.sh")
}

output "instance_id" {
  value = verda_instance.example.id
}

output "public_ip" {
  value = verda_instance.example.public_ip
}
```

***

## Key concepts

### Instance identity

The `name` field is a human-readable identifier for the instance.\
Use the Terraform-managed `id` output when referencing the instance from other resources such as volumes or firewall rules.

***

### Instance types

The `instance_type` defines the hardware configuration of the instance, including:

* CPU core count
* Memory
* GPU model and VRAM (for GPU instances)

Changing the `instance_type` usually requires the instance to be recreated. For a complete list of supported instance types, refer to the [Verda API documentation](https://api.verda.com/v1/docs#tag/instance-types).

***

### Images

The `image` field defines the operating system or base image used for the instance.

For reproducible deployments:

* Prefer explicit image versions
* Avoid floating aliases such as “latest” when possible

For a list of supported images, check [GET /images endpoint](https://api.verda.com/v1/docs#tag/images/GET/v1/images), `"image_type"` property.

***

### SSH access

SSH access is usually managed by attaching one or more SSH keys to the instance.

You can:

* Reference SSH keys created and managed by Terraform
* Reference existing SSH keys already registered in Verda

See **Compute – SSH Keys** for details.

***

### Startup scripts

Startup scripts allow you to run commands when the instance boots for the first time. Common use cases include:

* Installing system packages
* Pulling code repositories
* Configuring services
* Mounting storage volumes

Startup scripts are Script content. Example `#!/bin/bash echo hello world`

See **Compute – Startup Scripts**.

***

## Common configuration options

Verda compute instances commonly support:

* `name` – human-readable instance name
* `instance_type` – CPU/GPU hardware configuration
* `image` – operating system or base image
* `disk_size_gb` – root disk size (if configurable)
* `ssh_key_ids` – SSH keys allowed to access the instance
* `startup_script` – script executed on first boot

To see the exact schema supported by your provider version, run:

```bash
terraform providers schema -json | jq '.provider_schemas'
```

***

## Safe updates and lifecycle controls

Some changes (such as instance type or image) require destroying and recreating the instance.

To protect important instances, you can use lifecycle rules:

```hcl
resource "verda_instance" "example" {
  # ...

  lifecycle {
    prevent_destroy = true
  }
}
```

This is strongly recommended for production workloads.

***

## Import an existing instance

If an instance already exists in Verda, you can import it into Terraform:

```bash
terraform import verda_instance.example <instance-id>
```

Then run:

```bash
terraform plan
```

Adjust your Terraform configuration until the plan shows no changes.

***

## Troubleshooting

* **Authentication errors**\
  Ensure your Verda credentials are correctly set and accessible to Terraform.
* **Unexpected instance recreation**\
  Changes to `instance_type` or `image` often force replacement. Pin values explicitly.
* **SSH connectivity issues**\
  Verify the instance has a public IP, the correct SSH key is attached, and inbound SSH access is allowed.
