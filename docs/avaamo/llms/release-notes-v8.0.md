# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0.md

# Release notes v8.0

The Avaamo Conversational AI Platform `Atlas 8` release includes 1 new product,  3 new features, and 13  enhancements.

**New product:** The Avaamo Conversational AI Platform introduces a new product `LLaMB - Large Language Model for Business` in this release. See [Introducing LLaMB](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-llamb), for more information.

**New features**: This release includes the introduction of the 3 new features:

1. [Mercury theme](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-mercury-theme)
2. [User Acceptance Testing (UAT) in the Web channel ](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-uat-in-web-channel)
3. [Advanced agent](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-advanced-agent)

**Enhancements**: This release includes enhancements related to the following existing features:

<table><thead><tr><th width="208">Module</th><th>Enhancements</th></tr></thead><tbody><tr><td>Outreach</td><td><ul><li><a href="#faster-campaign-execution">Faster campaign execution</a></li><li><a href="#campaign-configuration-improvements">Campaign configuration improvements</a></li><li><a href="#improved-error-handling-with-recipient-csv">Improved error handling with Recipient CSV</a></li></ul></td></tr><tr><td>Live agent console</td><td><ul><li><a href="#view-real-time-conversation-duration">View real-time conversation duration</a></li><li><a href="#changelog-api">Changelog API</a></li><li><a href="#live-sessions-to-monitor-real-time-information">Live Sessions to monitor real-time information</a></li><li><a href="#send-attachments-to-live-agents">Send attachments to live agents</a></li></ul></td></tr><tr><td>Web channel</td><td><a href="#enable-streaming-messages-via-typing-animation">Enable streaming messages via typing animation</a></td></tr><tr><td>MS Teams </td><td><a href="#ms-teams-channel-configuration-improvements">MS Teams channel configuration improvements</a></td></tr><tr><td>Accessibility</td><td><a href="#accessibility-enhancements">Accessibility enhancements</a></td></tr><tr><td>SMS channel</td><td><a href="#track-sms-billing-using-sms-usage-report">Track SMS billing using SMS Usage report</a></td></tr><tr><td>C-IVR improvements</td><td><ul><li><a href="#improved-asr">Improved ASR</a></li><li><a href="#voice-idle-tone">Voice idle tone</a></li></ul></td></tr><tr><td>Javascript code</td><td><a href="#remove-user-property">Remove user property</a></td></tr></tbody></table>

**Changes:** This release includes changes related to the following modules:

