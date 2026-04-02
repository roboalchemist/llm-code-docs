Source: https://docs.slack.dev/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMSendWhileDisconnectedError

[@slack/rtm-api](/tools/node-slack-sdk/reference/rtm-api/) / RTMSendWhileDisconnectedError

# Interface: RTMSendWhileDisconnectedError

Defined in: [packages/rtm-api/src/errors.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/errors.ts#L47)

All errors produced by this package adhere to this interface

## Extends {#extends}

* [`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError)

## Properties {#properties}

### code {#code}

```text
code: SendWhileDisconnectedError;
```

Defined in: [packages/rtm-api/src/errors.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/errors.ts#L48)

#### Overrides {#overrides}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`code`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#code)

* * *

### errno? {#errno}

```text
optional errno: number;
```

Defined in: node\_modules/@types/node/globals.d.ts:102

#### Inherited from {#inherited-from}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`errno`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#errno)

* * *

### message {#message}

```text
message: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1077

#### Inherited from {#inherited-from-1}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`message`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#message)

* * *

### name {#name}

```text
name: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from {#inherited-from-2}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`name`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#name)

* * *

### path? {#path}

```text
optional path: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:104

#### Inherited from {#inherited-from-3}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`path`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#path)

* * *

### stack? {#stack}

```text
optional stack: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1078

#### Inherited from {#inherited-from-4}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`stack`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#stack)

* * *

### syscall? {#syscall}

```text
optional syscall: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:105

#### Inherited from {#inherited-from-5}

[`CodedError`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError).[`syscall`](/tools/node-slack-sdk/reference/rtm-api/interfaces/CodedError#syscall)
