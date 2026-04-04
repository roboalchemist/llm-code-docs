Source: https://docs.slack.dev/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookHTTPError

[@slack/webhook](/tools/node-slack-sdk/reference/webhook/) / IncomingWebhookHTTPError

# Interface: IncomingWebhookHTTPError

Defined in: [packages/webhook/src/errors.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/errors.ts#L25)

All errors produced by this package adhere to this interface

## Extends {#extends}

* [`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError)

## Properties {#properties}

### code {#code}

```text
code: HTTPError;
```

Defined in: [packages/webhook/src/errors.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/errors.ts#L26)

#### Overrides {#overrides}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`code`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#code)

* * *

### errno? {#errno}

```typescript
optional errno: number;
```

Defined in: node\_modules/@types/node/globals.d.ts:102

#### Inherited from {#inherited-from}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`errno`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#errno)

* * *

### message {#message}

```typescript
message: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1077

#### Inherited from {#inherited-from-1}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`message`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#message)

* * *

### name {#name}

```typescript
name: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from {#inherited-from-2}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`name`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#name)

* * *

### original {#original}

```text
original: Error;
```

Defined in: [packages/webhook/src/errors.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/errors.ts#L27)

* * *

### path? {#path}

```typescript
optional path: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:104

#### Inherited from {#inherited-from-3}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`path`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#path)

* * *

### stack? {#stack}

```typescript
optional stack: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1078

#### Inherited from {#inherited-from-4}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`stack`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#stack)

* * *

### syscall? {#syscall}

```typescript
optional syscall: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:105

#### Inherited from {#inherited-from-5}

[`CodedError`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError).[`syscall`](/tools/node-slack-sdk/reference/webhook/interfaces/CodedError#syscall)
