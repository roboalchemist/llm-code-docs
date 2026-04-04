# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents.md

# Debug agents

In case you are unable to receive the expected response from the agent, you can debug using the following troubleshooting tips:

{% hint style="success" %}
**Key points**:

* **Defining entities:**
  * Entities must be a logical grouping of nouns e.g. scheme name, which holds the same meaning across all training variations for the agent.
  * An entity must be relevant to your intent and must provide a specific context for an intent.
  * You must retain only those entities and slots that are required by the skill to process.
* **Defining skills**:
  * FAQ type skills must be Q\&A, all casual and informal queries must be Smalltalk.
  * If you have Smalltalk as Q\&A intents, then the priority of intent processing gets affected. Smalltalk has a lower priority when compared to Q\&A. See the[ Intent execution sequence](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence), for more information.
  * Also, note that Smalltalk does not participate in disambiguation.
* **Disable skill as that is no longer required**: If a skill that is no longer required is enabled, then the entities from that node still participate. The best practice is to disable the skill if it is no longer required.
  {% endhint %}

## **Using Insights**

* Click the eye icon below the user query to know the intent mapped to the query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPAchvj9LmpbB1awh5GTv%2Fimage.png?alt=media\&token=33e2c351-3a38-4254-a266-4828b4f6dece)

* In the **Insights** pop-up, you can know if the query is mapped to the required intent type, name, skill key, intent key, entities, and the language of the query. &#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6ClqLNL5TXphRYhFiOGf%2Fimage.png?alt=media\&token=a234ddb7-ad4b-45c4-a483-70d083a69a55)

* You can use this information to update the conversation flow, as required, based on the details available in the insights.&#x20;

{% hint style="success" %}
**Key Points**:&#x20;

* By default, the insights eye icon is available in the agent widget at the bottom-right corner when you are accessing the agent from the dashboard. You can enable the insights icon using debug parameter in the web channel URL if required. See [Customization parameters](https://docs.avaamo.com/user-guide/how-to/configure-agents/deploy/web-channel/configure-web-channel#customization-parameters), for more information.
* In the insights, at times additional entities are extracted. This is because in the agent all the entities that are available in any of the agent's skills are considered for extraction as it may be required in any of the JavaScript. But only those entities that are used in the slot of a training phrase are used to match the training phrases. So even if the entity is extracted, the slot is not created for that entity, it is not used for intent matching.
  {% endhint %}

## Using JS errors

In case, you have JavaScript code in your agent, then you can check for any errors using the **JS errors** option. In this section,  you can view errors related to SSML, live agent, custom channel, Regex entities, and JS errors across nodes. The following illustrates a few scenarios:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MdLipf-mhXIriWLZS-I%2F-MdM2FuEvDAAmN_gHXqM%2F5.7-js-errors.png?alt=media\&token=fb9da359-1b16-4d7f-b4cc-7ff5957f0321)

* In the **Agent** page, click **Debug  -> JS errors** option in the left navigation menu.&#x20;
* A list of JS Errors are displayed in the following format:
  * **Message**: Indicates the message or user query in the skill at the point of error.
  * **Step**: Indicates the node number in the flow that caused the error.
  * **Sender**: Indicates the details of the user who sent the message.
  * **Time**: Indicates the time of error creation.
  * **JS error**: Indicates the details of the JS error in the format -  `{"error":"<error>","line":<line number>,"section":"<section where error is present>"}`
* Correct the JS errors in the conversation flow, based on the error details displayed in the **JS errors** page.

{% hint style="info" %}
**Notes**:&#x20;

* You can use the **Clear All** option to clear all JS errors.
* The error messages are sorted based on the descending order of error creation time.
* All errors get displayed only when the specific cases are triggered in the conversation flow with a user query. For example, Regex entity error is displayed only when you use the entity in the conversation flow and it gets triggered in the conversation flow.
  {% endhint %}

## Using Debug logs

Use **console.log** to log messages at specific steps in the script. This helps to verify if the script is executing as expected and to identify points of failure. You can then use **Debug logs** options in **Dialog skill** to display all the logs generated using console.log.

Consider that in the **Order Status skill** of the **Pizza agent**,  you have logged **context** for an intent:

