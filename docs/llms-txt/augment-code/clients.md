# Source: https://docs.augmentcode.com/cli/acp/clients.md

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

### Neovim

To use Auggie with neovim, you can use one of the following plugins:

* [CodeCompanion](https://github.com/olimorris/codecompanion.nvim)
* [Avante](https://github.com/yetone/avante.nvim?tab=readme-ov-file#enabling-acp)

### Emacs

To use Auggie with emacs, you can use one of the following plugins:

* [agent-shell.el](https://github.com/xenodium/agent-shell)
