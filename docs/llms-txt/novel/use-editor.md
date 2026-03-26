# Source: https://novel.mintlify.dev/docs/components/utils/use-editor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novel.mintlify.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# useEditor

> Imperative API for interacting with the editor.

Your component must be a child of `EditorRoot` to use this hook.

```tsx
const CustomComponent = ({ open, onOpenChange }: LinkSelectorProps) => {
  const { editor } = useEditor();
...
}

<EditorRoot>
  <CustomComponent/>
</EditorRoot>
```

## Props

<ParamField path="editor" type="Editor">
  All methods are available here [Editor](https://tiptap.dev/docs/editor/api/editor)
</ParamField>


Built with [Mintlify](https://mintlify.com).