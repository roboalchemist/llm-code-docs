Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/CallbackOptions

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / CallbackOptions

# Interface: CallbackOptions

Defined in: [packages/oauth/src/callback-options.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L7)

## Properties {#properties}

### afterInstallation()? {#afterinstallation}

```text
optional afterInstallation: (installation, options, callbackReq, callbackRes) => Promise<boolean>;
```

Defined in: [packages/oauth/src/callback-options.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L33)

An additional logic to run right after executing the Slack app installation with the given OAuth code parameter.

When this method returns false, the InstallProvider skips storing the installation in database. You can set false when your app needs to cancel the installation (you can call auth.revoke API method for it) and then, the app needs to display an error page to the installing user.

Also, when returning false, this method is responsible to call callbackRes#end() method to build complete HTTP response for end-users.

#### Parameters {#parameters}

##### installation {#installation}

[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)<`"v1"` | `"v2"`, `boolean`\> | [`OrgInstallation`](/tools/node-slack-sdk/reference/oauth/type-aliases/OrgInstallation)

##### options {#options}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### callbackReq {#callbackreq}

`IncomingMessage`

##### callbackRes {#callbackres}

`ServerResponse`

#### Returns {#returns}

`Promise`<`boolean`\>

* * *

### beforeInstallation()? {#beforeinstallation}

```text
optional beforeInstallation: (options, callbackReq, callbackRes) => Promise<boolean>;
```

Defined in: [packages/oauth/src/callback-options.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L17)

An additional logic to run right before executing the Slack app installation with the given OAuth code parameter.

When this method returns false, the InstallProvider skips the installation. You can set false when the visiting user is not eligible to proceed with the Slack app installation flow.

Also, when returning false, this method is responsible for calling the callbackRes#end() method to build a complete HTTP response for end-users.

#### Parameters {#parameters-1}

##### options {#options-1}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### callbackReq {#callbackreq-1}

`IncomingMessage`

##### callbackRes {#callbackres-1}

`ServerResponse`

#### Returns {#returns-1}

`Promise`<`boolean`\>

* * *

### failure()? {#failure}

```text
optional failure: (error, options, callbackReq, callbackRes) => void;
```

Defined in: [packages/oauth/src/callback-options.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L63)

#### Parameters {#parameters-2}

##### error {#error}

[`CodedError`](/tools/node-slack-sdk/reference/oauth/interfaces/CodedError)

##### options {#options-2}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### callbackReq {#callbackreq-2}

`IncomingMessage`

##### callbackRes {#callbackres-2}

`ServerResponse`

#### Returns {#returns-2}

`void`

* * *

### failureAsync()? {#failureasync}

```text
optional failureAsync: (error, options, callbackReq, callbackRes) => Promise<void>;
```

Defined in: [packages/oauth/src/callback-options.ts:72](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L72)

#### Parameters {#parameters-3}

##### error {#error-1}

[`CodedError`](/tools/node-slack-sdk/reference/oauth/interfaces/CodedError)

##### options {#options-3}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### callbackReq {#callbackreq-3}

`IncomingMessage`

##### callbackRes {#callbackres-3}

`ServerResponse`

#### Returns {#returns-3}

`Promise`<`void`\>

* * *

### success()? {#success}

```text
optional success: (installation, options, callbackReq, callbackRes) => void;
```

Defined in: [packages/oauth/src/callback-options.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L43)

#### Parameters {#parameters-4}

##### installation {#installation-1}

[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)<`"v1"` | `"v2"`, `boolean`\> | [`OrgInstallation`](/tools/node-slack-sdk/reference/oauth/type-aliases/OrgInstallation)

##### options {#options-4}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### callbackReq {#callbackreq-4}

`IncomingMessage`

##### callbackRes {#callbackres-4}

`ServerResponse`

#### Returns {#returns-4}

`void`

* * *

### successAsync()? {#successasync}

```text
optional successAsync: (installation, options, callbackReq, callbackRes) => Promise<void>;
```

Defined in: [packages/oauth/src/callback-options.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/callback-options.ts#L52)

#### Parameters {#parameters-5}

##### installation {#installation-2}

[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)<`"v1"` | `"v2"`, `boolean`\> | [`OrgInstallation`](/tools/node-slack-sdk/reference/oauth/type-aliases/OrgInstallation)

##### options {#options-5}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### callbackReq {#callbackreq-5}

`IncomingMessage`

##### callbackRes {#callbackres-5}

`ServerResponse`

#### Returns {#returns-5}

`Promise`<`void`\>
