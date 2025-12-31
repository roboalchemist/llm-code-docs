# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent.md

# Pre-built live agent

Avaamo platform supports integration with a **live agent** for scenarios when there is a need for human intervention. If the user requests or if the agent senses dissatisfaction, frustration, anger, or if the agent has defined intents for transfer, it seamlessly transfers the conversation to a human agent system such as Live Agent Or Zendesk.

{% hint style="info" %}
**Notes**:&#x20;

* You can set up different rules for transferring a conversation to a live agent in the Avaamo platform. See[ Live agent transfer rules](#live-agent-transfer-rules), for more information.
* Currently, you cannot [transfer to a live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent) that is configured in the Avaamo Platform from the C-IVR channel. Instead, it is recommended that you use [Call forward](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#call-forward) for connecting to live agents.
  {% endhint %}

Avaamo Platform provides pre-built live agent integration with **Avaamo, Oracle Right Now, and Zendesk**. You can also configure your own custom live agent. See[ Custom live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/custom-live-agent), for more information.

### Configure live agent

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can configure a live agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

**To configure a live agent**:

* In the **Agent** page, navigate to the **Configure -> Live agent** option in the left navigation menu.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FqGPlaDge7PLFMQ4CvV5A%2F6.3-live-agent-configure.png?alt=media&#x26;token=f8fc3b47-215c-4b62-8ebc-ac3dcd822057" alt=""><figcaption></figcaption></figure>

* Move the slider **Live agent system** to **Enabled** to use this feature.
* **Save conversations**:&#x20;

To ensure compliance with data privacy regulations such as PII, PHI, and GDPR, the Avaamo Conversational AI system now includes a **Save Conversations** toggle. This feature provides administrators with granular control over whether live agent interactions are stored within the system

Using this toggle button, you can choose not to record live agent interactions in the agent conversation history. By default, the Save conversations toggle button is enabled, which implies that live agent conversations between users and live agents are saved in the conversation history. This option helps to protect users' sensitive data in live agent conversations.&#x20;

{% hint style="success" %}
**Key points**:

* Avaamo Conversational AI platform has always been GDPR compliant. Information masking can be used to protect PII/PHI/GDPR compliance data. See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more information.&#x20;

* This applies only to all the live agent conversations saved in the Avaamo platform. The live agent conversation data in the external live agent systems such as Oracle, Zendesk, or any custom live agents must be handled separately by the respective systems according to the business requirements.

* If the **Save conversations** toggle is set to **No**, then no data or chat conversations between the users and live agents are saved in the Avaamo platform. At the specific section in the Conversation history page, a system message indicating the same is displayed. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-conversation-history), for more information.
  {% endhint %}

* In the **Select a live agent system** dropdown, you can select one of the following live agent systems:
  * **Avaamo**: No configuration required.
  * **Oracle Right Now**: Configure using UserName, Password, and Site Name details provided by Oracle Right Now.&#x20;
  * **Zendesk**: Configure using the Chat Account Key provided by Zendesk. See [Zendesk integration](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent/zendesk-integration), for more information.
  * **Custom**: Configure your own custom live agent. See[ Custom live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/custom-live-agent), for more information.

### Live agent avatar

You can add a unique live agent avatar in the **Configuration -> Live agent** page. This feature helps:&#x20;

* Users to easily distinguish a real virtual agent from a virtual assistant.&#x20;
* Developers to abide by the privacy regulations of an organization as in certain organizations there can be a legal requirement to have a different avatar for a real virtual agent versus a virtual assistant.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fgziuays3tfGyUoiVz2Sj%2F6.3-live-agent-avatar.png?alt=media&#x26;token=08a90b12-1239-46fe-b2d7-72ead94b2820" alt=""><figcaption></figcaption></figure>

**To configure a live agent avatar**:

* Move the slider **Live agent persona** to **Enabled**.
* Click **Upload image** to upload a unique live agent avatar.&#x20;
  * Recommended image types: PNG, JPEG
  * Recommended image size: 200px \* 200px
* Provide a unique live agent name so that the user can identify the conversation with the live agent. The live agent name is displayed in the agent chat widget for all the themes except the **Messenger** theme. See [Agent theme](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#agent-theme), for more information.
* Click **Save** to save the live agent configuration changes.

The following is an illustration where you can view the live agent avatar when a user initiates chat with a live agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZWuDW43dEyD8kYkNUg4f%2F6.3-live-agent-avatar-chat.png?alt=media\&token=712b357d-9040-4d08-a8f6-ddf26b840123)

The following is an illustration where you can view the live agent avatar and live agent name when a user initiates a chat with a live agent. Note that the theme used here for the agent is the [Orange theme](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#agent-theme).

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHQTVKLfiWMCiozYo9hNx%2F6.3-live-agent-name-avatar.png?alt=media\&token=66c58348-bebf-49bc-8d59-4a1c56581858)

### Automated messages

You can configure automated messages for the agent to display during the transfer process:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q08-P4Si-pXXM-h21%2F-M-Q13m7TPB8G0UrYmBf%2Fagent-live-agent-messages.png?alt=media&#x26;token=7e1aaf4e-1f2e-46b7-9f81-3076851c12aa" alt=""></div>

* &#x20;**Switch to agent:** Enter a message to inform the user that the conversation is transferred to a live agent. You can also configure different responses in the messages such as text, card, carousel. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.

```
Example: I am now re-directing you to a live agent, who will be with you shortly.
```

* **Waiting message:** Enter a message that is displayed when the agent has not responded after a specified time. Use this message to acknowledge the user's patience and inform them of the wait duration. Currently, you can configure only simple text messages in the response.

```
Example: Sorry for the delay, an agent will assist you shortly.
```

* **Time-out message:** Enter a message that is displayed when there are no agents available even after the specified time. Use this message to inform the user of the unsuccessful transfer to a live agent. Currently, you can configure only simple text messages in the response.

```
Example:  I am sorry, there are no available agents to assist you right now. 
Please try again later.
```

* **Agent terminated chat:** Enter a message that is displayed after an agent terminates the conversation. Use this message to inform the user, the end of the conversation from the live agent. Currently, you can configure only simple text messages in the response.

```
Example: Agent has terminated the conversation.
```

* **Switch to agent message:**  Specify a message that is displayed when a user returns to the agent from live agent mode. You can also configure different responses in the messages such as text, card, carousel. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.

```
Example: I am still available to respond to your queries.
```

### Live agent transfer rules

You can configure a few specific rules for the agent to transfer the conversation to a live agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q08-P4Si-pXXM-h21%2F-M-Q1i96cN2QuN4NtEpZ%2Fagent-live-agent-transfer-rules.png?alt=media\&token=5e930ba3-f963-4acf-89db-71c84f38a4cb)

