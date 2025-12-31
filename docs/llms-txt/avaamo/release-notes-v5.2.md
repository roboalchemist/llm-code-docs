# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.2.x/release-notes-v5.2.md

# Release notes v5.2.0

The Avaamo Conversational AI Platform v5.2.0 release includes 1 new feature, 20 enhancements, and 4 changes distributed as follows:

* [New feature](#new-feature): Introduction of 8 new REST APIs.
* [Enhancements](#enhancements): The following lists the number of enhancements across different components in the platform:

| Component                                           | Number of enhancements |
| --------------------------------------------------- | ---------------------- |
| [Skills](#skills)                                   | 1                      |
| [Dialog skill builder](#dialog-skill-builder)       | 6                      |
| [Q\&A skill builder](#q-and-a-skill-builder)        | 3                      |
| [Smalltalk skill builder](#smalltalk-skill-builder) | 3                      |
| [Entity types](#entity-types)                       | 1                      |
| [JS files](#js-files)                               | 1                      |
| [Dictionaries](#dictionaries)                       | 1                      |
| [Insights](#insights)                               | 1                      |
| [Dashboard](#dashboard)                             | 1                      |
| [Skill store](#skill-store)                         | 2                      |

* [Changes](#changes): The following lists the number of changes across different components in the platform:

| Component                                       | Number of changes |
| ----------------------------------------------- | ----------------- |
| [Skills](#skills-1)                             | 1                 |
| [Dialog skill builder](#dialog-skill-builder-1) | 3                 |

## New feature

In this release, 7 new **Agent APIs** have been introduced to get agent details such as agent name, agent description, skills, intents, entity types, and dictionary values. You can use these details for agent analytics and for any other reporting purposes.&#x20;

This release also includes a **Test API** that helps you test bulk user queries in the agent instead of testing one query at a time in the agent simulator. In the response, you can view the insights on how the user’s intent is analyzed and matched in the agent flow for each query. You can use this information to improvise agent training and provide a better user experience.&#x20;

The following table summarizes the list of new REST APIs:

| API                                                                                                                                    | Description                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Agent details](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/agent-details)                      | Gets the agent details such as agent identifier, agent description, skills, entities used across all the skills, and list of custom entity types available in the agent. |
| [Intents](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/intents)                                  | Gets a list of all the dialog inline intents (Training Phrases) and Q\&A intents from the agent.                                                                         |
| [Dialog intents](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/dialog-intents)                    | Gets a list of all the dialog inline intents (Training Phrases) from the agent.                                                                                          |
| [Q\&A intents](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/q-and-a-intents)                     | Gets a list of all the Q\&A intents from the agent.                                                                                                                      |
| [Unhandled queries](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/unhandled-queries)              | Gets a list of all the unhandled queries from the agent. This does not include queries that led to disambiguation responses.                                             |
| [Dictionary values](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/dictionary-values)              | Gets a list of all the dictionary values from an agent.                                                                                                                  |
| [Custom entity type values](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/custom-entity-type-values)        | Gets a list of all entity values from a custom entity type.                                                                                                              |
| [Test user queries in the agent](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/test-user-queries) | Posts the user queries to the agent and gets insights on how the user’s intent is analyzed and matched in the agent flow for each query.                                 |

See [Getting started](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/quick-overview), to download the postman collection.

## Enhancements

The following lists the enhancements across different components in the platform:

| Component                                           | Enhancement                                                                                                                                                                                                                        |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Skills](#skills)                                   | UI support to display the complete skill name in the Skill widget of the Agent -> Skills page.                                                                                                                                     |
| [Dialog skill builder](#dialog-skill-builder)       | <p>Addition of agent simulator in all the pages of Dialog skill builder:</p><ol><li>Getting started  </li><li>Invocation intent </li><li>Implementation </li><li>Language </li><li>JS Errors </li><li>Regression testing</li></ol> |
| [Q\&A skill builder](#q-and-a-skill-builder)        | <p>Addition of agent simulator in all the pages of Q\&A skill builder:</p><ol><li>Getting started  </li><li>Question & Answers</li><li>Language </li></ol>                                                                         |
| [Smalltalk skill builder](#smalltalk-skill-builder) | <p>Addition of agent simulator in all the pages of Smalltalk skill builder:</p><ol><li>Getting started  </li><li>Question & Answers</li><li>Language </li></ol>                                                                    |
| [Entity types](#entity-types)                       | Addition of agent simulator in the Entity values page                                                                                                                                                                              |
| [JS files](#js-files)                               | Addition of agent simulator in the Edit JavaScript page                                                                                                                                                                            |
| [Dictionaries](#dictionaries)                       | Addition of agent simulator in the Words page                                                                                                                                                                                      |
| [Insights](#insights)                               | Addition of skill name in the message insights.                                                                                                                                                                                    |
| [Dashboard](#dashboard)                             | Optimized dashboard to work with a specific screen resolution                                                                                                                                                                      |
| [Skill store](#skill-store)                         | <ol><li>Search skills in skill store using skill description</li><li>Auto-pick entities during skill publishing</li></ol>                                                                                                          |

### Skills

In this release, the Skill widget in the Agent -> Skills page has been enhanced to support the display of the complete skill name. This helps you to clearly search and identify the skills with longer names. Note that the platform allows you to have skill names with a maximum of 49 characters.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8QB7mnhfpmUx1FkAQS%2F-M8QC1_Q5sKI8Ao32ejH%2Fwhatsnew-skillname.png?alt=media\&token=831cb828-78a3-4d10-bd1d-299fbfa9f691)

In the previous release, the skill name upto only 10 characters was displayed in the Skill widget of the Agent -> Skills page. Hence, it was difficult to identify the skills with names of more than 10 characters as it was not completely visible in the UI.

### Dialog skill builder&#x20;

In this release, the following pages in the Dialog skill builder have been enhanced to include the agent simulator at the bottom-right corner of each page:

1. Getting started &#x20;
2. Invocation intent&#x20;
3. Implementation&#x20;
4. Language&#x20;
5. JS Errors&#x20;
6. Regression testing

This feature helps you to test your agent using the agent simulator from any page available in the Dialog skill's left navigation pane without navigating back to the agent page.

**Few examples are listed below**:

* **Test invocation intent**: You can add new invocation intents to your Dialog skill and test the agent using the agent simulator from the **Invocation intent** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8RJJ1a8MLRWISRp5wZ%2F-M8RLyyjGDV_rptqoYih%2Fwn-agent-chat-dialog.png?alt=media\&token=d0fb696e-44c3-4a40-95df-b2ba4d2dfa14)

* **Test dialog flow**: You can build a multi-turn conversational flow in your Dialog skill and test agent using the agent simulator from the **Dialog Designer** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8RJJ1a8MLRWISRp5wZ%2F-M8RM_556GYHvnB6lJ35%2Fwn-agent-chat-dialog-flow.png?alt=media\&token=c6441d9e-68c3-46ec-8ba8-54367bd65c97)

In the previous release, after any change to the Dialog skill, you had to navigate back to the agent page to test the agent.

### Q\&A skill builder

In this release, the following pages in the Q\&A skill builder have been enhanced to include the agent simulator at the bottom-right corner of each page:

1. Getting started &#x20;
2. Question & Answers
3. Language&#x20;

This feature helps you to test your agent using the agent simulator from any page available in the Q\&A skill's left navigation pane without navigating back to the agent page.

**Example**: You can add new questions and answers to your Q\&A skill and test the agent using the agent simulator from the **Questions & Answers** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M89otMKn5GQ3aQocWFV%2F-M8A95NRB0dzZd1SK3nL%2Fwn-agent-chat-qa.png?alt=media\&token=07f08001-e30f-48ad-8498-4fff41dfbf83)

In the previous release, after any change to the Q\&A skill, you had to navigate back to the agent page to test the agent.

### Smalltalk skill builder

In this release, the following pages in the Smalltalk skill builder have been enhanced to include the agent simulator at the bottom-right corner of each page:

1. Getting started &#x20;
2. Question & Answers
3. Language&#x20;

This feature helps you to test your agent using the agent simulator from any page available in the Smalltalk skill's left navigation pane without navigating back to the agent page.

**Example**: You can add new questions and answers to your Smalltalk skill and test agent using the agent simulator from the **Questions & Answers** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8Q3bhzibpssYIfHIAh%2F-M8Q3wGZRxEMyrgs3r3v%2Fwhatsnew-smalltalk-qa.png?alt=media\&token=0604836b-23e8-436b-a19b-d1b62db8cdae)

In the previous release, after any change to the Q\&A skill, you had to navigate back to the agent page to test the agent.

### Entity types&#x20;

In this release, the **Entity values** page has been enhanced to include the agent simulator at the bottom-right corner of the page. This helps you to make changes (add, update, delete) to the entity values and test query using the agent simulator from the **Entity values** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8RMnN-FALfopgxuxgi%2F-M8RNBHweoaM3aitDb_Q%2Fwn-agent-chat-entity-values.png?alt=media\&token=d2f0aa22-5f41-4104-a4c8-a19ba19334a9)

In the previous release, after any change to the entity values, you had to navigate back to the agent page to test the agent.

### JS files

In this release, the **Edit JavaScript** page has been enhanced to include the agent simulator at the bottom-right corner of the page. This helps you to make changes (add, update, delete) to the JavaScript files and test user queries using the agent simulator from the **Edit JavaScript** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8PSrEkoN1Uob7YyiCL%2F-M8PajEsMH6kMC3FJfz3%2Fwhatsnew-edit-js-simulator.png?alt=media\&token=b6f3de12-acf3-4bf7-9eb2-4fc52b105fba)

In the previous release, after any change to the JavaScript, you had to navigate back to the agent page to test the agent.

### Dictionaries

In this release, the **Words** page has been enhanced to include the agent simulator at the bottom-right corner of the page. This helps you to make changes (add, update, delete) to the values and test user query using the agent simulator from the **Words** page itself without navigating back to the agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M89otMKn5GQ3aQocWFV%2F-M8AD7ZvRPEnV66gs6LK%2Fwn-agent-chat-dictionary.png?alt=media\&token=2cfe0456-ab06-4cc1-88ff-9f9df1dded2e)

In the previous release, after any change to the dictionary values, you had to navigate back to the agent page to test the agent.

### Insights

In this release, the Message Insights has been enhanced to include the skill name attribute. Skill name indicates the skill where the intent belongs to. This helps you to quickly search for the skill using the skill name in the Agent -> Skills page and hence enables you to debug faster.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8Ps4M5md5dpae8ujkH%2F-M8Pvyot7DvIjwKDhoDG%2FScreenshot%202020-05-28%20at%204.14.55%20PM.png?alt=media\&token=db25f0a1-36fe-4dd4-9d31-5dcb7bcc61a1)

In the previous release, you had to manually search for the skill using the skill number in the "Response node" attribute of the insights.

### Dashboard

In this release, the Avaamo Conversation AI Platform dashboard is optimized to work on a specific screen resolution. The window that renders the Avaamo Platform dashboard must have 1366 \* 768 screen resolution for UI components to be displayed correctly.&#x20;

If you have a lower or higher screen resolution, then the display of the UI components in the dashboard can get distorted.&#x20;

See [Basic requirements](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites#basic-requirements), for more information.

### Skill store

In this release, the following are the enhancements related to the skill store:&#x20;

1. [Search skills in skill store using skill description](#search-skills-in-skill-store-using-skill-description)
2. [Auto-pick entities during skill publishing](#auto-pick-entities-during-skill-publishing)

#### **Search skills in skill store using skill description**

In this release, you can search for skills in the skill store using the skill description in addition to the skill name provided at the time of publishing the skill. All the skills in the skill store that contains the search keyword in either skill name or skill description are displayed. See [Search skills in skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store#search-skills-in-skill-store), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M89NJT939eZ875WAH75%2F-M89jy1O2OdCP1ox7Wan%2Fskillstore-search.gif?alt=media\&token=28511775-5165-4f66-afe4-c2d342d9f969)

In the previous release, you were able to search for skills in the "Skill store" only using the skill name provided at the time of publishing the skill.

#### **Auto-pick entities during skill publishing**

In this release, during skill publishing/re-publishing, the entities that are used in the skill are automatically selected and displayed to the user. This feature helps to:

* Ensure that the user always selects the entities that are required for the skill before publishing the skill to skill store and hence reduces the probability of error when the same skill is imported and used in another agent.
* Reduce the manual effort of opening the skill in the new tab, noting down the entities that are required for publishing, and selecting the entities at the time of publishing a skill to skill store.

See [Publish skills to skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store#publish-skill), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M89NJT939eZ875WAH75%2F-M89iavtLOB8sEZjlVbN%2Fpublish-skill-auto-entities.gif?alt=media\&token=73aa5867-cd19-4fb1-852a-fc7ef6966352)

In the previous release, during skill publishing/re-publishing, the entities that were required for a skill had to be selected manually.

## Changes

The following lists the changes across different components in the platform:

| Component                                       | Sub-component                                                                                                                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Skills](#skills-1)                             | <ol><li>Disabled skills</li></ol>                                                                                                          |
| [Dialog skill builder](#dialog-skill-builder-1) | <ol><li>Dialog skill -> Test -> Simulator</li><li>Dialog skill -> Debug -> JS Errors</li><li>Dialog skill -> Debug -> Debug logs</li></ol> |

### Skills

In the release, the UI of the disabled skill widget has been changed which helps to easily identify the disabled skills in the Agent -> Skills page. All the text and icons in a disabled skill widget are in a shade of grey in addition to the Disabled text at the top-right corner.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8j7tQCWoDjyEveAz1k%2F-M8j8u8xEd-YNdmnhMsv%2Fwhatsnew-disabled.png?alt=media\&token=a8ce3d18-77e6-4499-ab08-1ec61436d04f)

In the previous release, there was not much visual identification for disabled skills apart from the Disabled text that was displayed at the top-right corner.

### Dialog skill builder

The following table summarizes the changes to the existing behavior in the v5.2.0 release:

| Component                           | Existing behavior                                 | Changed behavior                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dialog skill -> Test -> Simulator   | Opens Dialog skill simulator                      | <p>Opens the agent simulator that helps you to </p><p>test your dialog flow in the agent as and when you build it.</p>                                                                                                                                                                                                                   |
| Dialog skill -> Debug -> JS Errors  | Displays only the JS Errors related to the skill. | <p>Since the agent simulator is available in all pages of the Dialog skill, this is no longer relevant.</p><p> JS Errors page is already available in  </p><p>the Agent --> Debug -> JS Errors. </p><p>Hence, the Dialog skill -> Debug -> JS Errors page is blank in the current release and will be removed in the future release.</p> |
| Dialog skill -> Debug -> Debug logs | Displays the debug logs of only the current skill | Displays the debug logs of not only the current skill but also includes debug logs available at the agent level.                                                                                                                                                                                                                         |
