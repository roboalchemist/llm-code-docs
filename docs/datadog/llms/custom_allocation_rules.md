# Source: https://docs.datadoghq.com/cloud_cost_management/allocation/custom_allocation_rules.md

---
title: Custom Allocation Rules
description: Allocate cloud costs based on custom allocation rules.
breadcrumbs: Docs > Cloud Cost Management > Cost Allocation > Custom Allocation Rules
---

# Custom Allocation Rules

## Overview{% #overview %}

Custom allocation rules let you split and assign shared costs to any available tags, such as teams, projects, or environments, supporting accurate showback and chargeback.

The following allocation methods are available:

| Allocation Method     | Description                                                      | Use Case                                                                                                | Example                                                                                                                             |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Even                  | Split costs evenly among all destinations.                       | Scenarios where each team, project, or environment should be charged the same amount for a shared cost. | Untagged support costs are allocated evenly to teams `teamA`, `teamB`, and `teamC`.                                                 |
| Custom                | Split costs to each destination based on percentages you define. | Scenarios where business rules or agreements dictate how much each team should pay.                     | Untagged support costs are allocated 60% to `teamA`, 30% to `teamB`, and 10% to `teamC`.                                            |
| Proportional by spend | Split costs based on each destination's share of total spend.    | Scenarios where teams should pay in proportion to their actual spend.                                   | Untagged support costs are allocated to teams `teamA`, `teamB`, and `teamC` based on their proportion of total spend on Amazon EC2. |
| Dynamic by metric     | Split costs based on each destination's share of total usage.    | Scenarios where teams should pay in proportion to their actual usage.                                   | Shared PostgreSQL costs are allocated by total query execution time per team.                                                       |

Custom allocation rules run after [Tag Pipelines](https://docs.datadoghq.com/cloud_cost_management/allocation/tag_pipelines/), enabling cost allocations on the latest user-defined tags. Costs are allocated on a daily basis. Cost allocations can be applied to AWS, Google Cloud, and Azure costs.

You can manage custom allocation rules using the [API](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/custom_allocation_rule), [Terraform](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-custom-allocation-rule), or directly in Datadog by following the instructions below.

## Create a custom allocation rule{% #create-a-custom-allocation-rule %}

### Step 1 - Define the source{% #step-1---define-the-source %}

1. Navigate to [Cloud Cost > Settings > Custom Allocation Rules](https://app.datadoghq.com/cost/settings/custom-allocation-rules) and click **Add New Rule** to start.

1. From the dropdown, select the shared costs you want to allocate.

*Example: Untagged support costs, shared database costs.*

### Step 2 - Choose an allocation method{% #step-2---choose-an-allocation-method %}

Below is a description of how each allocation method works with examples.

{% tab title="Even" %}

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/even_diagram.d1e05bc0a71fc0908309daf3c488845e.png?auto=format"
   alt="Diagram illustrating the even split strategy" /%}

With the even strategy, costs are allocated evenly towards your destination tags. Apply a filter to refine which part of the bill determines the proportions.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/ui-even.d555d257d4ad350846c0eaa08b2b3420.png?auto=format"
   alt="The even split strategy as seen in Datadog" /%}

{% /tab %}

{% tab title="Custom percentage" %}

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/custom_percentage_diagram.7d3aa59803d5d38028f080350a97b95c.png?auto=format"
   alt="Diagram illustrating the even split strategy" /%}

With the custom percentage strategy, you can define static custom percentages for the destination tags you select. For example, if you have 3 destinations (`teamA`, `teamB`, `teamC`) you can allocate 60% to `teamA`, 30% to `teamB`, and 10% to `teamC`.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/ui-custom.f5fc6701c308c643143506244e8e8064.png?auto=format"
   alt="The even split strategy as seen in Datadog" /%}

{% /tab %}

{% tab title="Proportional" %}

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/proportional_diagram-2.63cfc1275fd8e56cee35da7757a622b5.png?auto=format"
   alt="Diagram illustrating the proportional split strategy" /%}

Costs are allocated based on the proportional spend of destination values. Similarly to even allocation, you can further customize your allocation by setting filters and partitions.

In the preceding diagram, the pink bar represents a filter on the cost allocation. With this filter applied, EC2 support fees are split across teams *based on each team's share of overall EC2 spend*.

To create a rule for this allocation, you can:

- Define the costs to allocate (source): **EC2 support fees** (`aws_product:support`).
- Choose the allocation method: **Proportional by spend**.
- Choose the destination tag to split your costs by: **User** (`User A`, `User B`, `User C`).
- Refine the allocation by applying filters: **EC2** (`aws_product:ec2`).
- Create suballocations by partitioning the allocation rule: **environment** (`env`).

You can also specify how cost proportions should be partitioned to ensure segment-specific allocations. For example, if you partition your costs by environment using tags like `staging` and `production`, the proportions are calculated separately for each environment. This ensures allocations are based on the specific proportions within each partition.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/ui-proportional-by-spend.c27977e2d1724a47e989e764c4d13f3a.png?auto=format"
   alt="The proportional split strategy as seen in Datadog" /%}

