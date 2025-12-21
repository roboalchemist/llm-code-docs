# Source: https://developers.openai.com/codex/ide.md

# Codex IDE extension

Codex is OpenAI's coding agent that can read, edit, and run code. It helps you build faster, squash bugs, and understand unfamiliar code. With the Codex VS Code extension you can use Codex side-by-side in your IDE, or delegate tasks to the cloud.

<YouTubeEmbed
  title="Codex IDE extension overview"
  videoId="sd21Igx4HtA"
  class="w-full"
/>

## Set up the extension

The Codex IDE extension works with VS Code forks such as Insiders, Cursor, or Windsurf.

You can get the Codex extension from the [Visual Studio Code marketplace](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt), or download it for your IDE:

- [Download for Visual Studio Code](vscode:extension/openai.chatgpt)
- [Download for Cursor](cursor:extension/openai.chatgpt)
- [Download for Windsurf](windsurf:extension/openai.chatgpt)
- [Download for Visual Studio Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)

<DocsTip>
  The Codex VS Code extension is available on macOS and Linux. Windows support
  is still experimental. For the best Windows experience, use Codex in a WSL
  workspace and follow our <a href="/codex/windows">Windows setup guide</a>. You
  can also reference the Microsoft docs for
  <a
    href="https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode"
    target="_blank"
    rel="noreferrer noopener"
  >VS Code + WSL</a>.
</DocsTip>

After installing, you'll find the extension in your left sidebar next to other extensions.
If you're using VS Code, you might need to restart VS Code to see the Codex extension on the left sidebar.

If you're using Cursor, this section displays horizontally by default, and collapsed items can hide Codex, so you can pin it and reorganize the order of the extensions.
![codex-extension](https://cdn.openai.com/devhub/docs/codex-extension.webp)

### Adding Codex to the right sidebar <a id="right-sidebar"></a>

In VS Code you should be able to click and drag the Codex icon to the right of your editor screen to move it to the right sidebar to make it more accessible.

In some IDEs, like Cursor, you will have to first change the display of the activity bar temporarily.

Go into your editor settings and search for "activity bar" (in Workbench settings), then change the orientation to "vertical." You'll have to restart your editor to see the changes.

![codex-workbench-setting](https://cdn.openai.com/devhub/docs/codex-workbench-setting.webp)

Now you can drag the Codex icon to the right of your editor screen into the same area as your Cursor chat. Codex now appears as another tab in the sidebar.

After moving it you can reset the activity bar orientation to "horizontal" to restore the default behavior.

### Sign in

Once you have installed the extension, it prompts you to sign in with your ChatGPT account, which is the recommended path.
You get usage credits with your ChatGPT plan, so you can use Codex without any extra setup.
If you wish to use Codex with an API key, you can do so, but this requires extra setup—you can learn more about this and what's included in each plan on the [pricing page](/codex/pricing).

### Update the extension

The extension auto updates, but you can also open the extension page in your IDE to manually check for updates.

### Keyboard shortcuts

Codex offers a series of commands that you can bind as keyboard shortcuts in your IDE settings such as toggling the Codex chat or adding something to the Codex context.

To see all available commands and bind them as keyboard shortcuts, press the Settings icon in the Codex chat and select "Keyboard shortcuts."

## Pair with Codex

Use Codex in your editor to chat, edit, and preview changes seamlessly.
With context from opened files and selected code, you can write shorter prompts and get faster, more relevant results.

You can reference any file in your editor by tagging it in your prompt like this:

```
Use @example.tsx as a reference to add a new page named "Resources" to the app that contains a list of resources defined in @resources.ts
```

### Switch between models

You can use Codex with GPT-5 (default), but consider switching to the newest model optimized for agentic coding in Codex: GPT-5-Codex.

You can switch between models with the switcher under the extension chat input.

![codex-switch-model](https://cdn.openai.com/devhub/docs/codex-switch-model.png)

### Reasoning effort

You can adjust the reasoning effort of Codex to make it think more or less before answering. GPT-5-Codex has the widest range of modulation; with high reasoning effort it will take longer to answer, but it can perform more complex tasks. High effort also uses more tokens and can consume your rate limits when you're using GPT-5-Codex, so start with medium and only switch to high when you need more depth.
If the tasks are short and you need speed, you can use a lower reasoning effort.

You can adjust the reasoning effort with the same model switcher shown above, and choose between `low`, `medium`, and `high` for each model.

### Approval modes

Codex uses a powerful default for how it works on your computer called `Agent`. In this approval mode, Codex can read files, make edits, and run commands in the working directory automatically. Codex still needs your approval to work outside the working directory or access the internet network.

When you just want to chat, or if you want to plan before diving in, you can switch to `Chat` with the switcher under the extension chat input.

![codex-approval-modes](https://cdn.openai.com/devhub/docs/codex-switch-mode.webp)

If you need Codex to read files, make edits, and run commands with network access, without approval, you can use `Agent (Full Access)`. Exercise caution before doing so.

### Detailed docs

The VS Code extension builds on the open source Codex CLI. For more detailed docs covering advanced configuration, MCP, and more, check out the README and docs on the GitHub repository: [github.com/openai/codex](https://github.com/openai/codex).