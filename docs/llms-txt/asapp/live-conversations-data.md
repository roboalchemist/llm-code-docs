# Source: https://docs.asapp.com/agent-desk/insights-manager/live-insights/live-conversations-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Conversations Data

> Learn how to view and interact with live conversations in Live Insights.

You can find all conversations that are currently connected to an agent in Live Insights.

Performance data updates automatically in Live Insights. If a conversation's metrics are outside their target range, the system displays alerts.

## Conversation Activity

The conversation activity table is the bread and butter of real-time monitoring.

You can see all conversations currently assigned to an agent. You can sort content by performance metrics to provide you with the view that is most relevant to your needs. Live Insights automatically refreshes performance data every 15 seconds.

Furthermore, you can access live transcripts for each conversation currently assigned.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=6e4be094f3f0d8b45d799d80cf48ff8a" data-og-width="2592" width="2592" data-og-height="1868" height="1868" data-path="images/messaging-platform/insights-manager/conversation-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=b8576863621ed5d7ab33e9bf081abf48 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=9cd996d473556b45bb4ec9c62409ea49 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7244b551e06bf260891ee0c77c78b2f4 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=496f57f9ff1eedc85cde9b2aa538ef7d 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=f1caf6f5574e3929be12f74e8072b8df 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-activity.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=9293b75ec86fdf81736bf49c76161631 2500w" />
</Frame>

1. **Links**: Provides a quick entry point to view historical transcripts or performance data.
2. **Conversation count & refresh**: Displays the total conversations displayed in the table. Live Insights updates the content automatically every 15 seconds.
3. **Sorting**: You can sort the content by each of the metrics captured for each conversation. You can sort all columns in ascending/descending order. To sort, click the **column header**. Click the **header** again to reverse the sorting order. Default: Ascending by time assigned.
4. **Conversations**: Each conversation currently assigned to an agent displays as a row in the Conversation Activity table. Metrics associated with the conversation display and update dynamically.
5. **Metric highlighting**: Metrics that have assigned thresholds are highlighted. See 'Metrics Highlighting' for more information.
6. **Alerts**: When an event is recorded, it displays in the column. Not all conversations will include an event.

<Tip>
  See [Alerts, Signals & Mitigation](/agent-desk/insights-manager/live-insights/alerts,-signals---mitigation "Alerts, Signals & Mitigation") for more information.
</Tip>

## Conversation Data Anatomy

Each row in the conversation activity table lists performance data.

The chart below outlines data available in Live Insights for each chat conversation.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=baf8402e0e8c58304fced360b2d383ab" data-og-width="1620" width="1620" data-og-height="968" height="968" data-path="images/messaging-platform/insights-manager/conversation-data-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=be220dcc1594f4cc5f734255b8a31d9c 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a50442d010576a484bb16e747217e085 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=0bb1760a3b2e0bc24fe5e2e3c747edc2 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=ddee0ae18ae6173f6f2b5a4a29a0fcbb 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=dfbaccbc4dc095412992aa91bee0e1fc 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/conversation-data-activity.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7c45d6aef484efa85ad8988d83ed161f 2500w" />
</Frame>

1. **Issue ID**: Unique conversation identifier that the system assigns to a customer intent.
2. **Agent name**: Name of the agent handling the conversation.
3. **Channel**: Detected channel the customer is engaging with.
4. **Intent**: Last detected intent before the system assigns the user to the queue.
5. **Time Assigned**: Time when the system assigned the conversation to an agent.
6. **Handle time**: Current handle time of the conversation.
7. **Average Response Time**: Average time it takes an agent to reply to customer utterances.
8. **Time Waiting**: Time since the last message that the sender has been waiting for a response.
9. **Alerts**: Event-based signals recorded throughout the conversation.
10. **Queue name**: Name of the queue that received the issue assignment. This feature only displays in Queue Groups. Click the **queue name** to go to the queue details view.

## View a Live Transcript

Each conversation connected to an agent includes a live transcript that you can view.

The transcript updates in real time. You can send a Whisper to the agent from the transcript.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=260df7f3930178944cdc348a493d5d29" data-og-width="2588" width="2588" data-og-height="1868" height="1868" data-path="images/messaging-platform/insights-manager/viewing-transcript.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=0ab2ae56c24b6fc7b3d389d42aff855c 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=f348341a1f03d42821da536501934319 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e264a83d20492a3924d147ae485523b6 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=ad2b112124e03f9dd20917533c7ff964 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a746cefdba9640d6de2b460ce26c683c 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/viewing-transcript.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=07421733d434a9d5775336dd25527efc 2500w" />
</Frame>

1. **Open transcripts**: To view a transcript, click any **row** in the Conversation Activity table.
2. **Transcript**: The transcript updates in real time. The system displays handle time alongside conversation data (issue ID, agent, channel and intent).
3. **Close transcripts:** To close a transcript, click the **Close** icon.
4. **Whisper**: A Whisper allows you to send a discrete message within the transcript that agents can see but that the system hides from customers.

## Conversations: Current Performance Data

Current queue performance data appears to the right of the activity table.

These metrics encompass all conversations currently in the queue or connected to an agent.

You can view a drill-down, enhanced view of the performance data under the Performance page.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=90ad185a6bb2e25647af53f8863bcf1d" data-og-width="2592" width="2592" data-og-height="1868" height="1868" data-path="images/messaging-platform/insights-manager/current-performance-data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7773d945c40c4825e4be4386cd787ad3 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=30332907db756205f8b09440e17a9fa9 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=dafe5b6d387dd2d084f55ec22e043fa6 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=8ba742b339a3d50c70248854cab54fdd 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=31492ab1fe3dfaefc34c5ac31a93b779 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/current-performance-data.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=cf16e25e7831ca5bd982148ce137bd5e 2500w" />
</Frame>

1. **Queue Activity**: Includes 'Queued', 'Avg current time in queue', 'Average wait time', and 'Average time to assign'.
2. **Volume**: Includes 'Offered', 'Assigned to agent', and 'Time out by agent'.
3. **Handle & Response Time**: Includes 'Average handle time (AHT)', 'Average response time (ART)', and 'Average first response time (AFRT)'
