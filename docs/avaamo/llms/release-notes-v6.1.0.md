# Source: https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.1.x/release-notes-v6.1.0.md

# Release notes v6.1.0

The Avaamo Conversational AI Platform v6.1.0 release includes 1 new feature, 7 enhancements, and 3 changes distributed as follows:

**New feature:** This release includes the introduction of a new agent referred to as **Universal agents.** See [What's new in v6.1.0?](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.1.x/whats-new-in-v6.1.0) for more information on the newly introduced features in v6.1.0.

**Enhancements**: This release includes enhancements related to the following existing features:

1. [Customizing the User feedback form](#customizing-the-user-feedback-form)
2. [Improvements in JS error email notifications](#improvements-in-js-error-email-notifications)
3. [Export errors from the JS errors page](#export-errors-from-the-js-errors-page)
4. [UI enhancements for language translations](#ui-enhancements-for-language-translations)
5. [Configuration options for Tabular answering ](#configuration-options-for-tabular-answering)
6. [Disambiguation between Answers skills](#disambiguation-between-answers-skills)
7. [Query Analyzer (QA) permission enhancements](#query-analyzer-qa-permission-enhancements)

**Changes:** This release includes changes related to the following existing features:

1. [Errors count on the home page](#errors-count-on-the-home-page)
2. [Language configuration for skill](#language-configuration-for-skill)
3. [Unhandled query analyzer name change](#unhandled-query-analyzer-name-change)

## Component-wise distribution

The following table lists the component-wise distribution of new features, enhancements, and changes in the v6.1.0 release:

{% tabs %}
{% tab title="New features" %}

| New feature                                                                                                            | Component                                                    |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [Universal agent](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.1.x/whats-new-in-v6.1.0) | <ul><li>Dashboard -> Create -> New universal agent</li></ul> |
| {% endtab %}                                                                                                           |                                                              |

{% tab title="Enhancements" %}

| Enhancements                                                                                  | Component                                                          |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [Customizing the User feedback form](#customizing-the-user-feedback-form)                     | <ul><li>Agent -> Configuration -> Custom feedback</li></ul>        |
| [Improvements in JS error email notifications](#improvements-in-js-error-email-notifications) | <ul><li>Configuration -> Settings -> Email notifications</li></ul> |
| [Export errors from the JS errors page](#export-errors-from-the-js-errors-page)               | <ul><li>Agent -> Debug -> JS errors</li></ul>                      |
| [UI enhancements for language translations](#ui-enhancements-for-language-translations)       | <ul><li>Skill message response pop-up window</li></ul>             |
| [Configuration options for Tabular answering ](#configuration-options-for-tabular-answering)  | <ul><li>Answers skills -> Configuration</li></ul>                  |
| [Disambiguation between Answers skills](#disambiguation-between-answers-skills)               | Agent with multiple Answers skills enabled.                        |
| [Query Analyzer (QA) permission enhancements](#query-analyzer-qa-permission-enhancements)     | <ul><li>Agent -> Monitor -> Query analyzer</li></ul>               |
| {% endtab %}                                                                                  |                                                                    |

{% tab title="Changes" %}

| Change                                                                        | Component                                                                                                                                                            |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Errors count on the home page](#errors-count-on-the-home-page)               | Dasboard -> Agents page                                                                                                                                              |
| [Language configuration for skill](#language-configuration-for-skill)         | <ul><li>Agent -> Configuration -> Language</li><li>Skill -> Configuration -> Language</li><li>Node response window </li><li>Import skills from Skill store</li></ul> |
| [Unhandled query analyzer name change](#unhandled-query-analyzer-name-change) | <ul><li>Agent -> Monitor -> Query analyzer</li></ul>                                                                                                                 |
| {% endtab %}                                                                  |                                                                                                                                                                      |
| {% endtabs %}                                                                 |                                                                                                                                                                      |

## Enhancements

### Customizing the User feedback form

In this release, an enhanced feature to customize the **User feedback** form using Javascript (JS) code has been included. This enhancement helps to:

* Build user feedback forms that are robust and intuitive. You can now create a custom feedback form by leveraging the rich set of objects and functions in the Avaamo Platform. Currently, you can create a Custom user feedback form using Cards only. See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card), for more information.
* Enhance the way in which you can collect feedback from the users. Since the feedback form can now be tailored to suit your business requirements, it enables you to collect relevant and effective feedback from users. The collected feedback can be used to significantly enhance the experience of the user when interacting with your agent.&#x20;
* Create different custom feedback forms for both positive and negative feedback.

The following is an illustration of a custom user feedback form that is displayed for providing positive feedback:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ffz7IiS6fAcQkUjLiT764%2F6.1-custom-feedback-example-new.png?alt=media\&token=40528613-9ab1-4e5a-9355-d3a9a16a8c0e)

{% hint style="info" %}
**Note**: This enhancement is available for the Web, Android, and iOS channels.&#x20;
{% endhint %}

A new **Feedback** tab has been added on the left panel to the **Agent -> Configuration** section. Using this tab, you can customize the feedback form that is displayed for both positive and negative feedback. See [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback), for more information.

### Improvements in JS error email notifications&#x20;

In this release, many improvements have been made to the email notifications that are sent when JS errors are encountered during agent interactions with users. These improvements provide more insight into the errors and help you identify and troubleshoot the errors quickly.&#x20;

The following lists the improvements in the JS error email notification:

* The stage of the agent in which the error has occurred.&#x20;
* A link to the JS errors page.
* The errors and the corresponding details of each error.
* An option to send an email to the agent owners is provided.&#x20;

The following illustration depicts a JS error email notification of an agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIgDzfu10GI4xGe7lE06A%2F6.1-js-errors-email.png?alt=media\&token=4c5dcf51-92b9-458d-ad5e-83169410bc5c)

See [Notifications](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#notifications) for more information.

### Export errors from the JS errors page&#x20;

In this release, the **Debug -> JS errors** page has been enhanced to allow you to **filter and export errors** from the JS errors page to a CSV file. The exported CSV can be used for further analysis and as a reference if required. This enhancement comes with a few other improvements to the JS errors page.

Other improvements in the JS errors page:

* **Date range**: You can filter the error list to selectively view errors that only occurred within a certain date range. The maximum allowed date range is upto 90 days from the current date.&#x20;
* **Pagination:** Use pagination to smoothly navigate and view JS errors.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F79ehJsPwj163Ks7ifay2%2FScreenshot%202022-05-11%20at%2011.03.17%20AM.png?alt=media\&token=ffca54ed-137d-4470-bd86-3d88825c9790)

See [JS Errors](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/js-errors) for more information.

### UI enhancements for language translations

In this release, there are a few UI enhancements related to language translations in the Skill response pop-up window. These enhancements help to:

* **Easily identify custom and system translations**: In this release, the background color of the skill response text area gets changed from white to blue for custom-translated text. This helps in easy identification of custom vs system-generated translations. It offers a simpler way to indicate custom-translated text.
* **Reset any custom-translated text to system-generated translation**: In this release, the UI of the skill response pop-up window has been enhanced to include a button in the skill response area that allows you to reset the custom translation to the system default translation.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FP9slQNIyz6TUnRhFMKWG%2F6.1-lang-reset.png?alt=media\&token=68fdfbd5-323e-4a6d-8272-2089908d5145)

In the earlier releases, it was very difficult to identify whether the text was a system-translated text versus custom-translated text. Also, there was no easy way to reset any custom-translated text to system-generated text in the Skill response pop-up window.

See [Language-specific responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#language-specific-responses), for more information.

### Configuration options for Tabular answering&#x20;

In this release, tabular answering in Answers has been enhanced with the following two configuration options:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcM9HcRFAYXYGDEU8esml%2F6.1-tabular-answering.png?alt=media\&token=c4cc38b9-1533-4db6-bcd1-1aabd9115315)

* [Display generative answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#display-generative-answer): Generate a plain text response using the information extracted from the table - making the response more conversational and easily understandable. For example, consider that the response to the query 'what is the IPO of burger king' is in a table. When this user query is posted to the agent, the response is extracted from the table and displayed as a sentence. The corresponding table from which the information is extracted is displayed below the generated sentence.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkZkskVd0xm77hziOZlQ1%2F6.x-display-generative-answer.png?alt=media\&token=599a47d6-080f-48f0-9358-3d65ffe9b76a)

* [Display single table row](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#display-single-table-row)**:** Extract only the single row that has the response to the user's question and display that row along with the corresponding column names. This allows the user to get a precise response from tables and eliminates the need to scroll through tables to locate information. The following illustration depicts the difference between a full table display versus a single table row display in the Answers response for the same user query

|                                                                                                              Full table                                                                                                             |                                                                                                          Single table row                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFzLEie8bfwh6qtsAdJlB%2F6.x-tabular-answering.png?alt=media\&token=b0081f22-a83d-4862-84f0-b069771cff47) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXQ88xrsqtYZUg4dMipKG%2F6.x-single-table-row.png?alt=media\&token=ec392826-b543-4fcd-9c35-6e8a1f9c42d8) |

### Disambiguation between Answers skills

In this release, the agent can disambiguate between responses from multiple answer skills.&#x20;

When a response to a user query is found in multiple Answers skills, the agent presents the names of the Answers skills that have the response. Based on the Answer skill that the user selects, the corresponding response is displayed. This enhancement allows the user to select a response within a given domain or context.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJJEYYlH0jnpqiimBsPJA%2F6.1-answers-disambiguation.png?alt=media\&token=faea7da6-d351-4b41-906a-4cbdbaba58ea)

### Query Analyzer (QA) permission enhancements

In this release, any user with at-least read-only permission on the agent can submit a QA job. This is useful in production agents, as typically only read-only permissions are provided to the business users. It helps them to run the UQA job to analyze the unhandled queries and further improvise the user experience with the agent. See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions) and [UQA](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/query-analyzer-deprecated), for more information.

Earlier only users with at-least edit permissions were able to submit the UQA job.

## Changes

### Errors count on the home page

In this release, the count of errors for an agent that is displayed on the home page (where agents are listed) is the count of the errors that occurred only in the past 90 days from the current date.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FuMWjlRQuhwGjVEupIBjg%2FScreenshot%202022-05-11%20at%2011.07.35%20AM.png?alt=media\&token=9d587a53-cd96-43ed-8609-697042c144f9)

In the previous release, the error count was the total number of errors recorded during the lifetime of the agent.&#x20;

### Language configuration for skill

In order to provide easy maintenance and a consistent approach to managing languages and their translations for an agent, language configuration at the skill level is removed. Earlier, this configuration was done using the legacy **Skill -> Configuration -> Language** page. This configuration was deprecated in release 6.0. With this release, it is completely removed.

**For new implementations**

For all languages added at the agent level, corresponding translations for skills are automatically generated and made available. Languages and custom translations can only be added at the agent level and not at the skill level. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on how to add and manage languages at the agent level.

**For existing skills**

* For skill-level languages that are supported at the agent level, the custom translations available at the skill level are migrated to the agent level after the upgrade.&#x20;
* In cases where custom translation for specific sentences or text is available at both the skill level and agent level, the agent-level translation is given priority.&#x20;
* Note that custom node-level translations of the skill level are retained as-is, even when the language is not available at the agent level. Later, when the specific language is added to the agent, node-level translations are given priority.

**Importing skills**

* When importing a skill, only translations of those languages that are supported by the agent are imported. If you wish to import the skill language that is not in the agent, then you must first add the language to the agent and then import the skill.
* In cases where custom translation for specific sentences or text is available at both the skill level and agent level, the agent-level translation is given priority.
* Since an imported skill language is considered only when the language is a part of the agent configuration, any node-level translations of the languages that are not a part of the agent are not imported either.
* See [Import and Re-import skills](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills), for more information.

### Unhandled query analyzer name change

In this release, the name of the **Unhandled query analyzer** in the **Agent -> Learning** section has been updated to **Query analyzer**, as it is used to analyze all queries and not just unhandled queries. Note that this is only a name change and there is no functionality impact with this change.

See [Query analyzer](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/query-analyzer-deprecated), for more information.&#x20;
