# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/custom-properties-api.md

# Custom properties API

## Get custom user properties&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/v1/user_info/{{user_id}}.json?access_token={{agent_access_token}}`

Get details about custom user properties from the agent.

#### Path Parameters

| Name                                       | Type    | Description                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user\_id<mark style="color:red;">\*</mark> | integer | <p>User identifier. Based on the requirement, you can get the user identifier in one of the following ways: <br>- From the <strong>avaamo\_id</strong> attribute in the <a href="../message-api#get-agent-messages">Get Message API.</a> <br>- From the <strong>user -> Id</strong> attribute in the <a href="agent-api/query-insights">Query Insights API</a>.<br></p> |

#### Query Parameters

| Name                                            | Type   | Description                                                                                                                                                                                                                                                                    |
| ----------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| access\_token<mark style="color:red;">\*</mark> | string | The agent access token. You can get agent access token from Agent -> Configuration -> Settings page. See [Agent Authentication Keys](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#agent-authentication-keys), for more information. |

{% tabs %}
{% tab title="200 Success" %}

```javascript
{
  "user_info": [
    {
      "user_id": 30572,
      "key": "customerType",
      "value": "guest"
    },
    {
      "user_id": 30572,
      "key": "customerLocation",
      "value": "India"
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/v1/user_info/30xxx.json?access_token=xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/v1/user_info/30xxx.json?access_token=xxxxxx8d9952499ea466fc007dxxxxxx',
  'headers': {
    'Content-Type': 'application/json'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endtab %}
{% endtabs %}

### Response attributes

In the response, user\_info array is returned with the key and value for each custom property:

| Attribute | Description                                 | Type   |
| --------- | ------------------------------------------- | ------ |
| key       | Indicates the key of the custom property.   | String |
| value     | Indicates the value of the custom property. | String |
