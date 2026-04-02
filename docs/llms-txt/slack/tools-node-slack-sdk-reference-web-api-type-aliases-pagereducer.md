Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/PageReducer

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PageReducer

# Type Alias: PageReducer()<A>

```typescript
type PageReducer<A> = (accumulator, page, index) => A;
```

Defined in: [packages/web-api/src/WebClient.ts:156](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L156)

## Type Parameters {#type-parameters}

### A {#a}

`A` = `any`

## Parameters {#parameters}

### accumulator {#accumulator}

`A` | `undefined`

### page {#page}

[`WebAPICallResult`](/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult)

### index {#index}

`number`

## Returns {#returns}

`A`
