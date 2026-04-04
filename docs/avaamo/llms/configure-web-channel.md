# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel.md

# Configure web channel

Web channel comes with many configuration options that make configuring and deploying your agent in the web channels easier.&#x20;

**To configure a web channel:**

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.

* By default, a web channel is always enabled. On the Channels page, click **View** in the Web Channel.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbdfT4eZ3bdLPvo6dS-%2F-MbdgJ8_Z9q71gexIdTI%2F5.7-default-web-channel.png?alt=media\&token=cb07ac61-cc6e-401c-8500-3aed170524bb)

* Specify the Channel name, Channel description, and other required details in each section of the Web channel configuration based on your business requirements:
  * [Channel details](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/channel-details): Provide channel name, and description, and enable or disable channel as required.&#x20;
  * [Theme](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/theme): Customize the look and feel of the agent widget.
  * [Agent widget configuration](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration): Configure various customizable parameters such as default locale, user name, and scroll behavior (to name a few) for your agent widget.
  * [Voice](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/voice): Enable a voice assistant to your web channel that can engage the users in intelligent conversations by understanding and interpreting the dialects and accents of the users.
  * [Deployment](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/deployment): Provides you a script to embed in the website source code for rendering the agent.&#x20;
  * [Security](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/security): Configure authentication mechanisms for your agent.
  * [Advanced](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced): Provide any other additional customizable parameters and configure auto-complete URL.&#x20;
  * [UAT](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/uat): For UAT users, add UAT queries and perform testing on the agent before deploying the agent to production. The UAT option is available in the Web channel only when LLaMB is enabled for your account. See [LLaMB](https://docs.avaamo.com/user-guide/llamb/overview-key-features), for more information.&#x20;
* Click **Save** and click **Test** to test the web channel.&#x20;
* A test link is displayed in the new window. Click the agent icon to test. See [Test channel settings](#test-channel-settings), for more information on how to test the web channel.
* After you configure web channel settings, you can also view, edit, disconnect, and delete web channel settings as per your requirements. See [Manage web channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/manage-web-channel), for more information.
* You can also deploy your agent through multiple instances of web channels simultaneously. See [Deploy in multiple web channel instances](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/deploy-and-test-web-channel), for more information.

{% hint style="success" %}
**Key Points:**&#x20;

* Each section also includes "Learn more" links that point to relevant topics in the documentation for further reading and understanding.
* You can set many of these parameters from the UI or using [customization parameters](#customization-parameters). However, setting a parameter in the customization parameters section always takes precedence over the value set in the UI.
  {% endhint %}

## Test channel settings

There are two types of testing for AI agents as it supports `Voice` and `Text` types of conversation.

After you save your web channel configuration settings, click **Test.**&#x20;

* In a new tab, a sample code and demo agent are displayed.&#x20;
* Ensure that you have made the agent publically accessible in the Channel configuration.
* For local debugging, create a sample HTML page and host it locally using apache or Node.js's http-server or any other appropriate option. See <https://www.npmjs.com/package/http-server#installation>, if you wish to explore the node-js approach.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3nxn822G7t24qxziBf%2F-M3o6de2eptNAcUJatH6%2Fweb-channel-test.png?alt=media\&token=f79be2aa-bff5-4468-b98f-3c11d6c8be9e)

{% hint style="info" %}
**Note**: In the chatbot URL, the parameters **demo=true** and **action=demo** are used for internal purposes only.
{% endhint %}

## Embed your agent in iFrame

After you save your web channel configuration settings, click **Test.**&#x20;

* Copy the URL displayed in the browser.
* In the URL, update demo.html to channel.html and include the URL in your iFrame source. The following is a sample HTML code:

```markup
<!DOCTYPE html>
        <html>
        <head>
          <title>Web Frame Example</title>
          <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
        </head>
        <body>
          <iframe src="https://cx.avaamo.com/web_channels/8aac6466-5ec1-4df9-9b52-b97e138f62a0/channel.html?theme=avm-messenger&banner=true&demo=true&banner_text=%20&banner_title=This%20is%20how%20the%20chat%20agent%20shows%20up" 
          width="700px" height="700px"></iframe>

        </body>
      </html>
```
