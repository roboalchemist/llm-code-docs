# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/detect-channel.md

# Detect user device

You can use **context.user.getDevice()** to get the device details of the user interacting with the agent. See [getDevice()](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/context/user#getdevice), for more information.

Consider that for analytical purposes you wish to log the details of the "user agent" with which the user is interacting with the MacPizza agent. The following is a sample JS to get the channel details and display them on the console. Similarly, you can get channel details and later use an external API to send data for analytical purposes, as required:

```javascript
var device = await(context.user.getDevice());
return "User agent details: " + device.user_agent;
```

In the agent, the "user agent" details are returned:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FR0xYuP3lH2tCJgIvxRmz%2Fimage.png?alt=media\&token=811fbe8d-22f3-40cd-aefa-4e6fa62e3302)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
