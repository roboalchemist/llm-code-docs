# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/handover-protocol-integration-facebook.md

# Handover Protocol Integration- Facebook

The Facebook Messenger Platform's handover protocol enables two or more Facebook apps to participate in a conversation by passing control of the conversation between them. This feature can be used in many ways to enrich your agent experience on the Messenger. For example, this protocol makes it possible for a Page to simultaneously use one Facebook app to build an agent for handling automated responses, and another Facebook app for customer service with live agents.

#### Prerequisites

To use the handover protocol, you must assign only one app with the Primary Receiver role and at least one app the Secondary Receiver role on your Facebook Page settings.

{% hint style="info" %}
Learn how to create a Primary App on the [*https://developers.facebook.com/*](https://developers.facebook.com/)*.*
{% endhint %}

## Generate API Token

The user needs to generate an API Token to use the Handover Protocol on Facebook for Developers portal. This token is then used on the Avaamo UI to generate the Webhook URL. To generate the token:

* Login to your account on Facebook for Developers portal.
* Click on Create Page, to create a new page on your Facebook account.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly37QgpOXgL4NZ9Gg6j%2Fagent-deploy-fb-handover-1.png?alt=media&#x26;token=cc9d039b-e45b-4830-9e68-abe74d38c7bf" alt=""></div>

* Enter the Display Name and Contact Email to Create a New App ID.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly37XMHUCRvgmc0cJtf%2Fagent-deploy-fb-handover-2.png?alt=media&#x26;token=8cbf1242-9c17-4b78-84a3-710de018abdb" alt=""></div>

* Go to the Primary App Dashboard and under the “Add a Product ” section, click on “Set Up” under Messenger.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly37akzMyyfdtFgeXdQ%2Fagent-deploy-fb-handover-3.png?alt=media&#x26;token=55c8eb92-c1de-4c97-ad99-56a0693c9f89" alt=""></div>

* On the Token Generation popup window, select the Facebook page, and generate the Page Access Token.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly37j9wozCuMXH91Jg_%2Fagent-deploy-fb-handover-4.png?alt=media&#x26;token=eb633808-4460-4ee1-8da4-1e4f10aeaf36" alt=""></div>

Copy the Page Access Token, this will be added on the Avaamo UI under the Facebook channel to generate the Webhook token.'

## Generate Webhook Token

* In the **Agent** page, navigate to the **Configuration -> Channels** option in the left navigation menu.
* On the Channels page, click **Connect** in Facebook Messenger.
* On the popup window, enable the switch to Yes for Manual Configuration and Reuse Videos.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly38A8Pa8Mi3poiWDGH%2Fagent-deploy-fb-handover-6.png?alt=media&#x26;token=a74b4f9c-f6c5-485e-bece-155b703cc36d" alt=""></div>

* Enter the Page Name, Page ID, and Page Access Token values from the Facebook page and app.
* Click Save.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly38K_zNgD4JFT7SAcK%2Fagent-deploy-fb-handover-7.png?alt=media&#x26;token=8cbcb683-f783-4867-8e75-78c0a4f7713d" alt=""></div>

Once you click save, it will generate the Webhook URL and Verification Token.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly38Q8uFkkJEMIAFueI%2Fagent-deploy-fb-handover-8.png?alt=media&#x26;token=c8af6396-dc8e-470b-86ac-10b3b1f29189" alt=""></div>

Copy and save the Webhook URL to setup Webhook on your Facebook app.

## Set up Webhooks

To set up the Webhooks, go to your Facebook app and under Webhooks section click on Setup Webhooks.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly38bsYKcexk0G_SNYt%2Fagent-deploy-fb-handover-9.png?alt=media&#x26;token=3126cbe0-7111-4f7f-b016-d5905789ac04" alt=""></div>

Select all the subscription fields, enter the Webhook URL and access token from the manual configuration on the Avaamo UI and click on Verify and Save.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly38gt6mgUT-pNy_6a0%2Fagent-deploy-fb-handover-10.png?alt=media&#x26;token=04916d9d-dc72-48a5-868f-e80972b8302d" alt=""></div>

Select your page from the drop-down and click on "Subscribe".

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly39J7AWWmdX3kCyQzN%2Fagent-deploy-fb-handover-11.png?alt=media\&token=dbaf6caf-5bfc-40cc-aad9-8a3ebf456986)

Under App Review for Messenger, add the submission of pages\_messaging.

For a Secondary app, create the secondary app on your Facebook account and follow the same steps with the secondary agent. And connect to the agent to the secondary app on the same Facebook page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly39PxWIaS-NWIBLMAC%2Fagent-deploy-fb-handover-12.png?alt=media\&token=1b6d9570-b79f-4b13-89f1-11a7853f207e)

Go to your Facebook page and click on Settings then go to Messenger Platform.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly39_Gjcoe_I8DruC4v%2Fagent-deploy-fb-handover-13.png?alt=media\&token=2bb4896b-ee13-45d4-87d4-d8a77edda8e3)

Under Connected Apps, you will have primary and secondary apps. Now, click on Configure.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly39kYNgkwNt7gaFOBN%2Fagent-deploy-fb-handover-14.png?alt=media\&token=8eac89ae-806e-441a-9835-bc3ddf9c821d)

Select your preference for the primary and secondary app.

{% hint style="info" %}
**Note**: By default, all messages are sent to the Primary Receiver app. When control of the conversation is passed to another, the Messenger Platform will send messages from the conversation to it instead. Only one app may control the conversation at a time.
{% endhint %}

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-qwgLAzn1A0bo_3Rp%2F-Ly39uxYzmu8Mi8R--Wp%2Fagent-deploy-fb-handover-15.png?alt=media&#x26;token=09242643-574b-4616-bdf0-61cd816d9430" alt=""></div>

Now, from Avaamo agents we need to switch the agent's response based on user queries for the response.
