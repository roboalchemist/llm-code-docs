# Source: https://docs.xano.com/xano-features/metadata-api/content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Content

The Metadata API enables you to interact with database table content (database records). The following are various of examples of how to create, update, delete, and truncate content.

### Create Content

In this example, we will create content. The endpoint requires a workspace ID and table ID. In addition, the name of the field(s) and value(s) that you wish to create.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/09b79afd-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=abd480d7bbc8ef8bc1ace4e9e402b4f7" width="2304" height="998" data-path="images/09b79afd-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "id": 11,
  "created_at": 1681349436618,
  "name": "headphones",
  "description": "high quality listening device",
  "category_id": 3,
  "price": 99
}
```

### Update Existing Content

To update an existing record, the content ID (primary ID of the record) is also required. In this example, we will update the price from the above example to be 500

<Info>
  The Metadata is flexible with updates: We only need to pass what we want to update. For example, if we want all the other fields to remain the same for ID 11 but want to update price then we can just pass the new value for price.
</Info>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/48100890-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=8cd29df0f26b06cb13433f7a359c31e5" width="2304" height="1108" data-path="images/48100890-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "id": 11,
  "created_at": 1681349436618,
  "name": "headphones",
  "description": "high quality listening device",
  "category_id": 3,
  "price": 500
}
```

### Delete Content

Deleting content is straightforward, it requires the content ID, table ID, and workspace ID.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a489d516-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=60ea9d63e4aa3246532270615a822f8a" width="2304" height="870" data-path="images/a489d516-image.jpeg" />
</Frame>

The response will be null since we are just deleting a record.

### Truncate Content

Truncate content will clear all the content of a table. You can optionally reset the primary key back to 1 for the table.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/a197f6a9-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=8d6442d87087b11ec280c3d8f1f62031" width="2304" height="893" data-path="images/a197f6a9-image.jpeg" />
</Frame>

The response will be null since we are truncating the table.

<Warning>
  This action cannot be done and will result in the loss of content (records).
</Warning>

### Search and Browse Content

To see examples of getting content via browse and search please visit the next page:


Built with [Mintlify](https://mintlify.com).