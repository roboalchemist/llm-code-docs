# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/user-authentication.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/user-authentication.md

# User Authentication

As in the Quick Start section, you can connect to chat as an anonymous user by not setting a user, or initializing an `ASAPPUser` with a null customer identifier. However, many chat use cases might require ASAPP to know the identity of the user.

To connect as an identified user, please specify a customer identifier string and a request context provider function. This provider will be called from a background thread, when the SDK makes requests that require customer authentication with your company's servers. The request context provider is a function that returns a map with keys and values agreed upon with ASAPP. Please ask your Implementation Manager if you have questions.

## Example:

```kotlin  theme={null}
val requestContextProvider = object : ASAPPRequestContextProvider {
    override fun getASAPPRequestContext(user: ASAPPUser,
                                        refreshContext:Boolean): Map<String, Any>? {
        return mapOf(
            "Auth" to mapOf(
                "Token" to "example-token"
            )
        )
    }
}
ASAPP.instance.user = ASAPPUser("testuser@example.com", requestContextProvider)
```

## Handle Login Buttons

If you connect to chat anonymously, you may be asked to log in when necessary by being shown a message button:

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f7ba73739835eeba130b45ae70053f49" data-og-width="660" width="660" data-og-height="334" height="334" data-path="image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=699f9d4122431625334daa96275a1998 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e890c2c78c10c7f155777235340a15a6 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e2dec323e8db7d2f7b1686e1f0fdd44d 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f46aab6913530212a15827fefc839887 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3dd55dbdc1b7ad83d326977b23e39f60 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bbfa4b7a-ca23-7407-c592-a8d5df402b5c.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1d09f528400968afb8cd8f44329729e8 2500w" />
</Frame>

If you then tap the **Sign In** button, the SDK will use the `ASAPPUserLoginHandler` to call to the application. Due to the asynchronous nature of this flow, your application should use the activity lifecycle to provide a result to the SDK.

How to Implement the Sign In Flow

1. Implement the `ASAPPUserLoginHandler` and start your application's `LoginActivity`, including the given request code.
   ```kotlin  theme={null}
   ASAPP.instance.userLoginHandler = object: ASAPPUserLoginHandler {
       override fun loginASAPPUser(requestCode: Int, activity: Activity) {
           val loginIntent = new Intent(activity, LoginActivity::class.java)
           activity.startActivityForResult(loginIntent, requestCode)
       }
   }
   ```
2. If a user successfully signs into your application, update the user instance and then finish your `LoginActivity` with `Activity.RESULT_OK`.
   ```kotlin  theme={null}
   ASAPP.instance.user = ASAPPUser(userIdentifier, contextProvider) 
   setResult(Activity.RESULT_OK)
   finish()
   ```
3. In case a user cancels the operation, finish your `LoginActivity` with `Activity.RESULT_CANCELED`.
   ```kotlin  theme={null}
   setResult(Activity.RESULT_CANCELED)
   finish()
   ```

After your `LoginActivity` finishes, the SDK will capture the result and resume the chat conversation.

## Token Expiration and Refreshing the Context

If the provided token has expired, the SDK will call the [ASAPPRequestContextProvider](https://docs-sdk.asapp.com/api/chatsdk/android/latest/chatsdk/com.asapp.chatsdk/-a-s-a-p-p-request-context-provider) with an `refreshContext` parameter set to `true` indicating that the context must be refreshed. In that case, please make sure to return a map with fresh credentials that can be used to authenticate the user. In case an API call is required to refresh the credentials, make sure to block the calling thread until the updated context can be returned.
