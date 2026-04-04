# Source: https://typescript-eslint.io/packages/rule-schema-to-typescript-types

On this page# `@typescript-eslint/rule-schema-to-typescript-types`
[](https://npmjs.com/@typescript-eslint/rule-schema-to-typescript-types)
Converts ESLint rule schemas to equivalent TypeScript type strings ✨
```
import { schemaToTypes } from &#x27;@typescript-eslint/rule-schema-to-typescript-types&#x27;;
// "
// type Options = [
//   /** My great option! */
//   string[]
// ];
// "
schemaToTypes({
description: &#x27;My great option!&#x27;,
items: { type: &#x27;string&#x27; },
type: &#x27;array&#x27;,
});
```
The following documentation is auto-generated from source code.
## Functions[​](#functions)
### schemaToTypes()[​](#schematotypes)
```
function schemaToTypes(schema): string;
```
Defined in: [index.ts:17](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/rule-schema-to-typescript-types/src/index.ts#L17)
Converts rule options schema(s) to the equivalent TypeScript type string.
#### Parameters[​](#parameters)
ParameterTypeDescription`schema``JSONSchema4` | readonly `JSONSchema4`[]Original rule schema(s) as declared in `meta.schema`.
#### Returns[​](#returns)
`string`
Stringified TypeScript type(s) equivalent to the options schema(s).
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/packages/RuleSchemaToTypeScriptTypes.mdx)- [Functions](#functions)[schemaToTypes()](#schematotypes)