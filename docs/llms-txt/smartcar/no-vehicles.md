# Source: https://smartcar.com/docs/errors/connect-errors/no-vehicles.md

# No Vehicles

> This error occurs when a vehicle owner has a connected services account, but there are no vehicles associated with the account.

| Parameter          | Required | Description                                                  |   |
| ------------------ | -------- | ------------------------------------------------------------ | - |
| error              | true     | no\_vehicles                                                 |   |
| error\_description | true     | User does not have an active connected vehicle subscription. |   |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=no_vehicles&error_description=No%20vehicles%20found.%20Please%20add%20vehicles%20to%20your%20account%20and%20try%20again.
```

The error is triggered when a user logs into their connected services account and is shown to have no vehicles listed like in the example below for BMW.

<Frame caption="No Vehicle Error">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=903fa8967ececee46d63b6f1c6aac5e0" data-og-width="455" width="455" data-og-height="478" height="478" data-path="images/api-reference/no_vehicle_error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a96f4ec8480911f6e7d7027eb49b6d87 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ee814a28e518096eee6fcde00cded710 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=998aadc98e9937aad55104a36b43af3b 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9d7cdaaadbac395ee86c112b98465a1d 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c938e037f052aee494e360ac3f2c3bb4 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d5df8eda25c97ae8c89e8d931ff5a00c 2500w" />
</Frame>

The user has the option to add vehicles or return to your application.
