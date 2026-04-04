# Source: https://firebase.google.com/docs/data-connect/pricing.md.txt

This document explains Firebase Data Connect pricing details.

If you pay in a currency other than USD, the prices listed in your currency on
[Cloud Platform SKUs](https://cloud.google.com/skus) apply.

## Understand Data Connect billing

Firebase Data Connect consists of two billable components:

- The Data Connect service itself
- The Cloud SQL for PostgreSQL instance that contains your project data.

If you integrate with Vertex AI, you are billed for vector embeddings.

### Data Connect service pricing

- Network egress has no cost up to 10 Gib/month; more than 10 Gib/month, egress
  is charged at
  [Google Cloud Internet Data Transfer Rate Premium Tier pricing](https://cloud.google.com/vpc/pricing#internet_egress).

- Operations (queries or mutations) executed from clients incur no cost up to
  250,000 operations per month; more than 250,000, operations are charged at
  $4.00 per million.

  > [!NOTE]
  > **Note:** The price is per operation and is not related to the amount of data read from the database; there is no "per row read" fee. Each Data Connect operation can perform efficient, complex, multi-table queries or multi-row updates.

### Cloud SQL no cost trial

If you accept the default configuration when you provision a Cloud SQL for
PostgreSQL instance, you will be qualified for a no cost trial for 3 months.

- 5 free trials are available per billing account.
- 1 free trial Cloud SQL for PostgreSQL instance per project, although you can have multiple non-free instances within that project.
- The default configuration of your Cloud SQL for PostgreSQL instance is equivalent to a [db-f1-micro instance](https://cloud.google.com/products/calculator?dl=CiRhNDU2NjBmOC1lODJiLTQ0NTctOTliNy00ZmEyZDAyYWFjYTMQBxokODA2Q0I5NzUtMTNEMC00QURFLTg5MUUtMDI2M0VGNzFBMDI0&e=13802955) that has 1 vCPU, 10 GB of storage, 628.74 MB of memory.

During the no cost trial, you can add computing resources to your Cloud SQL
instance, set up a private IP for your instance, and create a read replica for
your instance, at which point you will be billed according to
[Cloud SQL pricing](https://cloud.google.com/sql/docs/postgres/pricing).

After 3 months, pricing starts as low as $9.37 / month. Pricing varies based on
regions and configurations. See [Cloud SQL pricing](https://cloud.google.com/sql/docs/postgres/pricing).

> [!NOTE]
> **Note:** Existing customers who participated in the Public Preview trials will automatically roll into the 3 month no cost trials when General Availability starts.

> [!NOTE]
> **Note:** If you delete your no cost trial instance, your no cost trial for the associated Firebase project will terminate immediately.

### Vertex AI embedding generation

Using Data Connect with [Vertex AI](https://cloud.google.com/vertex-ai)
will incur standard usage charges from Vertex AI for embedding generation.

## Manage spending

To monitor your Data Connect usage, to access an overall view of all
service activity, and links to analyze individual service activity, open the
[Data Connect product page](https://console.firebase.google.com/project/_/dataconnect).
Use the dashboards to gauge your usage over different time periods.

To track your Data Connect costs, create a monthly budget in the
Cloud console. Budgets won't limit your usage, but you can set
alerts to notify you when you're approaching or exceeding your planned costs for
the month.

To set a budget, in the Cloud console, go to the
[Billing](https://console.cloud.google.com/billing/)
section and create a budget for your Cloud Billing account. You can use the
default alert settings or modify the alerts to send notifications at different
percentages of your monthly budget.

Learn more about [setting up budgets and budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails).