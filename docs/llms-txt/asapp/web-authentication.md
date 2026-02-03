# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Authentication

This section details the process for authenticating your users to the ASAPP Chat SDK.

* [Authenticating at Page Load](#authenticating-at-page-load "Authenticating at Page Load")
* [Authenticating Asynchronously](#authenticating-asynchronously "Authenticating Asynchronously")
* [Using the 'UserLoginHandler' Method](#using-the-userloginhandler-method "Using the 'UserLoginHandler' Method")

Before getting started, make sure you've [embedded the ASAPP Chat SDK](/agent-desk/integrations/web-sdk/web-quick-start#1-embed-the-script "1. Embed the Script") into your site.

<Note>
  Your site is responsible for the entirety of the user authentication process. This includes the presentation of an interface for login and the maintenance of a session, and for the retrieval and formatting of context data about that user. Please read the section on using the [Authentication with the ContextProvider](/agent-desk/integrations/web-sdk/web-contextprovider#authentication "Authentication") to understand how you can pass authorization information to the Chat SDK.
</Note>

Once your site has authenticated a user, you can securely pass that authentication forward to the ASAPP Chat environment by making certain calls to the ASAPP Chat SDK (more on those calls below). Your user can then be authenticated both on your web site and in the ASAPP Chat Environment, enabling them to execute within the ASAPP Chat use cases that require authentication.

ASAPP provides two methods for authenticating a user to the ASAPP Chat SDK.

* You can proactively [authenticate your user at page load](#authenticating-at-page-load "Authenticating at Page Load").
* You can [authenticate your user midway through a session](#authenticating-asynchronously "Authenticating Asynchronously") using the [SetCustomer API](/agent-desk/integrations/web-sdk/web-javascript-api#setcustomer "'setCustomer'").

With rare exceptions, you must also configure [UserLoginHandler](#using-the-userloginhandler-method "Using the 'UserLoginHandler' Method") to enable ASAPP to handle cases where a user requires authentication or re-authentication in the midst of a chat session (e.g., if a user's authentication credentials expire during a chat session.)

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f0a3e8b0941ca34e26df9268d9334a4a" data-og-width="1132" width="1132" data-og-height="662" height="662" data-path="image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=7177b6c2289e5da9ef0f867f8b4838e8 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2879a1fa4e884d43e1e1429170f7e4ee 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5ac392f858f7472a6c3519f82f571cc7 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9ec3c9b8a3c14e1abc87fa62c943a6b6 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ddb1c6f7974c02774288d7b505843ad6 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8ade9d85-5d88-c79d-ac59-de17e894032d.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=82c0c46cb37d1c7b5190e8511d58c6cf 2500w" />
</Frame>

## Authenticating at Page Load

If a user who is already authenticated with your site requests a page that includes ASAPP chat functionality, you can proactively authenticate that user to the ASAPP SDK at page load time. This allows an authenticated user who initiates a chat session to have immediate access to their account details without having to login again.

To authenticate a user to the ASAPP Chat SDK on page load, use the ASAPP [Load API](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'") providing both [ContextProvider](/agent-desk/integrations/web-sdk/web-app-settings#contextprovider "ContextProvider") and [CustomerId](/agent-desk/integrations/web-sdk/web-app-settings#customerid "CustomerId") as additional keys in the [Load method](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'").

For example:

```javascript  theme={null}
<script>
ASAPP('load', {
    APIHostname: 'examplecompanyapi.asapp.com',
    AppId: 'examplecompany',
    CustomerId: 'UserName123',
    ContextProvider: function (callback) {
        var context = {
            Auth: {
                Body: {
                    token_expiry: '1530021131',
                    token_scope: 'store'
                },
                Token: '3858f62230ac3c915f300c664312c63f'
            },
        };
        callback(context);
    }
});
</script>
```

The sample above initializes the ASAPP Chat SDK with your user's `CustomerId` and a `ContextProvider` incorporating that user's `Auth`.

When a user opens the ASAPP Chat SDK, they are already authenticated to the chat client and can access account information within the chat without being asked to login again.

## Authenticating Asynchronously

If a user's authentication credentials are not available at page load time, you can authenticate asynchronously using the ASAPP [SetCustomer](/agent-desk/integrations/web-sdk/web-javascript-api#setcustomer "'setCustomer'") API.

After you've retrieved your user's credentials, you can call the API to authenticate that user with the ASAPP Chat SDK mid-session.

You might want to asynchronously authenticate a user to the ASAPP Chat SDK when (for example) that user has just completed a login flow, or if their credentials are retrieved after the page initially loads, or if a session expires and the user needs to reauthenticate.

The following sample snippet shows how to call the SetCustomer API:

```javascript  theme={null}
<script>
ASAPP('setCustomer', {
    CustomerId: 'UserName123',
    ContextProvider: function (callback) {
        var context = {
            Auth: {
                Token: '3858f62230ac3c915f300c664312c63f'
            },
        };
        callback(context);
    }
});
</script>
```

Once you call the [SetCustomer](/agent-desk/integrations/web-sdk/web-javascript-api#setcustomer "'setCustomer'") method, and as long as the provided `Auth` information remains valid on your backend, any ASAPP Chat SDK actions that require authentication authenticate properly.

<Note>
  The SetCustomer method is typically called as part of the [UserLoginHandler](/agent-desk/integrations/web-sdk/web-app-settings#userloginhandler-11877 "UserLoginHandler").

  See the section on [Using the 'UserLoginHandler' Method](#using-the-userloginhandler-method "Using the 'UserLoginHandler' Method") for a complete picture of how you may want to authenticate a user during an ASAPP Chat SDK session.
</Note>

## Using the 'UserLoginHandler' Method

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1e6e4df222a0387b14c5f14b343bd1f5" data-og-width="1612" width="1612" data-og-height="910" height="910" data-path="image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=e74ca51ea2cedc5240afa49a8c2bce12 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4f1705e692216d2af41fae853f08a4a7 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ca91ab0b57c28091feaff6a88ca5efcc 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6ddb06fb81493d0dd75d0a488f1d3fe3 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f4ba2b9666e8d9c1944178d68d459393 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4699ebd3-525e-b694-a3b6-1e329e71fbbd.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fff5eef3c138893c26343dc772d4b5af 2500w" />
</Frame>

```javascript  theme={null}
<script>
ASAPP('load', {
    APIHostname: 'examplecompanyapi.asapp.com',
    AppId: 'examplecompany',
    UserLoginHandler: function () {
        /*
            Use case #1
            1. Redirect the user to a login page
            2. User logs in
            3. Once user is redirected, use `ASAPP('load', ...)`
               API to set authorization at page load
            Use case #2
            1. Show a login modal
            2. Authenticate the user asynchronously
            3. Retrieve and set the customer's ID and access token
               with `ASAPP('setCustomer', ...)`
        */
    }
});
</script>
```
