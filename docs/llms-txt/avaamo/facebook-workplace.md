# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-workplace.md

# Facebook Workplace

Facebook Workplace is a work collaboration tool built from Facebook. The Workplace helps teams and organizations collaborate efficiently wherever they work. See [Integrating with Workplace](https://developers.facebook.com/docs/workplace/introduction), for more information.

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.&#x20;
{% endhint %}

The agents developed on the Avaamo platform can be deployed on Facebook Workplace. In this article, the following steps are detailed:

1. [Before you begin](#before-you-begin)
2. [Integrating your Facebook Workplace bot with Avaamo agent](#integrating-your-facebook-workplace-bot-with-avaamo-agent)
3. [Testing Integration](#test-integration)
4. [Manage channel settings](#manage-channel-settings)

## Before you begin

{% hint style="success" %}
**Pre-requisite**:&#x20;

* The customer requiring the deployment of Avaamo agent on Facebook Workplace has already set up a Facebook workplace account.
* Custom integration is set up in the Facebook Workplace for integrating your Facebook Workplace bot with an Avaamo agent. See [Custom Integrations](https://developers.facebook.com/docs/workplace/custom-integrations-new/), for more information.
  {% endhint %}

Ensure that you get the following information from the customer before deploying the Avaamo agent on Facebook Workplace:

* **App Secret, App ID, and Access Token**: This information is available in the Admin panel of the Facebook Workplace bot when you set up a custom integration. See [Custom Integrations](https://developers.facebook.com/docs/workplace/custom-integrations-new/), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9S9frMkeCCFv6Gzz_g%2F-M9SGV40EAduHb6ESa8e%2Ffb-workplace-token.png?alt=media\&token=dbacb2de-2fc1-4db8-a5c3-9df12c93e328)

* **Page ID and Company Domain:** This information is available when you access the page that is created when you set up a custom integration. This is visible within your Workplace community. You can get the Page ID and Company Domain from the page URL:

```
https://<<Company Domain>>.workplace.com/chat/t/<<Page ID>>
```

## **Integrating your Facebook Workplace bot with Avaamo agent**

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can deploy an agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editin&#x67;**.**
    {% endhint %}

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.

* On the Channels page, click **Connect** in the Facebook Workplace channel.

* Specify all the details in the pop-up page and click **Save**. See [Before you begin](#before-you-begin), for more information on how to get these details.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9S9frMkeCCFv6Gzz_g%2F-M9SRajtvLpEtblOXSXN%2Ffb-workplace-setup.png?alt=media\&token=d057f223-ffb7-4fb9-a32e-b77b89c2b520)

## Test integration

After saving the Facebook Workplace channel details in the Avaamo platform successfully, your agent is ready to be tested in the Facebook Workplace:

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the Channels page, click **Test** in the **Facebook Workplace** channel.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9S9frMkeCCFv6Gzz_g%2F-M9STpmepAb7m-akminb%2Ffb-workplace-test.png?alt=media\&token=0e371eb7-eced-4d4a-8943-44615c5b2268)

* This launches the Facebook page "https\://<\<Company Domain>>.workplace.com/chat/t/<\<Page ID>>". Note that here Company Domain and Page ID are the details that you have specified&#x20;

  during the integration of your Facebook Workplace bot with Avaamo agent.&#x20;
* On the Facebook page, you can test the queries corresponding to your Avaamo agent and check if you are receiving appropriate responses.&#x20;

## Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
