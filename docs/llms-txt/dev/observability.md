# Source: https://dev.writer.com/home/observability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Platform observability

> Monitor usage, costs, and agent performance across your organization

AI Studio provides observability tools to help you understand how your organization uses AI and how your agents perform. Track spending and token usage at the organization level, or drill down into individual agent sessions to debug and optimize performance.

<CardGroup cols={2}>
  <Card title="Usage and spend" icon="chart-pie" href="#track-usage-and-spend">
    Monitor organization-wide costs, token usage, and consumption trends.
  </Card>

  <Card title="Agent performance" icon="gauge-high" href="/home/agent-observability">
    View session logs, debug conversations, and track agent-level metrics.
  </Card>
</CardGroup>

## Track usage and spend

<Info>
  The Consumption view is only available to [organization admins](https://support.writer.com).
</Info>

The Consumption view in AI Studio gives you a detailed view of your usage and spend month-by-month across all agents.

To access this view, [log in to AI Studio](https://app.writer.com/aistudio) and select the **Consumption** tab in the left sidebar.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=ab19b2ef2bb32d3fb54acce3836b7081" alt="Consumption view in AI Studio" data-og-width="276" width="276" data-og-height="322" height="322" data-path="images/home/consumption-sidebar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=edb4fdd6d2414c31b5380c8be62732c2 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e79c1bf0189bf976cf7031ade91f1ebc 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e4351b1596765558f41fcd825dff3e34 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=2ce6eb112595b0db4256515f7d2cdfd8 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=2b64ed70376a2f32dbd02a04abfa0c46 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/consumption-sidebar.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=26643b20a36917107d3025d31033ae03 2500w" />

You can switch between a cost view and an activity view, which shows the number of tokens used for each agent type. See below for more details about the data available in the [cost view](#cost-view) and the [activity view](#activity-view).

The image below shows the cost view for a sample organization.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=0b036ff3e33d2b42f64c8e413e112f8c" alt="February 2025 usage report showing $1,509.645 total spend, broken down by agent type (API, Framework, No-code) and spend source (LLM models, Others)." data-og-width="1792" width="1792" data-og-height="1278" height="1278" data-path="images/home/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=02afe1392c24a6f6056ec24106c6dc6d 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=8796c483e2f32fca8e3de5a99679e1fe 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=95e0bbaa60262ad2127813f43136f2c4 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=06b84e5f89c872b714a32c21915280d4 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=d0e5f3e82a8509f40fdf544702d081f4 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/usage.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=5beee59d9b168c588ebc617381a372dc 2500w" />

### Cost view

The cost view shows the following information:

* **Monthly usage-based spend**: The total cost of usage for the month, with a comparison to the previous month.
* **Spend by agent type**: A day-by-day breakdown of the cost of usage by agent type (API, Framework, and No-Code).
* **Spend breakdown**:
  * **LLM models**: The usage cost for each LLM model.
  * **Others**: The usage cost for all other services, such as Knowledge Graph hosting, web access, and optical character recognition (OCR).

### Activity view

The activity view shows the following information:

* **Monthly token usage**: The total number of tokens used for the month, with a comparison to the previous month.
* **Top users by token usage**: The top five users with the most token usage.
* **Top agents by token usage**: The top five agents with the most token usage.
* **Token usage by agent type**: A day-by-day breakdown of the token usage by agent type (API, Framework, and No-Code).
* **Token usage by model**: The total number of tokens used for each model.

## Next steps

Learn how to monitor individual agent performance with [session logs and agent metrics](/home/agent-observability).
