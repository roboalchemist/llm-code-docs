# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone.md

# Conversational IVR (C-IVR) or Phone (change needed)

You can deploy the agents built on the Avaamo Platform into your phone channel. This allows the callers to converse naturally with the agents via interactive voice responses (IVR) to get the desired results without having to navigate long audio menus. This feature can help to reduce live-agent calls, improve call routing, and provide a good user experience.

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.&#x20;
{% endhint %}

When you deploy your agents on the Avaamo platform, you can also add multiple languages for your agent's response, specify the timeout seconds, and choose the SMS option on call completion or when the call gets disconnected.&#x20;

In this article, the following steps are detailed:

1. [Before you begin](#before-you-begin)
2. [Configure C-IVR channel](#configure-c-ivr-channel)
3. [Test C-IVR channel](#test-c-ivr-channel)
4. [Manage channel settings](#manage-c-ivr-channel)
5. [Frequently asked questions](#frequently-asked-questions)

## Before you begin

Ensure that you have the C-IVR channel enabled for your account. If it is not enabled for your account, contact Avaamo Support for further assistance

## Configure C-IVR channel

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editin&#x67;**.**
    {% endhint %}

**To configure a C-IVR channel:**

After a successful configuration, a phone number is generated in the **Activated phone number** area and this is the number that can be used to connect to your agent via the C-IVR channel.

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the Channels page, click **Connect** in the C-IVR Channel.
* Specify the following channel setting details:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkiqUZI3g2pax8W0Onwwj%2FScreenshot%202025-02-12%20at%2012.36.48%E2%80%AFPM.png?alt=media&#x26;token=4f35e0f1-7edd-4401-98f7-28192776a5a0" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="167">Parameter</th><th>Descriptions</th></tr></thead><tbody><tr><td>Name</td><td>Indicates the <strong>Name</strong> used to identify the C-IVR channel. Note that you can have upto 150 characters in the channel name.</td></tr><tr><td><p>Languages and </p><p>Playback Voice for</p></td><td><p>Select the language and configure the voice or the persona to be used by your agent in the interactive phone conversations with the user. Each language has a different set of voice personas that you can choose from. Select the persona from the options provided in the "Playback voice for &#x3C;&#x3C;language>>" section:</p><p></p><ul><li>As with any enterprise voice, audio, or video application, each region or country has its phone number to dial. Similarly, in the C-IVR channel, you choose the language of the region or country where you wish to share the configured number. If you wish to share the number in multiple regions, then set up the C-IVR channel specific to each language. Note that one C-IVR channel is specific to only one language.</li><li>To hear the voice preview, type any text in the text area and click the play button. You can also download the voice preview if required.</li><li>You can select only those languages for which the agent is configured and those that are supported in the C-IVR channel. If you have switched to a language that is not supported in the C-IVR channel, then the agent responds in the default language.</li></ul><p>See <a href="../add-languages">Add languages</a> and <a href="voice-supported-languages">Supported languages</a>, for more information. </p></td></tr><tr><td>Speech timeout</td><td><p>Indicates a maximum wait time of the agent within which a user response is expected. If the user response is not received within the time-out period, then an automated message is rendered back to the user indicating that the agent is awaiting the user response. Currently, this is a standard message and cannot be customized.</p><ul><li>The default value is 1 second.</li><li>Use the up and down arrows to increase or decrease time as required.</li></ul></td></tr><tr><td>SMS message options</td><td>Enable this option and specify a message, if you wish to send an SMS message to the caller when the call gets disconnected and/or when the call is completed. Specify the SMS text message in the respective options as required. Note that a single SMS can have upto 150 characters.</td></tr><tr><td>Send an SMS after completion of call</td><td>Enable this option and specify a message, if you wish to send an SMS message to the caller when the call is completed. Note that a single SMS can have upto 150 characters. If a call is hung up after a successful dialogue between the user and the agent, that is a user asks a query and the agent responds back to the query, then it is considered as complete.</td></tr><tr><td>Send an SMS if call disconnects</td><td>Enable this option and specify a message, if you wish to send an SMS message to the caller when the call gets disconnected. Note that a single SMS can have upto 150 characters. A call is considered disconnected when the user asks a query and before the agent response is received the call gets hung up. This is the case when the user is in between a conversation flow.</td></tr><tr><td>Enable custom user authentication</td><td>Use this if you wish to enable custom authentication for your agents deployed on the phone channels using JavaScript code. See <a href="../../define-settings#user-authentication-handler">User authentication handler</a>, for more information.</td></tr><tr><td>Enable wait time tone</td><td><p>Use this option if you wish to play an idle tone to the user in case the agent is taking a little longer to respond. </p><p></p><p>Rather than experiencing silence or a lack of input, the introduction of a tone serves to engage the user actively and assures that the agent will respond shortly. For example, the system generates a typing tone when processing DTMF/keypad input.</p></td></tr><tr><td>Select file</td><td><p>Once you enable the wait time tone, the option to upload a file becomes available. You can customize the wait time tone by uploading an audio file that plays an idle tone for the user. The file must not exceed 10 seconds and should be within 5 MB in size.<br></p><p>Click <strong>Select File</strong>, then choose and upload the desired file for the wait time tone.</p></td></tr></tbody></table>

* Click **Save** to save the C-IVR channel configuration details. A phone number is generated in the **Activated phone number** area and this is the number that can be used to connect to your agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MObDJReaiTqqzn81xT6%2F-MObDyyKrmG8GjgSpKrn%2Fc-ivr-channel-settings-save.png?alt=media\&token=cba0dad3-39e7-40e5-95fc-479939d40e06)

{% hint style="success" %}
**Key Points**:&#x20;

* After you save the C-IVR configuration successfully, you get options to add "Agent voice",  "Voice menu", and "Voice hints" to the agent responses. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses) and [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings), for more information.
* If you have deployed your agent in the C-IVR or Phone channel and masking is enabled, then the audio files from the user responses are not available in the conversation history, since it can contain PII data. See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for information.
* Currently, you cannot [transfer to a live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent) that is configured in the Avaamo Platform from the C-IVR channel. Instead, it is recommended that you use [Call forward](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#call-forward) for connecting to live agents.
* You can also enable custom voice for your C-IVR agents in the Avaamo Platform. Contact Avaamo Support, for more information.
  {% endhint %}

## Test C-IVR channel

After you save your C-IVR channel configuration settings, you can test the C-IVR channel using Agent Simulator from the bottom-right corner of the page. See [Agent simulator](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/simulator), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MN8KHRCRxPxcH_jLXrm%2F-MNC9bSw4NGI3z7gB4LD%2Fc-ivr-agent-simulator.png?alt=media\&token=96bd9f8e-25d5-43d8-af59-4f8427ab27e0)

If you select the IVR / Phone option, then C-IVR activated phone number is displayed with a phone icon.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MN8KHRCRxPxcH_jLXrm%2F-MNByFw1WQvjaYOQBkJP%2Fc-ivr-test.png?alt=media\&token=1239ec82-d778-4d43-aab7-28c9310d74ce)

Click the phone icon to dial the activated phone number and test your conversation flow. Click transcripts to further know how your agent is interpreting the responses from the user.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MN8KHRCRxPxcH_jLXrm%2F-MNBzjsEhHULY4vqnN8u%2Fc-ivr-transcript.png?alt=media\&token=da98289c-5085-459a-8471-5384a47c1ee5)

## Manage channel settings

{% hint style="info" %}
**Note**: When you re-deploy a C-IVR channel, a new number is assigned and the existing phone number is removed from the channel.
{% endhint %}

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.

You can also deploy your agent through multiple C-IVR channels simultaneously. On the Channels page, click **Connect** in the C-IVR channel and follow the steps in [Configure C-IVR Channel](#configure-c-ivr-channel) to deploy your agent into another custom channel.

## Frequently asked questions

### 1. How to improve the accuracy or recognition of speech in the C-IVR channel?

You can specify certain keywords or phrases in the **Voice hints** that can provide better interpretation or recognition of the user response in the conversational IVR interaction. Providing voice hints can significantly improve user interaction with your agent. When you add voice hints, the agent gives preference to the phrases provided in the hints when interpreting the user responses. This helps you to redirect the conversational flow smoothly. See [Voice hints](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/voice-hints), for more information.

### 2. How is the PII (Personally identifiable information) data masked if my agent is deployed in the C-IVR channel?

If you have deployed your agent in the C-IVR or Phone channel and masking is enabled, then the audio files from the user responses are not available in the conversation history, since it can contain PII data.&#x20;

### 3. The agent is not recognising my response. What should I do?

In cases where you are unable to receive the expected agent response, refer to the following troubleshooting tips:

* Use the Agent simulator -> Chat transcripts to know how your agent is interpreting the responses from the user. See [Test C-IVR channel](#test-c-ivr-channel), for more information.
* Try adding Voice hints and check if that helps in improving the recognition of the user responses. You can add [Voice hints at the agent level](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings) and also for a node at the Dialog skill in the [Advanced settings -> Voice hints section](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#voice-hints).

### 4. I am unable to transfer to a live agent from the C-IVR channel. What can I do?

Currently, you cannot [transfer to a live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent) that is configured in the Avaamo Platform from the C-IVR channel. Instead, it is recommended that you use [Call forward](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#call-forward) for connecting to live agents.
