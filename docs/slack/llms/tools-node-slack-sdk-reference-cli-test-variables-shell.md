Source: https://docs.slack.dev/tools/node-slack-sdk/reference/cli-test/variables/shell

[@slack/cli-test](/tools/node-slack-sdk/reference/cli-test/) / shell

# Variable: shell

```text
const shell: object;
```

Defined in: [cli/shell.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/shell.ts#L9)

## Type Declaration {#type-declaration}

### assembleShellEnv() {#assembleshellenv}

```text
assembleShellEnv: () => Record<string, string | undefined>;
```

#### Returns {#returns}

`Record`<`string`, `string` | `undefined`\>

### checkIfFinished() {#checkiffinished}

```text
checkIfFinished: (proc) => Promise<void>;
```

Logic to wait for child process to finish executing

* Check if the close event was emitted, else wait for 1 sec
* Error out if > 30 sec

#### Parameters {#parameters}

##### proc {#proc}

`ShellProcess`

#### Returns {#returns-1}

`Promise`<`void`\>

### kill() {#kill}

```text
kill: (proc) => Promise<boolean>;
```

#### Parameters {#parameters-1}

##### proc {#proc-1}

`ShellProcess`

#### Returns {#returns-2}

`Promise`<`boolean`\>

### removeANSIcolors() {#removeansicolors}

```text
removeANSIcolors: (text) => string;
```

Remove all the ANSI color and style encoding

#### Parameters {#parameters-2}

##### text {#text}

`string`

string

#### Returns {#returns-3}

`string`

### runCommandSync() {#runcommandsync}

```text
runCommandSync: (command, args, shellOpts?) => string;
```

Run shell command synchronously

* Execute child process with the command
* Wait for the command to complete and return the standard output

#### Parameters {#parameters-3}

##### command {#command}

`string`

The command to run, e.g. echo, cat, slack.exe

##### args {#args}

`string`\[\]

The arguments for the command, e.g. 'hi', '--skip-update'

##### shellOpts? {#shellopts}

`Partial`<`SpawnOptionsWithoutStdio`\>

various shell spawning options available to customize

#### Returns {#returns-4}

`string`

command stdout

### sleep() {#sleep}

```text
sleep: (timeout) => Promise<void>;
```

Sleep function used to wait for cli to finish executing

#### Parameters {#parameters-4}

##### timeout? {#timeout}

`number` = `1000`

#### Returns {#returns-5}

`Promise`<`void`\>

### spawnProcess() {#spawnprocess}

```text
spawnProcess: (command, args, shellOpts?) => ShellProcess;
```

Spawns a shell command

* Start child process with the command
* Listen to data output events and collect them

#### Parameters {#parameters-5}

##### command {#command-1}

`string`

The command to run, e.g. echo, cat, slack.exe

##### args {#args-1}

`string`\[\]

The arguments for the command, e.g. 'hi', '--skip-update'

##### shellOpts? {#shellopts-1}

`Partial`<`SpawnOptionsWithoutStdio`\>

Options to customize shell execution

#### Returns {#returns-6}

`ShellProcess`

command output

### waitForOutput() {#waitforoutput}

```text
waitForOutput: (expString, proc, opts?) => Promise<void>;
```

Wait for output

#### Parameters {#parameters-6}

##### expString {#expstring}

`string`

expected string

##### proc {#proc-2}

`ShellProcess`

##### opts? {#opts}

###### timeout? {#timeout-1}

`number`

### Description

How long to wait for expected output in milliseconds. Defaults to 10 seconds.

#### Returns {#returns-7}

`Promise`<`void`\>