* **Intents to match:** You can add the intents that the agent can match with the user query and transfer the conversation. These intents must be defined in the agent.
* **Silent switch**: You can select the checkbox for the silent switch, for the agent to transfer the conversation without any automated messages. You can also specify a message that is displayed in the agent when transferring to a live agent.
* **Switch to live agent for unhandled queries:** You can program the agent to transfer the conversation for unhandled queries:
  * Select the checkbox for the number of unhandled queries the agent will process before making the transfer.
  * Select the checkbox for the user query message length, for the agent to make the transfer.
  * Select the checkbox for the silent switch, for the agent to transfer the conversation without any automated messages.

### Working hours

You select the checkbox for working hours so that the agent transfers the conversation only during the specified period. In the **Working Hours** section, you can specify the following details:&#x20;

* **Time zone** of working hours
* **From** and **To** time of working hours
* **Weekly holidays**. Note that during weekly holidays, the agent does not transfer the conversation to a live agent.
* **Unavailable message**: Enter the message that is displayed when a request to transfer to a live agent is after working hours. Use this message to indicate the unavailability and the working hours to the user.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q08-P4Si-pXXM-h21%2F-M-Q2eCN_fGn_9o2ZL6-%2Fagent-live-transfer-working-hours.png?alt=media&#x26;token=9c13dccf-f195-46b4-b8e0-8d4f67cf24f0" alt=""></div>

If you cannot specify the proper working hours using the options provided, then you can also specify a custom Javascript to handle the working hours by enabling **Custom working hours handler.** The following is a sample JS for defining custom working hours:

