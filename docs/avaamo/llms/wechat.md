# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/wechat.md

# WeChat

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.
{% endhint %}

WeChat allows users to interact with a fast, simple, secure messaging channel. WeChat provides many features such as text messaging, hold-to-talk voice messaging, broadcast (one-to-many) messaging, video calls and conferencing, video games, photograph and video sharing, as well as location sharing.&#x20;

The agents developed on the Avaamo platform can be deployed on the WeChat channel. In this article, the following steps are detailed:

1. &#x20;[Before you begin](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/skype#before-you-begin)
2. [Deploy your agent in WeChat](#deploy-your-agent-in-wechat)
3. [Manage channel settings](#manage-channel-settings)

## **Before you begin**&#x20;

* You must register for a WeChat Official Account. You also need to enable webhook integration for the agent to send and receive messages. See [WeChat Official Accounts Registration Process](https://wechatwiki.com/wechat-resources/wechat-official-account-registration-fees/), for more information.
* For testing and integration purposes, you can use the WeChat Sandbox environment to integrate and test the agent.
  * Register and log in to the WeChat Sandbox environment.&#x20;
  * After successful sign-in, make a note of the WeChat Sandbox App ID and App Secret in the WeChat Sandbox portal environment. This is later required when you deploy your agent on the WeChat channel in the Avaamo Platform.
  * On the bots platform, use the App ID and App Password to generate the Webhook URL and Access Token. Make a note of this information.

## Deploy your agent in WeChat

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* On the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.

* On the Channels page, click **Connect** in the **WeChat** channel.

* Provide a name for the WeChat channel.

* Specify the **App ID** and **App Password** generated on the WeChat Sandbox portal page. Also, enter the **Webhook URL** and **Access Token** that you generated in the bots platform. Contact Avaamo Support if you need help with generating the Webhook URL and Access Token. See [Before you begin](#before-you-begin), for more information.

* Click **Save**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZ0ZYftooJb0elcSyNPnR%2FScreenshot%202022-05-17%20at%201.15.24%20PM.png?alt=media\&token=aa0c03ae-94b0-4441-a2ff-dfc87ed5cff7)

## Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
