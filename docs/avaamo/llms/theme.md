# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/theme.md

# Theme

In the **Theme** section, you can customize the look and feel of your agent.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbAxuG6xhWLRAtM48xj%2F-MbAyKrAqjBcOzW80ie9%2F5.7-web-channel-theme.png?alt=media\&token=fc53c4a0-1a59-49e2-8cd5-26e1ae327bfa)

This feature and the ability to deploy "one agent" across multiple instances of a web channel enable you to style your agent for each instance separately. This allows you to maintain a "single code base" for your agent and still provide a different look and feel for your deployed agent on different instances of the web channel. See [Deploy in multiple web channel instances](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/deploy-and-test-web-channel), for more information.

### **Agent theme**

In the **Agent Theme** section, you can select the color scheme of the web channel.&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

**To configure the agent theme**:

* On the `Agent -> Channels` page, click `View` on the Web Channel.
* In the `Channels -> Theme` section, click the `Agent theme` dropdown to choose a theme based on your styling requirements.
* Choose a theme based on your requirements from the dropdown.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FyJCr8fjcjpgBOhw6zwSf%2FScreenshot%202023-12-13%20at%203.53.42%E2%80%AFPM.png?alt=media&#x26;token=124847ac-1d3f-4eed-b3e0-0ab55c494cad" alt=""><figcaption></figcaption></figure>

* Click `Save` and click `Test` to test the agent.&#x20;
* A test link is displayed in the new window. Click the agent icon to test. The agent widget is displayed with the new theme. See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### **Mercury theme**

`Mercury` is the default theme for all newly created agents and newly created web channels in the Avaamo Conversational AI Platform. &#x20;

The primary styling components of the `Mercury` theme offer a better display of user inputs and agent responses and hence aid in a better user experience. The following table shows the styling details of the `Mercury` theme:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FynsEKk7kMMqlilkbv5Za%2Fimage.png?alt=media\&token=5f97f68d-89a4-4136-8bee-f49874edf656)

<table><thead><tr><th width="160">Primary color</th><th width="126">Font color</th><th>Agent message background-color</th><th>User message background-color</th></tr></thead><tbody><tr><td>#ffffff</td><td>#374151</td><td>#ffffff</td><td>#2b0060</td></tr></tbody></table>

* **Streaming responses:** `Mercury` theme renders streaming responses through the typing animation to the user, eliminating idle waiting time. Streaming is intuitive, especially when there is a delay in agent response. It creates an impression to the user that the agent is responding and helps in actively engaging the user in the conversation flow.
* **Wider agent widget:** `Mercury` theme has a wider agent widget and provides more text area to display the agent response. For short responses, this can avoid scrolling to read answers.
* **Enhanced readability:** A clean UI in the `Mercury` theme with an enhanced white-tone usage, makes the theme look brighter and cleaner (less cluttered), thus enhancing readability when compared to the other themes.
* **Stop generating answers:** Users can stop generating answers in the `Mercury` theme. This helps the users to pause generating text in an ongoing conversation intermittently. This feature provides flexibility to the users in controlling the flow of interaction, allowing users to gather additional information, process intermediate results, or make decisions based on previous responses. To continue generating responses, users can just post queries back to the agent.

#### Feedback suggestions on thumbs-down

One of the significant improvements in the `Mercury` theme is the feedback collected from the users on the thumbs-down option for a response. In the `Mercury` theme, the feedback collected from the UAT users differs from what is collected from the production users.&#x20;

For production users who are actual customers, the feedback collected is open-ended and enables users to provide more descriptive suggestions.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjxaEVyXqvhTkEjPMdSeB%2Fimage.png?alt=media&#x26;token=50e29635-0834-4f12-9132-212cbb676cc5" alt=""><figcaption></figcaption></figure>

The feedback collected at the UAT stage aims towards collecting more specific details since UAT users are subject matter experts and testers within the account who are more aware of the agent and what is built into it when compared to the production users. Hence, the feedback collected at the UAT stage can be instrumental in fine-tuning the agent. See [UAT](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/uat), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUEZPojQJC0urbDYKtwEF%2Fimage.png?alt=media&#x26;token=e91e04e1-69ee-44f8-8eea-7f2f4d438555" alt=""><figcaption></figcaption></figure>

