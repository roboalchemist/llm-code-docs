# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview.md

# Skill message window - Overview

In the **Skill message** window, you can add responses to user intents. The following lists the steps to add responses:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbkKvaOiwIW6F0ZFSt0%2F-MbkL-45o1k7iOO1-DyO%2F5.7-skill-message-overview.png?alt=media\&token=ba6a358d-5473-4c25-abfe-1999e61816ae)

**Step 1: Select a channel**: You can add different customized responses for different channels your agent is deployed on. See [Channel-specific responses](#channel-specific-responses), for more information.

{% hint style="info" %}
**Notes:**

* You can also omit selecting a channel, if you do not wish to provide channel-specific responses.
* If you have deployed your agent in a specific channel for which you have not configured any response, then the response as specified in the "Default response" option is considered. **Example**: Consider that you have deployed your agent in Web, Android, and iOS channels and you have configured responses only for the Android channel. For the Web and iOS channel, the responses as specified in the **Default response** option is displayed.
  {% endhint %}

**Step 2: Select a language**: If you have added languages in your agent, you can customize responses specific to each language. See [Languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on how to add languages to an agent. See [Language-specific responses](#language-specific-responses), for more information on how to customize the language responses.

{% hint style="info" %}
**Note**: For [Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers) and [Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa), you can set channel-specific and language-specific messages from the **Implementation -> Question & Answers** page.&#x20;
{% endhint %}

**Step 3: Add response:** For each selected channel-language combination, you can add responses as per your requirements. You can also create multiple responses for each user intent, add tags, and create response filters as per your requirement. See [Add responses](#add-responses-channel-language-combination), for more information.

{% hint style="success" %}
**Key point**: With the ability to add channel-specific and language-specific skill responses, you can now add responses specific to each channel-language combination. **Example**: You can add a response specific to the Android channel in the French language.
{% endhint %}

## **Channel-specific responses**

Using this feature, you can add different customized responses for different channels as per your requirement.&#x20;

{% hint style="info" %}
**Note**: Only those channels that are enabled for your account or company are displayed in the Channel dropdown. If you wish to enable a channel, then contact Avaamo Support for further assistance.
{% endhint %}

**To add channel-specific response**:

* In the **Skill message** window, select the channel for which you wish to add the response from the **Channel** dropdown.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbjijIX-Un5805PaZId%2F-MbjkX-NjUcO0PsEwMyS%2F5.7-skill-message-channel-specific.png?alt=media\&token=209577e7-eee2-4117-8907-4114ab7f0dd5)

* If you have not configured any response for the selected channel, then the following message is displayed. Click **Add response** to proceed. See [Add responses](#add-responses-channel-language-combination), for more information on how to add responses.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbjV4SRPQWbx4wetiGx%2F-MbjVyYd0rVg0XAkAB_B%2F5.7-skill-message-add-channel-response.png?alt=media\&token=3133727b-6993-4bc5-a4b3-4a071e097fd3)

{% hint style="info" %}
**Note:** For [Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers) and [Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa), you can set channel-specific messages from the **Implementation -> Question & Answers** page.&#x20;
{% endhint %}

* If you have already configured a response for the selected channel, then the same is displayed. You can then edit the response as required.

## **Language-specific responses**

If you have added languages to your agent, you can view the list of languages in the language dropdown. This allows you to view and customize the responses in different languages. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information.

**To add language-specific response**:

* By default, the response in en-US is displayed. Select a **language** from the dropdown. The translated responses of the specific language are displayed. You can customize the response in the selected language as required. See [Add responses](#add-responses-channel-language-combination), for more information on how to add responses.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMeBxjvrBpC7J8HB0q2Jm%2F6.1-skill-response-lang.png?alt=media\&token=48ff1f78-8e3a-48dc-b781-819d795d1627)

* To customize the translation, click the text area where you wish to customize it. Specify the required custom translation. Note that when you provide a custom translation, the text area background is changed to blue. This helps you to easily identify custom and system-generated translations.
* Click the button in the bottom-right corner of the text area, if you wish to reset the translation to system-generated translation. You can also click the reset button at the top, to reset all the text in the skill response to system-generated translation.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FP9slQNIyz6TUnRhFMKWG%2F6.1-lang-reset.png?alt=media\&token=68fdfbd5-323e-4a6d-8272-2089908d5145)

{% hint style="info" %}
**Notes**:&#x20;

* For Greeting and Unhandled skills, you can add language-specific responses for those languages configured in your agent. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information.
* For [Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers) and [Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa), you can set language-specific messages from the **Implementation -> Question & Answers** page.
  {% endhint %}

## Add responses (Channel-Language combination)

In this section, for each selected channel-language combination, you can add responses as per your requirements. You can also create multiple responses for each user intent, add tags, and create response filters as per your requirement.&#x20;

This section contains two main panels:

* [Panel 1: Prompt details](#panel-1-prompt-details): This is where you can configure and preview the responses using different in-built response types such as Text, Card, Quick reply.&#x20;
* [Panel 2: Advanced settings](#panel-2-advanced-settings): In this panel, you can control skill flow, specify options to collect feedback, and specify idle prompt settings.

## Panel 1: Prompt details

The **Prompt details** panel is divided into three sections:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fcb3boIMIzMaqwbRfFRvt%2F6.1-skill-response-sections.png?alt=media\&token=38311416-9cc3-4e51-b2ee-f24e13e77a6a)

* **Left section**: In this section, you can add multiple responses for the same user intent. See [Responses](#responses), for more information.
* **Middle section**: View the preview of the message. See [Response](#response) and [Voice response](#voice-response), for more information.
* **Right section**: Add skill messages such as Text, Quick reply, and Card for each response. See [Messages](#messages), for more information.

### Responses

This helps to identify responses when you have multiple responses for the same user intent. Click **Add** to add another response for the same user intent.

{% hint style="info" %}
**Note**: If you add multiple responses for an intent without any response filter, then the system picks a random response from the set of multiple responses and displays it to the user.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbkT74sgBzlCh9mnr4v%2F-MbkU4NbnvDo9-VKd3Cx%2F5.7-skill-message-window-responses.png?alt=media\&token=53d9b38d-f9e4-4c36-83d9-e1022a5cec89)

* For each response, you can enter the response name.
* If you wish to use the default response for the selected channel, then move the slider **Use responses from default** to **Yes**.&#x20;

{% hint style="info" %}
**Note**: When you move the slider **Use responses from default** to "yes", then&#x20;

* The default response is used, even when you have configured a response for the selected channel.&#x20;
* The channel specific response is non-editable since you wish to use the default response for the selected channel.&#x20;
  {% endhint %}

You can add upto 50 responses to the same user intent. See [FAQs in Response filters](https://docs.avaamo.com/user-guide/build-agents/configure-agents/add-response-filters#3-when-multiple-responses-with-response-filters-match-the-user-intent), for more details on the order of execution.

### Response

This is where you can preview the response added in the **Messages** section. Click the plus icon and select from the list of response types.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbkUlyTO6LI_c6j9iKc%2F-MbkV-Tc5ict-AscxqGo%2F5.7-skill-message-window-response.png?alt=media\&token=63b2aa9a-5ca3-4966-805c-2da5fe98a65c)

For each response type, you can enter the details in the **Messages** section. As you enter the details in the [Messages](#messages) section, you can preview the same in the **Response** section.

### Voice response&#x20;

If you have enabled voice in web, android, or iOS channels, then you can specifically add a response for voice in the **Voice response** panel. See [Voice](https://docs.avaamo.com/user-guide/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), for more information on how to enable voice in web, android, or iOS channels.&#x20;

{% hint style="info" %}
**Notes**:

* You can also configure voice hints and playback voice of the voice assistant in the web channel. See [Voice settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings), for more information.

* If you have configured messages both in response and voice response, then the response message is displayed in the agent chat widget and the voice response is read out to the user.

* You can also omit configured Voice responses. If you have not configured a Voice response, then the Response message is read out to the user. Note that for the voice messages to be read out from the Response message, it must be either [Text](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-skill-messages-responses#text) or [Quick reply](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-skill-messages-responses#quick-reply) response types.

* Not all languages are supported in the voice assistant. See [Voice - Supported languages](applewebdata://F30A6D8E-2686-41CE-B971-3854BD2057D8/@avaamo/s/avaamo/~/drafts/-MYxGNUFf68iUPzf71u7/v/dev/how-to/build-agents/configure-agents/deploy/voice-supported-languages), for more information.
  {% endhint %}

* Select channel as either Web, Android, or iOS where you have enabled voice and wish to configure the voice response

* Click the plus icon and select from the list of response types.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbpTEmwPjDQw0e4KZ7l%2F-MbpTPStSLzQYqlAw954%2F5.7-skill-message-window-voice-response.png?alt=media\&token=bd79869b-be52-4ad1-8c2a-ac1f4b2cb38b)

* For each response type, you can enter the details in the **Messages** section. As you enter the details in the [Messages](#messages) section, you can preview the same in the **Voice** **Response** section.

### Messages

This is where you make changes to the skill response by adding messages, images, buttons, and elements. See [Add a skill message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#add-a-skill-message), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbkXKzErbsLaH9TLrG-%2F-MbkYAljq9vGkfk1fNzi%2F5.7-skill-message-window-messages.png?alt=media\&token=eb15d332-8804-4c0e-aaaf-32548f8915f3)

{% hint style="info" %}
**Note**: There is a 192 character limit for all the user-defined text fields.
{% endhint %}

#### **Tags**

Add tags to the skill responses, if you have configured any for the agent. This is useful when you wish to assess the usage of the agent by categorizing and tagging the intents distributed across different skill responses. As you type, a list of tags configured for your agent is displayed in the dropdown. You can also add multiple tags if required.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbkXKzErbsLaH9TLrG-%2F-MbkYAljq9vGkfk1fNzi%2F5.7-skill-message-window-messages.png?alt=media\&token=eb15d332-8804-4c0e-aaaf-32548f8915f3)

{% hint style="info" %}
**Note**:&#x20;

* You can upto 50 tags for a skill response. See [Add tags](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-tags), for more information.
* You can dynamically associate tags to responses using JS. See [Add tags (JS)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js), for more information.
  {% endhint %}

When the user query hits the node, all the corresponding tags added to the node are associated with the user query. You can view the top tags in the Analytics board. See [View analytics of top tags](https://docs.avaamo.com/user-guide/build-agents/monitor-and-analyze/analytics#top-tags), for more information on the "Top Tags" Analytics board.

#### **Response filters**

Add filters to the skill responses, if you have configured any for the agent. This is useful when you wish to add different responses for the same user intent based on certain user properties such as location and status. As you type, a list of response filters configured for your agent is displayed in the dropdown. You can also add multiple response filters if required.&#x20;

{% hint style="info" %}
**Note**: You can add upto 50 response filters to a skill response. Each response filter is an AND condition; the response is displayed only when all the filters match. See [Add response filters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters), for more information.
{% endhint %}

When the user query hits the node, the corresponding response filters are applied and the appropriate response is displayed for the user. See [FAQs in Response filters](https://docs.avaamo.com/user-guide/build-agents/configure-agents/add-response-filters#3-when-multiple-responses-with-response-filters-match-the-user-intent), for more details on the order of execution. Also, see [Example: Add response filters](https://docs.avaamo.com/user-guide/how-to/build-skills/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers#example-add-response-filters).

#### **Skip translation**

Check this option, if you wish to skip translation to the detected language.

## **Panel 2**: **Advanced Settings**

In the **Advanced settings** tab of skill response, you can control skill flow, specify options to collect feedback, and specify idle prompt settings. If you have deployed your agent in the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), then you can also specify Voice hints.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbkXKzErbsLaH9TLrG-%2F-MbkYme79A4wf3vZ4VpG%2F5.7-skill-message-window-adv-settings.png?alt=media\&token=2a1d50a3-41f3-4b80-a4e0-0e32e1c69a34)

See [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* **Advanced settings** option is available only for Dialog skill responses.
* To delete any field or element, hover on the field or element in the preview section and click the **Delete** icon.

{% endhint %}

## Example: Add response filters

Consider that you wish to display different responses for the same Dialog skill intent based on the user location property:

| User query                       | Indian user                                                                                                                                           | US user                                                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| I want to onboard a new employee | Alright. Let's start entering basic details. Can you enter the Aadhar number of the new employee? I will quickly check and fill in the other details. | Alright. Let's start entering basic details. Can you enter the SSN of the new employee? I will quickly check and fill in the other details. |

### Step 1: Add user properties&#x20;

Add a user property "Office City". See [Add user properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbaGeLBhmnw1SLge4K9%2F-MbaHC_k68ZRQcOUAkLW%2F5.7-add-user-property.png?alt=media\&token=0c904c12-7d28-445f-8b07-35dd045c74c1)

### Step 2: Add response filters

Configure two response filters, one for "Location - India" and another for "Location - US". Add values for each of these as required. See [Add response filters](https://docs.avaamo.com/user-guide/build-agents/configure-agents/add-response-filters#add-response-filters), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF-PS4TjwPpFPD93KH2%2F-MF-f6gM2ilJ17lWw4ca%2Fconfig-response-filters.png?alt=media\&token=47771aec-fa5d-42ba-a3c8-03d3c88fd039)

### **Step 3**: **Add response filters to Dialog skill response**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MUwRRnrBNnyk8VcZ1GC%2F-MUwSffwyNam4MSJIUoV%2Fdialog-skill-response-filters.png?alt=media\&token=60b2577a-b28b-47f4-8ab5-9af0f7ca40fa)

* In the Skill messages, add two text responses:
  * "Alright. Let's start entering basic details. Can you enter the Aadhar number of the new employee? I will quickly check and fill in the other details." and apply the "Location - India" response filter.
  * "Alright. Let's start entering basic details. Can you enter the SSN of the new employee? I will quickly check and fill in the other details." and apply the "Location - US" response filter.

### **Step 4: Test your agent**

* In the web channel URL, set the custom\_properties\[office\_city]=Bangalore. Specify the user query in your agent simulator and check if the response of the "Location - India" response filter is received.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8lgXQOV912bcAyMoYR9B%2Fimage.png?alt=media\&token=8b74c5b6-562a-4e38-af11-f410b3a7c786)

* &#x20;In the web channel URL, set the custom\_properties\[office\_city]=Boston. Specify the user query in your agent simulator and check if the response of the "Location - US" response filter is received.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSntBK2m4q8B4kaHQhkFN%2Fimage.png?alt=media\&token=f918074e-0a24-42bb-8a03-d65e0430502e)

* See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties) and [Test your web channel](https://docs.avaamo.com/user-guide/build-agents/configure-agents/deploy/web-channel#test-your-web-channel), for more information.
