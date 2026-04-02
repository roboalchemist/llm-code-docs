Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/PageAccumulator

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PageAccumulator

# Type Alias: PageAccumulator<R>

```typescript
type PageAccumulator<R> = R extends (accumulator, page, index) => infer A ? A : never;
```

Defined in: [packages/web-api/src/WebClient.ts:158](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L158)

## Type Parameters {#type-parameters}

### R {#r}

`R` _extends_ [`PageReducer`](/tools/node-slack-sdk/reference/web-api/type-aliases/PageReducer)
