# Source: https://docs.asapp.com/agent-desk/insights-manager/live-insights/metric-definitions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metric Definitions

> Learn about the metrics available in Live Insights.

## Performance - 'Right Now' Metrics

| **Metric name**                       | **Definition**                                                                                                                                                                                              |
| :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Offered**                           | The number of conversations that are currently connected with an agent or waiting in the queue.                                                                                                             |
| **Assigned to Agent**                 | The number of conversations where a customer is currently talking to a live agent.                                                                                                                          |
| **Timed out by Agent**                | Only available as a current period metric for the day.                                                                                                                                                      |
| **Queued**                            | The number of customers who are waiting in the queue to be connected to an agent.                                                                                                                           |
| **Queued - Eligible for Assignment**  | The number of customers who are waiting in the queue, received a check-in message, and replied to it.                                                                                                       |
| **Max Queue Time**                    | The actual wait time of the customer who is positioned last in the given queue.                                                                                                                             |
| **Average Wait Time**                 | The average queue time for all customers who are currently assigned to an agent or waiting in the queue, including 'zero-time' for customers directly assigned to an agent when there were available slots. |
| **Average Time in Queue**             | The average queue time for all customers who are currently waiting in the queue.                                                                                                                            |
| **Average Time to Assign**            | The average queue time for all customers who are currently assigned to an agent, including 'zero-time' for customers directly assigned to an agent when there were available slots.                         |
| **Queue Abandons**                    | Only available as a current period metric for the day.                                                                                                                                                      |
| **Average Abandon Queue Time**        | Only available as a current period metric for the day.                                                                                                                                                      |
| **Queue Abandonment Rate**            | Only available as a current period metric for the day.                                                                                                                                                      |
| **Average Agent Response Time**       | The average amount of time to respond to a customer message across the assignment for agents who are currently handling chats.                                                                              |
| **Average Agent First Response Time** | The average amount of time to send the first line to a customer after the chat was assigned for agents who are currently handling chats.                                                                    |
| **Average Handle Time**               | The time spent across all current chats by an agent per assignment starting from when the chat was assigned to when it is dispositioned.                                                                    |
| **Active Slots**                      | A ratio of the number of currently active conversations to number of concurrent slots for agents who are in an Active status or actively handling chats.                                                    |
| **Occupancy**                         | The percentage of currently assigned chats to the number of agents with slots set to active.                                                                                                                |
| **Concurrency**                       | The percentage of currently assigned chats to the number of agents with currently assigned chats.                                                                                                           |
| **Logged In Agents**                  | The number of agents currently logged in to Agent Desk.                                                                                                                                                     |
| **Active and Away Agents**            | The number of agents with an active-type and away-type label respectively.                                                                                                                                  |
| **Agent Status**                      | The number of agents with each status label.                                                                                                                                                                |

## Agent Metrics

| **Metric name**           | **Definition**                                                                                                                                                                                                          |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agent Name**            | Name of the agent currently logged in to Agent Desk. Agents currently handling assignments have their names underlined. When you click, the system displays the agent's current assignments in the 'Conversations' tab. |
| **Agent Status**          | Name of the status selected by the agent in Agent Desk. Green labels represent Available statuses, while orange labels represent Away statuses.                                                                         |
| **Time in Status**        | The time an agent has spent in the currently displayed status.                                                                                                                                                          |
| **Average Handle time**   | The time spent across all current assignments, starting from when the chat was assigned to when it is dispositioned, for a given agent.                                                                                 |
| **Average Response Time** | The average amount of time to respond to a customer message across all current assignments for a given agent.                                                                                                           |
| **Assignments**           | The number of assignments an agent is currently handling.                                                                                                                                                               |

## Conversation Metrics

| **Metric name**           | **Definition**                                                                                    |
| :------------------------ | :------------------------------------------------------------------------------------------------ |
| **Issue ID**              | Unique conversation identifier that the system assigns to a customer intent.                      |
| **Agent Name**            | Name of the agent handling the conversation.                                                      |
| **Channel**               | Channel the customer is engaging with.                                                            |
| **Intent**                | Last detected intent before the system assigns the user to the queue.                             |
| **Queue Membership**      | Queue where the system assigned the issue based on intent classification and queue routing rules. |
| **Time Assigned**         | Time when the system assigned the conversation to an agent.                                       |
| **Handle Time**           | Current handle time of the conversation.                                                          |
| **Average Response Time** | Average time it takes an agent to reply to customer utterances.                                   |
| **Time Waiting**          | Time since the last message sender awaits a response.                                             |
| **Alerts**                | Event-based signals that the system records throughout the conversation.                          |

## Performance - 'Current Period' Metrics (since 12 am)

