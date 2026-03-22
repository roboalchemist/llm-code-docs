<!-- Source: https://docs.verda.com/infrastructure-as-code/terraform/containers-serverless-jobs.md -->

# Containers – Serverless Jobs

Use Terraform to provision and manage **serverless container jobs** on Verda. Serverless jobs are designed for **finite, on-demand workloads** that run to completion and automatically release resources when finished.

Unlike long-running containers or services, serverless jobs do not stay active after execution. This makes them ideal for batch processing, scheduled tasks, and one-off compute workloads where you only pay for execution time.

***

## Typical use cases

Serverless jobs are well suited for:

* Batch data processing
* ETL and data transformation pipelines
* Model evaluation or offline inference
* Scheduled or event-driven tasks
* One-off administrative or maintenance jobs

***

## What this page covers

* Creating serverless jobs with Terraform
* Configuring container images and commands
* Passing environment variables and parameters
* Understanding job execution behavior
* Importing existing jobs into Terraform state

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

resource "verda_serverless_job" "example" {
  name  = "daily-etl-job"
  image = "ghcr.io/example/data-pipeline:1.0.0"

  command = [
    "python",
    "run_etl.py"
  ]

  cpu    = 2
  memory = 4096

  env = {
    ENVIRONMENT = "production"
    LOG_LEVEL   = "info"
  }
}

output "job_id" {
  value = verda_serverless_job.example.id
}
```

***

## Key concepts

### Job identity

The `name` field is a human-readable identifier for the job.

Always reference jobs using the Terraform-managed `id` when integrating with automation, monitoring, or external systems.

***

### Container image and command

Serverless jobs are created from **OCI-compatible container images**.

Best practices:

* Use immutable image tags (avoid `latest`)
* Ensure the container exits cleanly when the job completes
* Define job behavior explicitly using `command`, rather than relying on image defaults

If your image registry requires authentication, see **Containers – Registry Credentials**.

***

### Resource configuration

Serverless jobs allow you to specify resource limits such as:

* CPU allocation
* Memory limits
* (Optional) GPU resources, if supported

Choose resource values carefully to balance performance and cost. Over-allocating resources can increase execution cost without improving runtime.

***

### Environment variables

Environment variables allow you to parameterize job behavior without rebuilding images.

Example:

```hcl
env = {
  DATASET_PATH = "/data/input"
  MODE         = "batch"
}
```

For sensitive values, use Terraform variables or secret management rather than hardcoding values.

***

## Job execution behavior

Serverless jobs:

* Start when triggered by the platform or API
* Run until the container process exits
* Automatically stop and release resources upon completion

Jobs are **not restarted automatically** unless explicitly re-triggered. Design job logic to be **idempotent** whenever possible.

***

## Updating jobs safely

Most changes to a serverless job configuration (image, command, resources, or environment variables) will cause Terraform to **recreate the job definition**.

Best practices:

* Pin image versions explicitly
* Test changes in non-production environments
* Review `terraform plan` carefully before applying

***

## Import an existing job

If a serverless job already exists in Verda, you can import it into Terraform:

```bash
terraform import verda_serverless_job.example <job-id>
```

Then run:

```bash
terraform plan
```

Update your Terraform configuration until the plan shows no changes.

***

## Troubleshooting

**Job fails immediately**\
Verify the container image exists, the command is correct, and required environment variables are set.

**Unexpected job recreation**\
Changes to image tags, commands, CPU, memory, or environment variables typically force replacement.

**Image pull errors**\
Ensure registry credentials are configured correctly (see **Containers – Registry Credentials**).
