Source: https://docs.slack.dev/tools/node-slack-sdk/reference/logger/interfaces/Logger

[@slack/logger](/tools/node-slack-sdk/reference/logger/) / Logger

# Interface: Logger

Defined in: [index.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L14)

Interface for objects where objects in this package's logs can be sent (can be used as `logger` option).

## Methods {#methods}

### debug() {#debug}

```text
debug(...msg): void;
```

Defined in: [index.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L20)

Output debug message

#### Parameters {#parameters}

##### msg {#msg}

...`any`\[\]

any data to log

#### Returns {#returns}

`void`

* * *

### error() {#error}

```text
error(...msg): void;
```

Defined in: [index.ts:41](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L41)

Output error message

#### Parameters {#parameters-1}

##### msg {#msg-1}

...`any`\[\]

any data to log

#### Returns {#returns-1}

`void`

* * *

### getLevel() {#getlevel}

```text
getLevel(): LogLevel;
```

Defined in: [index.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L53)

Return the current LogLevel.

#### Returns {#returns-2}

[`LogLevel`](/tools/node-slack-sdk/reference/logger/enumerations/LogLevel)

* * *

### info() {#info}

```text
info(...msg): void;
```

Defined in: [index.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L27)

Output info message

#### Parameters {#parameters-2}

##### msg {#msg-2}

...`any`\[\]

any data to log

#### Returns {#returns-3}

`void`

* * *

### setLevel() {#setlevel}

```text
setLevel(level): void;
```

Defined in: [index.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L48)

This disables all logging below the given level, so that after a log.setLevel("warn") call log.warn("something") or log.error("something") will output messages, but log.info("something") will not.

#### Parameters {#parameters-3}

##### level {#level}

[`LogLevel`](/tools/node-slack-sdk/reference/logger/enumerations/LogLevel)

as a string, like 'error' (case-insensitive)

#### Returns {#returns-4}

`void`

* * *

### setName() {#setname}

```text
setName(name): void;
```

Defined in: [index.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L60)

This allows the instance to be named so that they can easily be filtered when many loggers are sending output to the same destination.

#### Parameters {#parameters-4}

##### name {#name}

`string`

as a string, will be output with every log after the level

#### Returns {#returns-5}

`void`

* * *

### warn() {#warn}

```text
warn(...msg): void;
```

Defined in: [index.ts:34](https://github.com/slackapi/node-slack-sdk/blob/main/packages/logger/src/index.ts#L34)

Output warn message

#### Parameters {#parameters-5}

##### msg {#msg-3}

...`any`\[\]

any data to log

#### Returns {#returns-6}

`void`
