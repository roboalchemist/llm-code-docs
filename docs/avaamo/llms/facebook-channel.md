# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel.md

# Facebook

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance.
{% endhint %}

The Facebook channel configuration on the Avaamo platform helps you deploy your agent on your Facebook page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M0WOTF3j-Q1E5iwDP4R%2F-M0Wqh62mKeXv7tnS8Bk%2Fagent-deploy-facebook-1.png?alt=media\&token=e3baba14-bb0d-48ed-bf1e-2a32f65427e6)

You can [configure the Facebook channel ](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/untitled)on your agent to use the features supported by the Avaamo platform:

* [Facebook file caching](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-buttons#facebook-file-cache): You can upload media files such as a video or an image or a GIF on your agent for the users to play and view the file multiple times with no buffering or streaming.
* [1:1 aspect ratio for images](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/image-aspect-ratio-facebook): You can upload images with the 1:1 aspect ratio that displays as a square image.
* [Camera button](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-buttons#camera-button): You can add a camera button for users to open the camera.
* [Handover protocol](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/handover-protocol-integration-facebook): You can enable two or more Facebook apps to participate in a conversation by passing control of the conversation between them.
* [Manual Configuration](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/facebook-channel-manual-configuration): You can manually configure the Facebook channel on the Avaamo platform for new apps.
* [Personas](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/persona-configuration): You can create different avatars for the agent.
* [Send scheduled messages](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/message-api): You can schedule messages (using message API) to be displayed on your agent for the users who are subscribed to the Facebook page.

{% hint style="info" %}
**Notes:**

* Audio and video responses are not supported in the Facebook channel&#x20;
* If you have more than one message in the response, then it is recommended to either

  * Add delays between messages in the response, or
  * Split it into two response messages, so that the responses get delivered in the proper sequence when sent to the Facebook channel.&#x20;

  Though the messages are sent sequentially from the Avaamo Platform to the Facebook channel, the FB channel processes this asynchronously, and hence sequencing cannot be assured. The amount of delay to be added between messages is by the trial and error method.
  {% endhint %}
