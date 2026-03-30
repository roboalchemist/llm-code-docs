# Source: https://docs.anyscale.com/administration/billing/budgets.md

# Budgets

[View Markdown](/administration/billing/budgets.md)

# Budgets

Admins can set cost budgets for organizations, clouds, or projects to receive alerts when spending limits are exceeded. Budgets act as soft limits, meaning they won't restrict usage or terminate clusters. Budgets aren't supported in the CLI and SDK.

## Create a budget[​](#create-a-budget "Direct link to Create a budget")

To create or manage a budget, navigate to **Organization settings > Billing > Budgets**.

If you are an admin user, you can view the budgets of your organization by clicking the user icon, going to Organization settings, and then to the Billing tab.

![Budget Lists](/assets/images/Budget_lists-3a065a4472314efb5b72b6ce6107e4d6.jpg)

### Set the budget scope[​](#set-the-budget-scope "Direct link to Set the budget scope")

You can scope budgets across different organizational levels. Set the budget scope by targeting the clusters in clouds, projects, or both.

![Set budget scope](/assets/images/Budget_scope-542304e660f6dfde32b8db752a34236d.jpg)

Depending on the type of budget, make the following selections for the **Cloud** and **Project** fields:

| **Type of budget**                    | **Cloud**      | **Project**      |
| ------------------------------------- | -------------- | ---------------- |
| To create an organization-wide budget | All clouds     | All projects     |
| To create a cloud-specific budget     | Select a cloud | All projects     |
| To create a project-specific budget   | Select a cloud | Select a project |

Anyscale aggregates usage from all clusters within the scope to track budget status.

note

You can create only one daily and one monthly budget per cloud-project combination.

### Set the budget rule[​](#set-the-budget-rule "Direct link to Set the budget rule")

Budget rules define the parameters for how a budget operates, including:

* The time range, which is daily or monthly cycle.
* The budget amount in [Anyscale Credits](https://www.anyscale.com/pricing-detail#what-is-an-anyscale-credit) (ACs).

![Set budget rule](/assets/images/Budget_rule-3cd6487a362897cca91bafc33f591b78.jpg)

**Time range**

* Daily: Budgets reset every 24 hours, starting from midnight UTC. If you set one midday, it includes historical usage for that day.
* Monthly: Budgets reset on the 1st of each month at midnight UTC. Even if you set one up midmonth, it includes usage during the entire month. For example, if you set up a budget on January 15, it includes usage starting from January 1st.

**Budget amount**

Define the total budget amount in ACs. ACs measure processing capacity per hour and vary based on factors like machine type and data processed.

**Conversion Rates**: [AC to USD](https://www.anyscale.com/pricing-detail).

### Configure notifications[​](#configure-notifications "Direct link to Configure notifications")

When a budget exceeds 100%, Anyscale can send an alert with an email, Slack notification, or a custom webhook. Configure notification channels as needed.

To send a Slack notification, add a webhook URL to your Slack organization. Set up incoming webhooks by following Slack's [documentation](https://api.slack.com/messaging/webhooks).

**Note**: Budgets are soft limits and won't restrict usage or terminate clusters.

![Configure notifications](/assets/images/Notifications-584659243cd318b11d122b74c22e3608.jpg)

## Monitor budgets[​](#monitor-budgets "Direct link to Monitor budgets")

Admins can monitor budget status by navigating to **Organization settings > Billing > Budgets**.

![Monitor budgets](/assets/images/Monitor_budgets-85d7409cec320aa292d2bda78410ea41.jpg)

## Manage budgets[​](#manage-budgets "Direct link to Manage budgets")

* **Enable/Disable**: Admins can activate or deactivate a budget. Disabled budgets don't send alerts, but historical data applies when you re-enable them.
* **Edit**: Admins can edit the `Time range` and the `Budget amount` of an existing budget by selecting it in the listing page. If you want to change other fields, you need to create a new budget and delete the existing one to replace it.
* **Delete**: Admins can permanently delete a budget.

![Manage budgets](/assets/images/Manage_budgets-20360d17538b5fabc83bbdfb2554f672.jpg)

For further assistance, contact [Anyscale support](mailto:support@anyscale.com).
