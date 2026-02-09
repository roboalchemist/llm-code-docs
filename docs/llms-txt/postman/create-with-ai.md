# The Create with AI block

The **Create with AI** block is a [beta feature](https://www.postman.com/legal/terms/).

![Create AI block](https://assets.postman.com/postman-docs/v10/create-with-ai-block-v10.jpg)

The **Create with AI** block uses artificial intelligence (AI) models to generate text, images, and JSON data based on your plain-language prompts. For example, you could enter a prompt like "Create a profile picture for a random person" or "Write a welcome email for a new employee at Postman".

You can assign another block's output to the **Create with AI** block's built-in variable, or [insert](/docs/postman-flows/reference/blocks/overview/#insert-data-blocks-into-other-blocks) data blocks. You can then reference the variable or data block in your prompt using curly braces. To learn how, see [Setup](#setup).

The number of credits a **Create with AI** block consumes any given time that it runs depends on which model it's using. To learn more, see [How Flow modules and actions consume credits](/docs/billing/flows-usage/#how-flow-modules-and-actions-consume-credits).

## Input

Connect another block's output port to the **Create with AI** block's single input port to assign incoming data to a variable. Select the variable's name to edit it. Select ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add data blocks** to [insert](/docs/postman-flows/reference/blocks/overview/#insert-data-blocks-into-other-blocks) a data block into the **Create with AI** block. You can then assign a value to the data block and reference it in your prompt with curly braces like `{{this}}`.

## Output

The output port sends the data that the AI model creates. The symbol next to this output port changes depending on the type of data selected.

## Setup

You can set up the **Create with AI** block to generate text, images, or JSON. Select the type of content you want from the dropdown list next to the block's title. To let the block decide the type of content you want based on your prompt, select **Smart** from the dropdown list.

Click the text box to enter a prompt in plain language. Click **Run** to see how the block handles your prompt and if it needs to be reworded.

To insert a variable data block into your **Create with AI** block, click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add data blocks**. For example, you could insert a **String** block, name the variable `animal`, and reference it in a prompt like this: `Create an image of {{animal}}`. The **Create with AI** block generates an image of whatever animal is assigned to the variable `animal`. You can change an inserted block to a different data block by clicking the inserted block's icon and choosing a block from the dropdown list.

### Use Mustache syntax in AI prompts

The **Create with AI** block supports [Mustache](https://mustache.github.io/mustache.5.html) syntax. You can use Mustache to dynamically format prompts, iterate over arrays, conditionally display text, and more.

If a referenced variable in your AI prompt contains an object, Mustache syntax in the **Create with AI** block returns the full JSON representation of the object, including field names, rather than `[object Object]`.

### Change the AI model

To change the AI model and adjust its settings, do the following:

1. Click the **Create with AI** block, then click ![Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Additional Settings**.
2. Click ![Agent Mode icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-postbot-stroke.svg#icon) **AI Model**, then select a model from the list.
3. (Optional) Click **Predictability** or **Creativity** to adjust their settings for the selected AI model. You can use the slider to set them higher or lower. A higher predictability value increases the chances of results repeating under the same conditions. A higher creativity value returns results with more variety.

## Example

To see the **Create with AI** block in an example flow, check out [Flow Snippets: Create with AI](https://www.postman.com/postman/flows-snippets/flow/6841fce881d05a003f60123b).

## Related blocks

You can insert a number of blocks into the **Create with AI** block to process their data including the [**String**](/docs/postman-flows/reference/blocks/string/), [**Bool**](/docs/postman-flows/reference/blocks/bool/), [**Number**](/docs/postman-flows/reference/blocks/number/), [**Null**](/docs/postman-flows/reference/blocks/null/), [**Select**](/docs/postman-flows/reference/blocks/select/), [**Now**](/docs/postman-flows/reference/blocks/now/), [**Date**](/docs/postman-flows/reference/blocks/date/), [**Date \u0026 Time**](/docs/postman-flows/reference/blocks/date-and-time/), and [**Get Variable**](/docs/postman-flows/reference/blocks/get-variable/) blocks.