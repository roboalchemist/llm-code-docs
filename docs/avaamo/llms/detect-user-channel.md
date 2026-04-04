# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/detect-user-channel.md

# Detect user channel

You can use **context.user.getChannel()** to get the device details of the user interacting with the agent. See [getDevice()](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/context/user#getdevice), for more information.

Consider that for analytical purposes you wish to log the details of the "Channel name" with which the user is interacting with the MacPizza agent. The following is a sample JS to get the channel details and display them on the console. Similarly, you can get channel details and later use an external API to send data for analytical purposes, as required:

```javascript
var channel = await(context.user.getChannel());
return "Here is the channel name - " + channel.name;
```

In the agent, the channel details is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fe7nSu9ePTHXTX7VLbWRV%2Fimage.png?alt=media\&token=920d2866-a0ea-4942-abe0-3bdb21f55c53)
