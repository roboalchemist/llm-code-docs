# Source: https://nx.dev/docs/reference/devkit/stripIndents.md

▸ **stripIndents**(`strings`, `...values`): `string`

Removes indents, which is useful for printing warning and messages.

Example:

```typescript
stripIndents`
 Options:
 - option1
 - option2
`
```

#### Parameters

| Name | Type |
| :------ | :------ |
| `strings` | `TemplateStringsArray` |
| `...values` | `any`[] |

#### Returns

`string`
