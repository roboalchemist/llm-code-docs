# Source: https://docs.safetycli.com/safety-docs/firewall/using-firewall/working-with-codebases.md

# Working with Codebases

## What is a Codebase in Safety?

A "codebase" in Safety refers to a project directory that is registered with Safety for vulnerability scanning and protection. When a directory is configured as a codebase:

1. Its dependencies are automatically scanned for vulnerabilities
2. Installation activities within that directory are tracked and monitored
3. Scan results and package installations are reported to Safety Platform
4. Organization policies are applied to package installations in that directory

## Setting Up a Codebase

### During Initialization

When you run `safety init`, Safety automatically detects Python projects in your current directory and offers to configure them as codebases.

### Manual Configuration

To manually set up a directory as a codebase, navigate to the project directory and run:

```bash
safety codebase init
```

Follow the prompts to name the codebase and configure it.

### What Happens When You Set Up a Codebase

When you configure a codebase, Safety:

1. Creates a `.safety-project.ini` file in the directory
2. Performs an initial scan of the project's dependencies
3. Uploads the scan results to the Safety Platform
4. Configures the directory for ongoing monitoring

{% hint style="info" %}
The name you choose for your codebase will be displayed in the Safety Platform, so choose something descriptive that helps you identify the project.
{% endhint %}

## Automatic Scanning

One of the key benefits of Safety Firewall is automatic dependency scanning:

### When Packages Are Installed or Removed

When you run commands like `pip install -r requirements.txt` or `pip uninstall package-name` within a configured codebase:

1. Safety Firewall intercepts the command
2. After the installation/removal completes, a scan is automatically triggered
3. Scan results are uploaded to Safety Platform
4. The codebase's security status is updated

This means you don't need to run `safety scan` manually after changing dependencies.

{% hint style="info" %}
Safety automatically updates your requirements files or pyproject.toml to use the Safety package index. This ensures that all package installations are routed through Safety Firewall.
{% endhint %}

## Manual Scanning

You can still perform manual scans at any time:

```bash
safety scan
```

This will scan the current directory's dependencies and update the results in the Safety Platform.

## Viewing Codebase Information

#### In Safety Platform

Your codebases appear in the "Codebases" section of the Safety Platform, where you can:

* View vulnerability counts and security status
* See detailed scan results for each codebase
* Track package installation history
* Manage codebase-specific policies

## Working with Unregistered Projects

If you install packages in a directory that isn't configured as a codebase:

1. Safety Firewall still protects you by analyzing packages before installation
2. Warnings or blocks are applied based on your organization's policies
3. Installation events are still recorded in the Safety Platform
4. However, scan results are not automatically uploaded to Platform

{% hint style="info" %}
**IMPORTANT**: Even if a directory isn't registered as a codebase, Safety Firewall still provides protection against vulnerable and malicious packages. The main difference is that scan results aren't automatically tracked in the Safety Platform.
{% endhint %}

## Managing Codebase Policies

Each codebase can have specific policies that override organization-level policies:

1. Navigate to your codebase in [Safety Platform](https://platform.safetycli.com)
2. Click "Codebase Settings"
3. Go to the "Policies" tab
4. Configure codebase-specific policies

If you have a local `.safety-project.yml` then your local `.safety-policy.yml` will no longer take effect. Instead, Safety will use the policy defined for the project in the Safety Platform.
