# Source: https://documentation.onesignal.com/docs/en/example-tag-substitution.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Personalize in-app messages

> Target users based on their data tags with tag substitution

Using [Message Personalization](./message-personalization) through [Data Tags](./add-user-data-tags), you can update your In-App Messages.

In the screenshots below, the In-App is configured with data tags in:

* Text block - to display the completed level and the reward for that level
* Image block - to display the image corresponding to the reward, along with the default image
* Button 2 text - to list down the reward value, along with the default value of 100
* Background image

<Frame caption="In-app message editor">
    <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b697ab5-config1.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=c40e541c296b138a7f04ac561b3b0c64" alt="" width="872" height="968" data-path="images/docs/b697ab5-config1.png" />
</Frame>

<br />

Here is how the In-App Message is displayed on the user’s device based on the completed level.

<Frame caption="In-app message displayed">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/973f097-JustTheIAMTagSub.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=0626ef7b31dfbfece633e74b072fbff5" style={{ width:"100%" }} width="338" height="607" data-path="images/docs/973f097-JustTheIAMTagSub.png" />
</Frame>

<Warning>
  [Property substitution](./using-liquid-syntax#property-include) does not work for In-App Messages at this time.

  Tag substitution does not work when an in-app message sending to test users via the "Send Test Message" buttons.
</Warning>

Built with [Mintlify](https://mintlify.com).
