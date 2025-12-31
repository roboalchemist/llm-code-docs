# Source: https://developers.openai.com/codex/integrations/linear.md

# Use Codex in Linear

## Availability

Codex in Linear is available to users on paid plans. ([Pricing](https://chatgpt.com/pricing))

If you're on an Enterprise plan, you may first need to ask your ChatGPT workspace admin to enable both Codex Cloud Tasks in [workspace settings](https://chatgpt.com/admin/settings), and the “Codex for Linear” Connector in [connector settings](https://chatgpt.com/admin/ca).

## Setup

### First, install Codex into your Linear workspace

1. Set up Codex Cloud by [connecting GitHub](https://chatgpt.com/codex), and [set up an environment](https://developers.openai.com/codex/cloud/environments) for the repository you want Codex to work with.
2. Install Codex into your Linear workspace via [Codex settings](https://chatgpt.com/codex/settings/connectors).

### Then, link your Linear account to your ChatGPT account

3. To trigger the link flow, mention @Codex in a comment thread on a Linear issue.

## Delegating to Codex

There are two ways to work with Codex in Linear:

1. **Assign an issue to Codex.** Once installed, you can assign issues to Codex via the same control as assigning to human teammates. After you assign the issue to Codex, it will begin work and keep you apprised of progress.
   <div class="not-prose my-4 -ml-4 sm:-ml-6">
     <img
       src="/images/codex/integrations/linear-assign-codex-light.webp"
       alt="Screenshot of assigning Codex to an issue (light mode)"
       class="block w-full rounded-lg border border-default my-0 dark:hidden"
     />
     <img
       src="/images/codex/integrations/linear-assign-codex-dark.webp"
       alt="Screenshot of assigning Codex to an issue (dark mode)"
       class="hidden w-full rounded-lg border border-default my-0 dark:block"
     />
   </div>
2. **Mention @Codex**. You can also mention @Codex in comment threads to delegate work or ask questions. Once Codex answers, you can follow up in a comment thread to have Codex continue with the same session.
   <div class="not-prose my-4 -ml-4 sm:-ml-6">
     <img
       src="/images/codex/integrations/linear-comment-light.webp"
       alt="Screenshot of mentioning Codex in the comments (light mode)"
       class="block w-full rounded-lg border border-default my-0 dark:hidden"
     />
     <img
       src="/images/codex/integrations/linear-comment-dark.webp"
       alt="Screenshot of mentioning Codex in the comments (dark mode)"
       class="hidden w-full rounded-lg border border-default my-0 dark:block"
     />
   </div>

Once Codex starts working on an issue it will [determine which environment and repo](#how-codex-chooses-an-environment-and-repo) to work on. Alternatively, you can tell Codex which repo to use, such as with “@Codex fix this in openai/codex”.

Afterwards, Codex will continue to stream progress updates to the issue that you can review by opening the “Activity” dialog on the issue. If you want a more detailed view, you can also click on the Codex task link directly to follow along.

Once the task is completed, Codex will comment with a summary and a link to the task so you can create a pull request.

## How Codex chooses an environment and repo

- First, given the repositories you have environments for in Codex, Linear recommends one for Codex to work in. Codex then selects the environment that best matches Linear's recommendation. If the request is ambiguous, it falls back to the environment you used most recently.
- The task runs against the default branch of the first repository listed in that environment’s repo map. Update the repo map in Codex if you need a different default or additional repositories.
- If no suitable environment or repository is available, Codex will reply in Linear with instructions on how to fix the issue before retrying.

## Automatically assign issues to Codex

You can programmatically assign issues to Codex by using triage rules. For this open your team's settings and enable triage. You can find your team settings by going to [Settings](https://linear.app/openai/settings/account/preferences), choosing your team on the left side under "Your teams" and then choosing "Triage" in the workflow section.

Afterwards create a new rule in the “Triage rules” section. Give your rule a name and optionally a trigger. Then choose Delegate → Codex and any other properties you want to set on the issue.

Any new issue that enters triage should now be picked up by Codex automatically. If you use triage rules, Codex will use the account of the issue creator to run the task.

<div class="not-prose my-4">
  <img
    src="/images/codex/integrations/linear-triage-rule-light.webp"
    alt='Screenshot of an example triage rule assigning everything to Codex and labeling it in the "Triage" status (light mode)'
    class="block w-full rounded-lg border border-default my-0 dark:hidden"
  />
  <img
    src="/images/codex/integrations/linear-triage-rule-dark.webp"
    alt='Screenshot of an example triage rule assigning everything to Codex and labeling it in the "Triage" status (dark mode)'
    class="hidden w-full rounded-lg border border-default my-0 dark:block"
  />
</div>

## Data usage, privacy, and security

When you mention `@Codex` or assign an issue to it, your issue’s content is sent to Codex to understand your request and create a task. Data handling follows OpenAI’s [Privacy Policy](https://openai.com/privacy), [Terms of Use](https://openai.com/terms/), and other applicable [policies](https://openai.com/policies). For more on security, see the [Codex Security Guide](https://developers.openai.com/codex/security).  
Codex uses large language models (LLMs) that can make mistakes. Always review answers and diffs carefully.

## Tips and troubleshooting

- **Missing connections** — If Codex cannot confirm your Linear connection, it will tell you in the issue and request you to connect your ChatGPT account.
- **Unexpected environment choice** — Reply in thread with the environment you want (e.g., “@Codex Please run this in openai/codex”).
- **Codex is working in the wrong part of the code** — Especially on a larger code base, vague issues might result in Codex being unsure where to work. Try adding more context in the issue or give explicit instructions by mentioning `@Codex`.
- For more help, see the [OpenAI Help Center](https://help.openai.com/).

## Connecting Codex to Linear for local tasks

If you are using the Codex CLI or IDE Extension and you want Codex to be able to access your Linear issues, you can also configure Codex to use Linear’s Model Context Protocol (MCP) server.

To learn more, [check out the Linear MCP docs](https://linear.app/integrations/codex-mcp).

The setup steps for the MCP server are the same regardless of whether you use the IDE Extension or the CLI since the configuration is shared.

### Preferred: using the CLI

If you have the CLI installed you can run the following command:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp
```

This will automatically prompt you to log in with your Linear account and connect it to your Codex.

**Note:** If this is the first time you are using an MCP in Codex you will need to enable the rmcp feature for this to work. Add the following into your `~/.codex/config.toml`:

```toml
[features]
rmcp_client = true
```

### Manual set up

1. Open the `~/.codex/config.toml` file in your preferred editor
2. Add the following:

```toml
[features]
rmcp_client = true

[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"
```

3. Run `codex mcp login linear` to log in.