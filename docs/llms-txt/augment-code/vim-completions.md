# Source: https://docs.augmentcode.com/vim/using-augment/vim-completions.md

# Completions

> Use code completions to get more done. Augment’s radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## Using completions

Augment’s code completions integrates with Vim and Neovim to give you autocomplete-like suggestions as you type. Completions are enable by default and you can use <Keyboard shortcut="Tab" /> to accept a suggestion.

| Command                                  | Action                                      |
| :--------------------------------------- | :------------------------------------------ |
| <Keyboard shortcut="Tab" />              | Accept the current suggestion               |
| <Keyboard shortcut=":Augment enable" />  | Globally enable suggestions (on by default) |
| <Keyboard shortcut=":Augment disable" /> | Globally disable suggestions                |

### Customizing accepting a suggestion

If you want to use a key other than <Keyboard shortcut="Tab" /> to accept a suggestion, create a mapping that calls `augment#Accept()`. The function takes an optional arugment used to specify the fallback text to insert if no suggestion is available.

```vim  theme={null}
" Use Ctrl-Y to accept a suggestion
inoremap <c-y> <cmd>call augment#Accept()<cr>

" Use enter to accept a suggestion, falling back to a newline if no suggestion
" is available
inoremap <cr> <cmd>call augment#Accept("\n")<cr>
```

You can disable the default <Keyboard shortcut="Tab" /> mapping by setting `g:augment_disable_tab_mapping = v:true` before the plugin is loaded.

<Next>
  * [Using Chat](/vim/using-augment/vim-chat)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>
