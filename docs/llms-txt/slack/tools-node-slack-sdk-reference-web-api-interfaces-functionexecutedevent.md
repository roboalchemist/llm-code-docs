Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FunctionExecutedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FunctionExecutedEvent

# Interface: FunctionExecutedEvent

Defined in: packages/types/dist/events/function.d.ts:11

## Properties {#properties}

### bot_access_token {#bot_access_token}

```text
bot_access_token: string;
```

Defined in: packages/types/dist/events/function.d.ts:30

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: packages/types/dist/events/function.d.ts:29

* * *

### function {#function}

```text
function: object;
```

Defined in: packages/types/dist/events/function.d.ts:13

#### app_id {#app_id}

```text
app_id: string;
```

#### callback_id {#callback_id}

```text
callback_id: string;
```

#### date_created {#date_created}

```text
date_created: number;
```

#### date_deleted {#date_deleted}

```text
date_deleted: number;
```

#### date_updated {#date_updated}

```text
date_updated: number;
```

#### description? {#description}

```text
optional description: string;
```

#### id {#id}

```text
id: string;
```

#### input_parameters {#input_parameters}

```text
input_parameters: FunctionParams[];
```

#### output_parameters {#output_parameters}

```text
output_parameters: FunctionParams[];
```

#### title {#title}

```text
title: string;
```

#### type {#type}

```text
type: string;
```

* * *

### function_execution_id {#function_execution_id}

```text
function_execution_id: string;
```

Defined in: packages/types/dist/events/function.d.ts:27

* * *

### inputs {#inputs}

```text
inputs: FunctionInputs;
```

Defined in: packages/types/dist/events/function.d.ts:26

* * *

### type {#type-1}

```text
type: "function_executed";
```

Defined in: packages/types/dist/events/function.d.ts:12

* * *

### workflow_execution_id {#workflow_execution_id}

```text
workflow_execution_id: string;
```

Defined in: packages/types/dist/events/function.d.ts:28
