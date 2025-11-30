# Source: https://developer.1password.com/docs/cli/config-directories

# How 1Password CLI detects configuration directories

1Password CLI configuration directories default to:

- `$/op` when `$` is set
- `~/.config/op` when `$` is not set

1Password CLI detects the configuration directory to read or write to in this order of precedence:

1.  A directory specified with `--config`
2.  A directory set with the `OP_CONFIG_DIR` environment variable.
3.  `~/.op` (following [go-homedir ](https://github.com/mitchellh/go-homedir) to determine the home directory)
4.  `$/.op`
5.  `~/.config/op` (following [go-homedir ](https://github.com/mitchellh/go-homedir) to determine the home directory)
6.  `$/op`