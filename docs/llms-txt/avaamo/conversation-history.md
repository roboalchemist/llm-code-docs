# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history.md

# Source: https://docs.avaamo.com/user-guide/debug/conversation-history.md

# Conversation history

The **Conversation history** page displays the records of the agent and all of its user interactions for the selected agent.

* Click any conversation to see the details. In the URL, you can also see a unique identifier for the conversation. This is referred to as conversation\_uuid. You can use this in APIs. See [Conversation API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/conversation-message-api), for an example.
* You can search through history to find specific conversations, messages, and users.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5ERfZEo234eNu92ReetN%2FScreenshot%202025-04-14%20at%208.31.32%E2%80%AFPM.png?alt=media&#x26;token=ab9ab10a-7bcf-4238-8967-a9d4d6ad50af" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notes**:&#x20;

* Currently, list view responses are not displayed in the conversation history.
* Conversation history is not real-time, and it may take up to 2 minutes for the Conversation history to be updated.
  {% endhint %}

The **Conversation history** page includes a search bar, agent profile icon, and user profile icon.

### Search bar

You can use the **Search** bar to search through conversation titles and message content. This helps you narrow down user queries and the agent’s response to the query.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHcpfnvbcnfVNcdQCHi3P%2FScreenshot%202025-04-14%20at%208.34.49%E2%80%AFPM.png?alt=media&#x26;token=840791d0-e577-4312-90c7-7ad53f02fdae" alt=""><figcaption></figcaption></figure>

#### Conversations

Each conversation in the **Conversation history** page is grouped by user name. You can search for conversations related to a specific user by entering the user name in the search bar. All the conversation for the user or message containing the user name is displayed in the result.

#### Messages

You can search the conversation history with messages. These messages can be user queries or the agent's response. To search with a message, type the message content in the search bar.

All the messages with the searched message content are displayed. Click the message to view the details and the conversations.

Note that if you have deployed your agent in C-IVR or Phone channel, then the user responses are available as audio files in the **Conversation history**.&#x20;

#### **Conversation Transcript and Audio Playback**

The transcript feature provides a comprehensive view of the conversation between the user and the agent, available at the bottom of the conversation history. It covers both text and voice interactions, helping you clearly understand the flow and context of each conversation.

For voice conversations, an audio recording is also available alongside the written transcript. You can play the audio directly within the interface to gain deeper insights into the interaction, which is especially useful when tone or pronunciation needs to be reviewed.

This feature is valuable not only for understanding conversations but also for debugging and troubleshooting purposes. By reviewing both the transcript and the audio, you can easily identify any discrepancies, misinterpretations, or technical issues that may have occurred during the conversation, leading to faster resolution and improved user experiences.

Additionally, the session end reason is displayed at the bottom of the transcript, offering further context for analyzing why the conversation concluded.

### Agent profile icon

The agent profile icon button allows you to edit the profile and change the view of the conversation history page. You can perform the following actions:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FigXlahE5ejdQmkCHvE7N%2FScreenshot%202025-04-14%20at%208.47.26%E2%80%AFPM.png?alt=media\&token=87e551cd-c9db-44a0-b9ed-e06d46c4666a)

* View the agent avatar by clicking the profile option.
* Change the outlook of the **Conversation history** page by clicking the **Compact view** option.
* Logs you out from the Avaamo platform dashboard.

### User icon

You can view the details of a user in the conversation by clicking the user profile icon:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbCZfIixfCso3Q8nUPRhd%2FScreenshot%2014-04-2025%20at%2020.50.png?alt=media\&token=2df3fda1-58c2-4bfe-aff1-010f4c53f6a0)

* The email address and other custom user authentication details are provided in the **Custom user authentication handler** and **Returning user message handler**. See [Define settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings), for more information.
* The channel through which the user interacted with the agent.
* The link for the agent.
* The location of the user's IP.
