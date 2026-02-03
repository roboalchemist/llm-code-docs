# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/set-variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Variable

> Learn about the Set Variable block and how to set it up in the Builder.

The Set Variable block is used to set the value of one or more variables. With it, you can modify variable values dynamically at any point in the flow.

## How to configure

1. Click on the Set Variable block in the canvas to open its settings.
2. Select the variable you want to modify.
3. Select the type of the modification:
   * **Value**: Set the variable to a specific value. You can also insert variables to make the value dynamic.
   * **Add/Subtract/Multiply/Divide**: Perform a mathematical operation on the variable. You can add, subtract, multiply, or divide the variable by a specific value. The value must be a number.
4. Enter the value.

<img src="https://chatling-assets.b-cdn.net/set-variable-block-settings.png" alt="Configure Set Variable block" width="350" />

## Multiple variables

You can set multiple variables at once by clicking on the **Add variable** button. This will add a new row where you can select another variable and set its value.

<img src="https://chatling-assets.b-cdn.net/add-additional-variable-to-set-variable-block.jpg" alt="Add additional variable" width="350" />

## Example

Let's say you're building a lead generation chatbot for a real estate brokerage. You want to prompt the AI to ask the customer three questions about their requirements and forward the answers to the team. You can do this by using a counter variable that increments each time the user answers a question.

Below is a sample flow that demonstrates how to use the Set Variable block.

<img src="https://chatling-assets.b-cdn.net/set-variable-real-estate-example-chatbot-flow-1.png" alt="Real estate sample chatbot flow using Set Variable block" />

We're using a variable called `counter` to keep track of the number of questions that have been asked. This variable is incremented by 1 each time the user answers a question.

Then, we're using the Condition block to check if the counter is greater or equal to 3. If it is, a message is displayed to inform the user that their inquiry has been forwarded to the team. Else, the AI asks the next question.
