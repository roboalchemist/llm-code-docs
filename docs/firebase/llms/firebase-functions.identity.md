# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md.txt

# identity namespace

## Functions

|                                                                                    Function                                                                                    |                              Description                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [beforeEmailSent(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeemailsent)                           | Handles an event that is triggered before an email is sent to a user. |
| [beforeEmailSent(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeemailsent)                     | Handles an event that is triggered before an email is sent to a user. |
| [beforeOperation(eventType, optsOrHandler, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeoperation) |                                                                       |
| [beforeSmsSent(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforesmssent)                               | Handles an event that is triggered before an SMS is sent to a user.   |
| [beforeSmsSent(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforesmssent)                         | Handles an event that is triggered before an SMS is sent to a user.   |
| [beforeUserCreated(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeusercreated)                       | Handles an event that is triggered before a user is created.          |
| [beforeUserCreated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeusercreated)                 | Handles an event that is triggered before a user is created.          |
| [beforeUserSignedIn(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeusersignedin)                     | Handles an event that is triggered before a user is signed in.        |
| [beforeUserSignedIn(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitybeforeusersignedin)               | Handles an event that is triggered before a user is signed in.        |
| [getOpts(blockingOptions)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.md#identitygetopts)                                   |                                                                       |

## Classes

|                                                                       Class                                                                        |                                                 Description                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [HttpsError](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md#identityhttpserror_class) | An explicit error that can be thrown from a handler to send an error to the client that called the function. |

## Interfaces

|                                                                                  Interface                                                                                  |                                  Description                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface) | Defines the auth event for 2nd gen blocking events                             |
| [AuthUserRecord](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecord_interface)          | The `UserRecord` passed to auth blocking functions from the identity platform. |
| [BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface)       | All function options plus idToken, accessToken, and refreshToken.              |

## identity.beforeEmailSent()

Handles an event that is triggered before an email is sent to a user.

**Signature:**  

    export declare function beforeEmailSent(handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeEmailResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                                Type                                                                                                                |                         Description                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeEmailResponse \| void\> | Event handler that is run before an email is sent to a user. |

**Returns:**

BlockingFunction

## identity.beforeEmailSent()

Handles an event that is triggered before an email is sent to a user.

**Signature:**  

    export declare function beforeEmailSent(opts: Omit<BlockingOptions, "idToken" | "accessToken" | "refreshToken">, handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeEmailResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                                Type                                                                                                                |                         Description                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| opts      | Omit\<[BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface), "idToken" \| "accessToken" \| "refreshToken"\>        | Object containing function options.                          |
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeEmailResponse \| void\> | Event handler that is run before an email is sent to a user. |

**Returns:**

BlockingFunction

## identity.beforeOperation()

**Signature:**  

    export declare function beforeOperation(eventType: AuthBlockingEventType, optsOrHandler: BlockingOptions | ((event: AuthBlockingEvent) => MaybeAsync<BeforeCreateResponse | BeforeSignInResponse | BeforeEmailResponse | BeforeSmsResponse | void>), handler: HandlerV2): BlockingFunction;

### Parameters

|   Parameter   |                                                                                                                                                                                                                                        Type                                                                                                                                                                                                                                        | Description |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| eventType     | AuthBlockingEventType                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |
| optsOrHandler | [BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface) \| ((event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeCreateResponse \| BeforeSignInResponse \| BeforeEmailResponse \| BeforeSmsResponse \| void\>) |             |
| handler       | HandlerV2                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |

**Returns:**

BlockingFunction

## identity.beforeSmsSent()

Handles an event that is triggered before an SMS is sent to a user.

**Signature:**  

    export declare function beforeSmsSent(handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeSmsResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                               Type                                                                                                               |                        Description                         |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeSmsResponse \| void\> | Event handler that is run before an SMS is sent to a user. |

**Returns:**

BlockingFunction

## identity.beforeSmsSent()

Handles an event that is triggered before an SMS is sent to a user.

**Signature:**  

    export declare function beforeSmsSent(opts: Omit<BlockingOptions, "idToken" | "accessToken" | "refreshToken">, handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeSmsResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                               Type                                                                                                               |                        Description                         |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| opts      | Omit\<[BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface), "idToken" \| "accessToken" \| "refreshToken"\>      | Object containing function options.                        |
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeSmsResponse \| void\> | Event handler that is run before an SMS is sent to a user. |

**Returns:**

BlockingFunction

## identity.beforeUserCreated()

Handles an event that is triggered before a user is created.

**Signature:**  

    export declare function beforeUserCreated(handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeCreateResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                                Type                                                                                                                 |                           Description                           |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeCreateResponse \| void\> | Event handler which is run every time before a user is created. |

**Returns:**

BlockingFunction

## identity.beforeUserCreated()

Handles an event that is triggered before a user is created.

**Signature:**  

    export declare function beforeUserCreated(opts: BlockingOptions, handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeCreateResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                                Type                                                                                                                 |                           Description                           |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| opts      | [BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface)                                                               | Object containing function options.                             |
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeCreateResponse \| void\> | Event handler which is run every time before a user is created. |

**Returns:**

BlockingFunction

## identity.beforeUserSignedIn()

Handles an event that is triggered before a user is signed in.

**Signature:**  

    export declare function beforeUserSignedIn(handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeSignInResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                                Type                                                                                                                 |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeSignInResponse \| void\> | Event handler which is run every time before a user is signed in. |

**Returns:**

BlockingFunction

## identity.beforeUserSignedIn()

Handles an event that is triggered before a user is signed in.

**Signature:**  

    export declare function beforeUserSignedIn(opts: BlockingOptions, handler: (event: AuthBlockingEvent) => MaybeAsync<BeforeSignInResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                                                                                                Type                                                                                                                 |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface)                                                               | Object containing function options.                               |
| handler   | (event: [AuthBlockingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingevent_interface)) =\> MaybeAsync\<BeforeSignInResponse \| void\> | Event handler which is run every time before a user is signed in. |

**Returns:**

BlockingFunction

## identity.getOpts()

**Signature:**  

    export declare function getOpts(blockingOptions: BlockingOptions): InternalOptions;

### Parameters

|    Parameter    |                                                                                 Type                                                                                  | Description |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| blockingOptions | [BlockingOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptions_interface) |             |

**Returns:**

InternalOptions