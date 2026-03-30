# Source: https://posthog.com/docs/customer-analytics/customer-profiles.md

# Customer profiles - Docs

**Customer Analytics is in beta**

Customer Analytics is currently in beta and free to use. We're actively developing this feature and would love your [feedback](https://app.posthog.com/customer_analytics#panel=support%3Afeedback%3Acustomer_analytics%3Alow%3Atrue).

Customer profiles consolidate everything about a customer in one place. Instead of jumping between different parts of PostHog to understand a customer, you get their full picture in a single view.

![Person profile](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_30_34_040_Z_e0dea14b33.png)![Person profile](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_30_59_919_Z_8a54ff12bf.png)

## What's included in a profile

Customer profiles pull together data from across PostHog and connected sources:

| Data type | Source | Requirements |
| --- | --- | --- |
| Events | [Product analytics](/docs/product-analytics.md) | Automatic |
| Errors | [Error tracking](/docs/error-tracking.md) | Error tracking enabled |
| LLM traces | [LLM observability](/docs/ai-engineering/observability.md) | LLM observability enabled |
| Support tickets | [Zendesk](/docs/cdp/sources/zendesk.md) | Zendesk data warehouse source connected |

## Viewing a customer profile

You can access customer profiles in two main ways:

1.  **From the dashboard**: Click on any customer in the [customer analytics dashboard](https://us.posthog.com/customer_analytics)
2.  **From customer lists**: Click any [person](https://app.posthog.com/persons) or [group](https://app.posthog.com/groups/0) from the lists to open their profile

Accessing customers from insights and other producs will also land in their profile page.

## Persons vs groups

Customer profiles work for both individual [persons](/docs/data/persons.md) and [groups](/docs/product-analytics/group-analytics.md).

-   **Person profiles** show activity for a single user
-   **Group profiles** show aggregated activity for an organization, company, or any other group type you've defined

This is useful for B2B products where you care about company-level activity, not just individual users.

## Usage metrics

Each customer profile displays [usage metrics](/docs/customer-analytics/usage-metrics.md) you've defined.

![Usage metrics in customer profile](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_47_09_424_Z_893c3cd740.png)![Usage metrics in customer profile](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_46_51_933_Z_ef9223c947.png)

## Connecting support tickets

To see support tickets in customer profiles, connect Zendesk as a [data warehouse source](/docs/cdp/sources/zendesk.md).

Once connected, support tickets appear in the profile alongside events and errors. This helps you understand the full context of a customer's experience: what they did, what went wrong, and what they asked for help with.

### How tickets are matched to customers

For people, the email associated with the person is used to get their Zendesk tickets. The ticket needs to have been created from the same email for it to show up.

For groups, all tickets from a given Zendesk organization are fetched. To correlate a PostHog group to a Zendesk organization, you need to set the organization `external_id` with the value of the `groupKey` used to create the group (ideally the ID of the group in your application's database). For more information about setting up groups, see [groups docs](/docs/product-analytics/group-analytics.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better