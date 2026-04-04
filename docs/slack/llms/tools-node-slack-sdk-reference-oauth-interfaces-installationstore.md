Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / InstallationStore

# Interface: InstallationStore

Defined in: [packages/oauth/src/installation-stores/interface.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/interface.ts#L5)

## Properties {#properties}

### deleteInstallation()? {#deleteinstallation}

```text
optional deleteInstallation: (query, logger?) => Promise<void>;
```

Defined in: [packages/oauth/src/installation-stores/interface.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/interface.ts#L16)

#### Parameters {#parameters}

##### query {#query}

[`InstallationQuery`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationQuery)<`boolean`\>

##### logger? {#logger}

[`Logger`](/tools/node-slack-sdk/reference/oauth/interfaces/Logger)

#### Returns {#returns}

`Promise`<`void`\>

* * *

### fetchInstallation() {#fetchinstallation}

```text
fetchInstallation: (query, logger?) => Promise<Installation<"v1" | "v2", boolean>>;
```

Defined in: [packages/oauth/src/installation-stores/interface.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/interface.ts#L11)

#### Parameters {#parameters-1}

##### query {#query-1}

[`InstallationQuery`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationQuery)<`boolean`\>

##### logger? {#logger-1}

[`Logger`](/tools/node-slack-sdk/reference/oauth/interfaces/Logger)

#### Returns {#returns-1}

`Promise`<[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)<`"v1"` | `"v2"`, `boolean`\>>

## Methods {#methods}

### storeInstallation() {#storeinstallation}

```text
storeInstallation<AuthVersion>(installation, logger?): Promise<void>;
```

Defined in: [packages/oauth/src/installation-stores/interface.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/interface.ts#L6)

#### Type Parameters {#type-parameters}

##### AuthVersion {#authversion}

`AuthVersion` _extends_ `"v1"` | `"v2"`

#### Parameters {#parameters-2}

##### installation {#installation}

[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)<`AuthVersion`, `boolean`\>

##### logger? {#logger-2}

[`Logger`](/tools/node-slack-sdk/reference/oauth/interfaces/Logger)

#### Returns {#returns-2}

`Promise`<`void`\>
