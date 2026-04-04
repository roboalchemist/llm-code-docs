# Add API documentation in Postman

You can view, create, and manage your API's documentation either with collections or the Postman API Builder. You can add detailed API documentation to a collection with types. This enables you to add more details to request parameters, headers, and bodies in an HTTP collection. With the API Builder, you can also add detailed documentation for any OpenAPI 2.0 or 3.0 definition. You can then generate a collection from the API or add a copy of an existing collection.

The API documentation includes complete API, path, and operation information, such as authentication methods, parameters, request bodies, response bodies and headers, and examples. The documentation also includes information for various data models, such as required attributes, default values, minimum and maximum values, and other constraints.

## Add API documentation with collections

Postman automatically creates [documentation for a collection](/docs/publishing-your-api/document-a-collection/) you create. With [types in collections](/docs/design-apis/collections/overview/), you can build out this documentation by designing your API with the Postman Collection format. You can add more details to request parameters, headers, and bodies in the collection, such as data type and possible values. Details you add appear in your collection's documentation.

To get started, [add types to parameters and headers](/docs/design-apis/collections/add-properties-to-parameters-and-headers/). You can also [add types to body data](/docs/design-apis/collections/add-properties-to-body-data/) in your requests.

To view the documentation for a collection with types, do the following:

1. Click **Collections** in the sidebar, then select a collection with types.
1. Click the collection's **Overview** tab and click **View complete documentation**.

![View documentation for a collection with types](https://assets.postman.com/postman-docs/v11/type-definition-view-docs-v11-12.jpg)

## Add API documentation with the API Builder

If you are [designing an API in the API Builder](/docs/design-apis/api-builder/develop-apis/defining-an-api/) based on the OpenAPI 2.0 or 3.0 specification, Postman automatically creates documentation based on your API definition.

With the API Builder, you can create documentation from a [new collection](#create-new-documentation-for-an-api) or an [existing collection](#add-existing-documentation-to-an-api). You can also [edit a collection's documentation](#edit-api-documentation) and [delete a collection and its documentation](#delete-api-documentation) if you no longer need it.

To view the documentation for an OpenAPI 2.0 or 3.0 API from the Postman API Builder, do the following:

1. Click **APIs** in the sidebar and select an API.
1. On the API's overview, under **Definition**, click **View schema documentation**.

![Viewing schema documentation](https://assets.postman.com/postman-docs/v10/documentation-view-schema-docs-v10-16.jpg)

You can also view schema documentation while editing your OpenAPI 2.0 or 3.0 definition. Postman displays a live preview of the documentation as you work on your API. Learn more about [previewing schema documentation](/docs/design-apis/api-builder/develop-apis/defining-an-api/#preview-schema-documentation).

## Create new documentation for an API

To generate a new collection for API documentation from the Postman API Builder, do the following:

1. Click **APIs** in the sidebar and select an API.
1. On the API's overview, next to **Collections**, click \[img alt="Add icon" src="https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon" width="16px"\] **Add** and select **Generate from definition**.
1. Select the checkbox if you want Postman to suggest updates for the collection when the API definition changes. This checkbox is selected by default. Learn more about [keeping a collection in sync with an API](/docs/design-apis/api-builder/develop-apis/adding-api-elements/#keep-a-collection-in-sync-with-your-api).
1. Change any settings to customize the new collection.
1. Click **Generate Collection**.

The new collection displays on your API's overview and under your API in the sidebar. To view documentation for the collection, select the collection and click **View complete documentation**.

You can also [generate a collection from Spec Hub](/docs/design-apis/specifications/generate-collections/). Postman automatically creates a collection with folders, requests, and response examples based on the specification.

## Add existing documentation to an API

Copy an existing collection with API documentation to an API.

If you copy a [collection with types](/docs/design-apis/collections/overview/), types won't be copied to the new collection linked to the API.

To use an existing collection for API documentation in the Postman API Builder, do the following:

1. Click **APIs** in the sidebar and select an API.
1. On the API's overview, next to **Collections**, click \[img alt="Add icon" src="https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon" width="16px"\] **Add** and select **Copy existing collection**.
1. Select an available collection and click **Copy Collection**.

The copy of the collection displays on your API's overview and under your API in the sidebar. To view documentation for the collection, select the collection and click **View complete documentation**.

When you add a collection, an independent copy of the collection is added to the API. The copy in the API will no longer be in sync with the original. If you move or delete an API, any collections contained in the API are moved or deleted with it.

## Edit API documentation

You can add to your API documentation collections from the API Builder.

To edit a documentation collection from the Postman API Builder, do the following:

1. Click **APIs** in the sidebar and select an API.
1. On the API's overview, select a collection and click **View full documentation**.
1. Enter a description for any item. To learn more about using Postman's built-in editing tools, see [Write your docs](/docs/publishing-your-api/authoring-your-documentation/).
1. Click outside of the editor to save your new content.

Schema documentation can't be edited directly. Instead, [edit your API's definition](/docs/design-apis/api-builder/develop-apis/defining-an-api/) and then click **Save**. Postman automatically updates the API docs to reflect the latest changes to your definition.

![Editing API documentation](https://assets.postman.com/postman-docs/v10/documentation-editing-api-docs-v10-16.jpg)

## Delete API documentation

The process to delete a collection's documentation requires you to delete the collection.

To delete a documentation collection from the Postman API Builder, do the following:

1. Click **APIs** in the sidebar and select an API.
1. Next to the API, click \[img alt="Options icon" src="https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon" width="16px" role="img"\] **View more actions**. Then click **Delete**.

## Next steps

After adding documentation to an API in Postman, you can edit and format the docs. You can also publish your API, including the documentation.

* To learn more about adding descriptions to a collection, including collections linked to an API, see [Document a collection in Postman](/docs/publishing-your-api/document-a-collection/).
* To learn more about editing and formatting your documentation, see [Write documentation in Postman](/docs/publishing-your-api/authoring-your-documentation/).
* To learn how users can access your documentation, see [View documentation in Postman](/docs/publishing-your-api/viewing-documentation/). By default, your documentation is private, so you must share an API with others before they can access it.
* To learn how to publish your API in the Postman API Builder to make it available to consumers, see [Publish a version of your API for consumers in the Postman API Builder](/docs/design-apis/api-builder/versioning-an-api/api-versions/).