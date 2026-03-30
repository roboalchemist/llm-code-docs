# Source: https://docs.knock.app/api-reference/objects/schemas/object.md

### Object

A custom [Object](/concepts/objects) entity which belongs to a collection.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **collection** (string) *required* - The collection this object belongs to.
- **created_at** (string) - Timestamp when the resource was created.
- **id** (string) *required* - Unique identifier for the object.
- **properties** (object) - The custom properties associated with the object.
- **updated_at** (string) *required* - The timestamp when the resource was last updated.

#### Example

```json
{
  "__typename": "Object",
  "collection": "assets",
  "created_at": null,
  "id": "specimen_25",
  "properties": {
    "classification": "Theropod",
    "config": {
      "biz": "baz",
      "foo": "bar"
    },
    "name": "Velociraptor",
    "status": "contained"
  },
  "updated_at": "2024-05-22T12:00:00Z"
}
```

