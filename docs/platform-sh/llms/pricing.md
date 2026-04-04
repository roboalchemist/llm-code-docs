# Source: https://docs.upsun.com/administration/pricing.md

# Pricing

Upsun offers flexible, predictable [pricing](https://upsun.com/pricing/) for organizations and projects.

**Note**: 

This page is meant to provide some context for how the pricing model relates to technical work on Upsun.
It is not meant to be your primary resource for the exact costs of certain features.

The official Upsun [Pricing page](https://upsun.com/pricing/) should always be considered the primary source of pricing details.

In general, there are four main dimensions that determine the cost of work on Upsun.

|  Pricing dimension  |  Details  |
|---|---|
|  Project fees |  An individual project on Upsun comes with a consistent monthly cost. The cost includes all of the orchestration and provisioning characteristics that define the Upsun platform.It comes with some baseline features and feature limits, such as infrastructure metrics and a certain number of build minutes. Individual preview environments do not come with their own associated creation cost - you are charged only for the resources those preview environments use during their lifespan (see next row).  |
|  [Project resources](https://docs.upsun.com/manage-resources.md) | Deploying on Upsun allows you fine-grained control over the amount of resources allocated for your application and service containers. CPU, memory, and disk (including backup disk) are calculated across each organization, project, and environment to determine your overall usage for a billing period.   |
|  [User licenses](https://docs.upsun.com/administration/users.md) | Each organization user comes with a license fee. Users can be given different levels of access to singular projects within an organization, or to multiple projects, without changing that license fee. There are two exceptions which are not charged the license fee: Viewers and Viewers who Manage Billing. There are no limits to the number of users you can have in an organization.|
|  Feature add-ons |  There are additional features that can be added to the organization that come with their own cost. Few of these are available immediately during the Beta phase, but more will be added.  |

A given organization's monthly billing is then made up of the sum of each of these dimensions. 

You can monitor your spend from the Console via a [current month estimate](https://docs.upsun.com/administration/billing/monitor-billing.md#current-month-estimate) and a [next month estimate](https://docs.upsun.com/administration/billing/monitor-billing.md#next-month-estimate).
You can also [set billing alerts](https://docs.upsun.com/administration/billing/monitor-billing.md#manage-billing-alerts) to receive an email when your current month estimate reaches a defined threshold.

## Dunning process

If a payment fails, your organization will be immediately restricted. Upsun will proceed to make three separate attempts to take the outstanding balance from your account. These attempts will be made on the 4th, 6th and 11th of the month. If your payment fails after the third attempt on the 11th, your organization will be suspended the following day.

When an organization is restricted or suspended, the following applies:

- Access to `/projects/{project_id}/user-access` and `/users/{user_id}/project-access` will be denied.  
- Access to `/projects/{project_id}/team-access` and `/teams/{user_id}/project-access` will be denied.  
- Access to `/projects/{project_id}/access` and its subresources will be denied.  
- Projects cannot be transferred to a restricted organization.  
- Editing or deleting the organization is not allowed.  
- Creating or deleting members is forbidden.  
- Editing member permissions is allowed only to add the billing permission - no permissions can be removed.  
- Access to all account proxy endpoints requiring `plans` or `project:create` permissions is denied, so creating or editing subscriptions at the organization level is forbidden.

If you are a new Upsun customer and your first payment has failed, your projects will be deleted on the 13th - two days after the final payment attempt.

For all other customers, projects will be deleted 30 days after your organization is suspended on the 11th. You will be notified 10 days before this deletion occurs and a payment will be attempted for the last time. If unsuccessful, all projects on the billing subscription will be deleted.

Be sure to visit the [Pricing page](https://upsun.com/pricing/) for exact details related to Upsun pricing.

