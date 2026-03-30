# Source: https://docs.rootly.com/integrations/terraform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Terraform

> Manage Rootly resources using infrastructure as code with the official Terraform provider for services, severities, workflows, and more.

Our Terraform provider is available at:

[https://registry.terraform.io/providers/rootlyhq/rootly/latest](https://registry.terraform.io/providers/rootlyhq/rootly/latest "https://registry.terraform.io/providers/rootlyhq/rootly/latest")﻿

## Documentation

[https://registry.terraform.io/providers/rootlyhq/rootly/latest/docs](https://registry.terraform.io/providers/rootlyhq/rootly/latest/docs "https://registry.terraform.io/providers/rootlyhq/rootly/latest/docs")﻿

## Example

```tf main.tf theme={null}
terraform {
  required_providers {
    rootly = {
      source = "rootlyhq/rootly"
    }
  }
}

# Configure the Rootly provider
provider "rootly" {
  # We recommend using the `ROOTLY_API_TOKEN` env var to set the API Token
  # when interacting with Rootly's API.
  # api_token = "<YOUR API KEY>"
}

# Severities
resource "rootly_severity" "sev0" {
  name = "SEV0"
  color = "#FF0000"
}

resource "rootly_severity" "sev1" {
  name = "SEV1"
  color = "#FFA500"
}

resource "rootly_severity" "sev2" {
  name = "SEV2"
  color = "#FFA500"
}

# Services
resource "rootly_service" "elasticsearch_prod" {
  name = "elasticsearch-prod"
  color = "#800080"
}

resource "rootly_service" "customer_postgresql_prod" {
  name = "customer-postgresql-prod"
  color = "#800080"
}

# Functionalities
resource "rootly_functionality" "add_items_to_card" {
  name = "Add items to cart"
  color = "#800080"
}

resource "rootly_functionality" "logging_in" {
  name = "Logging In"
  color = "#800080"
}

# Custom Form Fields
resource "rootly_form_field" "regions_affected" {
  name = "Regions affected"
  kind = "custom"
  input_kind = "multi_select"
  shown = ["web_new_incident_form", "web_update_incident_form"]
  required = ["web_new_incident_form", "web_update_incident_form"]
}

resource "rootly_form_field_option" "asia" {
  form_field_id = rootly_form_field.regions_affected.id
  value = "Asia"
}

resource "rootly_form_field_option" "europe" {
  form_field_id = rootly_form_field.regions_affected.id
  value = "Europe"
}

resource "rootly_form_field_option" "north_america" {
  form_field_id = rootly_form_field.regions_affected.id
  value = "North America"
}

# Jira workflow
resource "rootly_workflow_incident" "jira" {
  name        = "Create a Jira Issue"
  description = "Open Jira ticket whenever incident starts"
  trigger_params {
    triggers                  = ["incident_created"]
    incident_condition_kind   = "IS"
    incident_kinds            = ["normal"]
    incident_condition_status = "IS"
    incident_statuses         = ["started"]
  }
  enabled = true
}

resource "rootly_workflow_task_create_jira_issue" "jira" {
  workflow_id = rootly_workflow_incident.jira.id
  task_params {
    title       = "{{ incident.title }}"
    description = "{{ incident.summary }}"
    project_key = "ROOT"
    issue_type = {
      id   = "10001"
      name = "Task"
    }
    status = {
      id   = "10000"
      name = "To Do"
    }
    labels = "{{ incident.environment_slugs | concat: incident.service_slugs | concat: incident.functionality_slugs | concat: incident.group_slugs | join: \",\" }}"
  }
}
```


Built with [Mintlify](https://mintlify.com).