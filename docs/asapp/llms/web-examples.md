# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Examples

This section provides a few common integration scenarios with the ASAPP Chat SDK.

Before continuing, make sure you've [integrated the ASAPP SDK](/agent-desk/integrations/web-sdk/web-quick-start "Web Quick Start") script on your page. You must have the initial script available before utilizing any of the examples below. Also, be sure that you have a [Trigger](/agent-desk/integrations/web-sdk/web-features#triggers "Triggers") enabled for the page(s) you wish to display the Chat SDK.

* [Basic Integration (no Authentication)](#basic-integration-no-authentication "Basic Integration (no Authentication)")
* [Basic Integration (With Authentication)](#basic-integration-with-authentication "Basic Integration (With Authentication)")
* [Customizing the Interface](#customizing-the-interface "Customizing the Interface")
* [Advanced Integration](#advanced-integration "Advanced Integration")

## Basic Integration (no Authentication)

The most basic integrations are ones with no customizations to the ASAPP interface and no integrated use cases. If your company is simply providing an un-authed user experience, an integration like the one below may suffice.

ee the [App Settings](/agent-desk/integrations/web-sdk/web-app-settings "Web App Settings") page for details on the [APIHostname](/agent-desk/integrations/web-sdk/web-app-settings#apihostname "APIHostName") and [AppId](/agent-desk/integrations/web-sdk/web-app-settings#appid "AppId") settings. The following code snippet is an example of a non-authenticated integration with the ASAPP Chat SDK.

```json  theme={null}
document.addEventListener('DOMContentLoaded', function () {
    ASAPP('load', {
        APIHostname: 'example-co.api.asapp.com',
        AppId: 'example-co'
    });
});
```

With the above information set, a user will be able to access integrated use cases. If their session or token information has expired, then the user will be presented with a "Sign In" button. Once the user clicks the Sign In button, the Chat SDK will call your provided UserLoginHandler, allowing them to authorize. Here's a sample of what the Sign In button looks like.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8356aeef199beb98623a0433339ecebe" data-og-width="1070" width="1070" data-og-height="662" height="662" data-path="image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b16291bf3adbb49859596fde223a16c1 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d8ea1db893ef9f4e783999f2087fc98a 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=14b0bc7f7a3129c0cdbfe042a438c92d 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0cd21c3ad1e57079d630f856419df77a 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=868b3ad4d38c5deca34a5d1381773c33 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efa8b7d8-cb74-a362-73a8-5af1cd58d9e5.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e8e7c5581978393d4ca2f8edeaf2ab3f 2500w" />
</Frame>

## Basic Integration (With Authentication)

Integrating the Chat SDK with authenticated users requires the addition of the `CustomerId`, `ContextProvider`, and `UserLoginHandler` keys.

See the [App Settings](/agent-desk/integrations/web-sdk/web-app-settings "Web App Settings") page for more detailed information on their usage. With each of these keys set, a user will be able to access integrated use cases or be capable of logging in if they are not already.

The following code snippet is an example of providing user credentials for allowing a user to enter integrated use cases.

```json  theme={null}
document.addEventListener('DOMContentLoaded', function () {
    ASAPP('load', {
        APIHostname: 'example-co.api.asapp.com',
        AppId: 'example-co',
        CustomerId: 'hashed-customer-identifier',
        ContextProvider: function (callback, tokenIsExpired) {
            var context = {
                Auth: {
                    Token: 'secure-session-user-token'
                }
            };
            callback(context);
        },
        // If a user's token expires or their user credentials
        // are not available, handle their login path
        UserLoginHandler: function () {
            window.location.href = '/login';
        }
    });
});
```

With the above information set, a user will be able to access integrated use cases. If their session or token information has expired, then the user will be presented with a "Sign In" button.

Once the user clicks the Sign In button, the Chat SDK will call your provided `UserLoginHandler`, allowing them to authorize.

Here's a sample of what the Sign In button looks like.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=45868fc72539fcc66a11b4e92e452e67" data-og-width="1070" width="1070" data-og-height="662" height="662" data-path="image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4892361b8443362b2768efe973a843ed 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3cfb70c21f005407c18372ebf0edbec9 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e17f3ac872911befd133c64d40b8718e 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b85e816b411d4adb8bfd334890da1991 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0eabab981cff4d9f8778584bd8532ec4 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cdd86419-d919-b30f-d58f-58a236ccb57e.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4b49cedaa8de3aa841e64ab3bd224f49 2500w" />
</Frame>

## Customizing the Interface

The Chat SDK offers a few basic keys for customizing the interface to your liking.

The `Display` key enables you to perform those customizations as needed. Please see the [Display Settings](/agent-desk/integrations/web-sdk/web-app-settings#display "Display") section for detailed information on each of the available keys.

The following code snippet shows how to add the Display key to your integration to customize the display settings of the Chat SDK.

```json  theme={null}
document.addEventListener('DOMContentLoaded', function () {
    ASAPP('load', {
        APIHostname: 'example-co.api.asapp.com',
        AppId: 'example-co',
        Display: {
            Align: 'left',
            AlwaysShowMinimize: true,
            BadgeColor: '#36393A',
            BadgeText: 'Chat With Us',
            BadgeType: 'tray',
            FrameDraggable: true,
            FrameStyle: 'sideBar'
        }
    });
});
```

For cases in which you have more specific styling needs, you may utilize the available IDs or classnames for targeting and customizing the Chat SDK elements with CSS.

These selectors are stable and can be used to target the ASAPP Badge and iFrame for specific styling needs.

The following code snippet provides a CSS example showcasing a few advanced style changes.

```json  theme={null}
#asapp-chat-sdk-badge,
#asapp-chat-sdk-badge,
#asapp-chat-sdk-badge {
    border-radius: 25px;
    bottom: 10px;
    box-shadow: 0 0 0 2px #fff, 0 0 0 4px #36393A;
}
#asapp-chat-sdk-iframe {
    border-radius: 0;
}
```

With the above customizations in place, the Chat SDK Badge will look like the following.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b43ea0d466edcc89e1fb94a8cb0f4e30" data-og-width="640" width="640" data-og-height="120" height="120" data-path="image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8023c8732d3a91372981e7dd9eff3938 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f1d744ce558bc55baa0309d6e8325339 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6f24a82615194434c70c52879ebea5c6 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=43f699e5e806909e0f7ca20868b30746 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9b553611b022a67199ed8d8651654467 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-ef02c2ea-81d6-a600-7880-0f66c789599d.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3be316d111c1f6aaadbd13d29c390758 2500w" />
</Frame>

## Advanced Integration

Here's a more robust example showing how to utilize most of the ASAPP Chat SDK settings.

In the examples below we will define a few helper methods, then pass those helpers to the [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'") or [SetCustomer](/agent-desk/integrations/web-sdk/web-javascript-api#setcustomer "'setCustomer'") APIs.

The following example showcases a [ContextProvider](/agent-desk/integrations/web-sdk/web-contextprovider "Web ContextProvider") that sets some basic session information, then sets any available user authentication information. Once that information is retrieved, it passes the prepared context to the `callback` so that ASAPP can process each Chat SDK request.

The following code snippet is a ContextProvider example utilizing session expiration conditionals.

```javascript  theme={null}
function asappContextProvider (callback, tokenIsExpired, sessionInfo) {
    var context = {
        CustomerInfo: {
            Region: 'north-america',
            ViewingProduct: 'New Smartphone',
        }
    };
    if (tokenIsExpired || !sessionInfo) {
        sessionInfo = retrieveSessionInfo();
    };
    if (sessionInfo) {
        context.Auth = {
            Cookies: {
                'X-User-Header': sessionInfo.cookies.userValue
            },
            Token: sessionInfo.access_token
        };
    }
    callback(context);
}
```

The next example shows conditional logic for logging a user in on single or multi-page application. You'll likely only need to handle one of the cases in your application.

If a user enters a use case they are not authorized for, they will be presented with a "Sign In" button within the SDK.

When the user clicks that link, it will trigger your provided [UserLoginHandler](/agent-desk/integrations/web-sdk/web-app-settings#userloginhandler "UserLoginHandler") so you can allow the user to authenticate.

The following code snippet shows a UserLoginHandler utilizing page redirection or modals to log a user in.

```javascript  theme={null}
function asappUserLoginHandler () {
    if (isSinglePageApp) {
        displayUserLoginModal()
            .then(function (customer, sessionInfo) {
                ASAPP('SetCustomer', {
                    CustomerId: customer,
                    ContextProvider: function (callback, tokenIsExpired) {
                        asappContextProvider(callback, tokenIsExpired, sessionInfo)
                    }
                });
            })
    } else {
        window.location.href = '/login';
    }
}
```

The next helper defines the [onLoadComplete](/agent-desk/integrations/web-sdk/web-app-settings#onloadcomplete "onLoadComplete") handler.

It is used for preparing any additional logic you wish to tie to ASAPP or your own page functionality. The below example checks whether the Chat SDK loaded via a [Trigger](/agent-desk/integrations/web-sdk/web-features#triggers "Triggers") (via the `isDisplayingChat` argument).

If it's configured to display, it prepares some event bindings through the [Action API](/agent-desk/integrations/web-sdk/web-javascript-api#action-on-or-off "action: 'on' or 'off'") which in turn call an example metrics service.

The following code snippet shows an `onLoadComplete` handler being used with the isDisplayingChat conditional and Action API.

```javascript  theme={null}
function asappOnLoadComplete (isDisplayingChat) {
    if (isDisplayingChat) {
        // Chat SDK has loaded and exists on the page
        document.body.classList.add('chat-sdk-loaded');
        var customerId = retrieveCurrentSessionOrUserId();
        ASAPP('on', 'issue:new', function (event) {
            metricService('set', 'chat:action', {
                actionName: event.type,
                customerId: customerId,
                externalCustomerId: event.detail.customerId,
                issueId: event.detail.issueId
            })
        });
        ASAPP('on', 'message:received', function (event) {
            metricService('set', 'chat:action', {
                actionName: event.type,
                customerId: customerId,
                externalCustomerId: event.detail.customerId,
                isLiveChat: event.detail.isLiveChat,
                issueId: event.detail.issueId,
                senderType: event.detail.senderType
            })
        });
    } else {
        // Chat SDK is not configured to display on this page.
        // See Display Settings: Triggers documentation
    }
}
```

Finally, we tie everything together. The example below shows a combination of adding the above helper functions to the ASAPP [Load API](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'").

It also combines many of the [App Settings](/agent-desk/integrations/web-sdk/web-app-settings "Web App Settings") available to you and your integration.

```javascript  theme={null}
document.addEventListener('DOMContentLoaded', function () {
    var customerId = retrieveCustomerIdentifier();
    ASAPP('load', {
        APIHostname: 'example-co.api.asapp.com',
        AppId: 'example-co',
        Display: {
            Align: 'left',
            AlwaysShowMinimize: true,
            BadgeColor: 'rebeccapurple',
            BadgeText: 'Chat With Us',
            BadgeType: 'tray',
            FrameDraggable: true,
            FrameStyle: 'sideBar',
            Identity: 'subsidiary-branding'
        },
        Intent: {
            Code: 'PAYBILL'
        },
        RegionCode: 'US',
        Sound: true,
        CustomerId: customerId,
        ContextProvider: asappContextProvider,
        UserLoginHandler: asappUserLoginHandler,
        onLoadComplete: asappOnLoadComplete
    });
});
```
