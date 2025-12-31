# Source: https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/status-callback-url-outreach-custom-channel.md

# Status Callback URL (Outreach Custom Channel)

## Status of the campaign recipient via the custom channel.

<mark style="color:green;">`POST`</mark> `https://cx.avaamo.com/custom/v1/broadcast/messages/{{recipient_uuid}}/status`

The callback URL used by the campaign middleware component to send the status of the campaign recipient when a campaign is triggered via the custom channel. See [Campaign in Custom channel](https://docs.avaamo.com/user-guide/outreach/quick-start/campaign-in-custom-channel), for more information.

You can also use PUT instead of POST request

#### Path Parameters

| Name                                              | Type   | Description                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| recipient\_uuid<mark style="color:red;">\*</mark> | String | Recipient conversation identifier. You can get the recipient\_uuid from the status\_callback\_url parameter in the custom channel payload of the outgoing campaign message. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#payload-details), for more information. |

#### Headers

| Name                                           | Type   | Description      |
| ---------------------------------------------- | ------ | ---------------- |
| Content-Type<mark style="color:red;">\*</mark> | String | application/JSON |

#### Request Body

| Name                                     | Type    | Description                                                                                                                                                                                                                   |
| ---------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| error\_message                           | String  | The error message, if any. The error message is considered only when the error code is not mentioned, else the standard error message corresponding to the error code is used or the error message is set to "Unknown error". |
| error\_code                              | Integer | The error code of the campaign message.                                                                                                                                                                                       |
| status<mark style="color:red;">\*</mark> | String  | <p>Status of the campaign message. Possible values are - sent, failed, delivered, undelivered, skipped. </p><p>When a campaign message is sent, the initial status is set as "sent". </p>                                     |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
    "success": true
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl --location 'https://cx.avaamo.com//custom_channel/v1/broadcast/messages/f37f402c-b992-484a-bc5e-b24f6c872807/status' \
--header 'Content-Type: application/json' \
--data '{
  "status": "delivered"
}
'
```

{% endcode %}
{% endtab %}

{% tab title="node.js" %}
{% code overflow="wrap" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com//custom_channel/v1/broadcast/messages/f37f402c-b992-484a-bc5e-b24f6c872807/status',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "status": "delivered"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});


```

{% endcode %}
{% endtab %}
{% endtabs %}
