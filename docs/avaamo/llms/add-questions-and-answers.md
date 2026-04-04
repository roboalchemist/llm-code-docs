# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers.md

# Add questions and answers

In the **Questions and Answers** section, you can create user intents (questions) and skill responses (answers) manually or by importing a CSV file with Q\&A. See [Import Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/using-q-and-a-designer/build-and-manage-q-and-a-skill/perform-common-actions#import), for more information.

{% hint style="success" %}
**Key Points**:&#x20;

* Multiple developers can add questions and answers simultaneously in the same Q\&A skill, encouraging faster development of the skill. As a best design practice, it is recommended to distribute a set of intents among developers, so that it is easy to maintain and manage and results in seamless collaboration.
* See [Parallel development (QA & Smalltalk) FAQs](https://docs.avaamo.com/user-guide/ref/parallel-development-qa-and-smalltalk-faqs), for common FAQs around parallel development of QA and Smalltalk skills.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MZv_GIB83Qx8Roz2h2T%2F-MZviODyWdpC8XWctMaL%2F5.7-qa-add-new.png?alt=media\&token=0839e9c9-58c7-4b02-84c1-39997320bc7a)

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can manage a skill immediately after creating the skill. See [Create new Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/create-a-new-dynamic-q-and-a-skill), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

## **Add question and answers**:

* In the **Dynamic Q\&A** page, click **Question & Answers** in the **Implementation** tab.&#x20;
* Select the channel for which you wish to add the Q\&A. Using this feature, you can add different customized responses for different channels as per your requirement. If you have deployed your agent in a specific channel for which you have not configured any response, then the response as specified in the "Default response" option is considered. Example: Consider that you have deployed your agent in Web, Android, and iOS channels and you have configured responses only for the Android channel. For the Web and iOS channel, the responses as specified in the Default response option is displayed.

{% hint style="info" %}
**Note**: Only those channels that are enabled for your account or company are displayed in the Channel dropdown. If you wish to enable a channel, then contact Avaamo Support for further assistance.
{% endhint %}

* If you have configured languages in your skill, then select the language in which you wish to add the response. By default, the response of the default language as specified in the agent configuration is displayed. See [Add language-specific responses](https://docs.avaamo.com/user-guide/how-to/build-skills/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#language-specific-responses), for more information on how to add language-specific responses in the skill message.

{% hint style="success" %}
**Key Point:** With the ability to add channel-specific and language-specific skill responses, you can now add responses specific to each channel-language combination. Example: You can add a response specific to the Android channel in the French language.
{% endhint %}

* Click the plus icon to add user questions and the skill responses (answers).&#x20;
* Add required [Intent](#intent), [Entities](#entities), and [Prompt details](#prompt-details).&#x20;
* Click **Save** to save the Q\&A.
* You can continue to add questions and responses as required.

Your Q\&A skill is ready for testing. See [Test Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/test-q-and-a), for more information. You can also add languages, edit intents, and responses, and import Q\&A. See [Perform common actions](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/build-and-manage-q-and-a-skill/perform-common-actions), for more information.

{% hint style="success" %}
**Key point**: If you have added response filters to the skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

### Intent

You can specify the user questions in the **Intents** tab.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0u6LF-sKTWqZGdgkm%2F-Mb0uV3_1z8Lh2rPBvYk%2F5.7-dynamic-qa-add-intent.png?alt=media\&token=5de448ed-eb1a-406d-8b67-160ee9cef027)

<table><thead><tr><th width="150">Parameters</th><th width="375.72289156626505">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. </p><p></p><p>By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p><strong>Supported characters</strong>: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p></td><td align="center"><p>20 </p><p>characters</p></td></tr><tr><td>Intent name</td><td><p>Indicates the name of the intent. </p><p></p><p>Each intent name must be unique within the agent.</p></td><td align="center"><p>191 </p><p>characters</p></td></tr><tr><td>Training phrases</td><td><p>Indicates the training data or variations for the intent. Type the required training data and press enter or click Add. </p><p></p><p>You can add multiple training data to the intent as required. There is no limit on the number of training data or training phrases that can be added to an intent. </p><p></p><p>It is recommended that you follow the recommended best practices for adding training data. See <a href="../../../../design-skill#intent-and-training-phrases-training-utterances-or-training-data">Intents and training data</a>, for more information. </p><p></p><p>Note the following points on Training phrases: </p><ul><li>When you add the training phrase, the entities and slots are automatically extracted and displayed. </li><li>The color of the phrases in the user utterances matches with the slots for easy identification. </li><li>In cases, where the slots are not extracted, you can right-click on the word or phrase to select and add slots manually. Note that you can manually extract only those slots for which the entities are already added in the Q&#x26;A intent.</li><li>Click the slots to rename, if required.</li><li>You can delete the slots if it not required. Corresponding entities in the <a href="#entities">Entities</a> tab are also deleted.</li></ul></td><td align="center"><p>Each of </p><p>300 characters</p></td></tr></tbody></table>

{% hint style="success" %}
**Key points**:

* If you have multiple intents with exactly the same training data, then the latest intent response is displayed to the user.
* If you have multiple intents with similar training data, then the query goes for disambiguation.
* Slot name must be unique across all entity types in an agent. When a user query is posted, the intent execution considers the training data across all the skills in the agent, hence, the slot name must remain unique across all entity types in an agent. **Example**: Consider that you have a slot name "otp" with entity type as "Number". In this case, if you try to add the same slot name "otp"  for a different entity type "One-time password", then an error message is displayed that the slot name is already taken by another entity type.
  {% endhint %}

### Entities

In the **Entities** tab, you can view all the entities extracted for the Q\&A intent. You can delete the entity if it is not required and the corresponding slots in the training phrases are also removed.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0go0QqJQyt-aeik_T%2F-Mb0hSwiIgHvOUxG1vlT%2F5.7-dynamic-qa-entities.png?alt=media\&token=800667e4-cb44-4f9d-ae8f-b500caff943c)

{% hint style="success" %}
**Key point**: Slot name must be unique across all entity types in an agent. When a user query is posted, the intent execution considers the training data across all the skills in the agent, hence, the slot name must remain unique across all entity types in an agent. **Example**: Consider that you have a slot name "otp" with entity type as "Number". In this case, if you try to add the same slot name "otp"  for a different entity type "One-time password", then an error message is displayed that the slot name is already taken by another entity type.
{% endhint %}

### Prompt details&#x20;

In the **Prompt details** tab, specify the skill responses (answers) to user questions. You can also add filters to your responses and tag the responses for analytics. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FY1u4qAiU6JF5Xv5Fnznw%2F6.2-response-types-qa-smalltalk.png?alt=media\&token=fb15d71a-d7f2-4392-8e27-9400f2a85ae6)

Note that [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings) options as available for the Dialog skill are not applicable to the Q\&A skill.

## Add Intro and Outro messages

You can also specify Intro and Outro messages in the **Question & Answers** page:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MZvqdGqDd6fVggInpvF%2F-MZvt9PhygFZEBBVjjqD%2F5.7-qa-add-intro-outro.png?alt=media\&token=073b80b3-9c1d-4d3e-a3e6-06bb63a2564b)

