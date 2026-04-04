# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/hangup-call-c-ivr-channel.md

# Hangup call (C-IVR channel)

You can use `SmartCall.hangup` method to hang up the call in the C-IVR flow with a message.

{% hint style="info" %}
**Note**: This option works if you have deployed your agent in the C-IVR channel. See the [C-IVR channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
{% endhint %}

```javascript
return [<<message>>, SmartCall.hangup()];
```

Consider that you have an "Order Status" skill in your pizza agent that checks for the order status using the order number provided by the user. You have deployed your agent in the C-IVR channel. You have designed a flow, where you wish to hang up the call after reading out the status of the pizza order. You can use the following JS method to read out the message and hang up the call:&#x20;

```javascript
return ['You order is on its way and will be delivered in 20 minutes. Hanging up the call now. Have a good day.',SmartCall.hangup()];
```
