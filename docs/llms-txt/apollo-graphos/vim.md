# Source: https://www.apollographql.com/docs/ide-support/vim.md

# Graph Development in Vim and NeoVim

This guide outlines how to set up the Apollo Language Server in NeoVim using its native Language Server Protocol (LSP) client or in Vim/NeoVim using the `coc.nvim` plugin.
With this setup, you can get the same validations that composition provides, with errors and hints highlighted in your schema files on each save.

## Prerequisites

* A  current Vim or NeoVim installation
  * If using NeoVim you must use version >=5.0 to use its native LSP
  * Otherwise, the `coc.nvim` plugin also provides an LSP client and can be used with Vim version >= 9.0.0438 and NeoVim version >= 0.8.
* Rover version 0.27.0 or later

## Using NeoVim's (\<= v10.x) native LSP client

Version 11.0 of NeoVim (not yet released as of January 2025, when this document was written) has a new LSP client configuration format. We will update this documentation after v11.0's release.

NeoVim's native LSP client makes integrating language servers, including the Apollo Language Server, straightforward. This guide doesn't cover keybindings or UI customization, but the following configuration will set up `nvim` to work with Apollo Connectors.

### Configuration

Add the following snippet to your `init.lua` or any other Lua configuration file for NeoVim:

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'graphql',
  callback = function(ev)
    vim.lsp.start({
      name = 'apollo-language-server',

      -- If you're using a profile, you can append `'--profile', 'default'`
      -- to this list (substitute `default` for your profile name)
      cmd = {'rover', 'lsp', '--supergraph-config', 'supergraph.yaml'},

      -- Set the "root directory" to the parent directory of the file in the
      -- current buffer (`ev.buf`) that contains a `supergraph.yaml` file.
      root_dir = vim.fs.root(ev.buf, {'supergraph.yaml'}),
    })
  end,
})
```

### Notes

* The **File Type Autocommand** configuration triggers whenever a file with the type `graphql` is opened. If you want to be more selective about the types of files you want to use with the Apollo Language Server, modify this logic to suit your preferences.
* For more information about NeoVim's native LSP client, run the `:help lsp` command in `nvim`.

## Using `coc.nvim` with Vim/NeoVim

If you're using [`coc.nvim`](https://github.com/neoclide/coc.nvim) as your LSP client, you can configure it to work with the Apollo Language Server with a few lines of configuration.

### Configuration

Add the following to your `coc-settings.json` file, usually located in `~/.vim/coc-settings.json` or `~/.config/nvim/coc-settings.json`. Alternatively, run the command `:CocConfig` in any buffer to open the config file. Add the following:

```jsonc
{
  // ...
  "languageserver": {
    "apollo-language-server": {
      "command": "rover",

      // If you're using a profile, you can append `'--profile', 'default'`
      // to this list (substitute `default` for your profile name)
      "args": ["lsp", "--supergraph-config", "supergraph.yaml"],
      "filetypes": ["graphql"],

      // Set the "root directory" to the parent directory of the file in the
      // current buffer that contains a `supergraph.yaml` file.
      "rootPatterns": ["supergraph.yaml"]
    }
  }
}
```

### Notes

* Refer to the `coc.nvim` documentation for more info:
  * [Using the configuration file](https://github.com/neoclide/coc.nvim/wiki/Using-the-configuration-file)
  * [Register custom language servers](https://github.com/neoclide/coc.nvim/wiki/Language-servers#register-custom-language-servers)
  * [Debug language server](https://github.com/neoclide/coc.nvim/wiki/Debug-language-server)
