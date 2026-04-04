# Source: https://docs.avaamo.com/user-guide/live-agent-console/live-agent/set-live-agent-status.md

# Set live agent status

The Live agent console allows live agents to set the status as Online, Offline, or Away based on their availability.&#x20;

* **Online**: Indicates that the agent is actively logged into the system and available to handle customer inquiries or requests. When an agent is marked as "Online," it means they are ready and able to engage with customers and provide assistance in real time.
* **Offline**: Indicates that the agent is not actively logged into the live agent system or is completely unavailable. When an agent is marked as "Offline," it indicates that they are not currently accessible for customer inquiries or any other live agent activities.&#x20;
* **Away**: Indicates that the live agent is temporarily unavailable to handle customer inquiries or requests. When an agent sets their status to "Away," it typically indicates that they are not actively engaging with customers at that moment but are still logged into the live agent system. The "Away" status suggests that the agent may return to active duty soon or periodically check for customer inquiries.

{% hint style="info" %}
**Notes**:

* Supervisors can monitor and track live agent status in real-time and this helps supervisors to effectively adjust the configurations for better customer experience. For example, if an agent is marked as "away" or "offline", supervisors can adjust the configurations to bypass that agent and direct the request to an available agent, reducing wait times and improving efficiency. See [Advanced Configurations](https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations), for more information.
* Additionally, supervisors can override the live agent status, allowing them to address situations where a live agent may not be available, such as being on sick leave, but has not updated their status accordingly. See [Change live agent status](https://docs.avaamo.com/user-guide/supervisor/live-agents#change-live-agent-status), for more information.
  {% endhint %}

### **Set the live agent status**

* Click `Settings -> Avaamo Live agent` in the Avaamo dashboard home page to view the Live agent console
* In the `Live agent console`, click the status dropdown at the top-right corner.&#x20;
* Set the status as offline, online, or away as required. Note that it is the responsibility of the live agents to set the status appropriately based on their availability, although a supervisor can override the live agent status if required.
  * Only active live agents can start chatting with the users. Before starting the conversation with the user, the live agents must change the status to `Active`. See [Set live agent status](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/set-live-agent-status), for more information.
  * A live agent with any status can transfer the request to another team. See [Transfer to another team](https://docs.avaamo.com/user-guide/live-agent-console/transfer-to-another-team#at-the-time-of-accepting-the-chat), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfRMqRPCqZkjMzUcbAoac%2FScreenshot%202023-07-24%20at%206.46.23%20PM.png?alt=media&#x26;token=3a1927ca-218c-429a-8137-f31969f48611" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**:  When a live agent marks the status as offline or away, it is the responsibility of the agent to conclude all the active conversations.&#x20;
{% endhint %}
