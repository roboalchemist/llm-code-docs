Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WebAPIRateLimitedError

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WebAPIRateLimitedError

# Interface: WebAPIRateLimitedError

Defined in: [packages/web-api/src/errors.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L60)

All errors produced by this package adhere to this interface

## Extends {#extends}

* [`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError)

## Properties {#properties}

### code {#code}

```text
code: RateLimitedError;
```text

Defined in: [packages/web-api/src/errors.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L61)

#### Overrides {#overrides}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`code`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#code)

* * *

### errno? {#errno}

```text
optional errno: number;
```text

Defined in: node\_modules/@types/node/globals.d.ts:102

#### Inherited from {#inherited-from}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`errno`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#errno)

* * *

### message {#message}

```text
message: string;
```text

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1077

#### Inherited from {#inherited-from-1}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`message`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#message)

* * *

### name {#name}

```text
name: string;
```text

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from {#inherited-from-2}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`name`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#name)

* * *

### path? {#path}

```text
optional path: string;
```text

Defined in: node\_modules/@types/node/globals.d.ts:104

#### Inherited from {#inherited-from-3}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`path`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#path)

* * *

### retryAfter {#retryafter}

```text
retryAfter: number;
```text

Defined in: [packages/web-api/src/errors.ts:62](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L62)

* * *

### stack? {#stack}

```text
optional stack: string;
```text

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1078

#### Inherited from {#inherited-from-4}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`stack`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#stack)

* * *

### syscall? {#syscall}

```text
optional syscall: string;
```text

Defined in: node\_modules/@types/node/globals.d.ts:105

#### Inherited from {#inherited-from-5}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`syscall`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#syscall)
