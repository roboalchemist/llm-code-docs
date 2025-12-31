# Source: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/notebooks.md

# Notebooks

### What is a Notebook?

Notebooks are runnable documentation consisting of markdown text and list elements, code blocks, and runnable shell snippets that can be automatically executed in your terminal session. Notebooks are searchable and accessible through the [Command Palette](https://docs.warp.dev/terminal/command-palette) so you can access and run your documentation without ever leaving the terminal. You can also export Notebooks in .md format at any time.

### How to save and edit notebooks

You can create a new notebook from various entry points in Warp

{% tabs %}
{% tab title="macOS" %}

* From Warp Drive, + > New notebook
* From the [Command Palette](https://docs.warp.dev/terminal/command-palette), create a new team or personal notebook.
  {% endtab %}

{% tab title="Windows" %}

* From Warp Drive, + > New notebook
* From the [Command Palette](https://docs.warp.dev/terminal/command-palette), create a new team or personal notebook.
  {% endtab %}

{% tab title="Linux" %}

* From Warp Drive, + > New notebook
* From the [Command Palette](https://docs.warp.dev/terminal/command-palette), create a new team or personal notebook.
  {% endtab %}
  {% endtabs %}

Any of these entry points will open the notebook editor where you can:

* Title your notebook.
* Start adding text and code elements.

{% hint style="info" %}
Note: The notebook will not be saved until either title or body text is added.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4b9e7ba6e4520a38ebc283cae3bbeae80badea2c%2Fnotebooks_editor.gif?alt=media&#x26;token=abe316cc-279d-4134-8789-80657df479d5" alt=""><figcaption><p>Editing a Notebook</p></figcaption></figure>

### Working with Notebooks

#### Adding new elements

Notebook elements (text, code, list items) can be added in several ways:

* Using the appropriate markdown shortcut (e.g. ### for Heading 3).
* Typing /, which will open up a selection menu of supported elements.
* Pressing the + icon which appears when hovering over a line and selecting from the menu of supported elements.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bace71efc7ac809b73430ac964dcd925c296fcef%2FScreenshot%202024-02-20%20at%209.53.34%E2%80%AFAM.png?alt=media&#x26;token=10b354d4-458f-4467-909f-9ef4be2f2751" alt=""><figcaption><p>Markdown element types</p></figcaption></figure>

#### Styling existing elements

Existing notebook elements can be styled in several ways:

* Selecting an existing element and selecting text decorations (like bold, italics, or inline code) from the hover menu.
* Using markdown syntax for text stylings like \*\*bold\*\* or \*italic\*.
* Selecting an existing element and changing the overall type of the element via the dropdown element menu.

<div data-full-width="true"><figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a44f76dd4a83fcf4f6647925ee6a3aa0c2b953c0%2FScreenshot%202024-02-20%20at%209.54.37%E2%80%AFAM.png?alt=media&#x26;token=4fbc6219-3078-4683-8590-d269a984a7b2" alt=""><figcaption><p>Styling menu</p></figcaption></figure></div>

#### Using Command and Code Blocks

Command and code blocks have several unique properties such as syntax highlighting and quick actions that make working with code-based documentation simple. You can create a code or command block by either:

* Selecting Command or Code from the new element menu
* Typing ` ``` ` (triple backticks)

Once you’ve inserted your code block you can select the language at the bottom of the block from numerous options which will apply the appropriate syntax highlighting if available (or default to Code if your language is not found). All code and command blocks will apply syntax highlighting and provide a quick copy button for easy access.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-74d6ea0a64832a1e2a30b43891bf6c6c1a7a7f2f%2Fnotebook-code-block.png?alt=media" alt=""><figcaption><p>Example code block</p></figcaption></figure>

#### Special Properties of Command Blocks

If you insert a Command block or specify the language as “Shell”, Warp provides extra functionality to simplify terminal work.

#### Executing Command Blocks

Developers can execute shell command blocks by:

{% tabs %}
{% tab title="macOS" %}

* Using the insert button at the bottom of the block
* Pressing `CMD-ENTER` while the block is selected (a blue highlight will appear)
  {% endtab %}

{% tab title="Windows" %}

* Using the insert button at the bottom of the block
* Pressing `CTRL-ENTER` while the block is selected (a blue highlight will appear)
  {% endtab %}

{% tab title="Linux" %}

* Using the insert button at the bottom of the block
* Pressing `CTRL-ENTER` while the block is selected (a blue highlight will appear)
  {% endtab %}
  {% endtabs %}

The command text will be inserted into the developer’s active terminal session, or a new session if none are active.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-a6dd0c127c8cb4c2d82114901dcafbf58d1b5322%2Fnotebook-cmd-block-run.png?alt=media" alt=""><figcaption><p>Run option for command block</p></figcaption></figure>

#### Adding arguments to Command Blocks

Command blocks accept parameters in the same format as [Workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows). To add an argument to your command block, use {{double\_curly\_brackets}} to specify your argument term.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-7dd079367cb23d6824851fd0bb30c26bab9ff5b1%2Fnotebook-cmd-with-params.png?alt=media" alt=""><figcaption><p>Command block with parameters</p></figcaption></figure>

#### Navigating command blocks with the keyboard

Command Blocks also support keyboard navigation. There are two ways to enter the keyboard navigation mode:

{% tabs %}
{% tab title="macOS" %}

* Clicking on a shell block.
* Pressing `CMD-UP` or `CMD-DOWN.`

Once a command block is selected, press `CMD-ENTER` to insert it into the terminal input. You can also use `UP, DOWN, CMD-UP`, and `CMD-DOWN` to navigate between command blocks. While the Notebook is focused, press `CMD-L` to switch focus back to the terminal without inserting a command.
{% endtab %}

{% tab title="Windows" %}

* Clicking on a shell block.
* Pressing `CTRL-UP` or `CTRL-DOWN.`

Once a command block is selected, press `CTRL-ENTER` to insert it into the terminal input. You can also use `UP, DOWN, CTRL-UP,` and `CTRL-DOWN` to navigate between command blocks. While the Notebook is focused, press `CTRL-L` to switch focus back to the terminal without inserting a command.
{% endtab %}

{% tab title="Linux" %}

* Clicking on a shell block.
* Pressing `CTRL-UP` or `CTRL-DOWN.`

Once a command block is selected, press `CTRL-ENTER` to insert it into the terminal input. You can also use `UP, DOWN, CTRL-UP,` and `CTRL-DOWN` to navigate between command blocks. While the Notebook is focused, press `CTRL-L` to switch focus back to the terminal without inserting a command.
{% endtab %}
{% endtabs %}

#### Adding existing Workflows to Notebooks

If you have existing [Workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows) that you’d like to insert into your notebook rather than duplicating their content, you can select Embedded Workflow from the new element menu and select from the available Workflows. Once embedded in a notebook, the workflow will be executable like a regular command block. To edit the content of the embedded workflow, you will need to edit the source workflow which can be found by searching for the title in the [Command Palette](https://docs.warp.dev/terminal/command-palette).

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-fd9bc4dfd10d5c519c5d798efa387dd68d49c559%2FScreenshot%202024-02-20%20at%209.58.44%E2%80%AFAM.png?alt=media&#x26;token=abaa4739-a127-4b79-a129-d26bdf232e26" alt=""><figcaption><p>Embedding an existing workflow in a notebook.</p></figcaption></figure>

### Working with Notebooks in a team

If the notebook is shared with a team, all team members will have access to edit the notebook and updates will sync immediately for all members of the team.

{% hint style="info" %}
Note that only one editor is allowed at a given time. Opening the notebook while there is an active editor will open the notebook in Viewing mode. Your mode (view vs edit) can be toggled above the notebook’s title.
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-f50062bc4be1b34771fecbc6f6d1ee7d5bd3830b%2Fnotebook-view-mode.png?alt=media" alt=""><figcaption><p>View mode example</p></figcaption></figure>

### Import and Export Notebooks in Warp Drive

Please see our [Warp Drive Import and Export](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/..#import-and-export) instructions.
