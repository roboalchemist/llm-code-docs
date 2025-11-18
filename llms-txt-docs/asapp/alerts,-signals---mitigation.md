# Source: https://docs.asapp.com/messaging-platform/insights-manager/live-insights/alerts,-signals---mitigation.md

# Alerts, Signals & Mitigation

> Use alerts, signals, and mitigation measures to improve agent task efficiency.

To improve user focus and task efficiency, ASAPP elevates various alerts and signals within Live Insights.

These alerts notify users when performance is degrading, when events are detected, or when high queue mitigation measures can be activated based on volume.

## Type of Alerts

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e4b52417eff6c8214f0b43be6315cb1b" data-og-width="1704" width="1704" data-og-height="2362" height="2362" data-path="images/messaging-platform/insights-manager/alert-types.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=2191ce627379cb913d80151f203ada85 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=8b2c5557699d3dc65e112f66a26143bd 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=ec9fc24b61d33fef127aba644d73b846 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a3cddba2e25c50a4dfe7c07b670a3b1c 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7ed2ecb84b10241e1480ea35b20c6bdc 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/alert-types.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=094742010146db4a7b652469d4f8fc9c 2500w" />
</Frame>

Live Insights displays four alert types:

1. **Metric Highlighting**: Highlights metrics that are above their target threshold within Live Insights. You can see the highlights on the Overview page, as well as within single queues and queue groups. The alert will persist until the metric's performance returns below its threshold.
2. **Event-based Alerts**: Detects and records events per conversation and displays them in the conversation activity table.
3. **High Queue Mitigation**: Activates when the queue volume exceeds the target threshold. When active, you can use mitigation measures to reduce queue volume impacts.
4. **High Effort Issue**: Indicates when a high effort issue is awaiting assignment and is currently blocking other issues from being assigned.

## Metric Highlighting

Live Insights highlights metrics that are above their target threshold on the Overview page, as well as within single queues and queue groups.

The alert persists until the metric's performance returns below its threshold.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=4da86b9741190150c2dc01553cdaa618" data-og-width="1598" width="1598" data-og-height="1212" height="1212" data-path="images/messaging-platform/insights-manager/metric-highlight.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=598589b67e13869ff285111ef8d2b0c5 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=472d03804cb802781e03a95492c00a32 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=61518166b8c649bd9b6400684501ef00 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=3af1aeaf387eb214957614bf09dbef8d 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=da0c51d393ae9f98efcc670a272c2031 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/metric-highlight.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=dc5c3f4f8631ab1f6e50c1a36b96f4fd 2500w" />
</Frame>

Where metrics are highlighted:

1. **Conversation performance**: You can highlight both 'average handle time' and 'average response time'.
2. **Agent performance**: 'Time in status', 'average handle time', and 'average response time'.
3. **Queue performance**: You can highlight queue-level metrics within a single queue, queue groups, or on the Overview page.

## Event-based Alerts

Events are generated from actions taken by agents, customers or you.

Live Insights detects and records these events and displays them alongside conversation data, within the 'alert' column.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e8eae575ac6a12a0ffb7b1ffaea3faab" data-og-width="1698" width="1698" data-og-height="594" height="594" data-path="images/messaging-platform/insights-manager/event-based-alerts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a857e29fcdc5c7717c594f0f08ff074c 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=2db89ca270a368b5fd3fd29811f0d87d 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=66a2904939fdd00538e6c64707ded821 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=4058f135c4d1dd9203d262acd1c86545 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=100c9b5b62ce0747c2fb547d61975b59 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/event-based-alerts.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=66611e03058df58d633863489d28a20b 2500w" />
</Frame>

1. **Conversation events**: These events are related to a unique conversation. The events can be generated from agent actions or your actions.
   * **Customer transfers**: When an agent transfers a customer, Live Insights displays an alert next to the conversation.
   * **Whisper sent**: When you send a whisper message to an agent, Live Insights records and displays the event next to the conversation.
2. **Agent events**: These events impact the agent workload and help you contextualize agent performance. Live Insights displays the events for all targeted agents, within the Agent Performance panel.
   * **High effort**: Agents that are currently handling a high effort issue.
   * **Flex concurrency**: The agent is currently flexed and has a higher than normal utilization.

## High Queue Mitigation

ASAPP provides tools to enable workforce management groups to act fast when queues are or could be anomalously high.

**Tools Overview**

Live Insights can:

* Monitor queue volume for unusually high volume.
* Highlight 'Queued' metric based on severity level.
* Activate 'Custom High Wait Time' messaging and replace Estimated Wait Time messaging.
* Pause queues experiencing extremely high volume and prevent new queue assignments.

**Volume Thresholds:**

