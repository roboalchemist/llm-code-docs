# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.3.x/release-notes-5.3.0.md

# Release notes v5.3.0

The Avaamo Conversational AI Platform v5.3.0 minor release includes 4 new features, 6 enhancements, and 4 changes distributed as follows:

* **New features**:
  * [Introducing Dynamic Q\&A skill](#1-introducing-dynamic-q-and-a-skill)
  * [Introducing tagging capability for advanced analytics](#2-introducing-tagging-capability-for-advanced-analytics)
  * [Introducing multiple intent responses ](#3-introducing-multiple-intent-responses)
  * [Introducing new Query insights API](#4-introducing-new-query-insights-api)
* **Enhancements**: This release also includes enhancements related to NLU,  Message insights,  Feedback, and channel components in the platform. See [Enhancements](#enhancements), for more information.
* **Changes**: This release also includes changes related to Skill builder, NLU, and Dialog skill builder components in the platform. See [Changes](#changes), for more information.

## Component-wise distribution

The following table lists the component-wise distribution of new features, enhancements, and changes in the v5.3.0 release:

{% tabs %}
{% tab title="New features " %}
The following lists the usage of the new features across different components in the platform:

| Feature                                                                                                                                    | Components                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Introducing Dynamic Q\&A skill](#1-introducing-dynamic-q-and-a-skill)                                                                     | <ol><li>Add and remove slots in Q\&A intents</li><li>Q\&A skill response -> Add Entities. Show only entities used in the intent.</li></ol>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <p></p><p><a href="#2-introducing-tagging-capability-for-advanced-analytics">Introducing tagging capability for advanced analytics</a></p> | <ol><li>Configure different tags in the agent based on the user intents</li><li>Add and remove tags in Dialog skill responses</li><li>Add and remove tags in Q\&A skill responses</li><li>Add and remove tags in Smalltalk skill response</li><li>Add tags using JS</li><li>View analytics of Top tags</li><li>Query insights -> Filter by tags</li></ol>                                                                                                                                                                                                                                                                                                             |
| <p></p><p><a href="#3-introducing-multiple-intent-responses">Introducing multiple intent responses</a></p>                                 | <ol><li>Configure different user properties in agents on which you wish to apply the response filters</li><li>Configure response filters in agents based on user properties</li><li>Configure dictionaries with response filters</li><li>Add multiple Dialog skill responses for a user intent</li><li>Add and remove filters in Welcome responses</li><li>Add and remove filters in Dialog skill responses</li><li>Add and remove filters in Q\&A skill responses</li><li>Add and remove filters in Intro and Outro Q\&A skill responses.</li><li>Add and remove filters in Smalltalk skill responses</li><li>Query insights -> Filter by response filters</li></ol> |
| <p></p><p><a href="#4-introducing-new-query-insights-api">Introducing new Query insights API</a></p>                                       | <ol><li>Query insight API</li></ol>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| {% endtab %}                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

{% tab title="Enhancements " %}
The following lists the enhancements across different components in the platform:

<table><thead><tr><th width="231">Component</th><th>Enhancement</th></tr></thead><tbody><tr><td><a href="#1-nlu">NLU</a> </td><td><ol><li>Spell correction Improvement </li><li>Better negative query handling</li></ol></td></tr><tr><td><a href="#2-message-insights">Message insights </a></td><td><ol><li>Tone and Sentiments in message insights</li><li>View skill name for ambiguous intents</li><li>Get tone and sentiment attributes in the Context object</li></ol></td></tr><tr><td><a href="#3-feedback">Feedback</a></td><td><ol><li>Add feedback in any skill response using a JavaScript method</li></ol></td></tr><tr><td><a href="#4-channel-type-ahead">Channel</a></td><td><ol><li>Type-ahead (auto-complete) feature in Web, Android, and iOS channels.</li></ol></td></tr></tbody></table>
{% endtab %}

{% tab title="Changes " %}
The following lists the changes across different components in the platform:

<table><thead><tr><th width="216">Component</th><th>Change</th></tr></thead><tbody><tr><td><a href="#1-skill-builder">Skill builder</a></td><td>Removed old Q&#x26;A skill and added a new skill type Dynamic Q&#x26;A. </td></tr><tr><td><a href="#2-dialog-skill-builder">Dialog skill builder</a></td><td>Removed unhandled node This is no longer required at Dialog skill level since there is an Unhandled skill at the agent level.</td></tr><tr><td><a href="#3-nlu">NLU</a></td><td>Changed the disambiguation confirmation prompt when the agent is only showing one intent during disambiguation.</td></tr><tr><td><a href="#4-session-time-out">Session time-out</a></td><td>For security reasons, all the dashboard session, log out (time-out) after 12 hrs of inactivity.</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## New features

### 1. Introducing Dynamic Q\&A skill

In this release, a new skill - **Dynamic Q\&A** has been introduced.&#x20;

Dynamic Q\&A skill is essentially a Q\&A skill with an advanced capability to dynamically add entities and slots for Q\&A intents. All the other functionalities of the existing Q\&A skill are applicable to the Dynamic Q\&A skill also. Adding entities and slots capability to the existing Q\&A skill can lead to considerable migration overhead, hence the existing Q\&A skill is kept as-is and the new concept of adding entities and slots has been introduced in a new skill - Dynamic Q\&A.&#x20;

In the Dynamic Q\&A skill, similar to the Dialog skill, as you enter training phrases for the intent, the platform automatically extracts the slots and includes all the entities in your intent. You can view the entities in the **Entities** tab next to the **Intent** tab in the Intent pop-up window. This feature provides the flexibility to choose and delete the entities that are no longer required. You have a finer control now on the entities that are applicable to the Q\&A intent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEgExylvdTsGoZXgjLy%2F-MEgHfNOQ6ec4B3tVLo-%2Frn-qa-entities-slots.png?alt=media\&token=3801e9b9-3030-4878-b9d1-daaa7c61e434)

See [Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a), for more information.

### 2. Introducing tagging capability for advanced analytics

In this release, a new Analytics board - "Top tags" has been introduced that allows you to analyze the agent's usage via tags. This feature allows business users to create "tags" that can be used to track business metrics cutting across intents and channels. **Example**: You can create a tag called “pension” and include that in all responses across intents that relate to pension.

This feature is useful when you have a particular category of user intent distributed across different skill responses and you wish to assess the usage of those intents in the user-agent interactions. It gives a different perspective of viewing and understanding the user-agent interactions. See [View analytics of top tags](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#top-tags), for more information.

**Example**: In the HR agent, you can have different tags for - Bonus, Employee Referral, Pension, Payroll, Onboarding, Hike, (to name a few) related intents across skill responses in the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEb7JVhWyfGOGEdidRn%2F-MEbOTLbo54cx7C3SM0o%2Frn-top-tags.png?alt=media\&token=0a9189f1-f7fa-430a-9813-d261c93d5fdd)

You can associate tags to all the skill responses (Dialog, Smalltalk, Q\&A) except Answers skill. Also, you can dynamically associate tags to responses using JS. See [Add tags (JS)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js), for more information.&#x20;

In order to use this feature, you must:

1. Configure different tags in the agent based on the user intents in the Agent Configuration -> Tags section. See [Add tags](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-tags), for more information.
2. Add tags to skill responses. See tags details in the following links, for more information:
   * [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#panel-3-messages-tags)
   * [Add tags using JS](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js)

You can also get a closer look into the conversations by filtering the queries using tags in the Query Insights page. This can be useful in debugging if required. See [Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights), for more information.&#x20;

### 3. Introducing multiple intent responses

In this release, a new feature to add multiple skill responses to the same user intent has been introduced. This feature allows you to add filtered responses for a user query based on the user properties such as location, manager status, exempt/non-exempt status. This feature helps in:

* Rapid agent development: You can use the same agent and tailor the responses based on different user properties.
* Providing personalized responses for the same user intent, say, for example, based on the location of the user, or department a user belongs to, or time zone.
* Configuring filtered responses completely in the UI without writing any JS code

**Example**: In an HR agent, consider the user query "When is the year-end bonus paid?". Bonus paid for India and US employees can be different. You can define multiple responses for an intent based on the user's properties so that agent’s response is different for an Indian user and a US user.

|                                                                                                                            India User                                                                                                                            |                                                                                                                              US User                                                                                                                             |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEb_ZkPIFubSO4AD49s%2F-MEbd25joM3Rydr8MrjM%2FScreenshot%202020-08-13%20at%205.07.46%20PM.png?alt=media\&token=6ba16969-da08-4df4-8aa1-15b211887f55) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEb_ZkPIFubSO4AD49s%2F-MEbd66r5gMCehUur0ox%2FScreenshot%202020-08-13%20at%205.11.00%20PM.png?alt=media\&token=1ebba0d3-5709-42be-b117-35da56b25ec4) |

You can add response filters in all the skill responses (Dialog, Smalltalk, Q\&A) except Answers skill.

In order to use this feature, you must:

1. Configure different user properties in agents on which you wish to apply the response filters

   in the Agent Configuration -> User properties section. See [Add user properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.
2. Configure response filters in agents based on user properties in the Agent Configuration -> Response Filter section. See [Add response filters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters), for more information.
3. Configure dictionaries with response filters, if required. See [Add dictionaries](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-dictionaries), for more information.
4. Add response to skill responses. See details about response filters in the following links, for more information:
   * [Build Dialog skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses)
   * [Add questions and answers in Dynamic Q\&A responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers#example-add-response-filters)
   * [Add questions and answers in Smalltalk responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa#example-add-response-filters)
   * [Add questions and answers in Q\&A responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/build-and-manage-q-and-a-skill/add-intents-and-languages#example-add-response-filters)

You can also get a closer look into the conversations by filtering the queries using response filters in the Query Insights page. This can be useful in debugging if required. See [Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights), for more information.

### 4. Introducing new Query insights API

In this release, a new Query insights API has been introduced to get a closer look at the user conversations with the agent.

```javascript
https://cx.avaamo.com/api/v1/agents/{{agent_id}}/query_insights.json
```

You can use this API for debugging purposes and for any other reporting purposes. You can also filter the results using - date-time, intent, user, language, and channels. See [Query insights](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/query-insights), for more information.

## Enhancements

### 1. NLU&#x20;

This release includes the following enhancements in NLU:

#### **Spell correction improvements**

In this release, spell correction has been enhanced to identify and correct the phrase in the user query that is closest to the training data rather than correcting it to the best match.&#x20;

Example: Consider that you have the following data in your agent:

```javascript
Dictionary: lone
Entity types: Loan types -> Personal loan, Housing loan
Skill -> Get loan
Training data -> I want Axis bank personal loan
User query -> I want Axis bank personal lon
```

Consider user query "I want Axis bank personal lon". Note that here best phrase match for "lon" is "lone". However, when the user query is "I want Axis bank personal lon", lon gets corrected to "loan" instead of "lone", since that is closest to the training data.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MFiZqEoBguVBYgTgBz9%2F-MFihXbdN0judaP2WRpP%2Frn-nlu-best-phrase.png?alt=media\&token=0490c1e3-4b1e-4b88-b414-e2fe0de2ec1a)

**Better negative query handling**:&#x20;

In this release, the negative query handling has been improvised to reduce false positives. Example: If you have training data as "I want to order a pizza", then the user query "I do not want to order a pizza" will not match the training data.

&#x20;![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEgHqrs23ddvmQGr8Tg%2F-MEgc3Ia90Sfwe6xpTK5%2Frn-negative-query-handling.png?alt=media\&token=acdee95d-c717-4119-a7e3-ecf469e2926d)

In the previous release, the negative training data was getting matched to positive training data, hence creating false positives.&#x20;

### 2. Message insights

This release includes the following enhancements in Message insights:

#### **Tone and Sentiments in message insights**

In this release, "Message insights" has been enhanced to include tone and sentiment details of a user query by default. This information is available in the context insights and accessible via JavaScript in the flow. You can use user tone and sentiment programmatically to either change flows or respond with appropriate messages as per your business requirement.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEh-SJZPnT2e8inPXun%2F-MEh-fIjx2b8c8TH_SHN%2Frn-nlu-tone.png?alt=media\&token=523d425e-ff5f-4af2-9ffd-264973888c3e)

Avaamo Platform can detect the following tones from the user query:

| Tone      | Example                                   |
| --------- | ----------------------------------------- |
| Anger     | I am having the worst experience with you |
| Fear      | I am worried my card will be misused      |
| Happy     | You are perfect!                          |
| Sad       | this is depressing                        |
| Surprised | Oh my! that is good to know               |
| Urgency   | Hurry up! I wanted it yesterday           |

Avaamo Platform can detect the following sentiments from the user query:

| Sentiment | Example                   |
| --------- | ------------------------- |
| Positive  | I like this agent         |
| Negative  | I hate this agent         |
| Neutral   | I want to open an account |

See [Tone and sentiment](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/tone-and-sentiment), for more information.

In the previous release, the tone and sentiment had to be explicitly enabled in the platform and was not available by default.&#x20;

**View skill name for ambiguous intents**

In this release, the context object has been enhanced to include the skill name of ambiguous intents in the insights when the query goes for disambiguation. You can find the details of the ambiguous intent in `context.insights.ambiguous_intents.` Skill name indicates the skill where the intent belongs to. This helps you to quickly search for the skill using the skill name in the Agent -> Skills page and hence enables you to debug faster.&#x20;

```javascript
{
  "matchedWordCount": 1,
  "intent": "node_intent_node_1",
  "intent_name": "MacPizza Order",
  "skill_name": "MacPizza Order", //newly enhanced
  "score": 1,
  "intent_id": 206310,
  "domain_ids": [
    40369
  ],
  "intent_type": "INLINE::INTENT",
  "document": "I want to order pizza",
  "normalized_document": [
    "want",
    "pizza",
    "order"
  ],
  "bot_key": "3"
}
```

In the previous release, skill name was not available for ambiguous intents, hence locating the intent in the agent skills was tedious, you had to search manually using the intent name.

### 3. Feedback

In this release, the user feedback option has been enhanced to add feedback in any response (Dialog, Q\&A, Smalltalk) using a JavaScript`collectFeedback()`method. See [Add feedback](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-feedback), for an example.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEgfMGxbLcyIifxwRjc%2F-MEgjc1lbLUDDQoXxd4Z%2Frn-collect-feedback.png?alt=media\&token=50d33ee9-2b94-42e8-9bd4-17ab6446b2a4)

In the previous release, the feedback option in Q\&A skill was available only at the skill level and there was no programmatic way to add feedback in any response. With this enhancement, you can choose to disable the Feedback option at the Q\&A skill level and include in only responses that require feedback.&#x20;

### 4. Channel (Type-ahead)

In this release, the customizable parameters in Web, Android, and iOS channels has been enhanced with a **query\_autocomplete\_url** parameter that is used for the type-ahead (auto-complete) feature. The auto-complete feature provides a list of query options to the user as the user starts entering the query in the agent. Using this parameter, you can provide a URL of a JSON file that contains the list of query options.

This feature can reduce false positives and significantly improve accuracy. By presenting the user with a list of available options, it is likely that the user selects one of those options for which accurate curated responses are already available in the agent.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MFA0hudYIlXjb6s60ik%2F-MFA67JS2LUY0l7CxRxX%2Frn-auto-complete.png?alt=media\&token=257e7626-9fbc-40e3-95ef-fe84db051cd8)

See [Auto-complete in Web channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#query-autocomplete-url), for an example.

## Changes

### 1. Skill builder

In this release, the old Q\&A skill in the Skill builder has been removed with a new advanced Dynamic Q\&A skill. Dynamic Q\&A skill is essentially a Q\&A skill with an advanced capability to dynamically add entities and slots for Q\&A intents. See [Add skills to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent) and [Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MGNd4Wu-1855PxSQfxC%2F-MGNg4XNOYKOVCS7nalo%2Frn-skill-builder.png?alt=media\&token=ddb3895b-13ac-4fb6-b89a-d3a6c2a0c96f)

{% hint style="info" %}
**Notes**:

* You can still continue to manage your existing Q\&A skills with the previous Q\&A skill builder and you can use the new Dynamic Q\&A skill to create new Q\&A skills. If you wish to move the old Q\&A skill to the new Dynamic Q\&A skill, then currently the process is manual.&#x20;
* The new capability of [adding multi-intent responses](#3-introducing-multiple-intent-responses) and [tagging responses](#2-introducing-tagging-capability-for-advanced-analytics) is available for the existing Q\&A skill too.&#x20;
  {% endhint %}

### 2. Dialog skill builder

In this release, the default unhandled node in the Dialog skill builder has been removed for new skills. With the 5.x release, since the agent is a container of skills and already includes a built-in Unhandled skill, the default unhandled node is no longer required explicitly in the Dialog skill. Note that the unhandled node for the existing skills is retained as-is.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEgA-5nHrUionzNQExD%2F-MEgD72pBQidYpVyKc-3%2Frn-change-dialog-skill-unhandled.png?alt=media\&token=e2f858d1-a2d7-4732-b95f-9bcfd67a70d3)

### 3. NLU

In this release, the disambiguation confirmation prompt has been changed when the agent is only showing one intent during disambiguation. Instead of saying "Hmm, can you be a little more specific?", it displays a confirmation prompt - "Here is an option I can help with. Can you confirm?".&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEgEFMF7pGwzVgOa47m%2F-MEgEq8HOjA6FJssr2He%2Frn-change-disambiguation.png?alt=media\&token=89268933-d912-4bfa-b6ef-7a605cec331b)

### 4. Session time-out

In this release, for security reasons, all the dashboard sessions log out (timeout) after 12 hrs of inactivity:

* If a user tries to perform any action on the sessions after 12 hrs of inactivity, then the user is redirected back to the login page.&#x20;
* Clicking a link or performing any action on the page or refreshing a page resets the inactivity timer.