```javascript
var currentTime = moment();
var startTime = moment('08:30', "HH:mm");
var endTime = moment('18:00', "HH:mm");
var weekendEndTime = moment('09:30', "HH:mm");
var todayDate = moment().format("MM DD");
var HoliDay = moment('05 01').format("MM DD"); //.toString()
if (todayDate != HoliDay) { // Developers can define custom holiday(s)
    console.log("todayDate" + todayDate);
    if (moment().weekday() <= 5) {
        // moment().weekday() will give output as 1 to 7 , where 1 Refers to Monday and so on 
        if (currentTime.isBetween(startTime, endTime)) { // checking the working hours on daily working day basis
            console.log(" Agent is available. It is a weekday. "); 
            return true;
        } else {
            console.log(" Agent is not available "); 
            return false;
        }
    } else if (moment().weekday() <= 6) { // '6' refers to saturday 
        if (currentTime.isBetween(startTime, weekendEndTime)) {
           console.log(" Agent is available. It is a weekend. "); 
           return true;
        } else {
           console.log(" Agent is not available "); 
           return false;
        }
    } else {
        console.log(" Agent is not available "); 
       return false;
    }
} 
else {
   console.log(" Today is a holiday. Agent is not available "); 
   return false;
}
```

You must return true or false from the Custom working hours handler:

* When you return true, it implies that the agent is available and the automated messages as configured for the agent availability is displayed. See [Automated messages](#automated-messages), for more information.
* When you return false, it implies that the agent is unavailable and the message as configured in "Unavailable message" is displayed.

{% hint style="info" %}
**Note**: You can also transfer to a live agent in JS using Agent.transfer() method. See [Agent.transfer](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.transfer), for more information. When you are using Agent.transfer() in JS node to transfer to a live agent, then

* It gives you enhanced control of when to transfer to a live agent and what must be done once the transfer is completed.&#x20;
* Since it gives you more flexibility, you can set conditions required before transferring to a live agent in the JS itself. If any working hours is required before transferring to a live agent, it must be handled within the JS code itself before using Agent.transfer(). Hence, working hours set in the Live agent page is no longer applicable.
  {% endhint %}

### Callbacks

You can program the live agent system to give users options to execute scripts before the transfer of the conversation, time-out, and agent termination.&#x20;

You can use [Agent.setContext ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.setcontext)to set live agent context based on the user properties which can be used to set up routing rules. For example, you can set the context based on the user location and set up a rule in the Live agent system to transfer all the requests from the specific user location to a different team. See [Example: Routing rule based on location](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing#example-routing-rule-based-on-user-location), for a sample demonstration.&#x20;

**Examples**: To request user feedback after an agent conversation, to cancel the transfer, or to request a callback from an agent.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q2jDPgLc5cqNpTk7z%2F-M-Q5yvLw92U5KxpqoHl%2Fagent-live-transfer-callbacks.png?alt=media\&token=bd0f575f-2814-4b9d-8ec0-62e0638157e0)

The following is a sample code snippet for requesting user feedback after agent conversation:

{% hint style="info" %}
**Notes**:&#x20;

* Place this script in the **After terminated** section. This is just a sample script and you can customize this as per your requirement.
* &#x20;Thumbs up and Thumbs down are the default feedback options in the system, the customized feedback does not provide these options and customized feedback is not available in Analytics.
* You must use storage variables to capture and fetch back the customized feedback. See [How-to use storage](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/using-storage), for more information.
  {% endhint %}

In the sample script, you are using Post message API to post a message to the user after a live agent conversation. See [Post messages](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/message-api#post-messages), for more information. You can also post different messages using cards and quick reply using Post message API.

```javascript
function gotofeedback(){
  //console.log(" conversation_uuid ==>: "+context.conversation_uuid);
 var json ='{ "message":{"card":{"inputs":[{"type":"data_capture","title":"Please provide the Agent feedback "}]}},"conversation":{"uuid":"'+context.conversation_uuid+'"},"bot_id": <<agent_id>>}'
  fetch('https://cXX.avaamo.com/bots_api/v1/messages.json', {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
      'ACCESS-TOKEN': '<<user-access-token>>' 
    },
    body: json
  }).then(res=>res.json())
    .then(res => console.log(res));
}

return gotofeedback();
```

### Agent chat transcript

You can export the chat history of the conversation between live agents and the users for a selected date range in a CSV format.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q2jDPgLc5cqNpTk7z%2F-M-Q6Iv2zCaZstDrJrI9%2Fagent-live-transfer-chat-export.png?alt=media\&token=6bb76846-981b-49a1-9044-eacddf34f95b)
