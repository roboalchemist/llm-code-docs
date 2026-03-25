# Source: https://www.apollographql.com/docs/rover/commands/completion.md

# Rover completion Commands

Rover provides shell completion support for bash and zsh, enabling tab completion for Rover commands and their options. This makes it easier to discover available commands and options while working in the terminal.

## Generating completion scripts

### `completion bash`

The `completion bash` command generates a bash completion script:

```text
rover completion bash
```

This outputs a bash completion script to `stdout`. To enable bash completion, save the output to a file and source it in your shell configuration:

```bash
# Save the completion script
rover completion bash > ~/.rover-completion.bash

# Add to your ~/.bashrc or ~/.bash_profile
echo "source ~/.rover-completion.bash" >> ~/.bashrc

# Reload your shell configuration
source ~/.bashrc  # or restart your terminal
```

You'll now have tab completion for Rover commands.

### `completion zsh`

The `completion zsh` command generates a zsh completion script:

```text
rover completion zsh
```

This outputs a zsh completion script to `stdout`. To enable zsh completion, save the output to a file and source it in your shell configuration:

```zsh
# Save the completion script
rover completion zsh > ~/.rover-completion.zsh

# Add to your ~/.zshrc
echo "source ~/.rover-completion.zsh" >> ~/.zshrc

# Reload your shell configuration
source ~/.zshrc  # or restart your terminal
```

You'll now have tab completion for Rover commands.

Alternatively, you can use zsh's completion system by placing the script in your `fpath`:

```zsh
# Create completion directory if it doesn't exist
mkdir -p /usr/local/share/zsh/site-functions

# Save the completion script to fpath
rover completion zsh > /usr/local/share/zsh/site-functions/_rover

# Reload completions (or restart your terminal)
compinit
```

## Using completion

Once enabled, you can use tab completion to:

* Complete command names: Type `rover ` and press `Tab` to see available commands
* Complete subcommands: Type `rover graph ` and press `Tab` to see available graph subcommands
* Complete options: Type `rover graph publish ` and press `Tab` to see available options and flags

## Testing completion

To verify that completion is working correctly:

1. Open a new terminal or reload your shell configuration
2. Type `rover ` (with a space) and press `Tab` - you should see a list of available commands
3. Type `rover gra` and press `Tab` - it should autocomplete to `rover graph`
4. Continue typing `rover graph ` and press `Tab` - you should see available subcommands like `check`, `publish`, `fetch`, etc.

If completion isn't working, ensure that:

* You've reloaded your shell configuration or opened a new terminal
* The completion script file exists and is readable
* For bash: The script is being sourced in your `~/.bashrc` or `~/.bash_profile`
* For zsh: The script is being sourced in your `~/.zshrc` or is in your `fpath`
