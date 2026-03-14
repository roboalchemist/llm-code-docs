# Source: https://pipedream.com/docs/workflows/building-workflows/build-with-ai.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build with AI

> Build, configure, test and deploy Pipedream workflows with AI in String.com

## Create with AI

Build new agents and automations using AI at [String.com](https://string.com).

<Frame>
  <img src="https://mintcdn.com/pipedream/2iCuK7QAKkz01qI8/workflows/building-workflows/images/string-com.png?fit=max&auto=format&n=2iCuK7QAKkz01qI8&q=85&s=08f36904f278ac51439e08131daf10ca" alt="String.com interface for creating new agents and automations" width="979" height="605" data-path="workflows/building-workflows/images/string-com.png" />
</Frame>

## Edit Existing Workflows with AI

Click the **Edit with AI** button in the header of the builder or inspector.

<Frame>
  <img src="https://mintcdn.com/pipedream/2iCuK7QAKkz01qI8/workflows/building-workflows/images/edit-workflow-with-ai.png?fit=max&auto=format&n=2iCuK7QAKkz01qI8&q=85&s=95cfbe7e6aab0c0f081b401472e28dc0" alt="Edit with AI button in workflow header" width="2258" height="1269" data-path="workflows/building-workflows/images/edit-workflow-with-ai.png" />
</Frame>

Within any code step, click the **Edit with AI** button.

<Frame>
  <img src="https://mintcdn.com/pipedream/2iCuK7QAKkz01qI8/workflows/building-workflows/images/edit-code-with-ai.png?fit=max&auto=format&n=2iCuK7QAKkz01qI8&q=85&s=f688506ce7b900bc57fda3d6157143f5" alt="Edit with AI button in code step" width="870" height="575" data-path="workflows/building-workflows/images/edit-code-with-ai.png" />
</Frame>

When you encounter an error in your workflow, click the **Debug with AI** button in the step results to get AI-powered debugging assistance.

<Frame>
  <img src="https://mintcdn.com/pipedream/2iCuK7QAKkz01qI8/workflows/building-workflows/images/debug-with-ai.png?fit=max&auto=format&n=2iCuK7QAKkz01qI8&q=85&s=3c4a44701bce2d126670533c7fd7a218" alt="Debug with AI button in error results" width="869" height="732" data-path="workflows/building-workflows/images/debug-with-ai.png" />
</Frame>

## Limitations

Workflows with the following features cannot be edited in String.com:

* **Control flow** - Workflows using if/else, switch, or other control flow steps
* **GitHub Sync** - Workflows synchronized with GitHub repositories
* **Python code steps** - Workflows containing Python code (Node.js is supported)
* **Pipedream Connect** - Workflows using Pipedream Connect features
* **Multiple triggers** - Workflows with more than one trigger

## Working in String.com

Once you click any of the Edit with AI buttons, you'll be redirected to String.com where you can:

### Edit Your Workflow

Use natural language to describe the changes you want to make to your workflow:

* Add new steps or modify existing ones
* Change the logic or flow of your workflow
* Integrate new services or APIs
* Optimize performance and error handling

### Configure Steps

The AI assistant helps you:

* Set up authentication and connections
* Configure step parameters and options
* Map data between steps
* Handle edge cases and errors

### Test Your Changes

String.com provides a comprehensive testing environment where you can:

* Run test executions with sample data
* Debug issues in real-time
* Preview results before deployment
* Iterate quickly based on test outcomes

### Deploy to Production

Once you're satisfied with your changes:

* Deploy directly from String.com to your Pipedream account
* Changes are automatically synced
* Your workflow is ready to run in production

## Best Practices

### Clear Instructions

When working with AI in String.com, provide clear and specific instructions:

<Tip>
  **Good prompt**: "Add error handling to the HTTP request step that retries 3 times with exponential backoff when receiving a 429 status code"

  **Less effective**: "Fix the error handling"
</Tip>

### Iterative Development

Work iteratively with the AI:

1. Start with high-level requirements
2. Test and validate each change
3. Refine based on results
4. Deploy when ready

## Related Resources

<CardGroup cols={2}>
  <Card title="Workflow Basics" icon="book" href="/workflows">
    Learn the fundamentals of Pipedream workflows
  </Card>

  <Card title="Code Steps" icon="code" href="/workflows/building-workflows/code">
    Understanding code steps in workflows
  </Card>

  <Card title="Error Handling" icon="shield-exclamation" href="/workflows/building-workflows/errors">
    Best practices for error handling
  </Card>

  <Card title="Video Tutorials" icon="video" href="https://www.youtube.com/c/pipedreamhq">
    Watch tutorials on workflow development
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
