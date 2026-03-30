# Source: https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration.md

# Installation and Configuration

## System Requirements

Before installing Safety Firewall, ensure your system meets the following requirements:

* **Operating Systems**:
  * macOS 10.14 or later
  * Linux (Ubuntu, Debian, CentOS, RHEL)
  * Windows 10 or later
* **Python**: Version 3.8 or later

{% hint style="warning" %}
Safety Firewall works with pip, uv, and poetry. We'll automatically detect and configure the package managers on your system.
{% endhint %}

## Before You Begin

### Create a Safety Account

If you don't already have a Safety account, [sign up here](https://platform.safetycli.com/register).

### Get Your Organization Ready

To use Safety Firewall, your organization must have the Firewall feature enabled. If you're unsure whether your organization has access, contact your Safety administrator or [reach out to our support team](mailto:support@safetycli.com).

{% hint style="info" %}
If your Safety account was created before March 2025, the Firewall feature is disabled by default to ensure no breaking changes occur. To enable Firewall, please reach out to our [support team](mailto:support@safetycli.com).
{% endhint %}

## 1. Installation

### 1.1 Install Safety CLI

Open your terminal and run the following command:

{% tabs %}
{% tab title="pip" %}

```bash
pip install safety
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FxdyO0CQggTpx7hYPxeaq%2Fpip%20install%20safety.png?alt=media&#x26;token=c851b9b0-40a3-4b8d-91d7-f71dd5840bdf" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
If you already have Safety installed, please use `pip install -U safety` . The minimum version required to run Safety Firewall is v3.5.0.&#x20;
{% endhint %}
{% endtab %}

{% tab title="UV" %}

```bash
uv tool install safety
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FxdyO0CQggTpx7hYPxeaq%2Fpip%20install%20safety.png?alt=media&#x26;token=c851b9b0-40a3-4b8d-91d7-f71dd5840bdf" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### 1.2 Authenticate with Safety

Run the authentication command:

```bash
safety auth login
```

This will open a browser window where you can log in to your Safety account. Once authenticated, your terminal will show a success message.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fr5oAZya9WQptuwMWohYr%2Fsafety%20auth%20login.png?alt=media&#x26;token=ee1727fb-5939-4b12-ad7b-ff7c81a0595d" alt="" width="563"><figcaption></figcaption></figure>

### 1.3 Verify Authentication Status

You can check your authentication status at any time with:

```bash
safety auth status
```

This should display your email address and confirm that you're authenticated.

{% hint style="warning" %}
Make sure you're authenticated before proceeding to the next step. If you're not authenticated or don't have the Firewall feature enabled, the `safety init` command will not be available.
{% endhint %}

## 2. Initialization of Safety Firewall

After installing the Safety CLI and authenticating your account, you can initialize Safety Firewall with a single command:

```bash
safety init
```

This command starts the interactive setup process for Safety Firewall.

#### What Happens During Initialization

When you run `safety init`, the following actions take place:

1. Safety checks if you're authenticated and asks if you want to setup Safety Firewall.
2. Safety identifies the package managers on your system (pip, poetry, etc.)
3. Safety configures secure aliases for each package manager
4. Safety detects if there is a codebase in your current directory
5. Safety offers to set up this codebase for ongoing protection

{% hint style="warning" %}
**IMPORTANT**: After initialization, you'll need to refresh your shell environment for the aliases to take effect. This is typically done by running `source ~/.safety/.safety_profile` or the equivalent for your shell.
{% endhint %}

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fcll00ovDOXJ6N8YcQpOA%2Fsafety%20init.png?alt=media&#x26;token=c803302b-2f36-42b6-862d-865ad4877346" alt="" width="563"><figcaption></figcaption></figure>

## 3. Verifying Firewall Installation

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

If you don't see this output, your shell environment may need to be reloaded.
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

## Understanding Safety Firewall Configuration

### Package Manager Aliasing

Safety Firewall works by creating aliases for your package managers. When you run a command like `pip install requests`, the alias intercepts the command and routes it through Safety Firewall, which:

1. Analyzes the requested package(s) for vulnerabilities and malicious code
2. Applies your organization's security policies
3. Either warns, blocks, or allows the installation
4. Records the installation event in the Safety Platform

### Configuration Files

Safety Firewall creates several configuration files on your system:

* **`~/.safety/`**: The main directory for Safety Firewall configuration
* **`~/.safety/config.toml`**: Global configuration file
* **`.safety-project.ini`**: Project-specific configuration (created in each code base directory)

{% hint style="info" %}
Most users won't need to manually edit these files. Configuration changes are typically made through the Safety CLI or Safety Platform
{% endhint %}

## Configuring Your First Codebase

During initialization, Safety may detect a requirements file or Python project in your current directory and offer to configure it as a code base. If you accept, Safety will:

1. Create a `.safety-project.ini` file in the directory
2. Perform an initial scan of the project's dependencies
3. Upload the scan results to the Safety Platform
4. Configure the directory for ongoing monitoring

### Manual Codebase Configuration

If you want to set up a codebase after initialization, navigate to the project directory and run:

```bash
safety codebase init
```

Follow the prompts to name the code base and set up initial scanning.

{% hint style="info" %}
A "codebase" in Safety refers to a project that is tracked and monitored by the Safety Platform. When a codebase is configured, any package installations or removals within that directory will automatically trigger scans and update the project's security status in the Safety Platform.
{% endhint %}

### Configuration Options

#### Supported Package Managers

Safety Firewall currently supports the following package managers:

* **pip**: Fully supported
* **poetry**: Fully supported
* **UV**: Fully supported

Additional package managers will be added in future updates.
