Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WebAPIHTTPError

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WebAPIHTTPError

# Interface: WebAPIHTTPError

Defined in: [packages/web-api/src/errors.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L51)

All errors produced by this package adhere to this interface

## Extends {#extends}

* [`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError)

## Properties {#properties}

### body? {#body}

```text
optional body: any;
```text

Defined in: [packages/web-api/src/errors.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L57)

* * *

### code {#code}

```text
code: HTTPError;
```text

Defined in: [packages/web-api/src/errors.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L52)

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

### headers {#headers}

```text
headers: IncomingHttpHeaders;
```text

Defined in: [packages/web-api/src/errors.ts:55](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L55)

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

### stack? {#stack}

```text
optional stack: string;
```text

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1078

#### Inherited from {#inherited-from-4}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`stack`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#stack)

* * *

### statusCode {#statuscode}

```text
statusCode: number;
```text

Defined in: [packages/web-api/src/errors.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L53)

* * *

### statusMessage {#statusmessage}

```text
statusMessage: string;
```text

Defined in: [packages/web-api/src/errors.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/errors.ts#L54)

* * *

### syscall? {#syscall}

```text
optional syscall: string;
```text

Defined in: node\_modules/@types/node/globals.d.ts:105

#### Inherited from {#inherited-from-5}

[`CodedError`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError).[`syscall`](/tools/node-slack-sdk/reference/web-api/interfaces/CodedError#syscall)