Live Insights highlights metrics when they reach past a threshold defined for the queue.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=4dc900225731f1b8311bce37e3eb82bc" data-og-width="1714" width="1714" data-og-height="1448" height="1448" data-path="images/messaging-platform/insights-manager/high-queue-mitigation-severity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=df71ee8e00b3ca1e1c5236cf8b4922aa 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=57aab75697af1708d59b520b9aa5d1a4 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a443d59dc03af920bb37f87e3605a6e4 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=87d935d2a0bb2ee4a2c93100af9bf1ae 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=b983daa18ff98187db974b0ffc9344b5 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-severity.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=84036dbd679fc21a5a4c3a805e02249f 2500w" />
</Frame>

1. **Low Severity:** detects abnormal activity and has moderate impact on the queue.
2. **High Severity**: detects highly abnormal activity. The queue is severely impacted.

**Mitigation Options:**

<table class="informaltable frame-void rules-rows">
  <tbody>
    <tr>
      <td class="td leftcol"><p><strong>Mitigation</strong></p></td>
      <td class="td leftcol"><p><strong>Severity Threshold</strong></p></td>
      <td class="td leftcol"><p><strong>Features available</strong></p></td>
    </tr>

    <tr>
      <td class="td leftcol">
        <p><strong>Default behavior</strong></p>
        <p>Business as usual. All queues are operating based on this setting.</p>
      </td>

      <td class="td leftcol"><p>None</p></td>

      <td class="td leftcol">
        <ul>
          <li><p>Estimated Wait Time messaging is active.</p></li>
          <li><p>Routing & assignment rules remain unchanged.</p></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td class="td leftcol">
        <p><strong>Custom High Wait Time Message</strong></p>
        <p>Low severity mitigation measure. Replaces Estimated Wait Time messaging.</p>
      </td>

      <td class="td leftcol"><p>Low Severity</p></td>

      <td class="td leftcol">
        <ul>
          <li><p>Estimated Wait Time messaging is replaced with a custom message.</p></li>
          <li><p>Routing & assignment rules remain unchanged.</p></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td class="td leftcol">
        <p><strong>Pausing the Queue</strong></p>
        <p>High severity mitigation measure. Prevents new assignments to the queue.</p>
      </td>

      <td class="td leftcol"><p>High Severity</p></td>

      <td class="td leftcol">
        <ul>
          <li><p>Estimated Wait Time messaging is replaced with a custom message alerting users the queue is currently closed due to high volume.</p></li>
          <li><p>Assignment to the queue is paused.</p></li>
          <li><p>Users currently in the queue remain in the queue.</p></li>
          <li><p>To time out users waiting in the queue, please contact ASAPP.</p></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Activate Mitigation

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7ba1d6856793160d9f4f64c95c2922c7" data-og-width="2732" width="2732" data-og-height="1216" height="1216" data-path="images/messaging-platform/insights-manager/high-queue-mitigation-activation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=cc0701d621a974307065d6aa562f627c 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=de7228786be0eb410243d5641c453b15 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7c53feddc218366358e27e32e680822a 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=ad961b6d4cb6e69846bca5a70a0c26ca 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=94b6ac589d6e41bb1c0959fa8d22cc8e 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-queue-mitigation-activation.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=4db1d98a6848e4c04b9d2eea65bbd886 2500w" />
</Frame>

1. **Mitigation menu options**: When available, Live Insights displays a menu on the relevant queue card in the Overview, as well as on the 'Performance' page of single queues and queue groups. To view those options, click the **menu** icon. The menu icon only displays when you highlight 'Queued'.
2. **Select mitigation**: Based on the severity level, Live Insights displays different mitigation options. Select an **option** to activate it. To remove the mitigation behavior, select **Default behavior**.
3. **Mitigation applied**: When you select a mitigation option, it is indicated on the queue card or on the Performance page.

## High Effort Issues

ASAPP supports a capability to enable agent focus for higher effort issues, while maintaining efficiency.

This feature dynamically adjusts how many concurrent issues an agent should handle while assigned a high effort issue.

### What is a High Effort Issue

ASAPP will route customers based on the expected effort of their issue. All issues, by default, will have an effort of 1.

Any issue with an effort value greater than 1 will be considered "high effort". Reach out to your ASAPP Implementation team to configure high effort rules for your program.

## Feature Definition