```markup
console.log(context);
```

* In the **Agent** page, click **Debug  -> Debug logs** option in the left navigation menu.&#x20;
* Click the agent icon in the bottom-right corner.
* Enter the order number. Context details are displayed in the **Debug logs** window. Similarly, you can use **console.log** to log messages at specific steps in the script, as required.

{% hint style="info" %}
**Note**: In the `Debug logs` pop-up window, a maximum of 50 consecutive `Console.log` statements can be printed.
{% endhint %}

## Using Storage

You can view all the data stored either for a global session (applicable for all the users interacting with agents) or for a specific user session in your agent.

* In the **Agent** page, click **Debug  -> Storage** option in the left navigation menu.&#x20;
* You can search within a specified date range or using key values of the storage variables.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-OFfMF62I1obqCQHLE%2F-M-OIVWKLbFcplRbpROp%2Fhowto-agent-debug-storage.png?alt=media\&token=188ccde4-ad89-4419-b48f-3dca8901f192)

## Using Conversation history

The **Conversation history** page displays the records of the agent and all of its user interactions for the selected agent.&#x20;

* Click any conversation to see the details. In the URL, you can also see a unique identifier for the conversation. This is referred to as conversation\_uuid. You can use this in APIs. See [Conversation API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/conversation-message-api), for an example.
* You can search through history to find specific conversations, messages, and users.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-hMeUBSJsFGM7iSn0o%2F-M-hVP_x1cUnHhj9M3q9%2Fdebug-conversation-history.png?alt=media\&token=bec723d3-eb1c-4bbd-b8fd-4622a4710029)

{% hint style="info" %}
**Notes**:&#x20;

* Currently, list view responses are not displayed in the conversation history.
* Conversation history is not real-time and it may take upto 2 minutes for the Conversation history to be updated.
* In the Configuration -> Live agent page if the **Save conversations** toggle is set to **No**, then no data or chat conversations between the users and live agents are saved in the Avaamo platform. At the specific section in the Conversation history page, a system message indicating the same is displayed.&#x20;
  {% endhint %}

The **Conversation history** page includes a search bar, agent profile icon, and user profile icon.

### Search bar

You can use the **Search** bar to search through conversation titles and message content. This helps you narrow down user queries and the agent’s response to the query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-hW9QNr7FB4cQI1uJL%2F-M-hWofEdwnS_ZY-zFqh%2Fdebug-conversation-history-search.png?alt=media\&token=ab476434-82c0-4704-a170-d24a4539b54b)

#### Conversations

Each conversation in the **Conversation history** page is grouped by user name. You can search for conversations related to a specific user by entering the user name in the search bar. All the conversation for the user or message containing the user name is displayed in the result.

#### Messages

You can search the conversation history with messages. These messages can be user queries or the agent's response. To search with a message, type the message content in the search bar.

All the messages with the searched message content are displayed. Click the message to view the details and the conversations.

Note that if you have deployed your agent in C-IVR or Phone channel, then the user responses are available as audio files in the **Conversation history**.&#x20;

### Agent profile icon

The agent profile icon button allows you to edit the profile and change the view of the conversation history page. You can perform the following actions:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-hW9QNr7FB4cQI1uJL%2F-M-hXV0jMABmxYqm7d8s%2Fdebug-conversation-history-agent-profile.png?alt=media\&token=754536f1-1c55-404a-9a2a-8f14c103c972)

* View the agent avatar, first name, last name, and the job description. You can also view any custom user authentication setting if you have provided any.&#x20;
* Change the outlook of the **Conversation history** page by clicking the **Compact view** option.
* Logs you out from the Avaamo platform dashboard.

### User icon

You can view the details of a user in the conversation by clicking the user profile icon:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-hW9QNr7FB4cQI1uJL%2F-M-haVZVqozpVeavFJG4%2Fdebug-conversation-history-user-profile.png?alt=media\&token=19430e44-f830-4fde-b36c-512fcdca39e0)

* The email address and other custom user authentication details are provided in the **Custom user authentication handler** and **Returning user message handler**. See [Define settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings), for more information.
* The channel through which the user interacted with the agent.
* The link for the agent.
* The location of the user's IP.
