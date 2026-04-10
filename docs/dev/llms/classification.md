# Source: https://dev.writer.com/blueprints/classification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Classification

Classifies text into predefined categories using AI. Useful for tagging and routing inputs.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ec739da593fcfde2b777230a94edde9d" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/classification-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=93b6de9e6842369da72aff10876e58be 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1f66d9273e0a6f515c44c6a56b1fb1f2 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=019a0afcbe0834ddd7b05a89c4f900e5 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=dc81bdd25ad74422e45ebe95c4dcd9d2 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5e4867e3c8304f44e9bc59bb900afc1b 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5063e897b8798f77e2528867841f6a2d 2500w" />

## Overview

The **Classification** block classifies text into predefined categories using AI. Unlike blocks that have a single "success" path (such as the [Tool calling block](/blueprints/toolcalling)), the Classification block creates multiple execution paths based on your defined categories. The workflow continues down the specific path that matches the classification result, not through a single return value or success state.

This makes the Classification block ideal for:

* Routing workflows based on content type, sentiment, or intent
* Tagging content into predefined categories
* Branching logic where different categories trigger different actions

For example, if you define categories like `urgent`, `normal`, and `low_priority`, the Classification block analyzes the input text and continues execution down the corresponding path (`urgent`, `normal`, or `low_priority`).

**Key difference from other blocks**: the Classification block doesn't have a final `success` state that takes a return value. Instead, it creates separate execution paths for each category you define, and the workflow continues down the path that matches the classification result.

The `@{result}` variable from the **Classification** block contains the name of the selected category.

## Common use cases

* **Customer support routing**: Classify support tickets as "Technical", "Billing", or "General" to route them to appropriate teams
* **Content moderation**: Categorize user submissions as "Appropriate", "Needs Review", or "Inappropriate"
* **Sentiment analysis**: Classify feedback as "Positive", "Negative", or "Neutral"
* **Document organization**: Sort documents by type such as "Invoice", "Contract", or "Report"
* **Lead qualification**: Classify sales inquiries as "Hot Lead", "Warm Lead", or "Information Request"

## How it works

1. **Input text**: Provide the text you want to classify (often from user input or previous block results)
2. **Define categories**: Set up category names and descriptions that help the AI understand what each category represents
3. **AI classification**: The block analyzes the text and determines which category best fits
4. **Routing**: The workflow automatically follows the connection path that matches the chosen category

## Example

The following example shows a **Classification** block that analyzes customer reviews to determine their primary focus, then routes to different response workflows based on the classification.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a3d6e488dbdd0db1909864a487e8f99d" alt="" data-og-width="3454" width="3454" data-og-height="1802" height="1802" data-path="images/agent-builder/blueprints/classification-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7af2b73c61ea77475f3193abd27f9a18 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6639e09ad91ac545973e222f549d572c 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6bc76d8e731527a07045b5aec1f31369 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=fbc02d9f7600461c32974a225e75743d 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=448a1093e97836006a82304ae87f9307 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-example.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5fc7567f5fc4d7a3b36081a61b92c71c 2500w" />

In this example, a customer review is classified into one of five categories:

* **Packaging**: Issues with how the product was packaged or shipped
* **Pricing**: Concerns about cost, value, or billing
* **Quality**: Problems or praise related to product quality
* **Delivery**: Issues with shipping speed or delivery process
* **Empty**: Reviews that don't contain useful feedback

Based on the classification, the workflow routes to different **Text generation** blocks that create appropriate responses for each category.

### Setting up categories

When configuring the **Classification** block, you define categories as key-value pairs:

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=dd15b27e025c2bfbf31229d7f731457d" alt="" data-og-width="1882" width="1882" data-og-height="1064" height="1064" data-path="images/agent-builder/blueprints/classification-categories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=43d14e3dc10c06ed83a7a5b38116f127 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4586313c5e44163207d1378d50a66e3d 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a9d34594379d3a83998285f0564bf71e 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e76e9da908d5dfbd6e0b9b349833a482 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6b63363e973793449d210c42fbcafcc2 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/classification-categories.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d506e7a882b92faa381d38e0f7ab839e 2500w" />

**Key**: The category name (this becomes the connection point name)\
**Value**: A description that helps the AI understand what belongs in this category

For the customer review example:

* **Quality**: "The review is about the quality of the product or service"
* **Pricing**: "The review discusses pricing concerns or satisfaction"
* **Delivery**: "The review relates to delivery time or issues"

### Using classification results

After classification, the workflow automatically follows the connection that matches the selected category. You can connect different blocks to each category to create specialized workflows.

The classification result is also available in subsequent blocks using `@{result}`, which contains the name of the selected category.

## Best practices

### Writing effective category descriptions

* **Be specific**: Include concrete examples of what should be classified in each category
* **Use clear language**: Avoid ambiguous terms that could apply to multiple categories
* **Consider edge cases**: Think about borderline cases and which category they should fall into
* **Test with real data**: Use actual examples from your use case to verify classifications are accurate

### Category naming

* **Use descriptive names**: Choose names that clearly indicate the category's purpose
* **Follow naming rules**: Category names should contain only letters, digits, underscores, and spaces
* **Keep it consistent**: Use a consistent naming convention across all categories
* **Avoid special characters**: Stick to alphanumeric characters for reliable connections

### Performance optimization

* **Provide context**: Use the "Additional context" field to give the AI more information for better classification
* **Handle edge cases**: Always include a "Other" or "Unknown" category for inputs that don't fit your main categories

### Adding context for better classification

Use the "Additional context" field to provide information that helps with classification:

```
Additional context: This is a product review for a high-end electronics item. Focus on technical aspects, build quality, and user experience when classifying.
```

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Text</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The text you want to classify.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Categories</td>
      <td>Key-Value</td>
      <td>-</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>The keys should be the categories you want to classify the text into, for example 'valid' and 'invalid', and the values are the criteria for each category. Category names should contain only letters of the English alphabet, digits, underscores, and spaces.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Additional context</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>Any additional information that might help the AI in making the classification decision.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>-</td>
      <td>categories</td>
      <td>dynamic</td>
      <td>-</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error classifying the text.</td>
    </tr>
  </tbody>
</table>

The `dynamic` end state means that the exact values of this end state change based on how you define the block.

The output of a **Classification** block is a string that contains the classification of the input text. You can access the output of a **Classification** block using the `@{result}` variable in the block that follows it in a blueprint.
