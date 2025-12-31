# Source: https://docs.avaamo.com/user-guide/live-agent-console/live-agent/live-agent-translation.md

# Live agent translation

{% hint style="info" %}
**Pre-requisite:** The supervisor must ensure the **Enable Live Agent Translation** option is enabled for the live agents. See [Live Agents](https://docs.avaamo.com/user-guide/supervisor/live-agents#enable-translation-for-live-agents), for more information.
{% endhint %}

Avaamo Platform provides the capability to build virtual assistants in 100+ languages such as French, Arabic, Chinese, Polish, and many more. This enables the users to converse with the virtual assistant in their local language making the experience more personal and enriching. See [Web - supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages) and [Language pack](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/language-pack), for more information.

Now, consider a case where a user conversing with the virtual assistant in a local language, wishes to connect to a live agent. Ideally, the users must be connected to a live agent who understands the same local language for an effective conversation. This process can have many challenges:

* **Cost and Maintenance:** You need a team of live agents proficient in various languages supported by the virtual assistant. With the `Live agent translation` feature, customers, and agents can communicate in their preferred languages in real-time. This feature enables businesses to serve a diverse customer base without requiring agents to be fluent in every language, optimizing staffing and reducing the risk of miscommunication.
* **Operational efficiency**: In the live agent system, specific routing rules must be considered to detect the user's language and then route to the live agent.

With `Live agent translation` feature capability in the `Avaamo Live agent` console, all the above challenges are eliminated. This feature offers robust translation capabilities to facilitate seamless communication between users and live agents. It eliminates the need for language-specific live agents.

{% hint style="info" %}
**Note:** All end-user messages are translated into English only. `en-US` is the only language supported for Live agents.
{% endhint %}

### How it works?

This feature enables smooth translation between the users and the live agents.&#x20;

Users can continue to converse with the virtual assistant in their local language, however, during the conversation with the virtual assistant, when users connect to a live agent, the user messages are automatically translated from the user's local language to English and from English back to the user's local language. This ensures a smooth and effective conversation experience.

* **End user to Live agent:** When an end user communicates with a live agent, the responses are automatically translated into English. This ensures that live agents can understand and respond to inquiries regardless of the original language used by the virtual assistants.
* **Live Agent to the End User:** Similarly, when a live agent responds to the end user, the message is translated back into the user's conversation language in the virtual assistant.

**Example of Live agent translation:**

Consider a user is conversing with a virtual assistant in French.&#x20;

1. **User Initiates Conversation**: The user starts a conversation with a virtual assistant in French.
2. **Transfer to Live Agent**: The conversation is transferred to a live agent who communicates in English.
3. **Translation of User Messages**:
   * The system translates messages from the user, written in French, into English.
   * These translated messages are then displayed to the live agent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7wBuhEYTJXQxGbbD2S2E%2FScreenshot%2019-07-2024%20at%2012.35.png?alt=media&#x26;token=18c81fcf-503f-4663-8b1b-d31268f4bcdd" alt=""><figcaption></figcaption></figure>

4. **Agent's Response Translation**:

* The live agent responds in English.
* The system translates the agent's response into French.

5. **User Receives Response**: The translated response in French is sent back to the user, ensuring clear and effective communication.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FU6uQKE6sucJc80xxiAjF%2FScreenshot%2019-07-2024%20at%2012.35%20(3).png?alt=media&#x26;token=8061d1e4-484b-40c7-8a45-0b7c9b981208" alt="" width="375"><figcaption></figcaption></figure>

Live agents can review language translations by clicking "**View Translation**." This action displays a dialogue box showing the translated text and the source language from which the translation is being made.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFqiGQNCMF686oRKEbiBC%2FScreenshot%2031-07-2024%20at%2016.41.png?alt=media&#x26;token=a6d5b86b-5440-43dc-b232-2b6ce9ff9483" alt=""><figcaption></figcaption></figure>

Agents can review translated messages before sending them to the end user. By clicking "**Show Translated Text**," the translated message appears in a dialog box. You can also use a keyboard shortcut **Ctrl+U** for this option.

This feature allows live agents to see the virtual agents' languages and manually verify the translation if they are familiar with it.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7S8F6I5rHcfHg5BJ7KEd%2FScreenshot%2006-08-2024%20at%2012.23.png?alt=media&#x26;token=de711edf-5159-47f4-b0da-67350576be55" alt=""><figcaption></figcaption></figure>
