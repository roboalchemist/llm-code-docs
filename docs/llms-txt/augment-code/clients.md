# Source: https://docs.augmentcode.com/cli/acp/clients.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ACP Clients

> Configure Auggie to run in any Agent Client Protocol (ACP) compatible client like Zed, Neovim, or Emacs.

## About ACP Clients

[Agent Client Protocol](https://agentclientprotocol.com/overview/introduction) (ACP) is an open protocol that provides a standardized way to connect AI agents to different text editors, IDEs, and other tools. Auggie is a fully ACP compatible agent enabling you to bring the power of Augment to editors like Zed, Neovim, or Emacs. See a [full list of supported clients](https://agentclientprotocol.com/overview/clients) in the ACP docs.

## Prerequisites

* Auggie CLI [installed and configured](/cli/setup-auggie/install-auggie-cli)
* Login to Augment with `auggie login`
* A compatible ACP client

## Client configuration

If you have an ACP client that you would like to have listed here, please [open an issue](https://github.com/augmentcode/auggie/issues/new) and we'll be happy to add it.

### Zed

<Note>
  We recommend installing and configuring Auggie in [Zed](https://zed.dev/) using the [Auggie extension](https://zed.dev/extensions/auggie).
</Note>

If you want to configure Auggie manually through Zed's settings, you can use the following configuration. You can pass additional [command-line arguments](/cli/reference) to Auggie by adding them to the `args` array or use alternative [authentication methods](/cli/setup-auggie/authentication) by passing environment variables in the `env` object.

```
{
  "agent_servers": {
    "Auggie CLI": {
      "command": "auggie",
      "args": ["--acp"],
      "env": {}
    }
  }
}
```

### JetBrains

<Note>
  We recommend installing and configuring Augment in [JetBrains IDEs](/jetbrains/setup-augment/install-jetbrains-ides) using the [Augment extension](https://plugins.jetbrains.com/plugin/24072-augment-ai-coding-assistant-for-professionals).
</Note>

To use Auggie with JetBrains IDEs, you can configure it in your IDE settings. You can pass additional [command-line arguments](/cli/reference) to Auggie by adding them to the `args` array or use alternative [authentication methods](/cli/setup-auggie/authentication) by passing environment variables in the `env` object.

```json  theme={null}
{
  "agent_servers": {
    "Auggie CLI": {
      "command": "auggie",
      "args": [
        "--acp"
      ],
      "env": {}
    }
  }
}
```

### Neovim

To use Auggie with Neovim, you can use one of the following plugins:

#### [**Avante.nvim**](https://github.com/yetone/avante.nvim)

Add the following to your lazy.nvim configuration:

```lua  theme={null}
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    build = "make",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
    },
    opts = {
      provider = "auggie-acp",
      acp_providers = {
        ["auggie-acp"] = {
          command = "auggie",
          args = { "--acp" },
        },
      },
      behaviour = {
        auto_suggestions = false,
        auto_set_highlight_group = true,
        auto_set_keymaps = true,
        auto_apply_diff_after_generation = false,
        support_paste_from_clipboard = false,
      },
    },
  },

```

#### [**Agentic.nvim**](https://github.com/carlos-algms/agentic.nvim)

Add the following to your lazy.nvim configuration:

```lua  theme={null}
{
  "carlos-algms/agentic.nvim",
  opts = {
    provider = "auggie-acp",
    acp_providers = {
      ["auggie-acp"] = {
        command = "auggie",
        args = { "--acp" },
      },
    },
  },
}
```

#### [**CodeCompanion.nvim**](https://github.com/olimorris/codecompanion.nvim)

Add the following to your lazy.nvim configuration:

```lua  theme={null}
{
  "olimorris/codecompanion.nvim",
  opts = {
    strategies = {
      chat = {
        adapter = "auggie_cli",
      },
      inline = {
        adapter = "auggie_cli",
      },
    },
  },
}
```

### Emacs

To use Auggie with emacs, you can use one of the following plugins:

* [agent-shell.el](https://github.com/xenodium/agent-shell)
