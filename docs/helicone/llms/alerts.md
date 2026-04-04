# Source: https://docs.helicone.ai/features/alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerts

> Get notified when your LLM applications hit error thresholds or cost limits

Helicone Alerts let you monitor error rates and costs on LLM requests to catch issues before they impact users. Each alert can be configured with filters and automatically notify through channels like Slack or email.

## Alert Metrics

Helicone supports monitoring multiple metrics to help you track different aspects of your LLM application:

| Metric                 | Description                                                                   | Use Cases                                                                                                                                |
| ---------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Error Rate**         | Track the percentage of failed requests (4XX/5XX errors) over a time window   | Detect provider outages, catch breaking changes in prompts, monitor deployment health, identify patterns in user inputs causing failures |
| **Cost**               | Monitor spending to prevent budget overruns and detect unusual usage patterns | Prevent unexpected bills, track per-environment spending, detect potential abuse, monitor cost trends for specific features or users     |
| **Latency**            | Track response time for LLM requests                                          | Monitor performance degradation, ensure SLA compliance, detect slow endpoints                                                            |
| **Total Tokens**       | Monitor combined prompt and completion token usage                            | Track overall token consumption, manage rate limits, optimize prompt efficiency                                                          |
| **Prompt Tokens**      | Track tokens sent in requests                                                 | Monitor input size, detect unusually large prompts, optimize context usage                                                               |
| **Completion Tokens**  | Track tokens generated in responses                                           | Monitor output verbosity, track generation costs, detect runaway generations                                                             |
| **Prompt Cache Read**  | Track prompt cache read tokens (supported providers)                          | Monitor cache efficiency, optimize caching strategies                                                                                    |
| **Prompt Cache Write** | Track prompt cache write tokens (supported providers)                         | Monitor cache population, understand caching patterns                                                                                    |
| **Count**              | Track the total number of requests                                            | Monitor usage volume, detect traffic spikes, track feature adoption                                                                      |

## Creating Alerts

Navigate to **Settings → Alerts** in your Helicone dashboard to create new alerts.

