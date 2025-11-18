# Source: https://docs.augmentcode.com/vim/setup-augment/install-vim-neovim.md

# Install Augment for Vim and Neovim

> Augment for Vim and Neovim gives you powerful code completions and chat capabilities integrated into your favorite code editor.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const NeoVimLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_1012_311)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M2.11719 5.0407L7.2509 -0.14502V23.9669L2.11719 18.841V5.0407Z" fill="url(#paint0_linear_1012_311)" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M21.9551 5.08747L16.7572 -0.14502L16.8625 23.9669L21.9902 18.8404L21.9551 5.08747Z" fill="url(#paint1_linear_1012_311)" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M7.25 -0.111816L20.5981 20.2637L16.8629 24.0001L3.50781 3.66964L7.25 -0.111816Z" fill="url(#paint2_linear_1012_311)" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M7.24955 9.28895L7.24248 10.0894L3.14258 4.01872L3.52221 3.63086L7.24955 9.28895Z" fill="black" fill-opacity="0.13" />
</g>
<defs>
<linearGradient id="paint0_linear_1012_311" x1="258.803" y1="-0.14502" x2="258.803" y2="2411.04" gradientUnits="userSpaceOnUse">
<stop stop-color="#16B0ED" stop-opacity="0.800236" />
<stop offset="1" stop-color="#0F59B2" stop-opacity="0.837" />
</linearGradient>
<linearGradient id="paint1_linear_1012_311" x1="-239.663" y1="-0.14502" x2="-239.663" y2="2411.04" gradientUnits="userSpaceOnUse">
<stop stop-color="#7DB643" />
<stop offset="1" stop-color="#367533" />
</linearGradient>
<linearGradient id="paint2_linear_1012_311" x1="858.022" y1="-0.111816" x2="858.022" y2="2411.08" gradientUnits="userSpaceOnUse">
<stop stop-color="#88C649" stop-opacity="0.8" />
<stop offset="1" stop-color="#439240" stop-opacity="0.84" />
</linearGradient>
<clipPath id="clip0_1012_311">
<rect width="24" height="24" fill="white" />
</clipPath>
</defs>
</svg>;

export const ExternalLink = ({text, href}) => <a href={href} rel="noopener noreferrer">
    {text}
  </a>;

<CardGroup cols={1}>
  <Card title="Get the Augment Extension" href="https://github.com/augmentcode/augment.vim" icon={<NeoVimLogo />} horizontal>
    View Augment for Vim and Neovim on GitHub
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink text="Augment for Vim and Neovim" href="https://github.com/augmentcode/augment.vim" /> is easy and will take you less than a minute. You can install the extension manually or you can use your favorite plugin manager.

## Prerequisites

Augment for Vim and Neovim requires a compatible version of Vim or Neovim, and Node.js:

| Dependency                                                                                     | Minimum version |
| :--------------------------------------------------------------------------------------------- | :-------------- |
| [Vim](https://github.com/vim/vim?tab=readme-ov-file#installation)                              | 9.1.0           |
| [Neovim](https://github.com/neovim/neovim/tree/master?tab=readme-ov-file#install-from-package) | 0.10.0          |
| [Node.js](https://nodejs.org/en/download/package-manager/all)                                  | 22.0.0          |

## 1. Install the extension

<Tabs>
  <Tab title="Neovim">
    ### Manual Installation

    ```sh  theme={null}
    git clone https://github.com/augmentcode/augment.vim.git ~/.config/nvim/pack/augment/start/augment.vim
    ```

    ### Using Lazy.nvim

    Add the following to your `init.lua` file, then run `:Lazy sync` in Neovim. See more details about using [Lazy.nvim on GitHub](https://github.com/folke/lazy.nvim).

    ```lua  theme={null}
    require('lazy').setup({
      -- Your other plugins here
      'augmentcode/augment.vim',
    })
    ```
  </Tab>

  <Tab title="Vim">
    ### Manual Installation

    ```sh  theme={null}
    git clone https://github.com/augmentcode/augment.vim.git ~/.vim/pack/augment/start/augment.vim
    ```

    ### Using Vim Plug

    Add the following to your `.vimrc` file, then run `:PlugInstall` in Vim. See more details about using [Vim Plug on GitHub](https://github.com/junegunn/vim-plug).

    ```vim  theme={null}
    call plug#begin()

    " Your other plugins here
    Plug 'augmentcode/augment.vim'

    call plug#end()
    ```
  </Tab>
</Tabs>

## 2. Configure your workspace context

Add your project root to your workspace context by setting `g:augment_workspace_folders` in your `.vimrc` or `init.lua` file before the plugin is loaded. For example:

```vim  theme={null}
" Add to your .vimrc
let g:augment_workspace_folders = ['/path/to/project']

" Add to your init.lua
vim.g.augment_workspace_folders = {'/path/to/project'}
```

Augment's Context Engine provides the best suggestions when it has access to your project's codebase and any related repositories. See more details in
[Configure additional workspace context](/vim/setup-augment/workspace-context-vim).

## 3. Sign-in to Augment

Open Vim or Neovim and sign-in to Augment with the following command:

```vim  theme={null}
:Augment signin
```

<Next>
  * [Using Chat with Vim and Neovim](/vim/using-augment/vim-chat)
  * [Using Completions with Vim and Neovim](/vim/using-augment/vim-completions)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>
