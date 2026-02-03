# The Condition block

![Condition block](https://assets.postman.com/postman-docs/v11/flows-condition-block-v11-50.jpg)

The **Condition** block is a logical gate that routes data through one of multiple output ports based on the results of one or more conditions. It assigns incoming data to variables and checks the variables against a series of true/false expressions you provide. You can write the expressions using [TypeScript](/docs/postman-flows/typescript/typescript-overview/) or [Flows Query Language](/docs/postman-flows/flows-query-language/introduction-to-fql/) (FQL).

Each condition has an output port. The first condition that returns true sends the data from its corresponding output port. If no conditions return true, the data is routed through the **Default** output port. By combining multiple conditions, a single **Condition** block can do the work of multiple [**If**](/docs/postman-flows/reference/blocks/if/) or [**Evaluate**](/docs/postman-flows/reference/blocks/evaluate/) blocks.

## Inputs

**variable** - You can connect a block to this input port or [insert](/docs/postman-flows/reference/blocks/overview/#insert-data-blocks-into-other-blocks) a data block to assign data to a [variable](/docs/sending-requests/variables/variables-intro/). You can then reference the variable in your expressions. You can also click ![Add data blocks](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add data blocks** to insert a data block into the **Condition** block. You can change an inserted block to a different data block by clicking the inserted block's icon and selecting a different block from the dropdown list.

**Condition <number>** - Enter a true/false expression here using TypeScript or FQL. Click the dropdown list at the top of the block to select TypeScript or FQL. Click ![Add condition](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add condition** to add another **Condition** field. To rename a condition, hover over the condition's name and click ![Edit icon](https://assets.postman.com/postman-docs/aether-icons/action-edit-stroke.svg#icon) **Edit Title**. To delete a condition, hover over it and click ![Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon).

## Outputs

The first condition that evaluates to true routes the input data through its output port, and the block stops checking conditions. For example, if **Condition 1** evaluates to false and **Condition 2** evaluates to true, the input data is routed through the **Condition 2** output port. Once a condition returns true, no other conditions are checked. If no conditions are true, the input data is routed through the **Default** output port.

## Setup

1. To receive and evaluate data from another block in your flow, connect the **variable** input port to the other block's output port.
2. (Optional) To [insert](/docs/postman-flows/reference/blocks/overview/#insert-data-blocks-into-other-blocks) a block and evaluate its data, click ![Add data blocks](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add data blocks** then select a block from the dropdown list. You can reference the inserted block's value as a variable in your true/false expressions. To rename the variable, click the inserted block's name and enter a new name.
3. Click the dropdown list next to the block's title and select **TypeScript** or **FQL**.
4. Enter your true/false expression in the text box.
5. (Optional) Click ![Add condition](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add condition** to add another condition and enter an expression.

## Example

To see the **Condition** block in an example flow, check out [Flow Snippets: Condition](https://www.postman.com/postman/flows-snippets/flow/677c1263c3b62c003d81e9f8).

## Related blocks

* [**Evaluate**](/docs/postman-flows/reference/blocks/evaluate/)
* [**If**](/docs/postman-flows/reference/blocks/if/)

You can insert the following blocks into the **Condition** block to evaluate their data:

* [**Bool**](/docs/postman-flows/reference/blocks/bool/)
* [**Date**](/docs/postman-flows/reference/blocks/date/)
* [**Date & time**](/docs/postman-flows/reference/blocks/date-and-time/)
* [**Get Configuration**](/docs/postman-flows/reference/blocks/get-configuration/)
* [**Get Variable**](/docs/postman-flows/reference/blocks/get-variable/)
* [**List**](/docs/postman-flows/reference/blocks/list/)
* [**Now**](/docs/postman-flows/reference/blocks/now/)
* [**Null**](/docs/postman-flows/reference/blocks/null/)
* [**Number**](/docs/postman-flows/reference/blocks/number/)
* [**Record**](/docs/postman-flows/reference/blocks/record/)
* [**Select**](/docs/postman-flows/reference/blocks/select/)
* [**String**](/docs/postman-flows/reference/blocks/string/)