<Steps>
  <Step title="Configure">
    <Frame caption="Configuring an alert in Helicone">
      <div style={{ width: "70%", margin: "0 auto" }}>
        <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=3ce561c80479f0ab31bb68555c95dbb3" alt="Alert configuration interface showing metric, threshold, and time window" style={{ width: "100%" }} data-og-width="1526" width="1526" data-og-height="892" height="892" data-path="images/alerts/1AL-simple.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=4cd6fd87b83b031c23c670d0f836e039 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=d00b3192a41c5a064088d5fea04954ea 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=c739cda235f7a04b9bb5cf58bb25d47c 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=66cde0ccf64a22e0489b400756329abb 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=5c1ee9c98459e6a0d786cf8b99168981 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/1AL-simple.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=9fa116795e1d965974decf38461c499b 2500w" />
      </div>
    </Frame>

    Select the alert type (error rate or cost), set your threshold, and choose a time window.
  </Step>

  <Step title="Advanced Configuration (optional)">
    <Frame caption="Advanced alert configuration options">
      <div style={{ width: "70%", margin: "0 auto" }}>
        <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=79da4f3e5f5df478e43e75a907a2c81f" alt="Advanced configuration showing filters and minimum request thresholds" style={{ width: "100%" }} data-og-width="1526" width="1526" data-og-height="1692" height="1692" data-path="images/alerts/2AL-advanced.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=b384a02a177d52759c851f6f9612f60c 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=8d46548322509d3aeb80560a10498f22 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=2eb939ca1f362e30991cbc22df72602e 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=176d9b2e306bd553fb5892ca5da7e846 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=75ca3b9052c18895d8feb5a958882d9f 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/2AL-advanced.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=84ddf41aab4012609a7fdf4908d4569a 2500w" />
      </div>
    </Frame>

    Optionally add filters to target specific traffic, and configure minimum request thresholds to prevent false positives during low traffic periods.

    <Tip>
      Start with conservative thresholds (higher error %, longer windows) and tighten based on actual patterns. This prevents alert fatigue while you learn your app's normal behavior.
    </Tip>
  </Step>

  <Step title="Configure notifications">
    <Frame caption="Setting up alert notifications">
      <div style={{ width: "70%", margin: "0 auto" }}>
        <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=a0a878a5ab17ed4e8bae4ed2c8ecf79a" alt="Alert notification configuration showing email and Slack options" style={{ width: "100%" }} data-og-width="1566" width="1566" data-og-height="1076" height="1076" data-path="images/alerts/3AL-notifications.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=9e1a42a519fc64171e1236afa9bc8e5a 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=9828466dbc0db8827961ca94db9f4bd4 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=c992aafd9df9254cd46bb5fd8a06ec2e 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=d0e0e5391b9f2e3edca333b6a55a5736 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=db9ac20af534f2ddba4deb8b66ef130d 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/3AL-notifications.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=3d103832087fac0daabfaac8eafc909b 2500w" />
      </div>
    </Frame>

    Choose where alerts are sent:

    * **Email**: Add any email address (immediate delivery)
    * **Slack**: Select connected channels (#alerts, #engineering, etc.)
    * **Multiple recipients**: Add several emails or channels per alert
  </Step>

  <Step title="Monitor">
    <Frame caption="Helicone Alerts Dashboard showing configured alerts and their status">
      <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=f8f4b07a3bc8d6a315f345e1e0989729" alt="Helicone alerts dashboard with list of configured alerts" data-og-width="1713" width="1713" data-og-height="952" height="952" data-path="images/alerts/AL-alerts-view.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=d8386406ab0eb60c7e8dc2980a20b078 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=f5b76ebb644db6c8f89112051d03c97d 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=e5bf2982c3f5352512c0d94f4fbd4d93 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=8ec758ec8e837ed875db1b065792fb48 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=80d5bda9f144cdb2772fe09a65449332 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-alerts-view.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=82b2f816f98b280a9bc9e4160b93e6af 2500w" />
    </Frame>

    <Frame caption="Alert history showing recent triggers">
      <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=f21ca811933523b76261a116d94a1f6a" alt="Alert history view showing recent trigger events" data-og-width="3224" width="3224" data-og-height="1614" height="1614" data-path="images/alerts/AL-history.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=bd8276423f8f5a439e84d9e8cb77e77e 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=25e1997137b535dc08781bd2dea5e4b4 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=c84907aca7874106bef0ce12e3331bfb 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=de54cd3ae36ed4e6797a05c41bdf1b87 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=372b4e322760956922b385acf3bba4eb 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-history.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=4c13f574e6e0c0c292cef7e9f1b3b2fa 2500w" />
    </Frame>

    View all configured alerts, their current status, and recent trigger history in the dashboard. When an alert triggers, you can immediately see affected requests and investigate the issue.
  </Step>
</Steps>

## Configuration

### Basic Configuration

Every alert requires these fundamental settings:

* **Metric** - Choose from error rate, cost, latency, token metrics (total, prompt, completion, cache read/write), or request count
* **Threshold** - The value that triggers the alert:
  * Error rate: Percentage (e.g., 5-10% for production)
  * Cost: Dollar amount (e.g., $100, $1000)
  * Latency: Milliseconds (e.g., 1000ms, 5000ms)
  * Tokens: Token count (e.g., 100000, 1000000)
  * Count: Number of requests (e.g., 1000, 10000)
* **Time Frame** - Evaluation window for aggregating metrics (e.g., last 30 minutes, last 24 hours, last 30 days)

### Advanced Configuration (Optional)

Fine-tune your alerts with these optional settings:

* **Min Requests** - Minimum number of requests required before the alert can trigger. Prevents false positives during low traffic periods (e.g., set to 10 to require at least 10 requests in the time window)

* **Grouping** - Break down alerts by specific dimensions to track violations per group:
  * **Standard groupings**: User, Model, Provider
  * **Custom properties**: Any custom property you've added to your requests
  * When enabled, the alert tracks each group independently and shows which specific groups violated the threshold

* **Aggregation** - Choose how to calculate the metric value:
  * **Sum** (default): Total of all values (e.g., total cost, total tokens)
  * **Average**: Mean value across requests (e.g., average latency)
  * **Min**: Minimum value observed
  * **Max**: Maximum value observed
  * **Percentile**: Specify a percentile (e.g., p50, p95, p99 for latency)

* **Filter** - Target specific subsets of your traffic using the same powerful filter system as the Requests page

## Notification Channels

### Email Notifications

<Frame caption="Example alert notification email">
  <div style={{ maxHeight: "600px", overflow: "hidden" }}>
    <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=757484179f8beb006ecf70948e917fe0" alt="Email notification showing alert details and link to dashboard" style={{ width: "100%", height: "auto", maxHeight: "600px", objectFit: "contain" }} data-og-width="1054" width="1054" data-og-height="1610" height="1610" data-path="images/alerts/AL-email-example.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=24c4d1ba2bbaedf526a17663f57b3c50 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=6ffa55779cf8d5413a9fafe6301779e3 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=34fe2f379836e75d7781075dc66e7fac 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=6fe248f5441897db710085349e97819e 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=c31fb118f20239084b13ac2ba08c689c 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-email-example.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=211fd7bf1e6ae821022d5646751ab7a1 2500w" />
  </div>
</Frame>

### Slack Integration

When creating or editing an alert:

1. Select **Slack** as the notification method
2. Click **Connect Slack** button that appears
3. Authorize Helicone in your Slack workspace
4. Select a channel from the dropdown (#alerts, #engineering, etc.)

After connecting, you can simply select any channel from your workspace. Slack messages include the same details as emails with rich formatting and direct links to view affected requests.

<Frame caption="Example alert notification in Slack">
  <img src="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=fb222cca2ecbf686402f94047e2655b2" alt="Slack notification showing alert details and link to dashboard" data-og-width="1234" width="1234" data-og-height="722" height="722" data-path="images/alerts/AL-slack.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?w=280&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=4a021d914c24ba8aec5af8a28f096c0a 280w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?w=560&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=4a0b186324a49431e3c40c848644a0c4 560w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?w=840&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=b96884814cc9e9688ff43063e11c093d 840w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?w=1100&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=886661082150fbf52268aea970aa010e 1100w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?w=1650&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=b617b4fb04f21b3ece72db41e5010c40 1650w, https://mintcdn.com/helicone/LoV173ICj3D4jr2U/images/alerts/AL-slack.webp?w=2500&fit=max&auto=format&n=LoV173ICj3D4jr2U&q=85&s=2286f65329baa90d814e52b3747a085d 2500w" />
</Frame>

## Related Features

<CardGroup cols={2}>
  <Card title="Custom Properties" icon="tag" href="/features/advanced-usage/custom-properties">
    Filter alerts by environment, feature, or user segment
  </Card>

  <Card title="User Metrics" icon="users" href="/features/advanced-usage/user-metrics">
    Track costs and errors per user to set appropriate thresholds
  </Card>

  <Card title="Sessions" icon="link" href="/features/sessions">
    Monitor multi-step workflows that might trigger alerts
  </Card>

  <Card title="Datasets" icon="database" href="/features/datasets">
    Collect examples of requests that triggered alerts for analysis
  </Card>
</CardGroup>