* [Campaign statistics page ](#campaign-statistics-ui)
* [Outreach insights API](#outreach-insights-api)
* [Label change: Create new agent](#label-change-create-new-agent)

{% hint style="danger" %}
**Deprecation and removal notice**: See [Deprecated and removed features](https://docs.avaamo.com/user-guide/deprecated-and-removed-features/atlas-8-deprecated-and-removed-features), for a complete list&#x20;

of all the deprecated and removed features in the `Atlas 8` release.
{% endhint %}

## Outreach enhancements

### Faster campaign execution

In this release, significant enhancements have been made to the performance of campaign execution times for both SMS and Voice through internal code optimizations. This optimization greatly scales the campaign, enabling it to handle huge recipients efficiently.

This performance improvement extends to the download functionality of the campaign execution report from the `Campaign statistics` page. Given the optimized campaign execution time capable of managing larger loads, the campaign download report option has also been refined to handle similar demands. The `Download` option now initiates an asynchronous job, facilitating the seamless download of larger campaign reports.

See [Campaign statistics](https://docs.avaamo.com/user-guide/outreach/campaign-statistics), for more information.

### Campaign configuration improvements

In this release, a new optional textbox  `Country Code` has been introduced in the `Campaign -> Add Message` section, allowing users to specify the country code for recipients. This feature applies exclusively to SMS and voice campaigns.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbiRMGz9g8bHcrqXHKZ1v%2Fimage.png?alt=media&#x26;token=6f3febec-0381-4ec5-b9d4-6800115ec7b9" alt=""><figcaption></figcaption></figure>

Given the mandatory requirement for recipient phone numbers to be in the E.164 format, which necessitates a country code, this feature proves valuable when working with recipient files that lack country codes. By specifying a country code, all recipient phone numbers are automatically prefixed with the designated code, ensuring smooth delivery of campaign messages.

Previously, in the absence of a country code, the campaign would encounter failure with an invalid phone number error message, or users had to execute a pre-processing job to append the campaign recipients with a country code before initiating the campaign, thereby introducing delays to the campaign execution time.

See [Country code](https://docs.avaamo.com/user-guide/outreach/campaigns/create-new-campaign#country-code-optional), for more information.

### Improved error handling with Recipient CSV &#x20;

In this release, enhancements have been made to the error handling process during Recipient CSV parsing to facilitate more effective troubleshooting of campaign failures.

Upon encountering any recipient CSV parsing error during campaign execution, the system now displays a detailed error message in the `Campaign statistics` UI page, specifying the line or row where the error occurred. Furthermore, if users have configured campaign failure notifications, an email containing the error details is notified to all the users. See [Campaign failures](https://docs.avaamo.com/user-guide/outreach/campaigns/create-new-campaign#campaign-failures), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FWxKCNDS9jHo6wGbAfcRY%2Fimage.png?alt=media&#x26;token=71a66716-4fec-4b22-8b2b-4fe1dadb31ec" alt=""><figcaption></figcaption></figure>

See [Campaign statistics](https://docs.avaamo.com/user-guide/outreach/campaign-statistics), for more information.

## Live agent console enhancements&#x20;

### View real-time conversation duration

In this release, the `Live Agent Console` has been enhanced with a real-time conversation duration timer. Live agents can view this timer for all currently active chat requests in the Live agent console.

The conversation duration timer is a valuable indicator for managing customer support interactions efficiently, meeting SLAs, and enhancing the overall customer experience. It provides real-time insights into the progress of each chat and allows live agents to make informed decisions.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F39z2Q4i2fZkc6Qlq3ADr%2Fimage.png?alt=media&#x26;token=f45f510f-92c7-4039-a0a6-9d8a3114f965" alt=""><figcaption></figcaption></figure>

See [View real-time conversation duration](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/view-real-time-conversation-duration), for more information.

### Changelog API

In this release, the `Live Agent Console` has been enhanced with a new `Changelog API`.&#x20;

You can use the Changelog API to view all the configuration changes performed by the live agent (such as live agent status updates) and the supervisors (such as configuration changes in Teams, Routing rules, or Quick responses).&#x20;

```bash
// API Signature

https://cx.avaamo.com/api/v1/cap/change_logs.json

// Sample cURL request

curl --location --request GET 'https://cx.avaamo.com/api/v1/cap/change_logs.json?per_page=1' \
--header 'Content-Type: application/json' \
--header 'access-token: xxxxxxxxx9a34a44a838af10fxxxxxxx'

```

See [Live Agent Changelog API](https://docs.avaamo.com/user-guide/live-agent-console/live-agent-console-rest-apis/live-agent-changelog-api), for more information.

### Live Sessions to monitor real-time information&#x20;

In this release, the `Live agent console` for Supervisors has been enhanced with a new `Live Sessions` page.&#x20;

`Live Sessions` enable supervisors to monitor real-time information on the customer wait time and conversation duration of all the active and queued chat requests within the company. This provides valuable insights into traffic patterns and workload, allowing them to optimize chat routing and create specialized teams with specific skill sets, ultimately enhancing customer satisfaction.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F621YgOB3lLXE13M66718%2Fimage.png?alt=media&#x26;token=d676ccbb-78fa-4dab-9f34-ca29ba94d92b" alt=""><figcaption></figcaption></figure>

See [Live sessions](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/live-sessions), for more information.

### Send attachments to live agents

In this release, the `Web channel` configuration has been enhanced with a Send attachment option in the `Channels -> Widget configuration` section. This option is useful when users have to send attachments in the live agent conversations from the agent to the live agent.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F84uU2YxsElFrUApHUKsZ%2Fimage.png?alt=media&#x26;token=9565f886-474b-483c-bb6a-1a59fa2f7a63" alt=""><figcaption></figcaption></figure>

In the agent, the attach icon is enabled allowing the users to send file attachments. See [Send attachment](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration#send-file-attachment), for more information.

## Enable streaming messages via typing animation&#x20;

In this release, the Web channel configuration option has been enhanced with a new option `Stream message` in the web channel configuration page.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FX9cSPy5Zu5DqAvpNNMD0%2Fimage.png?alt=media&#x26;token=b870b362-7d4c-41e0-9672-a9f9dac201a7" alt=""><figcaption></figcaption></figure>

Enabling this option renders streaming responses through the typing animation to the user instead of displaying the response at once, eliminating idle waiting time. Streaming is intuitive, especially when there is a delay in agent response. It creates an impression to the user that the agent is responding and helps actively engage the user in the conversation flow.

See [Widget configuration -> Stream message](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration#stream-message), for more information.

## MS Teams channel configuration improvements

In this release, the MS Teams channel has been enhanced with a new option `Enable hero card` in the channel configuration page. Hero card support has been available since the [v6.3.0 release](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.3.x/release-notes-v6.3.0#hero-card-support).

In the `Atlas 8` release,  when you enable the option `Enable hero card` in the MS Teams Channel configuration, it renders the responses by default in Hero cards instead of Adaptive cards in the MS Teams channel. This functionality proves beneficial when dealing with numerous responses containing embedded HTML code within the card's title or description. As this is not supported in the Adaptive Card format, toggling `Enable hero card` option allows HTML tags to be rendered as-is in the MS Teams channel using Hero cards.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5r3k9BwESgw4ccHpxWiD%2Fimage.png?alt=media&#x26;token=410bd365-3ed1-469c-bfae-9b8ff944a872" alt=""><figcaption></figcaption></figure>

See [Enable hero card](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#enable-hero-card), for more information.

See [MS Teams Compliance](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#microsoft-teams-compliance), to understand the elements that are not compliant with the MS Teams channel for Hero cards. &#x20;

## Accessibility enhancements

In this release, the Accessibility inclusivity in the agents built using the Avaamo Conversation AI Platform has been improved. The following are a few key areas where **`accessibility has been  incorporated`** in this release based on WCAG 2.0 (Web Content Accessibility Guidelines):

* **Mercury theme:** In this release, a new theme - `Mercury` has been introduced and all elements within the `Mercury theme` are accessible in a manner consistent with the other existing themes. For instance, the streaming of responses which is exclusively a part of the `Mercury theme` is now accessible. See [Mercury theme](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-mercury-theme), for more information on the newly introduced theme.
* **Auto-complete combo box**: When the [auto-complete combo box](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#query-autocomplete-url) is open, the user can press the `Escape` button once to minimize or hide the combo box, and press the `Escape` button again to clear the text in the search input or the message text box in the agent widget according to the W3C ARIA Authoring Patterns combo box.
* **Welcome screen - Get started screen**:  The user interface (UI) elements on the [Get Started screen ](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/introduce-agent-get-started)are now equipped with accessibility features, mirroring those found in the agent widget. The accessibility capabilities applied to the UI elements within the agent widget are also applicable to the elements on the [Get Started screen](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/introduce-agent-get-started). For example, the ability to use keyboard navigation to access the welcome text in the `Get Started screen` or the ability to read out the entire welcome message text when the screen reader is enabled.
* **Error messages**: When the screen reader is activated, it now audibly conveys any error messages present in the agent widget. For instance, if a form response requires a mandatory text entry, and the user submits the form without providing the required text, an error message is displayed in the agent widget. These error messages are now audibly communicated, enhancing accessibility for users relying on screen readers.

## Track SMS billing using SMS Usage report

In this release, a new page `SMS Usage` has been introduced in the `Settings` section. This page is valuable for users with the SMS channel enabled in their agents, providing a means to monitor and track SMS usage within their accounts.&#x20;

You can also export the usage report from this page to analyze further. The page helps you to track the anticipated SMS billing associated with the company-level SMS configuration.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCkgnwPQEfxpOf4B63bvQ%2Fimage.png?alt=media&#x26;token=29738fc4-c758-42a0-8056-73f39bb85f0b" alt=""><figcaption></figcaption></figure>

See [SMS usage](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/sms-usage), for more information.

{% hint style="info" %}
**Note**: The `SMS Usage` page is available only for users with the Settings role.
{% endhint %}

## C-IVR improvements

### Improved ASR

In this release, Automatic Speech Recognition (ASR) has been fine-tuned with a new and improved model. The following are some of the key benefits of the new ASR model:

* Better quality recognition&#x20;
* Custom noise reduction (Background noise reduction)
* Better extraction of alphanumerics

{% hint style="info" %}
**Note**: Contact Avaamo Support with your use case to enable this for your account.
{% endhint %}

### Voice idle tone

In this release, enhancements have been made to the user experience, specifically in scenarios where the agent requires additional time to respond with an idle tone.&#x20;

Rather than experiencing silence or a lack of input, the introduction of a tone serves to actively engage the user and assures that the agent will respond shortly. For example, the system generates a typing tone when processing DTMF/keypad input.

{% hint style="info" %}
**Note**: Contact Avaamo Support with your use case to enable this for your account.
{% endhint %}

## Remove user property

In this release, the user property in the Javascript code has been enhanced with a new method `User.removeProperty` to delete or remove the specified user property added for a user.&#x20;

{% code overflow="wrap" %}

```javascript
User.removeProperty("<<key>>")
```

{% endcode %}

See [User.removeProperty](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.removeproperty), for more information.

## Changes&#x20;

### Campaign statistics UI

In this release, the following are the changes incorporated in the `Campaign statistics UI` for consistency and accurate label representation:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FiT4cB9ApxIjpJf2UXX9U%2Fimage.png?alt=media&#x26;token=f5eeaf59-2174-425d-887e-b7ceaf776467" alt=""><figcaption></figcaption></figure>

* The `Date Range` label in the `Campaign Statistics UI` has been refined to `Execution`provide a more precise indication of the date in the drop-down. The date in the drop-down refers to the campaign run or execution date.
* In alignment with the `Analytics UI` and to maintain a consistent user experience across the platform, the `Execution Date` drop-down now allows users to select up to 6 months of campaign runs.

See [Campaign statistics](https://docs.avaamo.com/user-guide/outreach/campaign-statistics), for more information.

### Outreach insights API

To ensure optimal performance and consistency, the date range in the Outreach Insights API has been modified to enable retrieval of a maximum of 6 months of data in a single fetch.

See [Outreach insights API](https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/outreach-insights-api), for more information.

### Label change: Create new agent

In this release, a new agent called the [Advanced Agent](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-advanced-agent) has been introduced. To differentiate creating an advanced agent vs the normal one, the normal agent is referred to as a "Standard agent". This is only a label change, all the functionalities of this agent remain as before the `Atlas 8` release.&#x20;

A new **Create** dropdown in the `Dashboard -> Development` tab with options to create **Standard agent** and **Advanced agent** has been included.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxcbQHXfX3R0vKCAFPqFz%2Fimage.png?alt=media&#x26;token=a3975be0-2469-4cf2-ae2d-7818fca3551e" alt=""><figcaption></figcaption></figure>

Note that when an `Advanced agent` is enabled for the account, the `Create new agent` label remains as-is without any change.&#x20;

See [Create Standard agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills) and [Create Advanced agent](https://docs.avaamo.com/user-guide/how-to/build-agents/create-advanced-agent) for more information.
