# Source: https://www.metabase.com/docs/latest/questions/alerts

<div>

1.  [Home](/docs/latest/)
2.  [Questions](/docs/latest/questions/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Alerts

Set up an alert to send the results of questions to people via email or Slack, or to a webhook.

Alerts are for questions only. If you instead want to get the results of a dashboard sent to you, check out [dashboard subscriptions](../dashboards/subscriptions).

## Prerequisite for alerts

To start using alerts, an administrator will need to have set up at least one of the following notification channels.

-   [Email](../configuring-metabase/email)
-   [Slack](../configuring-metabase/slack)
-   [Webhooks](../configuring-metabase/webhooks)

Only admins and people with [settings access](../permissions/application#settings-access) can use webhooks.

## Creating an alert

![Get alerts](./images/get-alerts-about-this.png)

To create an alert:

1.  Save your question.
2.  Click on the **three dots** in the top-right of the screen.
3.  Select **Create an alert**.
4.  Select what you want to be alerted about (options depend on the question type):
    -   [When a question returns a result](#results-alerts) - for any question.
    -   [When a time series crosses a goal line](#goal-line-alerts) - for a line, bar, or area chart displaying a time series.
    -   [When a progress bar reaches or goes below its goal](#progress-bar-alerts) - for progress bars.
5.  Select when you want Metabase to check the results: by the minute, hourly, daily, weekly, monthly, or on a custom schedule that you set using the Quartz [cron syntax](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html).
6.  Select the alert's destination: [email](../configuring-metabase/email), [Slack](../configuring-metabase/slack), or to a [webhook](../configuring-metabase/webhooks) (only admins and people with [settings access](../permissions/application#settings-access) can create and send to webhooks).
7.  Configure any other options (like [only sending the alert once](#send-a-one-time-alert)).
8.  Click **Done**.

## Send a one-time alert

When setting up an alert, if you select the option to **Only send the alert once**, Metabase will send that alert once, then delete itself, never to alert anyone ever again. These "disposable" alerts are handy for things like letting you know when you reach a one-time milestone.

## Testing alerts

To test the alert, first make sure that the question returns results (if the question doesn't return any results, Metabase won't send the alert).

Then hit the **Send now** button to trigger the alert.

## Results alerts

Metabase can send you an alert on a schedule when one of your questions returns *any* result. This kind of alert is also particularly useful if you have a question that doesn't *usually* return any results, but you want to know when the question *does* return results.

For example, you might have a table called `Reviews`, and you want to know any time a customer leaves a bad review, which you consider to be anything below three stars. To set up an alert for this situation, you'd go and create a raw data question (i.e., a question that returns a list of reviews), and add a filter to only include results with fewer than three stars.

You probably don't want to be alerted about all the bad reviews you've *ever* gotten, but just recent ones. So you can add a filter to only include results from yesterday or today, depending on how often you want to check for these bad reviews. At this point, when you check the results of this question, it probably won't return any results, which is a good thing.

Save the question, create an alert, and select how often you want Metabase to check this question for results. That's it!

## Goal line alerts

*Requires a [bar, line, or area chart](./visualizations/line-bar-and-area-charts) with a goal line.*

Goal line alerts are useful when you're doing things like tracking daily active users (DAU) and you want to know when you reach a certain number of DAU, or when you're tracking orders per week and you want to know whenever the number of orders ever goes below a certain threshold.

To create an alert when a time series crosses a goal line:

1.  Create a line, area, or bar chart displaying a number over time.

2.  Open up the visualization settings by clicking the **gear** icon in the bottom-left.

3.  In the **Display** tab, turn on the **Show goal** setting.

4.  Choose a value for your goal (and optionally a label) and click Done.

5.  Save the question.

6.  Click the **three dots** icon in top and select "Create alert"

    You can choose:

    -   Whether you want Metabase to alert you when the time series goes above the goal line or when it goes below the goal line.
    -   Whether you want Metabase to alert you every time the time series crosses a goal line, or only the first time it crosses the goal line.
    -   How often you want Metabase to check to see if the goal line has been crossed.

7.  Select the schedule and recipients for the alert, and click "Done"

## Progress bar alerts

*Requires the [progress bar visualization](./visualizations/progress-bar).*

If you want to set up an alert when a single number reaches a goal, you can use a progress bar visualization.

1.  Create a question that returns a single number as its result.
2.  Choose the Progress Bar chart type.
3.  In Visualization settings, select a goal value.
4.  Save your question.
5.  Create an alert by clicking the **three dots** in top right.

You'll see the options for when you want to get alerts about this progress bar:

-   Whether to alert when the progress bar reaches the goal line or below the goal,
-   Whether to alert only the first time the progress bar reaches the goal line, or every time
-   How often you want Metabase to check to see if the goal has been reached.

## Editing, deleting, and unsubscribing from alerts

To edit or delete alerts on a question, click on the **three dots** icon in the top right corner and select **Edit alerts**. What you can edit depends on whether you're an admin.

Everyone:

-   Everyone can edit alerts that they've personally set up (but not alerts set up by other people).
-   Everyone can view and unsubscribe from all alerts they receive by clicking on the **gear** icon in the upper right and navigating to **Account settings** \> **Notifications**.

Admins:

-   Admins can edit and delete any alert. This can't be undone, so be careful!
-   Admins can add or remove recipients on any alert, even ones that they didn't create themselves.
-   Admins can bulk manage alerts per person from the [People menu in Admin settings](../people-and-groups/managing#unsubscribe-from-all-subscriptions-and-alerts).

Metabase will email you when:

-   You set up an alert
-   You've been unsubscribed from an alert
-   One of your alerts has stopped working
-   You unsubscribed from an alert
-   An admin added you to an alert

## Avoid changing the name of the alerted channel in Slack

Once you set up an alert to a Slack channel, avoid changing the name of that channel in Slack. If you rename the channel in Slack, but you want Metabase to continue to send alerts to that renamed channel, you'll need to update the alert in Metabase to point to the new channel name.

## Alert expiration and special cases

Some circumstances will automatically change or delete alerts:

-   **You rename the target Slack channel**. Well, technically the alert won't get deleted, but Metabase will no longer have anywhere to send the alerts to. You'll need to update the alert's target channel in Metabase to the new channel's name.
-   **If a goal line is removed from the question powering a "Goal line" alert**, the alert will change to a "Results" type alert.
-   **If the question is deleted**, Metabase will delete any alerts set up for that question.

Alerts will continue to work *even if the person who set up the alert no longer has an active account*. For example, if an alert with multiple recipients (or to a Slack channel) was set up by someone whose account has since been deactivated, that alert will continue to work (though Metabase will stop sending the alerts to the deactivated account).

## Admins can see all alerts

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Usage analytics is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

Admins can view a list of all alerts and dashboard subscriptions that people have set up in your Metabase in the **Usage analytics** collection. See [Usage analytics](../usage-and-performance-tools/usage-analytics#alerts-model).

## How permissions work with alerts

See [Notification permissions](../permissions/notifications).

### Sending alerts to private Slack channels

See [Sending alerts and subscriptions to private Slack channels](../configuring-metabase/slack#sending-alerts-and-subscriptions-to-private-slack-channels).

## Removing Metabase branding from alerts

See [Remove Metabase branding from exports](./exporting-results#remove-metabase-branding-from-exports).

## Further reading

-   [Dashboard subscriptions](../dashboards/subscriptions)
-   [Setting up email](../configuring-metabase/email)
-   [Setting up Slack](../configuring-metabase/slack)
-   [Usage analytics](../usage-and-performance-tools/usage-analytics)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/questions/alerts.md) ]