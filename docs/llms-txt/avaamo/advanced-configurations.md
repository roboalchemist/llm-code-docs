# Source: https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations.md

# Advanced Configurations

This article describes the following advanced configurations of the live agent system:

* **Auto-accept**: Ability to automatically assign the incoming live agent requests to the active live agents without the need for any manual intervention by the live agent. See [Auto-accept](#auto-accept), for more information.
* **Concurrent assignment:** Ability to automatically assign multiple live agent requests to the same agent simultaneously. Instead of handling one request at a time, live agents can handle multiple inquiries concurrently. See [Concurrent assignment](#concurrent-assignment), for more information.
* **Round-robin assignment:** Ability to automatically distribute the live agent requests among available active live agents based on the online start time and current load without any manual intervention. See [Round-robin assignment](#round-robin-assignment), for more information.

{% hint style="info" %}
**Note**: These features are enabled and configured only on demand. Contact Avaamo Support, with your use case to further enable this feature. See [Before you begin](#before-you-begin), for more information.
{% endhint %}

### How do these configurations help?

All three advanced configuration features -> auto-accept, concurrent assignment, and round-robin goes hand-in-hand. The following are a few points that list the benefits of enabling these configurations in your organization:

* **Efficiency and Speed**: Speeds up the process as it minimizes the hops required to start chatting with the user, reducing the wait times and improving efficiency.
* **Workload Balancing**: Helps distribute the workload evenly among available agents. This improves overall agent productivity and prevents bottlenecks in the support workflow.&#x20;
* **Improved Agent Utilization**: Maximizes agent utilization by ensuring that available agents are continuously engaged in addressing customer inquiries. It minimizes idle time and keeps agents productive, leading to better resource utilization within the customer support organization.
* **Scalability and Flexibility**: Useful in high-volume customer support environments or during peak periods when the influx of inquiries is significant. The feature enables the system to scale and handle large volumes of inquiries efficiently.&#x20;

### Before you begin

Based on your organization's live agent structure, policy, and your requirement, you must provide the following details in the request to Avaamo Support which helps in configuring the advanced live agent configuration features for your account:

* If you wish to enable the auto accept feature for your account or not. See [Auto-accept](#auto-accept), for more information.
* The number of concurrent requests that can be assigned to the live agents by the system automatically when auto-accept is enabled.

### Auto-accept

Auto-accept refers to the ability to assign incoming live agent requests to active live agents without the need for any manual intervention by the live agent. This allows the live agents to start chatting with the users right away without the need to accept the chat first.&#x20;

With reference to the Avaamo live agent system, this implies that the live agent requests are automatically moved to the `Active conversation` list, instead of the `Queued conversation` list, where it is required for the live agents to manually check the requests from the `Queued conversation` list and accept the chat before starting a conversation with the users.

Auto-accept works with concurrent assignments and round-robin assignments.&#x20;

* The number of concurrent requests a live agent can be assigned at a time in the  `Active conversation` list is defined via concurrency. See [Concurrent assignment](#concurrent-assignment), for more information.
* Concurrency assignment is governed by the round-robin rule that defines how the requests are moved from the `Queued conversation` list to the `Active conversation` list. See [Round-robin assignment](#round-robin-assignment), for more information.

{% hint style="info" %}
**Notes**: When auto-accept is enabled,&#x20;

* Live agents can manually accept chats from the available queued conversation, even if the maximum limit of concurrent chats has been reached.
* When the chat is manually accepted by the live agent from the queued conversations, the preview of the chat conversations with `Start Chatting` and `Transfer to another team` option is not displayed.&#x20;
* Live agents can transfer to another team only after accepting the chat. See [Transfer to another team](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/transfer-to-another-team), for more information.&#x20;
  {% endhint %}

### Concurrent assignment

Concurrent assignment refers to the ability to automatically assign multiple live agent requests to the same agent simultaneously. Instead of handling one request at a time, agents can handle multiple live agent requests concurrently.

{% hint style="info" %}
**Notes**:&#x20;

* Ensure that auto-accept is enabled for your account.&#x20;
* Concurrency can be defined only at the account level and it is applicable to all the live agents in the account.
* By default, the Avaamo live agent console is set up to handle a maximum of 200 concurrent live agents with a maximum of 10 concurrent chats for each live agent. These settings are configurable based on the business requirement. Contact Avaamo Support, for further assistance.
  {% endhint %}

In the Avaamo live agent system, this implies that the live agent requests are automatically moved to the `Active conversation` list until the concurrency count is reached, instead of the `Queued conversation` list, where it is required for the live agents to manually check the requests from the `Queued conversation` list and accept the chat before starting a conversation with the users.

* Once the concurrency count is reached, the new live agent requests are displayed in the `Queued conversation` list.&#x20;
* As and when the live agents close the active conversations, the live agent requests from the  `Queued conversation` list are moved to the `Active conversation`  list until the concurrency count is reached and as per the round-robin assignment. See [Round-robin assignment](#round-robin-assignment), for more information.

### Round-robin assignment

Round-robin assignment refers to the ability to automatically distribute the live agent requests among available active live agents based on their online start time and current load without any manual intervention.&#x20;

* Requests are assigned to the live agents in the order of online start time. The live agent coming online first receives the first request.
* Subsequent requests are assigned to the live agents with the least load until the concurrency count is reached. See [Concurrent assignment](#concurrent-assignment), for more information. &#x20;
* Live agents can view all the assigned requests in the `Active Conversation` list.&#x20;

### Example 1: Concurrency count is 2 with 2 live agents

* Live agent A -> Came online first, No requests in the Queue or in the Active Conversation List.
* Live agent B -> Came online next, No requests in the Queue or in the Active Conversation List.

| Action                  | Live agent A | Live agent B |
| ----------------------- | ------------ | ------------ |
| New request (1)         | Request (1)  |              |
| New request (2)         |              | Request (2)  |
| New request (3)         | Request (3)  |              |
| Live agent A closes (1) |              |              |
| New request (4)         |              | Request (4)  |
| New request (5)         | Request (5)  |              |

Here, you can observe that when there is a new live agent request `New request (4)`, the system assigns the request to `Live agent B` instead of `Live agent A`, since at that point, `Live agent B` had the least load.

### Example 2: Concurrency count is 2 with 3 live agents

* Live agent A -> Came online first, No requests in the Queue or in the Active Conversation List.
* Live agent B -> Came online next, No requests in the Queue or in the Active Conversation List.
* Live agent C -> Came online last, No requests in the Queue or in the Active Conversation List.

<table><thead><tr><th width="181">Action</th><th width="225">Live agent A</th><th width="177">Live agent B</th><th>Live agent C</th></tr></thead><tbody><tr><td>New request (1)</td><td>Request (1)</td><td></td><td></td></tr><tr><td>New request (2)</td><td></td><td>Request (2)</td><td></td></tr><tr><td>New request (3)</td><td></td><td></td><td>Request (3)</td></tr><tr><td>New request (4)</td><td>Request (4)</td><td></td><td></td></tr><tr><td>New request (5)</td><td></td><td>Request (5)</td><td></td></tr><tr><td>Live agent A closes (1)</td><td></td><td></td><td></td></tr><tr><td>Live agent B closes (2)</td><td></td><td></td><td></td></tr><tr><td>New request (6)</td><td></td><td></td><td>Request (6)</td></tr></tbody></table>

Here, you can observe that when there is a new live agent request `New request (6)`, the system assigns the request to `Live agent C` instead of `Live agent A or B`, since at that point, `Live agent C` had the least load.
