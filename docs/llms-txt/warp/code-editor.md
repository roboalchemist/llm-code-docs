# Source: https://docs.warp.dev/code/code-editor.md

# Code Editor

## Built-in Code Editor

Warp comes with a native code editor designed for quick, in-flow edits alongside your Agent conversations. Instead of switching back and forth to an IDE, you can open and edit files directly in Warp — with essentials like syntax highlighting, a tabbed file viewer, find and replace, Vim keybindings, and a file tree for browsing and adding files as context.

The editor is built for fast changes to agent-generated code: renaming a variable, tweaking copy, or rewriting a short function. Having just enough editing power in-context makes it easier to land an agent’s changes and keep momentum.

### Opening Files in Warp

**You can open files in the editor in several ways:**

1. **Click a file path** from the terminal output or an AI conversation and select "Open in Warp."
2. **Use the file menu in the command palette** (`CMD + O` on macOS, `CTRL + SHIFT + O` on Windows or Linux) when in a Git-tracked repo to search for and open files inside that repo.

   1. You can also access this via the magnifying glass icon in the pane coding toolbelt at the top left of any pane.

   <figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-68913a093169d16c73c8d451558165dc54fbd566%2Fsearch-files-icon.png?alt=media" alt=""><figcaption></figcaption></figure>
3. **Browse via the** [file-tree](https://docs.warp.dev/code/code-editor/file-tree "mention") to open or create files.
4. **Opening a generated code diff** from an Agent Conversation: [reviewing-code](https://docs.warp.dev/code/reviewing-code "mention").

{% embed url="<https://screen.studio/share/H7hTUgf2>" %}

**To save your changes to files**: use `CMD + S` on macOS or `CTRL + S` on Windows or Linux.

### Tabbed File Viewer

Warp can group multiple files into a single tabbed viewer, reducing clutter and making it easier to work across multiple files.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-30d23d44aaee5cf76e0b05db106c1d846e3eb500%2Ftabbed-file-viewer.png?alt=media" alt=""><figcaption></figcaption></figure>

* Enabled by default for new users (can be toggled in `Settings > Features > General > Group files into a single editor pane`)
* Reorder, close, or drag file viewers between tabs.
* Merge enter panes together by dragging one into another.

**Here's a more in-depth demo:**

{% embed url="<https://www.loom.com/share/a682461da66944f583e2fa3d27b71189?sid=679ce8f6-e530-4c0d-99ab-0613d1269f8b>" %}

### **File Layout Options**

Choose how new files open in Warp by default in: `Settings > Features > General > Choose a layout to open files in Warp`

* **Split pane**: new files open alongside the current editor
* **New tab**: new files open in their own tabbed viewer

### Supported Languages

The editor supports syntax highlighting and editing for a wide range of languages, including:

Rust, Go, YAML, Python, JavaScript/TypeScript, JSX/TSX, Java/Groovy, C++, Shell/Bash, C#, HTML, CSS, C, JSON, HCL/Terraform, Lua, Ruby, PHP, TOML, Swift, Kotlin, Starlark, SQL, Powershell, and Elixir.

We’re continuously expanding language support.

### Other Editor Features

Warp's native code editor also supports the following features:

* [file-tree](https://docs.warp.dev/code/code-editor/file-tree "mention") — Browse, open, and manage your project with Warp’s native file tree.
* [find-and-replace](https://docs.warp.dev/code/code-editor/find-and-replace "mention") — Use Warp’s built-in find and replace to quickly search across a file, jump between matches, and make precise edits with options for regex, case sensitivity, and smart case preservation.
* [code-editor-vim-keybindings](https://docs.warp.dev/code/code-editor/code-editor-vim-keybindings "mention") - Use Vim keybindings to edit code and text in Warp's native code editor.
