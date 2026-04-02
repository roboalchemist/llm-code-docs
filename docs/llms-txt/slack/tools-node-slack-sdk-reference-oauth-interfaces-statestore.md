Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/StateStore

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / StateStore

# Interface: StateStore

Defined in: [packages/oauth/src/state-stores/interface.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L25)

Generates state parameter value in the OAuth flow. While the state parameter value works for the CSRF protection purpose, it can transfer the given InstallURLOptions value to the Redirect URL handler (Redirect URL: the default path is "/slack/oauth\_redirect")

## Properties {#properties}

### generateStateParam() {#generatestateparam}

```text
generateStateParam: (installOptions, now) => Promise<string>;
```

Defined in: [packages/oauth/src/state-stores/interface.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L31)

Generates a valid state parameter value, which can be decoded as a StateObj object by the verifyStateParam() method. This value may be stored on the server-side with expiration. The InstallProvider verifies if this value is set in the installer's browser session.

#### Parameters {#parameters}

##### installOptions {#installoptions}

[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)

##### now {#now}

`Date`

#### Returns {#returns}

`Promise`<`string`\>

* * *

### verifyStateParam() {#verifystateparam}

```text
verifyStateParam: (now, state) => Promise<InstallURLOptions>;
```

Defined in: [packages/oauth/src/state-stores/interface.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L39)

Verifies the given state string value by trying to decode the value and build the passed InstallURLOptions object from the data. This method verifies if the state value is not too old to detect replay attacks. If the value is invalid, this method can throw InvalidStateError exception.

#### Parameters {#parameters-1}

##### now {#now-1}

`Date`

##### state {#state}

`string`

#### Returns {#returns-1}

`Promise`<[`InstallURLOptions`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallURLOptions)\>
