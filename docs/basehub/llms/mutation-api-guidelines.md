# Mutation API Guidelines

> Learn how to create, update, and delete content in BaseHub using the Mutation API with detailed examples and best practices.

The Mutation API allows you to programmatically create, update, and delete content in your BaseHub repository. This guide covers all operation types with detailed examples and best practices.

## Operation Types

You can perform three types of operations:

*   `create`: Add new blocks
    
*   `update`: Modify existing blocks
    
*   `delete`: Remove blocks
    

## Create Operations

### Create a Text Block

```
{
  "parentId": "<layout-block-id>",
  "data": [{
    "type": "text",
    "title": "Hero Title",
    "value": "A purpose-built tool for planning and building products",
    "isRequired": true
  }]
}
```

In general, you'll want to mark all blocks as required.

### Create a Component Block

```
{
  "parentId": "<layout-block-id>",
  "data": [{
    "transactionId": "cta-component",
    "type": "component",
    "title": "CTA",
    "hidden": true,
    "value": [
      {
        "type": "text",
        "title": "Label",
        "value": "",
        "isRequired": true
      },
      {
        "type": "text",
        "title": "Href",
        "value": "",
        "isRequired": true
      },
      {
        "type": "select",
        "title": "Variant",
        "value": ["primary"],
        "acceptedValues": ["primary", "secondary", "ghost"],
        "multiple": false,
        "isRequired": true,
        "description": "We'll style the button based on the variant"
      }
    ]
  }]
}
```

Notice how we're not using `children` for nesting, but rather, we just use the `value` field, which in the case of layout blocks, accept an array of blocks.

### Create an Instance Block

```
{
  "parentId": "<layout-block-id>",
  "data": [{
    "type": "instance",
    "title": "Sign Up Button",
    "mainComponentId": "cta-component",
    "value": {
      "label": {
        "type": "text",
        "value": "Sign Up for Free"
      },
      "href": {
        "type": "text",
        "value": "/sign-up"
      },
      "variant": {
        "type": "select",
        "value": ["primary"]
      }
    }
  }]
}
```

Key points about instances:

*   We use `mainComponentId` to reference the component
    
*   The instance's `value` field is an object defining values via their API Names
    

### Create a Collection Block

```
{
  "parentId": "<layout-block-id>",
  "data": [{
    "type": "collection",
    "title": "Authors",
    "template": [
      {
        "type": "text",
        "title": "Role",
        "isRequired": true
      },
      {
        "type": "media",
        "title": "Avatar",
        "isRequired": true
      }
    ],
    "rows": [
      {
        "type": "instance",
        "title": "Frank Ocean",
        "value": {
          "role": {
            "type": "text",
            "value": "Musician"
          },
          "avatar": {
            "type": "media",
            "value": {
              "url": "https://assets.basehub.com/example.jpg",
              "fileName": "frank-ocean-avatar.jpg",
              "altText": "Frank Ocean"
            }
          }
        }
      }
    ]
  }]
}
```

### Create a Workflow Block

Workflow blocks enable automation in your BaseHub repository. They define triggers and actions that execute automatically when certain conditions are met.

```
{
  "parentId": "<layout-block-id>",
  "data": [{
    "type": "workflow",
    "title": "Author Bio Update Workflow",
    "value": {
      "trigger": {
        "type": "layout-block",
        "blocks": [
            "<trigger-block-id>", "<trigger-block-id>"
        ],
        "events": [ "updated" ]
      },
      "actions": [
        {
          "type": "webhook",
          "url": "https://<your-url>.com/api/notify"
        },
        {
          "type": "notification",
          "userIds": ["<user-id>"]
        },
        {
          "type": "ai-autofill",
          "block": "<block-to-autofill>",
          "prompt": "Complete the bio based on the title",
          "changeType": "direct"
        }
      ]
    }
  }]
}
```

Key components of a workflow:

*   `trigger`: Defines when the workflow should execute
    
*   `actions`: Array of actions to execute when triggered
    

#### Workflow Triggers

**Layout Block Trigger**: Triggers when specific blocks are modified

```
"trigger": {
  "type": "layout-block",
  "blocks": ["block-id-1", "block-id-2"],
  "events": ["created", "updated", "deleted"]
}
```

*   `blocks`: Array of block IDs to watch. **The must be siblings:** Have the same parent layout block.
    
*   `events`: Array of events (`created`, `updated`, `deleted`)
    

#### Workflow Actions

**Webhook Action**: Sends an HTTP POST request to a specified URL

