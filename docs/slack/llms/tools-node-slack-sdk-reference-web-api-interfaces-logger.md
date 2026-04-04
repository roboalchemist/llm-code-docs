Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Logger

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Logger

# Interface: Logger

Defined in: packages/logger/dist/index.d.ts:13

Interface for objects where objects in this package's logs can be sent (can be used as `logger` option).

## Methods {#methods}

### debug() {#debug}

```text
debug(...msg): void;
```text

Defined in: packages/logger/dist/index.d.ts:18

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
```text

Defined in: packages/logger/dist/index.d.ts:33

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
```text

Defined in: packages/logger/dist/index.d.ts:43

Return the current LogLevel.

#### Returns {#returns-2}

[`LogLevel`](/tools/node-slack-sdk/reference/web-api/enumerations/LogLevel)

* * *

### info() {#info}

```text
info(...msg): void;
```text

Defined in: packages/logger/dist/index.d.ts:23

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
```text

Defined in: packages/logger/dist/index.d.ts:39

This disables all logging below the given level, so that after a log.setLevel("warn") call log.warn("something") or log.error("something") will output messages, but log.info("something") will not.

#### Parameters {#parameters-3}

##### level {#level}

[`LogLevel`](/tools/node-slack-sdk/reference/web-api/enumerations/LogLevel)

as a string, like 'error' (case-insensitive)

#### Returns {#returns-4}

`void`

* * *

### setName() {#setname}

```text
setName(name): void;
```text

Defined in: packages/logger/dist/index.d.ts:49

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
```text

Defined in: packages/logger/dist/index.d.ts:28

Output warn message

#### Parameters {#parameters-5}

##### msg {#msg-3}

...`any`\[\]

any data to log

#### Returns {#returns-6}

`void`
