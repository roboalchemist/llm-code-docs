# Source: https://docs.avaamo.com/user-guide/live-agent-console/supervisor/live-sessions.md

# Live sessions

Live Sessions enable supervisors to monitor real-time information on the customer wait time and conversation duration of all the active and queued chat requests within the company. This provides valuable insights into traffic patterns and workload, allowing them to optimize chat routing and create specialized teams with specific skill sets, ultimately enhancing customer satisfaction.

For instance, Supervisors can leverage the traffic data to develop standardized responses or establish and manage routing rules. In the following example, Supervisors can assess the current traffic usage, including metrics such as wait time, and make informed decisions to update routing rules or explore alternative methods to enhance the overall customer experience. See [Advanced Configurations](https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F621YgOB3lLXE13M66718%2Fimage.png?alt=media&#x26;token=d676ccbb-78fa-4dab-9f34-ca29ba94d92b" alt=""><figcaption></figcaption></figure>

Some of the key benefits of the Live Sessions page include the following but not limited to:

* **Resource Allocation**: Supervisors can use the timer to allocate resources effectively. They can adjust agent workloads using certain advanced configurations based on the time spent on each conversation. See [Advanced configurations](https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations), for more information.
* **Agent Performance Evaluation**: The timer can be used to assess agent performance. If an agent consistently takes longer to resolve issues than their peers, it may signal a need for additional training or support.
* **Queuing and Routing**: The timer can also help in queuing and routing decisions. If a chat is taking too long, supervisors can use routing rules and make adjustments in the queue to reduce wait times. See [Rule-based routing](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing), for more information.

{% hint style="success" %}
**Key Point**: If you require to access historical data of Live Agent chat interactions for analytical or reporting purposes rather than real-time information, then see [Reports](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/reports) page for detailed information and insights.
{% endhint %}

### View real-time data

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Analytics and Reporting icon -> Live Sessions` page in the left navigation pane of the Supervisor interface to view real-time live agent reports in your organization.
* By default, in the **Live Sessions** page, all the queued requests are displayed first, followed by the active requests:
  * Within queued requests, the requests are displayed in the descending order of wait time which implies that the request with the maximum wait time is displayed first.&#x20;
  * Within active requests, the requests are displayed in the descending order of conversation duration which implies that the request with the maximum conversation duration is displayed first.&#x20;
  * Note only active and queued conversations are displayed in the **Live Sessions** page.&#x20;
* Each row is a chat request by the user and in the `Live Sessions` page, you can view the following details about each chat conversation:
  * **Conversations status**: Indicates the current status of the conversation.
    * **Queued**: The conversation that is yet to be accepted by a live agent.
    * **Active**: The ongoing conversation between live agent and user.
  * **User name**: Indicates the end user with whom the live agent is/was interacting.
  * **Live agent name**: Indicates the name of the live agent conversing with the user.
  * **Wait time**: Indicates the time the request was in the queue before a live agent accepted the request.&#x20;
    * The **Live Sessions** page displays real-time information on the customer wait time for each chat, which is kept updated every second.
    * The wait time becomes static when a live agent accepts a chat and starts chatting with the user.&#x20;
    * When the request is transferred to another team, the wait time is reset with a new entry in the `Live Sessions` page, and the original conversation status is marked as ended. Note that you can view only queued and active conversations on the page.
  * **Conversation duration**: Indicates the amount of time the current live agent is/was having a conversation with the user until the chat is terminated or transferred by the live agent to another team.
    * The **Live Sessions** page displays real-time information on the conversation duration for each chat, which is kept updated every second.
    * When the request is transferred to another team, the conversation duration is reset with a new entry in the `Live Sessions` page and the original conversation status is marked as ended.&#x20;
    * The page displays live, real-time information on conversation durations, continuously updating every second.
  * **Channel**: Indicates the channel used by the user to converse with a live agent.
  * **Team**: Indicates the team the request was routed to.
  * **Agent**: Indicates the agent (bot) name.
* Click the **Refresh** button to view the latest real-time status of the conversations in your organization.

### Refresh notifications

When the **Live Sessions** page remains open in a browser tab, Supervisors receive a browser tab refresh notification for any new chat requests received or updates to the conversation status for the existing chat requests.

In the **Live Session** page, a refresh notification is displayed, enabling supervisors to refresh the page as needed.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZhVBm6qYnNxYnAtUVL6y%2Fimage.png?alt=media&#x26;token=c6c74927-b756-4d4f-8b91-ef53f1572eae" alt=""><figcaption></figcaption></figure>
