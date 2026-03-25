# Source: https://docs.statsig.com/product-analytics/topline-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Topline Alerts

> Get notified when metrics shift beyond a fixed threshold or relative change in value.

<Info>
  Topline Alerts are in a limited beta. Please reach out if you would like these enabled for your Project.
</Info>

Topline Alerts are available in Statsig Cloud and Statsig Warehouse Native with support available for three types of Topline Alerts:

| Alert Condition Type | When to Use                                                             | Example                                                     |
| -------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Threshold**        | Use when you want to stay above or below a fixed number.                | “Alert me when P90 latency spikes above 15 seconds.”        |
| **Change**           | Use when the absolute size of the change matters.                       | “Alert me when hourly P90 latency increases by 10 seconds.” |
| **Change (%)**       | Use when the relative size of the change matters more than raw numbers. | “Alert me when hourly P90 latency increases by 50%.”        |

## Creating a Topline Alert

<Steps>
  <Step title="Navigate to Topline Alerts">
    Go to <strong>Analytics → Topline Alerts</strong> in the product menu.
  </Step>

  <Step title="Create a New Alert">
    Click <strong>+Create</strong> and give the new alert a name.
  </Step>

  <Step title="Select the Event or Metric Source">
    <p>Pick the data you want to monitor.</p>

    <ul>
      <li><strong>On Statsig Warehouse Native:</strong> Select a Metric Source, filter, and group by your desired dimensions.</li>
      <li><strong>On Statsig Cloud:</strong> Select the event, aggregation, filters, and group-by conditions for this alert.</li>
    </ul>

    <Info title="Example">
      We're setting up an alert to monitor P90 latency for <code>mex\_query</code> events, filtering out internal employee queries and grouping by the <code>hadGroupBy</code> dimension.
    </Info>

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/kJn0B4WnVhcYWq_L/images/infra-analytics/topline-alerts-choose-events.png?fit=max&auto=format&n=kJn0B4WnVhcYWq_L&q=85&s=41006739d646631086fd475172825f6d" alt="Select events or metrics for a Topline Alert" width="1357" height="409" data-path="images/infra-analytics/topline-alerts-choose-events.png" />
    </Frame>
  </Step>

  <Step title="Review the Alert Preview">
    <p>The preview shows how your metric is trending with the current setup. Confirm values look correct, or open the metric in <a href="/product-analytics/drilldown">Metrics Explorer</a> for deeper analysis.</p>

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/kJn0B4WnVhcYWq_L/images/infra-analytics/topline-alerts-preview.png?fit=max&auto=format&n=kJn0B4WnVhcYWq_L&q=85&s=2e073ec60003f7ca3ab012a29b851691" alt="Topline Alert preview showing trending metric" width="1352" height="365" data-path="images/infra-analytics/topline-alerts-preview.png" />
    </Frame>
  </Step>

  <Step title="Set Alert Conditions">
    <p>The preview updates along with each change. Define the:</p>

    <ul>
      <li>Condition type (threshold, change, change %)</li>
      <li>Directionality</li>
      <li><em>Alert</em> and <em>Warn</em> values</li>
      <li>Evaluation window</li>
    </ul>

    <Warning>
      On Warehouse Native: Define the evaluation frequency, lookback, and max delay—they directly influence warehouse compute costs.
    </Warning>

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/kJn0B4WnVhcYWq_L/images/infra-analytics/topline-alerts-conditions.png?fit=max&auto=format&n=kJn0B4WnVhcYWq_L&q=85&s=325391720b9e57ca67e39f6f58e33bc8" alt="Configure alert conditions for a Topline Alert" width="1344" height="342" data-path="images/infra-analytics/topline-alerts-conditions.png" />
    </Frame>
  </Step>

  <Step title="Add Notifications">
    <p>Notifications go to email, the Statsig Console, and Slack (if connected). Project-wide defaults live in Settings.</p>

    <ul>
      <li>Draft a clear, actionable message subscribers receive when the alert fires.</li>
      <li>Add subscribers.</li>
      <li>Set alert priority.</li>
      <li>Configure re-notification rules if alerts should resend while conditions hold.</li>
    </ul>
  </Step>

  <Step title="Save and Monitor">
    <p>Once saved, triggered alerts appear at the top of the page. From here you can:</p>

    <ul>
      <li>View samples of the event.</li>
      <li>Open the trend in <a href="/product-analytics/drilldown">Metrics Explorer</a>.</li>
      <li>Mute the alert temporarily if it is noisy or already under investigation.</li>
    </ul>

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/kJn0B4WnVhcYWq_L/images/product-analytics/topline-alerts-overview.png?fit=max&auto=format&n=kJn0B4WnVhcYWq_L&q=85&s=7aba8ba2928b861ae976283f66ed7e69" alt="Topline Alerts table with active alerts" width="2878" height="368" data-path="images/product-analytics/topline-alerts-overview.png" />
    </Frame>
  </Step>
</Steps>

## Diagnostics

Head to the <strong>Diagnostics</strong> tab to review alert history, inspect samples, jump into Metrics Explorer, or mute noisy alerts.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/kJn0B4WnVhcYWq_L/images/product-analytics/topline-alerts-diagnostics.png?fit=max&auto=format&n=kJn0B4WnVhcYWq_L&q=85&s=9b3fa474be6a819135ed7c6509bb320f" alt="Diagnostics tab showing alert history" width="2872" height="1312" data-path="images/product-analytics/topline-alerts-diagnostics.png" />
</Frame>

***

## Interested in More?

* 👉 Check out how to [create a Topline Alert on log lines](/infra-analytics/topline-alerts-logs)
* 🔔 Learn how to set up [team Slack notifications](/integrations/slack/#team-notifications)


Built with [Mintlify](https://mintlify.com).