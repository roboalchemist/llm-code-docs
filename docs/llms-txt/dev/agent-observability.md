# Source: https://dev.writer.com/home/agent-observability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor agent performance

> Monitor agent performance with session logs and observability metrics in AI Studio. Track usage, analyze conversations, and debug agent behavior.

AI Studio provides session logs and observability metrics for agents so you can understand how your agents are performing.

The following observability views are available for individual agents:

* [Session logs](#session-logs)
* [Agent observability](#agent-observability)

You can also view [global usage and spend](/home/observability) for your organization.

## Session logs

Organization admins can choose to retain logs from agent sessions. When enabled, you can view the logs for an agent for the given retention period.

<Info>
  Session logs are only available to [organization admins](https://support.writer.com). Logs are available for custom [no-code agents](/no-code/introduction) and [Writer Agent](https://support.writer.com/article/235-ask-writer), but are not yet available for prebuilt agents.
</Info>

### Enable session logging

To enable session logging, log in to [AI Studio](https://app.writer.com/aistudio) and navigate to the **Admin** tab in the left sidebar.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=b58aad872d7b07866131b08d6211bcc5" alt="Session log page in the Admin tab, which shows a list of agents and their session log settings." data-og-width="3172" width="3172" data-og-height="1684" height="1684" data-path="images/home/session-logs-admin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=0b7aa77f74d15ac313cda05b842540c9 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=6e5f486a8e19cc78daa74f5b0f9256f7 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=5f0f76ce2714aba04d987977b8798581 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=40aeaf857cbcdd0779616e747680126c 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=ad68fdb18547dab038d93d46cd965019 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/session-logs-admin.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=545e8ebd3379a66a0bfed5fbb36ffcea 2500w" />

From there, you can enable session logging for your organization.

Once enabled, you can choose the retention period for session logs for each agent. The default is no retention. The possible retention periods are 7 days, 30 days, 90 days, or 180 days.

Whenever someone updates an agent's session log settings, all organization admins receive an email notification.

### View session logs

To view session logs, navigate to [AI Studio](https://app.writer.com/aistudio) and select **Agents** from the left sidebar. Select an agent from the list, then select the **Observability** tab from the top of the page and choose the **Session logs** view. Click on an individual session to view the logs.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=15c696097203e5901807243dcfb52d63" alt="Session logs tab in AI Studio" data-og-width="3346" width="3346" data-og-height="884" height="884" data-path="images/home/agent-session-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a7b698e3372390bec6f1f42354caa7d7 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c395ce2df2cd8e6fa85b44242182a240 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=85d0dbcb56f9d742e319c7f55de0d152 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7c42aa4c9b2be08bf34f965ed828e473 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=786244119b3eadffb442ed02495ef9a1 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/home/agent-session-logs.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ebb4b178617997b743d37b93370b5229 2500w" />

#### Flagged responses

In a chat with a no-code agent, an end user can flag a response as inappropriate or inaccurate. An organization admin can then view the flagged responses within the session logs.

To flag a response in a chat, the user clicks the **Flag** button in the bottom right corner of the response.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=703838451f5ff82d87fbd0816aa4cfd0" alt="Button to flag a response within a chat" data-og-width="608" width="608" data-og-height="160" height="160" data-path="images/home/flag-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=51063df0bc5ab6f9121c1c1a2b7fb189 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=85acaad36a292d6fa8a742a29714a6db 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=37d43cbedb318f24ad895ffc9bc6a4de 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=5de8a9d172007886abb9ac1737d5cd72 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=659dbdbea3ef6a2e28ca61555327f743 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/flag-response.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=c2f001a87c2f1b4818d9bc9c42d87e80 2500w" />

In the session logs for a particular conversation, you can see any flagged responses by clicking the **View flagged responses** button in the top right corner of the session log.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=7bc2626f4aff561d059ebbbe455c16d4" alt="Button to view flagged responses for a particular conversation" data-og-width="552" width="552" data-og-height="140" height="140" data-path="images/home/view-flagged.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=239c775f5a5270d2751a008723aa173b 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e60c22df0c2d9b78cf773a35a75bac04 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=79e45d2a8f2a97294fbab932ab7842a6 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e4d202d00904a7dbb62834deb30b3562 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=2e3e7403bd081f8d7f717bfcf7f1d68f 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/home/view-flagged.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=5a623afd4e6244688a901e3110da4f24 2500w" />

## Agent observability

Agent observability provides a detailed view of an agent's engagement, performance, and usage. Anyone can view these metrics for agents in your organization. Session logs are also available, but [only for organization admins if the agent's session log settings are enabled](#view-session-logs).

These metrics are only available for deployed agents.

To view metrics for deployed agents, navigate to [AI Studio](https://app.writer.com/aistudio) and select **Agents** from the left sidebar. Select an agent from the list, then select the **Observability** tab from the top of the page and choose the specific metric you want to view.

* **Engagement metrics**: Show the top five users for the agent over the specified time period and the total number of user interactions for the agent.
* **Performance metrics**: Show the average response time as well as the P90, P95, and P99 response times for the agent over the specified time period. It also shows the response codes broken down by `200`, `400`, and `500` status codes.
* **Usage metrics**: Show the total number of tokens and the total spend for the agent over the specified time period.

## Next steps

* [Track platform-wide usage and spend](/home/observability) across all agents in your organization
* [Export telemetry data](/home/integrations/openllmetry) to your existing observability tools via OpenLLMetry
* [Configure guardrails](/home/guardrails) to enforce content policies across your agents
