# Source: https://developers.webflow.com/data/docs/working-with-the-cms/manage-collections-and-items.mdx

***

title: Managing CMS Collections and Items
subtitle: An end-to-end guide for creating and managing CMS content programmatically.
description: >-
An in-depth, example-driven guide to the end-to-end workflow of managing CMS
collections and items.
max-toc-depth: 3
----------------

This page covers how to programmatically manage your Webflow CMS content. You'll learn how to:

1. Create a collection and define its schema.
2. Populate the collection with content and perform CRUD operations on those items.
3. Publish a collection and its items.

<Note title="Generate schemas and content with AI">
  Use the [MCP Server](/data/docs/ai-tools) to create a Collection and its Items from a single natural language prompt. Go from a simple description to a fully populated Collection in seconds.
</Note>

***

## 1. Creating a collection

The first step in managing your content is to create a collection, which serves as a blueprint for your items. This process involves getting your `site_id`, defining a schema, and then creating the collection via the API. To learn more about collections, see the [Collections Reference](/data/reference/cms/collections).

<Steps>
  <Step title="Get your site ID">
    Every collection is associated with a specific Webflow site. You'll need your `site_id` to create a collection. You can find this by calling the [List Sites](/data/reference/sites/list) endpoint and locating the site you want to work with in the response.

    <EndpointRequestSnippet endpoint="GET /v2/sites" />
  </Step>

  <Step title="Define the collection schema">
    Next, you'll define the schema for your collection. This includes the `displayName` for the collection, the `singularName` for its items, the `slug` for the collection, and an array of `fields`.

    #### Default fields

    Each collection will always have the following fields in its schema:

    * `name` - The name of the item
    * `slug` - The slug of the item. Slugs should be unique, and formatted as all lowercase with no spaces. Any spaces will be converted to "-".

    #### Custom fields

    You can add additional custom fields to the collection. Each field will have its own `type`, `displayName`, `slug`, and other properties to configure its behavior. A collection's schema can have up to 60 fields. To see the different field types and their properties, see the [Field Types & Item Values Reference](/data/reference/field-types-item-values).

    Here is an example of a schema for a "Hitchhiker's Guide" collection that includes various field types:

    ```javascript title="Example collection schema"
    {
      "displayName": "Guide Entries",
      "singularName": "Guide Entry",
      "slug": "guide-entries",
      "fields": [
        {
          "type": "PlainText",
          "displayName": "Entry Title",
          "slug": "entry-title",
          "isRequired": true
        },
        {
          "type": "RichText",
          "displayName": "Entry HTML",
          "slug": "entry-html"
        },
        {
          "type": "Image",
          "displayName": "Illustration Image",
          "slug": "illustration-image"
        },
        {
          "type": "Number",
          "displayName": "Importance Level",
          "slug": "importance-level"
        },
        {
          "type": "Switch",
          "displayName": "Is Essential",
          "slug": "is-essential"
        },
        {
          "type": "Reference",
          "displayName": "Related Entry",
          "slug": "related-entry",
          "metadata": {
            "collectionId": "7f15043107e2fc95644e93807ee25dd6"
          }
        },
        {
          "type": "Option",
          "displayName": "Item Type",
          "slug": "item-type",
          "metadata": {
            "options": [
              {"name": "Survival Gear"},
              {"name": "Gadget"},
              {"name": "Other"}
            ]
          }
        }
      ]
    }
    ```

    <Warning title="Field Validations">
      When defining a field in the Webflow UI, you can also specify validations for the field. Currently, the API doesn't support field validations. All validations must be specified in the Webflow UI.
    </Warning>
  </Step>

  <Step title="Create the collection">
    With your `site_id` and schema, you can now create the collection by making a `POST` request to the [Create Collection](/data/reference/cms/collections/create) endpoint.

    <EndpointRequestSnippet endpoint="POST /v2/sites/{site_id}/collections" example="CollectionCreate" />
  </Step>
</Steps>

#### Adding advanced field types

When defining a collection's schema, `Option` and `Reference` fields require a `metadata` object to be configured.

