# Source: https://docs.tabnine.com/main/getting-started/inline-actions.md

# Inline Actions

{% hint style="danger" icon="eclipse" %}
Tabnine will **sunset** the Inline Actions feature by Version 6.2.0 around May 2026.
{% endhint %}

Inline actions allow you to work directly on selected snippets of code — getting AI-enabled edits, fixes, refactoring, documentation, and more — with all responses generated inline. Additionally, you can use inline actions to generate code directly at your cursor’s location inside the code editor.

Inline actions brings together the best of our AI chat and code completions into a single interface. By delivering AI-generated code or edits within the same environment where you’re working, inline actions are a faster and easier method to create, refine, document, and fix code. Inline actions enable you to stay in the flow by offering an intuitive way of using Tabnine.

### Getting started with inline actions

Inline actions are embedded in VS Code and the JetBrains family of IDEs (support for other IDEs to come soon). Trigger inline actions by clicking Edit in the code lens functionality (in VS Code), or by using the ⌘ + I (Ctrl + I for Windows and Linux) keyboard shortcut. These actions open up a Tabnine-specific command palette containing an array of commands.\\

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-1695d25dd5c9af669111d9c4eb07d5e0c47e8ab9%2FScreenshot%202024-08-26%20at%209.29.15%E2%80%AFAM.png?alt=media" alt=""><figcaption><p>Code lens functionality in VS Code</p></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5a92a69a30bcaf771f97ee53704c044c5113cabb%2FScreenshot%202024-08-21%20at%209.32.38%E2%80%AFPM.png?alt=media" alt=""><figcaption><p>Command palette for inline actions</p></figcaption></figure>

You can enter instructions for your task in natural language or choose from the available quick commands. We support /fix-code, /document-code, /explain-code, and /code-explore quick commands. The responses for /fix-code and /document-code are generated inline, whereas the responses for /explain-code and /code-explore quick commands are generated in the AI chat panel. This is because the answers to these tasks are typically not needed in the code files. Therefore, when using inline actions for /explain-code and /code-explore commands, we provide the responses in the AI chat panel, making it easier to consume them.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-41ebf430d132fcc8e31d9fd2d3819c66df540a9d%2FScreenshot%202024-08-23%20at%201.19.09%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

Inline actions support the [mentions (using the @ symbol) capability](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/interact#mentions) and allow you to include a specific code element (type, method, or class) from the workspace in the prompt. Inline actions also [leverage your context](https://docs.tabnine.com/main/welcome/readme/personalization) to deliver optimized recommendations for your use case — accessing locally available code and information in your IDE and (for Enterprise users) your organization’s global codebases to generate responses tailored to you and your organization.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d169079f77155330abaa525190bf852741c2f11f%2FScreenshot%202024-08-23%20at%201.26.01%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

You can specify the scope for your question — select a few lines of code or a code block that you want to edit, or inform Tabnine to generate the response at the cursor location.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2853830b0e6a7650dad41b087bef63d6713f04bd%2FScreenshot%202024-08-23%20at%201.28.01%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

Inline actions also benefit from Tabnine’s [switchable models](https://www.tabnine.com/blog/introducing-switchable-models-for-tabnine-chat/). Select the best model for your use case or corporate requirements, choosing from Tabnine’s custom-developed models ([Tabnine Protected 2](https://www.tabnine.com/blog/announcing-tabnine-protected-2-a-license-safe-llm-that-performs-as-strong-as-the-best/), Tabnine + Mistral) or from popular models from third parties (Command R+, [Claude 3.5 Sonnet](https://www.tabnine.com/blog/tabnine-adds-support-for-anthropics-claude-3-5-sonnet/), [GPT-4o](https://www.tabnine.com/blog/openai-gpt-4o-is-now-available-on-tabnine-chat/), and [Codestral](https://www.tabnine.com/blog/mistrals-codestral-is-now-available-on-tabnine/)). Note that the model selection persists across AI chat and inline actions. For example, if you select Claude 3.5 Sonnet as your model in the AI chat, then inline actions also uses Claude 3.5 Sonnet.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-cf3c9dc9ed6e80076ddafe1e135b9e50604ef58f%2FScreenshot%202024-08-23%20at%201.20.29%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

After you specify what you want to accomplish using inline actions and hit Enter (Command + Enter, or Ctrl + Enter for JetBrains IDEs), Tabnine provides inline responses along with a diff view that makes it easy to determine the suggested changes. You can accept (by clicking Alt + A), discard the response (by clicking Alt + R), or refine (using Alt + F) — after you accept, Tabnine inserts the response inline.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4bbc4950eead02fd1fca114e71340ce97ad26bef%2FScreenshot%202024-08-21%20at%209.35.52%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

### What you can do with inline actions

#### Generate new code inline

Simply click the ⌘ + I keyboard shortcut (Ctrl + I for Windows and Linux) to trigger inline actions. Type in natural language the instructions for creating new code and hit Enter. Tabnine generates the code and offers responses right where your cursor is. Review the suggestions quickly with the diff view, and accept (using Alt + A), reject (using Alt + R), or refine (using Alt + F).

{% embed url="<https://youtu.be/h_RIYwYzi8w>" %}

#### Fix code with inline actions

Click Edit in the code lens to open the inline actions command palette. Select the /fix-code command (or type in natural language) and hit Enter. Tabnine fixes the code and generates the response inline. Review quickly with the diff view and accept (using Alt + A), reject (using Alt + R), or refine (using Alt + F)..

{% embed url="<https://youtu.be/JcEFYcu9nyc>" %}

#### Create inline documentation

Use the ⌘ + I keyboard shortcut (Ctrl + I for Windows and Linux) to trigger inline actions. Type in natural language to create inline documentation (or use the /document-code quick command) and hit Enter. Tabnine generates inline responses — review them quickly and accept (using Alt + A), reject (using Alt + R), or refine (using Alt + F).

{% embed url="<https://youtu.be/E_fpgLG8IS8>" %}

#### Edit code with inline actions

Select the code, trigger inline actions using the ⌘+I keyboard shortcut (Ctrl + I for Windows and Linux), and enter instructions for making modifications in natural language. Once you hit Enter, Tabnine generates inline responses — review them quickly and accept (using Alt + A), reject (using Alt + R), or refine (using Alt + F).

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fdcb99163810ed42aa864dc7eecd15e8b16313bf%2F240905_Refactor_Demo_HR.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Keyboard shortcuts

* Trigger inline actions: ⌘ + I (Ctrl + I for Windows and Linux)
* Accept response: Opt + A (Alt + A)
* Reject response: Opt + R (Alt + R)
* Refine response: Opt + F (Alt + F)
