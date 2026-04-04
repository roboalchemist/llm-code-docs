Source: https://docs.slack.dev/tools/node-slack-sdk/reference/webhook/interfaces/CodedError

[@slack/webhook](/tools/node-slack-sdk/reference/webhook/) / CodedError

# Interface: CodedError

Defined in: [packages/webhook/src/errors.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/errors.ts#L6)

All errors produced by this package adhere to this interface

## Extends {#extends}

* `ErrnoException`

## Extended by {#extended-by}

* [`IncomingWebhookHTTPError`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookHTTPError)
* [`IncomingWebhookRequestError`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookRequestError)

## Properties {#properties}

### code {#code}

```text
code: ErrorCode;
```

Defined in: [packages/webhook/src/errors.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/errors.ts#L7)

#### Overrides {#overrides}

```text
NodeJS.ErrnoException.code
```

* * *

### errno? {#errno}

```typescript
optional errno: number;
```

Defined in: node\_modules/@types/node/globals.d.ts:102

#### Inherited from {#inherited-from}

```text
NodeJS.ErrnoException.errno
```

* * *

### message {#message}

```typescript
message: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1077

#### Inherited from {#inherited-from-1}

```text
NodeJS.ErrnoException.message
```

* * *

### name {#name}

```typescript
name: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from {#inherited-from-2}

```text
NodeJS.ErrnoException.name
```

* * *

### path? {#path}

```typescript
optional path: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:104

#### Inherited from {#inherited-from-3}

```text
NodeJS.ErrnoException.path
```

* * *

### stack? {#stack}

```typescript
optional stack: string;
```

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1078

#### Inherited from {#inherited-from-4}

```text
NodeJS.ErrnoException.stack
```

* * *

### syscall? {#syscall}

```typescript
optional syscall: string;
```

Defined in: node\_modules/@types/node/globals.d.ts:105

#### Inherited from {#inherited-from-5}

```text
NodeJS.ErrnoException.syscall
```
