# Source: https://smartcar.com/docs/errors/connect-errors/invalid-subscription.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Invalid Subscription

> This error occurs when a user’s vehicle is compatible but their connected services subscription is inactive because either it has expired or it has never been activated.

| Parameter          | Required | Description                                                  |   |
| ------------------ | -------- | ------------------------------------------------------------ | - |
| error              | true     | invalid\_subscription                                        |   |
| error\_description | true     | User does not have an active connected vehicle subscription. |   |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=invalid_subscription
&error_description=User%20does%20not%20have%20an%20active%20connected%20vehicle%20subscription
```

Smartcar will direct the user to the connected services website to (re-)activate their subscription. However, a user may choose to return back to your application instead, like in the example below.

<Frame caption="No Subscription">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=afd7635f3f21192d982b66bbe823f217" data-og-width="1275" width="1275" data-og-height="774" height="774" data-path="images/api-reference/no_subscription.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e1a56a41389ab618dc64d3df3494d360 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=830d21e11f453eaec9fcd3f7f8fa0666 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=626c6922cf2c384cf8d9b81f9fed33ae 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=66532b981cf306ba4f55387aeb11095b 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1e9c50d30adffc8a5a02409b30b32756 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=28ae13b73828f13f9b6ae7060e795dd9 2500w" />
</Frame>

## Testing

To test this error, launch Smartcar Connect in test mode and log in with the email [smartcar@invalid-subscription.com](mailto:smartcar@invalid-subscription.com) and any password. If you use Single Select, please see the table below for a simulated VIN.

| Email                                                                         | VIN               |
| ----------------------------------------------------------------------------- | ----------------- |
| [smartcar@invalid-subscription.com](mailto:smartcar@invalid-subscription.com) | 0SCAUDI0155C49A95 |

In the event of an `AUTHENTICATION_FAILED`, the user will need to be prompted to re-connect their vehicle. Smartcar Connect Re-authentication makes the process of re-authenticating a user much more seamless. In addition, the `AUTHENTICATION_FAILED` error provides a partially constructed URL for the re-authentication flow inside the resolution object.
