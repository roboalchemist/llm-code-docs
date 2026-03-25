# Source: https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration/uninstalling-firewall.md

# Uninstalling Firewall

## Firewall Uninstallation

If you need to uninstall Safety Firewall, you can do so with the following command:

```bash
safety firewall uninstall
```

This will remove all aliases and return your package managers to their original configuration.

{% hint style="warning" %}
If you're unable to run the uninstall command (for example, if you're not authenticated), you may need to manually remove the aliases from your shell configuration files and the `~/.safety` directory.
{% endhint %}
