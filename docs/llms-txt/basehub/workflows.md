# Workflows

> Automate content generation across your repository with AI-powered workflows.

![](https://assets.basehub.com/7b31fb4b/51ef68f5d02008617ad8c91ddc9d2a5c/cleanshot-2025-07-16-at-13.47.322x.png?width=3840&quality=90&format=auto)

Example of a workflow that narrates a changelog post.

You can trigger automated content updates with contextual prompts to let the AI agent know what to do when the workflow runs.

### Trigger

Use the **"A block changes"** trigger to run a workflow whenever a selected block is updated.

### Action

There are two types of actions your workflow can perform:

*   **AI Autofill**: Automatically generate or update a block’s content.
    
*   **Apply Variant**: Apply a predefined variant to a block.
    

## Get started

To get started, go anywhere in your Editor and add a new Workflow Block typing: `/workflow`

## How to configure

### Prerequisites

You’ll need:

*   At least one existing block to act as a **trigger**.
    
*   A **target block** where the generated content will go.
    

### Set the Trigger Type

In your workflow block, set the trigger to: **A block changes**

![](https://assets.basehub.com/7b31fb4b/3fd82ec307070af1d8e68830107d5f7c/screenshot-2025-07-16-at-12.37.30.png?width=3840&quality=90&format=auto)

### Select Trigger blocks

Choose the blocks that will activate the workflow when they change.

You’ll configure two selectors:

*   One for the **layout block**.
    
*   Another for the **child blocks** that will act as triggers.
    

![](https://assets.basehub.com/7b31fb4b/eb11a90ea2006f20ee92bb7dbfa91915/screenshot-2025-07-16-at-12.40.36.png?width=3840&quality=90&format=auto)

info:

**Important:** If you select a component, the trigger will also apply to all of its instances. This means you can set up a trigger in a list template and have the workflow generate content across all rows in that list.

### Define the Action

Choose the action type: **AI Autofill / Apply Variant**

Then select the **target block** where the generated content will be applied. The target block can only be a child of the selected layout block.

![](https://assets.basehub.com/7b31fb4b/cc5505f35200b6469a0d04a615b0b0c3/screenshot-2025-07-16-at-12.44.21.png?width=3840&quality=90&format=auto)

### Leave instructions for START

Prompt your AI agent with directives, and let them know if you want the content to be applied:

*   As draft changes.
    
*   In a content suggestion.
    
*   In a new commit.
    

![](https://assets.basehub.com/7b31fb4b/15a740ffa6035016a9b4c470b68d3911/screenshot-2025-07-16-at-12.45.43.png?width=3840&quality=90&format=auto)

### Monitor Workflow Runs

When a workflow is triggered, the **target block** will show a badge with the status in its label.

You can also track real-time workflow activity in the **Runs** section of the workflow block’s properties panel. Here, you can:

*   See the current status
    
*   Prevent, cancel, or retry workflow generations
    

![](https://assets.basehub.com/7b31fb4b/87e4194f637c7c03bb7f30c117bfe006/screenshot-2025-07-16-at-12.49.43.png?width=3840&quality=90&format=auto)

## Use cases

### Localize Docs or Product Pages

You can create a workflow to automatically translate the content of posts immediately after they change.

This "Translator" workflow, tells START to translate the content in the posts instances immediately after they change

### Summarize Longform Content

Automatically generate a summary every time an article, doc, or changelog post is updated.

### Generate Audio Narrations

Transform written content into audio.