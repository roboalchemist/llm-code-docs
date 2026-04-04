# Source: https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.0.x/release-notes-v6.0.0.md

# Release notes v6.0.0

The Avaamo Conversational AI Platform v6.0.0 release includes 9 new features and 3 enhancements distributed as follows:

**New features:** This release includes the following new features:&#x20;

1. [New enterprise channels](#new-enterprise-channels)
2. [Voice entity model](#voice-entity-model)
3. [Pull updates window](#pull-updates-window)
4. [Changelog API (v2)](#changelog-api-v2)
5. [Built-in functions window](#built-in-functions-window)
6. [New voice profiles](#new-voice-profiles)
7. [Tabular answering](#tabular-answering)
8. [Multilingual answering](#multi-lingual-answering)
9. [Content ingestion in Avaamo Answers using Webhooks](#content-ingestion-in-avaamo-answers-using-webhooks)

**Enhancements**: This release includes enhancements related to the following existing features:

1. [User feedback ](#user-feedback)
2. [Promote pop-up window improvements](#promote-pop-up-window-improvements)
3. [Regression testing](#regression-testing)
4. [Search documents in Answers skill using URL](#search-documents-in-answers-skill-using-url)

{% hint style="danger" %}
**Deprecation notice**: In this release, the Skill -> Configuration -> Language feature is deprecated. See [Deprecation notice](#deprecation-notice), for more information.
{% endhint %}

## Component-wise distribution

The following table lists the component-wise distribution of new features, enhancements, and changes in the v6.0.0 release:

{% tabs %}
{% tab title="New features" %}
The following lists the usage of the new features across different components in the platform:

<table><thead><tr><th width="277.36268105000516">New features</th><th width="484">Components</th></tr></thead><tbody><tr><td><a href="#new-enterprise-channels">New enterprise channels</a></td><td><ul><li>Configuration -> Channels -> MS teams</li><li>Configuration -> Channels -> WeChat  </li><li>Configuration -> Channels -> Nice InContact</li><li>Configuration -> Channels -> Genesys</li><li>Configuration -> Channels -> SIP</li></ul></td></tr><tr><td><a href="#voice-entity-model">Voice entity model</a></td><td><ul><li>Dialog skill -> Implementation -> Add user intent</li></ul></td></tr><tr><td><a href="#pull-updates-window">Pull updates window</a></td><td><p></p><ul><li>Testing -> Actions -> Pull updates</li><li>Staging -> Actions -> Pull updates</li><li>Production -> Actions -> Pull updates</li></ul></td></tr><tr><td><a href="#changelog-api-v2">Changelog API - V2</a></td><td><ul><li>REST API</li></ul></td></tr><tr><td><a href="#built-in-functions-window">Built-in functions window</a></td><td><ul><li>Skill -> Implementation -> Add agent response -> Javascript </li><li>Configuration -> JS Files</li></ul></td></tr><tr><td><a href="#new-voice-profiles">New voice profiles</a></td><td><ul><li>Configuration -> Voice settings -> Synthesis</li><li>Channels -> C-IVR </li><li>Channels -> Genesys</li><li>Channels -> Nice InContact</li></ul></td></tr><tr><td><a href="#tabular-answering">Tabular answering</a> </td><td><ul><li>Answers skill</li></ul></td></tr><tr><td><a href="#multi-lingual-answering">Multilingual answering</a></td><td><ul><li>Answers skill</li></ul></td></tr><tr><td><a href="#content-ingestion-in-avaamo-answers-using-webhooks">Content ingestion in Avaamo Answers using Webhooks</a></td><td><ul><li>Answers skill</li></ul></td></tr></tbody></table>

{% endtab %}

{% tab title="Enhancements" %}
The following lists the usage of enhancements across different components in the platform:

<table><thead><tr><th width="252.9230769230769">Enhancement</th><th width="429.0769230769231">Components</th></tr></thead><tbody><tr><td><a href="#export-user-feedback-in-csv-format">Export user feedback in CSV format</a></td><td><ul><li>Learning -> User feedback</li></ul></td></tr><tr><td><a href="#promote-pop-up-window-improvements">Promote pop-up window improvements</a></td><td><ul><li>Development -> Actions -> Promote</li><li>Testing -> Actions -> Promote</li><li>Staging  -> Actions -> Promote</li></ul></td></tr><tr><td><a href="#regression-testing">Regression testing</a></td><td><ul><li>Test -> Regression Testing</li></ul></td></tr><tr><td><a href="#search-documents-in-answers-skill-using-url">Search documents in Answers skill using URL</a></td><td><ul><li>Answers skill -> Implementation -> Document groups -> Documents</li></ul></td></tr></tbody></table>
{% endtab %}

{% tab title="Changes" %}

<table><thead><tr><th width="300.2039336344995">Component</th><th width="338.03650901798306">Change</th></tr></thead><tbody><tr><td>Skill -> Configuration -> Language</td><td><ul><li>Add language option has been removed.</li><li>Delete language option has been removed.</li></ul><p>Since managing the addition and deletion of languages at the agent level is easier and avoids confusion.</p><p></p><p>You can use Agent -> Configuration -> Language to add languages. At the skill level, you can customize translations for the languages added at the agent level. See <a href="../../../overview-and-concepts/advanced-concepts/language-pack">Language pack</a>, for more information.</p></td></tr><tr><td>Answers API</td><td><p>User access token must be used to authorize the Answers API. </p><p></p><p>See <a href="applewebdata://9891D414-620D-4A48-8416-492A241F5AE1/o/-LpXFbuTM3h40PfxYgao/s/-LpXFTiTgns4Ml77XGi3/~/changes/GcxgyiBDYMbLBVnEyA06/how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Get user access token</a>, for more information.</p></td></tr><tr><td><p>Content ingestion in Answers skill </p><p><br></p></td><td><p>Use valid JSON format for attributes while ingesting the content. With the v6.0 release, strict JSON validation is required to avoid any discrepancy in the data ingested into the system for attribute match. </p><p></p><p>See <a href="applewebdata://FC72E3BB-D6DD-4F39-9AB2-4E7E4D066D06/o/-LpXFbuTM3h40PfxYgao/s/-LpXFTiTgns4Ml77XGi3/~/changes/GcxgyiBDYMbLBVnEyA06/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1">Upload content</a>, for more information.</p></td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## New features

### New enterprise channels

In this release, the following new enterprise channels have been introduced:

* [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams)&#x20;
* [WeChat](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/wechat)
* [Genesys ](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/genesys)
* [NICE inContact](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/nice-incontact)
* [SIP](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sip)

**Microsoft Teams** and **WeChat** are the new text-based channels.&#x20;

**SIP, Genesys,** and **NICE inContact** are the new C-IVR enterprise channels to facilitate voice channel communication.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIDCyqBxnzy8pAU2nYBkO%2FScreenshot%202022-01-28%20at%205.51.39%20PM.png?alt=media\&token=78ea90d5-790a-4059-9e1a-6e1fb2c95038)

When a developer creates UI elements inside the Avaamo platform; for example, Microsoft Teams. the UI elements are converted to Microsoft's teams compatible UI. This allows the developer to seamlessly create a conversation without the need of writing extensive code.

See [Microsoft teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.

### Voice entity model

In this release, a new concept of Voice entity models has been introduced. Voice entity models are pre-built models to precisely detect relevant entities from the user's speech. It is a model built by using millions of actual user utterances combined with domain-specific data.&#x20;

Text-based conversations are not the same as voice-based conversations. It is critical to extract and understand the entities accurately since often it is the starting point of the conversation and it completes the user query. The voice entity model boosts the Avaamo platform's ability to collect crucial elements from users' speech. It helps us to:

* Enhance the accuracy of interpreting user query and hence provides a good user experience
* Accelerates agent development, since the same voice entity models can be used in multiple intent interpretations without having to code.

Voice entity models are available when you define users' intent in C-IVR conversational flow.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FG8L2LOWxpktcpva66Udb%2Fimage.png?alt=media\&token=078e11f7-be6c-4659-b43f-788647fb6f2e)

Few commonly used models include:

* Name
* Date
* Alphanumeric
* Numbers
* Postal Code
* Phone Number
* Email
* Time
* Amount
* Age
* Money

See [Voice entity mode](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/voice-entity-model)l, for more information.

### Pull updates window

In this release, a new **Pull updates** window has been introduced.&#x20;

As the agent progresses in its [lifecycle](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle) (Development, Testing, Staging, Production), updates made to an agent in the previous stage are pulled successively until it reaches production. When updates are pulled, it is critical to know the list of changes being pulled. This helps in evaluating the impact of the change in the current stage.&#x20;

The new **Pull updates** window is displayed when the agent's changes are pulled from a previous stage to the current stage.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FG4fr7PqtPOJ1z8qIhwrr%2Fimage.png?alt=media\&token=a92f0311-14ab-4e8e-8eb2-e98abb72ef54)

In this window, you can:

* Quickly view a list of changes that will be pulled from the previous stage to the current stage changes.&#x20;
* Confirm and accept the changes that are being pulled to the next stage.
* Download the summary of changes in a CSV file for reference and further analysis.

See [Promote and Pull updates](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates), for more information.

### Changelog API (v2)

In this release, a new version of Changelog API has been introduced. This version of Changelog API is a more scalable design that covers a broader range of logs for greater system traceability.

There are several advantages of using the new version of Changelog API:

* Auditing the changes is easier.
* Answers skill and Built-in skill changes are added to the new API.
* Since the new version provides enhanced coverage of tracking events in the agent, it helps in better operational troubleshooting.

See [Changelog API - V2](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api-v2), for more information.

{% hint style="info" %}
**Note**: To ensure backward compatibility, the older version of Changelog API is also supported. See [Changelog API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api), for more information on an older version of this API.
{% endhint %}

### Built-in functions window

In this release, a new **Built-in functions** window has been introduced. This window lists all the out-of-box JS functions available in the Avaamo platform that can be used in your JS code during agent development.

Avaamo platform provides a robust library with a rich set of objects and Javascript functions that can be leveraged to customize and create enterprise skills catering to a wide variety of business requirements across different domains. For an agent developer, it is very useful if the syntax and usage of all such functions are available in the JS editor itself during agent development. This helps in:

* Faster development, since the required functions are accessible within the JS editor itself during agent development.
* Writing JS code with correct syntax, since examples can be copied and hence it is less error-prone.
* Browsing any additional functions that can be of use during the development

The new **Built-in functions** window is available in the JS editor of the following pages:

* Skill -> Implementation -> Add agent response -> Javascript. See [Add skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#javascript), or more information.
* Configuration -> JS Files. See [Add JS files](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-js-files), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZA3B0aHr9pPSWy9bqJih%2Fimage.png?alt=media\&token=d2e4e5b7-d2af-47e3-a8f8-d8987a76a2d6)

In this window you can:

* Search the supported built-in JS functions in the Avaamo Platform.&#x20;
* Copy the example snippets and paste them into the editor.
* Click the documentation link for more in-depth information.&#x20;

See [Built-in functions window](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/built-in-functions-window), for more information

### New voice profiles

In this release, the following new high-quality natural voices have been introduced in the 6.0 release:&#x20;

<table><thead><tr><th width="150">Language</th><th width="580.4285714285713">Voices</th></tr></thead><tbody><tr><td>en-US</td><td><ul><li>George (male)</li><li>Alice (Female)</li></ul></td></tr></tbody></table>

A new persona generates speech that sounds more natural than other text-to-speech systems. It synthesizes speech with more human-like emphasis and inflection on syllables, phonemes, and words.

See [Voice settings -> Synthesis](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings#synthesis), for more information.

### Tabular answering

In this release, Avaamo Answers can now provide responses to user queries from tables present in the ingested documents. With this feature, you can

* Upload documents with a tabular format - HTMLs with tables, Excels and CSVs
* Get responses to user queries from the content available in Excel sheets, CSVs, tables embedded in PDFs, HTML

The following illustration depicts how Avaamo answers can provide answers to a user query from the ingested table content:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDFhonzBjlSekOPb82bw0%2Fanswers-tabular-6.0.png?alt=media\&token=75dfcc10-3c1f-43da-a21a-d0cd800e4c1a)

{% hint style="info" %}
**Note**: Contact Avaamo Support to start using this feature and for more information on repo access and API documentation.
{% endhint %}

See [Tabular answering](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/tabular-answering), for more information.

### Multilingual answering

In this release, you can use Avaamo Answers to ingest documents in the local language and provide responses to user queries from the content available in the local language itself. This helps in:

* Providing a wider reach of your agents. Makes agents more accessible to a broader scope of users.
* Providing more personal experience with your agents since interacting in the local language is more natural and relatable.

The following illustration depicts how Avaamo answers can provide responses to a user query in the local language from the ingested document in the corresponding language:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLCZ3NrkT9mJJQSYc8X9J%2Fimage.png?alt=media\&token=a8c6d970-b701-4252-a860-c4e5f02c368f)

{% hint style="info" %}
**Note**: Contact Avaamo Support to enable Answers for ingesting language-specific documents.
{% endhint %}

See [Multilingual answering](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/multilingual-answering), for more information.

### Content ingestion in Avaamo Answers using Webhooks

In this release, you can ingest content to Answers using any CMS Webhooks or pull content and upload it to the Answers knowledge base.&#x20;

Currently, the way to ingest content is by uploading the documents or the URL in the Answers skill. This process is tedious and time-consuming. Instead, you can use this new feature to configure webhooks to push content to Avaamo Platform using the API or run document parsing repo on a system to ingest content. The new content ingestion utility provides:

* Inbuilt support for indexes such as sitemaps
* Integration with any CMS systems by configuring webhooks
* Support for PDFs > 1000 pages

{% hint style="info" %}
**Note**: Contact Avaamo Support to start using this feature and for more information on repo access and API documentation.
{% endhint %}

See [Content ingestion using Webhooks](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/content-ingestion), for more information.

## Enhancements

### User feedback&#x20;

In this release, the **Learning -> User feedback** page has been enhanced with the following enhancements:&#x20;

* Date range: Allows you to filter user feedback in the specified date range.
* Export: Allows you to export user feedback in CSV format. This can be used as a reference and for further analysis.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F16E5NIxstlpYzHM2qINj%2Fimage.png?alt=media\&token=c7f6c0d9-52af-44da-a372-0dc2ea482491)

See [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback), for more information.

### Promote pop-up window improvements

In this release, the promote pop-up message window has been enhanced with the following details:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FvByiVtcgBBBNTf9sQkuZ%2Fimage.png?alt=media\&token=c1be4770-3691-4555-a24b-565a07eb0ce4)

* A new pop-up UI layout.
* Information on what details are not promoted from one stage to another.
* Take explicit confirmation from the user before promoting the agent from one stage to another stage.

See [Promote and Pull updates](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates), for more information.

### Regression testing

In this release, the **Test -> Regression testing** page has been enhanced to include a new Language column. This is useful when your agent is configured in multiple languages and you wish to know the language that was used to run regression testing.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQFhCGd9vAwRTHswoT4nq%2FScreenshot%202022-02-16%20at%203.04.53%20PM.png?alt=media\&token=aab8f191-7212-4614-ba33-c460f1108053)

See [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing), for more information.

### Search documents in Answers skill using URL

In this release, the search functionality in the **Answers skill -> Implementation -> Document groups -> Documents** page has been enhanced to include searching based on URLs. In the previous release, the document search was limited to document names only.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdDNsPGW2ETsOLMAg3wTy%2Fanswers-enhancement.png?alt=media\&token=4f09d6fa-04da-450d-86a7-8d626b8fec2d)

## Deprecation notice

In order to provide easy maintenance and a consistent approach to managing languages and their translations for an agent, the legacy **Skill -> Configuration -> Language** page is deprecated from the v6.0.0 release onwards.&#x20;

### Why?

Since all the configuration options for an agent are at the agent level, managing the addition and deletion of languages at the agent level is easier and avoids confusion.

### When is the support completely stopped?

This feature will be removed from v6.1.0 onwards.

### What action to take?

No action required

### How to add and manage languages for an agent?

You can use the **Agent -> Configuration -> Language** page to add, delete, and customize language translations at the agent level. See [Language pack](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/language-pack), for more information.
