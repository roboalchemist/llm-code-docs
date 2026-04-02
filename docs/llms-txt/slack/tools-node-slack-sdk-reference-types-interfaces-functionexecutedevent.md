Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/FunctionExecutedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / FunctionExecutedEvent

# Interface: FunctionExecutedEvent

Defined in: [events/function.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L13)

## Properties {#properties}

### bot_access_token {#bot_access_token}

```text
bot_access_token: string;
```

Defined in: [events/function.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L32)

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: [events/function.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L31)

* * *

### function {#function}

```text
function: object;
```

Defined in: [events/function.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L15)

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

Defined in: [events/function.ts:29](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L29)

* * *

### inputs {#inputs}

```text
inputs: FunctionInputs;
```

Defined in: [events/function.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L28)

* * *

### type {#type-1}

```text
type: "function_executed";
```

Defined in: [events/function.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L14)

* * *

### workflow_execution_id {#workflow_execution_id}

```text
workflow_execution_id: string;
```

Defined in: [events/function.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/function.ts#L30)
