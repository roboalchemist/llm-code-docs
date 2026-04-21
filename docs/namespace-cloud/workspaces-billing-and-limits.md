<!-- Source: https://namespace.so/docs/workspaces/billing-and-limits -->

# Billing & Included Amounts

Learn how pricing works at Namespace, how we calculate usage and what to expect on your invoice.

## Plans we offer

Namespace provides several pricing tiers, starting from a pay-as you go option, to standard plans and custom options for
larger needs. Designed for everyone from a small team, to startups, to bigger organizations.

You can get started on a standard plan, available as self-service in the dashboard and scale up as your needs grow.

For teams with advanced requirements or custom workloads, we support custom plans and enterprise agreements. Reach out
to our [sales team](mailto:sales@namespace.so), and we'll work with you on an optimized plan for your needs.

You can view full details on [our pricing page](https://namespace.so/pricing).

## Included amounts by plan

Each plan (apart from the Developer plan which is pay-as-you-go) comes with included free usage and features. Custom
plans can be tailored to your exact needs.

For more details check out [our pricing page](https://namespace.so/pricing).

## Understanding your invoice

Your invoice is a breakdown of charges including the period they occurred for. It includes:

- pre-paid charges as agreed per contract for the next billing period and
- any charges for additional usage that occurred during previous periods.

You’ll be billed monthly for:

- **Your selected plan**, meaning pre-paid charges as agreed per contract for the next billing period.
  (i.e. $100 / mo for a Team plan)
- **Any additional usage** that occurred during previous periods.
  (i.e. unit minutes above your plan from the previous period).
- **Add-ons as per your custom contract** for the coming period (i.e. Bazel).

Individual line items in your invoice include:

- [Compute](/docs/architecture/compute)  
  Split by usage [included in your plan](/pricing) and additional usage during the previous period.  
  Namespace accounts compute usage based on unit minutes, a unit minute represents using 1 vCPU
  and 2GB of RAM for a minute times the platform multiplier (i.e. 1 for Linux).
- [Builds](/docs/solutions/docker-builders)  
  Usage split by the number of builds included in your plan and additional builds run during the
  previous period.
- [Cache Volumes Storage](/docs/architecture/storage/cache-volumes)  
  Split by the amount of Cache Volumes Storage included in your plan and additional cache volumes
  stored during the previous period. Cache Volumes storage is shown in GB-month.
- [Cache Volumes Snapshots Used](/docs/architecture/storage/cache-volumes)  
  Split by the amount of snapshots included in your plan and additional snapshots used during the
  previous period. Cache Volumes snapshots usage is shown in GB-hour.
- [Registry Storage](/docs/architecture/storage/container-registry)  
  Split by the amount of registry storage included in your plan and additional registry storage
  used during the previous period. Registry storage is shown in GB-month.
- [Registry Reads](/docs/architecture/storage/container-registry)  
  Usage split by the included number of reads in your plan and additional reads occurred during
  the previous period. Registry writes are not charged and therefore not part of the invoice. Registry
  usage is shown in GB.
- [Artifacts Storage](/docs/architecture/storage/artifact-storage)  
  Split by the amount of artifacts storage included in your plan and additional artifacts storage
  used during the previous period. Artifacts storage is shown in GB-month.
- [Artifacts Reads](/docs/architecture/storage/artifact-storage)  
  Usage split by the reads included in your plan and additional
  reads occurred during the previous period. Artifacts reads are shown in GB.
- [Turborepo Storage](/docs/integrations/turborepo)  
  Split by the amount of turborepo cache storage included in your plan and additional turborepo
  cache storage used during the previous period. Turborepo cache storage is shown in GB-month.
- [Turborepo Reads](/docs/integrations/turborepo)  
  Usage split by the included number of reads in your plan and additional reads occurred during
  the previous period. Turborepo writes are not charged and therefore not part of the invoice.
  Turborepo reads are shown in GB.
- [Bazel Storage](/docs/integrations/bazel)  
  Split by the amount of Bazel cache storage included in your plan and additional Bazel cache
  storage used during the previous period. Bazel cache storage is shown in GB-month.
- [Bazel Reads](/docs/integrations/bazel)  
  Usage split by the included number of reads in your plan and additional reads occurred during
  the previous period. Bazel writes are not charged and therefore not part of the invoice. Bazel
  reads are shown in GB.

For detailed billing information for each item as well as included amounts in your plans,
visit [the pricing page](https://namespace.so/pricing).

You can access your invoices as well as manage your plan and payment details in **Workspace Settings → Billing**.

## How to monitor usage

You can view your current usage as well as a prediction for the current period at any time in your dashboard:

- Go to [**Workspace Usage**](https://cloud.namespace.so/workspace/usage)
- See current usage and prediction for the current period in terms of:

  - [Compute](https://cloud.namespace.so/workspace/usage): Unit minutes and Builds
  - [Cache](https://cloud.namespace.so/workspace/usage?focus=storage): Cache storage, Cache snapshot usage and Cache Hit Ratio
  - [Resource](https://cloud.namespace.so/workspace/usage?focus=concurrency): CPU and Memory usage over all your workflows
    over time per platform

You can also go to our Usage Explorer for more options to filter and breakdown your usage over time.
Go to the [Usage Explorer](https://cloud.namespace.so/workspace/usage/explore) or [learn more](/docs/dashboard/usage-explorer) about it.

## FAQs

### Can I upgrade or downgrade my plan at any time?

If you are on a monthly contract, you can change plans anytime from **Workspace Settings → Billing**. Changes apply
immediately, and any prepaid charges are prorated.

For custom contracts, the terms from the contract apply.

### Do you offer custom pricing?

Yes! If you have specific needs, large-scale workloads, or security or compliance requirements, we’re happy to work
with you. Reach out to [sales@namespace.so](mailto:sales@namespace.so) and we’ll tailor a plan for you.

### Do I need to pay for each user?

No. There is no charge for users or seats. You only pay for your actual usage.

### What if I go over my plan limits?

Usage is tracked and billed automatically for your billing cycle. If during one billing cycle, your usage exceeds the
agreed included amounts, you’ll be charged for additional usage extra.
For example additional unit minutes are charged at $0.0015 / unit minute.

We always support our customers to find the best plan for them so that overage charges are kept to a minimum. Our sales
team reaches out to customers on a regular basis in case the plan you subscribed to is no longer optimal for your usage
and needs.

Find all details on additional charges on [our pricing page](https://namespace.so/pricing).

### How do I get a copy of my invoice?

Invoices are available for download in [**Workspace Settings → Billing**](https://cloud.namespace.so/workspace/settings/billing) under **Last invoices**. Each invoice includes a breakdown of
usage and charges.

### How can I specify my company name and tax ID?

If you go to [**Workspace Settings → Billing**](https://cloud.namespace.so/workspace/settings/billing) you can set a company name and a billing email.
Then, if you click on **Manage Billing Details**, you'll find a page which has an option **Update Information** which allows you to specify a tax ID.

---

If you have any questions about your bill or usage, our [support team](mailto:support@namespace.so)
will be happy to help.

Last updated February 17, 2026
