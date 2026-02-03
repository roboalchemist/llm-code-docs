# Send a request with the HTTP Request block

You can build a flow that uses a request from your workspace or the [Postman API Network](/docs/collaborating-in-postman/public-api-network/public-api-network-overview/). You can also create a new request when building your flow.

In this tutorial, you’ll create a new flow, collection, and request. Then, you’ll use the **HTTP Request** block to send a request to the [Postman Echo API](/docs/developer/echo-api/).

## Create a new flow

You build flows in a workspace. Workspaces let you organize your API projects and collaborate with your team.

To create a new flow, do the following:

1. Choose an existing workspace or [create a new one](/docs/collaborating-in-postman/using-workspaces/create-workspaces/).
1. In the upper left corner, click **New** > ![Image 1: Flow icon](https://assets.postman.com/postman-docs/aether-icons/entity-flow-stroke.svg#icon) **Flow**.

## Add an HTTP Request block and create a request

With an **HTTP Request** block, you can select a request from your collection or create a new request. In this tutorial, you’ll create a new request with the **HTTP Request** block.

To add an **HTTP Request** block and create a new request, do the following:

1. From the Postman sidebar, click ![Image 2: Flow icon](https://assets.postman.com/postman-docs/aether-icons/entity-flow-stroke.svg#icon) **Flows**.
1. Select your new flow.
1. Click ![Image 3: HTTP Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-httpRequest-stroke.svg#icon) **Send a request**.

![Image 4: Send a request](https://assets.postman.com/postman-docs/v11/flows-select-send-request-v11-60.png)

1. Click **Find or create new request**. The collections in your workspace appear in a dropdown list.
1. Select a collection and click **Create a new request**. If you don’t have any collections, click **Create a new request**. The Postman Flows request editor opens.

![Image 5: Postman Flows request editor](https://assets.postman.com/postman-docs/v11/flows-request-editor-v11-69.png)

1. In the request editor, select a method from the dropdown list and enter a URL.

1. (Optional) Edit the request’s name.

1. (Optional) Edit the request’s parameters, headers, and body.

1. Click **Save**.

![Image 6: Display request](https://assets.postman.com/postman-docs/v11/flows-requests-icon-v11.png#icon)

To edit a request in an existing **HTTP Request** block, click ![Image 7: Requests icon](https://assets.postman.com/postman-docs/v11/flows-requests-icon-v11.png#icon) **Requests** in the right sidebar, then select the **HTTP Request** block whose request you want to edit.

## Connect a Display block

When you connect two blocks, you connect one block's input to another block's output. Inputs are on the block's left side and outputs are on its right side.

The **Display** block shows incoming data, such as the **HTTP Request** block's outgoing API response.

To connect a **Display** block, do the following:

1. Hover over the **HTTP Request** block's **Success** output port. The pointer changes to a crosshair.
1. Decide where on the canvas you want to place the **Display** block and drag the port to that location.
1. Click ![Image 8: Output icon](https://assets.postman.com/postman-docs/aether-icons/action-output-stroke.svg#icon) **Display**. If you want to search for the block, enter **Display** in search.

## Run the flow

From the canvas toolbar, click ![Image 9: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Run**.

![Image 10: Send a request flow](https://assets.postman.com/postman-docs/v11/postman-flows-simple-request-v11-60.png)

Congratulations! You sent a request and displayed the response in a **Display** block.