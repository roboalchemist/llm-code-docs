Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/classes/ClearStateStore

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / ClearStateStore

# Class: ClearStateStore

Defined in: [packages/oauth/src/state-stores/clear-state-store.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/clear-state-store.ts#L8)

Generates state parameter value in the OAuth flow. While the state parameter value works for the CSRF protection purpose, it can transfer the given InstallURLOptions value to the Redirect URL handler (Redirect URL: the default path is "/slack/oauth\_redirect")

## Implements {#implements}

* [`StateStore`](/tools/node-slack-sdk/reference/oauth/interfaces/StateStore)

## Constructors {#constructors}

### Constructor {#constructor}

```text
new ClearStateStore(stateSecret, stateExpirationSeconds?): ClearStateStore;
```

Defined in: [packages/oauth/src/state-stores/clear-state-store.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/clear-state-store.ts#L13)

#### Parameters {#parameters}

##### stateSecret {#statesecret}

`string`

##### stateExpirationSeconds? {#stateexpirationseconds}

`number` = `600`

#### Returns {#returns}

`ClearStateStore`

## Methods {#methods}

### generateStateParam() {#generatestateparam}

```text
generateStateParam(installOptions, now): Promise<string>;
```

Defined in: [packages/oauth/src/state-stores/clear-state-store.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/clear-state-store.ts#L18)

Generates a valid state parameter value, which can be decoded as a StateObj object by the verifyStateParam() method. This value may be stored on the server-side with expiration. The InstallProvider verifies if this value is set in the installer's browser session.

#### Parameters {#parameters-1}

##### installOptions {#installoptions}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### now {#now}

`Date`

#### Returns {#returns-1}

`Promise`<`string`\>

#### Implementation of {#implementation-of}

[`StateStore`](/tools/node-slack-sdk/reference/oauth/interfaces/StateStore).[`generateStateParam`](/tools/node-slack-sdk/reference/oauth/interfaces/StateStore#generatestateparam)

* * *

### verifyStateParam() {#verifystateparam}

```text
verifyStateParam(now, state): Promise<InstallURLOptions>;
```

Defined in: [packages/oauth/src/state-stores/clear-state-store.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/clear-state-store.ts#L27)

Verifies the given state string value by trying to decode the value and build the passed InstallURLOptions object from the data. This method verifies if the state value is not too old to detect replay attacks. If the value is invalid, this method can throw InvalidStateError exception.

#### Parameters {#parameters-2}

##### now {#now-1}

`Date`

##### state {#state}

`string`

#### Returns {#returns-2}

`Promise`<[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)\>

#### Implementation of {#implementation-of-1}

[`StateStore`](/tools/node-slack-sdk/reference/oauth/interfaces/StateStore).[`verifyStateParam`](/tools/node-slack-sdk/reference/oauth/interfaces/StateStore#verifystateparam)
