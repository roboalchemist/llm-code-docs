# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/user-authentication.md

# Source: https://docs.asapp.com/messaging-platform/integrations/android-sdk/user-authentication.md

# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/user-authentication.md

# User Authentication

## Set an ASAPPUser with a Request Context Provider

As in the Quick Start section, you can connect to chat as an anonymous user by specifying a nil user identifier when initializing an `ASAPPUser`. However, many use cases might require ASAPP to know the identity of the customer.
To connect as an identified user, please specify a user identifier string and a request context provider function. This provider will be called from a background thread when the SDK makes requests that require customer authentication with your company's servers. The request context provider is a function that returns a dictionary with keys and values agreed upon with ASAPP. Please ask your Implementation Manager if you have questions.
**Example:**

```json  theme={null}
let requestContextProvider = { needsRefresh in
    return [
        "Auth": [
            "Token": "exampleValue"
        ]
    ]
}
ASAPP.user = ASAPPUser(userIdentifier: "testuser@example.com",
requestContextProvider)
```

## Handle Login Buttons

If a customer connects to chat anonymously, they may be asked to log in when necessary by being shown a message button:

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=96e6df2db899576bf842c00d7278ead6" data-og-width="660" width="660" data-og-height="334" height="334" data-path="image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b3011bd07ad81b26bb8da042c0d2b8ad 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=f3dd690f8488f79288e05c634d03c994 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=68db17ac322df05db8e2a0eecf8f3380 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=cd472cf0ff2bc039576dbf6cb083016a 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e21f62728eb104218101d7d3241b909f 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-38220938-03e4-8029-538b-b2a4e5c694ac.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a46c8ce8d38b664e0e529f68d1d453eb 2500w" />
</Frame>

If the customer then taps on the **Sign In** button, the SDK will call a delegate method: `chatViewControllerDidTapUserLoginButton()`. Please implement this method and set `ASAPP.user` once the customer has logged in. The SDK will detect the change and then authenticate the user. You may set `ASAPP.user` in any thread. Make sure to set the delegate as well: for example, `ASAPP.delegate = self`. See `ASAPPDelegate` for more details.

## Token Expiration and Refresh the Context

In the event that the provided token has expired, the SDK will call the request context provider with an argument that is true, indicating that you must refresh the context. In that case, please make sure to return a dictionary with fresh credentials that the SDK can use to authenticate the user. If the SDK requires an API call to refresh the credentials, please make sure to block the calling thread until you can return the updated context.
