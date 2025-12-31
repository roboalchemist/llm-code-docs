# Source: https://docs.warp.dev/agents/using-agents/planning.md

# Planning

Warp has native planning functionality that helps you break down complex engineering tasks into structured, executable steps. Planning is tightly integrated with Warp's coding agent and provides a persistent plan editor, version history, selective execution, and deep links into your workspace.

{% embed url="<https://youtu.be/DawcFWyudV0?si=OzvuInMl8DoNR97R>" %}

***

### Creating a Plan

You can generate a plan using the `/plan` [slash command](https://docs.warp.dev/agents/slash-commands) or by asking the agent in natural language in the [universal-input](https://docs.warp.dev/terminal/universal-input "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2dac8a2b54cc62baa10c5e14e0641af2c9303b52%2Fplan-slash-command.png?alt=media" alt="" width="375"><figcaption><p>Prompting the agent to create a plan using the slash command.</p></figcaption></figure>

The agent then creates a structured plan inside Warp’s native rich text editor, which is designed for long, multi-step workflows. The editor includes clean formatting, inline code blocks, and clickable file paths so you can open referenced files immediately in Warp (see below) or in your external editor.

### Reviewing and Editing

Once a plan is generated, you can review it, reorganize steps, or refine details. You can edit the document manually or ask the agent to revise sections for you.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2b9f06a850d55a7cd8369a0e33598ffa3a6a1b37%2Fplanning-main-view.png?alt=media" alt=""><figcaption><p>Plan editor in Warp.</p></figcaption></figure>

Any updates made by the agent **creates a new version**. Version history lets you compare past iterations and restore an older version if you want to revert your approach, preserving a clear decision trail as the plan evolves.

### Executing a Plan

When you’re ready to start implementing, prompt the agent to run the plan. You can ask it to execute the full set of steps or only a specific section, such as “Implement phase 1 of the plan.”

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6a2f4dc0cc2cccd3e7448b85cb3da532d5d53ed6%2Fmanually-trigger-plan.png?alt=media" alt=""><figcaption><p>Manually referencing the plan using @ to kickoff the plan.</p></figcaption></figure>

The agent applies changes incrementally and updates files as it proceeds. This makes it easy to validate early steps before moving forward, adjust the plan mid-run, or try alternative paths without committing to the full workflow.

If you revise the plan while the agent is running, you can notify it directly; the agent will adjust its execution based on your updates.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-ad09cd96d943dcb0c73a7c15baa1e434ac4b918b%2Fupdate-agent-mid-plan.png?alt=media" alt="" width="375"><figcaption><p>Option to pass new plan to agent if plan changes during runtime.</p></figcaption></figure>

### Monitoring Progress

While the agent is running, you can reopen the plan at any time by selecting **View plan** in the [universal-input](https://docs.warp.dev/terminal/universal-input "mention"). You can also follow each change in real time through the [code-review](https://docs.warp.dev/code/code-review "mention") panel and add comments or guidance using [interactive-code-review](https://docs.warp.dev/code/code-review/interactive-code-review "mention").

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4703d53513d43853ad57e375ed190b3e83dab114%2Fview-plan-udi.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

This gives you clear oversight, helps confirm expected behavior, and lets you intervene quickly if something needs correction.

### Saving and Sharing

Warp automatically saves all plans in the *Plans* folder in [warp-drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive "mention"). You can export any plan as Markdown, check it into your repository, or share a link—useful for GitHub PRs, design reviews, or async collaboration.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-03cb4b5e7d423b431f583a10bf6ae9aacbf67999%2Fexport-notebooks.png?alt=media" alt="" width="375"><figcaption><p>Different ways to share a plan.</p></figcaption></figure>

Because plans persist in Warp Drive, you can return to them later, reuse them for new work, or treat them as documentation for ongoing projects. This is also naturally passed to the agent as context.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-34bb48924cc40fb7ba788480e93cf6ea7b2b6e37%2Fplans-in-drive.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

You can configure whether your plans will be automatically added and synced to Warp drive In your [agent-profiles-permissions](https://docs.warp.dev/agents/using-agents/agent-profiles-permissions "mention") under `Settings > AI > Agents > Profiles`.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4309952619d934effc5f1ac575a86538abff8334%2Fauto-sync-plans.png?alt=media" alt="" width="371"><figcaption></figcaption></figure>

### Using Plans Across Conversations

Plans are reusable across tasks and sessions. You can reference them in future prompts, continue where you left off, or build follow-up plans that rely on earlier work.

The **@plans** command helps you quickly search for and reopen previously saved plans, making planning a consistent part of your development workflow rather than a one-off step. Learn more about attaching context using @ [here](https://docs.warp.dev/agents/using-agents/agent-context/using-to-add-context).

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-bc2e9b17ad413a97c3f265de815c8f9dd0d2996f%2F%40-reference-plans.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>