* **Intro messages**: Displayed before an answer to the user question. All skill messages can be added to an intro message. Typically, this is used to acknowledge the user question such as "Thank you for showing interest".&#x20;
* **Outro messages**: Displayed after an answer to the user question. All skill messages can be added to an outro message. Typically, this is used to collect feedback. You can also create a JS to navigate to a skill and a node.&#x20;
* Continue to add questions and responses as required.

## Example: Add response filters

Consider that you wish to display different responses for the same Q\&A intent based on the user location property:

| User query           | Indian user                                                                                | US user                                           |
| -------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| Where is your store? | In India, you can find our stores in all major cities - Mumbai, Delhi, Chennai, Bangalore. | In the US, our store is located only in New York. |

### Step 1: Add user properties&#x20;

Add a user property "Office City". See [Add user properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

### Step 2: Add response filters

Configure two response filters, one for "Location - India" and another for "Location - US". Add values for each of these as required. See [Add response filters](https://docs.avaamo.com/user-guide/build-agents/configure-agents/add-response-filters#add-response-filters), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF-PS4TjwPpFPD93KH2%2F-MF-f6gM2ilJ17lWw4ca%2Fconfig-response-filters.png?alt=media\&token=47771aec-fa5d-42ba-a3c8-03d3c88fd039)

### **Step 3**: **Add response filters to Q\&A response**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0hXfeeu4iLEdbm-lD%2F-Mb0iaKc1oetDzUK88fx%2F5.7-dynamic-qa-resp-filters.png?alt=media\&token=fd0597b0-4e44-4ea5-be6c-d0e219607d5a)

* Add a Q\&A intent, say, "store" and with the user query "Where is your store? ".&#x20;
* In the Skill messages, add two text responses:
  * "In India, you can find our stores in all major cities - Mumbai, Delhi, Chennai, Bangalore." and apply the "Location - India" response filter.
  * "In the US, our store is located only in New York." and apply the "Location - US" response filter.

### **Step 4: Test your agent**

* In the web channel URL, set the custom\_properties\[office\_city]=Bangalore. Specify the user query in your agent simulator and check if the response of the "Location - India" response filter is received.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5LPJ7RqgctA0djRnpPDM%2Fimage.png?alt=media\&token=4e540401-2756-466c-8d3e-3cc115a5994a)

* &#x20;In the web channel URL, set the custom\_properties\[office\_city]=Boston. Specify the user query in your agent simulator and check if the response of the "Location - US" response filter is received.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F87qDJmDkWf4f9fyXSXSQ%2Fimage.png?alt=media\&token=16aa4f50-3808-403c-82e4-d8361117596f)

* See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties) and [Test your web channel](https://docs.avaamo.com/user-guide/build-agents/configure-agents/deploy/web-channel#test-your-web-channel), for more information.
