# Source: https://planetscale.com/docs/planetscale-plans.md

# PlanetScale plans

## Overview

PlanetScale is built to accommodate all companies at all stages. Whether you need a hassle-free managed database for your side project or you’re running millions of queries per second at the scale of YouTube, we have a solution for you.

Our plans are split into two general offerings: [Base (self-serve)](#base) and [Enterprise](#planetscale-enterprise-plan).

<Columns cols={2}>
  <Card title="Base" icon="database" href="#base">
    PlanetScale for Vitess offers fully-managed Vitess clusters with unlimited scalability. Features include sharding, branching, deploy requests, query insights, and more.

    <a href="/docs/vitess">View the Vitess docs</a>
  </Card>

  <Card title="Enterprise" icon="rocket" href="#planetscale-enterprise-plan">
    PlanetScale Postgres is a fully-managed PostgreSQL-compatible database. Features include high availability, query insights, branching, and more.

    <a href="/docs/postgres">View the Postgres docs</a>
  </Card>
</Columns>

## Base

Our base plan is completely self-serviceable. Just sign up for a PlanetScale account to get started.

PlanetScale databases come in two flavors: **network-attached storage** and **Metal**.
[Network-attached storage](/docs/plans/planetscale-skus#network-attached-storage) (Amazon Elastic Block Storage or Google Persistent Disk) databases come with autoscaling storage and have varying levels of compute power.
[Metal databases](/docs/plans/planetscale-skus#metal) are backed by locally-attached NVMe drives for storage, unlocking incredible performance and cost-efficiencies. Because the drives are locally-attached, you need to choose both your compute and storage resources when you create your database.

<Note>
  Cluster size options are capped to `PS-160` and `M-320` SKUs until you have a successfully paid an invoice of at least \$100.
  If you need larger sizes immediately, please [contact us](https://planetscale.com/contact) to unlock all sizes.
</Note>

On top of processing and memory, all **Base** cluster sizes share the following:

|                                                                   | **Vitess**                                                                                                    | **Postgres**                                                                                                                                              |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Storage/month (network-attached storage)**                      | 10 GB included; \$0.50 per instance per additional 1 GB\*                                                     | 10 GB included; \$0.50 per instance per additional 1 GB\*                                                                                                 |
| **Storage/month (Metal)**                                         | Depends on selected NVMe drive size                                                                           | Depends on selected NVMe drive size                                                                                                                       |
| **Row reads/month**                                               | *Unmetered*                                                                                                   | *Unmetered*                                                                                                                                               |
| **Row writes/month**                                              | *Unmetered*                                                                                                   | *Unmetered*                                                                                                                                               |
| **Available cluster sizes**                                       | 22                                                                                                            | 22                                                                                                                                                        |
| **Availability zones**                                            | 3                                                                                                             | 3                                                                                                                                                         |
| **Production branches**                                           | 1 included\*\*                                                                                                | 1 included                                                                                                                                                |
| **Development branches**                                          | \~1,440 hours included (2× hours of current month)                                                            | Billed as a new cluster                                                                                                                                   |
| **Concurrent Connections**                                        | *Unmetered*                                                                                                   | *Unmetered*                                                                                                                                               |
| **Single node**                                                   | Not available                                                                                                 | Available starting at \$5/mo                                                                                                                              |
| **Query Insights retention**                                      | 7 days                                                                                                        | 7 days                                                                                                                                                    |
| **Horizontal sharding**                                           | Included                                                                                                      | [Coming soon](https://planetscale.com/blog/announcing-neki)                                                                                               |
| **Vertical sharding**                                             | Included                                                                                                      | Included                                                                                                                                                  |
| [**Deployment options**](/docs/plans/deployment-options)          | Multi-tenant                                                                                                  | Multi-tenant                                                                                                                                              |
| **Read-only regions**                                             | Available as an add-on                                                                                        | Coming soon                                                                                                                                               |
| **Web console**                                                   | Included                                                                                                      | Not available                                                                                                                                             |
| **PlanetScale CLI**                                               | Included                                                                                                      | Included                                                                                                                                                  |
| **Connection pooling**                                            | [VTGates](/docs/vitess/scaling/vtgates) based on cluster size                                                 | [PgBouncer](/docs/postgres/connecting/pgbouncer)                                                                                                          |
| **SSO**                                                           | Available as an add-on\*\*\*                                                                                  | Available as an add-on\*\*\*                                                                                                                              |
| **Audit log retention**                                           | 6 months                                                                                                      | 6 months                                                                                                                                                  |
| **Private connections**                                           | [AWS](/docs/vitess/connecting/private-connections) and [GCP](/docs/vitess/connecting/private-connections-gcp) | [AWS](/docs/postgres/connecting/private-connections/aws-privatelink) and [GCP](/docs/postgres/connecting/private-connections/gcp-private-service-connect) |
| **BAAs**                                                          | Included                                                                                                      | Included                                                                                                                                                  |
| **Automatic backups**                                             | Every 12 hours                                                                                                | Every 12 hours                                                                                                                                            |
| **Support**                                                       | Standard, upgrade available\*\*\*                                                                             | Standard, upgrade available\*\*\*                                                                                                                         |
| [**Data Branching®**](/docs/vitess/schema-changes/data-branching) | Included                                                                                                      | Not available                                                                                                                                             |

\* For HA network-attached storage databases, production branch storage is billed at $1.50/GB (1 primary + 2 replicas) and development branch storage is billed at $0.50/GB (1 primary).

\*\* Additional production branches are billed at the cost of your selected cluster size per month.

\*\*\* [SSO](/docs/security/sso) and [Business support](/docs/support#business) options are available on the base plan for an additional fee.

### Additional production branches

Each HA production branch in the base plan provisions a separate, production database cluster in our infrastructure. Upon adding an additional production branch, you will be prompted to select the cluster size for the new branch.

Each cluster size is priced based on the selected region. You can find the full list of pricing in our [Vitess cluster pricing documentation](/docs/plans/cluster-sizing).

If you have a `main` network-attached storage production branch using the **PS-40** cluster size and two additional production branches using the **PS-20** cluster size, the total cost for the database would be **\$217.00** per month.

| **Production branch cluster** | **Cost per unit** | **Quantity** | **Total per month** |
| :---------------------------- | :---------------- | :----------- | :------------------ |
| PS-40                         | \$99.00           | 1            | \$99.00             |
| PS-20                         | \$59.00           | 2            | \$118.00            |
| **Grand total**               |                   |              | **\$217.00**        |

Also note that pricing is prorated.
If you create a new database in the middle of a billing cycle, you will only be charged for the appropriate fraction of the month.
This also applies to changes to an existing database, such as upsizing.
For example, if you have a database that started the month as a `PS-10` and at the halfway point in the month you upgrade to a `PS-20`, you would be charged $39/2 + $59/2 = \$49 (assuming no additional other charges for storage, etc). The billing for the new sizes begins as soon as you begin the cluster resize.

### Development branches

Billing for development branches differs depending on whether you're using PlanetScale Postgres or Vitess.

### Vitess development branches

Development branches, `PS-DEV` are billed for the time that they are running, prorated to the nearest second. Databases include `hours_in_current_month * 2` of development branch time per month (1,440 hours for a 30 day month) at no additional cost. Any time used over the included is billed at a rate of \~$0.014 per hour (`$10 / hours\_in\_current\_month\`). You may see how many development branch hours have been used at any time by visiting your [organization billing page](https://app.planetscale.com/~/settings/billing/). Data is updated hourly.

### Postgres development branches

Postgres development branches, `PS-DEV`, are billed for the time that they are running, prorated to the nearest second. Each development branch is \$5 per month. Development branches are not intended for HA production traffic, as they do not come with any replicas or have maintenance windows.

<Note>
  You can set spend email alerts from your billing page. See the [Spend management documentation](/docs/billing#spend-management) for more information.
</Note>

If a database is created in the middle of a billing cycle, the included development branch hours are prorated. For example, if you create your database with 15 days remaining in the current month, the database will have `15 days * 2` (720 hours) included for that billing period.

### Fractional vCPU allocation

Some tiers of the base plan indicate a fractional vCPU allocation. These branches run on our multi-tenant platform and this indicates the minimum number of cycles dedicated to your workload. The vast majority of the time, there are spare compute cycles available on the underlying machine instances hosting your branch, and those are available to be used by your workload as needed for no additional charge.

If you find the performance of a given query to be substantially inconsistent over the course of a given day, you may want to upgrade to a higher tier for more consistent performance.

## PlanetScale Enterprise plan

PlanetScale's Enterprise Plan is great for large-scale businesses who require the enterprise-level SLAs, want expert assistance through enterprise support, and would prefer to run in your own AWS or GCP account.

We offer many different deployment options, all of which come with the same set of standard features. The table below covers those shared features, as well as the different options that vary depending on your chosen deployment.

|                                                        | PlanetScale Enterprise                  | **[PlanetScale Managed](/docs/plans/managed)**                                                                                                                                                                                    |
| :----------------------------------------------------- | :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Horizontal sharding                                    | <Icon icon="check" color="blue" />      | <Icon icon="check" color="blue" />                                                                                                                                                                                                |
| Customizable feature limits                            | <Icon icon="check" color="blue" />      | <Icon icon="check" color="blue" />                                                                                                                                                                                                |
| [Support](/docs/support)                               | Business — Enterprise upgrade available | Enterprise                                                                                                                                                                                                                        |
| PCI compliant                                          | <Icon icon="xmark" color="red" />       | <Icon icon="check" />                                                                                                                                                                                                             |
| Dedicated AWS/GCP account                              | Optional                                | <Icon icon="check" color="blue" />                                                                                                                                                                                                |
| Bring your own cloud (an AWS or GCP account *you* own) | <Icon icon="xmark" color="red" />       | <Icon icon="check" color="blue" />                                                                                                                                                                                                |
| Billing                                                | Directly from PlanetScale               | Partial payment through PlanetScale and infrastructure costs through AWS/GCP. Take advantage of your own discounts. Optionally, purchase through [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-luy3krhkpjne4). |

## How do I know if I need an Enterprise plan?

If you’re not sure whether your use case requires an Enterprise plan, we’re more than happy to chat with you to figure it out together. You can [fill out this form](https://planetscale.com/contact), and we’ll be in touch.

In general, if you need any of the following, Enterprise may be the best solution for you:

* Enhanced support — our expert team becomes an extension of your own. Additional options for technical account management, Slack-based support, and phone escalation.
* You need additional support to horizontally shard and migrate your database(s) to PlanetScale
* You need your database deployed in a single-tenant environment
* You need to keep your data in **your own** AWS or GCP account
* You need a PCI DSS certified service provider
* Mission-critical [response times](/docs/support#initial-response-times) including continuous support coverage
* Any other customizations — Our Enterprise plans offer a lot of flexibility, so if you have a requirement that’s not listed here, it’s best to [reach out](https://planetscale.com/contact) and we can see how we can help

## Plan add-ons

### Single Sign-on (SSO)

You can [add SSO](/docs/security/sso) for your organization on the Scaler Pro plan for an additional fee of \$199/month.

### User-scheduled backups

On the Scaler Pro plan, we run automated backups every 12 hours. Disk space for default backups is not counted against your plan's storage limit.

You can also [schedule additional backups yourself](/docs/vitess/backups#create-manual-backups) as needed. For these additional user-scheduled backups, storage is billed at **\$0.023 per GB** per month. Backups include system tables as well as your data and start at around 140MB.

## Discounts

We offer two types of discounts:

* **Consumption commitment** — Save 2.5% if you agree to an annual consumption commitment.
* **Upfront payment** — Save an extra 10% if you pay your annual bill upfront.

You have the option to combine these two discounts for a total of 12.5% off your bill if you commit to an annual consumption commitment dollar amount **and** pay for the year upfront.

<Note>
  To be eligible for either of these discounts, you must commit to a minimum of \$5,000 per year.
</Note>

If you're interested in either of these discounts, please fill out our [contact form](https://planetscale.com/contact) and let us know which discount you're interested in, along with the following information:

* Annual spend commitment amount (in dollars)
* PlanetScale organization name (if it exists)
* Company name
* Company address
* Business point of contact name, email, phone
* Billing name, phone, email, address

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt