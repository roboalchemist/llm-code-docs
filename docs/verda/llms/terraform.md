# Source: https://docs.verda.com/infrastructure-as-code/terraform.md

# Terraform

Terraform allows you to manage Verda infrastructure declaratively using infrastructure as code. With the Verda Terraform provider, you can provision and maintain GPU compute instances, storage volumes, and container workloads in a reproducible and version-controlled way.

This section documents how to use Terraform to interact with Verda Cloud resources.

***

#### Quickstart

Add the Verda provider to your Terraform configuration:

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

Authentication is handled via environment variables:

```bash
export VERDA_CLIENT_ID="your-client-id"
export VERDA_CLIENT_SECRET="your-client-secret"
```

Once configured, you can start defining Verda resources such as compute instances, volumes, and containers.

***

#### Docs

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td>Getting Started</td><td><a href="terraform/getting-started">getting-started</a></td></tr><tr><td>Authentication</td><td><a href="terraform/authentication">authentication</a></td></tr><tr><td>Provider Configuration</td><td><a href="terraform/provider-configuration">provider-configuration</a></td></tr><tr><td>Compute – Instances</td><td><a href="terraform/compute-instances">compute-instances</a></td></tr><tr><td>Compute – SSH Keys</td><td><a href="terraform/compute-ssh-keys">compute-ssh-keys</a></td></tr><tr><td>Compute – Startup Scripts</td><td><a href="terraform/compute-startup-scripts">compute-startup-scripts</a></td></tr><tr><td>Storage – Volumes</td><td><a href="terraform/storage-volumes">storage-volumes</a></td></tr><tr><td>Containers – Containers</td><td><a href="terraform/containers-containers">containers-containers</a></td></tr><tr><td>Containers – Serverless Jobs</td><td><a href="terraform/containers-serverless-jobs">containers-serverless-jobs</a></td></tr></tbody></table>

#### What you can manage with Terraform

Using the Verda provider, you can manage:

* **Compute**
  * GPU instances
  * SSH keys for instance access
  * Startup scripts for automated provisioning
* **Storage**
  * Persistent NVMe volumes
  * Volume attachment to instances
* **Containers**
  * Serverless container deployments
  * Serverless batch jobs
  * Private container registry credentials
* **Lifecycle operations**
  * Create, update, and destroy resources
  * Import existing Verda resources into Terraform state

***

#### Documentation structure

The Terraform documentation is organized by resource type:

* **Getting Started** – Installing Terraform and verifying access
* **Authentication** – How Terraform authenticates with Verda
* **Provider Configuration** – Provider settings and options
* **Compute** – Instances, SSH keys, and startup scripts
* **Storage** – Persistent volumes
* **Containers** – Containers, serverless jobs, and registry credentials
* **Importing Existing Resources** – Bringing existing infrastructure under Terraform management

Use the navigation sidebar to jump directly to the resource you want to manage.

***

#### Terraform and OpenTofu compatibility

The Verda provider is compatible with both Terraform and OpenTofu.\
If you are using OpenTofu, see the **OpenTofu** section for registry configuration and migration notes.
