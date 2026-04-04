# Source: https://docs.avaamo.com/user-guide/live-agent-console/live-agent/accept-and-start-chat.md

# Accept and start chat

When a user sends a live agent request, the request is sent to the `Queued conversation` list of all the live agents irrespective of the live agent status.  Live agents can accept and start chatting by picking the requests from the `Queued conversation` list in the `Live agent console`.&#x20;

{% hint style="info" %}
**Note:**  Certain advanced configurations such as auto-accept provide the ability to assign the incoming live agent automatically requests to the active live agents without the need to accept the chat by the live agent. In such cases, live agents can directly move to [Step 3: Continue chatting or Transfer to another team](#step-3-continue-chatting-or-transfer-to-another-team). See [Advanced Configurations](https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations), for more information.
{% endhint %}

{% hint style="success" %}
**Key point**: The live agent console provides proactive notifications for incoming chat requests. If live agents have minimized the web browser or if the currently active browser tab is not the live agent console, then a browser tab notification is displayed to alert live agents about new chat requests.
{% endhint %}

### Step 1: Accept chat

{% hint style="info" %}
**Note**: Live agents must be `Active` to accept the chat requests. See [Set live agent status](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/set-live-agent-status), for more information.
{% endhint %}

* Click `Settings -> Avaamo Live agent` in the Avaamo dashboard home page to view the Live agent console.
* Live agents can start conversations with the customers by accepting the chat from the Queued conversation list in the `Live agent console`.&#x20;
* Click **Accept** to start chatting.&#x20;

### Step 2: Start chatting or Transfer to another team

When a live agent picks a chat from the live agent queue by clicking the `Accept` button,&#x20;

* A preview of the entire conversation history is displayed in a pop-up. Scroll to view the complete conversation history.&#x20;
* Any additional user information captured earlier before transferring to a live agent is also displayed. Live agents can use these details to personalize their interactions with users. See [View user information](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/view-user-information), for more details.

Based on this conversation, the live agents can determine whether the request must be transferred to another team even before engaging with the customer. See [Transfer to another team](https://docs.avaamo.com/user-guide/live-agent-console/transfer-to-another-team#at-the-time-of-accepting-the-chat), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7gWgRnMwqNskmqcJw94k%2Fimage.png?alt=media&#x26;token=18eeb015-d2bb-49df-9d28-5a67ee78e0ca" alt=""><figcaption></figcaption></figure>

Alternatively, if the live agent decides to continue chatting, they can click the`Start chatting` button, to start conversing with the customer. When a live agent starts chatting, the chat request moves from the `Queued conversation` list to the `Active conversation` list. A live agent can have multiple active conversations at a time based on the current requirement.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* Only active live agents can start chatting with the users. Before starting the conversation with the user, the live agents must change the status to `Active`. See [Set live agent status](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/set-live-agent-status), for more information.&#x20;
* A live agent with any status can transfer the request to another team. See [Transfer to another team](https://docs.avaamo.com/user-guide/live-agent-console/transfer-to-another-team#at-the-time-of-accepting-the-chat), for more information.
  {% endhint %}

### Step 3: Continue chatting or Transfer to another team

When a live agent continues chatting with the customer, they also view the complete conversation history which can further set the context and help in having better conversations with the customers.

* Scroll in the Message area to view the complete conversation history. All the messages prior to the system message `Transferred to Live Agent` is where the conversation history is available.
* Type any message in the Message box and press enter or the arrow button to send it to the user.
* If a live agent persona is configured, then the live agent persona image is displayed for live agent messages. This helps the user can identify the conversation with the live agent. See [Live agent persona](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#live-agent-avatar), for more information.
* The ongoing conversation of the live agent with the user is displayed in the area after the system message `Transferred to Live Agent`&#x20;

During the chat, live agents have the option to utilize pre-written responses, also known as `Quick responses`, or rephrase them in order to provide improved and precise responses that contribute to an enhanced customer experience.

A live agent can access the set of all the quick responses just by typing # in the message text box. See [Use quick responses](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/use-quick-responses), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FyVKmWoLmEgEG2We0fsAn%2Fimage.png?alt=media&#x26;token=20831532-3e9b-4c51-a104-902c9424e96c" alt=""><figcaption></figcaption></figure>

In certain situations, a live agent may initiate a chat with a customer and subsequently realize that there is another team better suited to assist with the specific query. In such instances, the live agent can utilize the `Transfer` icon located next to the chat message box to initiate a transfer to another team. &#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Flfn45GUzlO3Stk5Oeukx%2Fimage.png?alt=media&#x26;token=2447a9c3-3ad3-4237-9dbb-be5a7f5841a9" alt=""><figcaption></figcaption></figure>

See [Transfer to another team](https://docs.avaamo.com/user-guide/live-agent-console/transfer-to-another-team#at-the-time-of-accepting-the-chat), for more information.

### Step 4: End chat

Live agent chat can be either ended by the users or by the live agent themselves. Live agents can click `End chat` at the top of the current message window to end current conversations with the agent.

When a chat is terminated by the user or by a live agent,

* A toast message is displayed to the live agent with the user who is terminating the chat
* The terminated chat is indicated by a red background in the `Active conversation` list of the live agents and it remains as-is. Click the close conversation icon to remove the chat from the list.
* A new transfer request by the same user is a fresh new request now and gets appended in the Queued conversation list.&#x20;
* Live agents cannot send messages back to the users after the chat is terminated, however, the live agents can still view the complete conversation history.
