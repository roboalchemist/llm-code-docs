# The Evaluate block

![Evaluate block](https://assets.postman.com/postman-docs/v11/evaluate-block-v11.jpg)

The **Evaluate** block is a powerful tool for manipulating and evaluating data. It's ideal for filtering data, conditionally running parts of your flow, and integrating complex logic.

Using [TypeScript](/docs/postman-flows/typescript/typescript-overview/) scripts or [Flows Query Language](/docs/postman-flows/flows-query-language/introduction-to-fql/) (FQL) queries, you can set up the **Evaluate** block to process data and send the result. The **Evaluate** block has pre-defined snippets to help you create FQL queries.

## Input

**variable** - Accepts data from another block's output port.

## Output

**Result** - Sends the result of the script or query.

## Setup

The **Evaluate** block processes data it receives from its input ports and inserted [data blocks](/docs/postman-flows/reference/overview-data-blocks/).

When created, the **Evaluate** block has one input port. When you connect another block to this port, the **Evaluate** block inserts a **Select** block and assigns the selected value to a variable named **value1**. To rename the variable, click it and enter a new name.

You can also change the inserted **Select** block to a different data block by clicking the ![Flows select icon](https://assets.postman.com/postman-docs/aether-icons/action-flowsSelect-stroke.svg#icon) **Select** block's icon and choosing a data block from the dropdown list.

You can also insert more variable data blocks into the **Evaluate** block to process their data. For example, you could insert a **String** block into your **Evaluate** block, name the variable `string1`, and reference it in your query as `string1`. Click ![Add data blocks](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add data blocks** to insert a data block into your **Evaluate** block.

The **Evaluate** block has a text box where you can enter TypeScript to create scripts or FQL to create queries. Click the dropdown list at the top of the block to set the text box to use TypeScript or FQL. Then click inside the text box and enter your code. When the text box is set to use FQL, you can click **Snippets** and choose from a list of common tasks.

In a flow module or action, you can't modify environment variables, including by using scripts in **Evaluate** blocks.

## Example

To see the **Evaluate** block in an example flow, check out [Flow Snippets: Evaluate](https://www.postman.com/postman/flows-snippets/flow/63bc960882ae416b9e6bc11f).

## Related blocks

You can use the [**Condition**](/docs/postman-flows/reference/blocks/condition/) and [**If**](/docs/postman-flows/reference/blocks/if/) blocks instead, depending on your use case.

You can insert the following blocks into the **Evaluate** block to process their data including the [**String**](/docs/postman-flows/reference/blocks/string/), [**Bool**](/docs/postman-flows/reference/blocks/bool/), [**Number**](/docs/postman-flows/reference/blocks/number/), [**Null**](/docs/postman-flows/reference/blocks/null/), [**Select**](/docs/postman-flows/reference/blocks/select/), [**Now**](/docs/postman-flows/reference/blocks/now/), [**Date**](/docs/postman-flows/reference/blocks/date/), [**Date \u0026 Time**](/docs/postman-flows/reference/blocks/date-and-time/), [**List**](/docs/postman-flows/reference/blocks/list/), [**Record**](/docs/postman-flows/reference/blocks/record/), and [**Get Variable**](/docs/postman-flows/reference/blocks/get-variable/) blocks.

## Related pages

For tutorials that use the **Evaluate** block, see the following:

* [Calculate the years since a milestone](/docs/postman-flows/tutorials/beginner/calculate-years-since-milestone/)
* [Create a count-based loop with the Repeat block](/docs/postman-flows/tutorials/beginner/create-count-based-loop/)
* [Create a dashboard using Postman Flows](/docs/postman-flows/tutorials/advanced/create-a-dashboard-in-flows/)
* [Create a list-based loop with the For block](/docs/postman-flows/tutorials/beginner/create-list-based-loop/)
* [Send information from one system to another using Postman Flows](/docs/postman-flows/tutorials/advanced/send-information-from-one-system-to-another/)

## Troubleshoot vault secrets

You can reference vault secrets stored in your Postman Vault by adding a vault secret inside double curly braces (`{{vault:secret-name}}`) and appending the prefix `vault:` to the vault secret's name. For example, to reference a vault secret named "postman-api-key", use the following syntax:

```txt
{{vault:postman-api-key}}
```

To reference a vault secret in your local instance of Postman, use the `vault:` prefix in the vault secret name. For example, if you copied the vault secret value from the Postman Vault and saved it as a variable in your Postman environment, you can use the following syntax:

```txt
{{vault:your_variable_name}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret in a Postman workspace, you can use the following syntax:

```txt
{{vault:your_workspace_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman collection. For example, if you wanted to reference a vault secret in a Postman collection, you can use the following syntax:

```txt
{{vault:your_collection_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman environment. For example, if you wanted to reference a vault secret in a Postman environment, you can use the following syntax:

```txt
{{vault:your_environment_name/postman-api-key}}
```

You can also use the `vault:` prefix in the vault secret name to reference a vault secret in a Postman workspace. For example, if you wanted to reference a vault secret