To provide feedback on the thumbs-down option, select the category and specify a detailed explanation for the selected category in the feedback pop-up window.&#x20;

You can view the user feedback from the [Monitor -> Analytics](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#user-feedback) page and also under [Learning -> User Feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) section. Alternatively, you can also use the [User Feedback API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api) to collect feedback periodically to learn and analyze the experience of the user when they are interacting with your agent.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* Use [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback) to override the default feedback options.
* You can specify upto 60000 characters in the "Please explain" text area.
  {% endhint %}

### Themes comparison

The following table depicts supported themes and styling comparisons:

{% tabs %}
{% tab title="Mercury" %}

* Primary color: #ffffff
* Font color: #374151
* Display agent or user name: Agent name is displayed.
* Agent message background-color: #ffffff
* User message background-color: #2b0060
* Message display: Left -> Agent Message, Right -> User Message

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FynsEKk7kMMqlilkbv5Za%2Fimage.png?alt=media&#x26;token=5f97f68d-89a4-4136-8bee-f49874edf656" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Messenger" %}

* Primary color: #0d86de
* Font color: #001c33
* Display agent or user name: No
* Agent message background-color: #ffffff
* User message background-color: #DCDCDC
* Message display: Left -> Agent Message, Right -> User Message

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXuTLuaGGuj11rw2j2QQR%2Fimage.png?alt=media\&token=feae3ff6-fa49-4f30-abc5-e5e01da8484d)
{% endtab %}

{% tab title="Blue" %}

* Primary color: #0d86de
* Font color: #666666
* Display agent or user name: Yes
* Agent message background-color: #ffffff
* User message background-color: #f6fbfe
* Message display: Agent and User messages are displayed one below the other

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIW4EMsmjnbP99HMuiY7i%2Fimage.png?alt=media\&token=f8bb33fc-0c60-40e7-abdd-557f61593a43)
{% endtab %}

{% tab title="Orange" %}

* Primary color: #FBA361
* Font color: #001c33
* Display agent or user name: No
* Agent message background-color: #ffffff
* User message background-color: #fffaf6
* Message display: Agent and User messages are displayed one below the other

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3PKuQ7rTaj1kOSfSiPkK%2Fimage.png?alt=media\&token=5e124fdb-1990-4007-988c-0d7b35ada7ba)
{% endtab %}

{% tab title="Red" %}

* Primary color: #F17375
* Font color: #666666
* Display agent or user name: Yes
* Agent message background-color: #ffffff
* User message background-color: #fef9fa
* Message display: Agent and User messages are displayed one below the other

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7u8AgEOXV46S4zQmvs76%2Fimage.png?alt=media\&token=8b48e5ca-68a4-488f-97ad-718f244933f2)
{% endtab %}

{% tab title="Green" %}

* Primary color: #48C27C
* Font color: #666666
* Display agent or user name: Yes
* Agent message background-color: #ffffff
* User message background-color: #f4fbf7
* Message display: Agent and User messages are displayed one below the other

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FBelTxFlLDuBuSF8ls14G%2Fimage.png?alt=media\&token=a9f838d6-1905-46a9-a4a6-a2cb599e0319)
{% endtab %}
{% endtabs %}

### **Custom CSS**

You can provide a custom skin to the agent deployed on the Web channel using custom CSS. This provides a unique and personal experience to the user interacting with the agent. **Example**: font, background color, logo (to name a few). See [Web Channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel), for more information on Custom CSS.

{% hint style="success" %}
**Key Points**:&#x20;

