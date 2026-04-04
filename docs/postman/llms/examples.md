# Create examples of request responses to illustrate API use cases

Examples show your API endpoints in action and give more details on how requests and responses work. You can add an example to a request by saving a response, or you can create an example with a custom response to illustrate a specific use case. Once you've created examples, you can use them to set up a mock server or add more detail to your API documentation.

## Understanding examples

In Postman, an example is a pairing made up of a _request_ and a related _response_. Each example includes a request part (method, URL, parameters, headers, and body) and a response part (status code, body, and headers). You add examples to requests in collections, and one request can have multiple examples.

Having multiple examples for one request is useful for illustrating the different ways an endpoint can respond to a request. You might have examples that respond with different status codes (such as 200 or 404) or that return different data (or no data at all).

Examples are useful in several ways. Developers and testers can refer to examples to better understand how an endpoint functions in different scenarios. Examples can also be used to [set up mock servers](/docs/design-apis/mock-apis/set-up-mock-servers/), so developers and testers can start [writing code](/docs/tests-and-scripts/write-scripts/test-scripts/) against your API, even before it's complete. In addition, you can include examples in your API's [public documentation](/docs/publishing-your-api/publishing-your-docs/) to help anyone in the world who uses your API.

## Add an example

An example is always associated with a [request](/docs/sending-requests/create-requests/create-requests/) in a [collection](/docs/sending-requests/create-requests/intro-to-collections/), and a request can have more than one example. To add an example to a request, send the request and then save the response as an example. You can also manually add an example to a request and define a custom response. After adding an example using either method, you can edit it at any time to make changes.

> For optimal Postman performance, example responses must be smaller than 5 MB.

### Save a response as an example

When saving a [response](/docs/sending-requests/response-data/responses/) in Postman, you have the option to save it as an example.

