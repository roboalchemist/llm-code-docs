# Source: https://planetscale.com/docs/vitess/pricing.md

# Source: https://planetscale.com/docs/postgres/pricing.md

# PlanetScale Postgres pricing

> PlanetScale Postgres databases are billed based on their configuration and usage.

## Overview

Understanding the relationship between **databases**, **branches**, and **clusters** is key to understanding your billing:

* **Database**: Your overall project (e.g., "my-ecommerce-app")
* **Branch**: Isolated database deployments that provide you with separate environments for development and testing, as well as restoring from backups. [Learn more about branching](/docs/postgres/branching)
* **Cluster**: The underlying compute and storage infrastructure that powers each branch

**Each branch runs on its own dedicated cluster** and is billed separately based on its configuration and usage.

* You are billed for the compute and storage resources (cluster) that power each branch (prorated to the millisecond each month)
* Every database branch you launch has default included amounts of:
  * [Cluster disk storage](/docs/postgres/#cluster-disk-storage)
  * [Backup storage](/docs/postgres/#backups)
  * [Network egress data transfer](/docs/postgres/#network-data-transfer)
  * [Replicas](/docs/postgres/#additional-replicas)
* Usage beyond the included defaults is charged based on the costs for that resource, this includes:
  * Cluster disk storage used beyond the included amount (for network-attached storage)
  * Backup storage used beyond the included amount
  * Network egress beyond the included amount
  * Additional replicas

There are no upfront commitments, and as you adjust your configuration or usage changes, pricing will automatically adjust from that point.

<Note>
  For information on Vitess cluster pricing on the Scaler Pro plan, see [Scaler Pro cluster pricing](/docs/plans/cluster-sizing).
</Note>

## Cluster instance size

Each database branch runs on its own dedicated cluster infrastructure. Clusters are billed based on the selected instance size and prorated to the millisecond. Each instance size includes defined amounts of vCPU cores and memory, as well as storage based on the storage type selected ([network-attached storage](/docs/postgres/cluster-configuration/cluster-storage) or [PlanetScale Metal](/docs/metal)). See [cluster pricing](/docs/postgres/#cluster-pricing) for more information.

You can [increase or decrease your cluster size](/docs/postgres/cluster-configuration) at any time. Pricing is prorated to the millisecond, so if you temporarily increase, you will only be charged for the larger cluster size for the time that it was running. Billing for a modified cluster size begins once the resize is completed. You can also [spin up additional production branches](/docs/postgres/branching) at any time for additional cost. The pricing for these is also prorated.

## Cluster disk storage

<Note>
  We use **[gibibytes, otherwise known as binary gigabytes](https://simple.wikipedia.org/wiki/Gibibyte)**, to calculate storage and usage limits. For reference, 1 binary gigabyte is equivalent to 2^30 bytes.
</Note>

### Storage types explained

PlanetScale offers two storage options with different pricing models:

| [PlanetScale Metal](/docs/metal)                                                                                                                                                                                                                                                | [Network-Attached Storage](/docs/postgres/cluster-configuration/cluster-storage)                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **All-inclusive pricing**                                                                                                                                                                                                                                                       | **Configuration-based pricing**                                                                                                                                                                                                                                                                                                                                                                                       |
| - Storage cost is included in your cluster instance price <br /> - High-performance NVMe SSDs directly attached to your servers <br /> - To get more storage, you upgrade to a larger cluster size <br /> - Best for: High-performance applications that need predictable costs | - First 10 GB included with each cluster <br /> - Additional Storage is billed separately from your cluster instance configuration <br /> - Flexible scaling - add storage without changing cluster size <br /> - Automatic disk scaling with [autoscaling](/docs/postgres/cluster-configuration/cluster-storage#enable-autoscaling) <br /> - Best for: Applications with variable storage needs or cost optimization |

### Network-attached storage billing

For network-attached storage clusters, pricing varies by region and cloud provider:

* **Base storage**: you manually configure this in cluster settings, unless [autoscaling](/docs/postgres/cluster-configuration/cluster-storage#enable-autoscaling) is enabled
* **Additional IOPS**: you manually configure this in cluster settings (AWS only)
* **Additional Throughput**: you manually configure this in cluster settings (AWS only)

<Note>
  **AWS vs GCP Pricing**: AWS network-attached storage cluster types allow separate billing for IOPS and throughput that you manually configure. GCP network-attached storage cluster types include IOPS and throughput that scale automatically with disk size at no additional cost. See [AWS Storage Pricing](/docs/postgres/pricing/#aws-storage-pricing) and [GCP Storage Pricing](/docs/postgres/pricing/#gcp-storage-pricing) below for detailed regional pricing.
</Note>

Billing for modified storage attributes begins once the change for the cluster has completed.

**What are IOPS and Throughput?**

* **IOPS** (Input/Output Operations Per Second): How many read/write operations your database can handle per second. Higher IOPS = faster response for many small database queries.
* **Throughput**: How much data can be transferred per second (MiB/s). Higher throughput = faster for large data operations like bulk imports.

For more information on changing your cluster's storage, see the [Cluster storage configuration](/docs/postgres/cluster-configuration/cluster-storage) documentation.

## Backups

### Included backup storage

PlanetScale automatically includes backup storage with every database branch at no extra cost. Each branch gets backup storage equal to **2x your disk size**.

Examples:

| Disk Size | Backup Storage Included |
| :-------- | :---------------------- |
| 25 GB     | 50 GB                   |
| 50 GB     | 100 GB                  |
| 1000 GB   | 2000 GB                 |

<Note>
  For clusters with [network-attached storage](/docs/postgres/cluster-configuration/cluster-storage) with [autoscaling](/docs/postgres/cluster-configuration/cluster-storage#enable-autoscaling) enabled, **backup** storage changes as your **disk storage** autoscales.
</Note>

When your backup and WAL storage exceeds the included amount, additional storage is billed at **\$0.023 per GB per month**.

**Storage overage examples**:

| Storage Overage | Duration | Cost   |
| :-------------- | :------- | :----- |
| 100 GB          | 30 days  | \$2.30 |
| 100 GB          | 15 days  | \$1.15 |

### How backup billing works

**Storage calculation**: Both database data backups and WAL files are automatically compressed before being sent to backup storage. You're billed only on the compressed size, which is typically much smaller than your active database size.

Backup storage usage billing data is updated hourly.

For more details on backup functionality, see [Back up and restore](/docs/postgres/backups).

**What affects storage costs**:

| Factor                | Impact                                                  |
| :-------------------- | :------------------------------------------------------ |
| **Database activity** | More active databases generate more WAL files           |
| **Backup retention**  | Longer retention periods increase storage usage         |
| **Oldest backup age** | WAL files are kept as long as your oldest backup exists |

## [Network data transfer](/docs/postgres/#network-data-transfer)

Outgoing network traffic (egress) is billed based on the amount of data transferred out of PlanetScale Postgres instances to any other host or destination. You are not charged for data transfer for purposes such as Primary to Replica [replication](/docs/postgres/scaling/replicas) or [backups](/docs/postgres/backups). Each branch has a default amount of included network egress that is aggregated for all cluster instances in the entire branch.

| Branch Type          | Included Network Egress |
| -------------------- | ----------------------- |
| Production           | 100 GB per month        |
| Development (PS-DEV) | 10 GB per month         |

See [AWS Egress Pricing](#aws-egress-pricing) and [GCP Egress Pricing](#gcp-egress-pricing) below for detailed regional pricing.

Incoming network traffic (ingress) is free.

## Additional replicas

Each production cluster includes 2 [replicas](/docs/postgres/scaling/replicas) (excluding [single node](/docs/postgres/cluster-configuration/single-node)) to provide high availability and additional read capacity alongside the primary. Certain read-heavy workloads may demand additional read replicas. If you need additional replicas beyond what is included, you can add them for an additional cost based on the branch's instance size and storage requirements. The cost of an additional replica instance is \~1/3 the cost of the original 3-node cluster.

New replica(s) billing begins once the change has completed.

Examples:

| Base cluster configuration (includes 2 replicas) | Monthly base cluster cost           | Additional monthly replica cost     | Monthly total |
| :----------------------------------------------- | :---------------------------------- | :---------------------------------- | :------------ |
| M-160 (r8gd)                                     | \$589                               | \$197                               | \$786         |
| M-320 (r8gd)                                     | \$1,149                             | \$383                               | \$1,532       |
| M-1280 (i8g)                                     | \$5,319                             | \$1,773                             | \$7,092       |
| PS-10 (aarch64 CPU) with 100 GB storage          | $34 + $33.75 (additional storage)   | $12 + $12.50 (\*additional storage) | \$92.25       |
| PS-160 (aarch64 CPU) with 1000 GB storage        | $286 + $371.25 (additional storage) | $96 + $125 (\*additional storage)   | \$878.25      |

\*Note: Replicas with network-attached storage do not include the default included cluster storage disk amount of 10GB. You pay for the entire configured disk size. Figures shown here are for AWS based instances with additional storage amounts and no additional IOPS/Throughput configured.

Development branches and single node databases do not support replicas. For more information on replicas, see [Replicas](/docs/postgres/scaling/replicas).

## Cluster pricing

Cluster instance pricing is based on the cloud provider's own pricing for the compute resources, and varies per region. See the below links for the current region's pricing.

### Amazon Web Services

<CardGroup>
  <Card title="ap-northeast-1 (Tokyo)" href="https://planetscale.com/pricing?region=ap-northeast" icon="angles-right" horizontal />

  <Card title="ap-south-1 (Mumbai)" href="https://planetscale.com/pricing?region=ap-south" icon="angles-right" horizontal />

  <Card title="ap-southeast-1 (Singapore)" href="https://planetscale.com/pricing?region=ap-southeast" icon="angles-right" horizontal />

  <Card title="ap-southeast-2 (Sydney)" href="https://planetscale.com/pricing?region=aws-ap-southeast-2" icon="angles-right" horizontal />

  <Card title="ca-central-1 (Montreal)" href="https://planetscale.com/pricing?region=aws-ca-central-1" icon="angles-right" horizontal />

  <Card title="eu-central-1 (Frankfurt)" href="https://planetscale.com/pricing?region=eu-central" icon="angles-right" horizontal />

  <Card title="eu-west-1 (Dublin)" href="https://planetscale.com/pricing?region=eu-west" icon="angles-right" horizontal />

  <Card title="eu-west-2 (London)" href="https://planetscale.com/pricing?region=aws-eu-west-2" icon="angles-right" horizontal />

  <Card title="sa-east-1 (Sao Paulo)" href="https://planetscale.com/pricing?region=aws-sa-east-1" icon="angles-right" horizontal />

  <Card title="us-east-1 (N. Virginia)" href="https://planetscale.com/pricing?region=us-east" icon="angles-right" horizontal />

  <Card title="us-east-2 (Ohio)" href="https://planetscale.com/pricing?region=us-east-2" icon="angles-right" horizontal />

  <Card title="us-west-2 (Oregon)" href="https://planetscale.com/pricing?region=us-west" icon="angles-right" horizontal />
</CardGroup>

### Google Cloud

<CardGroup>
  <Card title="asia-northeast3 (Seoul, South Korea)" href="https://planetscale.com/pricing?region=gcp-asia-northeast3" icon="angles-right" horizontal />

  <Card title="northamerica-northeast1 (Montréal, Québec)" href="https://planetscale.com/pricing?region=gcp-northamerica-northeast1" icon="angles-right" horizontal />

  <Card title="us-central1 (Council Bluffs, Iowa)" href="https://planetscale.com/pricing?region=gcp-us-central1" icon="angles-right" horizontal />

  <Card title="us-east4 (Ashburn, Virginia)" href="https://planetscale.com/pricing?region=gcp-us-east4" icon="angles-right" horizontal />
</CardGroup>

## Storage pricing

Network-attached storage pricing varies by region and includes three billable components:

* **Storage**: The cost per GB of data stored per month (can [auto-scale](/docs/postgres/cluster-configuration/cluster-storage#enable-autoscaling) with usage if enabled)
* **Additional IOPS**: Cost when you manually configure more input/output operations per second beyond the included baseline
* **Additional Throughput**: Cost when you manually configure more data transfer throughput (MiB/s) beyond the included baseline

<Note>
  **Most applications only pay for base storage.** IOPS and throughput charges only apply if you manually increase these settings beyond the included baseline in your cluster configuration.
</Note>

The table below shows the pricing for all three components across different AWS regions. Your total storage cost will depend on your configuration of each component.

### AWS storage pricing

| Cloud Provider | Region                     | Storage (per GB/month) | Additional IOPS (per IOPS/month) | Additional Throughput (per MiB/s/month) |
| :------------- | :------------------------- | :--------------------- | :------------------------------- | :-------------------------------------- |
| AWS            | ap-northeast-1 (Tokyo)     | \$0.150                | \$0.011                          | \$0.088                                 |
| AWS            | ap-south-1 (Mumbai)        | \$0.143                | \$0.103                          | \$0.084                                 |
| AWS            | ap-southeast-1 (Singapore) | \$0.150                | \$0.011                          | \$0.088                                 |
| AWS            | ap-southeast-2 (Sydney)    | \$0.150                | \$0.011                          | \$0.088                                 |
| AWS            | ca-central-1 (Montreal)    | \$0.138                | \$0.010                          | \$0.081                                 |
| AWS            | eu-central-1 (Frankfurt)   | \$0.149                | \$0.011                          | \$0.088                                 |
| AWS            | eu-west-1 (Dublin)         | \$0.138                | \$0.010                          | \$0.081                                 |
| AWS            | eu-west-2 (London)         | \$0.145                | \$0.011                          | \$0.084                                 |
| AWS            | sa-east-1 (Sao Paulo)      | \$0.238                | \$0.018                          | \$0.139                                 |
| AWS            | us-east-1 (N. Virginia)    | \$0.125                | \$0.009                          | \$0.073                                 |
| AWS            | us-east-2 (Ohio)           | \$0.125                | \$0.009                          | \$0.073                                 |
| AWS            | us-west-2 (Oregon)         | \$0.125                | \$0.009                          | \$0.073                                 |

### GCP storage pricing

The table below shows the storage pricing for Google Cloud Platform regions. GCP storage pricing includes only base storage costs, with IOPS and throughput that scale with disk size.

| Cloud Provider | Region                                     | Storage (per GB/month) |
| :------------- | :----------------------------------------- | :--------------------- |
| GCP            | asia-northeast3 (Seoul, South Korea)       | \$0.221                |
| GCP            | northamerica-northeast1 (Montréal, Québec) | \$0.187                |
| GCP            | us-central1 (Council Bluffs, Iowa)         | \$0.170                |
| GCP            | us-east4 (Ashburn, Virginia)               | \$0.187                |

## Egress pricing

### AWS egress pricing

The table below shows the egress pricing (per GB beyond included amounts) for AWS regions.

| Cloud Provider | Region                     | Egress (per GB) |
| -------------- | -------------------------- | --------------- |
| AWS            | ap-northeast-1 (Tokyo)     | \$0.101         |
| AWS            | ap-south-1 (Mumbai)        | \$0.096         |
| AWS            | ap-southeast-1 (Singapore) | \$0.096         |
| AWS            | ap-southeast-2 (Sydney)    | \$0.111         |
| AWS            | ca-central-1 (Montreal)    | \$0.060         |
| AWS            | eu-central-1 (Frankfurt)   | \$0.060         |
| AWS            | eu-west-1 (Dublin)         | \$0.060         |
| AWS            | eu-west-2 (London)         | \$0.060         |
| AWS            | sa-east-1 (Sao Paulo)      | \$0.137         |
| AWS            | us-east-1 (N. Virginia)    | \$0.060         |
| AWS            | us-east-2 (Ohio)           | \$0.060         |
| AWS            | us-west-2 (Oregon)         | \$0.060         |

### GCP egress pricing

The table below shows the egress pricing (per GB beyond included amounts) for Google Cloud Platform regions.

| Cloud Provider | Region                                     | Egress (per GB) |
| -------------- | ------------------------------------------ | --------------- |
| GCP            | asia-northeast3 (Seoul, South Korea)       | \$0.117         |
| GCP            | europe-west1 (St Ghislain, Belgium)        | \$0.060         |
| GCP            | northamerica-northeast1 (Montréal, Québec) | \$0.060         |
| GCP            | us-central1 (Council Bluffs, Iowa)         | \$0.060         |
| GCP            | us-east4 (Ashburn, Virginia)               | \$0.060         |

## PgBouncer pricing

Dedicated PgBouncer instances are billed monthly based on their size and region. The local PgBouncer (included on the primary database instance) is free. Learn more about PgBouncer configuration in the [PgBouncer documentation](/docs/postgres/connecting/pgbouncer).

PgBouncer instances are available in six sizes:

| Size    | CPU       | Memory |
| ------- | --------- | ------ |
| PGB-5   | 1/16 vCPU | 128 MB |
| PGB-10  | 1/8 vCPU  | 256 MB |
| PGB-20  | 1/4 vCPU  | 512 MB |
| PGB-40  | 1/2 vCPU  | 1 GB   |
| PGB-80  | 1 vCPU    | 2 GB   |
| PGB-160 | 2 vCPU    | 4 GB   |

### AWS PgBouncer pricing

The table below shows the monthly pricing for dedicated PgBouncer instances across AWS regions.

| Region                     | PGB-5 | PGB-10 | PGB-20 | PGB-40 | PGB-80 | PGB-160 |
| -------------------------- | ----- | ------ | ------ | ------ | ------ | ------- |
| ap-northeast-1 (Tokyo)     | \$21  | \$41   | \$82   | \$164  | \$327  | \$653   |
| ap-south-1 (Mumbai)        | \$12  | \$24   | \$47   | \$93   | \$186  | \$371   |
| ap-southeast-1 (Singapore) | \$21  | \$41   | \$82   | \$164  | \$327  | \$653   |
| ap-southeast-2 (Sydney)    | \$21  | \$41   | \$82   | \$163  | \$325  | \$649   |
| ca-central-1 (Montreal)    | \$19  | \$38   | \$75   | \$150  | \$299  | \$598   |
| eu-central-1 (Frankfurt)   | \$21  | \$41   | \$82   | \$164  | \$327  | \$653   |
| eu-west-1 (Dublin)         | \$20  | \$39   | \$77   | \$153  | \$305  | \$610   |
| eu-west-2 (London)         | \$22  | \$44   | \$88   | \$176  | \$351  | \$701   |
| sa-east-1 (Sao Paulo)      | \$30  | \$59   | \$117  | \$234  | \$467  | \$933   |
| us-east-1 (N. Virginia)    | \$18  | \$35   | \$69   | \$138  | \$276  | \$551   |
| us-east-2 (Ohio)           | \$18  | \$35   | \$69   | \$138  | \$276  | \$551   |
| us-west-2 (Oregon)         | \$18  | \$35   | \$69   | \$138  | \$276  | \$551   |

### GCP PgBouncer pricing

The table below shows the monthly pricing for dedicated PgBouncer instances across Google Cloud Platform regions.

| Region                                     | PGB-5 | PGB-10 | PGB-20 | PGB-40 | PGB-80 | PGB-160 |
| ------------------------------------------ | ----- | ------ | ------ | ------ | ------ | ------- |
| asia-northeast3 (Seoul, South Korea)       | \$22  | \$44   | \$87   | \$174  | \$348  | \$695   |
| europe-west1 (Belgium)                     | \$19  | \$38   | \$76   | \$151  | \$302  | \$603   |
| northamerica-northeast1 (Montréal, Québec) | \$19  | \$38   | \$76   | \$151  | \$302  | \$604   |
| us-central1 (Council Bluffs, Iowa)         | \$18  | \$35   | \$70   | \$139  | \$277  | \$554   |
| us-east4 (Ashburn, Virginia)               | \$20  | \$39   | \$78   | \$155  | \$309  | \$617   |

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt