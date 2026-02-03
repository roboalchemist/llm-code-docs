# Source: https://smartcar.com/docs/errors/connect-errors/access-denied.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Access Denied

> This error occurs when a user denies your application access to the requested scope of permissions.

| Parameter           | Required | Description                        |
| ------------------- | -------- | ---------------------------------- |
| `error`             | `true`   | `access_denied`                    |
| `error_description` | `true`   | User denied access to application. |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home
?error=access_denied
&error_description=User+denied+access+to+application
```

## Testing

To test this error, launch Smartcar Connect in test mode and select “Deny access” on the permissions screen.

<Frame caption="Access Denied">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b45ddc2c280b865a3771507961d5ca39" data-og-width="1275" width="1275" data-og-height="773" height="773" data-path="images/api-reference/access_denied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b97ec8e6693eabba309af544dda4c7de 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=77c637f8151eda1513b07e61b78f5eab 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5580026d6dc60cba5a07ad7226232387 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=df87b9ccfe523517f78519dc0deaa9d6 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=897b2604624fc2b93a72870dd10a1f31 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3f1c8bdcd7945574102fbda9d1d58507 2500w" />
</Frame>

We recommend handling this error by re-prompting the user to authorize their vehicle and adding a message like in the example below.

<Frame caption="Access Denied Message">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=844e2501b98ecbb86634f85e969e9499" data-og-width="1275" width="1275" data-og-height="775" height="775" data-path="images/api-reference/access_denied_message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e61896e9355dd35847c69b49d7625d68 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5eb24ca7748ca2ffdb7b6a5cfaccd480 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=84e88aba94b6b918e11af0112ba4a2e3 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bca717e762619039ea2c9144b85242f2 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ef18bbc6c88ec00f2bccbc6a47cb1691 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1ac814add89245e26defb2a4337b9996 2500w" />
</Frame>
