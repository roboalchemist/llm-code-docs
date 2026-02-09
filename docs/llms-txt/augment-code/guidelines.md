# Source: https://docs.augmentcode.com/setup-augment/guidelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rules & Guidelines for Agent and Chat

> You can provide custom rules and guidelines written in natural language to improve Agent and Chat with your preferences, best practices, styles, and technology stack.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## What are Rules & Guidelines?

Agent and Chat rules and guidelines are natural language instructions that can help Augment reply with more accurate and relevant responses. Rules and guidelines are perfect for telling Augment to take into consideration specific preferences, package versions, styles, and other implementation details that can’t be managed with a linter or compiler. You can create guidelines for a specific workspace or globally for all chats in your IDE; guidelines do not currently apply to Completions, Instructions, or Next Edit.

User Guidelines are defined under Settings and stored within your IDE to be used to guide preferences inside of the Agent and Chat. Workspace Guidelines and Rules are stored directly in your repository.

## Working with User Guidelines

<Info>
  User Guidelines are stored locally in your IDE and will be applied to all future chats in that IDE. Guidelines defined in VSCode will not propagate to JetBrains IDEs and vice versa.
</Info>

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ea8daf68e19c31f2784d2de6765dc627" alt="Adding user guidelines" className="rounded-xl" data-og-width="1248" width="1248" data-og-height="603" height="603" data-path="images/user-guidelines.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=44a75f2ea891c74955080112b31425d7 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ad02067cd61b08f0b695db3c8cf91700 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=81690b18ca6b28ed1a140bb4663a8208 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=44503cc6949ec0dc58c04e73c3ea17be 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=5bc2aa6fc7e5b4a4289fb8b88cd7ef0f 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/user-guidelines.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=5f09033c7ae02a579cdafffcbf329bd0 2500w" />

You can add user guidelines by clicking Context menu (@), starting an @-mention inside Chat, or clicking Settings > Rules and User Guidelines.

### Navigating from the Context menu (@) User Guidelines

1. @ mention and select `User Guidelines`
2. Enter your guidelines (see below for tips)
3. Press Escape to save or wait for autosave

### Navigating from Settings > User Guidelines and Rules

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/open-rules.gif?s=07fce1fa6c1e2bdf6f78642658f804be" alt="Open rules and guidelines" className="rounded-xl" data-og-width="800" width="800" data-og-height="393" height="393" data-path="images/open-rules.gif" data-optimize="true" data-opv="3" />

1. In the top right corner, select the hamburger menu (⋯)
2. Select Settings
3. From the left menu in Augment Settings, select User Guidelines and Rules

## Working with Rules

You can craft Rules to guide Augment towards specific documentation, frameworks, workflows or workstyles.

Rules are files that live in the `.augment/rules` directory. Currently, we support 3 types of rules:

* **Always**: contents will be included in every user prompt
* **Manual**: needs to be tagged through @ attaching the Rules file manually
* **Auto**: Agent will automatically detect and attach rules based on a description field

### User Rules vs Workspace Rules

Rules can be defined at two levels:

| Scope     | Location                           | Availability                        |
| :-------- | :--------------------------------- | :---------------------------------- |
| User      | `~/.augment/rules/`                | Available in all workspaces         |
| Workspace | `<workspace_root>/.augment/rules/` | Available in current workspace only |

**User rules** are stored in your home directory and apply to all projects. Use these for personal preferences, coding style guidelines, or conventions you want to follow across all your work. User rules are always treated as **Always** type and are automatically included in every prompt regardless of any frontmatter configuration.

**Workspace rules** are stored in the project repository and apply only to that specific project. Use these for project-specific guidelines that should be shared with your team via version control. Workspace rules support all three types (Always, Manual, Auto) via frontmatter configuration.

### Hierarchical Rules

In addition to workspace-level rules, Augment supports **hierarchical rules** through `AGENTS.md` and `CLAUDE.md` files placed in subdirectories. When working on files in a subdirectory, Augment automatically discovers and applies rule files from that directory and all parent directories.

**How it works:**

1. When you work on a file, Augment looks for `AGENTS.md` and `CLAUDE.md` in the file's directory
2. It walks up the directory tree, checking each parent directory for these files
3. All discovered rules are included in the context for that work session
4. The search stops at the workspace root (workspace root rules are loaded separately)

**Example:**

```
my-project/
  AGENTS.md                  <- Always included (workspace root)
  src/
    AGENTS.md                <- Included when working in src/ or subdirs
    components/
      AGENTS.md              <- Included when working in src/components/
      Button.tsx
```

When working on `src/components/Button.tsx`, all three `AGENTS.md` files are loaded.

**Use cases:**

* Framework-specific guidelines (React rules in frontend/, Node.js rules in backend/)
* Module-specific conventions (API design patterns in api/)
* Team boundaries (different teams maintain their own standards)

<Note>Only `AGENTS.md` and `CLAUDE.md` files are discovered hierarchically. Files in `.augment/rules/` are only loaded from the workspace root.</Note>

### Importing Rules

