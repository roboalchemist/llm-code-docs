Source: https://docs.slack.dev/tools/node-slack-sdk/reference/cli-test/classes/SlackCLIProcess

[@slack/cli-test](/tools/node-slack-sdk/reference/cli-test/) / SlackCLIProcess

# Class: SlackCLIProcess

Defined in: [cli/cli-process.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L49)

## Constructors {#constructors}

### Constructor {#constructor}

```text
new SlackCLIProcess(   command,    globalOptions?,    commandOptions?): SlackCLIProcess;
```

Defined in: [cli/cli-process.ts:65](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L65)

#### Parameters {#parameters}

##### command {#command}

`string`\[\]

##### globalOptions? {#globaloptions}

`SlackCLIGlobalOptions`

##### commandOptions? {#commandoptions}

`SlackCLICommandOptions`

#### Returns {#returns}

`SlackCLIProcess`

## Properties {#properties}

### command {#command-1}

```text
command: string[];
```

Defined in: [cli/cli-process.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L53)

#### Description {#description}

The CLI command to invoke

* * *

### commandOptions {#commandoptions-1}

```text
commandOptions: SlackCLICommandOptions | undefined;
```

Defined in: [cli/cli-process.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L63)

#### Description {#description-1}

The CLI command-specific options to pass to the command

* * *

### globalOptions {#globaloptions-1}

```text
globalOptions: SlackCLIGlobalOptions | undefined;
```

Defined in: [cli/cli-process.ts:58](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L58)

#### Description {#description-2}

The global CLI options to pass to the command

## Methods {#methods}

### execAsync() {#execasync}

```text
execAsync(shellOpts?): Promise<ShellProcess>;
```

Defined in: [cli/cli-process.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L81)

#### Parameters {#parameters-1}

##### shellOpts? {#shellopts}

`Partial`<`SpawnOptionsWithoutStdio`\>

#### Returns {#returns-1}

`Promise`<`ShellProcess`\>

#### Description {#description-3}

Executes the command asynchronously, returning the process details once the process finishes executing

* * *

### execAsyncUntilOutputPresent() {#execasyncuntiloutputpresent}

```text
execAsyncUntilOutputPresent(output, shellOpts?): Promise<ShellProcess>;
```

Defined in: [cli/cli-process.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L92)

#### Parameters {#parameters-2}

##### output {#output}

`string`

##### shellOpts? {#shellopts-1}

`Partial`<`SpawnOptionsWithoutStdio`\>

#### Returns {#returns-2}

`Promise`<`ShellProcess`\>

#### Description {#description-4}

Executes the command asynchronously, returning the process details once the process finishes executing

* * *

### execSync() {#execsync}

```text
execSync(shellOpts?): string;
```

Defined in: [cli/cli-process.ts:108](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/cli-process.ts#L108)

#### Parameters {#parameters-3}

##### shellOpts? {#shellopts-2}

`Partial`<`SpawnOptionsWithoutStdio`\>

#### Returns {#returns-3}

`string`

#### Description {#description-5}

Executes the command synchronously, returning the process standard output
