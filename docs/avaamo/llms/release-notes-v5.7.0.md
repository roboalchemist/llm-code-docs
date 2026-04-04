# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.7.x/release-notes-v5.7.0.md

# Release notes v5.7.0

The Avaamo Conversational AI Platform v5.7.0 release includes 6 new features, 5 enhancements, and 7 changes distributed as follows:

**New features:** This release includes the following new features:&#x20;

1. [Web channel v2.0](#web-channel-v2.0)
   * [Deploy "one agent" across multiple web and mobile channel instances](#deploy-one-agent-across-multiple-web-and-mobile-channel-instances)
   * [Revamped layout and configurations in web and mobile channels](#revamped-layout-and-configurations-in-web-and-mobile-channels)
2. ["Voice-enabled" assistants](#voice-enabled-assistants-in-web-and-mobile-channels)
   * [Enable voice in the web and mobile channel](#enable-voice-in-the-web-and-mobile-channels)
   * [Add "Voice response" for voice-enabled assistants in web and mobile channels](#add-voice-response-for-voice-enabled-web-and-mobile-assistants)
   * [Configure voice hints for voice-enabled assistants in web and mobile channels](#configure-voice-hints-for-voice-enabled-web-and-mobile-assistants)
   * [Configure playback voice for voice-enabled assistants in web and mobile channels](#configure-playback-voice-for-voice-enabled-web-and-mobile-assistants)
3. ["Language" analytics board](#language-analytics-board)
4. [New analytics filters](#new-analytics-filters)
5. [Download PDF ](#download-pdf)
   * [Download analytics boards in PDF file](#download-analytics-board-in-pdf-file)
   * [Download user journey in PDF file](#download-user-journey-in-pdf-file)
6. [OAuth2 authorization in custom live agent](#oauth2-authorization-in-the-custom-live-agent-system)

**Enhancements**: This release includes enhancements related to the following existing features:&#x20;

1. [Analytics date filters](#analytics-date-filters)
2. [Skill and intent identifiers ](#skill-and-intent-identifiers)
3. [Regression testing - Disambiguation scenarios](#regression-testing-disambiguation-scenarios)
4. [Regression testing - Answers skill scenarios](#regression-testing-answers-skill-scenarios)
5. [Regression testing - Performance metrics](#regression-testing-performance-metrics)

**Changes:** This release includes changes related to the following existing features:&#x20;

1. [Regression testing](#regression-testing)
2. [User roles](#user-role-api-access)
3. [Agent voice hints](#agent-voice-hints-for-c-ivr)
4. [JS errors ](#js-errors)
5. [Default scroll in the web channel](#default-scroll-in-web-channel)
6. [Agent configurations](#agent-configurations)
7. [Persistent menu](#persistent-menu)
8. [Entity structure in context.insights object](#entity-structure-in-context.insights-object)

{% hint style="danger" %}
**Deprecation notice**: In this release, the "Export regression file" feature from the "Query insights" page is deprecated. See [Deprecation notice](#deprecation-notice), for more information.
{% endhint %}

## Component-wise distribution

The following table lists the component-wise distribution of new features, enhancements, and changes in the v5.7.0 release:

{% tabs %}
{% tab title="New features" %}
The following lists the usage of the new features across different components in the platform:

<table><thead><tr><th width="310.7449275362319">New features</th><th width="467">Components</th></tr></thead><tbody><tr><td><a href="#deploy-one-agent-across-multiple-web-and-mobile-channel-instances">Deploy "one agent" across multiple web and mobile channel instances</a></td><td><ul><li>Configuration -> Channels -> Web  </li><li>Configuration -> Channels -> Android  </li><li><p>Configuration -> Channels -> </p><p>iOS </p></li></ul></td></tr><tr><td><p></p><p><a href="#revamped-layout-and-configurations-in-web-and-mobile-channels">Revamped layout and configurations in web and mobile channel instances</a></p></td><td><ul><li>Configuration -> Channels -> Web</li><li>Configuration -> Channels -> Android  </li><li><p>Configuration -> Channels -> </p><p>iOS </p></li></ul></td></tr><tr><td><a href="#enable-voice-in-the-web-and-mobile-channels">Enable voice in the web and mobile channel</a></td><td><ul><li>Configuration -> Channels -> Web</li><li>Configuration -> Channels -> Android  </li><li><p>Configuration -> Channels -> </p><p>iOS </p></li></ul></td></tr><tr><td><p></p><p><a href="#add-voice-response-for-voice-enabled-web-and-mobile-assistants">Add "Voice response" for voice-enabled web and mobile assistants</a></p></td><td><ul><li>Skill message response in Dialog skill</li><li>Skill message response in Dynamic Q&#x26;A skill</li><li>Skill message response in Smalltalk skill</li><li>All built-in skill message response -> Greetings skill and Unhandled skill</li></ul></td></tr><tr><td><a href="#configure-voice-hints-for-voice-enabled-web-and-mobile-assistants">Configure voice hints for voice-enabled web and mobile assistants</a></td><td><ul><li>Configuration -> Voice settings -> Speech recognition</li></ul></td></tr><tr><td><a href="#configure-playback-voice-for-voice-enabled-web-and-mobile-assistants">Configure playback voice for voice-enabled web and mobile assistants</a></td><td><ul><li>Configuration -> Voice settings -> Synthesis</li></ul></td></tr><tr><td><a href="#language-analytics-board">"Language" analytics board</a></td><td><p></p><ul><li>Monitor agents -> Analytics</li><li>Detailed page for Language analytics </li></ul></td></tr><tr><td><a href="#new-analytics-filters">New analytics filters</a></td><td><ul><li>Monitor agents -> Analytics </li><li>Detailed page of each analytics board</li></ul></td></tr><tr><td><a href="#download-analytics-board-in-pdf-file">Download analytics board in PDF file</a></td><td><ul><li>Monitor agents -> Analytics</li><li>Detailed page of each analytics board</li></ul></td></tr><tr><td><a href="#download-user-journey-in-pdf-file">Download user journey in PDF file</a></td><td><ul><li>Monitor agents -> User journey</li></ul></td></tr><tr><td><a href="#oauth2-authorization-in-the-custom-live-agent-system">Configure OAuth2 authorization in the custom live agent system</a></td><td><ul><li>Configuration -> Live agent -> Custom live agent</li></ul></td></tr></tbody></table>
{% endtab %}

{% tab title="Enhancements" %}
The following lists the usage of enhancements across different components in the platform:

<table><thead><tr><th width="228">Enhancement</th><th width="481.53271028037386">Component</th></tr></thead><tbody><tr><td><a href="#analytics-date-filters">Analytics date filters</a></td><td><ul><li><p>Monitor agents -></p><p>Analytics </p></li><li>Detailed page of each analytics board</li></ul></td></tr><tr><td><p></p><p><a href="#skill-and-intent-identifiers">Skill and intent identifiers </a></p></td><td><ul><li>Create or Edit Dialog skill</li><li>Create or Edit Dynamic Q&#x26;A skill</li><li>Create or Edit Smalltalk skill</li><li>Create or Edit Answers skill</li><li>Add or Edit user intents in Dialog skill</li><li>Add or Edit Q&#x26;A in Dynamic Q&#x26;A skill</li><li>Add or Edit Q&#x26;A in Smalltalk skill</li><li>Skill response -> Advanced settings</li><li>Dialog flow designer UI</li><li>Search nodes within Dialog skill implementation</li><li>Flow control statements</li><li>Regression testing</li><li>Query insights</li><li>User journey</li><li>Message insights</li></ul></td></tr><tr><td><a href="#regression-testing-disambiguation-scenarios">Regression testing - Disambiguation scenarios</a></td><td><ul><li>Test -> Regression testing</li></ul></td></tr><tr><td><a href="#regression-testing-performance-metrics">Regression testing - Performance testing</a></td><td><p></p><ul><li>Test -> Regression testing</li></ul></td></tr></tbody></table>
{% endtab %}

{% tab title="Changes" %}

<table><thead><tr><th width="236.4525354746453">Component</th><th width="434.54746452535477">Change</th></tr></thead><tbody><tr><td><a href="#regression-testing">Regression testing</a></td><td><ul><li>"Add validation data" option is removed</li><li>"View results" from the "Actions" column is removed. Use "Download results" instead.</li><li>"View inputs" from the "Actions" column is removed. Use "Download Input CSV" instead.</li><li>"Re-run" option has been relabeled as "Run"</li></ul></td></tr><tr><td><a href="#user-role-api-access">User roles</a></td><td>API access role is removed</td></tr><tr><td><a href="#agent-voice-hints-for-c-ivr">Agent voice hints for C-IVR</a></td><td>Configuration -> Voice hints is removed. Instead use Configuration -> Voice settings -> Speech recognition</td></tr><tr><td><a href="#js-errors">JS errors</a></td><td>Message creation timestamp in the Sender column is removed. Instead, an additional column to indicate error creation time is displayed.</td></tr><tr><td><a href="#default-scroll-in-web-channel">Default scroll in web channel</a></td><td>Default scroll has been changed from "Bottom" to "Top"</td></tr><tr><td><a href="#agent-configurations">Agent configurations</a></td><td>The features in the Agent -> Configurations section has been re-arranged in the alphabetical order for easy of use.</td></tr><tr><td><a href="#entity-structure-in-context.insights-object">context.insights.entities</a></td><td>Each entity in the <code>context.insights</code> object includes metadata details such as entity type, current value, parent entity type. The metadata provides more insights about the entity and can be used for further processing.</td></tr></tbody></table>
{% endtab %}

{% tab title="Deprecated" %}

<table data-header-hidden><thead><tr><th width="233.00365333874566">Deprecated</th><th width="443.99634666125434">Component</th></tr></thead><tbody><tr><td>Deprecated</td><td>Component</td></tr><tr><td><a href="#deprecation-notice">Export regression file</a></td><td>Monitor agents -> Query insights</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## New features

### Web channel v2.0

In this release, a new version of the web channel - **Web channel v2.0** has been introduced. The new version of the web channel is a significant revamp of the existing web channel. It has a refreshed layout and provides many configuration options that make configuring and deploying your agent in the web channels easier.&#x20;

An important feature of **Web channel v2.0** is the ability to deploy the "one" agent across multiple instances of a web channel. Typically, large enterprises can have multiple websites catering to different aspects of the organization. Since all web channels are a part of the same organization, it may be required to deploy the same agent or assistant across different web channels.

The following are the key highlights of **Web channel v2.0**:

* [Deploy "one agent" across multiple web and mobile channel instances ](#deploy-one-agent-across-multiple-web-and-mobile-channel-instances)
* [Revamped layout and configurations in web and mobile channel instances ](#revamped-layout-and-configurations-in-web-and-mobile-channels)

#### Deploy "one agent" across multiple web and mobile channel instances

In this release, you can deploy "one agent" across multiple instances of a [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channel. The following lists a few use cases where this feature can be useful:

**Use-case 1: Add customized layouts**: You can style your agent for each web channel instance separately. See [Theme](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#theme), for more information.

**Use-case 2: Collect unified analytics:** Provide unified analytics cutting across different instances of web channels. See [Channel analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#channels), for more information,

**Use-case 3: Maintain different user sessions:** For security reasons, you can deploy your agent across multiple instances of a web channel with different authentication mechanisms. See [Security](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#security), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbdewKD-CTLPJ6t6nnF%2F-MbdfCq3_Ebv4OpR6-Ov%2F5.7-web-channel-multiple.png?alt=media\&token=09475958-635a-4873-be56-e4e7c45495ff)

See [Deploy in multiple web channel instances](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/deploy-and-test-web-channel) and [Use case analysis](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/overview#use-case-analysis), for more information.

#### **Revamped layout and configurations in** web and mobile channels&#x20;

In the release, the existing  [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channel layout has been significantly revamped. It has a refreshed layout and provides many configuration options that make configuring and deploying your agent in the web and mobile channels easier.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbLx7NO9dcfmjXugtwD%2F-MbLxyQmQMz4AnqRz3dU%2F5.7-web-channel-details.png?alt=media\&token=8d3f5d47-8c8d-4227-ac5b-2b03bec18bae)

The following sections have been introduced:

* [Channel details](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#channel-details): Provide channel name, description, and enable or disable channel as required.&#x20;
* [Theme](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#theme): Customize the look and feel of the agent widget.
* [Agent widget configuration](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#agent-widget-configuration): Configure various customizable parameters such as default locale, user name, scroll behavior (to name a few) for your agent widget.
* [Voice](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice): Enable a voice assistant to your web channel that can engage the users in intelligent conversations by understanding and interpreting the dialects and accents of the users.
* [Deployment](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#deployment): Provides you a script to embed in the website source code for rendering the agent.&#x20;
* [Security](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#security): Configure authentication mechanisms for your agent.
* [Advanced](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#advanced): Provide any other additional customizable parameters and configure auto-complete URL.&#x20;

See [Configure web channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel), for more information.

### "Voice-enabled" assistants in web and mobile channels

{% hint style="info" %}
**Note**: This feature is enabled only on-demand. Contact Avaamo Support, for further assistance.
{% endhint %}

In this release, a new feature to add a **Voice assistant** to your web channel has been introduced. This helps you to engage the users in intelligent conversations by understanding and interpreting the dialects and accents of the users.&#x20;

The following are the key highlights of this feature:

* [Enable voice in the web and mobile channels](#enable-voice-in-the-web-and-mobile-channels)
* [Add "Voice response" for voice-enabled web and mobile assistants ](#add-voice-response-for-voice-enabled-web-and-mobile-assistants)
* [Configure voice hints for voice-enabled web and mobile assistants](#configure-voice-hints-for-voice-enabled-web-and-mobile-assistants)
* [Configure playback voice for voice-enabled web and mobile assistants ](#configure-playback-voice-for-voice-enabled-web-and-mobile-assistants)

#### Enable voice in the web and mobile channels

In this release, you can add a **Voice assistant** to your [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels using **Enable voice** toggle in the **Voice** section of the channel deployment page. This option allows you to enable real-time transcriptions of the agent messages in the selected locale.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbM2454dgPHQJyUC-ax%2F-MbM2LMdsSUQajRYXMPm%2F5.7-web-channel-voice.png?alt=media\&token=6ac826cb-c49c-4981-9ee9-672e3a61a606)

See [Voice](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), for more information.

#### Add "Voice response" for voice-enabled web and mobile assistants&#x20;

In this release, you can add responses specific to voice-enabled assistants in [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels in the **Skill messages -> Prompt details** section.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbpTEmwPjDQw0e4KZ7l%2F-MbpTPStSLzQYqlAw954%2F5.7-skill-message-window-voice-response.png?alt=media\&token=bd79869b-be52-4ad1-8c2a-ac1f4b2cb38b)

This option is available in Dialog, Dynamic Q\&A, Smalltalk, and all built-in skills when you configure agent responses for voice-enabled Web, Android, iOS channels. The following response types are supported in **Voice response**:

* [Agent voice](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#agent-voice)
* [Javascript](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#javascript)
* [Integrations](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#integrations)
* [Delay](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#delay)

See [Voice response](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/skill-message-window-overview#voice-response), for more information.

#### Configure voice hints for voice-enabled web and mobile assistants&#x20;

In this release, you can configure voice hints for voice-enabled assistants in [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels in the **Speech recognition** section of the **Configuration -> Voice settings** page. You can specify certain keywords or phrases as **Voice hints** in the agent configuration that can help in providing better interpretation or recognition of the user response in voice interaction.&#x20;

{% hint style="info" %}
**Note**: Voice hints provided in the **Speech recognition** section is applicable across [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps), and [C-IVR](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone) channel.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mc8rLXHAJlfDmQO9w4I%2F-Mc8sd2ffMMsHumrrV-m%2F5.7-rn-voice-settings-speech.png?alt=media\&token=54469e43-704a-4e48-b4b5-f713a3e0a500)

You can use **Manage hints** to add or remove voice hints for the specific language.  See [Speech recognition](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings#speech-recognition), for more information.

#### Configure playback voice for voice-enabled web and mobile assistants&#x20;

In this release, you can configure playback voice for voice-enabled assistants in [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels in the **Synthesis** section of the **Configuration -> Voice settings** page. This helps to choose a persona for your voice assistants. It adds a personality to your voice assistants.

{% hint style="info" %}
**Note**: Playback voice provided in the **Synthesis** section is applicable across [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channel.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mc8enWKvxJBe9mPu9Yx%2F-Mc8p3Df-mhSmDA-ZN__%2F5.7-rn-voice-settings.png?alt=media\&token=a8a5b4df-8248-49ae-8676-b624694519f8)

Each language has a different set of voice personas that you can choose from. Select the persona from the options provided in the **Voice - Playback voice** section. See [Synthesis](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings#synthesis), for more information.

### "Language" analytics board

In this release, a new Analytics board - "Language" has been introduced. This feature allows business users to track business metrics cutting across different languages configured in your agent. It provides deeper insights into the user query in each language.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbL3zI8INWa5NUZS-qf%2F-MbL4QJjXZltH0aYW8Kn%2F5.7-analytics-languages.png?alt=media\&token=f3b6da4d-7cb1-4f14-8537-ddcccb7b7bc0)

See [Language analytics board](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#languages), for more information.

### New analytics filters

In this release, a new set of additional filters such as Channel, Language, Intent type, Intent, and Tag have been introduced in the **Analytics** page:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbKYHNTR2tBn88F80K8%2F-MbKZQy8Wt0dZzDLGLwj%2F5.7-analytics-additional-filters.png?alt=media\&token=d5a48cb4-0319-462f-8cf5-3cdee431685a)

This feature allows business users to filter the analytics data across multiple dimensions. It provides a quick and easy way to track business metrics cutting across these dimensions. This feature combined with the enhanced date range filter provides a powerful way to filter the analytics data as per your business requirements. See [Analytics date filter](#analytics-date-filters), for more information.

The following lists a few use cases and the filter options you can apply to get results for the specific use case:

| Use case                                                                   | Filter options                                                                            |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Q\&A queries in the "Web" channel over the last 3 months                   | <p>Date range: Last 90 days</p><p>Channel: Web</p><p>Intent type: Q\&A intent </p>        |
| Inline queries in the "French" language in the 6 months                    | <p>Date range: Last 180 days</p><p>Language: French</p><p>Intent type: Inline intent </p> |
| Queries that hit the "Order" tag in the last 3 months in the "Web" channel | <p>Date range: Last 90 days</p><p>Tag: Order</p>                                          |

See [Additional filter criteria](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#additional-filter-criteria), for more information.

### Download PDF

In this release, a new feature to download the analytics boards and user journey in a PDF file has been introduced. The following are the key highlights of this feature:

* [Download analytics board in PDF file](#download-analytics-board-in-pdf-file)
* [Download user journey in PDF file](#download-user-journey-in-pdf-file)

#### Download analytics board in PDF file

In this release, a new feature to download a PDF copy of the analytics board has been introduced.  You can use this for reporting purposes and for further analysis. The data as viewed in the UI is available in the downloaded PDF.&#x20;

This option is available in the **Analytics** page and also in the details page for **each Analytics board**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mc8Cr5op9MnuBezpu6Y%2F-Mc8CuO3_WoDXjsono7m%2F5.7-rn-download-pdf-analytics.png?alt=media\&token=816e87cb-5ad7-4abf-ac31-b79304d596e0)

The following illustration depicts the new **Download PDF** option in the **Top Q\&A intents** detail page:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbLHqFBXQZtR9pt_Z4N%2F-MbLI5MPo9k6xVbohAGs%2F5.7-analytics-top-qa-detail.png?alt=media\&token=1027fff2-b14b-4fd6-b1c1-2d8ceff7bb99)

See [Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics), for more information.

#### Download user journey in PDF file

In this release, a new feature to download a PDF copy of the user's journey has been introduced. Note that the downloaded PDF only shows the journey till the intent level or first node of the intent. You can use this for reporting purposes and for further analysis, as required.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbLDOLF9_Z_1c9O5td1%2F-MbLEZbjvbYYl7OT67WS%2F5.7-user-journey-download.png?alt=media\&token=260efbd0-8f5c-4408-805d-947e05c3f234)

See [User journey](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/user-journey), for more information.

### OAuth2 authorization in the custom live agent system

In this release, you can configure OAuth2 authorization in the custom live agent system using the authorization token issued by the OAuth2 provider. This feature is useful in scenarios where the connection to the custom live agent is not directly exposed and available only through an OAuth2 provider.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPwNYLdyYBfaAcGG4ehtL%2Fimage.png?alt=media\&token=a57c5a95-a7a3-4844-b6cc-318910dd2fa0)

See [OAuth2 authorization](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/custom-live-agent#oauth2-authorization), for more information.

## Enhancements

### Analytics date filters

In this release, the **Date** filter in the Analytics board has been enhanced with the following in-built filter options:

* Yesterday
* Today
* Last 7 Days
* Last 14 Days
* Last 28 Days&#x20;
* Last 90 Days
* Last 180 Days.&#x20;

This helps in the quick and easy filtering of analytics data based on the in-built date filters. You can also use **Custom range** to pick your own date range by selecting the start and end dates. See [Date filters](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#date-range), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbKXobQoTzlRqxGLyUi%2F-MbKYBdnDlGgS0lVofEN%2F5.7-analytics-default-date-range.png?alt=media\&token=c69b0d20-df5f-400c-ada6-12f2a3e412e5)

In the previous release, you could only filter use a date range option and in-built date filter options were not available.

### Skill and intent identifiers&#x20;

In this release, the ability to identify the skill and intents using skill and intent identifiers respectively has been enhanced. You can now specify a user-friendly identifier for your skill or intent at the time of creating the skill or intents using the **Skill key** and **Intent key** respectively. Providing user-friendly skill identifier and intent identifiers is useful in the following ways:

* Helps to easily **identify** and **refer** to the skill and intents in&#x20;
  * [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format)
  * [Flow control statements](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control) such as goto\_nod&#x65;*,* goto\_intent
  * [Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights)
  * [User journey](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/user-journey)
  * [Search nodes within Dialog skill implementation](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/perform-common-actions#search-nodes)
* **Retains the same skill key and intent keys** when the agents are [copied](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/make-a-copy), [exported](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents), [imported](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents) [promoted](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates), [published to skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), or [imported from skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills). Hence, the existing regression tests and flow control statements can be re-used.

The following illustration depicts how you can provide skill identifier using **Skill key** when creating a Dialog skill:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mc9CklaLL_1csEzuARh%2F-Mc9D1sk2kQIcQLuKrWL%2F5.7-create-dialog-skill-rn.png?alt=media\&token=494eb114-a3ca-4a43-b531-f336617899d4)

The following illustration depicts how you can provide intent identifier using **Intent key** when creating a Q\&A in Dynamic Q\&A skill:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb0u6LF-sKTWqZGdgkm%2F-Mb0uV3_1z8Lh2rPBvYk%2F5.7-dynamic-qa-add-intent.png?alt=media\&token=5de448ed-eb1a-406d-8b67-160ee9cef027)

Similarly, you can also edit the skill key and intent key, if required. However, note that if you update the key and if the key is used say in JS code or in regression testing, then you must update the skill or intent key manually.&#x20;

See the following topics for more information:

* [Create Dialog skill ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill)/ [Edit Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/perform-common-actions#edit-dialog-skill)
* [Create Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/create-a-new-dynamic-q-and-a-skill) / [Edit Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/perform-common-actions#edit-skill)
* [Create Answers skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/create-new-knowledge-base) / [Edit Answers skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/perform-common-actions#edit-answers-skill)
* [Create Smalltalk skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/create-new-knowledge-base) / [Edit Smalltalk skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/perform-common-actions#edit-smalltalk-skill)
* [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent)
* [Add question and answers in Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers)
* [Add question and answers in Smalltalk Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa)

In the previous release, skill and intent identifiers were automatically generated by the system as numbers. There was no option to edit the identifiers. The skill and intent identifiers changed when the agents were copied, exported, imported promoted, published to the skill store, or imported from the skill store. Hence, the existing regression tests and flow control statements had to be manually modified and re-used.

{% hint style="info" %}
**Note**: Post v5.7.0 upgrade, all the existing skill identifier and intent identifiers will continue to work as-is and no change is required.
{% endhint %}

### Regression testing - Disambiguation scenarios

In this release, testing disambiguation scenarios in regression testing have been improvised to perform a more granular level of testing with disambiguation options. You can now specify a set of disambiguation options as a pipe-separated list in the regression testing file when you are testing disambiguation scenarios.

The following table summarizes the disambiguation scenario improvements in the current release:

| v5.7.0                                                                                                                                                                                                                 | Previous release                                                                                                                                                                                                   | For more information                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `disambiguation:<<skill_key>>.<<intent_key>>\|<<skill_key>>.<<intent_key>>`                                                                                                                                            | `disambiguation`                                                                                                                                                                                                   | See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format#disambiguation) |
| If a query evaluates to a disambiguation response and there is a node specified in "Expected intent", then the result is evaluated as **Failed**, even if "Expected intent" is in the set of disambiguation responses. | If a query evaluates to a disambiguation response and there is a node specified in "Expected intent", then the result is evaluated as **Success**, if "Expected intent" is in the set of disambiguation responses. | See [Understanding results](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing#understanding-results), for more information.     |

In the previous release, there was limited scope for testing the disambiguation scenario.&#x20;

See [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing) and [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), for more information.

### Regression testing - Answers skill scenarios

In this release, regression testing has been enhanced to include testing of Answer skill responses. You can now specify the <\<skill.key>>.<\<intent.key>> of the Answers skill in the expected flow column of the regression testing file to test the Answers skill response.

| Column 1                    | Column 2                                         |
| --------------------------- | ------------------------------------------------ |
| 1,macpizza\_policy.RTIor1cb | Can you explain Avaamo's privacy policy for PII? |

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mcwz1RftMha3cSBJ7tF%2F-Mcx-xKOFa0qo5srPGgU%2F5.7-answers-skill-regression.png?alt=media\&token=502500a8-c17b-4045-b8dd-22c51b8dc9e6)

See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), for more information.

In the previous release, there was no option to test Answers skill responses in regression testing.

### Regression testing - Performance metrics&#x20;

In this release, you can view the **Accuracy** and **F1 Score** of regression testing results using the standard machine learning formula.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbKuC6GKQAZ5h_M7hJS%2F-MbKuK8tKw09zSQmz_Nf%2F5.7-regression-testing-results.png?alt=media\&token=9ebfe4bc-eb2d-4129-9625-ca5ae45948bc)

The goal must be to obtain a better F1 Score. To aim for a better F1 Score, you can check

* If there is sufficient training data in your agent.
* Check if the test cases are accurate to validate your agent.&#x20;

See [Performance metrics](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing#performance-metrics), for more information.

## Changes

### Regression testing

In this release, the following changes have been implemented in the **Regression testing** page:

**"Add Validation data" option has been removed**:&#x20;

Regression testing is typically done on a huge amount of data. Providing an input test file using "Add validation data" from the UI has limited usage, is tedious, and not practical. You could only perform simple testing and testing multi-turn conversations were not possible with the "Add validation data"  option.

Hence, this option has been removed. You can continue to upload the input test file in the required CSV format instead of using the **Upload test file** option. See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), for more information.

**Changes in the Actions column**:&#x20;

In the release, the following changes have been implemented in the Actions column:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbKuYFpj6hhDn8Tjyj2%2F-MbKuvh4nNXFxgjSAjpA%2F5.7-regression-testing-actions.png?alt=media\&token=bb160dab-7604-4b5f-a571-5e307c807396)

* **"View results" and "View inputs" options have been removed**: Since regression testing is typically done on a huge amount of data, going through the results or the input file from the UI is tedious and not practical. Hence, these options have been removed from the Actions column. You can instead use, "Downloading input CSV" and "Download results" option from the Actions column to download and view the input file and results respectively.&#x20;
* **Re-run** option has been re-labeled as **Run**
* **Downloading input CSV has been moved to the Actions column**: In the previous release, you could download the input CSV by clicking the file in the Regression file column. In this release, this option has been moved to the Actions column&#x20;

### User role - API access

In this release, the **API access** role has been removed in the following pages:

* [Add new user](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/users#add-new-user) and [Edit user](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/users#edit-user)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbFUQwc4Wn7MqUOv6Z9%2F-MbFUqkU3WYaVxVdfQUJ%2F5.7-add-new-user.png?alt=media\&token=1c487f68-0767-4dbc-9580-d77094b328f7)

* [Create group](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups#create-group-and-add-members) and [Edit group](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups#edit-group)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbFW0cwSaEh99AXALgI%2F-MbFecj6flscIswqHt1t%2F5.7-roles-groups.png?alt=media\&token=901bf9cf-7981-4b9a-99ec-0af366ca8fe2)

Since all the exposed RESTful APIs now require access to the agent which is handled with the agent permissions, having the API access role is redundant and no longer useful. See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

### Agent voice hints for C-IVR

In this release, the **Configuration -> Voice hints** page has been removed. Instead, you can now specify the agent-level voice hints in the **Speech recognition** section of the **Configuration -> Voice settings** page.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mc8rLXHAJlfDmQO9w4I%2F-Mc8sd2ffMMsHumrrV-m%2F5.7-rn-voice-settings-speech.png?alt=media\&token=54469e43-704a-4e48-b4b5-f713a3e0a500)

{% hint style="info" %}
**Note**: Post v5.7.0 upgrade, all the existing agent-level voice hints that are defined for the C-IVR channel in the **Configuration -> Voice hints** page will be available in the **Speech recognition** section of the **Configuration -> Voice settings** page.
{% endhint %}

Since these voice hints are also used for voice-enabled assistants in [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels, defining is a single section is easy to manage and maintain. See [Speech recognition](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-voice-settings#speech-recognition), for more information.

### JS errors

In this release, the message creation timestamp in the **Sender** column has been removed. Instead, a new column **Time** has been introduced to display the error creation time. The error messages are sorted based on the descending order of error creation time.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-McIOvc29Vn5YG8Z9K5X%2F-McIQV3-UF4fOxasAlj-%2F5.7-js-errors.png?alt=media\&token=b698bbaf-6c8a-4639-b143-f3e3c19ae018)

Since the earlier sorting was based on message creation timestamp, it was difficult to view and scroll to the recent error messages. See [JS errors](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-js-errors), for more information.

### Default scroll in web channel

In this release, the default scroll behavior in the [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#voice), [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps), and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps) channels has been changed from **Bottom** to **Top**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb_TKHoxRRB3CtCnvZR%2F-Mb_TN-sqYM3_aotZXh_%2F5.7-web-channel-scroll-behavior-top.png?alt=media\&token=28dc58c8-03f0-4d1c-abe7-943fa2810afe)

In the previous release, when there were multiple responses from the agent, then by default, the agent chat widget would scroll to the latest message, which is not a good user experience. The user either had to scroll up to read the first message or in such scenarios could miss reading the earlier posted messages. See [Scroll behavior](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel#scroll-behaviour), for more information.

### Agent configurations

In this release, the configuration options in the Agent -> Configurations section have been re-arranged in alphabetical order for ease of use.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-McUaPuVwlwZHfwufeAy%2F-McUeA2HBkgfN1XJ-eu8%2F5.7-rn-agent-configurations.png?alt=media\&token=bbaa1a02-2b36-4ef0-925e-0ca0081b3053)

In the previous release, the configurations were not arranged in any particular order and were difficult to locate.

### Persistent menu

In this release, the following notification messages are displayed in the persistent menu:

* Facebook does not support Deep Link (type).
* Facebook supports a maximum of 3 items. If more items are present, then the first three will be selected for Facebook.

Note that these are applicable only if you are using the Facebook channel to deploy your agents.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-McwSNMhRJyg2eqpzq6C%2F-McwTQK0i1aPnFO4m-sT%2F5.7-rn-persistent-menu.png?alt=media\&token=ddc31a98-9719-4a17-bf61-aad5658b56a2)

The "number of persistent menu items" restriction is due to the limitations of Facebook messenger See [call\_to\_actions in the properties section](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu#properties), for more information.

See [Persistent menu](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-persistent-menu), for more information.

### Entity structure in context.insights object

In this release, each entity in the `context.insights` object includes metadata details such as entity type, current value, parent entity type. The metadata provides more insights about the entity and can be used for further processing.

The following is an example of entity structure in the `context.insights` object:

```javascript
[
  {
      "entity": "country",
      "entity_type": "country",
      "entity_value": "United Kingdom",
      "domain_key": "bot_inline_domain_xxxxx",
      "value": "United Kingdom",
      "current_value": "London",
      "index": 10,
      "derived_parent": true,
      "parent_entity_key": null,
      "custom_entity_type": true
    },
    {
      "entity": "country",
      "entity_type": "country",
      "entity_value": "India",
      "domain_key": "bot_inline_domain_xxxxx",
      "value": "India",
      "current_value": "Delhi",
      "index": 0,
      "derived_parent": true,
      "parent_entity_key": null,
      "custom_entity_type": true
    }
  ]
```

The following table lists the entity structure change for a single entity value before and after the 5.7.0 release:

{% tabs %}
{% tab title="Before release" %}

```javascript
// Single entity value is an array and not required since it is just one value:
{ 
    "entity_type": "regex", 
    "entity": "package_no", 
    "entity_type_key": "package_number", 
    "custom_entity_type_id": 245, 
    "index": 0, 
    "entity_value": [ "888999" ], 
    "domain_key": "bot_inline_domain_xxx", 
    "value": "888999", 
    "current_value": [ "888999" ]
}

// Multiple entity values is an array and mapping its metadata is not easy:
// In the following example, it is difficult to understand 
// what is the parent value and which one is the child value.
{
  "entity": "country",
  "entity_type": "country",
  "entity_value": [
    "United Kingdom",
    "India"
  ],
  "domain_key": "bot_inline_domain_xxxxx",
  "value": [
    "United Kingdom",
    "India"
  ],
  "current_value": [
    "London",
    "Delhi"
  ],
  "index": 10,
  "derived_parent": true,
  "parent_entity_key": null,
  "custom_entity_type": true
}

```

{% endtab %}

{% tab title="After release" %}

```javascript
// Single entity value is a string instead of an array. 
// This is easier to read and process
{ 
    "entity_type": "regex", 
    "entity": "package_number", 
    "entity_type_key": "package_no", 
    "custom_entity_type_id": 245, 
    "index": 0, 
    "entity_value": "888999",
    "domain_key": "bot_inline_domain_xxx", 
    "value": "888999", 
    "current_value": "888999" 
}

// Each entity is a separate object with metadata. 
// Understanding and interpreting entities with metadata is much easier.

[
  {
    "entity": "country",
    "entity_type": "country",
    "entity_value": "United Kingdom",
    "domain_key": "bot_inline_domain_xxxxx",
    "value": "United Kingdom",
    "current_value": "London",
    "index": 10,
    "derived_parent": true,
    "parent_entity_key": null,
    "custom_entity_type": true
  },
  {
    "entity": "country",
    "entity_type": "country",
    "entity_value": "India",
    "domain_key": "bot_inline_domain_xxxxx",
    "value": "India",
    "current_value": "Delhi",
    "index": 0,
    "derived_parent": true,
    "parent_entity_key": null,
    "custom_entity_type": true
  }
]


```

{% endtab %}
{% endtabs %}

See [context.insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights), for more information.

{% hint style="info" %}
**Note**: This change is backward compatible which implies that if you are using `context.insights` for processing in say any JS code prior to this release, then there is no change required and you can continue to use it in the same manner. To enable backward compatibility, contact Avaamo Support.&#x20;
{% endhint %}

## <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTZ5YWcSjzjFT6eEzmh%2F-MTZC9Fv7M4NnKibmWgw%2FScreenshot%202021-02-15%20at%2011.10.31%20AM.png?alt=media&#x26;token=435a778d-2525-4628-af78-58a3809180e9" alt="" data-size="line"> Deprecation notice

In order to provide accurate coverage and flexibility to test your agents in the Avaamo Conversational AI Platform, the legacy **Export regression file** option from the **Query insights** page is deprecated from the v5.7.0 release onwards.

### Why?

Exporting regression testing data from the **Query insights** page provides only minimal coverage of the test cases. Since agents are complex and business-critical, this does not cover complete end-to-end test case scenarios that is expected of regression testing. In order to provide accurate coverage and flexibility to test your agents, it is recommended to manually create the regression test cases. See [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing), for more information.

### When is the support completely stopped?

This feature will be removed from v5.8.0 onwards.

### What action to take?

No action required

### How to create a regression file from the Query insights page?

1. Filter the required results by specifying search criteria in the **Query insights** page. See [Search and View Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights#search-and-view-query-insights), for more information.
2. In the **Query insights** page, click **Export jobs** and export the Query insights to a CSV file.  See [Export query insights data](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights#export-query-insights-data), for more information.
3. In the exported CSV file, you can use "User query", "Skill key", and the "Intent key" to create a regression file according to your requirement. See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), for more information.