* **Slot**: A slot represents a space for a chat to be assigned to an agent. You can assign and configure multiple slots to a single agent via User Management.
* **Effort**: Effort represents what is needed from an agent to solve an issue. For each effort point assigned to an issue, an agent must have an equivalent number of available slots to be assigned that issue. ASAPP determines an issue's effort by its relevant customer attributes.
* **High Effort Time Threshold**: A threshold that sets how much time an agent can parallelize a high effort issue with other issues. You can configure this threshold per queue. This threshold represents the duration of all existing assignments an agent is handling when a high effort issue is next in line.
* **Flex Slot**: All agents have 1 additional slot that can be used if they are eligible to receive a flex assignment or if they are temporarily over-effort when handling a high effort issue.
* **Linear Utilization Level:** A type of Linear Utilization relative to the number of assignments an agent has assigned at a given time, regardless of the assignment workload state.
* **Assignment Workload**: A measure of Linear Workload relative to the number of active assignments an agent has assigned at a given time. An assignment is not considered active if it has caused an agent to become Flex Eligible.
* **Effort Workload**: A measure of Linear Workload relative to the issue effort of all active assignments an agent has assigned at a given time.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7bd57988405f150eeb4d97b673b42fb5" data-og-width="1928" width="1928" data-og-height="793" height="793" data-path="image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=ad0fdfdbca930107f892ef1e0a0d7311 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=61a1805912489d9376423a5fc62ff921 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=84813367c490731a449c842b729ff34f 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=bb44a45f3989fc5d1742c41b61344c58 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=adefe9153c0ed9c69dae9d9017a68cdb 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d9e0c484-6703-5c97-858a-13055e603ff6.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=845b622c95dc39f44743be4b40a47f5e 2500w" />
</Frame>

### How are high effort issues prioritized and assigned?

ASAPP assigns high effort chats in the order that they entered the queue. You can prioritize high effort chats higher in the queue using customer attributes. This prioritization is optional and not required. A configurable *high effort time threshold* allows each queue to set how much time an agent can parallelize a high effort issue with other assignments.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ee1a8550265f82ea5a34b1caa13fcdd9" data-og-width="1131" width="1131" data-og-height="735" height="735" data-path="image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=289e6880ee6b7e163fb72d0ba01fa2fd 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=bf82687ec5961d54f0faf8d70fac8b43 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b416c606bf989aaff374f39de5e2f1f4 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=93bd831d6447c368375e758ffde6e8c9 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f497dd5b08fa20b55fd013dae908a879 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aea93058-21b5-38be-9a3c-5cb4dc3871cd.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7b7b0b4cda7fa7c27713bf4c8b25906f 2500w" />
</Frame>

### How are high effort issues assigned against other issues?

ASAPP assigns high effort issues in order of configured priority and when they entered the queue. An agent will receive a high effort assignment if they meet at least 1 of the following criteria:

* An agent has 0 active assignments.
* An agent has sufficient open slots to receive a high effort assignment.
* The **high effort time threshold** has elapsed for all of an agent's current assignments and the high effort chat's effort would not extend the agent's Effort Workload past their Flex Slot.

### How do high effort issues impact performance?

* High effort issues will not change current behavior for Queue Priority.
* High effort issues will not change current behavior for Flex Eligibility or Flex Protect.
* High effort issues take longer to assign because they have to wait for an agent to have sufficient effort capacity.
* If a set of queues has 50% or more agents in common, then a high effort issue at the front of one queue will hold the issues in the other "shared" queues until it is assigned.

### How do I monitor the impact of high effort issues?

You can view the 'Queued - High Effort' metric in Live Insights on queue detail pages. This metric captures the number of high effort issues currently waiting in the queue. If a high effort issue is first in queue and slows other issues from being assigned, Live Insights displays an alert on this metric. These changes will also be visible for programs that do not have high effort rules configured.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e93d1916fa586a75c52b60d5e09a95ad" data-og-width="2344" width="2344" data-og-height="1008" height="1008" data-path="images/messaging-platform/insights-manager/high-effort-states.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=5c8fb5b8e94cb7bac1ddd3b0eac6897e 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=bb6d62e55a48057f21ca690783b27608 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=3848a543cd69da5ff8f19368bca54fff 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=805922ead159108e77a6ab96629e8c57 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=fcb15a1d641ee7db42e1bf7ea273a947 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-states.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e32da90b47681043d1c2f97e3b520059 2500w" />
</Frame>

### How can I tell which agents are handling high effort issues?

In the Agent Right Rail, you can monitor which agents are currently handling high effort issues. ASAPP displays an icon next to the agent's utilization indicating a high effort issue is assigned. These changes will also be visible for programs that do not have high effort rules configured.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=85225dc11c642b159d064ce7b58ec78f" data-og-width="2344" width="2344" data-og-height="1008" height="1008" data-path="images/messaging-platform/insights-manager/high-effort-agent-states.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=b91ab04d32790f2a6ef9479e561173a8 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=369295dc94b9fe098615e2ca7957931b 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=b743aed0f1ba4e3f3bff37535be16b98 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=eb28564680814de4e304bdfe535f62f6 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=3e6f115cd141d691784b8eb87fc5be12 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/high-effort-agent-states.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=d6cd8dfaef48b03585b7afb7f1f50b18 2500w" />
</Frame>
