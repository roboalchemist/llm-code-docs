typebox::schema
# Struct Schema 
Source 

```
pub struct Schema {
    pub kind: SchemaKind,
    pub id: Option<String>,
    pub schema_version: Option<String>,
    pub title: Option<String>,
    pub description: Option<String>,
    pub default: Option<Value>,
    pub examples: Option<Vec<Value>>,
    pub read_only: Option<bool>,
    pub write_only: Option<bool>,
    pub deprecated: Option<bool>,
}
```

## Fields§
§`kind: SchemaKind`

The type definition.
§`id: Option<String>`

JSON Schema $id field for schema identification.
§`schema_version: Option<String>`

JSON Schema $schema field to specify the schema version.
§`title: Option<String>`

Human-readable title for the schema.
§`description: Option<String>`

Description of the schema.
§`default: Option<Value>`

Default value for the schema.
§`examples: Option<Vec<Value>>`

Example values matching this schema.
§`read_only: Option<bool>`

Mark as read-only.
§`write_only: Option<bool>`

Mark as write-only.
§`deprecated: Option<bool>`

Mark as deprecated.

## Implementations§