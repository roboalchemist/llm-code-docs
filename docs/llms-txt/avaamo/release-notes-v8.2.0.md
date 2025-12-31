# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.2.0.md

# Release notes v8.2.0

The Avaamo Conversational AI Platform v8.2.0 release includes **one new feature** and **7 enhancements.**&#x20;

## New feature - Introducing DataSync AI

This release introduces a new feature referred to as `DataSync AI`**.**&#x20;

The `DataSync AI` is a powerful feature within [LLaMB](https://docs.avaamo.com/user-guide/llamb) designed to facilitate seamless content access across repositories such as `SharePoint` and `ServiceNow`. It acts as an interface, enabling users to leverage resources stored in these repositories to enhance the capabilities of their LLaMB agents in responding to user queries effectively from the enterprise content.&#x20;

The following flow diagram illustrates the workflow of the DataSync AI.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4kJcP19lVTpGmM6sLhxM%2FContent%20connector.png?alt=media&#x26;token=f1754dc6-0f0e-4630-a9e4-12f4d0bab0f7" alt=""><figcaption></figcaption></figure>

See [Introducing DataSyncAI](https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.2.0/whats-new-v8.2.0-introducing-datasync-ai), for more information.

## Enhancements

These enhancements are categorized according to the modules within the Avaamo Conversational AI Platform for streamlined navigation.&#x20;

This release includes enhancements related to the following existing features:

<table><thead><tr><th width="225">Module</th><th>Enhancements</th></tr></thead><tbody><tr><td>Built-in Skills</td><td><a href="#enhanced-personalization-outro-message-support">Enhanced personalization: Outro message support</a></td></tr><tr><td>Live agent Console</td><td><a href="#enhanced-personalization-live-agent-translation-for-avaamo-live-agent">Enhanced personalization: Live agent translation for Avaamo Live Agent</a></td></tr><tr><td>MS Teams </td><td><a href="#improved-user-experience-show-more-toggle-to-render-long-responses-in-ms-teams-channel">Improved user experience: Show more toggle to render long responses in MS Teams channel</a><br><a href="#improved-user-experience-table-rendering-for-llamb-responses-in-microsoft-teams">Improved user experience: Table Rendering for LLaMB Responses in Microsoft Teams</a></td></tr><tr><td>Outreach</td><td><a href="#outreach-insight-api-filter-campaigns-using-multiple-campaign-ids-and-user-properties">Outreach insight API: Filter campaigns using multiple campaign IDs and user properties </a></td></tr><tr><td>C-IVR improvements</td><td><a href="#improved-asr">Improved ASR</a></td></tr><tr><td>Accessibility enhancements</td><td><a href="#improved-voice-over-narration-for-card-elements">Improved voice-over narration for card elements</a></td></tr></tbody></table>

{% hint style="danger" %}
**Deprecation notice**: See [Deprecated features,](https://docs.avaamo.com/user-guide/deprecated-and-removed-features/v8.2.0-deprecated-features) for all the deprecated features in the `v8.2.0` release.
{% endhint %}

### Enhanced personalization: Outro message support

In this release, the personalization experience with the user has been enhanced with a new  `Outro` feature.

This enhancement allows you to create and post a customized message to the user after an agent’s response. It is beneficial for skills that provide one-off replies, such as [Dynamic Q\&A ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a)and [LLaMB](https://docs.avaamo.com/user-guide/llamb) skills as it improves the user experience by providing a clear, standardized message after the agent responds as per your business requirement. It helps to streamline and provide consistent communication across all interactions.&#x20;

A common use case is to post disclaimers or system-generated messages, such as `This is a system-generated message, please do not reply` after the agent's response say in a Q\&A skill.&#x20;

In the following illustration, the outro message is configured to be displayed for all the Dynamic Q\&A responses:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FS8EzIyud5pTDbuGwushP%2Frelease%20copy.png?alt=media&#x26;token=0c4aa161-5a60-4259-9cf0-2945e24d2fa3" alt=""><figcaption></figcaption></figure>

In the agent response, the message configured in the outro skill is displayed after the agent's response:

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQXMGPtdAl02wb4KbG5pz%2Frelease1%20copy.png?alt=media&#x26;token=175d29e6-62d0-4828-b9e3-f2ba7d19dac4" alt="" width="375"><figcaption></figcaption></figure></div>

See [Outro skill](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent#outro-skill), for more information.

### Enhanced personalization: Live agent translation for Avaamo Live Agent

This release enhances language support for live agent transfers by enabling real-time translation between the end user and the live agent.&#x20;

Users can now chat with live agents in 100+ supported languages on the Avaamo Platform, while agents continue to communicate in English. The end-user's language is translated into English for the live agent, and the agent's response is translated back into the user's language. This seamless real-time translation ensures smooth communication when a conversation is transferred to a live agent.

Key advantages of this feature include:

* **Personalized User Experience:** Users can communicate in their native language, enhancing the overall interaction.
* **Cost and Maintenance Reduction:** Live agent translation removes the need for a multilingual agent team, allowing customers to communicate in their preferred languages. This feature enables businesses to cater to a diverse customer base without requiring agents to be fluent in every supported language, optimizing staffing and minimizing the risk of miscommunication.
* **Improved Operational Efficiency:** The need for specific routing rules to detect the user's language and direct them to the appropriate live agent is eliminated, streamlining the process.

Here's an example that demonstrates live agent translation where the user's local language is French:

* **End user to Live agent**: Messages from the end user in French are translated into English for the live agent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6Dnc70kY0v15019Y1krC%2Frelease2%20copy.png?alt=media&#x26;token=4a001d2b-4ef2-4bb0-b424-b44dd3452ca2" alt=""><figcaption></figcaption></figure>

* **Live agent to End User**: Responses from the live agent in English are translated back to French for the end user.

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLrPfDUZvNb2hQQmOYfPt%2Frelease4.png?alt=media&#x26;token=d94d86c7-f931-4c95-a83b-abbba7290fb6" alt="" width="375"><figcaption></figcaption></figure></div>

See [Live Agent Translation](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/live-agent-translation)[,](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent) for more information.

### Improved user experience: Show more toggle to render long responses in MS Teams channel

In the release, the MS Teams channel configuration page has been enhanced with a new `Enable Show more button` option.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FP3dMPxjr80XmZHGu4Cuj%2Fscreencapture-c6-avaamo-2024-08-23-14_40_30.png?alt=media&#x26;token=c0017936-0551-4e14-ab16-58f312a0071f" alt=""><figcaption></figcaption></figure>

This feature is designed for streaming responses and is useful when displaying summarized lengthy responses from LLaMB in the MS Teams channel. When enabled, it renders a partial response with a `Show more` button, enabling users to expand content gradually.&#x20;

This enhances the user experience by quickly displaying partial messages, reducing the wait time for full message rendering. This approach enhances clarity and streamlines the user experience effectively.

{% hint style="info" %}
**Note**: `Show more` option is displayed only when responses are rendered from the LLaMB skill.
{% endhint %}

See [MS Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.

### Improved user experience: Table Rendering for LLaMB Responses in Microsoft Teams

In this release, the table rendering process in agent's responses is significantly improved.&#x20;

Previously, users had to click the **View Table** button to view the entire table in a separate popup window. While this approach provided a focused view, it required additional user interaction to access the content.&#x20;

Now, instead of displaying the **View Table** button, tables are directly rendered within the chat screen itself, allowing for immediate access to the data without any extra steps.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVDKVL9eD6MRRWF59OyU3%2FScreenshot%2028-08-2024%20at%2014.13.png?alt=media&#x26;token=65c52433-0642-492a-b96b-9a8a5e078f7b" alt=""><figcaption></figcaption></figure>

This enhancement streamlines the user experience by eliminating the need for popups and allowing users to view table data in line with their conversation. This update simplifies the workflow, reduces interruptions, and enhances the overall user interaction with table data.

See [MS Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.

### Outreach insight API: Filter campaigns using multiple campaign IDs and user properties&#x20;

In this release, we have enhanced the outreach insights API with the following:

1. **Multiple Campaign ID Filtering**: You can now filter campaigns using multiple campaign IDs. Previously, this feature was limited to a single campaign ID, restricting the scope of your analysis. With this enhancement, you can gain insights across various campaigns simultaneously, providing a broader understanding of your outreach performance.
2. **Filter the messages using user properties:** This allows users to filter campaigns using predefined, fixed [user properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties). This enhancement helps quickly locate and manage messages based on standard user attributes. \
   Example: `first_name` , `last_name`

See [Outreach Insights API](https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/outreach-insights-api), for more information.

### Improved ASR

In this release, Automatic Speech Recognition (ASR) has been fine-tuned with a new and improved model. The following are some of the key benefits of the new ASR model:

* Better quality recognition
* Better extraction of alphanumerics

### Improved voice-over narration for card elements

When an agent response contains a card element, VoiceOver now narrates the message: `'Bot sent, Card. Use Shift  Tab to navigate through the items.'`  Previously, it narrated the message as `'Bot sent, Card'.`This functionality is designed to enhance the accessibility of the system, particularly for those who use assistive technologies to interact with content.

This helps the users who use assistive technologies be properly informed about available navigation shortcuts, improving the overall accessibility and usability of the interface.

{% hint style="info" %}
**Note:** Use standardized selectors when applying CSS. Relying on non-standard selectors like `aria-label` or others may lead to design inconsistencies when displaying content in the agent interface.
{% endhint %}
