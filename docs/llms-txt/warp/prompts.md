# Source: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts.md

# Prompts

## What is a Prompt?

A Prompt is a parameterized natural language query you can name and save in Warp to use with [Agent Mode](https://docs.warp.dev/agents/using-agents).

Prompts are searchable and easily accessed from the [Command Palette](https://docs.warp.dev/terminal/command-palette) so you can find and execute them without switching context. They allow you to save and reuse specific and complex AI workflows, making it easier to repeat multi-step tasks with Agent Mode.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4a7a7593ea9e583c8acde5950aff4814fd6953c1%2Fprompts-command-view.png?alt=media" alt="View of a Prompt in Warp Drive showing the command view interface"><figcaption><p>Command view of a Prompt in Warp Drive</p></figcaption></figure>

### Demo: Trigger Reusable Actions with Saved Prompts

Here's an example from [Warp University](https://www.warp.dev/university), where Zach walks through what Prompts he uses for PRs and Git commits:

{% embed url="<https://www.youtube.com/watch?ab_channel=Warp&v=pE15zjJmB4E>" %}

There's other great examples of Prompts on [Do Things](https://dothings.warp.dev/) and [Warp University](https://www.warp.dev/university).

## How to save and edit Prompts

You can create a new Prompt from Warp Drive by clicking the + button and selecting "Prompt".

* Name your Prompt
* Edit the natural language query along with any arguments (also known as parameters)
* Add a meaningful description that will be indexed for search (optional)
* Add arguments, descriptions for arguments, and default values (optional)

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b5f0aa58be3db8f09ff0288c2a04ee3d3c2a9b18%2Fprompts-edit-view.png?alt=media" alt="View of the Prompt editor interface showing the edit form with fields for name, query, description, and arguments"><figcaption><p>Edit view of a Prompt in Warp Drive</p></figcaption></figure>

Once a Prompt has been created, you can edit it at any time, as long as you have access to an internet connection.

### Working with arguments

In the Prompt editor, you can add arguments manually with "New argument" or by typing in double curly braces (`{{argument}}`) within the command field. If you select "New argument" while you have text selected, Warp will wrap that text in curly braces to create an argument.

There are some rules for creating valid arguments:

* Argument names can only include characters `A-Za-z0-9`, hyphens `-` and underscores `_`
* The first character of an argument cannot be a number

Arguments can be one of two types: text or enum. By default, all new arguments are text type.

#### Enum type arguments

Enums allow you to specify expected inputs to a Prompt argument. When you insert a Prompt with enums into the input editor, you will be prompted with suggestions for filling in the argument. You can open the suggestions menu by pressing `SHIFT-TAB` while selecting an argument.

For detailed information about creating and using enum type arguments, please see the [Enum type arguments section in Workflows documentation](https://docs.warp.dev/knowledge-and-collaboration/workflows#enum-type-arguments).

### Editing Prompts with a team

If the Prompt is shared with a team, all team members will have access to edit it and updates will sync immediately for all members of the team.

If a Prompt in the Warp Drive has been edited by another team member or a user on another device while you are attempting to edit the same Prompt, you will not be able to save changes; you will need to check out the latest version and try again.

## How to execute Prompts

You can execute a Prompt in several ways:

* From Warp Drive, click the Prompt
* From the [Command Palette](https://docs.warp.dev/terminal/command-palette) or [Command Search](https://docs.warp.dev/terminal/entry/command-search), search for a Prompt by name or type "prompts:" to see all available prompts and your prompt history
* When a Prompt is selected, you can use `SHIFT-TAB` to cycle through the arguments.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-390738e6639a1537144c71a295dbf0f2de7c4103%2Fprompts-command-palette.png?alt=media" alt="Command Palette interface showing a search for Prompts with results displayed"><figcaption><p>Search for Prompts in the Command Palette with <code>CMD + P</code></p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b88aa05c6d16d5d02a0f72d1976d33c2450f66fe%2Fprompts-command-search.png?alt=media" alt="Command Search interface showing a search for Prompts with results displayed"><figcaption><p>Search for Prompts in Command Search with <code>CTRL + R</code></p></figcaption></figure>

These options will paste the Prompt into your active terminal input. Prompt names and any relevant descriptions and arguments will be displayed in a dialog, so you can understand how to use the Prompt.

You can make any adjustments you need to the arguments before running the Prompt in your input editor.

### Import and Export Prompts in Warp Drive

Please see our [Warp Drive Import and Export](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/..#import-and-export) instructions.
