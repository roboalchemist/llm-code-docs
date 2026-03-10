# Source: https://render.com/docs/postgresql-refresh.md

# Flexible Plans for Render Postgres — Set your database's storage and compute independently.


> *Flexible Render Postgres plans are now enabled for all workspaces.*

Render has rolled out flexible plans for Render Postgres. With these plans, you can:

- Increase your database's storage at any time, without downtime
- Adjust your database's CPU and RAM, totally independent of storage
- Choose from a much wider range of compute options, up to 128 CPUs and 1 TB RAM

Additionally, we've expanded the availability of [certain PostgreSQL features](#expanded-feature-availability). For example, point-in-time recovery is being added to all paid databases.

> *[*Legacy instances*](postgresql-legacy-instance-types) keep their existing plan and pricing.*
>
> You can optionally move a legacy instance to a flexible plan by [moving it](postgresql-creating-connecting#changing-your-instance-type) to any [new paid instance type](#new-instance-types). Note that your database will be unavailable for a few minutes during the switch, and you can't move _back_ to a legacy instance type.

## What's new

### Independent storage and compute

*Prior to flexible plans,* a database's instance type always determined both its storage _and_ compute specs:

[image: Non-flexible PostgreSQL instance types in the Render Dashboard]

*With this refresh,* the new Render Postgres [instance types](#new-instance-types) _only_ determine compute specs—you can set storage independently. Each database is billed according to its particular combination of instance type and storage, so you can pay for exactly the resources you need.

- Instance types are billed according to their compute specs, prorated to the second. [See pricing.](#pricing-for-new-instance-types)
- Storage is billed at a fixed rate of $0.30 per GB per month, prorated to the second.
- You can increase your database's storage at any time, to any multiple of 5 GB.
  - Adding storage does not require any downtime for your database.
  - You can't _reduce_ storage for a database.

### New instance types

Render Postgres now offers four tiers of instance types:

------

###### Tier

*Free*

###### Description

The Free instance type is unchanged. Free databases have a fixed storage of 1&nbsp;GB, and they expire after 30 days. [Learn more about free Render Postgres databases](free#free-postgres).

---

###### Tier

*Basic*

###### Description

Instance types with compute and pricing comparable to Render's legacy *Starter*, *Standard*, and *Pro* instance types. [See pricing.](/pricing#postgresql)

---

###### Tier

*Pro*

###### Description

Instance types with a 1:4 CPU-to-RAM ratio, suitable for production workloads.

- *Smallest:* 1 CPU / 4 GB RAM
- *Largest:* 128 CPU / 512 GB RAM

[See pricing.](/pricing#postgresql)

---

###### Tier

*Accelerated*

###### Description

Instance types with an 1:8 CPU-to-RAM ratio, suitable for memory-intensive workloads.

- *Smallest:* 1 CPU / 8 GB RAM
- *Largest:* 128 CPU / 1 TB RAM

[See pricing.](/pricing#postgresql)

------

Each instance type has a name that reflects its tier and RAM, such as *Basic-1gb* or *Accelerated-64gb*.

### Expanded feature availability

The following Render Postgres features (some of which were previously limited to *Professional* workspaces or higher) are now available to any database with eligible specs:

------

###### Feature

[*Point-in-time recovery*](postgresql-backups)

###### Newly Eligible Databases

All paid databases receive point-in-time recovery (PITR) automatically. Your retention period for PITR depends on your workspace's plan:

- *Hobby:* 3 days
- *Professional or higher:* 7 days

Databases on a [legacy instance type](postgresql-legacy-instance-types) will receive point-in-time recovery as part of their first maintenance period following the release of flexible plans.

---

###### Feature

[*Read replicas*](postgresql-read-replicas)

###### Newly Eligible Databases

Any database on a flexible plan with at least 0.5 CPU and 10 GB of storage

---

###### Feature

[*High availability*](postgresql-high-availability)

###### Newly Eligible Databases

- Any database on a flexible plan using a *Pro* or *Accelerated* [instance type](#new-instance-types)
- Any database on a [legacy](postgresql-legacy-instance-types) *Pro* or *Pro Plus* instance type

------

## Pricing for new instance types

[*See the pricing page.*](/pricing#postgresql)

## FAQ

### Will Render automatically migrate legacy instances to a flexible plan?

*No.* By default, databases on a [legacy instance type](postgresql-legacy-instance-types) keep their current specs and pricing.

After flexible plans are enabled for your workspace, you can move an existing database to a flexible plan by changing its instance type in the Render Dashboard.

> *Note the following:*
>
> - If you move to a new instance type, your database will be unavailable for a few minutes while the new instance spins up.
> - You can't move a database back to a legacy instance type.

### Can I change my database's instance type?

*Yes.* You can [change your database's instance type](postgresql-creating-connecting#changing-your-instance-type) at any time in the Render Dashboard. You can change to a smaller _or_ larger instance type, without changing your storage.

> *Note the following:*
>
> - Your database will be unavailable for a few minutes while the new instance spins up.
> - You can't move a paid database to the Free instance type.
> - If you've enabled a Render Postgres feature with [minimum spec requirements](#expanded-feature-availability) (such as high availability), you can only move to another instance type that meets those requirements.

### Can I reduce my database's storage?

*No.* You can increase an existing database's storage at any time, but you can't reduce it.

To reduce your storage, you can create a _new_ database with the desired storage and migrate your data by restoring from a [backup](postgresql-backups#logical-backups).

### How are flexible database plans billed?

Each database on a flexible plan is billed according to its combination of instance type and storage:

- Instance types are billed according to their compute specs, prorated to the second. [See pricing.](/pricing#postgresql)
- Storage is billed at $0.30 per GB per month, prorated to the second.