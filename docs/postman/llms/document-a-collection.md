# Document a collection in Postman

Postman automatically generates basic documentation for any collection you create. The documentation includes details about all of the requests in your collection, along with sample code in various client languages. Request details include the method, authorization type, URL, headers, request and response structures, and examples. In addition, the documentation displays all key-value pairs for request parameters, headers, and bodies.

To make your documentation even more valuable to users, [add descriptions](/docs/publishing-your-api/authoring-your-documentation/#adding-descriptions-to-your-documentation) to the items in your collection. Any descriptions you add are automatically included in the documentation for your collection.

## Add descriptions to a collection

Add descriptions to your collections (including [collections linked to an API](/docs/publishing-your-api/documenting-your-api/)) to enhance your documentation and add more detail. You can use the Postman editor to view how your content will look as you write it, or use standard Markdown syntax to write content. With either editor, you can format text, add links, and insert images and videos in your documentation.

To add a description to a collection or folder, do the following:

1. Click **Collections** in the sidebar, and then select a collection or a folder.
2. Enter a description in the **Overview** tab. To learn more about using Postman's built-in editing tools, see [Write your docs](/docs/publishing-your-api/authoring-your-documentation/).
3. Click outside of the editor to save your new content.

![Documenting a collection](https://assets.postman.com/postman-docs/v11/documentation-overview-tab-v11.jpg)

To add a description to a request, do the following:

1. Click **Collections** in the sidebar, and then select a request.
2. Click the documentation icon ![Documentation icon](https://assets.postman.com/postman-docs/documentation-icon-v8-10.jpg#icon) in the right sidebar.
3. Enter a description in the right sidebar. To learn more about using Postman's built-in editing tools, see [Write your docs](/docs/publishing-your-api/authoring-your-documentation/).
4. Click outside of the editor to save your new content.

![Documenting a request](https://assets.postman.com/postman-docs/v11/documentation-pane-v11-b.jpg)

You can also edit descriptions when viewing the complete documentation for a collection. Select a collection in the sidebar, then click **View complete documentation** in the **Overview** tab. From here, you can add a description to any item in the collection.

## Document gRPC and WebSocket collections

Collections with gRPC or WebSocket requests use a different format than collections with HTTP requests. You can view documentation and add descriptions for gRPC or WebSocket requests. You can also add a description on the collection's **Overview** tab, but you can't view or edit documentation for the full collection. Learn more about [documenting gRPC requests](/docs/sending-requests/grpc/grpc-request-interface/#the-right-sidebar) or [documenting WebSocket requests](/docs/sending-requests/websocket/document-websocket-requests/).

## Associate environments with documentation

An [environment](/docs/sending-requests/variables/managing-environments/) is a set of related [variables](/docs/sending-requests/variables/variables/) you can use in Postman requests. You can also refer to variables when [writing descriptions](/docs/publishing-your-api/authoring-your-documentation/) in a collection. In each case, the shared value of the variable is automatically populated in the documentation.

Anyone using your collection can view the variables in the documentation if the associated environment is also shared with them. For public documentation, you can select an environment during the [publishing process](/docs/publishing-your-api/publishing-your-docs/). Publishing an environment makes it available to anyone [viewing public documentation](/docs/publishing-your-api/viewing-documentation/).

To use an environment variable in your documentation, do the following:

1. [Create a new environment](/docs/sending-requests/variables/managing-environments/) if one doesn't already exist.
2. Make the environment active by selecting it in the [environment dropdown list](/docs/sending-requests/variables/managing-environments/#switch-between-environments).
3. If needed, [add a new variable](/docs/sending-requests/variables/managing-environments/#add-environment-variables) to the environment.
4. Add a [reference to the variable](/docs/sending-requests/variables/variables/#using-variables) to requests or descriptions in your collection.

![Referencing a variable](https://assets.postman.com/postman-docs/v11/documentation-add-variable-v11-b.jpg)

If someone imports a collection using the **Run in Postman** button from your documentation, they also import the environment and any associated variables. The shared values for variables are published in your documentation, so make sure they don't contain any sensitive data.

## Next steps

After documenting a collection in Postman, you can edit and format the docs and publish them.

* To learn more about documenting an API in Postman, see [Add API documentation in Postman](/docs/publishing-your-api/documenting-your-api/).
* To learn more about editing and formatting your documentation, see [Write documentation in Postman](/docs/publishing-your-api/authoring-your-documentation/).
* To learn how users can access your documentation, see [View documentation in Postman](/docs/publishing-your-api/viewing-documentation/). By default, your documentation is private, so you must share a collection with others before they can access it.
* To make your documentation publicly available, see [Publish documentation in Postman](/docs/publishing-your-api/publishing-your-docs/).

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) See how to document an API with a collection template that's a boilerplate for documentation that you can customize and reuse. To try out this template, visit [API documentation](https://www.postman.com/templates/collections/api-documentation/).