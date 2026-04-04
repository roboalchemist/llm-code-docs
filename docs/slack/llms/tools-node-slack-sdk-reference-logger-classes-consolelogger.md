Source: https://docs.slack.dev/tools/node-slack-sdk/reference/logger/classes/ConsoleLogger

[@slack/logger](/tools/node-slack-sdk/reference/logger/) / ConsoleLogger

# Class: ConsoleLogger

Defined in: [index.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L66)

Default logger which logs to stdout and stderr

## Implements {#implements}

* [`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger)

## Constructors {#constructors}

### Constructor {#constructor}

```text
new ConsoleLogger(): ConsoleLogger;
```

Defined in: [index.ts:88](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L88)

#### Returns {#returns}

`ConsoleLogger`

## Methods {#methods}

### debug() {#debug}

```text
debug(...msg): void;
```

Defined in: [index.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L115)

Log a debug message

#### Parameters {#parameters}

##### msg {#msg}

...`any`\[\]

#### Returns {#returns-1}

`void`

#### Implementation of {#implementation-of}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`debug`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#debug)

* * *

### error() {#error}

```text
error(...msg): void;
```

Defined in: [index.ts:145](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L145)

Log an error message

#### Parameters {#parameters-1}

##### msg {#msg-1}

...`any`\[\]

#### Returns {#returns-2}

`void`

#### Implementation of {#implementation-of-1}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`error`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#error)

* * *

### getLevel() {#getlevel}

```text
getLevel(): LogLevel;
```

Defined in: [index.ts:93](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L93)

Return the current LogLevel.

#### Returns {#returns-3}

[`LogLevel`](/tools/node-slack-sdk/reference/logger/enumerations/LogLevel)

#### Implementation of {#implementation-of-2}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`getLevel`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#getlevel)

* * *

### info() {#info}

```text
info(...msg): void;
```

Defined in: [index.ts:125](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L125)

Log an info message

#### Parameters {#parameters-2}

##### msg {#msg-2}

...`any`\[\]

#### Returns {#returns-4}

`void`

#### Implementation of {#implementation-of-3}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`info`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#info)

* * *

### setLevel() {#setlevel}

```text
setLevel(level): void;
```

Defined in: [index.ts:100](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L100)

Sets the instance's log level so that only messages which are equal or more severe are output to the console.

#### Parameters {#parameters-3}

##### level {#level}

[`LogLevel`](/tools/node-slack-sdk/reference/logger/enumerations/LogLevel)

#### Returns {#returns-5}

`void`

#### Implementation of {#implementation-of-4}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`setLevel`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#setlevel)

* * *

### setName() {#setname}

```text
setName(name): void;
```

Defined in: [index.ts:107](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L107)

Set the instance's name, which will appear on each log line before the message.

#### Parameters {#parameters-4}

##### name {#name}

`string`

#### Returns {#returns-6}

`void`

#### Implementation of {#implementation-of-5}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`setName`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#setname)

* * *

### warn() {#warn}

```text
warn(...msg): void;
```

Defined in: [index.ts:135](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L135)

Log a warning message

#### Parameters {#parameters-5}

##### msg {#msg-3}

...`any`\[\]

#### Returns {#returns-7}

`void`

#### Implementation of {#implementation-of-6}

[`Logger`](/tools/node-slack-sdk/reference/logger/interfaces/Logger).[`warn`](/tools/node-slack-sdk/reference/logger/interfaces/Logger#warn)