**Augment** will automatically import rules if they are detected in the current workspace. Augment will look for markdown files, e.g., files ending with `*.md` or `*.mdx`. You can also manually import rules inside of Settings > Import rules.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=1a01f8bde915b4d3049d7b39f17eddba" alt="Import rules" className="rounded-xl" data-og-width="1600" width="1600" data-og-height="839" height="839" data-path="images/import-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0eb8b03ecb20cc3ef865dd35bd692b0c 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a16b6f051ca12bd4f523c818cbf1096c 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=98b8e52dbc26d79d38117c71c7303379 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f26d41383781b07faba4af8e7d93d7b5 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f558643818e7433474a1d0ea80c55602 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/import-rules.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=68e307de359234378d23d0613e747e89 2500w" />

### Importing Augment Memories into Rules or User Guidelines

Augment Memories are automatically created by the Agent. If you’ve ever modified the Memories or prompted the Agent to remember something you can import these preferences as Rules or User Guidelines.

1. From the prompt box, click on Augment Memories
2. Select the item you'd like to import and then click User Guidelines at the top of Augment Memories from inside the editor.
3. To add the memory as a Rule, you'll first need to add at least one rule using +Create new rule file. Now, you can select any information inside the Augment Memories and save it as a Rule.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=45a38f467945005fe2ac2779108ef06f" alt="Move memories" className="rounded-xl" data-og-width="1816" width="1816" data-og-height="426" height="426" data-path="images/move-memories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e62394563486d878453a223c426cf6be 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=04d51becdd41bbfd3f443be4028bb959 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=177121e2215c3364219ca1b6d85bcd22 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=84a7f76d24c1a4ead9755a2bb53945ff 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7a96b7c249d5fd4318c1e167eddc4fa8 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/move-memories.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f756375a0d1e054fe1820b2913453161 2500w" />

## Working with Workspace Guidelines `.augment-guidelines` (legacy)

You can add an `.augment-guidelines` file to the root of a repository to specify a set of guidelines that Augment will follow for all Agent and Chat sessions on the codebase. The `.augment-guidelines` file should be added to your version control system so that everyone working on the codebase has the same guidelines.

### Tips for good rules and guidelines

* Provide guidelines as a list
* Use simple, clear, and concise language for your guidelines
* Asking for shorter or code-only answers may hurt response quality

### Examples

<AccordionGroup>
  <Accordion title="User Guideline Examples">
    * Ask for additional explanation e.g. `For Typescript code, explain what the code is doing in more detail`

    * Set a preferred language e.g. `Respond to questions in Spanish`
  </Accordion>

  <Accordion title="Rule Examples">
    * Add links to Google Docs, Notion or Confluence files that define goals, product requirements, or project objectives

    * Point to specific documentation e.g. `Python 3.13.5` for the dependencies inside your project

    * Outline templates or example code commonly used in your project

    * Establish consistent frameworks, coding styles, and architectural patterns across your codebase

    * Provide examples on codebase style. For example:
      * Information that ONLY applies to the specific files, functions, or code snippets
      * Vague or obvious preferences that aren't actionable
      * General statements about good programming practices that any user would want
  </Accordion>

  <Accordion title="Workspace Guideline Examples">
    * Identifying preferred libraries e.g. `pytest vs unittest`
    * Identifying specific patterns e.g. `For NextJS, use the App Router and server components`
    * Rejecting specific anti-patterns e.g. `a deprecated internal module`
    * Defining naming conventions e.g. `functions start with verbs`
  </Accordion>
</AccordionGroup>

## FAQs

<AccordionGroup>
  <Accordion title="How are Rules different from Guidelines?">
    Guidelines and Rules differ in how they are stored and their scope of influence.

    * **User Guidelines** are stored in the user’s local IDE storage that will persist across Chat & Agent sessions; however, they do not persist across workspaces.
    * **User Rules** are stored in `~/.augment/rules/` and apply to all workspaces. They are always treated as "Always" type and automatically included in every prompt.
    * **Workspace Rules** are stored within the repository under the `.augment/rules` root that will allow you to split up previous Guidelines into multiple files to more precisely define your preferences. Workspace rules support all three types (Always, Manual, Auto).
    * **Workspace Guidelines** (legacy) stored within the repository under the `.augment-guidelines` file are a legacy set of rules that can be edited by editing the `.augment-guidelines` in your repository. Augment will automatically import Workspace Guidelines as Rules which you can access under Settings > User Guidelines and Rules.
  </Accordion>

  <Accordion title="What are the current limitations?">
    * User Guidelines are currently limited to a maximum of 24,576 characters.
    * Workspace Guidelines + Rules are limited to a maximum of 49,512 characters. If we exceed these limits, the user will be notified in app and be applied in order of (manual rules, always + auto rules, .augment-guidelines)
    * For VSCode, Guidelines are available in plugin version 0.492.0 and above
    * For JetBrains IDEs, Rules are available in plugin version 0.249.1 and above
  </Accordion>
</AccordionGroup>

## See Also

* [Custom Rules and Guidelines (CLI)](/cli/rules) - Configure rules for Auggie CLI
* [Workspace Context](/setup-augment/workspace-context-vscode) - Understanding workspace configuration in VSCode
* [Chat Context](/using-augment/chat-context) - Learn about context in Chat
