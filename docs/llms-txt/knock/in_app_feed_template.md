# Source: https://docs.knock.app/mapi-reference/templates/schemas/in_app_feed_template.md

### InAppFeedTemplate

An in-app feed template.

#### Attributes

- **action_buttons** (array) - The action buttons of the in-app feed message.
- **action_url** (string) - The URL to navigate to when the in-app feed is tapped. Can be omitted for multi-action templates, where the action buttons will be used instead.
- **markdown_body** (string) *required* - The markdown body of the in-app feed.

#### Example

```json
{
  "action_buttons": [
    {
      "action": "https://example.com",
      "label": "Button 1"
    }
  ],
  "action_url": "https://example.com",
  "markdown_body": "Hello, world!"
}
```

