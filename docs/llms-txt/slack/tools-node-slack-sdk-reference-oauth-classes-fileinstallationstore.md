Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/classes/FileInstallationStore

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / FileInstallationStore

# Class: FileInstallationStore

Defined in: [packages/oauth/src/installation-stores/file-store.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/file-store.ts#L14)

## Implements {#implements}

* [`InstallationStore`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore)

## Constructors {#constructors}

### Constructor {#constructor}

```text
new FileInstallationStore(__namedParameters?): FileInstallationStore;
```

Defined in: [packages/oauth/src/installation-stores/file-store.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/file-store.ts#L19)

#### Parameters {#parameters}

##### __namedParameters? {#__namedparameters}

`FileInstallationOptions` = `{}`

#### Returns {#returns}

`FileInstallationStore`

## Methods {#methods}

### deleteInstallation() {#deleteinstallation}

```text
deleteInstallation(query, logger?): Promise<void>;
```

Defined in: [packages/oauth/src/installation-stores/file-store.ts:99](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/file-store.ts#L99)

#### Parameters {#parameters-1}

##### query {#query}

[`InstallationQuery`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationQuery)<`boolean`\>

##### logger? {#logger}

[`Logger`](/tools/node-slack-sdk/reference/oauth/interfaces/Logger)

#### Returns {#returns-1}

`Promise`<`void`\>

#### Implementation of {#implementation-of}

[`InstallationStore`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore).[`deleteInstallation`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore#deleteinstallation)

* * *

### fetchInstallation() {#fetchinstallation}

```text
fetchInstallation(query, logger?): Promise<Installation<"v1" | "v2", boolean>>;
```

Defined in: [packages/oauth/src/installation-stores/file-store.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/file-store.ts#L61)

#### Parameters {#parameters-2}

##### query {#query-1}

[`InstallationQuery`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationQuery)<`boolean`\>

##### logger? {#logger-1}

[`Logger`](/tools/node-slack-sdk/reference/oauth/interfaces/Logger)

#### Returns {#returns-2}

`Promise`<[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)<`"v1"` | `"v2"`, `boolean`\>>

#### Implementation of {#implementation-of-1}

[`InstallationStore`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore).[`fetchInstallation`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore#fetchinstallation)

* * *

### storeInstallation() {#storeinstallation}

```text
storeInstallation(installation, logger?): Promise<void>;
```

Defined in: [packages/oauth/src/installation-stores/file-store.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-stores/file-store.ts#L28)

#### Parameters {#parameters-3}

##### installation {#installation}

[`Installation`](/tools/node-slack-sdk/reference/oauth/interfaces/Installation)

##### logger? {#logger-2}

[`Logger`](/tools/node-slack-sdk/reference/oauth/interfaces/Logger)

#### Returns {#returns-3}

`Promise`<`void`\>

#### Implementation of {#implementation-of-2}

[`InstallationStore`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore).[`storeInstallation`](/tools/node-slack-sdk/reference/oauth/interfaces/InstallationStore#storeinstallation)
