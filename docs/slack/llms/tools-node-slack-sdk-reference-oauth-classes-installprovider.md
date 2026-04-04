Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/classes/InstallProvider

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / InstallProvider

# Class: InstallProvider

Defined in: [packages/oauth/src/install-provider.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L32)

InstallProvider Class. Refer to InsallProviderOptions interface for the details of constructor arguments.

## Constructors {#constructors}

### Constructor {#constructor}

```text
new InstallProvider(__namedParameters): InstallProvider;
```

Defined in: [packages/oauth/src/install-provider.ts:87](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L87)

#### Parameters {#parameters}

##### __namedParameters {#__namedparameters}

[`InstallProviderOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallProviderOptions)

#### Returns {#returns}

`InstallProvider`

## Properties {#properties}

### installationStore {#installationstore}

```text
installationStore: InstallationStore;
```

Defined in: [packages/oauth/src/install-provider.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L38)

* * *

### stateStore? {#statestore}

```text
optional stateStore: StateStore;
```

Defined in: [packages/oauth/src/install-provider.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L35)

## Methods {#methods}

### authorize() {#authorize}

```text
authorize(source): Promise<AuthorizeResult>;
```

Defined in: [packages/oauth/src/install-provider.ts:177](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L177)

Fetches data from the installationStore

#### Parameters {#parameters-1}

##### source {#source}

[`InstallationQuery`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationQuery)<`boolean`\>

#### Returns {#returns-1}

`Promise`<[`AuthorizeResult`](/tools/node-slack-sdk/reference/oauth/interfaces/AuthorizeResult)\>

* * *

### generateInstallUrl() {#generateinstallurl}

```text
generateInstallUrl(   options,    stateVerification?, state?): Promise<string>;
```

Defined in: [packages/oauth/src/install-provider.ts:415](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L415)

Returns a URL that is suitable for including in an Add to Slack button Uses stateStore to generate a value for the state query param.

#### Parameters {#parameters-2}

##### options {#options}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### stateVerification? {#stateverification}

`boolean` = `true`

##### state? {#state}

`string`

#### Returns {#returns-2}

`Promise`<`string`\>

* * *

### handleCallback() {#handlecallback}

```text
handleCallback(   req,    res,    options?, installOptions?): Promise<void>;
```

Defined in: [packages/oauth/src/install-provider.ts:485](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L485)

This method handles the incoming request to the callback URL. It can be used as a RequestListener in almost any HTTP server framework.

Verifies the state using the stateStore, exchanges the grant in the query params for an access token, and stores token and associated data in the installationStore.

#### Parameters {#parameters-3}

##### req {#req}

`IncomingMessage`

##### res {#res}

`ServerResponse`

##### options? {#options-1}

[`CallbackOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/CallbackOptions)

##### installOptions? {#installoptions}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

#### Returns {#returns-3}

`Promise`<`void`\>

* * *

### handleInstallPath() {#handleinstallpath}

```text
handleInstallPath(   req,    res,    options?, installOptions?): Promise<void>;
```

Defined in: [packages/oauth/src/install-provider.ts:330](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L330)

Handles the install path (the default is /slack/install) requests from an app installer.

#### Parameters {#parameters-4}

##### req {#req-1}

`IncomingMessage`

##### res {#res-1}

`ServerResponse`

##### options? {#options-2}

[`InstallPathOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallPathOptions)

##### installOptions? {#installoptions-1}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

#### Returns {#returns-4}

`Promise`<`void`\>
