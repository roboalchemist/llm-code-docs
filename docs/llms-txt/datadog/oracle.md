# Source: https://docs.datadoghq.com/cloud_cost_management/setup/oracle.md

---
title: Oracle
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloud Cost Management > Setup > Oracle
source_url: https://docs.datadoghq.com/setup/oracle/index.html
---

# Oracle

## Overview{% #overview %}

To set up Cloud Cost Management for Oracle Cloud Infrastructure (OCI) in Datadog, you should:

1. Have an OCI tenancy
1. Have the [OCI integration](https://docs.datadoghq.com/integrations/oracle-cloud-infrastructure/) installed in Datadog

## Setup{% #setup %}

### Configure the OCI integration{% #configure-the-oci-integration %}

Navigate to [Setup & Configuration](https://app.datadoghq.com/cost/setup?cloud=oracle) and follow the steps to configure the OCI integration for your parent tenancy.

**Note**: If the OCI integration was created without the QuickStart method, then you need to follow the [documentation](https://docs.datadoghq.com/integrations/oracle-cloud-infrastructure/?tab=createvcnrecommended#oci-integration-manual-to-quickstart-migration) for QuickStart migration.

### Enable Cloud Cost Management{% #enable-cloud-cost-management %}

Once the integration is created, enable the toggle for Cloud Cost Management.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/oci/oci_ccm_enablement.22f8110fe7397a57cc82558d4d8a5b93.png?auto=format"
   alt="Toggle for enabling Cloud Cost Management" /%}

### Getting historical data{% #getting-historical-data %}

Oracle Cloud Infrastructure retains cost reports for 1 year. When you enable Cloud Cost Management, Datadog automatically ingests up to 15 months of available historical cost data from these retained reports (up to 1 year based on Oracle's retention).

Oracle does not provide a process for backfilling additional historical data beyond what is already retained in the cost reports.

## Cost types{% #cost-types %}

You can visualize your ingested data using the following cost types:

| Cost Type            | Description                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `oci.cost.amortized` | Total cost of resources allocated at the time of usage over an interval. Costs include all applicable discounts. |
| `oci.cost.ondemand`  | Total public, on-demand cost of resources before public and private discounts are applied over an interval.      |

### Out-of-the-box tags{% #out-of-the-box-tags %}

Datadog adds out-of-the-box tags to ingested cost data and help you further break down and allocate your costs. These tags are derived from your [FOCUS cost export](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm) and make it easier to discover and understand cost data.

The following out-of-the-box tags are available for filtering and grouping data:

| Tag Name                     | Tag Description                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `availabilityzone`           | A provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance.                                           |
| `billingaccountid`           | The identifier assigned to a billing account by the provider.                                                                                                                              |
| `billingaccountname`         | The display name assigned to a billing account.                                                                                                                                            |
| `billingcurrency`            | An identifier representing the currency that a charge for resources or services was billed in.                                                                                             |
| `chargecategory`             | The top-level type of charge in a billing row.                                                                                                                                             |
| `chargedescription`          | A self-contained summary that explains the purpose and price of a charge.                                                                                                                  |
| `chargefrequency`            | An indication of how often a charge occurs, helping to identify if it's recurring, and to forecast future charges.                                                                         |
| `chargesubcategory`          | Represents the sub-level classification of a charge based on the nature of how it is billed.                                                                                               |
| `commitmentdiscountcategory` | Whether the usage was reserved but not used.                                                                                                                                               |
| `commitmentdiscountid`       | The identifier assigned to a commitment discount by the provider.                                                                                                                          |
| `commitmentdiscountname`     | The display name assigned to a commitment discount.                                                                                                                                        |
| `commitmentdiscounttype`     | A provider-assigned name to identify the type of commitment discount applied.                                                                                                              |
| `invoiceissuer`              | The entity responsible for invoicing for the resources or services consumed.                                                                                                               |
| `pricingcategory`            | Describes the pricing model used for a charge at the time of use or purchase.                                                                                                              |
| `pricingunit`                | Provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage and purchase quantities after applying pricing rules like block pricing. |
| `providername`               | The name of the entity that made the resources or services available for purchase.                                                                                                         |
| `publishername`              | The name of the entity that produces the resources or services that were purchased.                                                                                                        |
| `region`                     | A provider-assigned display name for an isolated geographic area where a resource is provisioned or a service is provided.                                                                 |
| `resourceid`                 | An identifier assigned to a resource by the provider.                                                                                                                                      |
| `resourcename`               | A display name assigned to a resource.                                                                                                                                                     |
| `resourcetype`               | Describes the kind of resource the charge applies to.                                                                                                                                      |
| `servicecategory`            | The highest-level classification of a service based on the core function of the service.                                                                                                   |
| `servicename`                | An offering that can be purchased from a provider (e.g., cloud virtual machine, SaaS database, professional services from a systems integrator).                                           |
| `skuid`                      | A provider-specified unique identifier that represents a specific SKU.                                                                                                                     |
| `skupriceid`                 | A provider-specified unique identifier that represents a specific SKU Price associated with a resource or service used or purchased.                                                       |
| `subaccountid`               | An ID assigned to a grouping of resources or services, often used to manage access and/or cost.                                                                                            |
| `subaccountname`             | A name assigned to a grouping of resources or services, often used to manage access and/or cost.                                                                                           |
| `usageunit`                  | A provider-specified measurement unit, indicating how the provider rates measured usage and purchase quantities.                                                                           |

#### Cost and observability correlation{% #cost-and-observability-correlation %}

Viewing costs in the context of observability data is important for understanding how infrastructure changes impact costs, identifying why costs change, and optimizing infrastructure for both costs and performance.

Datadog updates resource identifying tags on cost data for top OCI products to simplify correlating observability and cost metrics. For example, to view cost and utilization for each Compute instance, you can make a table with `oci.cost.amortized`, `oci.computeagent.cpu_utilization`, and `oci.computeagent.memory_utilization` (or any other Compute metric) and group by `host`. To see Object Storage usage and costs side by side, you can graph `oci.objectstorage.stored_bytes` and `oci.cost.amortized` grouped by `name`.

The following out-of-the-box tags are available:

| OCI Product    | Tag(s) |
| -------------- | ------ |
| Compute        | `host` |
| Object Storage | `name` |

Additionally, Datadog provides the following tags that can be used with many observability metrics. For example, to view cost and execution duration of OCI Functions for each compartment, you can make a table with `oci.cost.amortized`, `oci.faas.function_execution_duration`, and group by `compartment_id`.

| Tag Name           | Tag Description                                                                         |
| ------------------ | --------------------------------------------------------------------------------------- |
| `compartment_id`   | The identifier (OCID) for the compartment.                                              |
| `compartment_name` | The name for the compartment.                                                           |
| `tenancy_ocid`     | The identifier (OCID) for the OCI tenant.                                               |
| `tenancy_name`     | The name for the OCI tenant.                                                            |
| `resource_id`      | An identifier assigned to a resource by the provider.                                   |
| `resource_type`    | Describes the kind of resource the charge applies to.                                   |
| `dd_resource_key`  | The Canonical Cloud Resource Identifier (CCRID) for the resource. Same as OCID for OCI. |

### Container cost allocation{% #container-cost-allocation %}

Container cost allocation is not available for OCI. See [Container Cost Allocation](https://docs.datadoghq.com/cloud_cost_management/allocation/container_cost_allocation/) for more details.

## Further reading{% #further-reading %}

- [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
- [Gain insights into your AWS bill](https://docs.datadoghq.com/cloud_cost_management/setup/aws)
- [Gain insights into your Azure bill](https://docs.datadoghq.com/cloud_cost_management/azure)
- [Gain insights into your Google Cloud bill](https://docs.datadoghq.com/cloud_cost_management/setup/google_cloud)
