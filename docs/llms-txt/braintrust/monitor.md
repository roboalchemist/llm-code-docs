# Source: https://braintrust.dev/docs/deploy/monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor deployments

> Track production performance and errors

Every production request flows through the same observability system you used during development. The Monitor page provides custom dashboards to track performance, costs, errors, and quality metrics across your deployed prompts and functions.

## View production metrics

The <Icon icon="chart-no-axes-column" /> **Monitor** page shows custom dashboards for tracking deployed prompts and functions. For details on creating custom charts, filtering data, selecting timeframes, and configuring dashboards, see [Monitor with dashboards](/observe/dashboards).

Production-specific metrics include:

* **Request count**: Volume of production traffic
* **Latency**: Response time (total duration, time to first token)
* **Token count**: Prompt tokens, completion tokens, and total usage
* **Cost**: Estimated spend based on model pricing
* **Scores**: Quality metrics from online scoring
* **Tools**: Tool call frequency and success rates

Filter by production environments, models, or errors to focus on specific segments. Group by model, environment, user, or custom metadata to analyze patterns across your deployments.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4c4b117a23bf49845bd74197c4429dce" alt="Monitor overview" data-og-width="3138" width="3138" data-og-height="1372" height="1372" data-path="images/guides/monitor/monitor-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=83d842d1748e3b426226f1413cb2d3f6 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4601a72cdc69c776a8a3440c87c2848f 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=064fd20702529c4d00cb6d1b15edeee0 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=aa25a846492a840b4740375f4109d6ba 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d432626a514d2961a15b7d639192da7d 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=992db3d4cb5bc1049cb1962464b1c778 2500w" />

## Set up alerts

Configure alerts to notify you when metrics exceed thresholds:

1. Navigate to **Configuration** > **Automations**
2. Click **+ Alert**
3. Define your conditions using SQL queries
4. Set notification channels (email, Slack, webhooks)

Example alerts:

* Error rate exceeds 5% for 10 minutes
* Average latency above 2 seconds
* Daily cost exceeds budget threshold
* Score drops below 0.8

See [Alerts](/admin/automations/alerts) for detailed configuration.

## Track costs

Cost charts estimate spending based on model pricing. Costs are calculated from:

* Token counts (prompt and completion)
* Model pricing rates
* Provider-specific pricing tiers

<Note>
  Cost estimates are approximate. Actual billing from providers may vary based on rate limits, batch discounts, and other factors.
</Note>

## Monitor quality

Online scoring automatically evaluates production requests. View score distributions and trends in the Monitor page:

* Group by score name to compare different quality metrics
* Filter by low scores to find problematic requests
* Track score changes over time to detect quality regressions

Configure online scoring in **Configuration** > **Online scoring**. See [Score online](/observe/score-online) for details.

## Next steps

* [Score online](/observe/score-online) to automatically evaluate production requests
* [Set up alerts](/admin/automations/alerts) to catch issues proactively
* [View logs](/observe/view-logs) to investigate specific requests
* [Use dashboards](/observe/dashboards) for detailed observability
