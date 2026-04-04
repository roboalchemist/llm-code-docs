# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/chat/inline-context.md

# Inline Context

Think of Context like the brain of Qodo Chat.

The Context is what Qodo's AI models know about your code and what they use to give the best, most accurate response.

**Adding more context will give more accurate and relevant responses**, so choosing context is an important part of using Chat to your advantage.

Use Inline Context to get dynamic, quick access to relevant code components and use them within your Qodo Chat queries with ease, improving efficiency and relevance.

## How to set Inline Context

1. Type `@` in the chatbox. A dropdown menu containing all referencing options will open.
2. **Select relevant component:** The dropdown menu provides a list of code components that can be referenced. These include:
   * Folders
   * Files
   * Classes
   * Functions
   * Methods
   * [Repository tags](https://docs.qodo.ai/qodo-documentation/qodo-gen/code-intelligence/context-engine)
   * Git Diff
     * You can tag your local changes, branch changes and more
3. **Type and Choose:** Start typing the name of the component you’re looking for until it shows in the dropdown menu. You can then choose it either by using the arrow keys or clicking on it.

Inline Context automatically suggests the current file and its symbols, ensuring that the most relevant code components are readily accessible.

## Keyboard Shortcut

You can add **code snippets** as context using a keyboard shortcut.

* **VSCode**:
  * macOS: `CMD+Shift+E`
  * Windows: `CTRL+Shift+E`
* **JetBrains IDEs**:
  * macOS: `CMD+ALT+,`&#x20;
  * Windows: `CTRL+ALT+,`&#x20;

## Example Usage

```typescript
function sayHello(name) {
    return "Hello World! I'm " + name;
}

const user = "Username";
```

In the chatbox, typing `@` would allow users to quickly reference the `sayHello` function or the `user` variable.
