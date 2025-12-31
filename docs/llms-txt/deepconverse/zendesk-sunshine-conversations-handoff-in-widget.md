# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/zendesk-sunshine-conversations-handoff-in-widget.md

# Zendesk Sunshine Conversations Handoff (In Widget)

We will walkthrough the setup required to do the Sunshine Conversations Handover using the DeepConverse chat widget.&#x20;

{% hint style="info" %}
This article allows you to do a handoff to Zendesk within DeepConverse chat widget&#x20;
{% endhint %}

1. Make sure you have connected to **Zendesk Sunshine Conversations** via the **Connections** page

2. Navigate to **Zendesk Admin** > **Bots**. Here you will see DeepConverse under marketplace bots. <br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FKiukx4Si43svDivEGTmf%2Fimage.png?alt=media&#x26;token=31fb78df-e1f0-4095-8718-078619140655" alt=""><figcaption></figcaption></figure>

3. Go ahead and navigate to **Messaging** to see if the web widget channel is active.<br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FK0eqsqxAyw2QZYmZzPaW%2Fimage.png?alt=media&#x26;token=bdd0439d-691e-4de9-8b91-be50e9316838" alt=""><figcaption></figcaption></figure>

4. Create an API Key for the Conversations API for DeepConverse. <br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FNzothIGckxLGZ8cckVIN%2Fimage.png?alt=media&#x26;token=bc72a935-b30a-401b-866f-e3884b33e6e0" alt=""><figcaption></figcaption></figure>

5. Reach out to the DeepConverse team to find out the **Web Messenger Integration Id** to use for the handoff. This is found via the integrations API \
   [`https://api.smooch.io/v2/apps/{{appId}}/integrations`](https://api.smooch.io/v2/apps/%7B%7BappId%7D%7D/integrations)<br>

6. Use the Web Messenger Integration Id along with the connection and fields to pass to Zendesk in the Escalation Flow.\ <br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FlACBsQPPYc5Y2CfwPObR%2Fimage.png?alt=media&#x26;token=6ab9dc45-844f-4bcc-83b9-727f3df94e39" alt=""><figcaption></figcaption></figure>

7. In order for DeepConverse to receive the Conversation events add a Conversation Integration with the following API: \
   \
   [`https://api.converseapps.com/messaging/smooch/events`](https://api.converseapps.com/messaging/smooch/events)<br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FW1DDTESQsaUyolW0gnPb%2Fimage.png?alt=media&#x26;token=4809660d-d925-4c1c-bafd-218ea78a23ca" alt=""><figcaption></figcaption></figure>

#### Fields Available in Handoff

<table><thead><tr><th width="370">Field Name</th><th>Description</th></tr></thead><tbody><tr><td>tags</td><td>Comma separated list of tags to add to Zendesk ticket</td></tr><tr><td>brand_id</td><td>Id of the Zendesk brand to use</td></tr><tr><td>priority</td><td>Priority of Zendesk ticket</td></tr><tr><td>requester.name</td><td>Name of the requester (Use $ to reference a parameter)</td></tr><tr><td>requester.email</td><td>Email of the requester</td></tr><tr><td>&#x3C;field_id></td><td>Custom field value to set</td></tr></tbody></table>
