# Build a "Hello, world" flow module

Postman Flows is a visual, low-code editor you can use to build almost any workflow you can imagine. With Postman Flows you can create *flow modules* that run locally, and [*actions*](/docs/postman-flows/build-flows/structure/actions/) that can be deployed in the Postman cloud.

In this tutorial, you'll create a two-block flow module that displays the text **Hello, world**. You'll learn how blocks and connections work and prepare yourself to build larger and more complex flows.

## Create a new flow module

With flows, you can create reusable flow components that can be added to multiple other flows. Then you can share your flows with teammates so they don't need to rebuild the same components.

You create flows in a workspace. Use workspaces to organize your API projects and collaborate with your team.

To create a new flow module, do the following:

1. Choose an existing workspace or [create a new one](/docs/collaborating-in-postman/using-workspaces/create-workspaces/).
1. In the upper left corner, click **New** \> ![Image 1: Flow icon](https://assets.postman.com/postman-docs/aether-icons/entity-flow-stroke.svg#icon) **Flow**.
1. In the sidebar, hover over the new flow module, click ![Image 2: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**, then select **Rename**.
1. Rename the flow module to **Hello, world**.
1. Press the **Return** or **Enter** key.

## Add a String block

Use the **String** block to define text, which you can send to another block.

To add a **String** block, do the following:

1. On the canvas toolbar, click ![Image 3: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Block**.
1. Select ![Image 4: String icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-string-stroke.svg#icon) **String**. You can also search for the block by entering "string" in the search box.
1. To the right of the **Start** block, click the canvas to place the **String** block in that location.
1. In the **String** block, enter the text **Hello, world**.

In the next procedure, you'll connect this block to a **Display** block to display your text.

## Connect a Display block

When you connect two blocks, you connect one block's input to another block's output. Inputs are on the block's left side and outputs are on its right side. The **Display** block displays incoming data, such as the **String** block's string value.

To connect a **Display** block, do the following:

1. Hover over the **String** block's output port. The pointer changes to a crosshair.
1. Drag the output port to the right of the **String** block to place the **Display** block in that location.
1. Select ![Image 5: Output icon](https://assets.postman.com/postman-docs/aether-icons/action-output-stroke.svg#icon) **Display**. You can also search for the block by entering "output" in the search box.

## Run the flow module

On the canvas toolbar, click ![Image 6: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Run**.

![Image 7: "Hello, world" flow](https://assets.postman.com/postman-docs/v11/postman-flows-build-your-first-flow-v11-40.jpg)

Congratulations! You built your first flow module and displayed **Hello, world** in a **Display** block.