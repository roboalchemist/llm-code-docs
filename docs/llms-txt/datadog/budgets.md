# Source: https://docs.datadoghq.com/cloudcraft/api/budgets.md

# Source: https://docs.datadoghq.com/cloud_cost_management/planning/budgets.md

---
title: Budgets
description: >-
  After starting to ingest costs in Cloud Cost Management, set up budgets and
  visualize how you're tracking against them.
breadcrumbs: Docs > Cloud Cost Management > Planning > Budgets
---

# Budgets

## Overview{% #overview %}

Set up budgets and enable engineering teams to visualize how they are tracking against budgets.

You can create two types of budgets:

- **Basic**: A flat, single-level budget for tracking your cloud costs.
- **Hierarchical**: A two-level, parent-child budget for tracking costs in a way that mirrors your organization's structure. For example, if your organization has departments made up of many teams, you can budget on the department (parent) and team (child) levels and track budget health at both levels. In addition, this option allows you to create a single budget instead of needing to create multiple budgets.

## Set up budgets{% #set-up-budgets %}

{% tab title="Basic" %}
To create a basic budget:

1. Navigate to [**Cloud Cost > Plan > Budgets**](https://app.datadoghq.com/cost/plan/budgets), or create a budget through the [API](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-or-update-a-budget) or [Terraform](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/cost_budget).

1. Click the **Create a New Budget** button.

1. Click **Basic** to create a basic budget.

1. You can either add budget information by **uploading a CSV** using the provided template in the UI, or **enter your budget directly** using the details below.

   {% video
      url="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-upload-your-csv.mp4" /%}

   - **Budget Name**: Enter a name for your budget.
   - **Start Date**: Enter a start date for the budget (this can be a past month). Budgets are set at the month level.
   - **End Date**: Set an end date for the budget (can be in the future).
   - **Provider(s)**: Budget on any combination of AWS, Azure, Google Cloud, Oracle Cloud, or other SaaS (including Datadog or custom costs).
   - **Dimension to budget by**: Specify a dimension to track the budget, along with its corresponding values. For example, if you wanted to create budgets for the top 4 teams, you would select "team" in the first dropdown, and the specific teams in the second dropdown.

1. Fill in all budgets in the table. To apply the same values from the first month to the rest of the months, enter a value in the first column of a row and click the **copy** button.

   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-copy-paste.09a53072dbeb46690c92009452e1dfb7.png?auto=format"
      alt="Budget Creation View: fill in budget details." /%}

1. Click **Save**.

{% /tab %}

{% tab title="Hierarchical" %}
To create a hierarchical budget:

1. Navigate to [**Cloud Cost > Plan > Budgets**](https://app.datadoghq.com/cost/plan/budgets), or create a budget through the [API](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-or-update-a-budget).

1. Click the **Create a New Budget** button.

1. Click **Hierarchical** to create a hierarchical budget.

1. Enter your budget information using the details below.

   - **Budget Name**: Enter a name for your budget.
   - **Start Date**: Enter a start date for the budget (this can be a past month). Budgets are set at the month level.
   - **End Date**: Set an end date for the budget (can be in the future).
   - **Scope to Provider(s)**: Budget on any combination of AWS, Azure, Google Cloud, Oracle Cloud, or other SaaS (including Datadog or custom costs).
   - **Parent Level**: Select the parent-level tag.
   - **Child Level**: Select child-level tag.
   - **Dimension to budget by**: Specify a dimension to track the budget, along with its corresponding values. For example, if you wanted to create budgets for the top 4 teams, you would select "team" in the first dropdown, and the specific teams in the second dropdown.

1. Fill in all budgets in the table. To apply the same values from the first month to the rest of the months, enter a value in the first column of a row and click the **copy** button.

   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-copy-paste.09a53072dbeb46690c92009452e1dfb7.png?auto=format"
      alt="Budget Creation View: fill in budget details." /%}

1. Click **Save**.

{% /tab %}

## View budget status{% #view-budget-status %}

The [Budgets page](https://app.datadoghq.com/cost/plan/budgets) lists all of your organization's budgets, highlighting the budget creator, any budgets that have gone over, and other relevant details. Click on **View Performance** to investigate the budget, and understand what might be causing you to go over budget.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-list-1.c8e40d49c19557461b100ccc0432e53b.png?auto=format"
   alt="List all budgets" /%}

From a **View Performance** page of an individual budget, you can toggle the view option from the top left:

{% alert level="info" %}
You cannot view budget versus actuals before 15 months, since cost metrics are retained for 15 months.
{% /alert %}

- You can view the budget status for the **current month**:

  {% image
     source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-status-month-2.3283b41a02d9059f85c5927847f0a90b.png?auto=format"
     alt="Budget Status View: view current month" /%}

- Or you can view the budget status for the **entire duration (all)**:

  {% image
     source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-status-all-2.e87c5e2b69af7860011e1f95c81b0cbf.png?auto=format"
     alt="Budget Status View: view total budget" /%}

To investigate budgets:

1. From the individual budget page, filter budgets using the dropdown at the top, or "Apply filter" in the table to investigate the dimensions that are over budget.
   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-investigate-3.1108f1a4ac49f2b73efb17ea8e1ba29b.png?auto=format"
      alt="Use the dropdown filter or Apply Filter option in the table to investigate over-budget dimensions." /%}
1. Click **Copy Link** to share the budget with others to help understand why budgets are going over. Or, share budgets with finance so that they can understand how you're tracking against budgets.

## Modify or delete a budget{% #modify-or-delete-a-budget %}

To modify a budget, click the edit icon on the Budgets page.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-edit-1.9f9422c03e1b38f05a3fdbeecf8dd302.png?auto=format"
   alt="Click the edit icon to edit a budget" /%}

To delete a budget, click the trash icon on the Budgets page.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-delete-2.7cf35a67aa3cf7833f1c3d1217037fd8.png?auto=format"
   alt="Click the delete icon to delete a budget" /%}

## Add a budget to a dashboard{% #add-a-budget-to-a-dashboard %}

You can add a budget to dashboards in two ways:

- Create a budget report and click **Share > Save to dashboard**.

  {% image
     source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budget-share-from-dashboard.fcf6f68224a6f3da1ebfd00df8d06371.png?auto=format"
     alt="Click Share and Save to dashboard to add a budget report to a dashboard" /%}

- From a dashboard, add the **Budget Summary** widget.

  {% image
     source="https://datadog-docs.imgix.net/images/cloud_cost/budgets/budgets-widgets.58bee60fc4b226e0c7955b61c7a1de8d.png?auto=format"
     alt="Search and add the Budget Summary widget from any dashboard" /%}

## Create an alert for your budget{% #create-an-alert-for-your-budget %}

Learn how to [create a budget-based monitor](https://docs.datadoghq.com/cloud_cost_management/cost_changes/monitors/).

## Further Reading{% #further-reading %}

- [Manage and optimize your OCI costs with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/cloud-cost-management-oci)
- [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