<Accordion title="Defining an Option Field">
  The `Option` field allows you to create a predefined list of choices for an item, which can be selected from a dropdown menu in the CMS.

  When creating an `Option` field, you must provide a `metadata` object containing an `options` array. Each object in the array defines a choice with a `name`. Webflow will automatically generate an `id` for each option.

  <CodeBlocks>
    <Code title="Field definition for an Option field">
      ```javascript
      {
        "type": "Option",
        "displayName": "Item Type",
        "slug": "item-type",
        "metadata": {
          "options": [
            {"name": "Survival Gear"},
            {"name": "Gadget"},
            {"name": "Other"}
          ]
        }
      }
      ```
    </Code>
  </CodeBlocks>
</Accordion>

<Accordion title="Defining Reference and Multi-Reference Fields">
  The `Reference` and `Multi-Reference` fields allow you to link a collection item to one or more other items from another collection.

  When creating `Reference` or `Multi-Reference` fields, you must provide a `metadata` object containing the `collectionId` of the collection you intend to reference.

  <Steps>
    <Step title="Get the Collection ID">
      First, you need the `id` of the collection you want to reference. You can get this by calling the [List Collections](/data/reference/cms/collections/list) endpoint and finding the target collection in the response.

      <EndpointRequestSnippet endpoint="GET /v2/sites/{site_id}/collections" />
    </Step>

    <Step title="Define the Field">
      Use the retrieved `collectionId` in the `metadata` object when defining your `Reference` or `Multi-Reference` field in a "Create Collection" or "Create Field" request.

      <CodeBlocks>
        <Code title="Field definition for a Reference field">
          ```javascript
          {
            "type": "Reference",
            "displayName": "Related Entry",
            "slug": "related-entry",
            "metadata": {
              "collectionId": "7f15043107e2fc95644e93807ee25dd6" // ID of the collection to reference
            }
          }
          ```
        </Code>
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

***

## 2. Managing collection items

Once your collection is created, you can begin to populate it with items. The following sections demonstrate how to perform CRUD (Create, Read, Update, Delete) operations on the items in your new collection.

When creating collection items, you can use the staged or live endpoints to manage the item's publishing state. For more details on publishing options when creating an item, see the [Publishing Guide](/data/docs/working-with-the-cms/publishing).

### Creating an item

<Steps>
  <Step title="Get the collection ID">
    First, you need the `id` of the collection you want to create an item for. The [Create Collection](/data/reference/cms/collections/create) response will include the collection's `id`. However, you can also get the collection ID by calling the [List Collections](/data/reference/cms/collections/list) endpoint and finding the collection in the response.

    <EndpointRequestSnippet endpoint="GET /v2/collections/{collection_id}" />
  </Step>

  <Step title="Create a collection item">
    To add an item, send a `POST` request to the [Create Collection Item](/data/reference/cms/collection-items/create-item) endpoint. The `fieldData` object in the request body must match the schema you defined for the collection.

    <EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/items" example="SingleItemUpdate" />
  </Step>
</Steps>

#### Populating advanced field types

Most fields accept simple values like strings or numbers. However, fields like `Option`, and `Reference` require specific identifiers. The sections below explain how to get the correct IDs to populate these fields when creating or updating an item.

<Accordion title="Populating an option field">
  `Option` fields require the unique `id` of the choice, which is defined in the collection's schema.

  <Steps>
    <Step title="Get collection details">
      To find the `id` for each option, retrieve the collection's schema by calling the [Get Collection Details](/data/reference/cms/collections/get) endpoint.

      <EndpointRequestSnippet endpoint="GET /v2/collections/{collection_id}" />
    </Step>

    <Step title="Find the option ID">
      In the response, locate your `Option` field within the `fields` array. The `validations.options` array will contain each choice with its `name` and `id`.

      ```json
      // Snippet from GET /v2/collections/{collection_id} response
      {
        "fields": [
          {
            "type": "Option",
            "slug": "item-type",
            "validations": {
              "options": [
                { "name": "Survival Gear", "id": "66f6e966c9e1dc700a857ca3" },
                { "name": "Gadget", "id": "66f6e966c9e1dc700a857ca4" },
                { "name": "Other", "id": "66f6e966c9e1dc700a857ca5" }
              ]
            }
          }
        ]
      }
      ```
    </Step>

    <Step title="Use the option ID">
      When creating or updating an item, pass the `id` of your chosen option as a string in the `fieldData`.

      <CodeBlocks>
        <Code title="fieldData with an option field">
          ```javascript
          {
            "fieldData": {
              "item-type": "66f6e966c9e1dc700a857ca3" // ID for "Survival Gear"
            }
          }
          ```
        </Code>
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

