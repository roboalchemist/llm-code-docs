Source: https://docs.slack.dev/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError

[@slack/rtm-api](/tools/node-slack-sdk/reference/rtm-api/) / CodedError

# Interface: CodedError

Defined in: [packages/rtm-api/src/errors.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/errors.ts#L6)

All errors produced by this package adhere to this interface

## Extends {#extends}

* `ErrnoException`

## Extended by {#extended-by}

* [`RTMNoReplyReceivedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMNoReplyReceivedError)
* [`RTMPlatformError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMPlatformError)
* [`RTMSendWhileDisconnectedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMSendWhileDisconnectedError)
* [`RTMSendWhileNotReadyError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMSendWhileNotReadyError)
* [`RTMWebsocketError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMWebsocketError)

## Properties {#properties}

### code {#code}

```text
code: ErrorCode;
```

Defined in: [packages/rtm-api/src/errors.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/errors.ts#L7)

#### Overrides {#overrides}

```text
NodeJS.ErrnoException.code
```

* * *

### errno? {#errno}

```text
optional errno: number;
```

Defined in: node\_modules/@types/node/globals.d.ts:102

#### Inherited from {#inherited-from}

```text
NodeJS.ErrnoException.errno
```

* * *

### message {#message}

```text
message: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1077

#### Inherited from {#inherited-from-1}

```text
NodeJS.ErrnoException.message
```

* * *

### name {#name}

```text
name: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from {#inherited-from-2}

```text
NodeJS.ErrnoException.name
```

* * *

### path? {#path}

```text
optional path: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:104

#### Inherited from {#inherited-from-3}

```text
NodeJS.ErrnoException.path
```

* * *

### stack? {#stack}

```text
optional stack: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1078

#### Inherited from {#inherited-from-4}

```text
NodeJS.ErrnoException.stack
```

* * *

### syscall? {#syscall}

```text
optional syscall: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:105

#### Inherited from {#inherited-from-5}

```text
NodeJS.ErrnoException.syscall
```
