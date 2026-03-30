# Source: https://northflank.com/docs/v1/application/billing/monitor-spending.md

# Monitor spending

You can view current usage by service, project, or account, which gives a breakdown of resource usage and costs for the current billing cycle.

The usage breakdown is calculated from the end of the last billing period to the current date and is updated on an hourly basis.

> [!note] 
> [Click here](https://app.northflank.com/s/account/billing) to view your account billing.
If your team is [managed by an organisation](https://northflank.com/docs/v1/application/collaborate/manage-an-organisation#manage-organisation-billing), you may have limited ability to view and update your billing details in the team account.

## View account billing

To view current usage by account, navigate to the billing page in your team settings.

You can view different breakdowns of your spend by selecting a view from the current usage section.

### Category

Divides spend by the following categories:

- Northflank platform usage, such as runtime, storage, and networking

- Bring your own cloud (BYOC) usage

- Recurring commitments such as organisation or enterprise plans

- Any other costs

### Project

Divides spend by project. Each project can be expanded to view services, jobs, and addons, which can also be expanded to view individual resources.

You can order this view alphabetically or by cost, and filter by amount.

### Resource Type

View spend by resource type:

- Addons

- Services

- Volumes

- Jobs

Each type can be expanded to view individual resources.

### Team

Organisations can also view spend by team. Each team can be expanded to view projects, resource types, and individual resources.

![The account billing overview in the Northflank application](https://assets.northflank.com/documentation/v1/application/billing/monitor-spending/team-billing-overview.png)

## View project billing

To view your current usage for a project, navigate to the project and select  Project Settings from the header.

The current usage, broken down by resource type, will be displayed. You can expand each entry for a list of associated resources, including their duration and cost.

You can also find a list of past invoices that the project has been included in.

![Project billing information on the project settings page in the Northflank application](https://assets.northflank.com/documentation/v1/application/billing/monitor-spending/project-billing.png)

## View resource billing

To view your current usage for a resource, including services, jobs and addons, navigate to the billing page on the resource you want to check.

The current usage, broken down by build time, runtime, and storage will be displayed, showing duration and cost.

You can also find a list of past invoices that the resource has been included in.

![The resource billing page in the Northflank application](https://assets.northflank.com/documentation/v1/application/billing/monitor-spending/resource-billing.png)

## Set up billing alerts

You can create billing alerts on your account or team billing page.

If your total monthly spend exceeds the set threshold(s), you will be notified on the registered email address for your account or team, and by any other [notification integrations](https://northflank.com/docs/v1/application/observe/configure-notification-integrations) you have set up and configured to receive billing alerts.

> [!note] 
> [Click here](https://app.northflank.com/s/account/billing/create-billing-alert) to create a billing alert.

## Add an invoice email address

You can assign multiple emails to receive invoices and billing alerts.

For details and to add an email address, see the [Add Invoice Email](https://northflank.com/docs/v1/application/billing/add-invoice-email).

## Next steps

- [View invoices: View your monthly Northflank invoices with detailed breakdowns of usage and cost.](/v1/application/billing/view-invoices)
- [Pay an invoice: Find and pay an overdue invoice.](/v1/application/billing/pay-an-invoice)
