# Source: https://cobra.dev/docs/how-to-guides/shell-completion/

Title: Shell Completion

URL Source: https://cobra.dev/docs/how-to-guides/shell-completion/

Markdown Content:
This guide shows you how to add shell completion (tab completion) to your existing Cobra CLI application. Shell completion helps users discover commands, flags, and arguments by pressing the Tab key.

Prerequisites
-------------

*   An existing Cobra CLI application
*   Basic knowledge of your target shell (bash, zsh, fish, or PowerShell)
*   Admin/sudo access may be required for system-wide installation

Basic Shell Completion Setup
----------------------------

Cobra provides built-in support for generating completion scripts. First, add a completion command to your application.

1.   **Add Completion Command**

Use the Cobra CLI generator to add a completion command:

`cobra-cli add completion``completion created at /path/to/your-cli` 
2.   **Build Your Application**

Build your CLI with the new completion command:

`go build -o your-cli` 
3.   **Test Basic Completion**

Verify the completion command works:

`./your-cli completion``Generate the autocompletion script for the specified shell` 

Shell-Specific Configuration
----------------------------

### Bash Completion

For Bash users, set up completion with these steps:

1.   **Generate Completion Script**

`./your-cli completion bash > your-cli-completion.bash` 
2.   **Install System-Wide** (recommended)

`sudo cp your-cli-completion.bash /etc/bash_completion.d/` 
3.   **Or Install User-Only**

`mkdir -p ~/.local/share/bash-completion/completions``cp your-cli-completion.bash ~/.local/share/bash-completion/completions/your-cli` 
4.   **Reload Your Shell**

`source ~/.bashrc` 

### Zsh Completion

For Zsh users, follow these steps:

1.   **Generate Completion Script**

`./your-cli completion zsh > _your-cli` 
2.   **Install in Zsh Function Path**

`sudo mkdir -p /usr/local/share/zsh/site-functions``sudo cp _your-cli /usr/local/share/zsh/site-functions/` 
3.   **Or Install User-Only**

`mkdir -p ~/.zsh/completions``cp _your-cli ~/.zsh/completions/``echo 'fpath=(~/.zsh/completions $fpath)' >> ~/.zshrc``echo 'autoload -U compinit && compinit' >> ~/.zshrc` 
4.   **Reload Your Shell**

`source ~/.zshrc` 

### Fish Completion

For Fish shell users:

1.   **Generate and Install Completion**

`./your-cli completion fish > ~/.config/fish/completions/your-cli.fish` 
2.   **Reload Fish Configuration**

`source ~/.config/fish/config.fish` 

### PowerShell Completion

For PowerShell users on Windows, macOS, or Linux:

1.   **Generate Completion Script**

`./your-cli completion powershell > your-cli.ps1` 
2.   **Create PowerShell Profile Directory**

`mkdir -p (Split-Path $PROFILE)` 
3.   **Add to PowerShell Profile**

`Add-Content $PROFILE ". /path/to/your-cli.ps1"` 
4.   **Reload PowerShell**

`& $PROFILE` 

Advanced Features
-----------------

### Custom Completions

Enhance your completion experience by adding custom completion functions to your commands:

`go get github.com/spf13/cobra`

Add custom completions in your command definitions:

go

```
cmd.RegisterFlagCompletionFunc("format", func(cmd *cobra.Command, args []string, toComplete string) ([]string, cobra.ShellCompDirective) {
    return []string{"json", "yaml", "csv"}, cobra.ShellCompDirectiveDefault
})
```

### Dynamic Completions

For file path completions, use Cobra’s built-in directives:

go

`cmd.MarkFlagFilename("config", "yaml", "yml", "json")`

Troubleshooting
---------------

### Completion Not Working

1.   **Check Installation Path**

Verify the completion script is in the correct location for your shell.

2.   **Verify Permissions**

`ls -la /etc/bash_completion.d/your-cli-completion.bash` 
3.   **Check Shell Configuration**

Ensure completion is enabled in your shell configuration file.

### Zsh Compinit Warnings

If you see compinit warnings, fix permissions:

`compaudit | xargs chmod g-w,o-w`

### PowerShell Execution Policy

If PowerShell blocks script execution:

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
