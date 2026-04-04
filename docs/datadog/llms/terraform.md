# Source: https://docs.datadoghq.com/getting_started/integrations/terraform.md

---
title: Getting Started with Terraform
description: >-
  Use the Datadog Terraform provider to programmatically create and manage
  Datadog resources. Configure cloud integrations, monitors, dashboards, and
  other resources with Terraform.
breadcrumbs: >-
  Docs > Getting Started > Introduction to Integrations > Getting Started with
  Terraform
---

# Getting Started with Terraform

## Overview{% #overview %}

You can use the [Datadog Terraform provider](https://registry.terraform.io/providers/DataDog/datadog/latest/docs) to create and programmatically manage Datadog resources. This guide provides an overview of getting started with Terraform, with links to Terraform resources and tutorials that address specific use cases.

## Setup{% #setup %}

1. If you haven't already, install [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli).
1. If you don't yet have a Terraform configuration file, read the [configuration section](https://docs.datadoghq.com/integrations/terraform/#configuration) of the main Terraform documentation to create a directory and configuration file.
1. From the directory that contains your Datadog Provider configuration, run `terraform init`.

## Resources{% #resources %}

### Cloud integrations{% #cloud-integrations %}

The [AWS integration resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_aws), [Azure integration resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_azure), and [Google Cloud Project integration resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_gcp_sts) can establish the connections to quickly get data flowing into your Datadog account from your [AWS](https://docs.datadoghq.com/integrations/amazon_web_services/), [Azure](https://docs.datadoghq.com/integrations/azure/), and [Google Cloud](https://docs.datadoghq.com/integrations/google_cloud_platform/) services, respectively. If you're using the AWS integration, see the [AWS integration with Terraform](https://docs.datadoghq.com/integrations/guide/aws-terraform-setup) guide for an example of setting up the integration along with its associated IAM role and permissions.

### Logs and Metrics{% #logs-and-metrics %}

See the [Manage Logs and Metrics with Terraform guide](https://docs.datadoghq.com/logs/guide/manage_logs_and_metrics_with_terraform/) for instructions on managing your logs and metrics with Terraform.

### Monitors{% #monitors %}

With data flowing into your Datadog account, implement [alerting with Datadog monitors](https://docs.datadoghq.com/monitors/) to be notified about any unexpected changes or anomalous behavior. Use the [monitor resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/monitor) to create and manage your monitors, or use the [monitor JSON resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/monitor_json) to use JSON definitions for your monitors. See the [create a monitor](https://docs.datadoghq.com/integrations/terraform/#create-a-monitor) section of the main Terraform documentation for an example `monitor.tf` file that creates a [Live Process monitor](https://docs.datadoghq.com/monitors/types/process/).

### Account management{% #account-management %}

See the [Manage Datadog with Terraform guide](https://docs.datadoghq.com/account_management/guide/manage-datadog-with-terraform/) for instructions on managing your Datadog account with Terraform.

### Dashboards{% #dashboards %}

To further analyze or display your data for an audience, create [Datadog dashboards](https://docs.datadoghq.com/dashboards/). Terraform provides the [dashboard resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/dashboard) for this, or you can use the [dashboard JSON resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/dashboard_json) to create dashboards with JSON definitions. You can also [restrict the editing of a dashboard](https://docs.datadoghq.com/dashboards/guide/how-to-use-terraform-to-restrict-dashboard-edit/) by configuring restricted roles.

### Synthetic tests{% #synthetic-tests %}

- For API tests, see the [Terraform section](https://docs.datadoghq.com/synthetics/guide/create-api-test-with-the-api/#terraform) of the **Create An API Test With The API** page.
- For Browser tests, see the [Terraform section](https://docs.datadoghq.com/synthetics/guide/manage-browser-tests-through-the-api/#manage-your-browser-tests-with-terraform) of the **Manage Your Browser Tests Programmatically** page.

### Webhooks{% #webhooks %}

You can send custom API requests and payloads to your own services in response to the data in your Datadog account with [Webhooks](https://docs.datadoghq.com/integrations/webhooks/). This allows you to alert your services or initiate automated actions in your infrastructure. Use the Terraform [Webhook resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/webhook) to create and manage your webhooks with Terraform.

## Go further with Terraform{% #go-further-with-terraform %}

Follow the [Terraform Datadog Provider](https://developer.hashicorp.com/terraform/tutorials/use-case/datadog-provider) tutorial for a detailed walk-through of implementing and managing Datadog with Terraform, including the deployment of an example Kubernetes application with the Datadog Agent and the creation of [synthetic tests](https://docs.datadoghq.com/synthetics/).

## Further Reading{% #further-reading %}

- [Managing Datadog with Terraform](https://www.datadoghq.com/blog/managing-datadog-with-terraform/)
