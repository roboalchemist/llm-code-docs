# Source: https://docs.frigade.com/platform/analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics

> Frigade provides analytics and connects to external analytics platforms

## Built-in Analytics

***

Frigade provides built-in funnel analysis to help you understand the performance of your Flows. Frigade will automatically track how many users have interacted with a Flow and how many have completed it. You can also see how many users have dismissed or quit a Flow.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f632aa1260d214f0364db81a4566f739" alt="Analytics" data-og-width="3106" width="3106" data-og-height="1776" height="1776" data-path="images/platform/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=72d6dc8a6477300becc5350f3e5e7ce0 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=da579b6f77d2c7d1fd7f2811ff551df8 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fbd93eac453fa2084d86b9c93f7a0a46 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4566eb22a43927ab822444ce9880d93b 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8915b788cbdaa7d148e5968e2154f453 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/analytics.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=65a9008f491bdeb74916b03e2ca902cb 2500w" />
</Frame>

### Flow cohorts

Frigade analytics are based on user cohorts. Frigade will group users into daily cohorts based on the date they first interacted with the Flow.

You can see detailed breakdowns by hovering on any given day in the graph. Statuses include completing the Flow, dismissing or quitting the Flow, or not yet completing the Flow.

### Time windows

You can change the time range for the stats by clicking on the dropdown in the top right corner of the analytics page. You can choose between `Last 7 days`, `Last 30 days`, or `All time`. The metrics on the right side represent the totals for the selected time window, and the graph and step completion rates below will also adjust to the selected time window.

### Flow versions

Each time a new [version](/platform/versioning) of a Flow is published it will its own analytics. This allows you to review the performance of different versions of the same Flow over time.

## External Analytics

***

You can send Frigade tracking events to an external analytics platform for dashboards and reporting. Check out the [integrations](/integrations/) section to see our supported platforms.

Additionally, you can always connect Frigade to the analytics platform of your choice using webhooks. See the [webhooks](/api-reference/webhooks) documentation for more information.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9cfdcb084ead8cf77cb44421b03cfe38" alt="Groups" data-og-width="3106" width="3106" data-og-height="1776" height="1776" data-path="images/integrations/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ab1f96ac1e4c54dc18ae33bf8d0f88c 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=50be02071b773e204d8a6ea58a3b6e39 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4defa9a2e689018355b64671129b49cc 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3fffb24e60feff80877f0c7beae82304 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f63e2f3404243e8ef32d55a369d8a72e 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/overview.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=63ae0fb4d2e02604ff6d7c923064f7b4 2500w" />
</Frame>
