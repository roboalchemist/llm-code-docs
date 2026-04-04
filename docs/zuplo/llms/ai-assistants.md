# Source: https://www.zuplo.com/docs/dev-portal/zudoku/configuration/ai-assistants.md

# AI Assistants

By default, Dev Portal shows "Use in Claude" and "Use in ChatGPT" options in dropdown menus on both
[API reference](./api-reference.md) and [documentation](./docs.md) pages. You can customize this
behavior using the top-level `aiAssistants` configuration.

## Disable AI Assistants

To remove all AI assistant options:

```ts title=zudoku.config.ts
const config = {
  aiAssistants: false,
  // ...
};
```

## Use Only Specific Presets

```ts title=zudoku.config.ts
const config = {
  aiAssistants: ["claude"], // Only show Claude
  // ...
};
```

Available presets: `"claude"`, `"chatgpt"`

## Add Custom AI Assistants

You can add custom entries with a label and URL. Use `{pageUrl}` as a placeholder in the URL string,
or provide a callback for full control:

```ts title=zudoku.config.ts
const config = {
  aiAssistants: [
    "claude", // built-in preset
    {
      label: "Open in MyAI",
      // Simple string with placeholder
      url: "https://myai.com/?context={pageUrl}",
    },
    {
      label: "Open in CustomAI",
      // Callback for full control
      url: ({ pageUrl, type }) => {
        if (type === "openapi") {
          return `https://custom.ai/?q=${encodeURIComponent("Explain this API: " + pageUrl)}`;
        }
        return `https://custom.ai/?q=${encodeURIComponent("Explain this page: " + pageUrl)}`;
      },
    },
  ],
  // ...
};
```

The callback receives `{ pageUrl: string, type: "docs" | "openapi" }` so you can customize behavior
per context.
