# Source: https://help.aikido.dev/ide-plugins/features/aikido-expansion-packs.md

# Aikido Expansion Packs

{% hint style="warning" %}
Visual Studio support is coming soon
{% endhint %}

Aikido Expansion Packs allows you to add extra security tooling that runs on your machine from inside your IDE. You can enable or disable these add-ons from the Expansion Packs screen. Each pack improves a different part of your workflow and helps keep your code and device secure without slowing you down.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FD71QEZkTQTDQPWPe7pmr%2FScreenshot%202025-12-18%20at%2010.06.22.png?alt=media&#x26;token=23bbb92c-1160-402b-80ac-9e597717ee64" alt=""><figcaption></figcaption></figure>

## How to use

Open the Aikido sidebar, toggle open `Getting Started` if not already and click on the `Configure Aikido Expansion Packs` link.&#x20;

Alternatively use the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface) and run `Aikido: Expansion Packs`&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FMjd5wxKzT7kSRfnu3Dpj%2FScreenshot%202025-11-27%20at%2011.54.02.png?alt=media&#x26;token=4f6ddbd0-6e15-41f7-860f-266c84ddfac2" alt="" width="375"><figcaption></figcaption></figure>

## Features

### Pre-commit Hook

The secrets pre-commit hook checks your code for hardcoded secrets before you commit. It prevents accidental leaks and runs locally without configuration. Read more on [aikido-secrets-pre-commit-hook](https://help.aikido.dev/code-scanning/local-code-scanning/aikido-secrets-pre-commit-hook "mention")

### Safe Chain

Safe Chain protects your environment from malicious packages. It adds a safety layer around your package manager and prevents installation of known malware. Read more on [aikido-malware-scanning](https://help.aikido.dev/code-scanning/aikido-malware-scanning "mention")

### Aikido MCP

The Aikido MCP Server brings Aikido's security scanning capabilities directly into your AI coding workflow. Read more on [aikido-mcp](https://help.aikido.dev/mcp/aikido-mcp "mention")
