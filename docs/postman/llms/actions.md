# Deploy flows as actions in Postman Flows

An _action_ is a flow that's deployed in the Postman cloud. Unlike [_flow modules_](/docs/postman-flows/get-started/build-your-first-flow/), which must be run manually, actions can be scheduled, or triggered by external systems like third-party services, other APIs, or webhooks. Actions are useful for running automations and exposing functionality as an API or as an AI tool for MCP servers.

## Create an action

To create a new action, do the following:

1. In the **Flows** tab, select ![Image 1: Create a new folder or flow](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Create a new folder or flow** > ![Image 2: Flows action icon](https://assets.postman.com/postman-docs/aether-icons/action-flowsAction-stroke.svg#icon) **Create action**. The action appears with a [**Request** block](/docs/postman-flows/reference/blocks/request/), a placeholder [**Template** block](/docs/postman-flows/reference/blocks/template/), and a [**Response** block](/docs/postman-flows/reference/blocks/response/). The **Request** block's three output ports will send headers, query parameters, and body data received from an external API call.

1. Delete the **AI Agent** and **Display** blocks if you don't need them.

1. Set up the [**Request** block](/docs/postman-flows/reference/blocks/request/).

1. Add and connect blocks to [create a flow](/docs/postman-flows/get-started/build-your-first-flow/) that processes data from one or more of the **Request** block's output ports. The flow will also route data to the **Response** block's **Status Code**, **Headers**, and **Body** ports.

1. Set up the [**Response** block](/docs/postman-flows/reference/blocks/response/) to return status codes and include routed data in the response's headers and body according to your requirements.

1. Click **Run** to test your action locally with [scenario](/docs/postman-flows/build-flows/configure/scenarios/) data.

You can design your actions to be _synchronous_ (sync) or _asynchronous_ (async). In a sync action, all the blocks complete their functions before the action sends a response. An async action sends a response before its blocks finish running. For more information, see [Synchronous and Asynchronous actions](/docs/postman-flows/reference/flows-actions-overview/#synchronous-and-asynchronous-actions).

Learn more about creating actions with this [video tutorial](/docs/postman-flows/tutorials/video/work-with-actions/).

## Deploy an action

After you create an action you can _deploy_ it to make it publicly available. For more information about deploying actions, see [Deploy actions with snapshots](/docs/postman-flows/reference/flows-actions-overview/#deploy-actions-with-snapshots).

To deploy an action to the cloud, do the following:

1. In your action, click **Deploy** and enter the following:

    * **Snapshot** - Create a new [snapshot](/docs/postman-flows/build-flows/configure/snapshots/) of the action or select an existing snapshot. This is the version of the action that will be deployed.
    
    * **Action URL** - This path will be added to the domain where the action is deployed. You can use the resulting URL to call the action.
    
    * **Timeout** - Sets the amount of time that the action will wait before sending a 408 Request Timeout error if it hasn't finished running. Enter a value between 5 and 30 seconds (inclusive). For more information, see [Manage long-running actions](/docs/postman-flows/reference/flows-actions-overview/#manage-long-running-actions).
    
    * **Description** - Describe the action's purpose and any important details.

1. Click **Deploy**. The action runs in the Postman cloud at the specified URL, and a summary of the action appears. The summary includes the action's status, URL, and version.

## Deploy a new snapshot of an action

If you make changes to your action, you can deploy the new version and create a new [snapshot](/docs/postman-flows/build-flows/configure/snapshots/) of it.

To deploy a new version of an existing action, do the following:

1. In your action, click **Deploy**.

1. (Optional) Enter a description of the changes.

1. Click **Deploy**. The new version of the action is deployed to the original URL and a new snapshot is created.

## Deploy a previous snapshot of an action

To revert an action to a previous [snapshot](/docs/postman-flows/build-flows/configure/snapshots/), do the following:

1. In your action, click **Deploy**.

1. Click the ![Image 3: Versions icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-versions-stroke.svg#icon) **Snapshots** dropdown list.

1. Select the snapshot you want to deploy.

1. Click **Deploy**.

    The local version of your action doesn't automatically restore the snapshot when you deploy it. To learn about restoring snapshots and more, see [Version flows with snapshots](/docs/postman-flows/build-flows/configure/snapshots/).

## Schedule an action to run automatically

You can trigger actions at regular intervals or at specific times.

To trigger an action with a schedule, do the following:

1. In the **Request** block in your action, click **Change trigger** and select ![Image 4: Calendar icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-calendar-stroke.svg#icon) **Schedule**. The **Request** block changes to a **Schedule** block.

1. In the text box, enter when you want the action to run in plain language. For example, you could enter "Run once per minute for five minutes." The shortest time increment you can schedule is one minute. The longest is one year.

1. Click **Apply**.

1. [Deploy the action](#deploy-an-action). The **Deploy** window shows the action's current schedule and next scheduled run. When deployed, the action runs automatically on the specified schedule.

1. (Optional) To trigger the action with a request instead of a schedule, in the **Schedule** block click **Change trigger**, select ![Image 5: Open right icon](https://assets.postman.com/postman-docs/aether-icons/action-openRight-stroke.svg#icon) **Request**, and deploy the action again.

## Enforce bearer token authorization for actions

You can configure actions to authorize requests with a [_bearer token_](/docs/sending-requests/authorization/authorization-types/#bearer-token). To require a bearer token for your action, do the following:

1. [Create](#create-an-action) and [deploy](#deploy-an-action) an action.

1. In the **Deploy** dialog, click **Turn on \u003e Turn on**.

    ![Image 6: Enable auth](https://assets.postman.com/postman-docs/v11/flows-enable-actions-auth-v11-52.jpg)

1. Click ![Image 7: Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy** to copy the **Auth** token. You can then share the token with authorized users so they can include it in requests to the action's URL.

    ![Image 8: Async action](https://assets.postman.com/postman-docs/v11/flows-actions-copy-auth-v11-52.jpg)

1. (Optional) Click ![Image 9: Refresh icon](https://assets.postman.com/postman-docs/aether-icons/action-refresh-stroke.svg#icon) **Regenerate token** to create a new token.