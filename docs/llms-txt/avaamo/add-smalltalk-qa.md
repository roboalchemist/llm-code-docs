# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa.md

# Add questions and answers

In the **Customize Smalltalk** section of the Smalltalk skill, you can add user intents (questions) and skill responses (answers) manually or by importing a CSV file with the questions and answers. See [Import Smalltalk,](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/perform-common-actions#import-smalltalk) for more information.&#x20;

{% hint style="success" %}
**Key Points**:&#x20;

* Multiple developers can add questions and answers simultaneously in the same Smalltalk skill, encouraging faster development of the skill. As a best design practice, it is recommended to distribute a set of intents among developers, so that it is easy to maintain and manage and results in seamless collaboration.
* See [Parallel development (QA & Smalltalk) FAQs](https://docs.avaamo.com/user-guide/ref/parallel-development-qa-and-smalltalk-faqs), for common FAQs around parallel development of QA and Smalltalk skills.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MZvH2Oclrimfh_ZuRvD%2F-MZv_19ngfA1GOsaAn6I%2Fst-add-new.png?alt=media\&token=7f058e5c-e6f8-457e-a9d4-320f7b57ad9f)

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can manage a skill immediately after creating the skill. See [Create new Smalltalk skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/create-new-knowledge-base), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

## **Add questions and answers**

* In the **Smalltalk** skill page, navigate to **Implementation -> Customize Smalltalk**

  option in the left navigation menu.&#x20;
* By default, the response of the default language as specified in the agent configuration is displayed.&#x20;
* Select the channel for which you wish to add the Q\&A. Using this feature, you can add different customized responses for different channels as per your requirement. If you have deployed your agent in a specific channel for which you have not configured any response, then the response as specified in the "Default" option is considered. **Example**: Consider that you have deployed your agent in Web, Android, and iOS channels and you have configured responses only for the Android channel. For the Web and iOS channels, the responses as specified in the **Default** option are displayed.

{% hint style="info" %}
**Note**: Only those channels that are enabled for your account or company are displayed in the Channel dropdown. If you wish to enable a channel, then contact Avaamo Support for further assistance.
{% endhint %}

* If you have configured languages in your skill, select the language in which you wish to add the response. By default, the response of the default language as specified in the agent configuration is displayed. See [Add language-specific responses](https://docs.avaamo.com/user-guide/how-to/build-skills/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#language-specific-responses), for more information.

{% hint style="success" %}
**Key Point:** With the ability to add channel-specific and language-specific skill responses, you can now add responses specific to each channel-language combination. Example: You can add a response specific to the Android channel in the French language.
{% endhint %}

* Click the **plus icon** to add user questions and the skill responses (answers).&#x20;
* Add required [Intent](#intent) and [Prompt details](#prompt-details).&#x20;
* Click **Save** to save the Q\&A.
* You can continue to add questions and responses as required.

Your Smalltalk skill is ready for testing. See [Test Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/test-smalltalk-q-and-a), for more information. You can also add languages, edit or delete Q\&A, and import Smalltalk. See [Perform common actions](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/perform-common-actions), for more information.

{% hint style="info" %}
**Note**: If you have added response filters to the Smalltalk skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

### Intent

In the **Intent** tab, specify the following details:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0vgkDAwrkLKa8IPWd%2F-Mb0w80ol-RCZF1IQawt%2F5.7-smalltalk-qa.png?alt=media\&token=511aaaa0-26df-4559-a569-1ab252947523)

<table><thead><tr><th width="157">Parameters</th><th width="392">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p></td><td align="center">20 characters</td></tr><tr><td>Intent name</td><td>Indicates the name of the intent. Each intent name must be unique within the agent.</td><td align="center">191 characters</td></tr><tr><td>User intent matches</td><td><p>Indicates the training data or variations for the intent. Type the required training data and press enter. You can add multiple training data to the intent as required. </p><p></p><p>There is no limit on the number of training data or training phrases that can be added to an intent. It is recommended that you follow the recommended best practices for adding training data. See <a href="../../../../design-skill#intent-and-training-phrases-training-utterances-or-training-data">Intents and training data</a>, for more information.</p></td><td align="center">Each of 300 characters</td></tr></tbody></table>

{% hint style="info" %}
**Notes**:

* If you have multiple intents with exactly the same training data, then the latest intent response is displayed to the user.

* If you have multiple intents with similar training data, then the query goes for disambiguation.

* The **Smalltalk** response is displayed only when the user query (including punctuations) exactly matches the training data provided in the Smalltalk.
  {% endhint %}

* You can also add intents to capture emojis and respond to emoji responses as required.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0xIuCv43WzcMb290W%2F-Mb0xUu7WDxDAUtNIyn9%2Fsmalltalk-emojis.png?alt=media\&token=f46a4378-3d40-4e92-b44a-b9701874e096)

### Prompt details

In the **Prompt** **details** tab, specify the skill responses (answers) to user questions. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information. Note that [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings) options available for the Dialog skill are not applicable to the Smalltalk skill

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FU7xAYhFQuJ51r8Zl1TrE%2F6.2-response-types-smalltalk.png?alt=media\&token=713bd249-b987-4308-9d79-9c6faad075b3)

## Example: Add response filters

Consider that you wish to display different Smalltalk greeting messages for different users based on their location:

| **User query**    |                    **Indian user**                    |                       **US user**                       |
| ----------------- | :---------------------------------------------------: | :-----------------------------------------------------: |
| How was your day? | Namaste. Doing great so far. Hope you are doing well. | Hey there. Doing great so far. Hope you are doing well. |

### Step 1: Add user properties&#x20;

Add a user property "Office City". See [Add user properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

### Step 2: Add response filters

Configure two response filters, one for "Location - India" and another for "Location - US". Add values for each of these as required. See [Add response filters](https://docs.avaamo.com/user-guide/build-agents/configure-agents/add-response-filters#add-response-filters), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF-PS4TjwPpFPD93KH2%2F-MF-f6gM2ilJ17lWw4ca%2Fconfig-response-filters.png?alt=media\&token=47771aec-fa5d-42ba-a3c8-03d3c88fd039)

### **Step 3**: **Add response filters to Smalltalk response**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0yIUCP7kkZLGjJbZL%2F-Mb0yRXN7g0O5c4qhQlZ%2F5.7-smalltalk-add-prompt-details.png?alt=media\&token=f6c6c7c9-d9b4-468c-8e7b-76f8fbcf454c)

* Add a Smalltalk intent, say, "greeting" and with the user query "How was your day? ".&#x20;
* In the Skill messages, add two text responses:
  * "Namaste. Doing great so far. Hope you are doing well." and apply the "Location - India" response filter.
  * "Hey there. Doing great so far. Hope you are doing well." and apply the "Location - US" response filter.

### **Step 4: Test your agent**

* In the web channel URL, set the custom\_properties\[office\_city]=Bangalore. Specify the user query in your agent simulator and check if the response of the "Location - India" response filter is received.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0jPxTr1rVVK6hraOlsVE%2Fimage.png?alt=media\&token=767a44ec-731e-442c-a162-e7be5e41bd6f)

* In the web channel URL, set the custom\_properties\[office\_city]=Boston. Specify the user query in your agent simulator and check if the response of the "Location - US" response filter is received.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXtoCU3sQJAXIXXsHBbKl%2Fimage.png?alt=media\&token=969dedeb-dbe3-408c-ab6f-488189f01bf3)

* You can also set custom properties using User.setProperty. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties) and [Test your web channel](https://docs.avaamo.com/user-guide/build-agents/configure-agents/deploy/web-channel#test-your-web-channel), for more information.
