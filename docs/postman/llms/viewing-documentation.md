# View documentation in Postman

[Documentation](/docs/publishing-your-api/api-documentation-overview/) helps you get more out of the collections and APIs that you work with in Postman. View documentation to learn more about the requests in a collection or how to interact with an API's endpoints.

By default, documentation for a collection or API is private. You can view the documentation for any collections or APIs that have been shared with you directly or through an internal workspace.

Documentation writers can also choose to [publish their documentation](/docs/publishing-your-api/publishing-your-docs/) to make it publicly available. Anyone in the world can view the public documentation using a browser. If the associated collection is in a public workspace, people can also view the collection in Postman.

## Viewing documentation for a collection

You can view the documentation for any collection that you created or for collections that have been [shared with you](/docs/collaborating-in-postman/sharing/).

Postman teammates with the Viewer role can view documentation, while teammates with the Editor role can also create and update documentation. Learn more about [roles and permissions](/docs/administration/roles-and-permissions/).

To view documentation for a collection, do the following:

1. Click **Collections** in the sidebar, then select a collection.
2. In the **Overview** tab, click **View complete documentation**.

![View complete documentation](https://assets.postman.com/postman-docs/v11/documentation-view-complete-v11-68.png)

You can't view complete documentation if your collection has multi-protocol requests like [gRPC](/docs/sending-requests/grpc/grpc-request-interface/#the-right-sidebar) or [WebSocket](/docs/sending-requests/websocket/document-websocket-requests/). To view the description for a multi-protocol collection or folder, click it in the sidebar. To view the request's description, open the request and click ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Documentation** in the right sidebar.

The documentation includes a [description](/docs/publishing-your-api/authoring-your-documentation/#adding-descriptions-to-your-documentation) of each request and details such as the method and URL, the required authorization type, and any headers or parameters. For each request, you can view sample code in various client languages, together with example response bodies and headers.

Use the following options to customize the appearance of the documentation:

* **Version** - This defaults to **CURRENT** and isn't shown in the published documentation. You can't create versions or releases for collections in Postman v10 and later, but you can [publish versions of an API in the Postman API Builder](/docs/design-apis/api-builder/versioning-an-api/api-versions/).
* **Language** - Select a language to use for sample code.
* **Code Generation Settings** - Click ![Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings** to customize settings for the selected language.

Another way to view documentation is to visit your [user profile](https://postman.co/me/collections). Select the **Collections** tab for a list of collections that have been shared with you and your own collections. Select a collection, then click **View complete documentation** to view its documentation.

## Viewing API documentation

Postman automatically creates [documentation for a collection](#viewing-documentation-for-a-collection) you create. With [types in collections](/docs/design-apis/collections/overview/), you can build out this documentation by designing your API using a collection. You can add more details, such as data type and possible values, to request parameters, headers, and bodies in an HTTP collection.

Postman also automatically generates API documentation for any OpenAPI 2.0 or 3.0 API [defined in the API Builder](/docs/design-apis/api-builder/develop-apis/defining-an-api/). API developers can [create detailed documentation](/docs/publishing-your-api/documenting-your-api/) for any API to help consumers understand and interact with their API's endpoints.

### Viewing API documentation in a collection

To view API documentation from a collection with types, do the following:

1. Click **Collections** in the sidebar, then select a collection with types.
2. Click the collection's **Overview** tab and click **View complete documentation**.

![View documentation for a collection with types](https://assets.postman.com/postman-docs/v11/type-definition-view-docs-v11-12.jpg)

### Viewing API documentation in the API Builder

To view API documentation from the Postman API Builder, do the following:

1. Click **APIs** in the sidebar, then select an API.
2. Select a documentation source on the API's overview:
   * To view schema documentation, under **Definition**, click **View schema documentation**. (Schema documentation is available for OpenAPI 2.0 and 3.0 definitions.)
   * To view collection documentation, select a collection and click **View complete documentation**. To get sample code in a different language, select it in the **Language** dropdown list.

![Viewing API documentation](https://assets.postman.com/postman-docs/v10/documentation-view-schema-docs-v10-16.jpg)

API developers can publish different versions of an API in the Postman API Builder. You can view documentation for each published version. Learn more about [viewing a published API version](/docs/design-apis/api-builder/versioning-an-api/api-versions/).

## Viewing public documentation

Public documentation is hosted by Postman. To access public documentation, enter the documentation URL in the address bar of your browser. The URL is generated by Postman during the [publication process](/docs/publishing-your-api/publishing-your-docs/#share-your-public-docs).

Each request entry can have the following:

* A description of the request
* The required authorization type
* The method and URL
* Any headers or parameters
* Sample client code for the request
* Example response bodies and headers

Use the options in the header to customize the appearance of the documentation:

* **Version** - If the documentation has multiple versions, you can select a specific release to view. (Starting with Postman v10, you can no longer create versions or releases for collections, but you can [publish versions of an API in the Postman API Builder](/docs/design-apis/api-builder/versioning-an-api/api-versions/).)
* **Environment** - If an [environment](/docs/publishing-your-api/document-a-collection/#associate-environments-with-documentation) was published with the documentation, you can select it to populate any variables.
* **Layout** - **Double column** displays sample code in a column next to the documentation. **Single column** displays sample code inline beneath each request.
* **Language** - Select a language to use for sample code.
* **Language Settings** - Select the language settings icon ![Language settings icon](https://assets.postman.com/postman-docs/icon-settings-v9.jpg#icon) to customize settings for any of the available languages.
* **Theme** - Select the theme icon ![Light theme icon](https://assets.postman.com/postman-docs/v10/icon-theme-light-v10.jpg#icon) or ![Dark theme icon](https://assets.postman.com/postman-docs/v10/icon-theme-dark-v10.jpg#icon) to switch between light and dark themes.

![Published documentation example](https://assets.postman.com/postman-docs/v11/documentation-published-docs-v11-23.jpg)

## Linking to public documentation

Want to share a specific endpoint with someone or bookmark it for later? You can save links to sections in public documentation, including the introduction, requests, folders, and responses.

To save a link, select a section, folder, or request in the sidebar. Copy the URL in your browser's address bar, or save it as a bookmark. Next time, you can use the URL to link directly to the selected section.