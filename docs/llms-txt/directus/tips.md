# Source: https://directus.io/docs/raw/guides/ai/assistant/tips.md

# Best Practices

> Get the most out of AI Assistant with practical tips, example prompts, and common pitfalls to avoid.

Follow these tips to work effectively with AI Assistant and get better results from your conversations.

## Be Specific About Collections and Fields

The more specific you are, the better results you'll get.

**Less effective:**

> "Add a new post"

**More effective:**

> "Create a new article in the articles collection with title 'Getting Started with Directus', status 'draft', and assign it to the 'Tutorials' category"

## Complex Tasks

Break complex requests into smaller, more manageable steps:

1. "First, show me all products without descriptions"
2. "Now update product X with this description: ..."
3. "Next, do the same for product Y..."
4. "Finally, verify the products were updated correctly"

## Start Fresh for New Topics

Long conversations can lose context. When switching to a different task, clear the conversation and start fresh.

**Signs you should start a new conversation:**

- The AI seems confused about your schema
- Responses are becoming less relevant
- You're working on an unrelated task

## Configure Tool Approvals

- Read-only tools like Schema can safely be set to <icon className="text-success" name="material-symbols:check">



</icon>

 **Always Allowed**
- Keep write operations on <icon className="text-warning" name="material-symbols:approval-delegation">



</icon>

 **Needs Approval** until you're confident
- <icon className="text-error" name="material-symbols:block">



</icon>

 **Disable** tools you don't need to reduce token usage

See [Tool Behavior](/guides/ai/assistant/tools#tool-behavior) for more details.

## Use Context Effectively

Context attachments help the AI understand what you're working with. See [Adding Context](/guides/ai/assistant/usage#adding-context) for setup details.

**When to attach context:**

- Asking about or modifying specific items
- Comparing or batch-processing content
- Making AI-assisted edits in the Visual Editor
- Using prompts to maintain consistent formatting
- Asking the AI to analyze or describe images
- Providing reference documents (PDFs, text files) for content tasks
- Sharing audio or video files for transcription or analysis

**Keep in mind:**

- Maximum 10 context items per message
- Context is captured as a snapshot when sent
- Large items increase token usage

**Visual Editor tips:**

- Add multiple elements as context before sending a message
- Hover context cards to verify you've selected the right elements
- Add elements from different pages—context persists while navigating

**File attachment tips:**

- Use drag-and-drop for quick uploads from your desktop
- Select from the File Library when referencing existing assets
- Image files show previews; other types show a file icon
- Files are uploaded to your AI provider — review [Security](/guides/ai/assistant/security) for data handling details

### Context Example Prompts

**With Prompts attached:**

```text
Use the "Brand Voice" prompt to write a product announcement
```

```text
Apply the "SEO Description" template to this page
```

**With Items attached:**

```text
Compare these two products and highlight the differences
```

```text
Update this article to match the tone of the attached reference
```

**With Visual Elements attached:**

```text
Translate this section to French
```

```text
Make this paragraph more concise while keeping the key points
```

```text
Rewrite this heading to be more engaging
```

**With Files attached:**

```text
Describe what's in this image
```

```text
Summarize the key points from this PDF
```

```text
Transcribe this audio recording
```

## Manage Costs

AI Assistant requires API keys from OpenAI or Anthropic — you cannot use a ChatGPT Plus or Claude Pro subscription. API access is billed per token, so costs scale with usage. Be mindful of this, especially with larger models.

<callout color="warning" icon="material-symbols:paid">

**Disable tools you don't use.** Disabled tools are not loaded into context, reducing token usage and API costs. If you only work with content, disable schema modification tools.

</callout>

---

## Example Prompts by Use Case

### Content Management

```text
Show me all published articles from this month
```

```text
Create a new blog post titled "AI in Content Management" with status draft
```

```text
Update all products in the "Summer Sale" category to have a 20% discount tag
```

```text
Find articles without a featured image
```

### Schema Operations

```text
What fields does the products collection have?
```

```text
Add a "featured" boolean field to the articles collection
```

```text
Create a relationship between products and categories (many-to-many)
```

```text
Show me how the pages collection is structured
```

### Flow Automation

```text
List all active flows
```

```text
Create a flow that sends an email when a new order is placed
```

```text
Trigger the "Generate Report" flow for all products
```

### Data Exploration

```text
How many users signed up last week?
```

```text
Show me the 10 most recent orders
```

```text
What's the relationship between articles and authors?
```

```text
Find all items with status "pending review"
```

---

## Common Gotchas

### Permissions Apply

The AI operates with your user permissions. If you're receiving permissions errors in AI Assistant, it's likely the user account doesn't have the necessary permissions to perform the action.

### Deletions Require Extra Care

The AI is instructed to ask for confirmation before deleting items. However, LLMs don't always follow instructions perfectly — keep destructive tools on "Ask" approval mode if you want guaranteed confirmation before deletions.

### Related Data May Be Affected

When deleting items that have relationships, consider cascade behavior:

- Deleting an author may affect related articles
- Deleting a category may orphan products

The LLM may not always warn you about potential impacts.

---

## When AI Assistant Works Best

**Great for:**

- Exploring and understanding your schema
- Quick content operations (create, update, query)
- Setting up new collections and fields
- Triggering manual flows

**Consider other approaches for:**

- Very large bulk operations (use direct API or import / export through the Data Studio)
- Complex data migrations (use scripts or dedicated tools)
- Sensitive operations on production data (test in staging first)

## Next Steps

<card-group>
<card icon="material-symbols:construction" title="Available Tools" to="/guides/ai/assistant/tools">

See what actions the AI can perform.

</card>

<card icon="material-symbols:security" title="Security" to="/guides/ai/assistant/security">

Access control and data protection.

</card>
</card-group>
