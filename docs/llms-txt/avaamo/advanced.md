# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced.md

# Advanced

In the **Advanced** section, you can provide any advanced configuration such as any [additional customization parameters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#advanced-customization-parameters) or an [autocomplete URL](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#query-autocomplete-url), if required.&#x20;

You can include additional parameters to the web channel such as user information and theme.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* You can set many of these parameters from the UI also. However, setting a parameter in the customization parameters section always takes precedence over the value set in the UI.
* avm-siri theme is supported only in text-based web channels.
  {% endhint %}

{% hint style="info" %}
**Before configuring the advanced customization parameters in the web channel**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

**To add advanced customization parameters**:

* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Advanced** section, specify the key in the **Key** text box and the corresponding value. See [Customization parameters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#customization-parameters), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNpxylhyV2PdcnTpJTKcW%2FScreenshot%202025-01-22%20at%202.12.07%E2%80%AFPM.png?alt=media\&token=e50ca24a-4466-46d6-94eb-dad0bfd2dfb0)

* Click **Save** and click **Test** to test the skill. See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Customization parameters

<table><thead><tr><th width="176">Parameter Name</th><th width="343.5">Description</th><th>Values</th></tr></thead><tbody><tr><td>debug</td><td>To show the debug icon with every agent response. Useful to see the message insights.</td><td><p>true/false </p><p></p><p>Default: false</p></td></tr><tr><td>show_bot_typing</td><td><p>Show agent typing animation while waiting for agent response. </p><p></p><p>Typically used when you have external API calls to generate agent responses.  </p></td><td><p>true/false </p><p></p><p>Default: true</p></td></tr><tr><td>bot_typing_duration</td><td><p>Duration of the agent typing animation. </p><p></p><p>Typically used when you have external API calls to generate agent responses. Set it to 0 if you do not wish to use the agent typing animation.</p></td><td><p>milliseconds<br></p><p>Example: 30000 for 30 seconds. </p><p></p><p>Default: 500 milliseconds</p></td></tr><tr><td>audio_visible</td><td>Whether the voice reading feature is enabled or not.</td><td><p>true/false </p><p></p><p>Default: false</p></td></tr><tr><td>audio_on</td><td>This is to enable the speaker icon <span data-gb-custom-inline data-tag="emoji" data-code="1f508">🔈</span> in the chat widget.</td><td><p>true/false </p><p></p><p>Default:false</p></td></tr><tr><td>theme</td><td>The color scheme of the web channel</td><td><p>avm-messenger</p><p>avm-blue</p><p>avm-red</p><p>avm-orange</p><p>avm-green</p><p>avm-siri </p><p>avm-mercury</p><p></p><p>Default: avm-mercury</p></td></tr><tr><td>draggable</td><td>Whether the embedded web channel window is draggable around the page or not.</td><td><p>true/false </p><p></p><p>Default: false</p></td></tr><tr><td>history</td><td><p>Whether to show the previous history of messages on page load or not. </p><p></p><p>Note that when you set history=false, the conversation history is still available, but the past conversation in the agent is cleared to the users when they open the agent in the browser tab. Hence, only the greeting message is displayed to the user and not the past conversations.</p></td><td><p>true/false </p><p></p><p>Default: true</p></td></tr><tr><td>voice_auto_send</td><td>Whether to send the voice message automatically </td><td>true/false</td></tr><tr><td>collect_info</td><td>Whether to ask the user for email, first name, and last name before allowing access to the web channel or not</td><td><p>true/false </p><p></p><p>Default: false</p></td></tr><tr><td>scroll_behaviour</td><td><p>Decides if the agent must scroll to the top or bottom. </p><p></p><p><strong>show_full_response</strong>: Scrolls to the top of the first agent message after the user sends a query. </p><p></p><p><strong>bottom</strong>: Scrolls user to the last message from the agent.</p></td><td><p>show_full_response</p><p>/bottom </p><p></p><p>Default: top</p></td></tr><tr><td>user_info</td><td><p>user_info is the JWT information containing<br>{uuid: unique_id, first_name:, last_name, email: }<br>signed with the agent's secret. </p><p></p><p>See <a href="authentication-using-jwt">Authentication using JWT</a>, for more information.</p></td><td><p>JWT token <br><br>Default:</p><p>Identifies as an anonymous user and assigns - user &#x3C;&#x3C;random_uid>></p></td></tr><tr><td>voice_on</td><td>Whether the new agent message is read out by default</td><td><p>true/false </p><p></p><p>Default: false</p></td></tr><tr><td>voice_locale</td><td>Whether the voice is set to the selected locale of the agent. Note that you must add a locale to the agent. See <a href="../../add-languages">Add languages</a>, for more information.</td><td>Locale specified in standard <a href="https://en.wikipedia.org/wiki/IETF_language_tag#Syntax_of_language_tags">IETF format</a></td></tr><tr><td>css_url</td><td>If you have an external CSS file URL, then the external CSS file URL is considered instead of custom CSS in the web channel setting</td><td>External CSS file URL</td></tr><tr><td>css_class</td><td>You can provide a qualifier or namespace that helps you to define custom CSS elements within scope. </td><td>Custom CSS class</td></tr><tr><td>locale</td><td>This is the default locale for the web channel, for this language needs to be included in the agent.</td><td><p>Locale specified in standard <a href="https://en.wikipedia.org/wiki/IETF_language_tag#Syntax_of_language_tags">IETF format</a> </p><p></p><p>Default: English (en-US)</p></td></tr><tr><td>custom_properties</td><td><p>Used to pass custom properties in web channel URL without using JWT. </p><p></p><p>If you are using JWT, you can pass JWT using user_info. See <a href="../../../../build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties">Create custom user properties</a>, for an example.</p></td><td><p>[&#x3C;&#x3C;key1>>]=&#x3C;&#x3C;value1>></p><p></p><p>Key, value pair of custom properties </p></td></tr><tr><td>query_autocomplete_url</td><td>A set of pre-canned questions as per your requirement. Currently, this feature is supported only in the English language.</td><td>JSON file in any publically accessible URL such as Github</td></tr><tr><td>message</td><td><p>This message is posted as a user query to the agent as soon as it is invoked. </p><p></p><p>For example, you can post #clear message to tag the greeting message so that it can be captured in Analytics.</p></td><td><p>String </p><p></p><p>&#x3C;&#x3C;custom message>> </p><p></p><p><strong>Example</strong>: message="#clear"</p></td></tr></tbody></table>

#### **Example 1: User information**

Next, configure the agent setting for the Web Channel.

* You can request the user information before allowing the user to interact with the agent, and add *collect\_info=true* in the query string of the agent script URL. **Example**: web\_channels/2f36cccd-b872-4830-abc5-e606350c1089.js?

```javascript
<script type="text/javascript" async src="https://webchannel.avaamo.com/web_channels/<bot-uuid>.js?theme=avm-blue&collect_info=true"></script>
```

#### **Example 2: Movable chatbox**

You can make the chatbox draggable or movable for the user's convenience. Add *draggable=true* in the query string.

<pre><code><strong>https://webchannel.avaamo.com/web_channels/&#x3C;bot-uuid>.js?theme=avm-blue&#x26;draggable=true
</strong></code></pre>

### Query autocomplete URL

{% hint style="info" %}
**Notes**:&#x20;

* Currently, this is supported only in the English (en-US) language.
* If you have [enabled voice](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#enable-voice) in the agent, then auto-complete works only if the "Send the voice message automatically" option is disabled. See [Send the voice message automatically](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#send-the-voice-message-automatically), for more information.
  {% endhint %}

The auto-complete feature provides a list of query options to the user as the user starts entering the query in the agent. This feature can reduce false positives and significantly improve accuracy. By presenting the user with a list of available options, the user likely selects one of those options for which accurate curated responses are already available in the agent.

**To test query autocomplete URL**:

* Identify a set of pre-canned questions as per your requirement and create a JSON file:

```javascript
[
  "I want to order pizza",
  "I want to order veg cheese pizza",
  "I want to know store details",
  "where is your store",
  "How to order pizza",
  "How was your day"
]
```

* Upload the JSON file to any publicly accessible URL.Upload the JSON file in any publically accessible URL.
* &#x20;On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Advanced** section, add the JSON URL in the **Query autocomplete URL** textbox.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FOSkU45Mve3RWRsxPRTV4%2FScreenshot%2006-02-2025%20at%2013.53.png?alt=media\&token=b6eb08dc-984b-4c6e-b134-983557312650)

* Click `Save` and click `Test` to test the skill.&#x20;
* A test link is displayed in the new window. Click the agent icon to test. As you type the text, the auto-complete list is displayed in the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKcMfvODpZzBHOUhyq5Fw%2Fimage.png?alt=media\&token=94413e42-3e5b-4b9f-9013-1a1624197012)

* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### **Enable Markdown Format**

This option allows you to use the `Markdown` format for LLaMB response. By default, this option is unchecked.

{% hint style="info" %}
**Note:** To utilize this option, ensure you re-ingest the document before enabling it.
{% endhint %}

* Markdown simplifies formatting, making generating and displaying elements like paragraphs, tables, bullet points, and hyperlinks easier.
* This change enables more flexible and universal formatting options, thereby enhancing readability and improving compatibility with LLaMB.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Frl0WKM9Kj7zBLDnhP566%2Fspaces_-LpXFTiTgns4Ml77XGi3_uploads_dd4hClMhusM4Xa4EwxA3_Screenshot%202025-02-24%20at%204.png?alt=media&#x26;token=40ad65cd-1d66-404f-bb89-80d19054210c" alt=""><figcaption></figcaption></figure>

**To enable the MD Format option**:

* On the `Agent > Channels` page, click `View` on the Web Channel.
* Navigate to `Channels > Advanced`**.**
* Click `Advanced`  tab in the left panel of the channel configuration widget. &#x20;
* Locate the `Enable Markdown Format` option under `LLaMB Settings`**.** Click the checkbox next to the option to enable it.
* Click `Save` and click `Test` to test the agent. A test link is displayed in the new window. Click the agent icon to test.&#x20;

### Disable citation links

In LLaMB responses, citation links are references provided by the agent to indicate the source of information. They often point to [ingested documents](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content) or [preview URLs ](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/common-actions#edit)added during the document ingestion. This feature adds credibility to the information displayed to the user. &#x20;

Disable citation links option allows you to enable/disable [citation links](https://docs.avaamo.com/user-guide/llamb/citation-links) in the LLaMB responses. By default, citation links are always displayed in LLaMB responses.&#x20;

{% hint style="info" %}
**Note**: This option is visible only when **Enable Markdown Format** is checked under **LLaMB Settings**.
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F11LEvwNVTn7ycixGeTRZ%2Fspaces_-LpXFTiTgns4Ml77XGi3_uploads_dd4hClMhusM4Xa4EwxA3_Screenshot%202025-02-24%20at%204.png?alt=media&#x26;token=eae431b5-1add-4393-ba27-a4a9130b37f5" alt=""><figcaption></figcaption></figure>

**How to Enable or Disable citation links:**

* In the `Agent` page, navigate to the `Configure > Channels` option in the left navigation menu.
* On the Channels page, click `View` in the Web Channel.
* Click `Advanced`  tab in the left panel of the channel configuration widget. &#x20;
* Click `Enable Markdown format` under `LLaMB Settings` to view the `Disable Citation links` option. By default, citation links are always displayed in LLaMB responses; hence, this option is unchecked.
* Check to disable the citation links, and uncheck to display them in LLaMB responses.
* Click `Save` and click `Test` to test the agent. A test link is displayed in the new window. Click the agent icon to test

| When citation links are enabled                                                                                                                                                                                                                                                           | When citation links are disabled                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FN1aOf7ydlFddp1nFwJkS%2FScreenshot%2024-02-2025%20at%2019.22.png?alt=media&#x26;token=edccbc6a-9c75-48b5-a930-d164046279ee" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4Zx6je25hfgHsovMH8Iw%2FScreenshot%2024-02-2025%20at%2019.23.png?alt=media&#x26;token=9b44dd3a-b91e-474f-9ccd-bb314c6ef3d3" alt="" data-size="original"> |

### Enable concise response

This feature enhances the conversational experience by generating shorter, more natural, and to-the-point responses while preserving key information in LLaMB responses

{% hint style="info" %}
**Note**: This option is visible only when **Enable Markdown Format** is checked under **LLaMB Settings**.
{% endhint %}

When `Enable Concise Responses` is turned on, the agent prioritizes brevity and conversational fluency. Instead of providing lengthy, detailed responses, it focuses on delivering information in a clear and engaging manner for users.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDQq7PTXowHTmBxOintEl%2Fspaces_-LpXFTiTgns4Ml77XGi3_uploads_dd4hClMhusM4Xa4EwxA3_Screenshot%202025-02-24%20at%204.png?alt=media&#x26;token=90aceffe-cb69-4e35-a3bc-7086afcd38f8" alt=""><figcaption></figcaption></figure>

**How to Enable or Disable the Option:**

* On the `Agent` page, navigate to the `Configure > Channels` option in the left navigation menu.
* On the Channels page, click `View` in the Web Channel.
* Click `Advanced`  tab in the left panel of the channel configuration widget. &#x20;
* Click `Enable Markdown format` under `LLaMB Settings` to view the `Enable concise response` option. By default, this option is unchecked.
* Check to disable the concise LLaMB responses and uncheck to enable concise LLaMB responses.
* Click `Save` and click `Test` to test the agent. A test link is displayed in a new window. Click the agent icon to test

| Before enabling                                                                                                                                                                                                                                                                           | After enabled                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F81F6LCk0U2g6Pu1oy1Fl%2FScreenshot%2024-02-2025%20at%2019.24.png?alt=media&#x26;token=883b6c07-430c-43a8-a078-1c63fa342754" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4EXpiF6gzyIGiCSqnVy6%2FScreenshot%2024-02-2025%20at%2019.25.png?alt=media&#x26;token=67ecb000-cd86-4a94-b842-f4a9c54c1b2b" alt="" data-size="original"> |

{% hint style="success" %}
**Key point:**

When using Agent Assist or AI Agent, where precise responses are required and source links are not needed, you can disable them using these options.
{% endhint %}
