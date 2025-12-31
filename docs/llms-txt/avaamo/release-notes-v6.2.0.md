# Source: https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.2.x/release-notes-v6.2.0.md

# Release notes v6.2.0

The Avaamo Conversational AI Platform v6.2.0 release includes 13 enhancements and 1 change distributed as follows:

**Enhancements**: In order to make the navigation around the enhancements easier, they are classified as follows based on the modules in the Avaamo Conversational AI Platform:

<table><thead><tr><th width="155.5338606984372">Module</th><th width="590.4285714285713">Enhancements</th></tr></thead><tbody><tr><td>Accessibility</td><td><ul><li><a href="#enhance-agent-accessibility-with-consistent-navigation-and-voice-over-rendering">Enhance agent accessibility with consistent navigation and voice-over rendering</a></li></ul></td></tr><tr><td>Dialog Designer</td><td><ul><li><a href="#upload-files-audios-and-videos-in-q-and-a-and-smalltalk">Upload files, audios, and videos in Q&#x26;A and Smalltalk</a></li></ul></td></tr><tr><td>Channel</td><td><ul><li><a href="#show-agent-typing-animation-while-waiting-for-agent-response-in-ms-teams-channel">Show agent typing indicator while waiting for agent response in MS Teams channel</a></li></ul></td></tr><tr><td>Live agent</td><td><ul><li><a href="#protect-interactions-with-live-agents-by-not-recording-them">Protect interactions with live agents by not recording them</a></li><li><a href="#analyze-all-the-live-agent-interventions-in-the-improved-agent-intervention-analytics">Analyze all the agent interventions in the improved Agent intervention analytics</a></li></ul></td></tr><tr><td>Masking</td><td><ul><li><a href="#provide-developers-flexibility-to-control-and-manage-agent-response-masking">Provide developers flexibility to control and manage agent response masking</a></li></ul></td></tr><tr><td>Query insights</td><td><ul><li><a href="#search-and-export-results-using-timezone-in-query-insights-to-interpret-results-accurately">Search and export results using timezone in Query insights to interpret results accurately </a> </li><li><a href="#performance-improvements-for-message-api-and-query-insights-api">Performance improvements for Message API and Query insights API</a></li></ul></td></tr><tr><td>Answers</td><td><ul><li><a href="#use-document-name-for-card-title-in-answers-skill-response">Use document name for card title in Answers skill response</a></li><li><a href="#improve-accuracy-with-the-right-model-based-on-the-content-in-the-answers-skill">Improve accuracy with the right model, based on the content in the Answers skill</a></li><li><a href="#fine-tune-language-specific-responses-in-the-answers-skill">Fine-tune language-specific responses in the Answers skill</a></li><li><a href="#add-chunk-preview-url-for-answers">Add chunk preview URL for Answers</a></li><li><a href="#improved-answer-prediction-api">Improved Answer prediction API</a></li></ul></td></tr></tbody></table>

**Changes:** This release includes changes related to the following existing features:

