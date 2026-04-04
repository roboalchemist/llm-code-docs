# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0.md

# Release notes v9.0.0

The Avaamo Conversational AI Platform `9.0.0` release includes a new agent - the `AI agent`,  3 new features, and 17 enhancements.

## **New AI agent**&#x20;

The Avaamo Conversational AI Platform introduces a new `AI agent` in this release.&#x20;

The `AI agent` is a next-generation agent built to power highly intelligent and dynamic voice or text-based conversations. With advanced context awareness and adaptive response capabilities, the `AI Agent` elevates query handling and user engagement, delivering more natural, intuitive, and human-like interactions.

{% hint style="info" %}
**Note**: The AI agent is enabled on demand. Contact your dedicated Customer Success Manager for further assistance.
{% endhint %}

See [AI Agents](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/introducing-ai-agents), for more information.

## New features

This release includes the introduction of the 3 new features:

1. [LLaMB Content Regression Testing](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/introducing-llamb-content-regression-testing)
2. [Voice Usage](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/introducing-voice-usage)
3. [Aura – your smart support agent](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/meet-aura-your-smart-support-agent)

## Enhancements

Enhancements are categorized according to the Avaamo Conversational AI Platform modules for streamlined navigation. Following is the list of all the enhancements in the 9.0.0 release:

<table><thead><tr><th width="181.30145263671875">Module</th><th>Enhancements</th></tr></thead><tbody><tr><td>LLaMB</td><td><p>Content ingestion improvements </p><ul><li><a href="#html-uploads-made-easy">HTML uploads made easy: Upload directly from the UI—no API needed.</a></li><li><a href="#rate-limits-in-content-ingestion-apis">Enhanced stability with rate limits in content ingestion APIs</a></li></ul><p>User experience improvements</p><ul><li><a href="#llamb-goes-multilingual">LLaMB goes multilingual: Conversation with LLaMB in any Avaamo-supported language.</a></li><li><a href="#configurable-response-rendering-in-llamb">Configurable response rendering in LLaMB – Enable concise answers and citation links as needed</a></li></ul><p>Troubleshooting and Debugging</p><ul><li><a href="#observability-deeper-insights-into-llamb-response-chunks">Observability: Gain deeper Insights into LLaMB Response Chunks  </a></li></ul><p>Analytics</p><ul><li><a href="#export-llamb-usage-reports">Export LLaMB usage reports </a></li></ul><p>Security</p><ul><li><a href="#disable-citation-link-security-in-llamb-responses">Disable citation link security in LLaMB response</a></li></ul></td></tr><tr><td>Information Masking</td><td><ul><li><a href="#default-masking-for-new-agents">Default masking for new agents</a></li><li><a href="#retention-period">Retention period: Set how long data is retained before masking</a></li><li><a href="#improved-response-masking-now-only-pii-data-is-masked">Improved response masking: Now only PII data is masked </a></li><li><a href="#enhanced-agent-details-api-response-with-masking-information">Enhanced Agent details API response with masking information</a></li></ul></td></tr><tr><td>Usage reports</td><td><a href="#usage-reports-track-your-product-usage-in-one-place">Track your product usage in one place</a></td></tr><tr><td>Web channel security configuration</td><td><a href="#cookie-expiry-setting-for-better-session-management">Cookie expiry setting for better session management</a></td></tr><tr><td>Configuration > Settings</td><td><ul><li><a href="#enable-debug-logs-for-easier-troubleshooting">Enable debug logs for easier troubleshooting</a> </li><li><a href="#disable-co-reference-for-agents-without-context">Disable co-reference for agents without context</a></li></ul></td></tr><tr><td>MS Teams Channel configuration </td><td><a href="#disable-incoming-request-authorization-in-ms-teams-channel">Disable incoming request authorization in MS Teams channel</a></td></tr><tr><td>Conversational IVR (C-IVR) or Phone channel</td><td><a href="#customize-wait-time-audio">Customize wait-time audio </a></td></tr></tbody></table>

## Changes

This release includes changes related to the following modules:

