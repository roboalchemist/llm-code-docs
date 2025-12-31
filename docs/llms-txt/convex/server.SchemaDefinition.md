# Source: https://docs.convex.dev/api/classes/server.SchemaDefinition.md

# Class: SchemaDefinition\<Schema, StrictTableTypes>

[server](/api/modules/server.md).SchemaDefinition

The definition of a Convex project schema.

This should be produced by using [defineSchema](/api/modules/server.md#defineschema).

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name               | Type                                                            |
| ------------------ | --------------------------------------------------------------- |
| `Schema`           | extends [`GenericSchema`](/api/modules/server.md#genericschema) |
| `StrictTableTypes` | extends `boolean`                                               |

## Properties[​](#properties "Direct link to Properties")

### tables[​](#tables "Direct link to tables")

• **tables**: `Schema`

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/schema.ts:658](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L658)

***

### strictTableNameTypes[​](#stricttablenametypes "Direct link to strictTableNameTypes")

• **strictTableNameTypes**: `StrictTableTypes`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/schema.ts:659](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L659)

***

### schemaValidation[​](#schemavalidation "Direct link to schemaValidation")

• `Readonly` **schemaValidation**: `boolean`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/schema.ts:660](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L660)
