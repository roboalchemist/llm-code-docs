# Source: https://novita.ai/docs/guides/codecompanion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CodeCompanion

> Supercharge Your Neovim Workflow with Novita AI and CodeCompanion.nvim.

CodeCompanion.nvim is a lightweight yet powerful Neovim plugin that connects advanced language models (LLMs) directly to your editor, enabling developers to work smarter and faster. With built-in support for Novita AI’s state-of-the-art models, this integration transforms your workflow by offering intelligent code suggestions, automated debugging, and streamlined refactoring tools.

In this comprehensive guide, we’ll walk you through the step-by-step process of setting up Novita AI with CodeCompanion.nvim. Learn how to optimize your Neovim setup and unlock the full power of AI-assisted coding for faster, smarter development.

## How to Leverage Novita AI with CodeCompanion.nvim

You can find the GitHub repository of CodeCompanion.nvim here: [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim).

### Step 1: Generate Your Novita AI API Key

1. [Log in](https://novita.ai/user/login) to your Novita AI account.
2. Access the [Key Management Page](https://novita.ai/settings/key-management).
3. Create a new API key and copy it for later use.

### Step 2: Select a Model

1. Visit the[ Novita AI Model Library](https://novita.ai/models).
2. Choose a model that suits your needs (e.g., `meta-llama/llama-3.1-8b-instruct`).
3. Note down the model name.

### Step 3: Configure CodeCompanion

<Warning>
  We assume you have already installed the Neovim, and if not, you can install it by referring to the [Neovim Installation Guide](https://github.com/neovim/neovim/blob/master/INSTALL.md).
</Warning>

1. Open your [Neovim](https://neovim.io/) configuration file (`init.lua` or equivalent).

<Tip>
  The Neovim configuration file is typically located at: `~/.config/nvim/init.lua` (for macOS or Linux). And you can create this directory and file if they don't exist yet.
</Tip>

2. Install the CodeCompanion plugin.

You can install the plugin by referring to the [CodeCompanion.nvim Installation Guide](https://codecompanion.olimorris.dev/installation.html).

3. Add the following setup for CodeCompanion in your Neovim configuration file:

```lua  theme={"system"}
require("codecompanion").setup({
    adapters = {
        novita = {
            base_url = "https://api.novita.ai/openai",
            api_key = "<YOUR_API_KEY>", -- Replace with your actual API key
            model = "meta-llama/llama-3.1-8b-instruct" -- Replace with your chosen model
        }
    }
})
```

4. Save and reload Neovim.

### Step 4: Verify Integration

1. Run the following command in Neovim:

```vim  theme={"system"}
:checkhealth codecompanion
```

2. Ensure all dependencies are installed and configured correctly.

### Step 5: Test Novita AI Features

1. Open a code file in Neovim and start using CodeCompanion.nvim features such as inline suggestions or chat-based assistance.
2. For example:
   * Use shortcuts to trigger intelligent code completions.
   * Start a chat session by invoking `:CodeCompanionChat` for interactive problem-solving.


Built with [Mintlify](https://mintlify.com).