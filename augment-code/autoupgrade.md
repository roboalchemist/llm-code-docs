# Source: https://docs.augmentcode.com/cli/autoupgrade.md

# Automatic Updates

> Learn how to manage and troubleshoot Auggie CLI's automatic update feature.

## How Automatic Updates Work

Auggie CLI automatically updates itself when running in interactive mode to ensure you always have the latest features and bug fixes.

### Interactive Mode (TUI)

* Automatically checks npm for newer versions when you start Auggie
* Performs upgrades without prompting to minimize interruption
* Shows a brief notification when an update is applied
* Best-effort approach - continues running even if update fails

### Non-interactive Mode (Print/Text Mode)

* Auto-update is completely disabled
* Respects version pinning in automation scripts

## Disabling Automatic Updates

Set the `AUGMENT_DISABLE_AUTO_UPDATE` environment variable to `1` to disable automatic updates.

### Environment Variable (Recommended for Scripts)

```bash  theme={null}
# Disable for current session
export AUGMENT_DISABLE_AUTO_UPDATE=1

# Disable for single command
AUGMENT_DISABLE_AUTO_UPDATE=1 auggie --print "Your instruction here"
```

## Manual Updates

You can manually update Auggie CLI by running the following command.

```bash  theme={null}
auggie upgrade
```