```
{
  "type": "webhook",
  "url": "https://your-api.com/webhook"
}
```

**Notification Action**: Sends in-app notifications to specified users

```
{
  "type": "notification",
  "userIds": ["user-id-1", "user-id-2"]
}
```

**AI Autofill Action**: Uses AI to automatically fill block content

```
{
  "type": "ai-autofill",
  "block": "target-block-id",
  "prompt": "Generate content based on context",
  "changeType": "direct" | "suggestion" | "auto-commit"
}
```

*   `direct`: Automatically applies the AI-generated content
    
*   `suggestion`: Creates a suggestion for manual approval
    
*   `auto-commit` : Applies the content and auto-commits that specific change
    

**AI Autofill Variant Action**: Uses AI to fill variant-specific content

```
{
  "type": "ai-autofill-variant",
  "changeType": "direct" | "suggestion" | "auto-commit", 
  "block": "variant-set-block-id",
  "prompt": "Generate localized content"
}
```

## Update Operations

### Update a Text Block

```
{
  "data": [{
    "id": "<block-id>",
    "title": "Updated Title",
    "value": {
      "role": {
        "type": "text",
        "value": "Producer and Podcast Host"
      }
    }
  }]
}
```

### Update a Workflow Block

When updating a workflow, you can modify the trigger conditions, add/remove actions, or change action parameters:

```
{
  "data": [{
    "id": "workflow-id",
    "type": "workflow",
    "value": {
      "trigger": {
        "type": "layout-block",
        "blocks": [
          "trigger-block-id"
        ],
        "events": [
          "updated"
        ]
      },
      "actions": [
        {
          "type": "webhook",
          "url": "https://your-api.com"
        },
        {
          "type": "notification",
          "userIds": []
        },
        {
          "type": "ai-autofill-variant",
          "changeType": "suggestion",
          "block": "variant-set-block-id",
          "prompt": ""
        },
        {
          "type": "ai-autofill",
          "block": "block-to-auto-fill",
          "prompt": "Complete the bio based on the title",
          "changeType": "direct"
        }
      ]
    }
  }]
}
```

### Update with Variants

```
{
  "data": [{
    "id": "<block-id>",
    "value": {
      "heroTitle": {
        "type": "text",
        "variantOverrides": {
          "language-es": {
            "value": "Finalmente, un CMS que se mueve tan rápido como tú."
          }
        }
      }
    }
  }]
}
```

## Primitive Block Value Formats

Here are all primitive block types and their corresponding value formats:

*   **text**: `{ "type": "text", "value": "string content" }`
    
*   **number**: `{ "type": "number", "value": 123 }`
    
*   **boolean**: `{ "type": "boolean", "value": true }`
    
*   **date**: `{ "type": "date", "value": "2025-03-07" }`
    
*   **color**: `{ "type": "color", "value": "#RRGGBB" }`
    
*   **media**: `{ "type": "media", "value": { "url": "...", "fileName": "...", "altText": "..." } }`
    
*   **reference (single)**: `{ "type": "reference", "value": "block-id" }`
    
*   **reference (multiple)**: `{ "type": "reference", "multiple": true, "value": ["block-id-1", "block-id-2"] }`
    
*   **event**: `{ "type": "event", "value": { "schema": {}, "view": 'table' | 'chart' } }`
    
*   **workflow**: `{ "type": "workflow", "value": { "trigger": {}, "actions": [] } }`
    

## Rich Text Format

```
{
  "type": "rich-text",
  "value": {
    "format": "json",
    "value": [...] // ProseMirror-compatible JSON
  }
}
```

## Code Snippet Format

```
{
  "type": "code-snippet",
  "value": {
    "code": "const hello = 'world';",
    "language": "javascript"
  }
}
```

## Workflow Block Best Practices

*   **Be specific with triggers**: Only watch the blocks that are relevant to your automation
    
*   **Use meaningful titles**: Name your workflows descriptively for easier management
    
*   **Test AI prompts**: Use `suggestion` changeType first to verify AI outputs before switching to `direct`
    
*   **Order actions logically**: Actions execute in sequence, so plan the order carefully
    
*   **Validate webhook endpoints**: Ensure your webhook URLs are accessible and handle BaseHub's payload format
    

## Common Mutation API Errors

### Rich Text Formatting Mismatch

Passing `format: "json"` with a markdown string will result in an error. You should pass a Rich Text JSON object instead.

### Workflow Validation Errors

*   **Invalid block IDs**: Ensure all referenced block IDs exist in your repository
    
*   **Missing required fields**: Each action type has required fields that must be provided