1. [Trim text response toggle in the Answers configuration ](#trim-text-response-toggle-in-the-answers-configuration)

{% hint style="danger" %}
**Deprecation notice**: In this release, the agent widget support on the Internet Explorer browser is deprecated. See [Deprecation notice](#deprecation-notice), for more information.
{% endhint %}

## Component-wise distribution

The following table lists the component-wise distribution of enhancements and changes in the v6.2.0 release:

{% tabs %}
{% tab title="Enhancements" %}

<table><thead><tr><th width="277.7125091441112">Enhancements</th><th width="435.85714285714283">Component</th></tr></thead><tbody><tr><td><a href="#enhance-agent-accessibility-with-consistent-navigation-and-voice-over-rendering">Enhance agent accessibility with consistent navigation and voice-over rendering</a></td><td><ul><li>Agent widget</li></ul></td></tr><tr><td><a href="#upload-files-audios-and-videos-in-q-and-a-and-smalltalk">Upload files, audios, and videos in Q&#x26;A and Smalltalk</a></td><td><ul><li>Dynamic Q&#x26;A -> Skill response </li><li>Smalltalk -> Skill response</li></ul></td></tr><tr><td><a href="#show-agent-typing-animation-while-waiting-for-agent-response-in-ms-teams-channel">Show agent typing indicator while waiting for agent response in MS Teams channel</a></td><td><ul><li>MS Teams channel</li></ul></td></tr><tr><td><a href="#protect-interactions-with-live-agents-by-not-recording-them">Protect interactions with live agents by not recording them</a></td><td><ul><li>Configuration -> Live agent</li><li>Debug -> Conversation history</li></ul></td></tr><tr><td><a href="#analyze-all-the-live-agent-interventions-in-the-improved-agent-intervention-analytics">Analyze all the agent interventions in the improved Agent intervention analytics</a></td><td><ul><li>Monitor -> Agent intervention</li><li>Monitor -> Query insights</li><li>REST APIs -> Agent intervention API <code>https://cx.avaamo.com</code><br><code>/bots/analytics/{{agent_id}}/agent_intervention.json</code></li></ul></td></tr><tr><td><a href="#provide-developers-flexibility-to-control-and-manage-agent-response-masking">Provide developers flexibility to control and manage agent response masking</a></td><td><ul><li>Configuration -> Settings</li></ul></td></tr><tr><td><a href="#search-and-export-results-using-timezone-in-query-insights-to-interpret-results-accurately">Search and export results using timezone in Query insights to interpret results accurately </a> </td><td><ul><li>Monitor -> Query insights</li></ul></td></tr><tr><td><a href="#performance-improvements-for-query-insights-api">Performance improvements for Message API and Query insights API</a></td><td><ul><li>REST APIs -> Message API </li></ul><p><code>https://cx.avaamo.com/v1/messages.json</code></p><ul><li>REST APIs -> Query insights API <code>https://cx.avaamo.com</code><br><code>/bots/analytics/{{agent_id}}/agent_intervention.json</code></li><li>All APIs where <code>per_page</code> parameter is used</li></ul></td></tr><tr><td><a href="#use-document-name-for-card-title-in-answers-skill-response">Use document name for card title in Answers skill response</a></td><td><ul><li>Answers -> Configuration</li></ul></td></tr><tr><td><a href="#improve-accuracy-with-the-right-model-based-on-the-content-in-the-answers-skill">Improve accuracy with the right model, based on the content in the Answers skill</a></td><td><ul><li>Answers -> Configuration</li></ul></td></tr><tr><td><a href="#fine-tune-language-specific-responses-in-the-answers-skill">Fine-tune language-specific responses in the Answers skill</a></td><td><ul><li>Answers -> Configuration</li></ul></td></tr><tr><td><a href="#add-chunk-preview-url-for-answers">Add chunk preview URL for Answers</a></td><td><ul><li>Answers -> Implementation -> Document groups -> Knowledge -> Sections</li></ul></td></tr><tr><td><a href="#improved-answer-prediction-api">Improved Answer prediction API</a></td><td><ul><li>REST APIs -> Answer Prediction API <code>https://mx.avaamo.com/answers/v2/process-query</code></li></ul></td></tr></tbody></table>
{% endtab %}

{% tab title="Change" %}

| Change                                                                                                             | Component                |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| [Trim text response toggle in the Answers configuration ](#trim-text-response-toggle-in-the-answers-configuration) | Answers -> Configuration |
| {% endtab %}                                                                                                       |                          |
| {% endtabs %}                                                                                                      |                          |

## Enhancements

### Enhance agent accessibility with consistent navigation and voice-over rendering

In this release, the Accessibility inclusivity in the agents built using Avaamo Conversation AI Platform has been improved. This release makes the agents easily accessible by providing a  uniform and consistent approach for navigating elements in the agent widget.

The following are a few key enhancements incorporated in this release:

* Top to bottom navigation: The tab order follows the visual flow of the agent - `top to bottom` and `left to right` flow with the exception of when the agent is launched for the first time. In this case, the first focus is on the `Type a Message` text area.
* Link navigations:&#x20;
  1. All inputs, buttons, links, and divs follow `top to bottom, left to right` navigation flow.&#x20;
  2. Users can use `tab` and `shift + tab` keys to navigate from one element to another.
  3. Example: Buttons in Quick reply, Persistent Menu, Links, inputs, and buttons navigation in Cards. Use `tab` and `shift + tab` keys.&#x20;
* Skip links: Enable user to navigate from header to typing text area at the bottom. See [Skip links](http://web-accessibility.carnegiemuseums.org/code/skip-link/), for more information. Note that the skip link is accessed only via the keyboard, specifically by pressing the `Tab` key only when the focus is at the topmost header element in the agent.
* Cards in a Carousel: Navigation starts from the `left (left arrow key)` through the last element (`right arrow key`).
* Arrow (`Up and down`) navigation for message conversations in the agent:

<table><thead><tr><th>User action</th><th width="150">Windows</th><th width="343">Mac OS</th></tr></thead><tbody><tr><td>Move up one interaction</td><td><code>Page Up</code></td><td><code>Function + Option + Up Arrow</code></td></tr><tr><td>Move down one interaction</td><td><code>Page Down</code></td><td><code>Function + Option + Down Arrow</code></td></tr><tr><td>Jump to the first interaction</td><td><code>Home</code></td><td><code>Function + Option + Left Arrow</code></td></tr><tr><td>Jump to the last interaction</td><td><code>End</code></td><td><code>Function + Option + Right Arrow</code></td></tr></tbody></table>

* Voice-Over improvements: Consistent rendering of elements using improved aria-labels.
  * Improved Aria-labels on cards, links, buttons, and images&#x20;
  * Improved Aria-live on notification&#x20;
  * Improved Input aria-labels

{% hint style="info" %}
**Note**:&#x20;

* The keyboard shortcuts are based on the [W3C's ARIA 1.2 authoring practice example](https://www.w3.org/TR/wai-aria-1.2/#feed) for navigating feeds.
* All focus states have been designed to meet the current iteration of [WCAG 2.2's forthcoming Focus Appearance (Minimum) criterion](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/#2411-focus-appearance-minimum-aa).
  {% endhint %}

### Upload files, audios, and videos in Q\&A and Smalltalk

In this release, the available response types in the Dynamic Q\&A skill and Smalltalk have been enhanced with the following:

* Files
* Audio
* Video

Using these response types, you can build a conversation flow allowing users to upload files, audio, and video for any Q\&A or Smalltalk responses. The following illustration depicts the newly added response types in the Dynamic Q\&A skill. Similar response types are displayed in the Smalltalk skill -> Prompt details pop-up window:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FY1u4qAiU6JF5Xv5Fnznw%2F6.2-response-types-qa-smalltalk.png?alt=media\&token=fb15d71a-d7f2-4392-8e27-9400f2a85ae6)

In the previous release, [Files](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#files), [Audio](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#audio), and [Video](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#video) response types were available only in the Dialog skill responses.&#x20;

### Show agent typing indicator while waiting for agent response in MS Teams channel

In this release, the user experience interacting with the Avaamo agent in the MS Teams channel has been enhanced by displaying an agent typing indicator to the user while they wait for the agent's response. Typically, this is useful when you have external API calls to generate agent responses where you can expect some delay in responses.

{% hint style="success" %}
**Key points:**

* When the agent response contains multiple replies, then the typing indicator is visible only for the first agent reply.&#x20;
* There is a default timeout of 20 seconds for the typing indicator. If the agent replies in 2 seconds, then the typing indicator gets disabled in 2 seconds. If the agent fails to reply to the user query, then the typing indicator is visible for 20 seconds.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FaSkow7MUIeg8WZ6E3boH%2FScreenshot%202022-08-08%20at%203.50.22%20PM.png?alt=media\&token=e01b982d-e169-4645-b5dc-d3fbb12b2f9b)

See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on the MS Teams channel.

In the earlier release, there was no typing indicator displayed in the MS Teams channel while waiting for the agent's response. This caused confusion as it was unclear to the user whether the agent has stopped responding or the user had to wait for the agent's response.

### Protect interactions with live agents by not recording them

Typically, in certain domains such as Banking and Finance, a user’s interaction with a live agent can capture sensitive details such as the user’s identification number, policy number, and email (to name a few). Therefore, it is critical to audit the data and protect data privacy in such cases.

Hence, as a part of protecting PII/PHI/GDPR compliance data of the live agent interactions within the Avaamo Conversational AI system, a new toggle button **Save conversations** has been introduced in this release. Using this option, you can choose to not record the live agent interactions in the agent conversation history. This option is available in the Agent -> Configuration -> Live agent page.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FTR0ddiaNnV1wOgBJqe2e%2F6.2-save-live-agent-data.png?alt=media\&token=8dda6ed4-adb8-4b85-b079-847e28ecba7e)

See [Configure live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#configure-live-agent), for more information.

{% hint style="success" %}
**Key points**:

* Avaamo Conversational AI platform has always been GDPR compliant. Information masking can be used to protect PII/PHI/GDPR compliance data. See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more information.&#x20;
* This enhancement is applicable only to all the live agent conversations saved in the Avaamo platform. The live agent conversation data in the external live agent systems such as Oracle, Zendesk, or any custom live agents must be handled separately by the respective systems according to the business requirements.
* If the **Save conversations** toggle is set to **No**, then no data or chat conversations between the users and live agents are saved in the Avaamo platform. At the specific section in the Conversation history page, a system message indicating the same is displayed. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-conversation-history), for more information.
  {% endhint %}

### Analyze all the live agent interventions in the improved Agent intervention analytics

In this release, the **Agent intervention** analytics board has been enhanced to capture the following details:

* Transfers to live agents triggered via JavaScript code. See [Transfer to live agent using JS](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/transfer-to-live-agent), for more information.
* Transfers to live agents triggered using commands such as `#transfer to agent / #talk to agent`. See [Agent commands](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/skill-commands), for more information.
* Transfers to live agent triggered via C-IVR channel.&#x20;
  * See [Call forward](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses#call-forward), for more information.
  * See [SmartCall.forward](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/forward-call-c-ivr-channel), for more information.

{% hint style="success" %}
**Key points**:&#x20;

* From the v6.2.0 release onwards, Agent intervention data and Agent intervention API displays the actual count of agent transfers irrespective of the way it is called or the channel it is triggered from.&#x20;
* Post v6.2.0 upgrade, for the historical data, in addition to the actual agent transfer, [silent switch](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#live-agent-transfer-rules) is also considered. Hence, you may notice a spike in the agent intervention analytics for the existing agents after the v6.2.0 upgrade.
* To ensure data consistency, the Agent intervention API has been updated in the v6.2.0 release to get the statistics of the actual live agent transfers by the users. In the previous release, the Agent intervention API would get the statistics on the live agent transfers requested by the users. See [Agent intervention API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/agent-intervention), for more information.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbKzasXlnguP04D04ku%2F-MbKzwnQEVBMPvH8HVPp%2F5.7-analytics-agent-intervention.png?alt=media\&token=20621c98-9f79-406b-9126-3b780a732637)

With this feature, a new concept of System tags has been introduced in this release. These are in-built tags that are maintained internally by the Platform. See [Tags](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-tags), for more information.&#x20;

In the previous release, the **Agent intervention** analytics board only captured system live agent interactions that are configured using the **Configuration -> Live agent** option. Live agent transfers triggered via a JavaScript code or via the C-IVR channel were not captured in the **Agent intervention** analytics board.

See [Agent intervention ](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#agent-intervention)for more information.

### Provide developers flexibility to control and manage agent response masking

In this release, developers have the flexibility to control masking at the agent level using the **Information masking** toggle button in the Agent -> Configuration -> Settings page. With this enhancement, developers can:

* Fully control and manage agent response node-level masking without having to contact Avaamo Support.&#x20;
* Use this toggle to test and debug masking during the development and testing phase.

{% hint style="success" %}
**Key point**: For masking user messages where patterns or entities are required, developers must still continue to contact Avaamo Support with all the required masking configurations. See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more details.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fr1quR4d7RCkzq1eg0Q7l%2F6.2-agent-level-masking.png?alt=media\&token=cb650459-eea7-4c2f-b407-2553a8b29a47)

In the previous release, even though the agent response node-level masking toggle was available in the UI, developers had to contact Avaamo Support to first enable masking at the agent level, and only then agent response node-level masking would work. The option to enable or disable masking was not exposed in the UI.

See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking) and [Enable Information masking](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#enable-information-masking), for more information.

### Search and export results using timezone in **Query insights** to interpret results accurately

In this release, the date criterion in the **Monitor -> Query insights** page has been enhanced with a new **Date range** field. This field replaces the existing "From date" and "To date" fields in the Query insights page to make the search more simple, specific, and efficient. The new **Date range** field provides options to:

* Select a date range from a set of pre-defined date filters in a single click.&#x20;
* Select a **Custom Range** to pick your own date range by selecting the start and end dates.&#x20;
* Select a timezone to search and filter the results.&#x20;

It allows you to search and export the results in the selected date and timezone from the **Query insights** page. Business users from different regions can view the exact date and timezone of the records in exported CSV and hence can interpret the results accurately.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDwM5PSF4nLUJu5uFY7Ap%2F6.2-query-insights-date-range.png?alt=media\&token=f3441f59-8d75-431e-bcf3-ac9b9c2a9a5a)

In the previous release, there was no option to select the timezone, and the user's local timezone from the browser was used in the Query insights export. This created a lot of confusion when business users in different regions downloaded the same report.

See [Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights) for more information.

### Performance improvements for Message API and Query insights API

In this release, the performance of the Message API and Query insights API has been improved to avoid timeout errors even for a high volume of data. See [Query insights API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/query-insights), for more information. With this improvement, the default `per_page` parameter for all the APIs has been changed from 5 to 25.&#x20;

{% hint style="info" %}
**Note**: The default `per_page` parameter change is backward compatible, which implies that the API will return a response when `per_page` is 5.
{% endhint %}

In the earlier release, Message API and Query insights API would result in timeout errors for a high volume of data and hence developers had to request Avaamo Support for obtaining Message API and Query insights API data. Also, with the default `per_page` size as 5, the pagination calls were more frequent, and hence for a huge volume of data, it resulted in slower performance of the APIs.

### Use document name for card title in Answers skill response

In this release, the Answers skill -> Configuration page has been enhanced with a new configuration option **Use document name for card title** in the **Display** section.&#x20;

This option allows you to enable or disable the display of the document title in the agent response when the response is rendered as HTML. When you disable the **Use document name for card title** toggle, the document title is not displayed and only the section header is displayed in the agent response.

| Use document name for card title = enabled                                                                                                                                                                                                       | Use document name for card title = disabled                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNoJevvhNgp8C87GU7SsU%2F6.2-answers-document-title-enabled.png?alt=media\&token=05401d6a-a76d-4b75-999b-0884f8b0795a) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FrCqsBU8aWOo6r7T6QugH%2F6.2answers-document-title-disabled.png?alt=media\&token=9734fe2b-9ca4-4ec5-8916-41d6735c73fb) |

See [Use document name for card title](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#use-document-name-for-card-title), for more information.

### Improve accuracy with the right model, based on the content in the Answers skill

In this release, the Answers skill -> Configuration page has been enhanced with a new configuration option **Answering mechanism** in the **Additional settings** section. This option allows you to select a relevant model to be used by the Platform for providing agent responses based on the content type in your knowledge base. The platform uses the selected model to optimize the response and hence results in better accuracy.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnCCroACAwLMi48HbFTlT%2F6.2-configure-answering-mechanism.png?alt=media\&token=8c40c85f-b895-4b62-96e2-25ca6104d3c6)

See [Answering mechanism](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#answering-mechanism), for more information.&#x20;

### Fine-tune language-specific responses in the Answers skill&#x20;

In this release, the Answers skill -> Configuration page has been enhanced with two new configuration options related to language translation.&#x20;

* **Get responses only from documents in the query language**: Display responses only from the documents in which the user query is posted.
* **Fallback to all documents**: If the response is not available in the user query language, then translated response, if available in another language document is displayed.

These options are useful when you have the same content uploaded in multiple languages. It helps you to display relevant responses to the users based on the business requirement and languages of the uploaded document. See [Translation configuration](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#translation-configuration), for more information.

### Add chunk preview URL for Answers

In this release, the Knowledge -> Sections tab has been enhanced with a **Preview URL** option. This option allows you to specify a different preview URL for each chunk or section in the extracted knowledge base based on your requirement. See [Sections](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/view-and-edit-knowledge#sections), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FoSFDlcKnKCbMdZ5yl6CZ%2F6.2-preview-url.png?alt=media\&token=b8eabc5f-f314-4417-b456-0dccc42985ae)

When a response from this section is displayed in the agent, then the **View more** link in the response navigates to the link specified in the **Preview URL** option. Instead of using a generic document URL for all the chunks, this helps you to fine-tune the responses and provide accurate navigation links that can be helpful to the users.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fta55z9CMgEZPD86Fx4GX%2F6.2-preview-url-view-more.png?alt=media\&token=8e8f4a9a-3d18-4f87-acac-dead88dab8aa)

In the earlier release, for all the chunks or sections, only the document URL was used. There was no option to specify a different URL for each chunk or section.

### Improved Answer prediction API

In this release, the Answer prediction API has been enhanced with a simpler payload for ease of use and better understandability. In the improved version, the configuration object is removed and the options specified only in the Answers -> Configuration page are considered to avoid confusion.&#x20;

The following is the API endpoint with a sample payload of the improved Answer prediction API:

```json
// API Endpoint

https://mx.avaamo.com/answers/v2/process-query

// Payload

{
    "kp_id": [1],
    "query": "What information do you collect?",
    "query_id": "xxxx",
    "query_insights": {
        "detected_language": "en-US"
    },
    "conversation_id": "xxxx",
    "request_uuid": "xxxx"
}
```

See [Answer prediction API](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/answer-prediction-api), for more information.

Earlier Answer prediction API had configuration parameters in the payload that were repeated in the UI. The API would always consider the configuration options from the UI. Hence, the response received by the API was unclear to the developers, especially when the configuration options in the API and the UI were different.

## Changes

### **Trim text response** toggle in the Answers **c**onfiguration&#x20;

In this release, the **Trim text response** toggle in the Answers skill -> Configuration page has been decoupled from **Render as HTML** toggle. You can enable or disable the **Trim text response** toggle irrespective of whether you have enabled **Render as HTML** toggle or not.&#x20;

This change is useful when the Answer skills contain a mix of content - both PDF and URLs. In such cases, you can have **Render as HTML** and **Trim text response** toggles both enabled. Here, note that although both the toggles are enabled, the **Trim text response** toggle is used and applicable only for PDF content and has no effect on the HTML content.

See [Trim text response](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#trim-text-response) and [Render as HTML](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#render-as-html), for more information.

In the earlier release, the **Trim text response** toggle was functional only when **Render as HTML** toggle was disabled as trimming a text response is not applicable for HTML documents. If the Answers skill contained both URLs and PDFs, then using both the toggle functionalities was not possible.

## :warning:Deprecation notice

In this release, the agent widget support in the Internet Explorer browser has been deprecated. It will continue to work with limited functionality. We will no longer release any fixes specific to Internet Explorer.

### Why?

Microsoft Internet Explorer is a legacy system and does not offer support for the advanced functionality offered by our platform. Microsoft has announced the end of lifecycle support for IE. See [Lifecycle policy for Internet Explorer](https://docs.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge#what-is-the-lifecycle-policy-for-internet-explorer-), for more information.

### When is the support completely stopped?

This feature will be removed from the next release onwards.

### What action to take?

Use any of the supported platform browsers. See [Supported browsers](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/overview#supported-browsers), for more information.
