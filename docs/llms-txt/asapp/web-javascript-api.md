# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-javascript-api.md

# Web JavaScript API

This section details the various API methods you can call to the ASAPP Chat SDK.

Before making any API calls, make sure you've [integrated the ASAPP SDK](/agent-desk/integrations/web-sdk/web-quick-start "Web Quick Start") script on your page.

Once you've integrated the SDK with your site, you can use the JavaScript API to toggle settings in the Chat SDK, trigger events, or send information to ASAPP.

The Chat SDK Web JavaScript API allows you to perform a variety of actions after the SDK has been initialized, such as the [`load`](#setCustomer) method if you are authorization a user after a conversation has started, or updating the customers info mid conversation with the [`setCustomer`](#setcustomer) method.

Read on for details on each of these methods:

* [action: `on` or `off`](#action-on-or-off)
* [`getState`](#getstate)
* [`hide`](#hide)
* [`load`](#load)
* [`refresh`](#refresh)
* [`send`](#send)
* [`set`](#set)
* [`setCustomer`](#setcustomer)
* [`setIntent`](#setintent)
* [`show`](#show)
* [`showChatInstead`](#showchatinstead)
* [`unload`](#unload)
* [`unloadAndClearSession`](#unloadandclearsession)

## action: `on` or `off`

This API subscribes or unsubscribes to events that occur within the Chat SDK. A developer can apply custom behavior, track metrics, and more by subscribing to one of the Chat SDK custom events. To utilize the Action API, pass either the `on` (subscribes) or `off` (unsubscribes) keywords to the `ASAPP` method. The next argument is the name of the event binding.

The final argument is the callback handler you wish to attach. The following code snippet is an example of the Action API subscribing and unsubscribing to the `agent:assigned` and `message:received` events:

```javascript  theme={null}
function agentAssignedHandler (event) {
    onAgentAssigned(event.detail.issueId, event.detail.externalSenderId);
}
function messageHandler (event) {
    const { isFirstMessage, externalSenderId } = event.detail;
    if (isFirstMessage && externalSenderId) {
        OnAgentInteractive(event.detail.issueId, event.detail.customerId);
    } else if (isFirstMessage === false && isFromRep) {
        ASAPP('off', 'message:received', messageHandler);
    }
}
ASAPP('load', {
    onLoadComplete: () => {
        ASAPP('on', 'agent:assigned', agentAssignedHandler);
        ASAPP('on', 'message:received', messageHandler);
    }
});
```

### Event Object

Each event receives a `CustomEvent` object as the first argument to your event handler. This is a [standard event object](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent) with all typical interfaces. The object has an `event.type` with the name of the event and an `event.detail` key which contains the following custom properties:

`issueId` (Number)

The ASAPP identifier for an individual issue. This ID may change as a user completes and starts new queries to the ASAPP system.

`customerId` (Number)

The ASAPP identifier for a customer. This ID is consistent for authenticated users but may be different for anonymous ones. Anonymous users will have a consistent ID for the duration of their session.

`externalSenderId` (String)

The external identifier you provide to ASAPP that represents an agent identifier. This property will be undefined if the user is not connected with an agent.

### Chat Events

Chat events trigger when a user opens or closes the Chat SDK window. These events do not have any additional event details.

`chat:show`

* Cancellable: true

This event triggers when a user opens the Chat SDK. It may fire multiple times per session if a user repeatedly closes and opens the chat.

`chat:hide`

* Cancellable: true

This event triggers when a user closes the Chat SDK. It may fire multiple times per session if a user repeatedly opens and closes the chat.

### Issue Events

Issue events occur when a change in state of an Issue occurs within the ASAPP system. These events do not have any additional event details.

`issue:new`

* Cancellable: false

This event triggers when a user has opened a new issue. It fires when they first open the Chat SDK or if they complete an issue and start another one.

`issue:end`

* Cancellable: false

This event triggers when a user or agent has ended an issue. It fires when the user has completed an automated support request or when a user/agent ends an active chat.

### Agent Events

Agent events occur when particular actions occur with an agent within ASAPP's system. These events do not have any additional event details.

`agent:assigned`

* Cancellable: false

This event triggers when a user is connected to an agent for the first time. It fires once the user has left an automated support flow and has been connected to a live support agent.

### Message Events

Message events occur when the user receives a message from either SRS or an agent. These events have the following additional event details:

`senderType` (String)

Returns either `srs` or `agent`.

`isLiveChat` (Boolean)

Returns `true` when a user is connected with an agent. Returns `false` when a user is within an automated flow.

`isFirstMessage` (Boolean)

Returns `true` only when a message is the first message received from an agent or SRS. Otherwise returns `false`.

`message:received`

* Cancellable: false

This event triggers whenever the Chat SDK receives a message event to the chat log. It will fire when a user receives a message from SRS or an agent.

## getState

This API returns the current state of Chat SDK session. It accepts a callback which receives the current state object.

```javascript  theme={null}
ASAPP('getState', function(state) {
    console.log(state);
});
```

### State Object

The state object contains the following keys which give you insight into the user's actions:

`hasContext` (Object)

Returns the current [context](/agent-desk/integrations/web-sdk/web-contextprovider "Web ContextProvider") known by the SDK.

`hasCustomerId` (Boolean)

Returns true when the SDK has been provided with a [CustomerId](/agent-desk/integrations/web-sdk/web-app-settings#customerid "CustomerId") setting.

`isFullscreen` (Boolean)

Returns true when the SDK will render in fullscreen for mobile web devices.

`isLiveChat` (Boolean)

Returns true when the use is connected to an agent.

`isLoggingIn` (Boolean)

Returns true if the user has been presented with and clicked on a button to Log In.

`isMobile`(Boolean)

Returns true when the SDK is rendering on a mobile or tablet device.

`isOpen` (Boolean)

Returns true if the user has the SDK open on the current or had it open on the previous page.

`unreadMessages` (Integer)

Returns a count of how many messages the user has received since minimizing the SDK.

## hide

This API hides the Chat SDK iframe. See [Show](#-show- "'show'") for revealing the Chat SDK iframe. This method is useful for when you want to close the SDK iframe after certain page interactions or if you've provided a custom Badge entry point.

```javascript  theme={null}
ASAPP('hide');
```

## load

This API initializes the ASAPP Chat SDK for display on your pages and typically specify a [`contextProviderHandler`](/agent-desk/integrations/web-sdk/web-contextprovider).

To call the `load` the API and initialize the SDK, specify any of the [Web App Settings](/agent-desk/integrations/web-sdk/web-app-settings), though the following are required:

* [APIHostname](/agent-desk/integrations/web-sdk/web-app-settings#apihostname): The Hostname for connection customers with customer support.
* [AppId](/agent-desk/integrations/web-sdk/web-app-settings#appid "AppId"): Your unique Company Identifier (or company marker).

Work with your ASAPP Account Team to determine the correct values for these settings.

Typically, you'll also specify a [`ContextProvider` handler](/agent-desk/integrations/web-sdk/web-contextprovider) to provide context to the SDK such as user authentication information or other customer information.

```javascript Load with CustomerInfo And Authentication Token theme={null}
ASAPP('load', {
    APIHostname: '[API_HOSTNAME]',
    AppId: '[APP_ID]',
    ContextProvider: (callback) => {
        const context = {
            CustomerInfo: {
                category: 'payment',
                parent_page: 'Pay my Bill'
            },
            Auth: {
                Token: '[AUTH_TOKEN]'
            }
        };
        callback(context);
    }
});
```

Please see the [Web App Settings](/agent-desk/integrations/web-sdk/web-app-settings) page for a list of all the available properties that can be passed to the `Load` API.

## refresh

This API checks to make sure that [Triggers](/agent-desk/integrations/web-sdk/web-features#triggers) work properly when a page URL changes in a SPA (Single-Page Application). You should call this API every time the page URL changes if your website is a SPA.

```javascript  theme={null}
ASAPP('refresh')
```

## send

Use this API to update the `customerInfo` object at any time, regardless of whether the user is currently typing in the Chat SDK.

Typically, the `customerInfo` is updated as part of your [`contextProviderHandler`](/agent-desk/integrations/web-sdk/web-app-settings#contextprovider) function defined in your [`load`](#'load') call, which is called whenever the user types in the Chat SDK.

This API is primarily used to send information that is used to show a proactive chat prompt when a specific criteria or set of criteria are met. The `send` API is rate limited to one request for every 5 seconds.

To use this API:

* Specify a `type` of `customer`
  <Note>
    Only the `customer` event type is supported.
  </Note>
* Provide a `data` object containing the `customerInfo` object:

```javascript  theme={null}
ASAPP('send', {
    type: 'customer',
    data: {
        "key1": "value1",
        "key2": "value2"
    }
});
```

For example, you could use a key within `CustomerInfo` to indicate that a customer had abandoned their shopping cart. Do not use the send API for transmitting any information that you would consider sensitive or Personally Identifiable Information (PII). The accepted keys are listed below.

## set

This API applies various user information to the Chat SDK. Calling this API does not make a network request. The API accepts two arguments. The first is the name of the key you want to update. The second is the value that you wish to assign the key.

```javascript  theme={null}
ASAPP('set', 'Auth', { Token: '3858f62230ac3c915f300c664312c63f' });
ASAPP('set', 'ExternalSessionId', 'j6oAOxCWZh...');
```

Please see the [Context Provider](/agent-desk/integrations/web-sdk/web-contextprovider "Web ContextProvider") page for a list of all the properties you can provide to this API.

## setCustomer

This API provides an access token with your customers account after the Chat SDK has already loaded. This method is useful if a customer logs into their account or if you need to refresh your customers auth token from time to time. See the [SDK Settings](/agent-desk/integrations/web-sdk/web-app-settings "Web App Settings") section for details on the [CustomerId](/agent-desk/integrations/web-sdk/web-app-settings#customerid "CustomerId") (Required), [ContextProvider](/agent-desk/integrations/web-sdk/web-app-settings#contextprovider "ContextProvider") (Required), and [UserLoginHandler](/agent-desk/integrations/web-sdk/web-app-settings#userloginhandler "UserLoginHandler") properties accepted for SetCustomers second argument.

```javascript  theme={null}
ASAPP('setCustomer', {
    CustomerId: 'a1b2c3x8y9z0',
    ContextProvider: function (callback) {
        var context = {
            Auth: {
                Token: '3858f62230ac3c915f300c664312c63f'
            }
        };
        callback(context);
    }
});
```

## setIntent

This API lets you set an intent after Chat SDK has already been loaded and will take effect even if the user is in chat. ASAPP recommends that you use [Intent](/agent-desk/integrations/web-sdk/web-app-settings#intent "Intent") via App Settings during load.

This method takes an object as a parameter, with a required key of `Code`. `Code` accepts a string. Your team and your ASAPP Implementation Manager will determine the available values.

```javascript  theme={null}
ASAPP('setIntent', {Code: 'PAYBILL'});
```

## show

This API shows the Chat SDK iframe. See [Hide](#-hide- "'hide'") for hiding the Chat SDK iframe. This method is useful for when you want to open the SDK iframe after certain page interactions or if you've provided a custom Badge entry point.

```javascript  theme={null}
ASAPP('show');
```

## showChatInstead

This API displays the [Chat Instead](../chat-instead/web "Web") feature.

This API displays the Chat Instead feature.

In order to enable this feature, please integrate with the `showChatInstead` API and then contact your Implementation Manager.

**Options:**

<table class="informaltable frame-void rules-rows">
  <thead>
    <tr>
      <th class="th"><p>Key</p></th>
      <th class="th"><p>Description</p></th>
      <th class="th"><p>Required</p></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="td"><p><code class="code">phoneNumber</code></p></td>
      <td class="td"><p>Phone number used when a user clicks phone in Chat Instead.</p></td>
      <td class="td"><p>Yes</p></td>
    </tr>

    <tr>
      <td class="td"><p><a class="link linktype-component" href="/agent-desk/integrations/web-sdk/web-app-settings.html#apihostname" title="APIHostName"><code class="code">APIHostName</code></a></p></td>
      <td class="td"><p>Sets the ASAPP APIHostName for connecting customers with customer support.</p></td>

      <td class="td" rowspan="2">
        <p>No</p>
        <p>(Required if you have not initialized the WebSDK via the <a class="link linktype-component" href="/agent-desk/integrations/web-sdk/web-javascript-api.html#-load-" title="'load'"><code class="code">Load</code></a> API on the page)</p>
      </td>
    </tr>

    <tr>
      <td class="td"><p><a class="link linktype-component" href="/agent-desk/integrations/web-sdk/web-app-settings.html#appid" title="AppId"><code class="code">AppId</code></a></p></td>
      <td class="td"><p>Your unique Company Identifier.</p></td>
    </tr>
  </tbody>
</table>

**Example Use Case:**

```html  theme={null}
<a href="tel:8001234567" onclick="ASAPP('showChatInstead', {'phoneNumber': '(800) 123-4567'})">(800) 123-4567</a>
```

## unload

This API removes all the SDK related elements from the DOM (Badge, iframe, and Proactive Messages if any). If the SDK is already open or a user is in live chat, ASAPP will ignore this call. To reload the SDK, you need to call the "Load" API.

```javascript  theme={null}
ASAPP('unload')
```

## unloadAndClearSession

This API removes all SDK instances from the browser and clears the session details. This method is specifically designed to be called during user logout to ensure complete session cleanup and allow users to reinstantiate the chat with a completely new session.

This API will:

* Remove chat instances from the browser
* Clear all session details and stored data
* Allow reinstantiation of chat with a fresh session
* Ensure proper session cleanup for user privacy

Unlike the `unload` API, this method performs a complete cleanup of all session-related data, making it ideal for logout scenarios where you want to ensure no user data persists.

```javascript  theme={null}
ASAPP('unloadAndClearSession')
```

**Usage Example:**

```javascript  theme={null}
// Call this method when user logs out
function handleUserLogout() {
    // Perform other logout operations
    performLogout();
    
    // Clear ASAPP chat session
    ASAPP('unloadAndClearSession');
}
```

<Note>
  It's recommended to call `unloadAndClearSession` as part of your application's logout process to ensure proper session cleanup and user privacy. After calling this API, you will need to call the `load` API again to reinitialize the chat SDK.
</Note>
