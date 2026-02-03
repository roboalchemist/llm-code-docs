# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-app-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web App Settings

This section details the various properties you can provide to the Chat SDK.

These properties are used for various display, feature, and application settings.

Before utilizing these settings, make sure you've [integrated the ASAPP SDK](/agent-desk/integrations/web-sdk/web-quick-start "Web Quick Start") script on your page.

Once you've integrated the SDK with your site, you can use the [JavaScript API](/agent-desk/integrations/web-sdk/web-javascript-api "Web JavaScript API") for applying these settings.

The properties available to the ASAPP Chat SDK include:

* [APIHostName](#apihostname "APIHostName")
* [AppId](#appid "AppId")
* [ContextProvider](#contextprovider "ContextProvider")
* [CustomerId](#customerid "CustomerId")
* [Display](#display "Display")
* [Chat](#chat "Chat")
* [Intent](#intent "Intent")
* [Language](#language)
* [onLoadComplete](#onloadcomplete "onLoadComplete")
* [RegionCode](#regioncode "RegionCode")
* [Sound](#sound "Sound")
* [UserLoginHandler](#userloginhandler-11877 "UserLoginHandler")

Each property has three attributes:

* Key - provides the name of the property that you can set.
* Available APIs - lists the [JavaScript APIs](/agent-desk/integrations/web-sdk/web-javascript-api "Web JavaScript API") that the property is accepted on.
* Value Type - describes the primitive type of value required.

## APIHostName

* Key: `APIHostName`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `String`

Sets the ASAPP APIHostName for connecting customers with customer support.

## AppId

* Key: `AppId`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `String`

Your unique Company Identifier.

## Chat

* Key: `Chat`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load)
* Value Type: `Object`

The `Chat` setting allows you to customize the:

* [Styling](/agent-desk/integrations/web-sdk/web-customization#dynamic-styling-configuration)
* [Icons](/agent-desk/integrations/web-sdk/web-customization#custom-icons)
* [Features](/agent-desk/integrations/web-sdk/web-customization#chat-features)

## ContextProvider

* Key: `ContextProvider`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'"), ['setCustomer'](/agent-desk/integrations/web-sdk/web-javascript-api#setcustomer "'setCustomer'")
* Value Type: `Function`

The ASAPP `ContextProvider` is used for passing various information about your users to the Chat SDK. This information may include authentication, analytics, or session information. Please see the in-depth section on [Using the ContextProvider](/agent-desk/integrations/web-sdk/web-contextprovider "Web ContextProvider") for details about each of the use cases.

## CustomerId

* Key: `CustomerId`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'"), ['setCustomer'](/agent-desk/integrations/web-sdk/web-javascript-api#setcustomer "'setCustomer'")
* Value Type: `String`

The unique identifier for an authenticated customer. This value is typically a customer's login name or account ID. If setting a **`CustomerId`** you must also provide a [ContextProvider ](#contextprovider "ContextProvider")property to pass along their access token and any other required authentication properties.

## Display

* Key: `Display`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `Object`

The `Display` setting allows you to customize the presentation aspects of the Chat SDK. The setting is an object that contains each of the customization's you wish to provide.

Read on below for the currently supported keys:

```javascript  theme={null}
ASAPP('load', 
{   "APIHostname": "example-co-api.asapp.com",
    "AppId": "example-co",
    "Display": {
        "Align": "left",
        "AlwaysShowMinimize": true,
        "BadgeColor": "rebeccapurple",
        "BadgeText": "Support",
        "BadgeType": "tray",
        "FrameDraggable": true,
        "FrameStyle": "sidebar",
        "HideBadgeOnLoad": false,
        "Identity": "electronics"
    }
}
```

### Align

* Key: `Align`
* Value Type: `String`
* Accepted Values: `'left'`, `'right'` (default)

Renders the [Chat SDK Badge](/agent-desk/integrations/web-sdk/web-customization#badge "Badge") and [iframe](/agent-desk/integrations/web-sdk/web-customization#iframe "iframe") on the left or right side of your page.

### AlwaysShowMinimize

* Key: `AlwaysShowMinimize`
* Value Type: `Boolean`

Determines if the iframe minimize icon displays in the Chat SDK's header. The default `false` value displays the button only on tablet and mobile screen sizes. When set to `true`, the button will also be visible on desktop-sized screens.

### BadgeColor

* Key: `BadgeColor`
* Value Type: `String`
* Accepted Values: `Color Keyword`,`RGB hex value`

Customizes the background color of the [Chat SDK Badge](/agent-desk/integrations/web-sdk/web-customization#badge "Badge").

This will be the primary color of Proactive Messages and Channel Picker if the PrimaryColor is not provided.

### BadgeText

* Key: `BadgeText`
* Value Type: `String`

Applies a caption to the [Chat SDK Badge](/agent-desk/integrations/web-sdk/web-customization#badge "Badge").

<Note>
  This setting only works when applying the `BadgeType`:`tray`.
</Note>

### BadgeType

* Key: `BadgeType`
* Value Type: `String`
* Accepted Values: `'tray'`,`'badge'`(default) , `'none'`

`BadgeType: 'tray'`

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=258eb50768eb900f598e1334048df8fd" data-og-width="180" width="180" data-og-height="65" height="65" data-path="image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9ba570aaee7082ec63b21ce118ed8d69 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ecf1b834fd23baccc0f57231802a9b41 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3a9a30ee6fa78c83d43d5ca678bf14b1 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=bfa6f16cdc442161146f32e39e551e9b 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0b97b5eb27c416ad43bc8f8ab1b1dc69 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-97cd2bcf-644f-e074-98a0-92642e96e750.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=09afe14a647a1c2a875eaaea3676c5c9 2500w" />
</Frame>

`BadgeType: 'badge'`

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0cc21f0850b03f32d9a07610d848ad53" data-og-width="81" width="81" data-og-height="81" height="81" data-path="image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5cf6fd38b8bc2b7560c6c07f5dcd12b2 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5ac9371bfed86499488dfc31aed026f3 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=609ba37cf12b4b590097d2e4467edcca 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2f0def9ce70cdf8f50d3a64b20baeac7 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=afe66cc9b60eb63f332a1fdb14fb230a 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5aae3dc1-edc7-7cc7-b609-8ac390ab04f8.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fc72d516de7fcb0babb56022563189ea 2500w" />
</Frame>

Customizes the display of the [Chat SDK Badge](/agent-desk/integrations/web-sdk/web-customization#badge "Badge"). When you set the type to `'tray'`, you may also enter a `BadgeText` value. When you set this to 'none', the badge will not render.

### FrameDraggable

* Key: `FrameDraggable`
* Value Type: `Boolean`

Enabling this setting allows a user to reposition the placement of the [Chat SDK iframe](/agent-desk/integrations/web-sdk/web-customization#iframe "iframe").

When this is set to `true`, a user can hover over the frame's heading region, then click and drag to reposition the frame. The user's frame position will be recalled as they navigate your site or minimize/open the Chat SDK.

If the user has repositioned the frame, a button will appear allowing them to reset the Chat SDK to its default position.

### FrameStyle

* Key: `FrameStyle`
* Value Type: `String`

Accepted Values: `'sidebar'`, `'default'` (default)

Customizes the layout of the [Chat SDK iframe](/agent-desk/integrations/web-sdk/web-customization#iframe "iframe").

By default, the frame will appear as a floating window with a responsive height and width. When set to `'sidebar'`, the frame will be docked to the side of the page and take 100% of the browser's viewport height. The`'sidebar'` setting will adjust your page's content as though the user resized their browser viewport.

Use the `Align` setting if you wish to change which side of the page the frame appears on.

### HideBadgeOnLoad

* Key: `HideBadgeOnLoad`
* Value Type: `Boolean`
* Accepted Values: `'true'`,`'false'`(default)

When set to true, [Chat Badge](/agent-desk/integrations/web-sdk/web-customization#badge "Badge") is not visible on load. You can open the [Chat SDK iframe](/agent-desk/integrations/web-sdk/web-customization#iframe "iframe") via Proactive Message, [Chat Instead](../chat-instead/web "Web"), or [Show API](/agent-desk/integrations/web-sdk/web-javascript-api#show "'show'").

Once you open the Chat SDK iframe, Chat Badge will become visible allowing a user to minimize/reopen.

### Identity

* Key: `Identity`
* Value Type: `String`

A string that represents the branding you wish to display on the SDK. Your ASAPP Implementation Manager will help you determine this value.

If set to a non-supported value the Chat SDK will display in a generic, non-branded experience.

### PrimaryColor

* Key: `PrimaryColor`
* Value Type: `String`
* Accepted Values: `Color Keyword`,`RGB hex value`

Customizes the primary color of Proactive Messages and [Chat Instead](/agent-desk/integrations/chat-instead/web "Web").

This will be the background color of the [Chat SDK Badge](/agent-desk/integrations/web-sdk/web-customization#badge "Badge") if the BadgeColor is not provided.

## Intent

* Key: `Intent`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#-load- "'load'")
* Value Type: `String`

The intent code that you wish for a user's conversation to initialize with. The setting takes an object, with a required key of `Code`. `Code` accepts a string.

Your team and your ASAPP Implementation Manager will determine the available values.

```javascript  theme={null}
ASAPP('load', {
    APIHostname: 'example-co-api.asapp.com',
    AppId: 'example-co',
    Intent: {
        Code: 'PAYBILL'
    }
});
```

## Language

* Key: `Language`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `String`

By Default, the SDK will use English (`en`). You can override this by setting the `Language` property. It accepts a value of:

* `en` for English
* `fr` for French
* `es` for Spanish

ASAPP does not support switching languages mid-session, after a conversation has started. You must set a language before starting a conversation.

<CodeGroup>
  ```javascript English theme={null}
  ASAPP('load', {
      APIHostname: 'example-co-api.asapp.com',
      AppId: 'example-co',
      Language: 'en'
  });
  ```

  ```javascript French theme={null}
  ASAPP('load', {
      APIHostname: 'example-co-api.asapp.com',
      AppId: 'example-co',
      Language: 'fr'
  });
  ```
</CodeGroup>

## onLoadComplete

* Key: `onLoadComplete`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `Function`

A callback that is triggered once the Chat SDK has finished initializing. This is useful when attaching events via the [Action API](/agent-desk/integrations/web-sdk/web-javascript-api#action-on-or-off "action: 'on' or 'off'") or whenever you need to perform custom actions to the SDK after it has loaded.

The provided method receives a single argument as a boolean value. If the value is `false`, then the page is not configured to display under the [ASAPP Trigger feature](/agent-desk/integrations/web-sdk/web-features#triggers "Triggers"). If the value is `true`, then the Chat SDK has loaded and finished appending to your DOM.

```
ASAPP('load', {
    APIHostname: 'example-co-api.asapp.com',
    AppId: 'example-co',
    onLoadComplete: function (isDisplayingChat) {
        console.log('ASAPP Loaded');
        if (isDisplayingChat) {
            ASAPP('on', 'message:received', handleMessageReceivedEvent);
        } else {
            console.log('ASAPP not enabled on this page');
        }
    }
});
```

## RegionCode

* Key: `RegionCode`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `String`

Localizes the Chat SDK with a certain region. It accepts a value from the [ISO 3166 alpha-2 country codes](https://www.iso.org/obp/ui/#home) representing the country you wish to localize.

## Sound

* Key: `Sound`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `Boolean`

When set to `true`, users will receive an audio notification when they receive a message in the chat log. This defaults to `false`.

## UserLoginHandler

* Key: `UserLoginHandler`
* Available APIs: [Load](/agent-desk/integrations/web-sdk/web-javascript-api#load "'load'")
* Value Type: `Function`

The `UserLoginHandler` allows you to provide a means of authentication so a user may access account information via the ASAPP Chat SDK. When the Chat SDK determines that a user is unauthorized, a "Log In" button appears. When the user clicks that button, the Chat SDK will call the method you provided. See the [Authentication](/agent-desk/integrations/web-sdk/web-authentication "Web Authentication") page for options on how you can authenticate your customers. Note: If you do not provide a `UserLoginHandler`, a user will not be able to transition from an anonymous to an authorized session.

When the Chat SDK calls the `UserLoginHandler`, it provides a single argument.

The argument is an object and contains various session information that may be useful to your integration. You and your Implementation Manager determine the information provided.

It may contain things such as [CompanySubdivision](/agent-desk/integrations/web-sdk/web-contextprovider#company-subdivisions "Company Subdivisions"), [ExternalSessioninformation](/agent-desk/integrations/web-sdk/web-contextprovider#session-information "Session Information"), and more.

```javascript  theme={null}
ASAPP('load', {
    APIHostname: 'example-co-api.asapp.com',
    AppId: 'example-co',
    UserLoginHandler: function (data) {
        if (data.CompanySubdivision === 'chocolatiers') {
            // Synchronous login
            window.open('/login?makers=tempering')
        } else {
            // Get Customer Id and access_token ...
            var CustomerId = 'Retrieved customer ID';
            var access_token = 'Retrieved access token';
            // Call SetCustomer with retrieved access_token, CustomerId, and ContextProvider
            ASAPP('setCustomer', {
                CustomerId: CustomerId,
                ContextProvider: function (callback) {
                    var context = {
                        Auth: {
                            Token: access_token
                        }
                    };
                    callback(context);
                }
            });
        }
    }
});
```
