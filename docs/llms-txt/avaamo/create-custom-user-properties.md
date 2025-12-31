# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties.md

# Create custom user properties

You can use [context.user.custom\_properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user) to get any additional user properties specified by the channel when sending a request to the agent.&#x20;

You can set custom properties in one of the following ways:

1. **Using parameter in the web channel URL**: In the web channel, you can pass custom properties in the URL, using `custom_properties[<<key1>>]=<<value1>>` in the web channel URL. See [Customization parameters](https://docs.avaamo.com/user-guide/build-agents/configure-agents/deploy/web-channel/configure-web-channel#advanced-customization-parameters), for a complete list of parameters that can be passed in the web channel URL.&#x20;
2. Using **User.setProperty:** You can also set custom properties using **User.setProperty**. See [Set user property](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/set-user-property), for more information.

{% hint style="info" %}
**Note**: You can also access custom properties using `context.params.custom_properties` from the [User Authentication Handler](https://docs.avaamo.com/user-guide/build-agents/configure-agents/define-settings#user-authentication-handler).
{% endhint %}

Consider that the MacPizza application sends the **custId** and **customerType** properties in the **context user** object through a [custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel) when a user starts interacting with the agent:

```javascript
{
  "bot_uuid": "edb408fb-de21-45ed-b899-915eb5cab81e",
  "channel_uuid": "5acc8a59-1c51-4735-8b28-dc2f0151533c",
  "event_type": "MESSAGE",
  "user": {
    "uuid": "9ac15843-151d-47fb-8b3d-930b89ce797e",
    "first_name": "Will",
    "last_name": "Smith",
    "layer_id": "e3e7372d-70ee-43cc-ad2d-747e477e88e5",
    "custom_properties": {
      "custId": "11521932",
      "customerType": "guest"
    }
  },
  "conversation": {
    "uuid": "c040161d7299f0c5b3d995fc086c1ce9"
  },
  "sender": "BOT",
  "message": {
    "text": "Hi Will welcome to Mac Pizza",
    "request_message_uuid": "92cdceb1-6a4f-4096-a002-7dd656a21c54",
    "sequence": 1
  }
}
```

The following is a sample JS to get the custom user properties and [store in a user session ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/using-storage#set-and-get-user-variables)that can be used later:

```javascript
if (context.user.custom_properties) {
    context.variables.custId = context.user.custom_properties.custId;
    context.variables.customerType = context.user.custom_properties.customerType;
    Storage.user.set("custId", context.variables.custId);
    Storage.user.set("customerType", context.variables.customerType);
    console.log("custId: ", context.variables.custId);
    console.log("customerType: ", context.variables.customerType);
} else {
    Storage.user.set("custId", "");
    Storage.user.set("customerType", "");
    console.log("No user details found.");
}
```

Since there are "console log" statements in the above code, you can use [Debug logs](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/debug-logs) to view the log statements:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzuBAZpAK7rp6Wh0T5fSr%2Fimage.png?alt=media\&token=9d844a9c-969a-4872-b611-0a9440b731ed)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
