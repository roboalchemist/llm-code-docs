# Source: https://docs.avaamo.com/user-guide/how-to/agent-console.md

# Agent Console

Avaamo platform supports integration with a **live agent** for scenarios, where there is a need for human intervention. If the user requests or if the agent senses dissatisfaction, frustration, anger, or if the agent has defined intents for transfer, it seamlessly transfers the conversation to a human agent system such as Avaamo Live Agent Or Zendesk. **Agent Console** is an interface of Avaamo live agent console for live agent interaction with users.&#x20;

See [Switch to live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent), for more information.

## **Access Agent Console**

{% hint style="info" %}
**Notes**:&#x20;

* This option is available only for users with the **Live agent** or **Admin** role. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

* Currently, the Agent console is certified on the latest version of the Chrome browser.

* Currently, each conversation with a live agent starts as a fresh chat, and hence the conversation history of the previous live agent chat is not available in the Agent Console.&#x20;

* Avaamo platform offers a new and enhanced Live agent console which is designed to enhance engagement and facilitate efficient workflow management for live agents during customer interactions. This is enabled only on demand. Contact Avaamo support, for further assistance. See [Live agent console](https://docs.avaamo.com/user-guide/live-agent-console/overview), for more information.
  {% endhint %}

* In the Avaamo Platform Dashboard, right-click on the user name available at the top-right corner and click the **Agent Console** option.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QSTp_0vmWcZBNtx2d%2F-M-QT0oS-dc9UngClzFb%2Fagent-console.png?alt=media\&token=21fbe3b0-74e6-4444-8efa-47eac3ac9aa6)

* The **Agent Console** page is opened in a new tab. This is the console used for Avaamo live agent interaction with users.&#x20;
* When a live agent chat is initiated, a new request is available in the Agent Console with a notification sound.&#x20;

{% hint style="success" %}
**Key Point**: Ensure that you have allowed notifications in your browser settings to receive the notification sound.
{% endhint %}

* Click the request to start a live agent conversation with the user. You can view the user details and the IP address from where the request is initiated. See [Masking IP address in Agent Console](#masking-ip-address-in-agent-console), for more information on how to mask the IP address in the Agent Console for security reasons.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MSafVlJkoZgZVcyGeaa%2F-MSaguYlxn5nKWJh2maM%2F5.6-agent-console-accept.png?alt=media\&token=469c1eef-d036-4045-8afd-6473c6a05968)

* Click **Accept** to start the conversation with the user. By default, the last 30 messages between the agent and the user is sent to the live agent. This helps the live agent understand the context of the conversation better for responding to user queries. As you continue the conversation with the user, the text that you enter in the Agent Console is displayed to the user in the agent widget and vice-versa, thus facilitating a two-way communication:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MSb3I1SAgKDtK6oHz3W%2F-MSb6BQvwseSKFJuNRKV%2F5.6-agent-console-conversation.png?alt=media\&token=76e26046-fa64-4ca1-a355-84688471e586)

{% hint style="info" %}
**Note**: After you accept the chat request, you can also view the details of the user who initiated the request by clicking the User profile icon in the top-right corner
{% endhint %}

* When a user terminates a chat or ends chat with a live agent, the following notification is received in the Live agent console that the chat is terminated:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MSky79SzHFdIg7MVbd3%2F-MSl4eCk8kO9ZExvu3Wj%2FScreenshot%202021-02-05%20at%2012.33.43%20PM.png?alt=media\&token=bcb53c67-f363-476a-b7fe-647cc069d5c0)

## Masking location IP address in Agent Console

You can mask the location IP address in the Agent Console [for a specific agent](#at-the-agent-level). When masking is enabled, you cannot view the location IP address from where the request is initiated, as the location IP address is masked in the Live agent console.&#x20;

The following illustration depicts how the location IP address is masked in the Accept chat request pop-up:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTA4_ZmJLlyv05-5_AX%2F-MTA7N84uvclp782zfsd%2F5.6.0-rn-masking-new_censored.jpg?alt=media\&token=c15f79c0-21eb-4a3e-9b92-e6eaccbdb757)

The following illustration depicts how the location IP address is masked in the User profile:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTA4_ZmJLlyv05-5_AX%2F-MTA82zN672v4qOz3fc0%2F5.6.-masking-user-profile_censored.jpg?alt=media\&token=8921b57e-8ac6-40fe-954d-63155187b94f)

### **At the agent level**

IP address masking is enabled by default for all agents created after the 9.0.0 release. If you wish to enable IP address masking for an agent created prior, you can contact Avaamo Support to request activation for that specific agent. See [How to mask the location IP address in Agent Console?](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#10-how-to-mask-the-location-ip-address-in-agent-console), for more information.
