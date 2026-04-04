# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/skype.md

# Skype for Business

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.&#x20;
{% endhint %}

**Skype for Business** (formerly **Microsoft Lync** and **Office Communicator**) is an enterprise instant messaging software developed by **Microsoft** as part of the **Microsoft Office** suite. It is designed for use with the on-premises Skype for Business Server software, and software as a service version offered as part of Office 365. It supports text, audio, and video chat, and integrates with Microsoft Office components such as Exchange and SharePoint.

The agents developed on the Avaamo platform can be deployed on the Skype for Business channel. In this article, the following steps are detailed:

1. [Before you begin](#before-you-begin)
2. [Deploy your agent to Skype for Business channel](#deploy-your-agent-to-skype-for-business-channel)
3. [Manage channel settings](#manage-channel-settings)

## **Before you begin**&#x20;

* You must create a bot in Microsoft Bot Development Framework. See [Microsoft Bot Framework](https://dev.botframework.com/), for more information.
* Note down the **Application ID** and **Secret key** generated when you create a bot in Microsoft Bot Development Framework. This is later required when you deploy your agent on the Skype for Business channel in the Avaamo Platform.

## Deploy your agent to Skype for Business channel

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.

* On the Channels page, click **Connect** in **Skype for Business** channel.

* Specify the **Application ID** and **Secret key** generated when you created a bot in Microsoft Bot Development Framework. See [Before you begin](#before-you-begin), for more information.

* Add the bot registered on MS Bot Framework to the Skype for Business environment. See [Add a bot to Skype for Business](https://docs.microsoft.com/en-us/skype-sdk/skype-for-business-bot-framework/docs/overview#add-a-bot-to-skype-for-business), for more information.

## Supported Versions ( Limitations )

The Skype for Business channel works with Skype for Business Online and Skype for Business Hybrid environments only. See [Supported Skype for Business versions](https://docs.microsoft.com/en-us/skype-sdk/skype-for-business-bot-framework/docs/overview#version-suport), for more information.

### Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
