# Source: https://dev.writer.com/blueprints/textgeneration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Text generation

Generates text using a Writer model. Use for completions, summaries, or creative writing.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=25b22fc709f4cb902f4cf166e5c6e06e" alt="" data-og-width="2192" width="2192" data-og-height="1464" height="1464" data-path="images/agent-builder/blueprints/text-generation-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=87379f398e58948a9e89499f6187cfb3 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8ff88604171bc1341fc8fe49ebef991d 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=da534fe1173e8371db73875a2ea8b14a 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2c4afb581fdfef9447fa61acaf0079c6 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2d45daa87bd180b3475bdb492819057e 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b3f921e41522f0470aea0be4e8cff382 2500w" />

## Overview

The **Text generation** block generates text using a Palmyra model. Use it for text completions, summaries, creative writing, and more. You provide a prompt, and the model generates a response based on your instructions.

You can control the creativity of the output using the temperature setting, and limit the length with the max output tokens field.

## Common use cases

* Generating summaries or explanations
* Creative writing such as stories, marketing copy, and abstracts
* Expanding or rewriting text
* Answering questions based on a prompt

## How it works

1. **Prompt**: Enter the text or instructions for the model.
2. **Model**: Select the model to use for generation. Learn more about [the suite of Palmyra models](/home/models).
3. **Temperature**: Adjusts randomness and creativity. A higher temperature value like 0.7-1.0 makes the output more creative, while a lower temperature value like 0.0-0.3 makes it more deterministic.
4. **Max output tokens**: Sets the maximum length of the generated text.

The block sends the prompt and settings to the model, which returns the generated text as output.

## Examples

### Content creation workflow

This example shows a marketing workflow where user input is transformed into professional marketing copy.

**Blueprint Flow:**

1. **UI Trigger** → Marketing team submits product details through form
2. **Text generation** → Creates product description based on input
3. **Set state** → Stores generated content for review and approval in the interface

**Block Configuration:**

* **Prompt:** "Create a compelling product description for a @{product_name} that highlights its @{key_features}. Target audience: @{target_audience}. Tone: professional but approachable."
* **Model:** `palmyra-x5`
* **Temperature:** `0.7`

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0de274488bad6f873e8827ca24a9752d" alt="" data-og-width="2180" width="2180" data-og-height="1434" height="1434" data-path="images/agent-builder/blueprints/text-generation-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=19202ba74f7d7d8d7585f17fe85ec717 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=660875c818a785f7f7c94f2894efadb0 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d5473703e5b2a6f7fa7d0cae065b9d04 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0a9b616761a68da88bae2ac2fa39bc9d 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d3c12e300cf36e7bc8a8ce930d558fe8 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=26062a29cbcbdae5b5347021e5e505a2 2500w" />

This workflow automates content creation while ensuring appropriate tone and messaging for different marketing channels.

### Customer support response system

This example demonstrates an automated support system that generates personalized responses based on customer inquiries.

**Blueprint Flow:**

1. **UI Trigger** → Customer submits support ticket
2. **Classification** → Categorizes the issue type
3. **Text generation** → Creates personalized response based on category
4. **Set state** → Stores response for customer to display in the interface

**Block Configuration:**

* **Prompt:** "Generate a helpful and empathetic response for a customer unable to log into their @{product}. Address common login troubleshooting steps like password reset, browser cache clearing, and two-factor authentication issues. Include links to our password reset tool and support documentation. If these steps don't resolve the issue, provide instructions for escalating to our technical support team."
* **Model:** `palmyra-x5`
* **Temperature:** `0.4`

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2aa360886c3ed6a03a2c5dcaabc82e5e" alt="" data-og-width="2812" width="2812" data-og-height="1598" height="1598" data-path="images/agent-builder/blueprints/text-generation-support-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3220fc4260f7964253d77b666c091624 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=bc72bbf6c09a36ed7df59f37c03a2324 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=606adc394eb89c29cd76f843aa7b7b26 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ad9274d093086606de59368f3f8c2ce9 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0ad1673ecfe86013b733aa6f60707de7 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/text-generation-support-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=fdba4ed64177ddefd4130d296c31bc1b 2500w" />

This workflow provides automated, personalized customer support responses while maintaining human-like empathy and helpfulness.

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
      <td>Prompt</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Model</td>
      <td>Model Id</td>
      <td>-</td>

      <td>
        <code>palmyra-x5</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Temperature</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <code>0.7</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Range:
        0    to  1
      </td>
    </tr>

    <tr>
      <td>Max output tokens</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <code>1024</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Range:
        1    to  16384
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
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>Text was generated successfully.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error generating text.</td>
    </tr>
  </tbody>
</table>

The **Text generation** block returns the generated text as output. You can access this value in the following block as `@{result}`.
