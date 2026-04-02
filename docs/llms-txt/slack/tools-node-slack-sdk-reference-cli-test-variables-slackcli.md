Source: https://docs.slack.dev/tools/node-slack-sdk/reference/cli-test/variables/SlackCLI

[@slack/cli-test](/tools/node-slack-sdk/reference/cli-test/) / SlackCLI

# Variable: SlackCLI

```text
const SlackCLI: object;
```

Defined in: [cli/index.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/cli-test/src/cli/index.ts#L22)

Set of functions to spawn and interact with Slack Platform CLI processes and commands

## Type Declaration {#type-declaration}

### app {#app}

```text
app: object;
```

#### app.delete() {#appdelete}

```text
delete: (args) => Promise<string> = del;
```

`slack app delete`

##### Parameters {#parameters}

###### args {#args}

`ProjectCommandArguments`

##### Returns {#returns}

`Promise`<`string`\>

command output

#### app.install() {#appinstall}

```text
install: (args) => Promise<string>;
```

`slack app install`

##### Parameters {#parameters-1}

###### args {#args-1}

`ProjectCommandArguments`

##### Returns {#returns-1}

`Promise`<`string`\>

command output

#### app.list() {#applist}

```text
list: (args) => Promise<string>;
```

`slack app list`

##### Parameters {#parameters-2}

###### args {#args-2}

`ProjectCommandArguments`

##### Returns {#returns-2}

`Promise`<`string`\>

command output

### auth {#auth}

```text
auth: object;
```

#### auth.loginChallengeExchange() {#authloginchallengeexchange}

```text
loginChallengeExchange: (args) => Promise<string>;
```

`slack login --no-prompt --challenge --ticket`

##### Parameters {#parameters-3}

###### args {#args-3}

`AuthLoginChallengeExchangeArugments`

##### Returns {#returns-3}

`Promise`<`string`\>

#### auth.loginNoPrompt() {#authloginnoprompt}

```text
loginNoPrompt: (args?) => Promise<{  authTicket: string;  authTicketSlashCommand: string;  output: string;}>;
```

`slack login --no-prompt`; initiates a CLI login flow. The `authTicketSlashCommand` returned should be entered into the Slack client, and the challenge code retrieved and fed into the `loginChallengeExchange` method to complete the CLI login flow.

##### Parameters {#parameters-4}

###### args? {#args-4}

`AuthLoginNoPromptArguments`

##### Returns {#returns-4}

`Promise`<{ `authTicket`: `string`; `authTicketSlashCommand`: `string`; `output`: `string`; }>

#### auth.logout() {#authlogout}

```text
logout: (args?) => Promise<string>;
```

`slack logout`

##### Parameters {#parameters-5}

###### args? {#args-5}

Omit<SlackCLIGlobalOptions, "team"> & (Pick<SlackCLIGlobalOptions, "team"> | { all?: boolean | undefined; })

##### Returns {#returns-5}

`Promise`<`string`\>

command output

### collaborator {#collaborator}

```text
collaborator: object;
```

#### collaborator.add() {#collaboratoradd}

```text
add: (args) => Promise<string>;
```

`slack collaborators add`

##### Parameters {#parameters-6}

###### args {#args-6}

`ProjectCommandArguments` & `CollaboratorEmail`

##### Returns {#returns-6}

`Promise`<`string`\>

command output

#### collaborator.list() {#collaboratorlist}

```text
list: (args) => Promise<string>;
```

`slack collaborators list`

##### Parameters {#parameters-7}

###### args {#args-7}

`ProjectCommandArguments`

##### Returns {#returns-7}

`Promise`<`string`\>

command output

#### collaborator.remove() {#collaboratorremove}

```text
remove: (args) => Promise<string>;
```

`slack collaborators remove`

##### Parameters {#parameters-8}

###### args {#args-8}

`ProjectCommandArguments` & `CollaboratorEmail`

##### Returns {#returns-8}

`Promise`<`string`\>

command output

### create() {#create}

```text
create: (args) => Promise<string>;
```

`slack create`

#### Parameters {#parameters-9}

##### args {#args-9}

`ProjectCommandArguments` & `object`

#### Returns {#returns-9}

`Promise`<`string`\>

command output

### datastore {#datastore}

```text
datastore: object;
```

#### datastore.datastoreDelete() {#datastoredatastoredelete}

```text
datastoreDelete: (args) => Promise<string>;
```

`slack datastore delete`

##### Parameters {#parameters-10}

###### args {#args-10}

`ProjectCommandArguments` & `Pick`<`DatastoreCommandArguments`, `"datastoreName"` | `"primaryKeyValue"`\>

##### Returns {#returns-10}

`Promise`<`string`\>

command output

#### datastore.datastoreGet() {#datastoredatastoreget}

```text
datastoreGet: (args) => Promise<string>;
```

`slack datastore get`

##### Parameters {#parameters-11}

###### args {#args-11}

`ProjectCommandArguments` & `Pick`<`DatastoreCommandArguments`, `"datastoreName"` | `"primaryKeyValue"`\>

##### Returns {#returns-11}

`Promise`<`string`\>

command output

#### datastore.datastorePut() {#datastoredatastoreput}

```text
datastorePut: (args) => Promise<string>;
```

`slack datastore put`

##### Parameters {#parameters-12}

###### args {#args-12}

`ProjectCommandArguments` & `Pick`<`DatastoreCommandArguments`, `"datastoreName"` | `"putItem"`\>

##### Returns {#returns-12}

`Promise`<`string`\>

command output

#### datastore.datastoreQuery() {#datastoredatastorequery}

```text
datastoreQuery: (args) => Promise<string>;
```

`slack datastore query`

##### Parameters {#parameters-13}

###### args {#args-13}

`ProjectCommandArguments` & `Pick`<`DatastoreCommandArguments`, `"datastoreName"` | `"queryExpression"` | `"queryExpressionValues"`\>

##### Returns {#returns-13}

`Promise`<`string`\>

command output

### env {#env}

```text
env: object;
```

#### env.add() {#envadd}

```text
add: (args) => Promise<string>;
```

`slack env add`

##### Parameters {#parameters-14}

###### args {#args-14}

`ProjectCommandArguments` & `EnvCommandArguments`

##### Returns {#returns-14}

`Promise`<`string`\>

command output

#### env.list() {#envlist}

```text
list: (args) => Promise<string>;
```

`slack env list`

##### Parameters {#parameters-15}

###### args {#args-15}

`ProjectCommandArguments`

##### Returns {#returns-15}

`Promise`<`string`\>

command output

#### env.remove() {#envremove}

```text
remove: (args) => Promise<string>;
```

`slack env remove`

##### Parameters {#parameters-16}

###### args {#args-16}

`ProjectCommandArguments` & `Pick`<`EnvCommandArguments`, `"secretKey"`\>

##### Returns {#returns-16}

`Promise`<`string`\>

command output

### externalAuth {#externalauth}

```text
externalAuth: object;
```

#### externalAuth.add() {#externalauthadd}

```text
add: (args) => Promise<string>;
```

`slack external-auth add`

##### Parameters {#parameters-17}

###### args {#args-17}

`ProjectCommandArguments` & `Pick`<`ExternalAuthCommandArguments`, `"provider"`\>

##### Returns {#returns-17}

`Promise`<`string`\>

command output

#### externalAuth.addSecret() {#externalauthaddsecret}

```text
addSecret: (args) => Promise<string>;
```

`slack external-auth add-secret`

##### Parameters {#parameters-18}

###### args {#args-18}

`ProjectCommandArguments` & `Omit`<`ExternalAuthCommandArguments`, `"all"`\>

##### Returns {#returns-18}

`Promise`<`string`\>

command output

#### externalAuth.remove() {#externalauthremove}

```text
remove: (args) => Promise<string>;
```

`slack external-auth remove`

##### Parameters {#parameters-19}

###### args {#args-19}

`ProjectCommandArguments` & `Omit`<`ExternalAuthCommandArguments`, `"secret"`\>

##### Returns {#returns-19}

`Promise`<`string`\>

command output

#### externalAuth.selectAuth() {#externalauthselectauth}

```text
selectAuth: (args) => Promise<string>;
```

`slack external-auth select-auth`

##### Parameters {#parameters-20}

###### args {#args-20}

`ProjectCommandArguments` & `Pick`<`ExternalAuthCommandArguments`, `"provider"`\> & `object`

##### Returns {#returns-20}

`Promise`<`string`\>

command output

### function {#function}

```text
function: object = func;
```

#### function.access() {#functionaccess}

```text
access: (args) => Promise<string>;
```

`slack function access`

##### Parameters {#parameters-21}

###### args {#args-21}

`ProjectCommandArguments` & `FunctionAccessArguments`

##### Returns {#returns-21}

`Promise`<`string`\>

command output

### manifest {#manifest}

```text
manifest: object;
```

#### manifest.info() {#manifestinfo}

```text
info: (args) => Promise<string>;
```

`slack manifest info`

##### Parameters {#parameters-22}

###### args {#args-22}

`ProjectCommandArguments` & `object`

##### Returns {#returns-22}

`Promise`<`string`\>

command output

#### manifest.validate() {#manifestvalidate}

```text
validate: (args) => Promise<string>;
```

`slack manifest validate`

##### Parameters {#parameters-23}

###### args {#args-23}

`ProjectCommandArguments`

##### Returns {#returns-23}

`Promise`<`string`\>

command output

### platform {#platform}

```text
platform: object;
```

#### platform.activity() {#platformactivity}

```text
activity: (args) => Promise<string>;
```

`slack platform activity`

##### Parameters {#parameters-24}

###### args {#args-24}

`ProjectCommandArguments` & `object`

##### Returns {#returns-24}

`Promise`<`string`\>

command output

#### platform.activityTailStart() {#platformactivitytailstart}

```text
activityTailStart: (args) => Promise<ShellProcess>;
```

`slack platform activity` but waits for a specified sequence then returns the shell At the specific point where the sequence is found to continue with test

##### Parameters {#parameters-25}

###### args {#args-25}

`ProjectCommandArguments` & `StringWaitArgument` & `TimeoutArgument`

##### Returns {#returns-25}

`Promise`<`ShellProcess`\>

command output

#### platform.activityTailStop() {#platformactivitytailstop}

```text
activityTailStop: (args) => Promise<string>;
```

Waits for a specified string in the provided `activityTailStart` process output, kills the process then returns the output

##### Parameters {#parameters-26}

###### args {#args-26}

`StringWaitArgument` & `ProcessArgument` & `TimeoutArgument`

##### Returns {#returns-26}

`Promise`<`string`\>

command output

#### platform.deploy() {#platformdeploy}

```text
deploy: (args) => Promise<string>;
```

`slack deploy`

##### Parameters {#parameters-27}

###### args {#args-27}

`ProjectCommandArguments` & `Omit`<`RunDeployArguments`, `"cleanup"`\>

##### Returns {#returns-27}

`Promise`<`string`\>

command output

#### platform.runStart() {#platformrunstart}

```text
runStart: (args) => Promise<ShellProcess>;
```

start `slack run`. `runStop` must be used to stop the `run` process returned by this method.

##### Parameters {#parameters-28}

###### args {#args-28}

`ProjectCommandArguments` & `RunDeployArguments` & `TimeoutArgument`

##### Returns {#returns-28}

`Promise`<`ShellProcess`\>

shell object to kill it explicitly in the test case via `runStop`

#### platform.runStop() {#platformrunstop}

```text
runStop: (args) => Promise<void>;
```

stop `slack run`

##### Parameters {#parameters-29}

###### args {#args-29}

`ProcessArgument` & `TimeoutArgument` & `object`

##### Returns {#returns-29}

`Promise`<`void`\>

### stopSession() {#stopsession}

```text
stopSession: (args) => Promise<void>;
```

Delete app and Log out of current team session

#### Parameters {#parameters-30}

##### args {#args-30}

`Partial`<`ProjectCommandArguments`\> & `object`

#### Returns {#returns-30}

`Promise`<`void`\>

### trigger {#trigger}

```text
trigger: object;
```

#### trigger.access() {#triggeraccess}

```text
access: (args) => Promise<string>;
```

`slack trigger access`

##### Parameters {#parameters-31}

###### args {#args-31}

`ProjectCommandArguments` & `TriggerAccessArguments`

##### Returns {#returns-31}

`Promise`<`string`\>

command output

#### trigger.create() {#triggercreate}

```text
create: (args) => Promise<string>;
```

`slack trigger create`

##### Parameters {#parameters-32}

###### args {#args-32}

`ProjectCommandArguments` & `CreateArguments`

##### Returns {#returns-32}

`Promise`<`string`\>

command output

#### trigger.delete() {#triggerdelete}

```text
delete: (args) => Promise<string> = del;
```

`slack trigger delete`

##### Parameters {#parameters-33}

###### args {#args-33}

`ProjectCommandArguments` & `TriggerIdArgument`

##### Returns {#returns-33}

`Promise`<`string`\>

command output

#### trigger.info() {#triggerinfo}

```text
info: (args) => Promise<string>;
```

`slack trigger info`

##### Parameters {#parameters-34}

###### args {#args-34}

`ProjectCommandArguments` & `TriggerIdArgument`

##### Returns {#returns-34}

`Promise`<`string`\>

command output

#### trigger.list() {#triggerlist}

```text
list: (args) => Promise<string>;
```

`slack trigger list`

##### Parameters {#parameters-35}

###### args {#args-35}

`ProjectCommandArguments` & `object`

##### Returns {#returns-35}

`Promise`<`string`\>

command output

#### trigger.update() {#triggerupdate}

```text
update: (args) => Promise<string>;
```

`slack trigger update`

##### Parameters {#parameters-36}

###### args {#args-36}

`ProjectCommandArguments` & TriggerIdArgument & (CreateFromFile | Partial<CreateFromArguments>)

##### Returns {#returns-36}

`Promise`<`string`\>

command output

### version {#version}

```text
version: object;
```

#### version.version() {#versionversion}

```text
version: () => Promise<string>;
```

`slack version`

##### Returns {#returns-37}

`Promise`<`string`\>

command output
