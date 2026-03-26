# Source: https://novel.mintlify.dev/docs/components/editor-bubble-item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novel.mintlify.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Editor Bubble Item

> Bubble Item

```tsx
<EditorBubbleItem
  key={index}
  onSelect={(editor) => {
    item.command(editor);
  }}>
  ...
</EditorBubbleItem>
```

## Props

<ParamField required path="children" type="ReactNode" />

<ParamField path="className" type="string" />

<ParamField path="onSelect" type="(editor: Editor) => void" />


Built with [Mintlify](https://mintlify.com).