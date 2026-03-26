# Source: https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping.md

# Context Scoping

Context Scoping is a mechanism that explicitly shows the user the scope in which Tabnine searches for relevant context.

For private installations, context scoping became available from version 5.15.0 and replaced the Workspace selector.

### What is Context Scoping?

Tabnine Chat searches for additional relevant context beyond the user's prompt to help answer questions more effectively. The relevant context can be found in various sources:

* The current open file
* The current conversation history
* The local workspace in the IDE
* Connected remote repositories from the organization's codebase (Enterprise only)

**Context Scoping** is a mechanism that explicitly shows the user the scope in which Tabnine searches for relevant context. It allows users to refine the scope, guiding Tabnine on where to look or where not to look for context.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5b3704ffb7bec2b7f7907ccdcda75a444f153c93%2FScoping.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Why is this important?

The additional relevant context is passed to the AI model, directly affecting the accuracy of the Chat answer. In some cases, the most relevant context was not added, and the answers were not as accurate as expected. This can happen due to various reasons; the most common ones are that there is too much code to look in or similar content that "hides" the actually relevant context. Scoping allows users to direct Tabnine's focus on relevant areas, improving the results.

For example, by default Tabnine prefers the context from the current files and local workspaces, as it usually provides the most relevant context. However, for some questions the most relevant context is actually in a remote repository. The user can change the context scope to a remote codebase or specific remote repository, resulting in more accurate answers.

### Working with Context Scoping

The chat context scoping is managed for each chat conversation. The state of the context scoping of the conversation appears in a dedicated section next to the user prompt. Each type of scope is indicated with the relevant tag representing that scope. Tabnine will only search for relevant context in the existing context scoping.

### Types of Scoping

#### High-Level Scopes

* **Current file**: Tabnine can take the context from the current open file, if an open file exists. If this scope is not selected, Tabnine will ignore the current file.
* **Local Workspace**: Tabnine can look for relevant context in the local IDE workspace. If this scope is not selected, Tabnine will not look for relevant context in the local IDE workspace.

{% hint style="info" %}
**Local Indexing**:\\

If folders are not under version control (which might not be the case for local folders), then Tabnine by default won't index the folder.\
\
To fix this, create a file named `.tabnine_root` in the root folder, then restart your IDE. This will signal to Tabnine to index local content in the root folder.\\
{% endhint %}

* **Remote Codebase**: Tabnine can look for relevant context in all the remote repositories connected to the account from the codebase. If this scope is not selected, Tabnine will not look for relevant context in the connected repositories.

{% hint style="info" %}
**Unindexed Files:**\
\
As of 5.23.0, you can refer to the following filetypes with the following extensions via Context Scoping: `.md, .mkd, .mdwn, .mdown, .mdtxt, .mdtext, .markdown, .yaml, .yml, .json, .xml, .gradle, bash, .sh, .txt, .ini, .properties, .prefs, .cfg, .cmake`
{% endhint %}

#### Specific Scopes

* **Remote repository**: Indicates a specific remote repository from the codebase which is connected to the account.
* Folders and files from remote repositories in the codebase
* Folders from the local workspace

### Managing and Adjusting Context Scoping

Context scoping is defined at the Chat conversation level.

Each conversation maintains a separate scoping status. Each conversation starts with the default scoping, and the user can change the scoping by adding and removing scope.

#### Scoping State

The following three options comprise the default scoping state:

* Current file
* Local workspace
* Remote codebase (Enterprise only, if the account has connected repositories)

The default scoping appears when starting a new conversation or when resetting the scope, ensuring that Tabnine searches for context using the initial settings before any customizations.

While not part of the default scoping state, you can also add your Terminal to your context scope. The following will show you how to modify resources in your context scope with reset, adding, and removing:

#### Resetting Scope

To reset the context scope, click the "<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c096be1dc324c09158177ddb47f02c6d57381754%2Ficon%3Dhisrory.svg?alt=media" alt="" data-size="line"> **Reset scope"** option in the input window:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-12d5574e150a316167906cc3d09f685cd2f7b63b%2FReset%20scope.gif?alt=media" alt=""><figcaption><p>Resetting scope in Tabnine</p></figcaption></figure>

#### Adding More Scope

The user can add more scope by clicking the "+ **Add scope**" option and choosing the scope to add.

High-level scope can be added by checking the high-level option in the **Add context scope** menu.

Remote repositories, remote folders, and/or remote files are added by clicking the relevant option in the menu and then select (or search) for the desired repository:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-6a06fdc8ba5fa089113bbc0a093f58df67b4c36a%2FAdd%20Remote%20Codebase.png?alt=media" alt=""><figcaption></figcaption></figure>

The Terminal is added by selecting it from the **+ Add scope** menu.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-71583d4155c1a0adbaf0bf2216bc8ed5fcb07402%2FAdd%20Terminal%20Scope.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Removing Scope

Scope can be removed by simply clicking small "x" icon on the on each scope tag.

High-level scoping can also be removed by unchecking the high-level option in the Add context scope menu.

You can also tap the "x" option inside the input menu:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a37ac6cc21f5f5f516c9016c9a4590d54506c138%2FDelete%20Scope.gif?alt=media" alt=""><figcaption><p>Deleting context scope within the input window</p></figcaption></figure>
