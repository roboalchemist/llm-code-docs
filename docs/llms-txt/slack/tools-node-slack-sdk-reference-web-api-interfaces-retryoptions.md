Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RetryOptions

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RetryOptions

# Interface: RetryOptions

Defined in: [packages/web-api/src/retry-policies.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/retry-policies.ts#L6)

Options to create retry policies. Extends from [https://github.com/tim-kos/node-retry](https://github.com/tim-kos/node-retry).

## Extends {#extends}

* `OperationOptions`

## Properties {#properties}

### factor? {#factor}

```text
optional factor: number;
```text

Defined in: node\_modules/@types/retry/index.d.ts:125

The exponential factor to use.

#### Default {#default}

```text
2
```text

#### Inherited from {#inherited-from}

```text
OperationOptions.factor
```text

* * *

### forever? {#forever}

```text
optional forever: boolean;
```text

Defined in: node\_modules/@types/retry/index.d.ts:88

Whether to retry forever.

#### Default {#default-1}

```text
false
```text

#### Inherited from {#inherited-from-1}

```text
OperationOptions.forever
```text

* * *

### maxRetryTime? {#maxretrytime}

```text
optional maxRetryTime: number;
```text

Defined in: node\_modules/@types/retry/index.d.ts:98

The maximum time (in milliseconds) that the retried operation is allowed to run.

#### Default {#default-2}

```text
Infinity
```text

#### Inherited from {#inherited-from-2}

```text
OperationOptions.maxRetryTime
```text

* * *

### maxTimeout? {#maxtimeout}

```text
optional maxTimeout: number;
```text

Defined in: node\_modules/@types/retry/index.d.ts:135

The maximum number of milliseconds between two retries.

#### Default {#default-3}

```text
Infinity
```text

#### Inherited from {#inherited-from-3}

```text
OperationOptions.maxTimeout
```text

* * *

### minTimeout? {#mintimeout}

```text
optional minTimeout: number;
```text

Defined in: node\_modules/@types/retry/index.d.ts:130

The number of milliseconds before starting the first retry.

#### Default {#default-4}

```text
1000
```text

#### Inherited from {#inherited-from-4}

```text
OperationOptions.minTimeout
```text

* * *

### randomize? {#randomize}

```text
optional randomize: boolean;
```text

Defined in: node\_modules/@types/retry/index.d.ts:140

Randomizes the timeouts by multiplying a factor between 1-2.

#### Default {#default-5}

```text
false
```text

#### Inherited from {#inherited-from-5}

```text
OperationOptions.randomize
```text

* * *

### retries? {#retries}

```text
optional retries: number;
```text

Defined in: node\_modules/@types/retry/index.d.ts:109

The maximum amount of times to retry the operation.

#### Default {#default-6}

```text
10
```text

#### Inherited from {#inherited-from-6}

```text
OperationOptions.retries
```text

* * *

### unref? {#unref}

```text
optional unref: boolean;
```text

Defined in: node\_modules/@types/retry/index.d.ts:93

Whether to [unref](https://nodejs.org/api/timers.html#timers_unref) the setTimeout's.

#### Default {#default-7}

```text
false
```text

#### Inherited from {#inherited-from-7}

```text
OperationOptions.unref
```text