1. Select **Collections** in the sidebar.
1. Open a request and select **Send**.
1. In the response pane, select ![Image 1: Example icon](https://assets.postman.com/postman-docs/aether-icons/entity-example-stroke.svg#icon) **Save Response**.

![Image 2: Save a response as an example](https://assets.postman.com/postman-docs/v11/examples-save-response-v11-42.jpg)

> For [gRPC examples](/docs/sending-requests/grpc/using-grpc-examples/) with streaming methods, you must end the stream before saving the response/message stream as an example.

### Add a custom example

With a custom example, you can define how both the [request](/docs/sending-requests/create-requests/create-requests/) and the [response](/docs/sending-requests/response-data/responses/) look, including the status code and response body.

1. Select **Collections** in the sidebar.
1. Select ![Image 3: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to a request and then select **Add example**.
1. Enter a name for the example.
1. Edit the request part of the example.

    * Add any parameters or headers as needed.
    * Enter the request body and select a content type.

1. Edit the response part of the example.

    * Enter a **Status Code** (such as `200` or `404`).
    * Enter the response body and select a content type.
    * Add any headers as needed.

1. Select **Save** to save the example.

## Try an example

Examples are stored in a collection with their associated requests. You can try an example by opening the example as a request in a new tab.

1. Select **Collections** in the sidebar.
1. Select a request, and then select an example to open it.
1. Select **Try** to open the example as a request in a new tab. The request will automatically send in the new tab.

![Image 4: Trying example](https://assets.postman.com/postman-docs/v11/sending-example-response-v11.jpg)

1. Review the request and response details.

![Image 5: Open example as a request](https://assets.postman.com/postman-docs/v11/sending-example-response-duplicate-request-v11-42.jpg)

> The new request isn't automatically saved.

The name of the example you're trying is next to the request's name in the workbench. Select the example's name to open it in a separate tab.

![Image 6: Select example name](https://assets.postman.com/postman-docs/v11/example-response-name-v11.jpg)

1. Optionally, you can select **Save** to save the new request to a new or existing collection in your workspace.
1. Choose a location to save the new request, and then select **Save**.

![Image 7: Save request](https://assets.postman.com/postman-docs/v10/sending-example-response-save-request-v10-22.jpg)

## Edit an example

You can edit an example at any time to remove sensitive tokens, change the status code, or make any other adjustments.

To edit an example, do the following:

1. Select **Collections** in the sidebar.
1. Select a request, and then select an example to open it.
1. Make any changes to the example request or response.
1. Select **Save** to save the example.

To edit an example after trying it, do the following:

1. Select **Collections** in the sidebar.
1. Select a request, and then select an example to open it.
1. Select **Try** to open the example as a request in a new tab.

![Image 8: Trying example](https://assets.postman.com/postman-docs/v11/sending-example-response-v11.jpg)

1. Make any changes to the new request.
1. Select **Send**.
1. In the response pane, select ![Image 9: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** \> Update example. You will receive confirmation once the example is updated.

![Image 10: Updating example](https://assets.postman.com/postman-docs/v11/updating-example-response-v11.23.jpg)

> The new request isn't automatically saved.

1. Optionally, you can select **Save** to save the new request to a new or existing collection in your workspace.
1. Choose a location to save the new request, and then select **Save**.

![Image 11: Save request](https://assets.postman.com/postman-docs/v10/sending-example-response-save-request-v10-22.jpg)

## Share an example

You can share examples with collaborators by going to the example you want to share in the sidebar. Select ![Image 12: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to the example you want to share, then select **Share**.

![Image 13: Share example](https://assets.postman.com/postman-docs/v11/share-request-v11.23.jpg)

For more details about sharing examples, see [Share your work in Postman](/docs/collaborating-in-postman/sharing/).

## Add comments to an example

1. Select ![Image 14: Comments icon](https://assets.postman.com/postman-docs/aether-icons/action-comments-stroke.svg#icon) **Comments** in the right sidebar and enter your comment.
1. (Optional) Select the **Watch collection** checkbox to be notified when there are changes to the collection that the example is in.
1. Select **Comment** to add your comment.

You can learn more about [using comments to collaborate on examples](/docs/collaborating-in-postman/comments/).

## Duplicate an example

Duplicate an example to add a new example using an existing example as a base. You can then edit the copied example to change the name, status code, or any other part of the request or response.

1. Select **Collections** in the sidebar.
1. Select ![Image 15: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to an example, and then select **Duplicate**.
1. Make any changes to the example request or response.
1. Select **Save** to save the example.

## Delete an example

Deleting an example removes it from the collection and from the associated API documentation. Any mock servers you have set up can no longer use the example to return a response.

1. Select **Collections** in the sidebar.
1. Select the more actions icon ![Image 16: More actions icon](https://assets.postman.com/postman-docs/icon-more-actions-v9.jpg#icon) next to an example, and then select **Delete**.
1. Select **Delete** to confirm.

## Use examples in documentation

Postman automatically [generates documentation](/docs/publishing-your-api/document-a-collection/) for every collection you create. The generated documentation [includes any examples](/docs/publishing-your-api/authoring-your-documentation/#including-examples) that have been added to the collection. If you edit an example, the documentation is automatically updated with your changes.

![Image 17: Examples in documentation](https://assets.postman.com/postman-docs/v11/documentation-including-examples-v11-1.jpg)

Examples give more details and clarification for your API and help your team to work together on API development. Front-end developers, back-end developers, and testers can all work in parallel, using the examples in the documentation for guidance or to set up [mock servers](/docs/design-apis/mock-apis/set-up-mock-servers/).

> You can [publish your documentation](/docs/publishing-your-api/publishing-your-docs/) to make your examples publicly available to anyone in the world.

## Next steps

You can use examples to set up a mock server and enhance your documentation.

* To learn how to use examples to set up a mock server, visit [Set up a Postman mock server](/docs/design-apis/mock-apis/set-up-mock-servers/).
* To learn how to include examples in your API documentation, visit [Document a collection in Postman](/docs/publishing-your-api/document-a-collection/).