<Accordion title="Populating reference and multi-reference fields">
  `Reference` and `Multi-Reference` fields link an item to one or more other collection items. To create a reference, you need the `id` of the item you want to link to.

  <Note>
    To reference a collection item, the collection must be published to the site.
  </Note>

  <Steps>
    <Step title="Find the item IDs">
      To get the `id` of the item you want to reference, call the [List Items](/data/reference/cms/collection-items/staged-items/list-items) endpoint on the collection that contains the target item. You can filter the results to find the specific items you need.
    </Step>

    <Step title="Use the item IDs">
      For a `Reference` field, pass the item `id` as a string. For a `Multi-Reference` field, pass an array of item `id` strings.

      <CodeBlocks>
        <Code title="fieldData with reference fields">
          ```javascript
          {
            "fieldData": {
              "related-entry": "42b720ef280c7a7a3be8cabe", // Single item reference
              "mentioned-in": [
                "62b720ef280c7a7a3be8cabd",
                "62c880ef281c7b7b4cf9dabc"
              ] // Multi-item reference
            }
          }
          ```
        </Code>
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

### Listing, updating, and deleting items

<Steps>
  <Step title="List collection items">
    To get a list of all items in a collection, send a `GET` request to the [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) endpoint.

    <EndpointRequestSnippet endpoint="GET /v2/collections/{collection_id}/items" />

    #### Pagination

    When listing items, the response will be paginated. You can control the pagination using the `limit` and `offset` query parameters.

    * `limit`: The maximum number of items to return (up to 100).
    * `offset`: The number of items to skip from the beginning of the list.

    By default, the API will return up to 100 items. If a collection contains more than 100 items, you can use `offset` to retrieve additional pages of results. For example, to get the second page of 100 items, you would set `offset` to `100`.

    <EndpointRequestSnippet endpoint="GET /v2/collections/{collection_id}/items?offset=100&limit=100" />

    The response will include a `pagination` object with `total`, `limit`, and `offset` fields, which you can use to loop through the pages of results.

    ```json title="Example pagination object"
    // Snippet from GET /v2/collections/{collection_id}/items response
    {
      "items": [
        // ... item data ...
      ],
      "pagination": {
        "total": 250,
        "limit": 100,
        "offset": 100
      }
    }
    ```
  </Step>

  <Step title="Update a collection item">
    To modify an existing item, you'll first need its `id`. You can get the item's `id` by calling the [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) endpoint and finding the item in the response.

    Then, use the `PATCH` endpoint to [Update a Collection Item](/data/reference/cms/collection-items/staged-items/update-items). You only need to provide the fields you want to change in the `fieldData` object.

    <EndpointRequestSnippet endpoint="PATCH /v2/collections/{collection_id}/items/{item_id}" example="SingleItem" />
  </Step>

  <Step title="Delete a collection item">
    To remove an item from a collection, you'll need its `id`. You can get the item's `id` by calling the [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) endpoint and finding the item in the response.

    Then, use the `DELETE` endpoint to [Delete a Collection Item](/data/reference/cms/collection-items/staged-items/delete-items).

    <EndpointRequestSnippet endpoint="DELETE /v2/collections/{collection_id}/items/{item_id}" />
  </Step>
</Steps>

***

## 3. Publishing a collection

Once you've created your collection and its items, you can publish the collection. This will make the collection and its items visible on your live site. Additionally, this allows the collection's items to be referenced by other collections.

To publish a collection or any collection items, **you'll need to publish the entire site.** You can publish the site by calling the [Publish Site](/data/reference/sites/publish) endpoint.

<EndpointRequestSnippet endpoint="POST /v2/sites/{site_id}/publish" />

***

## Next steps

Once you have created your collections and populated them with content, you can explore more advanced topics like publishing and localization.

<CardGroup>
  <Card
    title="Publishing Content"
    href="/data/docs/working-with-the-cms/publishing"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/PublishDesigner.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/PublishDesigner.svg" alt="" className="block dark:hidden" />
    </>
}
  >
    Learn how to tailor CMS publishing workflows to your needs.
  </Card>

  <Card
    title="Localizing Content"
    href="/data/docs/working-with-the-cms/localization"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Localization.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Localization.svg" alt="" className="block dark:hidden" />
    </>
}
  >
    Learn how to create and manage linked CMS items across multiple locales.
  </Card>
</CardGroup>
