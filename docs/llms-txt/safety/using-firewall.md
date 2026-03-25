# Source: https://docs.safetycli.com/safety-docs/firewall/using-firewall.md

# Using Firewall

This guide covers the everyday experience of working with Safety Firewall, including how package installations work, viewing scan results, and understanding warning messages.

## Using Aliased Package Managers

After installing Safety Firewall, your package managers (like pip) are aliased to their Safety equivalents. This means every time you use a package manager, Safety Firewall automatically intercepts and analyzes the request.

### Verifying Alias Configuration

After initialization, you can verify that Safety Firewall is correctly installed by checking your package manager aliases:

{% tabs %}
{% tab title="Mac/Linux" %}
After initialization, you can verify that Safety Firewall is correctly installed by checking your package manager aliases:

```bash
which pip
```

You should see output similar to:

```
pip: aliased to safety pip
```

If you don't see this output, you may need to reload your shell configuration:

```bash
source ~/.profile  # or ~/.bashrc, ~/.zshrc, etc.
```

{% endtab %}

{% tab title="CMD.exe" %}
After initialization, you can verify that Safety Firewall is correctly installed by checking your package manager aliases:

```bash
where pip
```

You should see output similar to:

```
pip: aliased to safety pip
```

If you don't see this output, your shell environment may need to be reloaded.
{% endtab %}

{% tab title="PowerShell" %}
After initialization, you can verify that Safety Firewall is correctly installed by checking your package manager aliases:

```bash
gcm pip
```

You should see output similar to:

```
pip: aliased to safety pip
```

If you don't see this output, your shell environment may need to be reloaded.
{% endtab %}
{% endtabs %}

## Installing Packages

### Basic Package Installation

Install packages as you normally would:

```bash
pip install requests
```

Safety Firewall will:

1. Intercept the request
2. Analyze the package and its dependencies
3. Apply your organization's policies
4. Either warn, block, or allow the installation
5. Record the installation event in Safety Platform

### Installing from Requirements Files

When installing from requirements files:

```bash
pip install -r requirements.txt
```

Safety Firewall will analyze all packages specified in the file before installation.

{% hint style="info" %}
When working within a registered codebase, Safety Firewall automatically updates your requirements files to use Safety's secure package index.
{% endhint %}

## Understanding Warning Messages

### Vulnerability Warnings

When installing packages with known vulnerabilities, you may see warnings like:

{% code overflow="wrap" %}

```
Warning: Package "django==3.2.0" has known vulnerabilities (CVE-2023-xxxx).See https://platform.safetycli.com/vulnerabilities/CVE-2023-xxxx for details.
```

{% endcode %}

These warnings are displayed based on your organization's policies.

### Policy-Based Blocks

If a package violates a blocking policy, you'll see a message like:

{% code overflow="wrap" %}

```
Blocked: Package "malicious-package" is known to be malicious.For more information, visit https://platform.safetycli.com/packages/malicious-package
```

{% endcode %}

{% hint style="warning" %}
**IMPORTANT**: Blocked installations are recorded in Safety Platform for audit purposes. If a legitimate package is blocked, contact your organization's Safety administrator.
{% endhint %}

## Performance Considerations

### Installation Speed

Package installations through Safety Firewall may be slightly slower than direct installations. This is because Safety Firewall downloads the package before delivering it to your system.

{% hint style="info" %}
The slight increase in installation time is offset by the security benefits of preventing vulnerable or malicious packages from entering your system.
{% endhint %}

## Working with Codebases

### Automatic Scans

When working in a registered codebase, Safety Firewall automatically scans your dependencies whenever you:

* Install packages with `pip install`
* Remove packages with `pip uninstall`
* Update your requirements with `pip install -r requirements.txt`

These scans happen in the background and results are uploaded to Safety Platform.

### Manual Scans

You can still perform manual scans at any time:

```bash
safety scan
```

This is useful when you want to check the current security status of your project.

## Viewing Results in Safety Platform

### Installation Activity

All package installations across your organization appear in the "Firewall" section of Safety Platform. Here you can:

* See who installed what packages and when
* Filter by user, package, or date
* View detailed information about each installation event

### Codebase Security Status

The "Codebases" section of Safety Platform shows:

* Current vulnerability counts for each codebase
* Recent scan activity
* Package installation history
