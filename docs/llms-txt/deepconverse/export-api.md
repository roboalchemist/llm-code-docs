# Source: https://docs.deepconverse.com/product-docs/analytics/export-api.md

# Export API

{% hint style="info" %}
This feature is only available with the **Enterprise** plan
{% endhint %}

We provide ability for you to export conversations and messages for internal analytics, GDPR or storage purposes at your premises.

The Export API consists of two endpoints:

* Conversations&#x20;
  * Conversation data along with metadata and parameters
* Messages
  * Individual messages exchanged between customers, agents and chatbot

### Usage Limitations

The API is accessing data from our archive and storage. To ensure a smooth experience we enforce the following limitations:

#### Rate Limit

The API is limited to 3 requests / per second per endpoint.

#### Page Size&#x20;

Exports utilize a cursor based iteration. Each call is limited to 1000 records that can be exported.&#x20;

### API access token

You will need your API access token to export the data. Your account access token can be found in the dashboard and is only accessible to the site admin.

You will find this under **Account** > **API**&#x20;

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FV9c0MxVidcjYqTo85kXl%2Fimage.png?alt=media&#x26;token=4d8d8740-e1ef-4074-bd15-97d63dc7f594" alt=""><figcaption></figcaption></figure>
