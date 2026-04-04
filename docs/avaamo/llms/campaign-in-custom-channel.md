# Source: https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-custom-channel.md

# Campaign in Custom channel

Avaamo Conversational AI Platform allows you to trigger an outreach campaign via SMS, MS Teams, and C-IVR.  However, if you wish to send outreach campaigns in any other enterprise channels, than those available, then you can configure and trigger the campaign via a custom channel. This widens the reach of the campaigns to a larger set of audience and better adoption of the Outreach campaign programs.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FG0F6qNaOGgj1ChqVyQCf%2Fimage.png?alt=media&#x26;token=95ec69c1-a0ad-47a3-9056-24edb526fa0d" alt=""><figcaption></figcaption></figure>

The following lists some of the other key benefits of configuring your campaign via the custom channel:

* Custom channel also allows seamless data exchange between systems&#x20;
* Promotes flexibility and scalability as it eliminates the need to be tightly coupled with a specific channel.&#x20;

This article describes how to create an outreach program using the Custom channel. The following lists the steps for setting up an outreach program via a Custom channel:

1. [Create an agent and deploy in Custom Channel](#step-1-create-an-agent-and-deploy-in-custom-channel)
2. [Create Middleware - Message transformer](#step-2-create-middleware-message-transformer)
3. [Create a new recipient list](#step-2-create-a-new-recipient-list)
4. [Create and test your campaign](#step-3-create-and-test-your-campaign)
5. [Send status update from Middleware](#step-5-send-status-update-from-middleware)

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new outreach campaign program.
{% endhint %}

The following diagram illustrates the data flow between the user, Avaamo platform, Middleware, and a Third-party system:&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FI9TKFf2WFzX3OcTOublJ%2Fimage.png?alt=media&#x26;token=64202323-101a-4288-a2e7-367ff72f0083" alt=""><figcaption></figcaption></figure>

### Step 1: Create an agent and deploy in Custom Channel

The first step to trigger an outreach campaign via the Custom channel is to create an agent and then deploy the agent in the Custom channel.

* Ensure that the custom channel is asynchronous.
* The API URL in the custom channel must be the URL of the [Middleware - Message transformer](#step-2-create-middleware-message-transformer) application interface.
* See [Custom Channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel), for more information.

### Step 2: Create Middleware - Message transformer

Middleware acts as a message transformer to transform the message to and from the custom channel and third party respectively.&#x20;

When a campaign is triggered,&#x20;

* The outgoing message or payload from the campaign is sent via the custom channel in the standard outgoing message payload format from the Avaamo Conversational AI Platform to the Middleware. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#payload-details), for more information on the outgoing message payload format.
* The Middleware receives the payload and is responsible for transforming and sending the payload according to the standards the third-party receiver expects.

For the incoming messages from the recipient to the campaign,&#x20;

* The payload or message is first sent by the third party to the Middleware.
* The Middleware receives the payload and is responsible for transforming and sending the payload according to the incoming message payload format expected by the Avaamo Conversational AI Platform. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#payload-details), for more information on the outgoing message payload format.

{% hint style="info" %}
**Notes**:&#x20;

* The middleware component has the complete flexibility to use all the parameters in the custom channel outgoing payload to identify the recipient parameters.&#x20;
* Middleware transformer component is outside the scope of the Avaamo Conversational AI Platform. It is the responsibility of the party wishing to integrate a third-party channel with Avaamo to ensure that the Middleware is in place and working as expected.&#x20;
  {% endhint %}

### Step 3: Create a new recipient list

The next step in any outreach program is to create a list of recipients for whom the outreach program is intended for. You can quickly set up a recipient list using a simple CSV file and upload it to your campaign.&#x20;

**To create a new recipient list**:

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Recipients Lists** tab, and click **Create new recipient list.**
* Provide a recipient list name and upload a CSV with the required recipient lists.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* The easiest way to upload a recipient list is to download a sample format of the recipient list, update or make a copy of the same file, rename it as required, and then upload the file. &#x20;
* Since this is your first outreach program and first recipient list, specify only the required details with a test email and skip the other details for now. See [Create new recipient list,](https://docs.avaamo.com/user-guide/outreach/recipient-lists) for more detailed information.
  {% endhint %}

### Step 4: Create and test your campaign

* In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Campaigns** tab, and click **Create new campaign -> Custom channel**.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUkAUuonmXPqfsen60eOZ%2Fimage.png?alt=media&#x26;token=8146f6f9-d607-454b-9a0a-84a0490715ea" alt=""><figcaption></figcaption></figure>

* In the **Configure** section, specify the following details:
  * Campaign name, campaign description, pick the recipient list created in [Step 3: Create a new recipient list](#step-3-create-a-new-recipient-list)
  * Select a channel from an existing agent to make your campaign conversational. Pick the agent deployed on the Custom channel with all the prerequisites and channel settings for triggering the campaign message. See [Step 1: Create an agent and deploy on Custom channel](#step-1-create-an-agent-and-deploy-in-custom-channel), for more information.
  * Click **Next** to proceed with the next step.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fz1PxQxLK6F9NpOatG9MZ%2Fimage.png?alt=media&#x26;token=310b570a-88a6-4c3f-a2c3-27abe2b22114" alt=""><figcaption></figcaption></figure>

* In the **Add Message** section, specify a text message and select the primary header such as email or phone number or uuid and click **Next**.&#x20;
  * The field selected in the primary header is the `client_uuid` in the custom channel outgoing payload.&#x20;
  * A campaign triggered to a recipient is hence identified by the combination of `channel_uuid and client_uuid` in the Avaamo Conversational AI Platform.&#x20;
  * See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#payload-details), for more information on the outgoing message payload format.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7rl417BKmF1qJfun101v%2Fimage.png?alt=media&#x26;token=fab75592-7e89-4864-a352-3795388d5527" alt=""><figcaption></figcaption></figure>

* In the **Activate** section, pick when you wish to send the outreach program to the users. You can either send it right after activating the campaign or at a specific scheduled time. Since this is your first outreach program, enable **Send on activate** toggle option. See [Activate](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate) section, for more information on scheduling a campaign at a specific time.
* Click **Create** to save your first campaign. A summary details pop-up is displayed. You can quickly glance at all the details and click **Activate** to test your campaign.&#x20;
* Since you have opted to send the campaign on activation, a message is sent via the Custom channel and received on the API URL as mentioned in the custom channel confirmation. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#payload-details), for more information on the outgoing message payload format.
* It is Middleware's responsibility to transform the message to and from the custom channel and third party respectively. See [Step 2: Create Middleware - Message transformer](#step-2-create-middleware-message-transformer), for more information.

### Step 5: Send status update from Middleware

When a campaign message payload is sent to the Middleware via the custom channel, a `status_callback_url` is also sent in the payload for each recipient. The Middleware component can use the `status_callback_url` for sending the status of the outreach message back to the Avaamo Conversational AI Platform based on the status update received from the third party.

This helps to map the status of the campaign message to the corresponding recipient. Once the status is received via the callback URL, the same status is updated for the corresponding recipient in the campaign in the Avaamo Conversational AI Platform. You can also view the status in the [Campaign statistics](https://docs.avaamo.com/user-guide/outreach/campaign-statistics) page.&#x20;

See [Status Callback URL](https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/status-callback-url-outreach-custom-channel), for more information on the API.

{% hint style="info" %}
**Note**: Middleware transformer component is outside the scope of the Avaamo Conversational AI Platform. It is the responsibility of the party wishing to integrate a third-party channel with Avaamo to ensure that the Middleware is in place and working as expected.&#x20;
{% endhint %}

### Next steps&#x20;

Now that you have successfully created and tested your first outreach program, you can dig deeper and understand:

* [How to schedule a campaign?](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#activate)
* [How to deactivate a campaign?](https://docs.avaamo.com/user-guide/campaigns/manage-campaigns#deactivate-campaign)
* [How to create customized Custom channel templates for different outreach programs?](https://docs.avaamo.com/user-guide/templates#custom-message)