* To create a custom CSS, you must identify the CSS selector that must be customized. Locate or inspect the web element in the Chrome browser, identify the CSS selector, and then customize in Custom CSS as required.
* The maximum Custom CSS code limit is 65535 characters and the maximum file size is 64 KB. If you have a CSS file that exceeds this limit, then you can consider one of the following approaches:
  * Remove unnecessary CSS data.
  * Minify the data by eliminating unwanted characters.
  * If you have a larger CSS file, then it is recommended to use the External CSS approach. See[ External CSS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#custom-css-url), for more information.
    {% endhint %}

Consider that you wish to customize the background color of the messages displayed in the MacPizza agent. Currently, without custom CSS, the MacPizza agent has messages displayed with a transparent background.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnJ2eK14yyRwDEjQSTRb3%2Fimage.png?alt=media\&token=d4aa91ba-4cae-4e44-9d0b-99fdfce59fa9)

**To style the agent**:

* Locate or inspect the web element in the Chrome browser and identify the CSS selector that must be customized.
* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Theme** section, customize the CSS selector as required in the **Custom CSS** text-area. The following is a sample CSS that customizes the look and feel of the agent messages:

```css
#messages-list .conversation-item.not-mine .media .message-wrap p.desc.text-content {
     border-radius: 0px 25px 25px 25px;
      max-width: 270px;
      padding: 8px 9px 8px 8px;
      box-shadow: 2px 0px 3px -1px #ccc;
      background: #a4ae7d;
      color: #fff;
}
```

* Click **Save** and click **Test** to test the agent.&#x20;
* A test link is displayed in the new window. Click the agent icon to test. The agent widget is displayed with customized CSS changes. See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9kI61fyjzQNgWgH5aga6%2Fimage.png?alt=media\&token=df71af7d-7763-4dd0-b5be-5fd6fed8ce2f)

### **Custom CSS URL**

Instead of adding inline custom CSS, you can provide an externally hosted CSS URL for better maintainability.

**To add custom CSS URL**:

* Identify and create custom CSS as per your styling requirement. See [Custom CSS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#custom-css), for more information on how to identify and customize the CSS selectors.&#x20;
* Upload the CSS file in any publically accessible UR&#x4C;**.** Ensure that the mime type is "text/css".
* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Theme** section, add the CSS URL in the **Custom CSS URL** textbox.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbGH5yNBjcgKP40I5xI%2F-MbGPkL83PXh0EZnpf1f%2F5.7-web-channel-custom-css.png?alt=media\&token=5f8ba2f5-32d2-40cb-9887-dcdbc0d96e14)

* Click **Save** and click **Test** to test the agent.&#x20;
* A test link is displayed in the new window. Click the agent icon to test. The agent widget is displayed with customized CSS changes as specified in the Custom CSS URL. See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

### Custom CSS class

Using the **Custom CSS class**, you can provide a qualifier or namespace that helps you to define custom CSS elements within scope. Adding a qualifier helps you to define the scope where the CSS must be applied so that it does not interfere with the style of the same element in the parent website where the agent is deployed.&#x20;

**To add custom CSS class**:

* Identify the custom CSS class name that you wish to specify.
* On the **Agent -> Channels** page, click **View** on the Web Channel.
* In the **Channels -> Theme** section, add the custom CSS class in the **Custom CSS class** textbox. You can use the custom CSS class to style the elements so that it does not interfere with the style of the same element in the parent website where the agent is deployed.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbX8fwOVq5Wvwb8NdPE%2F-MbX9GFsKErv6SHWN4V9%2F5.7-web-channel-custom-css-class.png?alt=media\&token=61ae61ee-386c-4622-9bea-f03f2820ebda)

* Click **Save** and click **Test** to test the agent.&#x20;
* A test link is displayed in the new window. Click the agent icon to test. The agent widget is displayed with customized CSS changes. See [Test channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/configure-web-channel#test-channel-settings), for more information on how to test the web channel.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fzgfbi0JM5G0alsgcnvdl%2Fimage.png?alt=media\&token=ba6affbd-fcbd-491a-a0ee-44e617fa8f66)

{% hint style="success" %}
**Key point**: When you specify a custom CSS class and save the web channel settings, the class is applied in the \<body> tag. You can use this class to define custom CSS elements within the scope.
{% endhint %}
