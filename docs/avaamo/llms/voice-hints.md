# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/voice-hints.md

# Voice hints - Improve accuracy

You can specify certain keywords or phrases in the Voice hints that can provide better interpretation or recognition of the user response in the conversational IVR interaction. Providing voice hints can significantly improve user interaction with your agent. When you add voice hints, the agent gives preference to the phrases provided in the hints when interpreting the user responses. This helps you to redirect the conversational flow smoothly.

The following lists a few use-cases where voice hints can be used:

* To help agents understand certain nuances of dialects or accents of users.
* To provide clues or hints to the agent indicating that the user can provide such similar inputs at the specified node when the response is read out to the user.

{% hint style="success" %}
**Key Point**: It is recommended to use the Voice entity model instead of Voice hints as applicable. Voice entity models are more robust helps in significantly increasing the accuracy of user utterances. See [Voice entity model](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/voice-entity-model), for more information.&#x20;
{% endhint %}

## **How does it work?**

Adding voice hints to your agent is a simple three-step process:

* [Step 1: Identify the voice hints that you wish to add](#step-1-identify-the-voice-hints-that-you-wish-to-add)
* [Step 2: Identify where to add voice hints](#step-2-identify-where-to-add-voice-hints)
* [Step 3: Test and Monitor using conversation history](#step-3-test-and-monitor-using-conversation-history)

### Step 1: Identify the voice hints that you wish to add

One of the main challenges of adding voice hints is predicting the possible voice hints that are required to be added. The best way to know the voice hints required for an agent is by continuously monitoring the agent-user interactions using the Conversation history.&#x20;

In the Conversation history, you can

* Check for the user queries that went unhandled.&#x20;
* Analyze, if it is because of incorrect recognition and how adding a voice hint to the user phrase can help.

See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-conversation-history), for more information.

### Step 2: Identify where to add voice hints

Voice hints can be added at the agent level and node level:

<table><thead><tr><th width="150">Where?</th><th width="505.4285714285714">When?</th></tr></thead><tbody><tr><td>Agent -> Configuration -> Voice hints</td><td><p></p><ul><li>Use this if you have phrases that are commonly used across skill</li><li>Adding all the voice hints at the agent level impacts the accuracy of the response, hence, it is recommended to carefully evaluate before adding voice hints at the agent level. </li><li>See <a href="../../../how-to/build-agents/configure-agents/add-voice-settings#configure-voice-hints">Add voice hints</a>, for more information.</li></ul></td></tr><tr><td>Skill -> Advanced Settings -> Voice hints</td><td><p></p><ul><li>Use node-level voice hints when you require better accuracy or recognition at a specific node. </li><li>Node level voice hints are applied when control is at the node level and then the voice hints at the agent level are considered. </li><li><p>See <a href="../../../how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#voice-hints">Voice hints</a>, for more information.</p><p> </p></li></ul></td></tr></tbody></table>

You can also use in-built Voice hints commands to specify certain commonly used voice hints. See [Voice hints commands](#voice-hints-commands), for more information.&#x20;

### Step 3: Test and Monitor using conversation history

After you add the required voice hints and test it, monitor the conversation history to know if adding the voice hints helped in better recognition. Continue monitoring the conversation to learn voice hints that can be added to the agent. See [Test C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone#test-c-ivr-channel), for more information.

## **Voice hints commands**

You can also use the following voice hints commands that help the agents in better recognition and identification of user responses for certain specific types of data:

* **Dates**: If you are expecting a date response, then you can use `expecting_date` in the voice hints.
* **Numbers**: If you are expecting a numeric response, then you can use `expecting_number`\
  &#x20;in the voice hints.
* **Alphanumeric**: If you are expecting an alphanumeric response, then you can use\
  &#x20;`expecting_alphanumeric` in the voice hints.

## **FAQs**

### 1. I do not want to repeat adding voice hints at each node. Can I add all voice hints at the agent level itself?

You can use agent-level voice hints when you have voice hints that are required to be used commonly by different skills in an agent. Note that adding all the voice hints at the agent level impacts the accuracy of the response, hence, it is recommended to carefully evaluate before adding voice hints at the agent level.

**Example**: Consider that you have added an inbuilt voice hint `expecting_number` to recognize numbers better at the agent level, so that similar sounding phonetics such as "won" -> "one", "four" -> "for"  get interpreted as numbers accurately. Now, since you have added this at the agent level, even when the user is actually trying to say "for", it gets recognized as "four" and this can lead to incorrect matches. In this case, adding a voice hint at the node level is a better option.

Hence, when you require better accuracy or recognition at a specific node, it is recommended to provide voice hints at the node level. These voice hints are only applicable to that node where it is specified. See [Advanced Settings -> Voice hints](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#voice-hints), for more information.&#x20;

### &#x20;2. Can I add sentences in voice hints?

It is recommended to add phrases or words in voice hints.&#x20;

### 3. How to add voice hints in bulk?

Currently, there is no option to add voice hints in bulk. You have to add it manually one at a time from the UI.
