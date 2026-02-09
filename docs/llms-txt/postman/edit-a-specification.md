# edit-a-specification

Edit your API specification
===========================

Edit your specification to update the structure and design of your API. [Navigate your specification](#navigate-your-specification) using the outline in the sidebar and [the command palette](#navigate-using-the-command-palette) to find and jump to specific sections. You can [add new sections using snippets](#add-new-sections-using-snippets) to add pre-formatted blocks that you can fill out. You can [generate a schema from a JSON request or response body](#generate-a-schema-from-a-json-body), and add the schema directly to your specification. You can also organize your OpenAPI 2.0, 3.0, or 3.1 specification into [multiple files and folders](#add-files-and-folders).

As you edit your specification, Postman offers [autocomplete suggestions](#edit-your-specification-using-autocomplete) for properties and valid values.

Postman identifies [syntax errors and API governance issues](/docs/design-apis/specifications/validate-a-specification/), and shows details so you can fix them. Postman also displays a [live preview of your API's documentation](/docs/design-apis/specifications/view-live-documentation/) and [identifies syntax errors](/docs/design-apis/specifications/validate-a-component-file).

Your teammates can't reuse components in a draft component file. [Publish a version of a component file](#version-and-publish-a-component-file) to allow your teammates to reference its components in their specifications.

## Postman Vault integrations

Integrate your Postman Vault with Postman Flows to enable you to:

* Create Meeting
* Update Meeting
* Get Meeting
* Get Meeting By ID
* Delete Meeting
* Add Meeting Registrant
* Get Meeting Registrant
* Delete Meeting Registrant
* Get Recording By Meeting ID
* Search Recording
* Create Folder
* Move Folder
* Get Folder By ID
* Search Folders
* Delete Folder
* Download File

To connect your Postman Vault to a Postman Flows action, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Zoom** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Postman Vault.
6. Connect the **Request** block's output ports to the Zoom **Connector** block's input ports, based on the selected operation.
7. Connect the Zoom **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Azure API Gateway to Postman Flows

To connect your Azure API Gateway to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Azure Gateway** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Azure Gateway.
6. Connect the **Request** block's output ports to the Azure Gateway **Connector** block's input ports, based on the selected operation.
7. Connect the Azure Gateway **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Amazon API Gateway to Postman Flows

To connect your Amazon API Gateway to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Amazon API Gateway** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Amazon API Gateway.
6. Connect the **Request** block's output ports to the Amazon API Gateway **Connector** block's input ports, based on the selected operation.
7. Connect the Amazon API Gateway **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Google API Client to Postman Flows

To connect your Google API Client to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Google API Client** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Google API Client.
6. Connect the **Request** block's output ports to the Google API Client **Connector** block's input ports, based on the selected operation.
7. Connect the Google API Client **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Microsoft Graph to Postman Flows

To connect your Microsoft Graph to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Microsoft Graph** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Microsoft Graph.
6. Connect the **Request** block's output ports to the Microsoft Graph **Connector** block's input ports, based on the selected operation.
7. Connect the Microsoft Graph **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Microsoft Teams to Postman Flows

To connect your Microsoft Teams to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Microsoft Teams** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Microsoft Teams.
6. Connect the **Request** block's output ports to the Microsoft Teams **Connector** block's input ports, based on the selected operation.
7. Connect the Microsoft Teams **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector** block's input ports, based on the selected operation.
7. Connect the Slack **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

## Connect your Slack to Postman Flows

To connect your Slack to Postman Flows, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click the **Template** block and click \u003cimg alt=\"Delete icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon\" width=\"16px\"\u003e **Delete**.
3. Right-click the canvas and select **Slack** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Slack.
6. Connect the **Request** block's output ports to the Slack **Connector