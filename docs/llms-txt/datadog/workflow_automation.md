# Source: https://docs.datadoghq.com/getting_started/workflow_automation.md

# Source: https://docs.datadoghq.com/account_management/billing/workflow_automation.md

---
title: Workflow Automation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > Workflow Automation
---

# Workflow Automation

## Overview{% #overview %}

Datadog [Workflow Automation](https://docs.datadoghq.com/actions/workflows/) billing is based on the number of **workflow executions**. Workflow executions are recorded whenever a published workflow runs, regardless of its run method (manually, programmatically, or automatically).

## Summary{% #summary %}

- **Billing metric**: You incur a cost per committed execution or on-demand execution, depending on your billing plan. Specific pricing can be found on the [Workflow Automation pricing page](https://www.datadoghq.com/pricing/?product=workflow-automation#products).
- **Scope**: All published executions are billed, regardless of success/failure.
- **Visibility**: Usage and cost breakdowns are available in [Plan & Usage](https://app.datadoghq.com/billing/usage?selected_cost_products=workflow_execution).
- **Exceptions for certain SKUs**:
  - CSM/DevSecOps SKUs include 5-20 executions per host.
  - [Incident Management](https://docs.datadoghq.com/incident_response/incident_management/), [On-Call](https://docs.datadoghq.com/incident_response/on-call/), and [App Builder](https://docs.datadoghq.com/actions/app_builder/) SKUs include free unlimited executions when triggered by events from these products.

## Pricing model{% #pricing-model %}

### Definition of workflow execution{% #definition-of-workflow-execution %}

A workflow execution refers to one full run of a published workflow, regardless of how many steps or actions it includes. Executions can be triggered through:

- Manual starts in the Datadog UI
- API or programmatic triggers
- Event-based triggers (monitors, incidents, etc.)
- Workflows triggered from other workflows
  - **Note**: If one workflow triggers another workflow, they are both counted for billing.

Unpublished (test or draft) runs are **not billed**.

{% alert level="info" %}
Failed executions are not exempt from billing. All published executions are billed once they successfully start, regardless of success or failure. This includes runs that:
- Fail due to an error.
- Are interrupted or canceled.
- Time out mid-run.

{% /alert %}

### Billing metrics{% #billing-metrics %}

Workflow Automation is billed **per execution**. This means that each complete workflow run counts toward your bill.

The two billing options are committed executions and on-demand executions. Committed executions are purchased in advance, while on-demand executions are billed as they occur. Prepaid executions cost less than on-demand executions.

### Usage tracking{% #usage-tracking %}

The best source of truth for billing is on your [Datadog Plan & Usage page](https://app.datadoghq.com/billing/usage?selected_cost_products=workflow_execution), where execution usage is continuously tracked. Under **Products**, select only **Workflow Executions** for the filter. If you have multiple Datadog orgs, you can filter for them under **Sub-Orgs**. You can also filter further by team or any other tag in the **Usage Attribution** tab.

Other sources of usage tracking that do not include billing metrics are the [Workflow Automation API](https://docs.datadoghq.com/api/latest/workflow-automation/) and the [Workflows Overview dashboard](https://app.datadoghq.com/dash/integration/30994/workflows-overview?fromUser=false&refresh_mode=sliding&from_ts=1760203373269&to_ts=1762885373269&live=true). Through the API, you can view granular information such as [all instances of a given workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#list-workflow-instances). The Workflows Overview dashboard is based on execution metrics, before any billing considerations take place. Additionally, the dashboard does not reflect billing complexities such as free allotments of workflows.

## Included workflow allotments by SKU{% #included-workflow-allotments-by-sku %}

Certain Datadog SKUs include Workflow Automation allotments as part of their pricing:

| SKU                                                                                                   | Included Workflow Executions | Allotment Basis |
| ----------------------------------------------------------------------------------------------------- | ---------------------------- | --------------- |
| [CSM Pro](https://www.datadoghq.com/pricing/?product=cloud-security#products)                         | 5 executions per host        | Monthly         |
| [DevSecOps Pro](https://www.datadoghq.com/pricing/?product=infrastructure-monitoring#products)        | 5 executions per host        | Monthly         |
| [CSM Enterprise](https://www.datadoghq.com/pricing/?product=cloud-security#products)                  | 20 executions per host       | Monthly         |
| [DevSecOps Enterprise](https://www.datadoghq.com/pricing/?product=infrastructure-monitoring#products) | 20 executions per host       | Monthly         |

These included executions are automatically applied to your account each month and used before any committed or on-demand executions. They are not reflected in [your Plan & Usage page](https://app.datadoghq.com/billing/usage?selected_cost_products=workflow_execution) and do not show up on your bill.

### Included automations{% #included-automations %}

Workflows triggered automatically or manually by events from the following products are **free** and included in their respective SKU pricing:

- [**Incident Management**](https://docs.datadoghq.com/incident_response/incident_management/)
- [**On-Call**](https://docs.datadoghq.com/incident_response/on-call/)
- [**App Builder**](https://docs.datadoghq.com/actions/app_builder/)

This means that if your automation originates from one of these services, those executions **do not count** toward your Workflow Automation bill. For example, a workflow triggered by an incident creation or an on-call handover does not incur a cost.
