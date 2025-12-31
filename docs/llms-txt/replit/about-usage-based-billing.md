# Source: https://docs.replit.com/billing/about-usage-based-billing.md

# Publishing and Database Billing

> Learn how Replit bills for publishing and databases, including outbound data transfer, compute units, requests, and PostgreSQL usage metrics.

There are three types of usage-based billing for publishing:

1. Outbound Data Transfer
2. Autoscale Compute Units
3. Requests

You can view your usage in your account [here](https://replit.com/account#resource-usage). Billing occurs monthly or once your accumulated costs exceed your monthly credits. Replit Core and Teams users receive monthly allowances for these resources.

If you need additional credits beyond your monthly subscription allowance, you can purchase credit packs on your billing page. See [Managing Your Spend](/billing/managing-spend) for more information about credit packs.

<Note>
  Credit packs are gradually rolling out to customers, so you may not have access yet. If you have any questions, you can [contact our Support team](https://replit.com/help).
</Note>

# Publishing

### 1. Publishing Outbound Data Transfer

This type of usage is billed per byte with Replit Core users receiving a monthly allowance. Only egress (outgoing) data is counted against this allowance, potentially leading to overages. In contrast, ingress (incoming) data is always free.

| Subscription | Allowance |
| ------------ | --------- |
| Replit Core  | 100 GiB   |

The allowances apply to [Static](/cloud-services/deployments/static-deployments), [Autoscale](/cloud-services/deployments/autoscale-deployments), [Reserved VM](/cloud-services/deployments/reserved-vm-deployments) and [Scheduled](/cloud-services/deployments/scheduled-deployments) deployments.

See the [pricing page](https://www.replit.com/pricing) for the current price of outbound data transfer.

***

### 2. Compute Units

Autoscale Deployments are billed based on Compute Units, which take into account both CPU and RAM usage over time.

Overages are billed based on Compute Units. The granularity of the billing is down to each individual compute unit. See the [pricing page](https://www.replit.com/pricing) for the current price of compute units.

Here is a breakdown of how RAM and CPU seconds for an Autoscale Deployment translate into Compute Units:

| Resource     | Compute Units |
| ------------ | ------------- |
| 1 RAM Second | 2 Units       |
| 1 CPU Second | 18 Units      |

Static Deployments don't consume Compute Units. Their billing is solely for Outbound Data Transfers beyond a [specified amount](#).

[Learn more about Autoscale Deployments](/cloud-services/deployments/autoscale-deployments).

***

### 3. Requests

Autoscale Deployments also consider the number of requests made.

See the [pricing page](https://www.replit.com/pricing) for the current price of requests.

# Databases

### 1. PostgreSQL Usage Metrics

Replit PostgreSQL offers effortless high availability with no administrative or maintenance burden. Being serverless, Replit PostgreSQL only charges for actual usage, resulting in potential cost savings of up to 10 times.

Replit PostgreSQL databases bill for usage based on the following usage metrics:

* **[Compute Time](#compute-time)**: The amount of compute resources used per hour.
* **[Data Storage](#data-storage)**: The volume of data and history stored.

You can view your usage in your account [here](https://replit.com/account#resource-usage).

#### **Compute Time**

Compute time is determined by number of hours your database remains active during a given billing period. Databases are considered active when they receive requests and for an additional 5-minute period after the last request. If a database remains idle for 5 minutes, it will be suspended and enter an inactive state.

#### **Data Storage**

Data storage is the total volume of data stored across all databases in your account, measured in gibibytes (GiB). Storage is calculated as the maximum amount of storage used per month. Each PostgreSQL database consumes 33MB of storage, even if it doesn't contain any data. This is the default storage footprint of the Postgres server.

<Note>The total storage limit for each database is 10 gibibytes (GiB).</Note>

# Additional Notes

If there's an issue with your payment method, we'll notify you. Continuous payment failures might lead to the suspension of your published apps. If this happens, please [contact support](https://replit.com/help) and update your payment details to regain access to our services.
