# Source: https://developers.openai.com/codex/cli.md

# Codex CLI

<div class="grid grid-cols-1 lg:grid-cols-2 gap-12 pb-16 lg:pb-24">
  <YouTubeEmbed
    title="Codex CLI overview"
    videoId="iqNzfK4_meQ"
    class="order-1 w-full max-w-xl mx-auto lg:mx-0 lg:order-1"
  />
  <div class="text-secondary [&_p]:text-secondary! order-2 text-lg content-center lg:order-2">
    Codex CLI is a coding agent that you can run locally from your terminal and
    that can read, modify, and run code on your machine, in the chosen
    directory. It's open source, built in Rust for speed and efficiency, and
    rapidly improving at [openai/codex](https://github.com/openai/codex) on
    GitHub.
  </div>
</div>

<h2 class="text-center lg:heading-2xl! mb-8 lg:pt-4">
  <span>Get started with the Codex&nbsp;CLI</span>
</h2>

<CliSetupSteps client:load />

<h2 class="text-center lg:heading-2xl! mb-8 lg:pt-4">
  <span>Working with the Codex CLI</span>
</h2>

<BentoContainer>
  <BentoContent href="/codex/cli/features#running-in-interactive-mode">

### Run Codex interactively

To pair with Codex in your terminal, run `codex` to start up an interactive terminal UI (TUI) session.

  </BentoContent>
  <BentoContent href="/codex/cli/features#models-reasoning">

### Control model & reasoning

Switch between GPT-5-Codex and GPT-5 or adjust reasoning levels with `/model` whenever you need deeper analysis.

  </BentoContent>
  <BentoContent href="/codex/cli/features#image-inputs">

### Image inputs

Attach screenshots or design specs so Codex reads them alongside your prompt.

  </BentoContent>

  <BentoContent href="/codex/cli/features#running-local-code-review">
### Run local code review

Get your code reviewed by a separate Codex agent before you commit or push your changes.

  </BentoContent>

  <BentoContent href="/codex/cli/features#web-search">

### Web search

Use Codex to search the web for information and get up-to-date information for your task.

  </BentoContent>

  <BentoContent href="/codex/cli/features#working-with-codex-cloud">

### Codex Cloud tasks

Launch Codex Cloud task, pick environments, and apply the resulting diffs without leaving your terminal.

  </BentoContent>

  <BentoContent href="/codex/sdk#using-codex-cli-programmatically">

### Scripting Codex

Automate repeatable workflows by scripting Codex with the `exec` command.

  </BentoContent>
  <BentoContent href="/codex/mcp">

### Model Context Protocol

Give Codex access to additional third-party tools and context with Model Context Protocol (MCP).

  </BentoContent>
  
  <BentoContent href="/codex/cli/features#approval-modes">

### Approval modes

Choose the approval mode that matches your comfort level before Codex edits or runs commands.

  </BentoContent>
</BentoContainer>

<h2 class="text-center lg:heading-2xl! mt-12">
  <span>Take Codex everywhere</span>
</h2>

<div class="grid grid-cols-1 gap-6 lg:grid-cols-3 not-prose">
  <CodexHighlightCard
    title="Codex Cloud"
    imageSrc="/images/codex/codex_web.webp"
    url="/codex/cloud"
    class="lg:h-[400px]"
  />
  <CodexHighlightCard
    title="Codex IDE Extension"
    imageSrc="/images/codex/codex_cover_extension.webp"
    url="/codex/ide"
    titlePlacement="bottom-right"
    class="lg:h-[400px]"
  />
  <CodexHighlightCard
    title="Codex for Slack"
    imageSrc="/images/codex/codex_slack.webp"
    url="/codex/integrations/slack"
    class="lg:h-[400px]"
  />
</div>

<h2 class="text-center lg:heading-2xl! mt-12 pt-4 lg:pt-4">
  <span>Next steps</span>
</h2>

<div class="grid grid-cols-1 gap-6 not-prose md:grid-cols-2 lg:grid-cols-4">
  <div class="h-full">
    <CodexCard
      title="Use AGENTS.md files"
      description="Give Codex additional instructions and context for your project."
      imageSrc={resourceImage("codex", 1)}
      slug="guides/agents-md"
      icon="NotebookText"
    />
  </div>
  <div class="h-full">
    <CodexCard
      title="Slash commands"
      description="Learn how to use slash commands to use built-in Codex functionality or create your own for common prompts."
      imageSrc={resourceImage("codex", 2)}
      slug="guides/slash-commands"
      icon="SlashCommand"
    />
  </div>
  <div class="h-full">
    <CodexCard
      title="Model Context Protocol"
      description="Connect Codex to third-party tools and extended context using MCP."
      imageSrc={resourceImage("codex", 3)}
      slug="mcp"
      icon="MCP"
    />
  </div>
  <div class="h-full">
    <CodexCard
      title="Automate fixes in CI"
      description="Use Codex Autofix to review diffs and ship clean builds automatically."
      imageSrc={resourceImage("codex", 4)}
      slug="guides/autofix-ci"
      icon="Bug"
    />
  </div>
</div>