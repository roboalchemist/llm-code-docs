# Source: https://docs.verda.com/infrastructure-as-code/terraform/getting-started.md

# Getting Started

This guide helps you get up and running with Terraform on Verda. By the end of this page, you will have Terraform installed, the Verda provider configured, and be ready to provision your first resources.

***

#### Prerequisites

Before you begin, make sure you have:

* A **Verda account** with API access enabled
* A **Client ID** and **Client Secret** for the Verda API
* **Terraform 1.1.0 or newer** installed\
  (OpenTofu users can follow the same steps with OpenTofu 1.6+)
* Basic familiarity with **HCL (HashiCorp Configuration Language)**

***

#### Install Terraform

If Terraform is not already installed, follow the official installation instructions for your platform:

* macOS (Homebrew)
* Linux (package manager or binary)
* Windows

After installation, verify it works:

```bash
terraform version
```

You should see Terraform 1.x listed.

***

#### Create a Terraform project

Create a new directory for your Terraform configuration:

```bash
mkdir verda-terraform
cd verda-terraform
```

Inside this directory, create a file named `main.tf`.

***

#### Configure the Verda provider

Add the Verda provider to your configuration:

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

This tells Terraform to download the Verda provider from the registry.

***

#### Configure authentication

The Verda provider authenticates using environment variables.

Set the following variables in your shell:

```bash
export VERDA_CLIENT_ID="your-client-id"
export VERDA_CLIENT_SECRET="your-client-secret"
```

> For security reasons, avoid hardcoding credentials directly in Terraform files.\
> Environment variables are recommended for local use and CI/CD pipelines.

***

#### Initialize Terraform

Initialize the working directory to download the provider:

```bash
terraform init
```

If successful, Terraform will report that the Verda provider has been installed.

***

#### Verify the setup

You can now verify your setup by running:

```bash
terraform plan
```

At this point, your configuration does not define any resources yet, so Terraform should report that no changes are required.

***

#### Next steps

You’re now ready to start managing Verda resources with Terraform.

Next, explore:

* **Authentication** – detailed authentication options and best practices
* **Provider Configuration** – provider settings and advanced configuration
* **Compute** – provisioning GPU instances, SSH keys, and startup scripts
* **Storage** – managing persistent volumes
* **Containers** – deploying containers and serverless jobs
