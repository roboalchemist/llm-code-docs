# Source: https://docs.augmentcode.com/vim/setup-augment/vim-keyboard-shortcuts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Commands and shortcuts for Vim and Neovim

> Augment flexibly integrates with your editor to provide keyboard shortcuts for common actions. Customize your keymappings to quickly accept suggestions and chat with Augment.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## All available commands

| Command                                         | Action                                      |
| :---------------------------------------------- | :------------------------------------------ |
| <Keyboard shortcut=":Augment enable" />         | Globally enable suggestions (on by default) |
| <Keyboard shortcut=":Augment disable" />        | Globally disable suggestions                |
| <Keyboard shortcut=":Augment chat <message>" /> | Send a chat message to Augment              |
| <Keyboard shortcut=":Augment chat-new" />       | Start a new chat conversation               |
| <Keyboard shortcut=":Augment chat-toggle" />    | Toggle the chat panel visibility            |
| <Keyboard shortcut=":Augment signin" />         | Start the sign in flow                      |
| <Keyboard shortcut=":Augment signout" />        | Sign out of Augment                         |
| <Keyboard shortcut=":Augment status" />         | View the current status of the plugin       |
| <Keyboard shortcut=":Augment log" />            | View the plugin log                         |

## Creating custom shortcuts

You can create custom shortcuts for any of the above commands by adding mappings to your `.vimrc` or `init.lua` file. For example, to create a shortcut for the :Augment chat\* commands, you can add the following mappings:

```vim  theme={null}
" Send a chat message in normal and visual mode
nnoremap <leader>ac :Augment chat<CR>
vnoremap <leader>ac :Augment chat<CR>

" Start a new chat conversation
nnoremap <leader>an :Augment chat-new<CR>

" Toggle the chat panel visibility
nnoremap <leader>at :Augment chat-toggle<CR>
```

## Customizing accepting a completion suggestion

By default <Keyboard shortcut="Tab" /> is used to accept a suggestion. If you want to use a key other than <Keyboard shortcut="Tab" /> to accept a suggestion, create a mapping that calls `augment#Accept()`. The function takes an optional arugment used to specify the fallback text to insert if no suggestion is available.

```vim  theme={null}
" Use Ctrl-Y to accept a suggestion
inoremap <c-y> <cmd>call augment#Accept()<cr>

" Use enter to accept a suggestion, falling back to a newline if no suggestion
" is available
inoremap <cr> <cmd>call augment#Accept("\n")<cr>
```

You can disable the default <Keyboard shortcut="Tab" /> mapping by setting `g:augment_disable_tab_mapping = v:true` before the plugin is loaded.
