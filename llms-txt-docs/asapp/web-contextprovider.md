# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-contextprovider.md

# Web ContextProvider

This section details the various ways you can use the ASAPP ContextProvider with the Chat SDK API. Before using the ContextProvider, make sure you've [integrated the ASAPP SDK](/agent-desk/integrations/web-sdk/web-quick-start "Web Quick Start") script on your page.

The ASAPP `ContextProvider` is used for passing various information about your users or their sessions to the Chat SDK. It is a key that may be set in the [Load and SetCustomer](/agent-desk/integrations/web-sdk/web-javascript-api) APIs. The key must be assigned a function that will receive two arguments.

The first argument is a `callback` function. The second argument is a `needsRefresh` boolean indicating whether or not the authorization information needs to be refreshed.

The `ContextProvider` is called whenever the user types in the Chat SDK.

## 'Callback'

After you've retrieved all the context needed for a user, call the `callback` argument with your context object as the sole argument. This will pass your context object to the ASAPP Chat SDK.

## 'needsRefresh'

The `needsRefresh` argument returns a boolean value indicating whether or not your user's authorization has expired.

```javascript  theme={null}
function contextProviderHandler(callback, needsRefresh) {
    var contextObject = Object.assign(
        {},
        yourGetAnalyticsMethod(),
        yourGetSessionMethod(),
        yourGetAuthenticationMethod()
    );
    if (needsRefresh) {
        Object.assign(contextObject.Auth,
            getUpdatedAuthorization()
        );
    }
    callback(contextObject);
}
ASAPP('setCustomer', {
    CustomerId: yourGetCustomerIdMethod(),
    ContextProvider: contextProviderHandler
}
)
\
;
```

## Authentication

The `ContextProvider` plays an important role in authorizing your users with the ASAPP Chat SDK. Whether your users are always authenticated or transitioning from an anonymous to integrated use case, you must use the ContextProvider's `Auth` key to provide a user's authorization.

<Note>
  Your site is responsible for retrieving and providing all authorization information. Once provided to ASAPP, your user will be allowed secure access to any integrated use cases.
</Note>

Along with providing a [CustomerId](/agent-desk/integrations/web-sdk/web-app-settings#customerid "CustomerId"), you'll need to provide any request body with information, cookies, headers, or access tokens required for ASAPP to authorize with your systems.

You may provide this information using the `Auth` key and the following set of nested properties:

```javascript  theme={null}
function contextProviderHandler(callback, needsRefresh) {
    var contextObject = {
        // Auth key provided to the ContextProvider
        Auth: {
            Body: {
                customParam: 'value'
            },
            Cookies: {
                AuthCookie: 'authCookieValue'
            },
            Headers: {
                'X-Custom-Header': 'value'
            },
            Scopes: ['paybill'],
            Token: 'b34r3r...'
        }
    };
    callback(contextObject);
}
```

Each key within the `Auth` object is optional, but you must provide any necessary information for your authenticated users.

* The `Body`, `Cookies`, and `Headers` keys all accept an object containing any number of key:value pairs.
* The `Scopes` key accepts an array of strings defining which services may be updated with the provided token.
* The `Token` key accepts a single access token string.

Please see the [Authentication](/agent-desk/integrations/web-sdk/web-authentication "Web Authentication") section for full details on using the `ContextProvider` for authenticating your users.

## Customer Info

You may assign analytic data and add other customer information to a user's Chat SDK interactions by using the `CustomerInfo` key. The key is a child of the context object and contains a series of key:value pairs.

Your page is responsible for defining and setting the keys you would like to track. You may define and pass along as many keys as you would like.

You must discuss and agree upon the attribute names with your Implementation Manager.

**CustomerInfo:**

* Key: `CustomerInfo`
* Value Type: `Object`

The object should contain a set of key:value pairs that you wish to provide as analytics or customer information. The value of each key must be a string.

<Warning>
  **WARNING ABOUT SENSITIVE DATA**

  Do NOT send sensitive data via `CustomerInfo`, `custom_params`, or `customer_params`. For more information, [click here](/security/warning-about-customerinfo-and-sensitive-data "Warning about CustomerInfo and Sensitive Data").
</Warning>

A user does not need to be authenticated in order to provide analytics information. The following code snippet shows the `CustomerInfo` key being used to pass along analytics data.

```javascript  theme={null}
function contextProviderHandler(callback, needsRefresh) {
    var contextObject = {
        CustomerInfo: {
            // Your own key: value pairs
            category: 'payment',
            action: 'ASAPP',
            parent_page: 'Pay my Bill'
        }
    };
    // Return the callback
    callback(contextObject);
}
ASAPP('load', {
    APIHostname: '[API_HOSTNAME]',
    AppId: '[APP_ID]',
    ContextProvider: contextProviderHandler
});
```

## Session Information

The `ContextProvider` may be used for passing existing session information along to the Chat SDK. This is for connecting a user's page session with their SDK session.

You may provide two keys---`ExternalSessionId `and `ExternalSessionType`---for connecting session information. The value of each key is at your discretion.

A user does not need to be authenticated in order to provide session information.

### ExternalSessionId

* Key: `ExternalSessionId`
* Value Type: `String`
* Example Value: `'j6oAOxCWZh...'`
  Your user's unique session identifier. This information can be used for joining your session IDs with ASAPP's session IDs.

### ExternalSessionType

* Key: `ExternalSessionType`
* Value Type: `String`
* Example Value:`'visitID'`

A descriptive label of the type of identifier being passed via the `ExternalSessionId`.

## Company Subdivisions

If your company has multiple entities segmented under a single AppId, you may use the `ContextProvider` to pass the entity information along to the Chat SDK.

To do so, provide the optional `CompanySubdivision`key with a value of your subdivision's identifier. The identifier value will be determined in coordination with your ASAPP Implementation Manager.

### CompanySubdivision

* Key: `CompanySubdivision`
* Value Type: `Object`
* Example Value: `'divisionId'`

An object containing a set of key:value pairs that you wish to provide as analytics information. The value of each key must be a string.

## Segments

If your company needs to group users at a more granular level than [AppId](/agent-desk/integrations/web-sdk/web-app-settings#appid "AppId") or [CompanySubdivision](#company-subdivisions "Company Subdivisions"), you may use the `Segments` key to apply labels to your reports.

Each key you provide allows you to filter your reporting dashboard by those values.

### Segments

* Key: `Segments`
* Value Type: `Array`
* Example Value: \[`'north america'`, `'usa',``'northeast'`]

The key value must be an array containing a set of strings.