| **Metric name**                       | **Definition**                                                                                                                                                                                                      |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Offered - Total**                   | The total instances where the conversation was either placed in queue or assigned directly to an agent attributed to the time interval the Queue or direct Assignment event (without being placed in queue) occurs. |
| **Assigned to Agent - Total**         | The total instances where the customer was assigned to an agent.                                                                                                                                                    |
| **Timed Out by Agent - Total**        | The total instances assigned to an agent where they "Timed Out" the customer.                                                                                                                                       |
| **Queued - Total**                    | The total instances where a customer was placed in or is currently waiting in the queue to be connected to an agent.                                                                                                |
| **Queued - Eligible for Assignment**  | Only available as a right now metric.                                                                                                                                                                               |
| **Max Queue Time**                    | Only available as a right now metric.                                                                                                                                                                               |
| **Average Wait Time**                 | The average time a customer waited to abandon or be assigned to an agent, including 'zero-time' for customers directly assigned to an agent when there were available slots.                                        |
| **Average Time in Queue**             | The average time a customer waited in queue for those who either abandoned the queue or were assigned to an agent.                                                                                                  |
| **Average Time to Assign**            | The average queue time for all customers who were assigned to an agent, including 'zero-time' for customers directly assigned to an agent when there were available slots.                                          |
| **Queue Abandons**                    | The total count of customers who abandoned the queue.                                                                                                                                                               |
| **Average Abandon Queue Time**        | The average time a customer waited in queue prior to abandoning, either by being dequeued on the web or ending the chat before being assigned to an agent.                                                          |
| **Queue Abandonment Rate**            | The percent of customers who required a visit to the queue and abandoned before being assigned to an agent.                                                                                                         |
| **Average Agent Response Time**       | The average amount of time it takes an agent to respond to a customer message across all assignments.                                                                                                               |
| **Average Agent First Response Time** | The average amount of time it takes an agent to send the first line to a customer after the chat was assigned across all assignments.                                                                               |
| **Average Handle Time**               | The average amount of time spent by an agent per assignment, from when the chat was assigned to when the agent finishes dispositioning the assignment.                                                              |
| **Active Slots**                      | Only available as a right now metric.                                                                                                                                                                               |
| **Occupancy**                         | The percentage of cumulative utilization time to cumulative available time for all agents who handled chats.                                                                                                        |
| **Concurrency**                       | The weighted average number of concurrent chats that agents are handling at once, given an agent is utilized by handling at least one chat.                                                                         |
| **Logged In Agents**                  | Only available as a right now metric.                                                                                                                                                                               |
| **Active and Away Agents**            | Only available as a right now metric.                                                                                                                                                                               |
| **Agent Status**                      | Only available as a right now metric.                                                                                                                                                                               |

## Teams and Locations

You can track the live behaviors of agents by overseeing outages and staff levels at different geographic locations. Furthermore, each team provides hourly updates as to who is active/lunch etc and they want to be able to get this information easily.

Admins see a list of agents when they click into a particular queue and select Performance from the left-hand panel and clicked into the Agents icon on the right-hand panel. Admins can further oversee results by performance metrics of the current day and filter both the agent list and metrics by any of the following attributes:

* **Agent Name**
* **Location**
* **Team**
* **Status**

### Team Table

Admins can filter teams by type of role and review each company assigned to the team. Also, each result shows the size and the occupancy of each team.

Each administrator can provide an hourly update of how many agents are active, on lunch, or in a different state as well as view corresponding metrics.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=168470f76294c6a9485bc9b7d2060676" data-og-width="1304" width="1304" data-og-height="807" height="807" data-path="image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9b8a3ff9c222c34be666c5177e4f8043 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0a61aec0a9dd7fa886b02c935b77d134 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c52e803e25d11a97931c893c6e2fcd2c 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=f473882dc773d19b2a15833213348d98 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=31dc6ec9dfdfdf313420d18b3967fe4a 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-28cd97c5-0043-6d41-19f7-f206fa2c9573.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c82fed23ba2fa98a405c8774d20a319f 2500w" />
</Frame>

### Location Table

Admins can filter locations by region and review the occupancy and size of each location.

Each location provides updates of performance and agent names.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=604fb418fbbf38106515db37f72c3b86" data-og-width="1301" width="1301" data-og-height="812" height="812" data-path="image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c8c7321584ec4e8fbf1ccf8a293a4800 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6f1f26930c6d7961c317941f38ea98ca 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a48aed361ce55bfd86bf1961ce30ebb7 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=caa205723b07ab35f82341bcd83bcf5f 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=dd726825564dca6a14aaa13b272c2c95 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bed415e-39a5-f14e-07bc-d30b485ccd04.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=39d8fea530ea219a86cc65aa35327a90 2500w" />
</Frame>
