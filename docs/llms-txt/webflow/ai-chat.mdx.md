# Source: https://developers.webflow.com/mcp/v1.0.0-beta/reference/utility-tools/ai-chat.mdx

***

title: AI Chat
description: >-
Query Webflow's API documentation using natural language through an AI-powered
chat interface.
---------------

The AI Chat tool provides an intelligent interface for asking questions about Webflow's API documentation. Instead of manually searching through docs, you can ask natural language questions and receive relevant, contextual answers.

## When to use

Use the AI Chat tool when you need to:

* **Learn about Webflow APIs**: Ask questions about specific endpoints, parameters, or capabilities
* **Find documentation**: Locate relevant docs for a specific feature or use case
* **Understand workflows**: Get guidance on how to accomplish complex tasks
* **Troubleshoot issues**: Ask for help understanding error messages or unexpected behavior

<Tip>
  The AI Chat tool searches Webflow's complete API documentation, including Data API, Designer API, and best practices.
</Tip>

## Tool details

**Tool name**: `ai_chat`

**Parameters**:

| Parameter | Type   | Required | Description                                         |
| --------- | ------ | -------- | --------------------------------------------------- |
| `message` | string | Yes      | Your question about Webflow's APIs or documentation |

## How it works

When you invoke the AI Chat tool:

1. Your question is sent to Webflow's documentation AI system
2. The AI searches across all Webflow API documentation
3. Relevant context is identified and synthesized
4. A comprehensive answer is streamed back to your AI agent
5. Your agent can then apply the knowledge to your task

<Note>
  The AI Chat tool has access to up-to-date Webflow documentation, including recent changes and new features.
</Note>

## Example usage

### Basic documentation query

Ask about a specific API endpoint:

```
How do I create a new CMS collection using the Data API?
```

The AI will provide information about the collections endpoint, required parameters, and example requests.

### Complex workflow

Ask about multi-step processes:

```
What's the best way to migrate CMS items from one collection to another while preserving field mappings?
```

The AI will explain the workflow, relevant tools, and potential gotchas.

### Troubleshooting

Get help with errors:

```
I'm getting a 403 error when trying to update collection items. What could be wrong?
```

The AI will explain common causes of 403 errors and how to resolve them.

## Best practices

<Accordion title="Ask specific questions">
  Be clear and specific about what you want to know:

  **Good**: "What parameters does the create element tool accept?"

  **Better**: "How do I create a div element with a specific class using the Designer API?"
</Accordion>

<Accordion title="Include context when relevant">
  If you're working on a specific task, mention it:

  "I'm building a component that needs to update styles across multiple breakpoints. How should I approach this with the Designer API?"
</Accordion>

<Accordion title="Follow up for clarity">
  If the initial answer isn't complete, ask follow-up questions:

  "Can you show me a specific example of updating a style property at the tablet breakpoint?"
</Accordion>

## Limitations

* **Documentation scope**: Only has access to Webflow API documentation, not general web development questions
* **Real-time data**: Cannot access your actual site data or current state
* **No execution**: Provides information but doesn't execute API calls

<Warning>
  Always verify information from AI Chat against the official API reference documentation for critical implementations.
</Warning>

## Related tools

<Cards>
  <Card
    title="Rules"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Resources.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Resources.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/utility/rules"
  >
    Get guidelines and best practices for using Webflow tools
  </Card>

  <Card
    title="Sites"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Globe.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Globe.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/data/sites"
  >
    List and manage your Webflow sites
  </Card>

  <Card
    title="Elements"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Elements.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Elements.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/elements"
  >
    Create and modify elements on the canvas
  </Card>
</Cards>