1. [Updated location of Enable Markdown format option](#enable-markdown-format)
2. [Mask user IP toggle on the Privacy page](#mask-user-ip-on-the-privacy-page)
3. [Refreshed UI for the Login page](#refreshed-ui-for-the-login-page)
4. ["Standard agent" is now "Classic agent"](#standard-agent-is-now-classic-agent)
5. [Domain configuration now centralized under Web Channel settings](#domain-configuration-now-centralized-under-web-channel-settings)

## LLaMB enhancements

### HTML uploads made easy

In this release, the content ingestion in LLaMB has been enhanced to support direct HTML file uploads from the UI, removing the dependency on ingestion APIs for this use case. This update streamlines the ingestion workflow, enabling faster onboarding of web content in LLaMB.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0JoSKvGL6I4oUPsRsqzK%2FScreenshot%2009-04-2025%20at%2015.00.png?alt=media&#x26;token=a0e22c40-a35b-48bb-b4a0-b8f62f23bf7e" alt=""><figcaption></figcaption></figure>

Previously, only HTML URLs could be ingested through the UI, while HTML file uploads required using [Content ingestion API](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis).

See [Upload Documents](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content#upload-documents), for more information.

### Rate limits in content ingestion APIs

In this release, the [upload-web](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis#upload-document-html-url-to-llamb) and [upload-file](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis#upload-different-types-of-files-pdf-docx-pptx-xlsx-csv-html-to-llamb) Content Ingestion APIs now include a `rate limit` parameter, capped at **50 uploads per minute**. This improvement enhances system performance and promotes efficient use of resources.

See [Content Ingestion API](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis), for more information.

### LLaMB goes multilingual

This release enhances multi-language support for LLaMB, enabling real-time streaming translation across all [supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages) in the Avaamo Conversational AI Platform.

Users can now interact with the agent in any of the supported languages and the agent responds in the same language—even if the original content is in English. This provides a smooth, multilingual experience without needing content in multiple languages and a wider reach for LLaMB across the globe.

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeCrOnII6xB1f9oYQHZga%2FScreenRecording2025-04-08at11.43.42PM-ezgif.com-video-to-gif-converter%20(1).gif?alt=media&#x26;token=b34a02d1-29e8-4363-9646-c9c536f92fbb" alt="" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
**Notes**:

* To use this feature, ensure your agent is enabled for **Markdown format**. See [Enable MarkDown format](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#enable-markdown-format), for more information.
* Languages can be added via configuration, allowing flexibility based on your user base.
* While conversations can be multilingual, documents must be ingested in English (en-US).
  {% endhint %}

Refer [Multi-language support](https://docs.avaamo.com/user-guide/llamb/multi-language-support), for more information.

### Configurable response rendering in LLaMB

In this release, the configuration options for rendering responses in LLaMB have been enhanced with the following options in the agent's channel configuration settings:

* **Enable concise response**: For shorter, natural replies that retain key info—ideal for quick summaries, with full details available via citation links. See [Enable concise response](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#enable-concise-response), for more information.

| Before enabling                                                                                                                                                                                                                                                                           | After enabling - Responses are short with key info                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F81F6LCk0U2g6Pu1oy1Fl%2FScreenshot%2024-02-2025%20at%2019.24.png?alt=media&#x26;token=883b6c07-430c-43a8-a078-1c63fa342754" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4EXpiF6gzyIGiCSqnVy6%2FScreenshot%2024-02-2025%20at%2019.25.png?alt=media&#x26;token=67ecb000-cd86-4a94-b842-f4a9c54c1b2b" alt="" data-size="original"> |

* **Disable citation links**: To remove [citation links](https://docs.avaamo.com/user-guide/llamb/citation-links) in LLaMB agent responses. See [Disable citation links](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#disable-citation-links), for more information.

| Before enabling                                                                                                                                                                                                                                                                           | After enabling - Citation links are not displayed                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FN1aOf7ydlFddp1nFwJkS%2FScreenshot%2024-02-2025%20at%2019.22.png?alt=media&#x26;token=edccbc6a-9c75-48b5-a930-d164046279ee" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4Zx6je25hfgHsovMH8Iw%2FScreenshot%2024-02-2025%20at%2019.23.png?alt=media&#x26;token=9b44dd3a-b91e-474f-9ccd-bb314c6ef3d3" alt="" data-size="original"> |

{% hint style="info" %}
**Notes**:&#x20;

* Ensure that the [Enable Markdown Format](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#enable-markdown-format) option is enabled to view this setting.
* When using Agent Assist or AI Agent, where precise responses are required and source links are not needed, you can disable them using these options.
  {% endhint %}

### Observability: Deeper insights into LLaMB response chunks

This release introduces new `Query Context` feature in `Message insights` for LLaMB responses, providing detailed visibility into the **chunks** used to generate each LLaMB response.&#x20;

This helps you understand how different parts of your data contribute to the response—making it easier to debug, optimize, and trust the results.&#x20;

**Key highlights**:

* Enhanced visibility into the chunks used to generate responses
* Chunk-based responses show how queries are matched with relevant data
* Improved debugging with traceable chunk information for better optimization
* Greater transparency into how LLaMB builds and delivers answers

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnbQc0foGKgUzcnhG4ItA%2FScreenshot%202025-03-21%20at%2012.32.37%E2%80%AFPM.png?alt=media&#x26;token=d16a8601-076c-4950-9e70-5b676cf0fdd5" alt="" width="375"><figcaption></figcaption></figure></div>

Click `Query context` to see all the chunks used in forming the answer. Chunks marked as `Strong match` indicate high relevance to your query.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzCdkOp41KhhI5WYJ6z9p%2FScreenshot%202025-03-21%20at%2012.43.19%E2%80%AFPM.png?alt=media&#x26;token=8bd1a190-4647-46e5-a9ed-e79bf34b15d7" alt=""><figcaption></figcaption></figure>

Click any `chunk` to explore detailed info such as - Document name, Source URL, Intent used, Custom properties, and Additional descriptions to know exactly how user attributes and document properties are aligned to generate the response.&#x20;

See [Query context](https://docs.avaamo.com/user-guide/llamb/get-started/step-3-test-your-agent#query-context), for more information.

### Export LLaMB usage reports

In this release, you can now easily export your LLaMB usage data for better tracking and analysis.

**Key highlights**:

* Access the feature by navigating to:\
  `Profile Icon > Settings > Usage Reports > LLaMB Usage`
* Click `Export Usage Report` to download your data
* Get a CSV report of your LLaMB usage, including regression testing details
* Use it to analyze agent-wise trends, optimize usage, and make data-driven decisions

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDzzF8SGqaZnSF5NdBRoi%2Fu%20copy.png?alt=media&#x26;token=477e592f-683b-4a92-a1df-59e91b748296" alt=""><figcaption></figcaption></figure>

See [LLaMB Usage](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage), for more information.

### Disable citation link security in LLaMB responses

In this release, you now have the option to disable citation link expiration in LLaMB responses from the `Settings` page under the `Configuration` section.

**Key highlights**:

* By default, citation links expire 24 hours after generation. See [Citation links](https://docs.avaamo.com/user-guide/llamb/citation-links), for more information.
* When disabled, links remain accessible at any time without any expiry restrictions. It is recommended to keep citation link security enabled at all times to maintain secure and controlled access.
* Useful for debugging, troubleshooting, or sharing persistent references with users

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSKbEHDdrt3BENQscIzMb%2FScreenshot%202025-04-21%20at%207.51.50%E2%80%AFPM.png?alt=media&#x26;token=38344fd3-4432-4ba9-b35f-08ed00180e92" alt=""><figcaption></figcaption></figure>

This gives you more flexibility in how you manage and share LLaMB-generated links.

See [Advanced features](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#advanced-features), for more information.

## Masking enhancements

### Default masking for new agents

Starting this release, all newly created agents have information masking enabled by default to better protect Personally Identifiable Information (PII) and ensure compliance with data privacy regulations, right out of the box.

{% hint style="info" %}
**Note:** Masking support for non-English conversations is currently under continuous evaluation.
{% endhint %}

**What’s enabled by default**:

{% hint style="success" %}
**Key points:**&#x20;

Real-time masking is enabled by default, so any personal information in both your messages and the agent’s replies is automatically purged to keep your data safe.
{% endhint %}

By default, the following personal information is automatically masked in real-time:

* Date (example: date of birth)
* email
* person
* phone
* SSN
* first\_name&#x20;
* last\_name
* ip\_address
* Any user-uploaded files

See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more information.

### Retention period

In this release, the `Information masking` feature has been enhanced with configurable `Retention Period` support.&#x20;

The retention period in masking defines the duration for which data remains accessible before masking is applied. This enhancement enables agent-level control over data masking, supporting compliance with data privacy regulations while maintaining system performance.

{% hint style="success" %}
**Key Points:**&#x20;

It is recommended that the retention period be set to a maximum of 24 hours to ensure smooth data access for live agent use cases and enable timely data exports.
{% endhint %}

For example, if the retention period is set to 10 minutes, any PII data in the conversation is automatically masked the next time the process runs after the 10-minute window.

You can set the `Retention period` when `Information masking` is enabled from the `Settings` page:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FhsBXv2zgpmxkzbJdjfqM%2FRetension.png?alt=media&#x26;token=fd6d8d85-33b3-48e2-a6cc-b949c4cfd4e8" alt=""><figcaption></figcaption></figure>

See [Retention period](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#retention-period), for more information.

### Improved response masking: Now only PII data is masked&#x20;

In this release, enhanced the response node masking functionality. Previously, the entire response was masked if [skill level](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill) and [node level](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#mask-response) masking were enabled. With this improvement, only the PII data within agent responses is masked, while the rest of the response remains visible.

This enhancement provides greater clarity by allowing you to see the non-sensitive parts of the response, making it easier to understand the conversation flow. It also significantly improves debugging and troubleshooting, as you can now review the visible parts of the response without compromising sensitive data.

{% hint style="info" %}
**Key point:** This behavior is `enabled by default` for all agents created after the feature rollout. For agents created prior, you can manually enable masking from the [Agent Settings page](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#enable-information-masking), or contact Avaamo Support for assistance.
{% endhint %}

| Before 9.0                                                                                                                                                                                                                                                                                                                             | After 9.0                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFAPvV16MXh7g8uxB2QB6%2FScreenshot%202025-04-15%20at%202.32.48%E2%80%AFPM.png?alt=media&#x26;token=fead020f-a823-4404-b754-f0eec0b534f9" alt=""><figcaption></figcaption></figure></div> | <div><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdhavwMVhoZxgO8R8PH00%2FScreenshot%202025-04-15%20at%202.21.09%E2%80%AFPM.png?alt=media&#x26;token=c0be4e4c-7dae-4a96-b08b-f04645f6cf9f" alt=""><figcaption></figcaption></figure></div> |

### Enhanced Agent details API response with masking information

In this release, the `Agent details API` has been updated to include the following new response attributes with masking configuration details:

| Field                             | Description                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| realtime\_masking\_enabled        | Indicates whether real-time masking is enabled for the agent or not.                 |
| api\_masking\_enabled             | Indicates if masking via API is enabled or not for the agent.                        |
| retention\_period                 | Defines the retention period for the agent, measured in minutes.                     |
| mask\_responses\_from\_all\_nodes | Indicates if masking responses from all nodes is enabled or not for the agent.       |
| system\_entity\_types             | An array of system entity types that are masked.                                     |
| custom\_entity\_types             | An array of custom entity types that are masked.                                     |
| response\_masking\_pattern        | An array of regular expression patterns that must be masked in the agent's response. |
| user\_properties                  | An Array of custom and system user attributes that are masked.                       |

See [Agent details API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/agent-details), for more information.

## Usage reports - Track your product usage in one place

You can now access all your billing and usage statistics for LLaMB, Voice, and SMS in a centralized new `Usage reports` section—designed for admins and user groups to monitor product usage in your account.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJIQTrorRi8X4z8uBXO8a%2FUsage.png?alt=media&#x26;token=623f1606-2c9e-467e-844d-2985476612c5" alt=""><figcaption></figcaption></figure>

**What you can track:**

* **LLaMB Usage**\
  See how many queries are generated and gain real-time insights to optimize usage. In the previous release, `LLaMB usage`  page was accessible from the top menu, now it is centralized and moved under `Usage reports` section. See [LLaMB Usage](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage), for more information.
* **SMS Usage**\
  Monitor how many SMS messages were sent and get an understanding of your expected billing for each month. In the previous release, `SMS usage`  was a separate page in the `Settings` section, now it is centralized and moved under `Usage reports` section. See [SMS usage,](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/sms-usage) for more information.
* **Voice Usage**\
  Provides insights into voice usage associated with the company’s license configuration. It allows you to track the number of incoming and outgoing calls made on your account. See [Voice Usage](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/voice-usage), for more information.

Everything you need to understand and manage your usage for LLaMB, Voice, and SMS—is now in one easy-to-access place.&#x20;

## Cookie expiry setting for better session management

In this release, the `Security` section in the `Web channel` configuration page has been enhanced with an option `Cookie expires in (hours)` option.&#x20;

**Key highlights**:

* Set how long browser cookies stay active (between 1–8760 hours). You cannot set the value to **zero.**
* Helps auto-expire user sessions after inactivity, improving session management
* Once expired, users see: *"Please check your network connection"* and must refresh to restart the conversation
* If no value is set, the default expiry duration is 1 year.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfL7JXsODxokBjCFqgmtI%2FScreenshot%2006-05-2025%20at%2014.52.png?alt=media&#x26;token=c9b6ca51-c4a0-4f82-8eab-fb5a52593300" alt=""><figcaption></figcaption></figure>

See [Security](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/security), for more information.

## Disable co-reference for agents without context

In this release, the agent configuration option has been enhanced with `Disable co-reference query generation` under the `Settings` tab. This enhancement allows Classic agents with LLaMB skill to maintain or ignore conversational context based on specific use cases, giving you greater control over how user inputs are interpreted.

Navigate to `Configuration>Settings` in the left navigation menu, and locate the option `Disable Co-reference query generation` under Advanced features.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FhrXpsi9cdXDgsY7MXQK1%2FScreenshot%202025-04-10%20at%209.20.10%E2%80%AFPM.png?alt=media&#x26;token=6eb7f8ae-c6da-4a09-a417-7dbb0f517136" alt=""><figcaption></figcaption></figure>

See [Disable Co-reference query generation](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#disable-co-reference-query-generation), for more information.

## Enable debug logs for easier troubleshooting

In this release, the `Settings` section on the configuration page has been enhanced with the option `Enable debug logs`.&#x20;

**Key highlights**:

* Toggle debug logs on or off at the agent level
* Especially useful when masking is enabled, as logs are otherwise suppressed
* When enabled all logs generated using `console.log` are displayed.
* When the checkbox is unchecked, logging is disabled, and no logs are displayed.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbPLGJWHqUkRWyuV5od4n%2Fdebug%20log.png?alt=media&#x26;token=c4387af8-41f8-4311-a699-0118ee19073e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notes:**&#x20;

1. By default, this option is **disabled**.
2. `Enable debug logs` setting is preserved during pull and promotion.
   {% endhint %}

See [Enable debug logs](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#enable-debug-logs), for more information.

## Disable incoming request authorization in MS Teams channel

In this release, the [Microsoft Teams (MS Teams)](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams) channel configuration has been enhanced with the `Disable Incoming Request Authorization` checkbox option under the `Security Options` tab.&#x20;

**Key highlights**:

* By default, the platform authenticates all requests from Microsoft Azure
* You can now choose to disable this authentication using a checkbox
* When enabled: unauthorized requests return a 400 Bad Request
* When disabled: unauthorized third-party requests are blocked with a 403 Forbidden

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F40H6spHu95cECIl6gAvb%2Fdisable%20incoming%20request%20auth.png?alt=media&#x26;token=ace75e75-1435-4319-acaf-744a75422abc" alt=""><figcaption></figcaption></figure>

See [Microsoft Teams (MS Teams)](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.

## Customize wait-time audio

In this release, the Conversational IVR (C-IVR)  channel configuration now includes an option to upload a custom wait time tone. You can customize the wait time tone by uploading an audio file that plays an idle tone for the user.&#x20;

{% hint style="success" %}
**Key points**:

* The upload option becomes available once the `Enable wait time tone` setting is enabled. Click **Select File**, then choose and upload the desired file for the wait time tone.
* &#x20;The file must not exceed 10 seconds in duration and must be within 5 MB in size.
  {% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Faw29T0GI2wntkos6QJmU%2Fimage.png?alt=media&#x26;token=f85d09c7-809d-4476-a771-3a5bdc3c540b" alt=""><figcaption></figcaption></figure>

See [Conversational IVR (C-IVR) or Phone](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.

## Changes

### Enable markdown format&#x20;

In this release, the location of  `Enable Markdown Format` option has been changed in the Web, Mobile (Android, iOS), and Custom channel configurations as follows:

#### Web, Android, iOS

| Before 9.0                                                                                                                                                                                                          | After 9.0                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Widget Configuration -> Use MD format                                                                                                                                                                               | Advanced settings -> LLaMB Settings. See [Enable Markdown format](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#enable-markdown-format), for more information. |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdzujI2aCQbwmjgC4jfhR%2Fimage.png?alt=media\&token=af331022-1a06-4194-b30c-d60f29e6c637) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FA72CiYz6cYs1KS7rAUAq%2Fimage.png?alt=media\&token=3904ef12-e1fe-41cf-b02b-00af6bdec6cb)  |

#### Custom channel

| Before 9.0                                                                                                                                                                                                          | After 9.0                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Appears on the first custom channel configuration page where you specify the initial custom channel settings                                                                                                        | Appears after saving the initial custom channel configuration in the LLaMB settings section. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#configure-custom-channel), for more information.                           |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNN9ANlzFNVnYbkdRoh6s%2Fimage.png?alt=media\&token=282e0298-929e-4212-b8fb-7bf0f981d1bd) | <div><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7aKHvKGLiw7khhqCjO4l%2Fimage.png?alt=media&#x26;token=41006276-decc-455f-8abd-085ce7d6e14b" alt=""><figcaption></figcaption></figure></div> |

### **Mask user IP on the Privacy page**

In this release, the `Mask user IP` toggle at the company level on the [Privacy](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/privacy) page has been removed.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQxNTwfo7ZAE7mOQHAGsV%2Fimage.png?alt=media&#x26;token=a22077f6-3873-4a3c-bd0d-b17cb928f545" alt=""><figcaption></figcaption></figure>

Since all the masking configurations are at the agent level, to maintain consistency, the `Mask user IP` option is now available at the agent level masking and is enabled by default for all new agents. See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more information. To configure IP address masking specific to your agent, contact `Avaamo Support`.

{% hint style="info" %}
**Notes**:&#x20;

* Only the location of the Mask User IP option has been changed from the company level to the agent level, the functionality of this feature remains unchanged.
* If Mask user IP is enabled for your company before the 9.0.0 release, then all the agents in the company have this option enabled by default after the upgrade. &#x20;
  {% endhint %}

### Refreshed UI for the Login page

In this release, the user interface (UI) of the Avaamo platform's `Login` page has been revamped with a modern UI, featuring a refreshed color scheme, improved layout, and refined typography to deliver a fresh look for the 9.0 release.&#x20;

{% hint style="info" %}
**Note**: Only the UI of the `Login` page has been refreshed in the 9.0.0 release. The login functionality remains unchanged.
{% endhint %}

#### Login page before the 9.0 release:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJCmIrpa25BBA60F0mtBm%2Fimage.png?alt=media&#x26;token=4876b893-af09-47f3-b6b3-936189b3d33d" alt=""><figcaption></figcaption></figure>

#### Login page after the 9.0 release:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEEOSPSfJ9dtqoN0ieIK0%2FScreenshot%2004-04-2025%20at%2014.11.png?alt=media&#x26;token=282d0c2d-fdbf-4ef1-9ae9-e6a99f49504b" alt=""><figcaption></figcaption></figure>

### "Standard agent" is now "Classic agent"

In this release, we are renaming the `Standard agent` to `Classic agent` to improve nomenclature consistency and support a clearer understanding of available agent experiences as the platform evolves.

You can view this change on the agent creation page, where you can now select `Classic agent` instead of `Standard agent` from the `Create` dropdown.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fq86WHflkt9WkbvJx82JL%2Fimage.png?alt=media&#x26;token=4500015a-4511-4950-91e5-9064b31ff93a" alt=""><figcaption></figcaption></figure>

### Domain configuration now centralized under Web Channel settings

In this release, the option `Mention the domain to which the web channel resources are allowed to be loaded` has been removed from the [Security Policy](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/security-policy) page.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FRYm7jJ4CGvwFbtzdN7ti%2FScreenshot%202025-04-21%20at%206.19.51%E2%80%AFPM.png?alt=media&#x26;token=0d419e5b-6829-4cee-86fb-a66e778b6d1b" alt=""><figcaption></figcaption></figure>

The configuration has been moved to the `Web Channel > Security > Allowed Domains` section for more effective management. Ensure that all allowed domains are specified here.

&#x20;Refer [Security](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/security), for more information.
