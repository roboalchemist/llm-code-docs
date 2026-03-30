# Source: https://docs.safetycli.com/safety-docs/firewall/using-firewall/troubleshooting.md

# Troubleshooting

## Verifying Installation

### Problem: Command Not Found

If you see `safety: command not found` or similar errors:

1. Verify that Safety CLI is installed:

   ```bash
   pip list | grep safety-cli
   ```
2. Ensure the installation directory is in your PATH:

   ```bash
   echo $PATH
   ```
3. Reinstall Safety CLI if needed:

   ```bash
   pip install --upgrade safety-cli
   ```

### Problem: "No such command" for Firewall Commands

If you see `Error: No such command 'init'` or `Error: No such command 'firewall'`:

1. Verify that you're authenticated:

   ```bash
   safety auth status
   ```
2. If not authenticated, log in:

   ```bash
   safety auth login
   ```
3. Verify that your account has the Firewall feature enabled in Safety Platform

{% hint style="warning" %}
If you're logged in but still can't access Firewall commands, your organization may not have the Firewall feature enabled. Contact your Safety administrator or [reach out to support](mailto:support@safetycli.com).
{% endhint %}

## Alias Configuration Issues

#### Problem: Package Manager Not Aliased

If `which pip` doesn't show `pip is aliased to safety pip`:

1. Reload your shell configuration:

   ```bash
   source ~/.safety/.safety_profile # or ~/.bashrc, ~/.zshrc, etc.
   ```
2. If that doesn't work, check the alias in your profile file:

   ```bash
   grep -r "alias pip=" ~/.profile ~/.bashrc ~/.zshrc 2>/dev/null
   ```
3. If the alias is missing, run the installation again:

   ```bash
   safety init
   ```

{% hint style="info" %}
On Windows, we recommend restarting your terminal after installation to ensure the alias takes effect.
{% endhint %}

## Alias Not Working After System Restart

If aliases stop working after restarting your system:

1. Check which shell you're using:

   ```bash
   echo $SHELL
   ```
2. Ensure Safety added aliases to the correct profile file for your shell
3. Add the source command to your shell's startup file if needed

{% hint style="info" %}
On macOS or Linux, you can add `source ~/.safety/shell/profile.sh` to your shell's startup file to ensure aliases are always loaded.&#x20;
{% endhint %}

## Authentication Issues

### Unable to Authenticate

If you're having trouble authenticating:

1. Ensure you have a valid Safety account
2. Check your internet connection
3. Try authenticating with the verbose flag:

   ```bash
   safety auth login --verbose
   ```
4. If the browser doesn't open automatically, manually copy and paste the URL from the terminal

### Authentication Unexpectedly Fails

If you suddenly lose authentication:

1. Check your authentication status:

   ```bash
   safety auth status
   ```
2. Re-authenticate if needed:

   ```bash
   safety auth login
   ```
3. Check if your organization's API key has been rotated (for organization admins)

## Firewall Uninstallation Issues

### Unable to Uninstall Firewall

If `safety firewall uninstall` fails with "No such command":

1. First, ensure you're authenticated:

   ```bash
   safety auth login
   ```
2. If still unable to uninstall, manually remove the aliases:
   * Check your shell profile files (\~/.bashrc, \~/.zshrc, etc.) for Safety aliases
   * Remove the Safety-related lines
   * Delete the \~/.safety directory:

     ```bash
     rm -rf ~/.safety
     ```

{% hint style="info" %}
Manually uninstalling should be a last resort. This process will remove all Safety configuration from your system.
{% endhint %}

## Package Installation Issues

### Slow Package Installation

If package installations through Safety Firewall are slower than expected:

1. This is normal behaviour in the current version of Safety Firewall
2. Future versions will improve performance by streaming packages while analyzing them

{% hint style="info" %}
The slight increase in installation time is a trade-off for the security benefits of preventing vulnerable or malicious packages from entering your system.
{% endhint %}

### Unexpected Blocking of Packages

If legitimate packages are being blocked:

1. Check your organization's policies in Safety Platform
2. Look for overly restrictive rules that might be causing false positives
3. Consider temporarily modifying the policy to use warnings instead of blocks
4. If the package is incorrectly flagged, report it to [Safety support](mailto:support@safetycli.com)

## Codebase Issues

### Codebase Not Appearing in Platform

If your codebase doesn't appear in Safety Platform after configuration:

1. Verify the codebase is properly initialized:

   ```bash
   ls -la | grep .safety-project.ini
   ```
2. Ensure you've run a scan at least once:

   ```bash
   safety scan
   ```
3. Check that you're authenticated with the correct organization:

   ```bash
   safety auth status
   ```

### Automatic Scans Not Working

If automatic scans aren't running after package installations:

1. Verify that you're in a properly configured codebase directory
2. Check the `.safety-project.ini` file for any configuration issues
3. Verify package manager alias is working correctly (use `which pip`)
4. Run a manual scan to check if scanning works at all:

   ```bash
   safety scan --verbose
   ```

## Platform Connection Issues

### CLI Can't Connect to Platform

If the CLI can't connect to Safety Platform:

1. Check your internet connection
2. Verify your authentication:

   ```bash
   safety auth status
   ```
3. Check for proxy or firewall issues in your network
4. Try with the verbose flag to see more details:

   ```bash
   safety scan --verbose
   ```

## Getting Additional Help

If you're still experiencing issues:

1. Run commands with the `--verbose` flag to get more detailed output
2. Check the Safety logs (located in `~/.safety/logs/`)
3. Contact Safety support at <support@safetycli.com> with:
   * Command output (including any error messages)
   * Log contents
   * Your operating system and version
   * Your Safety CLI version (`safety --version`)
