# Source: https://posthog.com/docs/customer-analytics/create-usage-metrics.md

# Create usage metrics - Docs

**Customer Analytics is in beta**

Customer Analytics is currently in beta and free to use. We're actively developing this feature and would love your [feedback](https://app.posthog.com/customer_analytics#panel=support%3Afeedback%3Acustomer_analytics%3Alow%3Atrue).

You can create usage metrics in two ways:

1.  Go to **Settings** > **Customer Analytics** and click **Add usage metric**
2.  Open any [customer profile](/docs/customer-analytics/customer-profiles.md) and click **Add usage metric**

![Usage metrics creation form](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_24_16_161_Z_0fde31684b.png)![Usage metrics creation form](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_23_19_968_Z_a4de4c95f4.png)

### Configuration options

| Field | Description |
| --- | --- |
| Name | The column title shown in customer lists |
| Interval | Time period for the metric: 7, 30 or 90 days |
| Format | How the value should be formated: Numeric or currency |
| Match events | Which events to count toward this metric |
| Filters | Additional conditions to narrow down matched events |

### Match events

Click **Add event matcher** to specify which events count toward this metric. You can add multiple event matchers, the metric will count events matching any of them.

For example, to track API usage, you might match events named `api_request` or `api_call`.

### Filters

Filters apply to all matched events. Use them to narrow down what counts—for example, only counting successful API calls by filtering for `status = 200`.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better