# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/functions/wrapopenai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wrapOpenAI

> TypeScript SDK reference

# wrapOpenAI

▸ **wrapOpenAI**\<`T`>(`openai`): `T`

Wraps the OpenAI API to enable function tracing for OpenAI calls.

#### Type parameters

| Name | Type                |
| :--- | :------------------ |
| `T`  | extends `OpenAIAPI` |

#### Parameters

| Name     | Type |
| :------- | :--- |
| `openai` | `T`  |

#### Returns

`T`

`Example`

```ts  theme={null}
const openai = wrapOpenAI(new OpenAI());
const result = await openai.chat.completions.create({
  model: 'gpt-3.5-turbo',
  messages: [{ role: 'user', content: 'Hello, world!' }]
});
```

#### Defined in

[integrations/openai.ts:469](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/integrations/openai.ts#L469)
