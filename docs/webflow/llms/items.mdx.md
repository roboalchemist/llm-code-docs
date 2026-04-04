# Source: https://developers.webflow.com/mcp/reference/data/cms/items.mdx

***

title: Items
description: 'Create, update, and manage CMS collection items'
--------------------------------------------------------------

Create, update, and manage CMS collection items using the Items tools. Items are the actual content entries in your collections.

## List items

List items in a CMS collection with optional filtering and sorting.

**Tool:** `collections_items_list_items`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="cmsLocaleId" type="string" required={false}>
    Unique identifier for the locale
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    Maximum number of records to return (max: 100)
  </ParamField>

  <ParamField path="offset" type="number" required={false}>
    Offset for pagination
  </ParamField>

  <ParamField path="name" type="string" required={false}>
    Filter by item name
  </ParamField>

  <ParamField path="slug" type="string" required={false}>
    Filter by item slug
  </ParamField>

  <ParamField path="sortBy" type="string" required={false}>
    Field to sort by
  </ParamField>

  <ParamField path="sortOrder" type="string" required={false}>
    Sort order (asc/desc)
  </ParamField>
</Card>

**Returns**
A list of items in the collection.

<EndpointResponseSnippet endpoint="GET /v2/collections/{collection_id}/items" />

***

## Create item (draft)

Create new items in a CMS collection as drafts.

**Tool:** `collections_items_create_item`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Item creation request with field values
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/items" />

**Returns:** Created item object with ID

<Note>
  Items created with this tool are saved as drafts and must be published.
</Note>

<Warning title="This tool does not create localized items">
  This tool does not create localized items.
</Warning>

***

## Create item (live)

Create and publish new items in a CMS collection directly to the live site.

**Tool:** `collections_items_create_item_live`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Item creation request with field values
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/items/live" />

**Returns:** Created and published item object

Items created with this tool are immediately published to the live site.

***

## Update items (draft)

Update existing items in a CMS collection as drafts.

**Tool:** `collections_items_update_items`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Item update request with item IDs and field updates
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="PATCH /v2/collections/{collection_id}/items" />

**Returns:** Updated item objects

***

## Update items (live)

Update and publish existing items in a CMS collection directly to the live site.

**Tool:** `collections_items_update_items_live`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Item update request with item IDs and field updates
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="PATCH /v2/collections/{collection_id}/items/live" />

**Returns:** Updated and published item objects

***

## Publish items

Publish draft items in a CMS collection to make them live.

**Tool:** `collections_items_publish_items`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="itemIds" type="array" required={true}>
    Array of item IDs to be published
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/items/publish" />

**Returns:** Publishing confirmation

***

## Delete item

Delete an item in a CMS collection. Items will only be deleted in the primary locale unless a `cmsLocaleId` is included in the request.

**Tool:** `collections_items_delete_item`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="itemId" type="string" required={true}>
    Item ID to be deleted
  </ParamField>

  <ParamField path="cmsLocaleIds" type="string" required={false}>
    Unique identifier for the locale
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="DELETE /v2/collections/{collection_id}/items/{item_id}" />

**Returns:** Deletion confirmation
