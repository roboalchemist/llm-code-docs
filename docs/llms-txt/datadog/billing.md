# Source: https://docs.datadoghq.com/account_management/billing.md

---
title: Billing
description: >-
  Understand billing cycles, payment methods, usage calculations, and host
  counting with detailed pricing information for Datadog products.
breadcrumbs: Docs > Account Management > Billing
source_url: https://docs.datadoghq.com/billing/index.html
---

# Billing

## Overview{% #overview %}

The billing cycle begins the first of the month (UTC) regardless of when you sign up. Your first month is prorated based on your actual sign-up date.

Datadog meters the count of hosts and custom metrics hourly. The billable count of hosts is calculated at the end of the month using the maximum count (high-water mark) of the lower 99 percent of usage for those hours. Datadog excludes the top 1 percent to reduce the impact of spikes in usage on your bill. The billable count of custom metrics is based on the average number of custom metric hours for the month. See your [Usage](https://app.datadoghq.com/account/usage/hourly) in Datadog. Billing pages are only accessible to users with the Datadog Admin Role.

### Hosts{% #hosts %}

A host is any physical or virtual OS instance that you monitor with Datadog. It could be a server, VM, node (in the case of Kubernetes), App Service Plan instance (in the case of Azure App Service), or Heroku dyno (in the case of the Heroku platform). Hosts can be instances with the Datadog Agent installed plus any Amazon EC2s, Google Cloud, Azure, or vSphere VMs monitored with Datadog integrations. Any EC2s or VMs with the Agent installed count as a single instance (no double-billing).

Non-reporting hosts (status `INACTIVE` in your [Infrastructure list](https://docs.datadoghq.com/infrastructure/)) do not count towards billing. It could take up to 2 hours for these hosts to drop out of the [Infrastructure List](https://docs.datadoghq.com/infrastructure/). Datadog retains the historical data for these hosts (paid accounts). Metrics can be graphed on a dashboard by knowing the specific host name or tags.

### Containers{% #containers %}

It is recommended that containers are monitored with a single containerized Agent per host. This Agent collects both container and host metrics. If you choose to install the Agent directly in each container, each container is counted as a host from a billing perspective. More details can be found in the [Agent installation](https://docs.datadoghq.com/agent/) documentation.

### Serverless{% #serverless %}

Datadog bills based on the average number of functions per hour across the month for your accounts. Every hour, Datadog records the number of functions that were executed one or more times and monitored by your Datadog account. At the end of the month, Datadog charges by calculating the average of the hourly number of functions recorded. Pro and Enterprise plans include five custom metrics per billable function.

Billing for serverless APM is based on the sum of AWS Lambda invocations connected to APM ingested spans in a given month. You will also be billed for the total number of [indexed spans](https://docs.datadoghq.com/account_management/billing/pricing/#apm) submitted to the Datadog APM service exceeding the bundled quantity at the end of the month. There are no billable [APM Hosts](https://docs.datadoghq.com/account_management/billing/pricing/#apm) when using serverless.

For more information, see the [Serverless billing page](https://docs.datadoghq.com/account_management/billing/serverless) and the [Datadog Pricing page](https://www.datadoghq.com/pricing/?product=serverless#serverless).

### IoT{% #iot %}

Datadog meters the count of IoT devices hourly. The billable count of IoT devices is calculated at the end of the month using the maximum count (high-water mark) of the lower 99 percent of usage for those hours, excluding the top 1 percent to reduce the impact of spikes in usage on your bill.

For more information about IoT billing, see the [Datadog Pricing page](https://www.datadoghq.com/pricing/).

## Plan details{% #plan-details %}

To manage your **Payment Method** and view **Subscription Details**, you must be a Datadog Admin user.

Alternately, roles with Billing Read (`billing_read`) and Billing Edit (`billing_edit`) [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#billing-and-usage) can access this data.

### Managing your payment method{% #managing-your-payment-method %}

The [**Payment Method**](https://app.datadoghq.com/billing/plan) section contains details on your payment options.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/PaymentMethodOverview.e946755fe70e2b62f640a17b53c25317.png?auto=format"
   alt="Payment method on the Plan page" /%}

**Edit Payment** provides options to manage payment methods. You can edit or remove cards, and request to change your payment method from card to invoice and vice versa.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/PaymentSettingsDetails.637ee9ae23b80533f87e8f2db9770abd.png?auto=format"
   alt="Payment settings on the Plan page" /%}

### Managing your billing contact details{% #managing-your-billing-contact-details %}

You can view your billing contact details on the [**Billing Contact Details**](https://app.datadoghq.com/billing/plan) section.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/BillingContactDetailsOverview.8deeb4a4cb665caf077ba847348c1349.png?auto=format"
   alt="Billing contact details on the Plan page" /%}

**Edit Details** to add, edit, or remove your billing address. You can also specify the email addresses where invoices should be sent.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/BillingContactDetailsEdit.b51ff22ccecbc8300145f6cf9428e61d.png?auto=format"
   alt="Editing billing contact details on the Plan page" /%}

**Note**: The email address does not need to be a team member within Datadog. For example, you could use `invoices@example.com`.

### View your subscription details{% #view-your-subscription-details %}

The [Subscription Details](https://app.datadoghq.com/billing/plan) section includes the quantity, contract price, and on-demand price for all committed products.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/subscription_details.05bafa4e33fd025417731e644e1d2f70.png?auto=format"
   alt="Account Plan & Usage page highlighting Subscription Details section" /%}

**Note**: If your billing is managed directly through a Datadog Partner, Subscription Details are not supported.

## Payment{% #payment %}

There are two choices for payment method:

- Credit card
- Invoicing (ACH, wire, or check)

### Credit card{% #credit-card %}

If you pay by credit card, receipts are available to [Administrators](https://docs.datadoghq.com/account_management/rbac/#datadog-default-roles) for previous months under [Billing History](https://app.datadoghq.com/account/billing_history). For copies of your invoice, email [Datadog billing](mailto:billing@datadoghq.com).

See [Credit Card Billing](https://docs.datadoghq.com/account_management/billing/credit_card/) for more details.

### Invoicing{% #invoicing %}

If you pay by check, ACH, or wire, invoices are emailed to the billing email addresses near the 10th business day of each month. To request an additional copy, email [Datadog billing](mailto:billing@datadoghq.com). Details on where to remit payment can be found on the invoice.

## Contact{% #contact %}

| Question or concern                                                                                                                                                   | Contact                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Dispute and credit requestUsagePayment method changePayment concernGeneral account concernsUpdate contactsStatement of accountUpdate billing and shipping information | [success@datadoghq.com](mailto:success@datadoghq.com)               |
| Invoice copiesTime sensitive charge requestsBilling breakdownPortal invitation                                                                                        | [billing@datadoghq.com](mailto:billing@datadoghq.com)               |
| Payment remittance                                                                                                                                                    | [remittances@datadoghq.com](mailto:remittances@datadoghq.com)       |
| Purchase order copies                                                                                                                                                 | [purchaseorders@datadoghq.com](mailto:purchaseorders@datadoghq.com) |

## Further Reading{% #further-reading %}

- [Pricing](https://docs.datadoghq.com/account_management/billing/pricing/)
- [Usage details](https://docs.datadoghq.com/account_management/plan_and_usage/usage_details/)
- [Usage Metrics](https://docs.datadoghq.com/account_management/billing/usage_metrics/)
- [Credit card](https://docs.datadoghq.com/account_management/billing/credit_card/)
- [Custom metrics](https://docs.datadoghq.com/account_management/billing/custom_metrics/)
- [Containers](https://docs.datadoghq.com/account_management/billing/containers/)
- [Log management](https://docs.datadoghq.com/account_management/billing/log_management/)
- [APM (Distributed Tracing & Continuous Profiler)](https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/)
- [Serverless](https://docs.datadoghq.com/account_management/billing/serverless/)
- [Real User Monitoring](https://docs.datadoghq.com/account_management/billing/rum/)
- [CI Visibility](https://docs.datadoghq.com/account_management/billing/ci_visibility/)
- [AWS integration](https://docs.datadoghq.com/account_management/billing/aws/)
- [Azure integration](https://docs.datadoghq.com/account_management/billing/azure/)
- [Alibaba integration](https://docs.datadoghq.com/account_management/billing/alibaba/)
- [Google Cloud integration](https://docs.datadoghq.com/account_management/billing/google_cloud/)
- [vSphere integration](https://docs.datadoghq.com/account_management/billing/vsphere/)
- [Usage attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution/)
