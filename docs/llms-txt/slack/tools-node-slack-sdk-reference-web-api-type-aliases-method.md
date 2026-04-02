Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/Method

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Method

# Type Alias: Method()<MethodArguments, MethodResult>

```typescript
type Method<MethodArguments, MethodResult> = (options?) => Promise<MethodResult>;
```

Defined in: [packages/web-api/src/methods.ts:561](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/methods.ts#L561)

## Type Parameters {#type-parameters}

### MethodArguments {#methodarguments}

`MethodArguments`

### MethodResult {#methodresult}

`MethodResult` _extends_ [`WebAPICallResult`](/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult) = [`WebAPICallResult`](/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult)

## Parameters {#parameters}

### options? {#options}

`MethodArguments`

## Returns {#returns}

`Promise`<`MethodResult`\>
