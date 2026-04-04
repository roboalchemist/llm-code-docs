# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration.md

# Widget configuration

{% hint style="info" %}
**Before configuring the widget in the web channel**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

* On the **Agent -> Channels** page, click **View** on the Web Channel.

* In the **Channels -> Widget configuration** section, you can configure various customizable parameters such as default locale, user name, and scroll behavior (to name a few) for your agent widget.

### Display user name in chat

This option can be used to display user names in the agent chat widget during agent-user conversations.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* This works only for those themes that support user name display. This option is not supported by the default messenger theme.
* By default, this option is not enabled.
  {% endhint %}

**To enable displaying user name in chat widget**:

* In the **Channels -> Widget configuration** section, slide the toggle **Display user name in chat** to **Yes**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbZBkrNC1SwS-DVKElv%2F-MbZC6aMgHp1xDlohaTZ%2F5.7-web-channel-display-user-name.png?alt=media\&token=cdc4e6e5-7c90-4cca-be0f-59375c63189f)

* Click **Save** and click **Test** to test the agent.&#x20;
* A test link is displayed in the new window. Click the agent icon to test.&#x20;

Consider that you have selected the Orange theme for your agent chat widget. See [Agent theme](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#agent-theme), for more information. Notice that the user name is now displayed in the agent chat widget:

&#x20;![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FlUho0d27tgMWUeDqmGqo%2Fimage.png?alt=media\&token=2354d961-17c9-4f42-b298-4b98dfa9b8db)

### Default web channel locale

This option is to set the default locale for the web channel. All the languages configured in the agent is displayed in the dropdown. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* By default, the web channel locale is English (en-US).
* When you set a language as default in the **Configuration -> Language** page, then the default language set in the respective channels is not considered. The agent's default language set in the **Configuration -> Language** page takes precedence. See [Make default](https://docs.avaamo.com/user-guide/how-to/build-agents/add-languages#make-default-language), for more information on how to set the default language from the **Configuration -> Language** page
  {% endhint %}

**To choose the default web channel locale:**

* In the **Channels -> Widget configuration** section, select the default web channel locale, and say French from the dropdown.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb_FHAd0V38CA3VoE3U%2F-Mb_I901HTgHu1pXqCVu%2F5.7-web-channel-default-locale.png?alt=media\&token=030773ce-c322-495c-b804-526f83b8b004)

* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. You can now see that the default locale of the web channel is changed to French.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FhCyYbxHjHx0whmHs1Tvm%2Fimage.png?alt=media\&token=11de0902-f494-41e8-bc0e-db0b7e17fedd)

* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Show previous history on load

There are two configuration options related to showing the previous history on load:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbZq7az_L5Lb0_czlAE%2F-MbZqZd9Ybym8niX8Pex%2F5.7-web-channel-history.png?alt=media\&token=1291ec40-cf70-44dc-9972-e8f47416aea8)

<table><thead><tr><th width="161">Name</th><th width="290">Description</th><th>Values</th><th>Default</th></tr></thead><tbody><tr><td>Show previous history on load </td><td>Whether to show the previous history in the agent chat widget or not on load.</td><td>Enabled / Disabled</td><td>Enabled</td></tr><tr><td>Number of previous messages to show</td><td>Number of previous messages to show in agent chat widget on load. You can set a maximum value of 200.</td><td>Number</td><td>10</td></tr></tbody></table>

By default, when the agent chat widget is opened, it displays the last 10 messages of the agent-user interaction.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FB6u45KNfx0hjKAGqBmBc%2Fimage.png?alt=media\&token=fa76a9b5-2f74-4c26-b694-d2f741e58acb)

**To disable previous history in chat widget**:

* In the **Channels -> Widget configuration** section, slide the toggle **Show previous history on load** to **No**.&#x20;
* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. You can now see that the previous history of messages is not displayed.&#x20;

{% hint style="info" %}
**Note**: When you set **Show previous history on load** to **No**, the conversation history is still available, but the past conversation in the agent is cleared to the users when they open the agent in the browser tab. Hence, only the greeting message is displayed to the user and not the past conversations.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FqB7fC27w9aEnhmk23I2V%2Fimage.png?alt=media\&token=c6212e88-a375-4a0b-95d5-731d02af8c83)

* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Collect user information

This option can be used to ask the user for email, first name, and last name before allowing access to agent chat widget.

{% hint style="info" %}
**Note**: By default, this option is not enabled.
{% endhint %}

**To enable collect user information option**:

* In the **Channels -> Widget configuration** section, slide the toggle **Collect user information** to **Yes**.
* Select the user details such as the first name, last name, email, and language that you wish to ask the user before accessing the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb_1Lc8Xqm5fM0I1a_y%2F-Mb_1pIiQfgt1CnpR6Ft%2F5.7-web-channel-collect-user-info-enable.png?alt=media\&token=2d195781-9e00-49ab-889f-74476d3ac9ca)

* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. If you wish to test for a new user, then ensure that all the cookies are cleared. Click the agent icon to test. The selected user information is displayed in the chat widget.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FBWkzJTKCqNLBRQT5nxdW%2Fimage.png?alt=media\&token=0f4bfb63-e609-4b31-9bcb-b59b4553b630)

* Enter the details and press next.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FlVgGSAA1E9SlbHiUx4r5%2Fimage.png?alt=media\&token=db4f0d05-a6c4-4dce-8f10-9d8d142287a4)

* If you have selected a theme that supports displaying of user name and enabled [Display user name](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#display-user-name-in-chat) in the chat option, then you can view the same name in the agent-user interactions.&#x20;
* The collected user information details is also available in the [context.user](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user) object, if you wish to access it later for any other purposes.
* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Agent typing animation

There are two configuration options to show the agent typing animation:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbZkpNg1NAVNyejfUX-%2F-MbZlyWDqNkJNyb4stQe%2F5.7-web-channel-agent-animation.png?alt=media\&token=82e7f0d4-ce16-4b31-b400-22479e18bda8)

<table><thead><tr><th width="175">Name</th><th>Description</th><th>Values</th><th>Default</th></tr></thead><tbody><tr><td>Show agent typing animation</td><td><p>Show agent typing animation while waiting for agent response. </p><p></p><p>Typically used when you have external API calls to generate agent responses. </p></td><td>Enabled / Disabled</td><td>Enabled</td></tr><tr><td>Agent typing animation duration (milliseconds)</td><td><p>Duration of the agent typing animation. </p><p></p><p>Typically used when you have external API calls to generate agent responses.</p></td><td>milliseconds<br>Example: 30000 for 30 seconds.</td><td>5000</td></tr></tbody></table>

By default, the **Show agent typing animation** option is enabled. When it is enabled, the typing animation is displayed as follows in the agent widget:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbOirUPMgfnHIhzORDrMs%2Fimage.png?alt=media\&token=cd3a112d-bd95-4a8d-8e55-038e568709c2)

**To disable agent typing animation option in chat widget**:

* In the **Channels -> Widget configuration** section, slide the toggle **Show agent typing animation** to **No**.&#x20;
* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. Click the agent icon to test. You can now see that the agent typing animation is not displayed. See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Draggable

This option can be used to make the embedded web channel window draggable around the page.&#x20;

{% hint style="info" %}
**Note**: By default, this option is not enabled.
{% endhint %}

**To enable draggable option in chat widget**:

* In the **Channels -> Widget configuration** section, slide the toggle **Is agent widget draggable in the page?** to **Yes**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbZ_B0G5QhHI4YapKzL%2F-MbZdlKznd5fYBEpW-UG%2F5.7-web-channel-draggable.png?alt=media\&token=47252924-970b-4da8-be72-3fe90eb8a7bc)

* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. Click the agent icon to test. As you place the cursor on the agent chat widget, a draggable icon <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbZe0liCmWbWxjqqc6V%2F-MbZgXlO-2Lwo3IxS5f-%2Ficon.png?alt=media&#x26;token=1e86c0eb-e1d4-4570-a18c-3377726e86b2" alt="" data-size="line"> is displayed. You can use this to drag the agent chat widget anywhere in the page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbZh4inbOI0yjWZEMt8%2F-MbZh9YAmmaFgy1schYX%2F5.7-web-channel-draggable-test.png?alt=media\&token=b9914ce5-91ab-4547-8449-36c7773300ac)

* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Scroll behaviour

This option can be used to decide if the agent messages must scroll to the top or bottom in the chat widget.&#x20;

* **Top**: Scrolls to the top of the first agent message after the user sends a query.&#x20;
* **Bottom**: Scrolls user to the last message from the agent.

{% hint style="info" %}
**Note**: By default, the scroll behavior is set to **Top.**
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLilMBC0ut3QV7CxvuFEb%2F5.7-web-channel-scroll-behavior-top.png?alt=media\&token=288a0214-549c-40c1-aea2-1e3c518ceaf7)

**To set the scroll behavior**:

* In the **Channels -> Widget configuration** section, select the **Scroll behavior**. Here, the scroll behavior is set to the **Bottom**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FK7k0lJLg6hg8ApZxPssM%2F5.7-web-channel-scroll-behavior%20\(1\).png?alt=media\&token=a5de2f22-7bc5-4ade-aaa5-b97405312ed5)

* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. Click the agent icon to test. You can now see that it scrolls the user to the last message from the agent.
* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### **Stream message**

This option is useful when you wish to render streaming responses to the user via typing animation instead of displaying it at once.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXRLHbdPD4Aj8PYjAVfsy%2FScreenshot%202025-01-22%20at%202.04.34%E2%80%AFPM.png?alt=media&#x26;token=265857af-261b-483e-b8ad-d51a667404df" alt=""><figcaption></figcaption></figure>

Streaming is intuitive, especially when there is a delay in agent response. It creates an impression to the user that the agent is responding and helps actively engage the user in the conversation flow.

**To enable the Stream message option**:

* On the **Agent -> Channels** page, click **View** on the Web Channel.
* Slide the toggle **Stream message** to Yes in the **Channels -> Widget configuration** section.&#x20;
* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. Click the agent icon to test.&#x20;
* You can now view the agent responses rendered as a stream with an option to stop generating the response.
* You can stop generating responses to pause generating text in an ongoing conversation intermittently. This feature provides flexibility to the users in controlling the flow of interaction, allowing users to gather additional information, process intermediate results, or make decisions based on previous responses. To continue generating responses, users can just post queries back to the agent.
* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### **Send attachment**

This option is useful when users have to send attachments in the live agent conversations from the agent to the live agent.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSgY1dNRPDhSyNdK0royJ%2FScreenshot%202025-01-22%20at%201.04.28%E2%80%AFPM.png?alt=media&#x26;token=e0d5892b-8375-4798-92f9-8639bcab5f90" alt=""><figcaption></figcaption></figure>

**To enable the file attachment option**:

* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Widget configuration** section, slide the toggle **Send attachment** to **Yes**.&#x20;
* Click **Save** and click **Test** to test the agent. A test link is displayed in the new window. Click the agent icon to test.&#x20;
  * You can now see an attachment icon before the **Send** option in the agent widget.&#x20;
  * Click the `Attachment icon` to send an attachment from your system.&#x20;
  * You can send only one attachment at a time with a maximum size of 4 GB. You can send attachments of any type, there is no restriction on the type of attachments that you can send.
  * Select the attachment you wish to send. The file format and the file name are displayed in the message box.
  * Once the attachment is sent, the live agents and the users can click the file to view the details of the file.
  * To include a message with an attachment, you must first send the attachment, followed by a separate message to the user.&#x20;
* See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

{% hint style="info" %}
**Note**: When you upload an attachment using the upload icon, the agent responds with an unhandled message.&#x20;

* You can have a [Dialog skill with pre-unhandled intent](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent#id-5.-pre-unhandled-intent-handler), or any [Dialog skill with custom code intent](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent#id-4.-custom-intent-handler) to process it accordingly.&#x20;
* `context.last_message.<<uuid>>` and `context.last_message.<<uuid>>.name` contains the name and identifier of the uploaded file. You can use this information for further processing as per the business requirements.
  {% endhint %}
