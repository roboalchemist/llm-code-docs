# Source: https://grafbase.com/docs/cli/commands/completions.md

# Grafbase Completions Command

Grafbase generates shell completion scripts for various shells. Put the file in your shell's location.

**Usage:**

```bash
grafbase completions <COMMAND>
```

**Arguments:**

- `<COMMAND>`: The shell to generate the completion script for. Either `bash`, `elvish`, `fish`, `powershell`, or `zsh`.

## Examples

Generate a bash completion script:

```bash
./grafbase completions bash >> ~/.bashrc
```

Generate a fish completion script:

```bash
./grafbase completions fish >> ~/.config/fish/completions/grafbase.fish
echo "source ~/.config/fish/completions/grafbase.fish" > ~/.config/fish/conf.d/grafbase.fish
```

Generate an elvish completion script:

```bash
grafbase completions elvish > ~/.elvish/lib/grafbase-completions.elv
echo "use grafbase-completions" >> ~/.elvish/rc.elv
```

Generate a zsh completion script:

```bash
grafbase completions zs >> ~/.zshrc
```

Generate a PowerShell completion script:

```bash
grafbase completions powershell >> $PROFILE.CurrentUserAllHosts
```