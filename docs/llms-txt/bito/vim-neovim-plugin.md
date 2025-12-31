# Source: https://docs.bito.ai/ai-code-reviews-in-ide/installation-guide/vim-neovim-plugin.md

# Vim/Neovim Plugin

We are excited to announce that one of our users has developed a dedicated Vim and Neovim plugin for Bito, integrating it seamlessly with your favorite code editor. This plugin enhances your coding experience by leveraging the power of Bito's AI capabilities directly within Vim and Neovim.

**Installation**

To get started with "vim-bitoai," follow these steps:

**Step 1: Install Bito CLI**

Make sure you have Bito CLI installed on your system. If you haven't installed it, you can find detailed instructions in the Bito CLI repository at[ https://github.com/gitbito/CLI](https://github.com/gitbito/CLI).

**Step 2: Install the Plugin**

Open your terminal and navigate to your Vim or Neovim plugin directory. Then, clone the "vim-bitoai" repository using the following command:

```sh
git clone https://github.com/zhenyangze/vim-bitoai.git

```

**Step 3: Configure the Plugin**

Open your Vim or Neovim configuration file and add the following lines:

```sh
" Vim Plug
Plug 'zhenyangze/vim-bitoai'

" NeoBundle
NewBundle 'zhenyangze/vim-bitoai'

" Vundle
Plugin 'zhenyangze/vim-bitoai'
```

Save the configuration file and restart your editor or run :source \~/.vimrc (for Vim) or  :source \~/.config/nvim/init.vim (for Neovim) to load the changes.

**Step 4: Verify the Installation**

Open Vim or Neovim, and you should now have the "vim-bitoai" plugin installed and ready to use.

**Usage**

You can use its powerful features once you have installed the "vim-bitoai" plugin. Here are some of the available commands:

* BitoAiGenerate: Generates code based on a given prompt.
* BitoAiGenerateUnit: Generates unit test code for the selected code block.
* BitoAiGenerateComment: Generates comments for methods, explaining parameters and output.
* BitoAiCheck: Performs a check for potential issues in the code and suggests improvements.
* BitoAiCheckSecurity: Checks the code for security issues and provides recommendations.
* BitoAiCheckStyle: Checks the code for style issues and suggests style improvements.
* BitoAiCheckPerformance: Analyzes the code for performance issues and suggests optimizations.
* BitoAiReadable: Organizes the code to enhance readability and maintainability.
* BitoAiExplain: Generates an explanation for the selected code.

To execute a command, follow these steps:

1. Open a file in Vim or Neovim that you want to work on.
2. Select the code block you want to act on. You can use visual mode or manually specify the range using line numbers.
3. Execute the desired command by running the corresponding command in command mode. For example, to generate code based on a prompt, use the : BitoAiGenerate command.\
   Note: Some commands may prompt you for additional information or options.
4. The plugin will communicate with the Bito CLI and execute the command, providing the output directly within your editor.

By leveraging the "vim-bitoai" plugin, you can directly harness the power of Bito's AI capabilities within your favorite Vim or Neovim editor. This integration lets you streamline your software development process, saving time and effort in repetitive tasks and promoting efficient coding practices.

**Customization**

The "vim-bitoai" plugin also offers customization options tailored to your specific needs. Here are a few variables you can configure in your Vim or Neovim configuration file:

* **g:bito\_buffer\_name\_prefix:** Sets the prefix for the buffer name in the Bito history. By default, it is set to 'bito\_history\_'.
* **g:vim\_bito\_path:** Specifies the path to the Bito CLI executable. If the Bito CLI is not in your system's command path, you can provide the full path to the executable.
* **g:vim\_bito\_prompt\_{command}:** Allows you to customize the prompt for a specific command. Replace {command} with the desired command.

To define a custom prompt, add the following line to your Vim or Neovim configuration file and replace your prompt with the desired prompt text:

```javascript
if !exists("g:vim_bito_prompt_{command}")
    let g:vim_bito_prompt_{command}="your prompt"
endif
```

Remember to restart your editor or run the appropriate command to load the changes.

We encourage you to explore the "vim-bitoai" plugin and experience the benefits of seamless integration between Bito and your Vim or Neovim editor. Feel free to contribute to the repository or provide feedback to help us further improve this plugin and enhance your coding experience.