{% /tab %}

{% tab title="Dynamic by metric" %}

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/dynamic_diagram.b3d6a43e4a91d6f282127fddb5c58af1.png?auto=format"
   alt="Diagram illustrating the dynamic by metric strategy" /%}

Metrics-based allocation provides the ability to split up costs based on Datadog's [metrics queries](https://docs.datadoghq.com/metrics/#querying-metrics). By using performance metrics to allocate expenses, you can more accurately allocate costs based on application usage patterns.

For example, this PostgreSQL metrics query `sum:postgresql.queries.time{*} by {user}.as_count()` tracks the total query execution time per user. The relative values are then used to determine what proportion of total PostgreSQL costs should be allocated to each user.

To create a rule for this allocation, you could:

- Define the costs to allocate (source): **PostgreSQL costs** (`azure_product_family:dbforpostgresql`).

- Choose the allocation method: **Dynamic by metric**

- Choose the destination tag to split your costs by: **User** (`User A`, `User B`, `User C`).

- Define the metric query used to split the source costs: **Query execution time per user** (`sum:postgresql.queries.time{*}` by `{user}.as_count`).

- Create suballocations by partitioning the allocation rule: **environment** (`env`).

  {% image
     source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/ui-dynamic-by-metric.2735313f01811b263e50183b90d859b9.png?auto=format"
     alt="The dynamic by metric split strategy as seen in Datadog" /%}

{% /tab %}

### Step 3 - Define the destination{% #step-3---define-the-destination %}

Decide which dimensions, such as `team`, `department`, or `service`, receive the allocated costs. For example:

You can select multiple values for your destination tag. For instance, if you select the `team` tag, you can choose specific teams like `teamA`, `teamB`, and `teamC` to receive the allocated costs.

### Step 4 - (optional) Apply filter(s){% #step-4---optional-apply-filters %}

Apply a filter across the entire allocation rule. Filters help you target the allocation rule to the relevant subset of your cloud spend.

*Example: Only apply cost allocation where environment is production.*

- **Proportional by spend**: Let's say you allocate shared costs to the team tag, proportional to how much each team spends. You can add a filter, creating a cost allocation that is proportional to how much team spends on `aws_product` is `ec2`.
- **Dynamic by metric**: Let's say you allocate shared PostgreSQL costs to the service tag, proportional to the query execution time of each service. You can add a filter, creating a cost allocation that only applies where `environment` is `production`.

### Step 5 - (optional) Apply a partition{% #step-5---optional-apply-a-partition %}

Partitioning allows you to split a single allocation rule into multiple sub-allocations. For example, instead of creating separate rules for each environment (like production and staging), you can create one rule that is partitioned by `environment`. Each partitioned sub-allocation uses the same allocation structure, but applies only to costs matching that tag value.

**Note**: For Dynamic by Metric, the tag you select to partition by must exist in both your cloud cost and metric data.

{% tab title="Even allocation" %}
With this partition, the same even allocation rule is applied to each environment.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/even_partition_diagram.5b460e52598618bdfa10b9cff77614d8.png?auto=format"
   alt="Diagram illustrating the even split strategy with partitioning" /%}

{% /tab %}

{% tab title="Proportional allocation" %}
With this partition, the same proportional allocation rule is applied to each environment.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/proportional_partition_diagram-2.ff8ba91f8aa612b64b1e7638aa46c43d.png?auto=format"
   alt="Diagram illustrating the proportional split strategy with partitioning" /%}

{% /tab %}

{% tab title="Dynamic by metric allocation" %}
With this partition, the same dynamic by metric allocation rule is applied to each environment.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/dynamic_partition_diagram.2f8321dacc7f38da897421d7d50a245b.png?auto=format"
   alt="Diagram illustrating the dynamic split strategy with partitioning" /%}

{% /tab %}

## Managing rules{% #managing-rules %}

Rules can be modified and deleted in the [Custom Allocation Rules section](https://app.datadoghq.com/cost/settings/custom-allocation-rules) of the Cloud Cost settings page. All fields except for the rule name can be reconfigured.

When you delete a custom allocation rule, the associated allocation is automatically removed from the current month and prior month's data within 24 hours. To remove allocations from older data, contact [Datadog support](https://www.datadoghq.com/support/) to request a backfill.

You can also disable a custom allocation rule without deleting it.

Rules are applied in the same order as shown in the list.

## Visualize your allocations{% #visualize-your-allocations %}

Changes to custom allocation rules may take up to 24 hours to be applied. After being applied, the new allocations can be seen throughout Cloud Cost Management. Custom allocated costs also include an `allocated_by_rule` tag, denoting the rule name that applied the allocation.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/custom_allocation_rules/visualize_your_allocations-1.44a6ecdabb8615c40c9963408d7d108a.png?auto=format"
   alt="See your allocations throughout Datadog" /%}

## Further reading{% #further-reading %}

- [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/?tab=aws#overview)
- [How we've created a successful FinOps practice at Datadog](https://www.datadoghq.com/blog/finops-at-datadog/)
