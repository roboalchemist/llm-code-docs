# Source: https://docs.knock.app/api-reference/objects/schemas/inline_object_request.md

### InlineIdentifyObjectRequest

A custom [Object](/concepts/objects) entity which belongs to a collection.

#### Attributes

- **channel_data** (unknown) - An optional set of [channel data](/managing-recipients/setting-channel-data) for the object. This is a list of `ChannelData` objects.
- **collection** (string) *required* - The collection this object belongs to.
- **created_at** (string) - Timestamp when the resource was created.
- **id** (string) *required* - Unique identifier for the object.
- **name** (string) - An optional name for the object.
- **preferences** (unknown) - An optional set of [preferences](/concepts/preferences) for the object.

#### Example

```json
{
  "collection": "projects",
  "id": "project_1",
  "name": "My project"
}
```

