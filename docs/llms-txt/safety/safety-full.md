# Safety Documentation

Source: https://docs.safetycli.com/llms-full.txt

---

# Introduction to Safety

**Safety shields your people, codebases, and AI-assistants from open-source software threats.**&#x20;

[**Safety Firewall**](https://docs.safetycli.com/safety-docs/firewall/introduction-to-safety-firewall) prevents vulnerable and malicious packages from entering your systems before they can cause harm. Unlike traditional scanners, Safety pre-screens every open source package and acts as a security filter between public repositories and your organization, protecting developers, codebases, and AI-assistants from malicious, vulnerable, and non-compliant packages. Unlike traditional vulnerability scanners that detect issues after packages are installed, Safety Firewall acts as a protective barrier around your development environments and build pipelines, analyzing every package installation request in real-time.

[**Safety CLI** ](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning)is a dependency vulnerability scanner designed to enhance software supply chain security and enable the secure use of Python packages, from development to deployment.‍ Safety CLI can be deployed in minutes and provides clear, actionable recommendations, leveraging the industry's most comprehensive database of vulnerabilities and malicious packages for Python.

{% hint style="success" %}

## Get Started with a 7-Day Free Trial

[Click here to create an account and access a 7-day Free Trial.](https://platform.safetycli.com/register/)
{% endhint %}

{% hint style="info" %}

## Upgrade to Safety 3.7.0

[Safety 3.7.0](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning) is now available. The minimum version required to run Safety Firewall is 3.5.0. To upgrade, use `pip install -U safety` or `uv tool install safety==3.7.0`

For details on upgrading from Safety CL 2.x to Safety CLI 3.x, [refer to our migration guide](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/migrating-from-safety-cli-2.x-to-safety-cli-3.x).
{% endhint %}

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fl5X2IQTrPcf0cjeglp91%2FSafety%20Scan%20GIF.gif?alt=media&#x26;token=220e43f1-165e-438f-93d9-f7ca6b07ce1d" alt=""><figcaption></figcaption></figure>

### Guides

Follow our handy guides to get started on the basics as quickly as possible:

{% content-ref url="firewall/introduction-to-safety-firewall" %}
[introduction-to-safety-firewall](https://docs.safetycli.com/safety-docs/firewall/introduction-to-safety-firewall)
{% endcontent-ref %}

{% content-ref url="firewall/installation-and-configuration" %}
[installation-and-configuration](https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration)
{% endcontent-ref %}

{% content-ref url="safety-cli/introduction-to-safety-cli-vulnerability-scanning/quick-start-guide" %}
[quick-start-guide](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/quick-start-guide)
{% endcontent-ref %}

{% content-ref url="safety-cli/scanning-for-vulnerable-and-malicious-packages/viewing-scan-results" %}
[viewing-scan-results](https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/viewing-scan-results)
{% endcontent-ref %}

{% content-ref url="safety-cli/scanning-for-vulnerable-and-malicious-packages/available-commands-and-inputs" %}
[available-commands-and-inputs](https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/available-commands-and-inputs)
{% endcontent-ref %}


# Introduction to Safety Firewall

## What is Safety Firewall?

Safety Firewall is a new approach to software supply chain security that *prevents* vulnerable and malicious packages from entering your systems before they can cause harm. Safety Firewall intercepts package installation requests, analyzes them against Safety's comprehensive vulnerability and malicious package database, and either approves, warns about, or blocks installations based on your organization's security policies.

### Key Benefits

* **Prevention-First Security**: Stop threats before they enter your system instead of detecting them after installation
* **Developer-Friendly Protection**: Seamlessly integrates with existing workflows and package managers (pip, poetry, and more)
* **Comprehensive Coverage**: Protects against known vulnerabilities, malicious packages, typosquatting, and other supply chain risks
* **Real-Time Protection**: Analyzes every package installation request as it happens
* **Organizational Visibility**: Provides insights into what packages are being installed, where, and by whom across your organization'

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FVOdAnu6Z3BwbgfDHqaHa%2FFirewall%20Dashboard.png?alt=media&#x26;token=af5c10e7-d421-4422-aeea-b6a2862e0883" alt=""><figcaption></figcaption></figure>

### How Safety Firewall Works

1. Safety Firewall creates secure aliases for your package managers (pip, poetry, etc.)
2. When a package installation is requested, Safety Firewall intercepts the request.
3. The package is analyzed in real-time against Safety's comprehensive vulnerability and malicious package database.
4. Based on your policies, the package is either approved, flagged with a warning, or blocked.
5. All installation activity is logged to Safety Platform for visibility and audit purposes.

{% hint style="success" %}
Safety Firewall protects not only code projects but also development environments and systems that fall outside of version-controlled codebases. This means even ad-hoc package installations by developers or data scientists are protected.
{% endhint %}

### Who Benefits from Safety Firewall?

* **Security Teams**: Gain confidence that supply chain threats are being prevented, not just detected
* **DevOps Teams**: Ensure consistent security policies across all environments without disrupting workflows
* **Developers**: Stay protected without changing how you work or adding security overhead
* **Compliance Teams**: Generate comprehensive audit logs of all package installations across the organization


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


# Installing Safety CLI via Binary

### Overview

Safety CLI can be installed using three different methods: pip, uv, or pre-compiled binaries. This guide covers the binary installation method.

#### Benefits of Binary Installation

Installing Safety via binaries offers several advantages:

* **No Python Required**: Safety runs as a standalone executable, eliminating Python installation and version management
* **Zero Dependency Conflicts**: Completely isolated from your Python environment and projects
* **Faster Startup**: Pre-compiled binaries start faster than Python-based installations
* **Simplified CI/CD**: Easier integration into build pipelines without Python environment setup
* **Consistent Performance**: Guaranteed consistent behavior across different environments
* **Smaller Footprint**: No need to install and manage Python dependencies

### Prerequisites

Before installing Safety via binary, ensure you have:

* **Linux/macOS**: `curl` installed (typically pre-installed)
* **Windows**: PowerShell 5.0 or later (included in Windows 10+)
* Internet connection to download the binary from GitHub releases

### Uninstalling Existing Safety Versions

If you already have Safety installed through pip or uv, you must uninstall it first to avoid conflicts between the global binary and Python package installations.

#### Check Current Installation

First, verify if Safety is currently installed and identify the installation method:

```bash
safety --version
which safety  # Linux/macOS
where safety  # Windows
```

#### Uninstall Python-based Installations

**If installed via pip:**

```bash
pip uninstall safety
```

**If installed via uv tool:**

```bash
uv tool uninstall safety
```

**If installed in a virtual environment:**

If Safety was installed in a virtual environment, you don't need to uninstall it unless you want the binary to be your primary Safety installation. The binary will be installed globally and take precedence when called from outside virtual environments.

#### Verify Uninstallation

After uninstalling, verify that Safety is no longer available:

```bash
safety --version
```

This command should return "command not found" or similar. If it still shows a version, check for additional installations:

```bash
# Linux/macOS: Check all Safety installations
which -a safety

# Windows: Check all Safety installations  
where /R C:\ safety.exe
```

## Installing Safety CLI Binary

The binary installation uses a shell script (Linux/macOS) or PowerShell script (Windows) that automatically:

1. Detects your operating system and architecture
2. Downloads the appropriate pre-compiled binary from GitHub releases
3. Installs Safety to your system PATH
4. Makes the `safety` command available globally

{% tabs %}
{% tab title="Windows" %}

#### Windows

Run the following command in PowerShell (as Administrator recommended):

```powershell
powershell -ExecutionPolicy ByPass -c '$env:SAFETY_LATEST_TAG=1; irm https://getsafety.com/cli/install.ps1 | iex'
```

**What this does:**

* `-ExecutionPolicy ByPass`: Temporarily bypasses PowerShell execution restrictions for this installation
* `$env:SAFETY_LATEST_TAG=1`: Sets the environment variable to download the latest version, including prereleases
* `irm`: PowerShell alias for `Invoke-RestMethod` (downloads the script)
* `iex`: PowerShell alias for `Invoke-Expression` (executes the script)

#### Installation Location

After installation, the Safety binary will be available globally:

* **Windows**: Typically installed to `%``USERPROFILE%\.safety\bin\safety.exe`
  {% endtab %}

{% tab title="Linux and macOS" %}

#### Linux and macOS

Run the following command in your terminal:

```bash
curl -LsSf https://getsafety.com/cli/install.sh | SAFETY_LATEST_TAG=1 sh
```

**What this does:**

* `curl -LsSf`: Downloads the installation script
  * `-L`: Follows redirects
  * `-s`: Silent mode (no progress bar)
  * `-S`: Shows errors if they occur
  * `-f`: Fails silently on server errors
* `SAFETY_LATEST_TAG=1`: Flag to download the latest available version (including pre-releases)
* `sh`: Executes the installation script

#### Installation Location

After installation, the Safety binary will be available globally:

* **Linux/macOS**: Typically installed to `~/.local/bin/safety` or `/usr/local/bin/safety`
  {% endtab %}
  {% endtabs %}

### Verifying Installation

After installation completes, verify that Safety is installed correctly:

```bash
safety --version
```

This should display the installed Safety version. You can also check the installation location:

```bash
which safety  # Linux/macOS
where safety  # Windows
```

### Important Notes and Troubleshooting

#### Download Speed and Rate Limiting

The installation script downloads binaries directly from GitHub releases. If you experience slow downloads or timeouts:

* **GitHub Rate Limiting**: Unauthenticated GitHub API requests are limited. Downloads may take up to 3 minutes depending on GitHub's current rate limits and your location
* **Network Issues**: Ensure you have a stable internet connection
* **Future Improvement**: CloudFront-based distribution is planned to improve download speeds and reliability

#### Version Control

The `SAFETY_LATEST_TAG=1` flag ensures you receive the latest available version:

* Includes both stable releases and pre-releases
* If you need a specific version, this flag can be adjusted once additional version options are available

#### Permission Issues

**Linux/macOS:** If you encounter permission errors during installation:

```bash
# Try with elevated permissions
curl -LsSf https://getsafety.com/cli/install.sh | sudo SAFETY_LATEST_TAG=1 sh
```

**Windows:** Run PowerShell as Administrator if you encounter access denied errors.

#### PATH Configuration

If the `safety` command is not found after installation:

**Linux/macOS:** Add the installation directory to your PATH by adding this line to your `~/.bashrc`, `~/.zshrc`, or equivalent:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload your shell configuration:

```bash
source ~/.bashrc  # or ~/.zshrc
```

**Windows:** The installer should automatically add Safety to your PATH. If not, manually add the installation directory to your system PATH through System Properties > Environment Variables.

### Next Steps

After successfully installing Safety CLI, proceed to authenticate with your Safety account:

For detailed authentication instructions, see the [Installation and Authentication](https://docs.safetycli.com/safety-docs/safety-cli/installation-and-authentication) guide.

### Switching Between Installation Methods

If you want to switch from binary installation back to pip or uv:

1. Remove the binary from your system PATH (location varies by OS)
2. Install using your preferred method: `pip install safety` or `uv pip install safety`
3. Verify the installation: `safety --version` and check the installation path

***

**Note**: Binary installation is currently in preview. Once fully production-ready, this will become a recommended installation method alongside pip and uv options.


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


# Using Safety Firewall in Docker

This guide explains how to integrate Safety Firewall into your Docker builds to protect package installations during image creation.

### Overview

Safety Firewall wraps your package manager (e.g. pip and uv) to automatically scan packages for vulnerabilities and block malicious packages before they're installed. In Docker, you install Safety first, then use it to protect your package installations.

### Prerequisites

* A Safety API key (available from your [Safety dashboard](https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration/using-safety-firewall-in-docker))
* Docker with BuildKit support (recommended for secure secret handling)

### Basic Setup

The simplest approach is to install Safety and then use it to wrap your pip install command:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install safety
RUN safety --key "YOUR_API_KEY" pip install --no-cache-dir -r requirements.txt
```

{% hint style="warning" %}
This example includes the API key directly in the Dockerfile, which is not recommended for production use. The key will be visible in your image history and any systems that have access to your Dockerfile. Use this approach only for initial testing.
{% endhint %}

### Recommended: Using Docker BuildKit Secrets

Docker BuildKit secrets allow you to pass sensitive values to your build without embedding them in the image or Dockerfile.

#### Option 1: Environment Variable

Pass your API key as an environment variable at build time.

**Dockerfile:**

```dockerfile
# syntax=docker/dockerfile:1.4
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install safety
RUN --mount=type=secret,id=safety_api_key \
    SAFETY_API_KEY="$(cat /run/secrets/safety_api_key)" && \
    safety --key "$SAFETY_API_KEY" pip install --no-cache-dir -r requirements.txt
```

**Build command:**

```bash
export SAFETY_API_KEY="your-api-key-here"

DOCKER_BUILDKIT=1 docker build \
    --secret id=safety_api_key,env=SAFETY_API_KEY \
    -t my-app .
```

#### Option 2: Using a .env File

If you prefer to store your API key in a file (useful for local development or when using .env files), you can source it directly.

**Dockerfile:**

```dockerfile
# syntax=docker/dockerfile:1.4
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install safety
RUN --mount=type=secret,id=safety_api_key \
    . /run/secrets/safety_api_key && \
    safety --key "$SAFETY_API_KEY" pip install --no-cache-dir -r requirements.txt
```

**Create a secrets file** (e.g., `safety-api-key.env`):

```bash
SAFETY_API_KEY="your-api-key-here"
```

{% hint style="info" %}
Make sure to add this file to your `.gitignore` to avoid accidentally committing your API key.
{% endhint %}

**Build command:**

```bash
DOCKER_BUILDKIT=1 docker build \
    --secret id=safety_api_key,src=./safety-api-key.env \
    -t my-app .
```

### CI/CD Integration

In CI/CD pipelines, store your Safety API key as a secret in your CI platform (GitHub Actions, GitLab CI, etc.) and pass it to the Docker build using the environment variable approach shown above.

For example, in GitHub Actions:

```yaml
- name: Build Docker image
  env:
    SAFETY_API_KEY: ${{ secrets.SAFETY_API_KEY }}
  run: |
    DOCKER_BUILDKIT=1 docker build \
        --secret id=safety_api_key,env=SAFETY_API_KEY \
        -t my-app .
```

### Troubleshooting

| Issue                       | Solution                                                               |
| --------------------------- | ---------------------------------------------------------------------- |
| `safety: command not found` | Ensure `pip install safety` runs before the Safety Firewall command    |
| Authentication errors       | Verify your API key is valid and properly passed to the build          |
| BuildKit not enabled        | Set `DOCKER_BUILDKIT=1` or configure Docker to use BuildKit by default |


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


# Working with Codebases

This guide explains how Safety Firewall interacts with your codebases and how to manage your projects efficiently.

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


# Firewall Monitoring and Management

This guide covers how to monitor Safety Firewall activity and manage your organization's protection status using Safety Platform.

## Accessing Firewall Monitoring

To access Firewall monitoring features:

1. Log in to Safety Platform at [platform.safetycli.com](https://platform.safetycli.com)
2. Navigate to the "Firewall" section in the main navigation

### Live Firewall Updates

The Live Firewall Updates stream displays real-time events from across your organization, including:

* Package installations
* Installation warnings
* Blocked installations
* Authentication events

This stream is particularly useful for:

* Quick debugging of Firewall activity
* Monitoring recent activity across your organization
* Verifying that events are being properly recorded

{% hint style="info" %}
The live Firewall Updates stream is an excellent way to confirm that Safety Firewall is properly configured and reporting events from your team members' environments.
{% endhint %}

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fg57l2CqOiozMGY7HnXAH%2FFirewall%20Dashboard.png?alt=media&#x26;token=b91dc831-c227-49d5-bc81-e47999521d6d" alt=""><figcaption></figcaption></figure>

## Organization Protection Status

The Protection Status section provides an overview of your organization's Safety Firewall implementation, including:

### Users Overview

* Total number of protected users
* List of users with Safety Firewall installed
* Last activity time for each user

### Package Managers

For each user, you can see which package managers are protected:

* pip
* poetry
* UV
* Other package managers (future releases)

This helps you ensure complete coverage across your organization.

### Installed Packages Overview

The Installed Packages section shows all packages installed across your organization:

* Package name and version
* Installation date and time
* User who performed the installation
* Whether any warnings or blocks were triggered

You can search and filter this list to find specific packages or activity.

## Managing Team Members

### Adding Users to Firewall

To add new users to Safety Firewall:

1. Navigate to the "Team" section in Safety Platform
2. Click "Invite Team Member"
3. Enter the user's email address
4. Assign appropriate roles and permissions
5. Send the invitation

New users will receive an email invitation with instructions to set up Safety Firewall.

### Monitoring Installation Status

After inviting team members, you can monitor their Firewall installation status:

1. Navigate to the "Firewall" section
2. Check the "Users" tab to see which team members have installed Firewall
3. Follow up with team members who haven't completed installation

{% hint style="info" %}
Team members must complete both the installation of Safety CLI and the Firewall initialization process to appear as protected in Safety Platform.
{% endhint %}


# Firewall Policy Management

This guide explains how to configure and manage policies in Safety Firewall to control package installation behavior across your organization.

### Understanding Firewall Policies

Policies define how Safety Firewall responds when users attempt to install packages. You can configure policies to:

* Warn users about vulnerabilities
* Block installation of vulnerable or malicious packages
* Apply different rules based on vulnerability severity
* Set organization-wide or codebase-specific policies

### Policy Hierarchy

Safety Firewall policies follow a hierarchical structure:

1. **Organization Policies**: Apply to all users and codebases
2. **Codebase Policies**: Specific to individual codebases, override organization policies
3. **Default Policies**: Applied when no specific policies are defined

{% hint style="info" %}
More specific policies always override more general policies. For example, a codebase policy takes precedence over an organization policy.
{% endhint %}

### Default Policies

Safety Firewall includes sensible default policies out of the box:

* **Installation**: Warns on all vulnerability severities
* **Scanning**: Reports all vulnerabilities regardless of severity
* **Malicious Packages**: Blocks known malicious packages

### Accessing Policy Management

To manage policies:

1. Log in to Safety Platform at [platform.safetycli.com](https://platform.safetycli.com)
2. Navigate to "Organization" → "Policies" for organization-wide policies
3. Navigate to a specific codebase and select the "Policies" tab for codebase-specific policies

{% hint style="warning" %}
**IMPORTANT:** the visual Policy Builder wizard in Safety Platform does not yet support Firewall policies. Until this is supported, you must select the **Advanced Configuration** option on the policy configuration page.
{% endhint %}

### Policy Structure and Syntax

Safety Firewall policies use a JSON structure with specific rules for allowing and denying packages or vulnerabilities.

#### Basic Policy Structure

{% code overflow="wrap" %}

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "allow": {
      // Allow rules
    },
    "deny": {
      // Deny rules
    }
  }
}
```

{% endcode %}

{% hint style="info" %}
The `default-action` determines what happens when no specific rule matches. We recommend keeping this as `"allow"` and defining specific denial rules for vulnerabilities and packages.
{% endhint %}

### Configuring Allow and Deny Rules

#### Allow Rules

Allow rules specify packages or vulnerabilities that should be explicitly permitted:

```json
"allow": {
  "packages": [
    {
      "ecosystem": "pip",
      "specifications": [
        "boto3==2.14",
        "django>=2.0",
        "flask>=1.0",
        "jinja2~=2.0"
      ]
    }
  ],
  "vulnerabilities": {
    "59901": {
      "reason": "We are not impacted by this vulnerability",
      "expires": "2024-03-15"
    },
    "62044": {
      "reason": "No upstream python images provide updated pip yet",
      "expires": "2024-06-01"
    }
  }
}
```

{% hint style="info" %}
Allow rules for vulnerabilities are helpful for temporarily ignoring specific vulnerabilities that don't affect your application or can't be remediated immediately. Always include an expiration date to ensure these exceptions are revisited.
{% endhint %}

#### Deny Rules

Deny rules specify packages or vulnerabilities that should trigger warnings or blocks:

```json
"deny": {
  "packages": {
    "warning-on-any-of": {
      "age-below": "3 months",
      "packages": [
        {
          "ecosystem": "pip",
          "specifications": [
            "safety"
          ]
        }
      ]
    },
    "block-on-any-of": {
      "age-below": "1 month",
      "packages": [
        {
          "ecosystem": "pip",
          "specifications": [
            "safety"
          ]
        }
      ]
    }
  },
  "vulnerabilities": {
    "warning-on-any-of": {
      "cvss-severity": [
        "critical",
        "high"
      ]
    },
    "block-on-any-of": {
      "cvss-severity": [
        "critical"
      ]
    }
  }
}
```

### Complete Policy Example

Here's a complete policy example that:

* Allows specific package versions
* Exempts specific vulnerabilities with explanations
* Warns on packages less than 3 months old and on critical/high vulnerabilities
* Blocks packages less than 1 month old and packages with critical vulnerabilities

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "allow": {
      "packages": [
        {
          "ecosystem": "pip",
          "specifications": [
            "boto3==2.14",
            "django>=2.0",
            "flask>=1.0",
            "jinja2~=2.0"
          ]
        }
      ],
      "vulnerabilities": {
        "59901": {
          "reason": "We are not impacted by this vulnerability",
          "expires": "2024-03-15"
        },
        "62044": {
          "reason": "No upstream python images provide updated pip yet",
          "expires": "2024-06-01"
        }
      }
    },
    "deny": {
      "packages": {
        "warning-on-any-of": {
          "age-below": "3 months",
          "packages": [
            {
              "ecosystem": "pip",
              "specifications": [
                "safety"
              ]
            }
          ]
        },
        "block-on-any-of": {
          "age-below": "1 month",
          "packages": [
            {
              "ecosystem": "pip",
              "specifications": [
                "safety"
              ]
            }
          ]
        }
      },
      "vulnerabilities": {
        "warning-on-any-of": {
          "cvss-severity": [
            "critical",
            "high"
          ]
        },
        "block-on-any-of": {
          "cvss-severity": [
            "critical"
          ]
        }
      }
    }
  }
}
```

{% hint style="info" %}
When defining package specifications, you can use the same version specifiers as in requirements.txt files: exact versions (`==`), minimum versions (`>=`), compatible releases (`~=`), etc.
{% endhint %}

### Common Policy Patterns

#### Basic Security Policy

Warn on high severity vulnerabilities, block critical ones:

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "deny": {
      "vulnerabilities": {
        "warning-on-any-of": {
          "cvss-severity": [
            "high"
          ]
        },
        "block-on-any-of": {
          "cvss-severity": [
            "critical"
          ]
        }
      }
    }
  }
}
```

#### New Package Caution

Warn about packages that are less than 3 months old:

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "deny": {
      "packages": {
        "warning-on-any-of": {
          "age-below": "3 months"
        }
      }
    }
  }
}
```

### Best Practices for Policy Management

* **Start Permissive**: Begin with warning-only policies to minimize disruption
* **Gradually Increase Restrictions**: Tighten policies as your team becomes familiar with Safety Firewall
* **Communicate Changes**: Inform your team before implementing blocking policies
* **Add Documentation**: Use the `"reason"` field to document why exceptions are being made
* **Set Expirations**: Always include an `"expires"` date for vulnerability exceptions
* **Monitor Impact**: Watch the Firewall logs to see how policies affect your team's workflow

{% hint style="info" %}
Blocking policies can disrupt developer workflows. Before implementing blocking policies, start with warnings and communicate the planned changes to your team.
{% endhint %}


# Troubleshooting

This guide helps you identify and resolve common issues with Safety Firewall. If you encounter problems during installation, configuration, or daily usage, the solutions here should help you get back

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


# Introduction to Safety CLI Vulnerability Scanning

Vulnerability Scanning for Secure Python Development

Safety CLI is a Python dependency vulnerability scanner designed to enhance software supply chain security by detecting packages with known vulnerabilities and malicious packages in local development environments, CI/CD, and production systems.&#x20;

Safety CLI can be [deployed in minutes](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/quick-start-guide) and provides [clear, actionable recommendations](https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/viewing-scan-results) for [remediation](https://docs.safetycli.com/safety-docs/vulnerability-remediation/applying-fixes) of detected vulnerabilities.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FGrcxqWf45l82S9nhkza8%2Fsafety_scan_S_white.gif?alt=media&#x26;token=ff8033aa-e92a-4a82-b97d-717c6623a3f5" alt="" width="518"><figcaption></figcaption></figure>

Leveraging the industry's most comprehensive database of vulnerabilities and malicious packages, Safety CLI Scanner allows teams to detect vulnerabilities at every stage of the software development lifecycle.

## Key Features

* Versatile, comprehensive dependency security scanning for Python packages.
* Leverages Safety DB, the most comprehensive vulnerability data available for Python.
* Clear output with detailed recommendations for vulnerability remediation.
* Automatically updates requirements files to secure versions of dependencies where available, guided by your project's policy settings.
* Scanning of individual requirements files and project directories or system-wide scans on developer machines, CI/CD pipelines, and Production systems to detect vulnerable or malicious dependencies.
* JSON, SBOM, HTML and text output.
* Easy integration with CI/CD pipelines, including GitHub Actions.
* **Enterprise Ready:** Safety CLI can be deployed to large teams with complex project setups with ease, on-premise or as a SaaS product.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F5dVcrP1wZAillCuBs46A%2Fimage.png?alt=media&#x26;token=4441abb1-fee7-4979-b957-6fee2b5308f0" alt=""><figcaption><p>Safety CLI,  Version 3.0.0</p></figcaption></figure>

Integrating into your existing workflow is easy, and it is possible to scan the full software development lifecycle, from developer machines to CI/CD pipelines and Production systems.<br>

Safety CLI is backed by our industry-leading vulnerability data and recommends fixes for vulnerabilities as they are detected.

> ### Versatile, comprehensive dependency security scanning

‍Safety can be deployed in minutes, seamlessly integrates with existing workflows, and allows developers to make informed security-based decisions without disrupting productivity.

> We transitioned from the free Snyk scanning to Safety because of the recommendation of one of our lead developers. **And we have loved it.**
>
> **Sean Howard -** CEO, Flightpath

## **Supported Ecosystems**

Safety currently supports Python only but will expand to support JavaScript and Java in H2 2025.


# Quick Start Guide

Running your first scan using Safety CLI takes less than a minute and can be performed via our  [Command Line Interface](#command-line-interface) or through the [GitHub Action](#github-action) .  Below we detail [1. Installation](#id-1.-installation), [2. Authentication](#id-2.-log-in-or-register), and [3. Running your first scan](#id-3.-running-your-first-scan).

To learn more about upgrading from Safety 2.x to Safety CLI please check out our [Migration guide](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/migrating-from-safety-cli-2.x-to-safety-cli-3.x).

## Command Line Interface

## 1. Installation

Begin by installing Safety on your development machine.

1. Open your Terminal
2. Run the following command to install:

```
pip install safety
```

{% hint style="info" %}
If you already have Safety installed, please use `pip install -U safety`&#x20;
{% endhint %}

## 2. Log In or Register

1\. Once installed, try to run your first scan using the following command:&#x20;

```
safety scan
```

2\. If you are already logged in, Safety will perform the scan. If you are not already authenticated, Safety CLI will prompt you to [create an account](https://platform.safetycli.com/register/) or [log in](https://platform.safetycli.com/login/) using existing credentials.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FUfzkaeezbhMsGsBCwzqU%2FAuth%20Step%201.gif?alt=media&#x26;token=26ee156c-5ef6-40ab-8449-f48aef15d88b" alt=""><figcaption></figcaption></figure>

In both cases, a browser window will open with clear instructions on how to log in or create a new account. Once logged in, Safety CLI will show that you are authenticated and can proceed with the next step.

{% hint style="warning" %}
You will be unable to perform vulnerability scans unless you are authenticated. [Create an account and access your free trial here. ](https://platform.safetycli.com/register/)If you require assistance, please email <support@safetycli.com>.
{% endhint %}

{% hint style="info" %}
To check your authentication status, you can run **`safety auth`** at any time.&#x20;
{% endhint %}

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F6hD5zET5qM5jOBO41OX7%2Fimage.png?alt=media&#x26;token=c66aeb22-16aa-4fc7-9a4a-98da66c8857f" alt="" width="563"><figcaption><p>Safety CLI after Successful Authentication</p></figcaption></figure>

## 3. Running Your First Scan

1. Using the Terminal, navigate to a project, e.g. `cd my/project/`. (This root folder would normally contain files such as `composer.lock`, `requirements.txt`, `READMEs`, `Pipfile.lock`,  `pyproject.toml`, `.gitignores` etc.)
2. Run the **`safety scan`** command.
3. Safety will now perform a scan of the current project directory, detecting all Python installations and requirements files. The output of the scan will be presented in the Terminal window.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FH0vrNDq570gOzOTBTt04%2Fsafety_scan_S_white.gif?alt=media&#x26;token=d634310e-1501-4fb7-8b9e-649aa307e050" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Performing scans across entire development machines and in CI/CD**

Detailed documentation on how to integrate Safety with other tools, perform system-wide scans, and more are available via the links to the left.
{% endhint %}

#### Jupyter Notebook Quickstart

For users who prefer a more interactive environment, we also provide a Jupyter Notebook Quickstart guide. This notebook offers step-by-step instructions for running Safety CLI within a Jupyter environment, making it easier to explore the functionality and perform your first scan in a familiar interface.

You can access the quickstart notebook here: [Jupyter Notebook Quickstart](https://github.com/pyupio/safety/blob/main/docs/Safety-CLI-Quickstart.ipynb).

## Basic Commands

The following are the most commonly used commands. [A full glossary of available commands can be found here](https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/available-commands-and-inputs).

* **`safety --help`** accesses Help and displays all available commands, utility commands, and options.
* **`safety auth`** starts the authentication flow if not logged in and displays authentication status if logged in.
* **`safety scan`** performs a vulnerability scan in the current directory.
* **`safety system-scan`** performs a vulnerability scan across the entire development machine.
* `safety scan --apply-fixes` performs a scan and automatically updates vulnerable dependencies to the next secure version.

{% hint style="info" %}
**Enterprise Customers:**

* Your organization may require installation to be performed via approved software bundles.&#x20;
* If your organization leverages SAML-based authentication, you will be prompted to enter your corporate login credentials at the authentication stage.&#x20;

If you are unsure whether your organization uses either of these options, please contact your administrator or email <support@safetycli.com>.
{% endhint %}

## GitHub Action

The quickest way to test Safety CLI in CI/CD is by using our [GitHub Action](https://github.com/pyupio/safety-actions), new in Safety CLI. Full [documentation on the GitHub Action](https://docs.safetycli.com/safety-docs/installation/github-actions) is available here:

[github-actions](https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions "mention")

If you require assistance, please email <support@safetycli.com>.


# Migrating from Safety CLI 2.x to Safety CLI 3.x

Safety CLI 3 is a significant update from Safety CLI 2.x versions, including enhancements to core features, new capabilities, and [breaking changes](https://docs.safetycli.com/safety-docs/miscellaneous/release-notes/breaking-changes-in-safety-3).&#x20;

Here's a step-by-step guide covering everything you need to know when upgrading.

## Installing Safety 3.x

1. Start by opening your Terminal and uninstall the current version of Safety CLI installed in your environment:&#x20;

```
pip uninstall safety
```

2. Install the latest version of Safety using the following command:&#x20;

```
pip install safety
```

Safety CLI 3.x should now be installed on your machine. To check which version is currently installed:

```
safety --version
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F48dCdeGq4nev7MsoWukZ%2FCLI%20Version.png?alt=media&#x26;token=c9414bd9-69bc-4f29-be5e-de6db00e0a82" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
If this returns a version other than 3.x, there could be more than one installation of Safety on your machine. To check where Safety is being run from, run the **`which safety`** command.&#x20;
{% endhint %}

## Switching to the new \`scan\` command:

The most significant change is Safety CLI 3's `scan` command, which replaces the old `safety check` command as the main security scanning command. `safety scan` is more powerful, configurable, and easier to use compared to `safety check`, and differs in the following key ways:

* it searches the target directory being scanned recursively, finding and reporting all Python dependency manifest files and virtual environments automatically, without any need for specifying where these files are
* it natively supports requirements.txt, poetry.lock, and Pipfile.lock files as well as Python virtual environment directories
* it is configured with a differently structured .safety-policy.yml file, which is incompatible with the .safety-policy.yml file used with the older \`safety check\` command, and visa versa. This new configuration file is more flexible and powerful
* it can be configured for how it searches the project directory, which vulnerabilities it reports on, and separately defines rules for which vulnerabilities will return a failing (non-zero) exit code, for use within CI/CD pipelines and build scripts

We highly recommend switching to `safety scan` as soon as possible.&#x20;

## Configuration files: Convert to the new policy file format

{% hint style="info" %}
If you are not currently using a `.safety-policy.yml` file with safety check, you can skip this section!
{% endhint %}

Safety CLI 3's `scan` and `system-scan` commands are configured using a new and updated configuration file. See [Safety 3's policy file documentation page](https://docs.safetycli.com/safety-docs/administration/safety-policy-files) for full details on the new structure and features of this policy file.

If you have been using a `.safety-policy.yml` file with `safety check`, you'll need to convert this to safety scan's new policy file format to use it to maintain the same policies with `safety scan`. To do this:&#x20;

* Navigate to the root of your existing project
* Move your existing policy file to a different location within your project, so that you can reference it later. (If you want to continue using safety check while also the new safety scan command, see instructions below \[link])
* Using Safety CLI 3 (run `safety --version` to confirm your Safety CLI version), run `safety generate policy_file` to generate a new policy file with the updated format.&#x20;
* Open both policy files, and translate the relevant parts from your old policy file into the new one. The key configurations that move are:
  * Any specific vulnerabilities you have ignored in `security:ignore-vulnerabilities` move to `report:auto-ignore-in-report:vulnerabilities` which contains the same list of ignores.
  * `security:ignore-cvss-severity-below` and `security:ignore-cvss-unknown-severity` move to a combined `report:auto-ignore-in-report:cvss-severity` which is now a YAML list with options: `critical`, `high`, `medium`, `low`, and `unknown`.
  * The boolean `security:continue-on-vulnerability-error:True` property is now removed. To suppress exit codes in the new policy file, use the `fail-scan-with-exit-code:dependency-vulnerabilities:enabled:False` property.&#x20;
  * The alert section of the old policy file is no longer supported and must be removed. This functionality is being replaced by Safety Platform.&#x20;
* With these changes your policies are now translated to the new policy format, ready to be used with `safety scan`
* When using the `validate` command, Safety CLI 3 will validate a 3.0 policy file by default.

## Updating your scan target(s)

If you were using Safety check with the -r flag to specify requirements.txt files to scan, you no longer need these with `safety scan` - they should be found automatically.

If `safety scan` is finding dependency files or virtual environments you do not want to include in your reports, use the new `scanning-settings:exclude` property in your `.safety-policy.yml` file to exclude specific files, file types or folders from the scan. [See more details on excluding here.](https://docs.safetycli.com/safety-docs/administration/safety-policy-files)

## New JSON output format

Safety scan has a new [JSON output](https://docs.safetycli.com/safety-docs/output/json-output) format that differs substantially from the JSON output of safety check.

## Upgrading from safety 2.x to safety 3.x while using safety check's JSON output

Safety CLI 3 still supports the safety check command, which is almost identical to safety check from Safety 2.x. If you are upgrading from Safety CLI 2 to Safety CLI 3, you can do so without needing to make any changes. The only breaking changes in this case may be the JSON output structure. Safety 3.0's JSON output from `safety check` uses the same structure as Safety CLI 2.4.0b. If you are upgrading from safety<=2.3.5 to safety>=3.x the JSON output from `safety check` will differ.

## Using both safety check and safety scan in the same project

You can use Safety CLI 3 to run both `safety check` and `safety scan` commands, each with their own policy files. To achieve this, keep your old `safety check` policy file in your project directory under a new name, for example `.safety-check-policy.yml`, and run the check command using `safety check --policy-file .safety-check-policy.yml` to specify the policy file's path. This will allow you to shift to using `safety scan` and the new policy file format at the default `.safety-policy.yml` location.


# Installation and Authentication

## Installation

To scan and secure Python projects, you first need Safety CLI version 3 to be installed on your machine.

{% hint style="info" %}
To check whether Safety CLI 3.x is already installed, open your **terminal** and type:

```
safety --version
```

{% endhint %}

If the safety command is not found, **or your safety version is less than 3.0,** you need to install Safety version 3 using the following command before continuing:

```
pip install safety
```

{% hint style="info" %}
If you already have Safety installed, please use `pip install -U safety`&#x20;
{% endhint %}

## Login Methods

When the installation of Safety version 3 has been confirmed, launch your terminal and authenticate using one of the methods outlined below.

### **Free & Team Customers**

Customers on our Free and Team plans will log in using an email and password defined when you [create your account](https://platform.safetycli.com/register/).

In your **terminal,** type:

```
safety auth login
```

Your default browser will open and you will be asked to authenticate using your Safety username and password. Login via Google is currently supported, and support for additional SSO providers will be added soon.

Once logged in, return to your terminal to verify Safety is authenticated with your account details by typing:

```
safety auth
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fdyn3a5051wOzizx3ih1L%2Fimage.png?alt=media&#x26;token=c98a997e-6485-49ae-8402-09dae7d045a3" alt="" width="563"><figcaption><p>1. "safety auth" launches the default browser.</p></figcaption></figure>

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FdH7aZXBqlUI0YOZnwjy1%2Fimage.png?alt=media&#x26;token=c4846462-7f1b-4929-a124-0c2e63c0b2ab" alt="" width="563"><figcaption><p>2. Browser-based Authentication</p></figcaption></figure>

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fe9czE5VMpu58M2VooZVA%2Fimage.png?alt=media&#x26;token=f3c52d5f-61a3-4866-bcae-1cf1edbe6448" alt="" width="563"><figcaption><p>"safety auth" triggering browser authentication and successful login</p></figcaption></figure>

### **Enterprise Customers**

Enterprise customers can leverage the method described above or SAML-based authentication, allowing users to be authenticated using organization-specific identities. The latter preserves approved authentication flows and prevents access to anyone not registered in your internal identity platform.

As above, when installation has been confirmed, in your **terminal,** type:

```
safety auth login
```

This will open your browser to authenticate the Safety CLI tool using your work email address and password. If your organization uses SAML authentication, you will be redirected to your corporate login page.

Once logged in, return to your terminal to verify Safety is authenticated with your account details by typing:

```
safety auth
```

If you are unclear as to which method your organization uses, please contact your administrator or email us at <support@safetycli.com>.


# Scanning for Vulnerable and Malicious Packages

Scan and secure projects against dependency vulnerabilities.

## Scanning a Python project

Once Safety CLI is installed and you have authenticated, let's **scan a Python project.**&#x20;

In your terminal, navigate to the root folder of a Python project, e.g. **`cd /my/project/`**. (This root folder would normally contain files such as **`composer.lock`**, **`requirements.txt`**, **`READMEs`**, **`Pipfile.lock`**,  **`pyproject.toml`**, **`.gitignores`** etc.)

Once you have navigated your terminal to your Python project's root directory, run:

```
safety scan
```

{% hint style="info" %}
If this is the first time Safety has scanned this project, you may be prompted to set the project's name for tracking within Safety Platform.
{% endhint %}

Running `safety scan` will:

* Scan your Python project's entire directory for Python package files and Python virtual environments, indexing all the packages found.
* Conduct a security analysis of these packages against known security vulnerabilities and malicious package lists.
* Identify known vulnerabilities in these packages, including their location and version
* Provide fix recommendations.

{% hint style="info" %}
Safety CLI is a powerful and flexible command-line tool. It can be used in a variety of use cases, environments and stages of the development lifecycle. It can output scan reports into different formats like JSON, and it can be integrated into any CI/CD pipeline or testing system. To learn more, refer to [Safety CLI Documentation](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning).
{% endhint %}

Once complete, your terminal will show a summary of the vulnerable packages that were found and recommended actions.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FzwND8F6sZdeeLdTxsVjG%2Fimage.png?alt=media&#x26;token=c735a841-153c-4b88-a638-872e0228440f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If the `safety scan` command is not found, **or your safety version is less than 3.0,** you need to [install Safety version 3](https://docs.safetycli.com/safety-docs/safety-cli/installation-and-authentication) before continuing below.
{% endhint %}

{% hint style="info" %}
**Targeting/Including Specific Requirements Files**

In Safety CLI 2, it was possible to target specific requirements files. The new Safety Scan command is designed to allow you to scan all files in a project directory (or sub-directory) simultaneously rather than running separate scans targeted on each file.

The [Policy File](https://docs.safetycli.com/safety-docs/administration/safety-policy-files) enables you to control the depth of those scans to detect nested requirements files, e.g. six folders deep within the current directory.

If you wish to specify a target directory for the Safety Scan, you can do so using the **`--target`** option, e.g. `safety scan`` `**`--target /path/to/project`**. Safety Scan does not allow you to target single files, but the include-files section of the Policy File does allow you to include specific files in your scan if these are not detected in a normal scan.&#x20;

Example:

**`include-files:`**

**`- path: inside_target_dir/requirements-docs.txt`**&#x20;

**`file-type: requirements.txt`**

**`- path: inside_target_dir/requirements-dev.txt`**

**`file-type: requirements.txt`**

When running a new Safety Scan, the new CLI output will separate findings and recommendations by requirements file, e.g. requirements.txt will have its own set of recommendations, requirements-dev.txt will have its own, etc. This means that instead of running separate scans for each file, you can now run one simple scan and see all findings and recommendations in one output.
{% endhint %}


# Viewing Scan Results

How to view and understand scan results in the Safety CLI

## CLI Screen Output

When a **`safety scan`** is run, output will be displayed in the Terminal window. This output is split into the following sections:

1. **Scan Details:**&#x20;
   * Version of Safety installed
   * Project repository being scanned
   * Account details of the user performing the scan
   * Confirmation that Python has been detected and the number of requirements files detected in the current location.
2. **Dependency Vulnerabilities Detected**
   * Safety provides details on all dependencies detected during the scan, the number of vulnerabilities present in each, and detailed data about those vulnerabilities, including the Vulnerability ID and relevant CVE IDs.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F3PyTmxMV1nmp7jPLrHOO%2Fimage.png?alt=media&#x26;token=a6291f64-05de-4e8f-a623-d34eec10daeb" alt=""><figcaption><p>Safety CLI output showing vulnerabiities detected in a requirements file.</p></figcaption></figure>

3. **Recommendations**
   * For each vulnerability that has been detected, Safety will recommend that each be updated to a version in which the vulnerabilities have been fixed.&#x20;
   * A URL is provided, which can be copied and pasted into your browser to review additional information on each dependency, the vulnerabilities detected, and versions with the fix applied.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FzDbDECfzfUyCQoMoIgGg%2Fimage.png?alt=media&#x26;token=3aa882ee-2080-4d46-909f-aa9e75215a63" alt=""><figcaption><p>Recommendations provided for each vulnerability detected in the previous step.</p></figcaption></figure>

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fj5ni2fIdNU1tdCwF7VVe%2Fimage.png?alt=media&#x26;token=ef51de11-2924-426a-b8b9-04b18aa1049e" alt=""><figcaption><p>Example of detailed changelogs for a package detected in the original scan using the URL provided.</p></figcaption></figure>

## Safety Platform

In addition to viewing output in the Terminal, all scan results are pushed to Safety Platform. Full details on how to view, interpret, and act upon Safety Platform information will be published as part of the Safety Platform documentation.&#x20;

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FSmDv4c6ZAfiISf45x1GH%2Fimage.png?alt=media&#x26;token=c37b4f40-ba1f-41dc-ad7e-7945399fb2f4" alt=""><figcaption></figcaption></figure>


# Available Commands and Inputs

The available commands and options within Safety CLI Scanner are detailed below. These can also be found within Safety CLI by typing `safety --help` or `safety [command] --help`.

## Authentication

<table><thead><tr><th width="188.33333333333331">safety auth --help</th><th width="239">Command/Option</th><th>Description</th></tr></thead><tbody><tr><td>Commands</td><td><code>login</code></td><td>Authenticate with Safety CLI to perform scans. Your default browser will automatically open to <a href="https://platform.safetycli.com/">https://platform.safetycli.com</a> unless already authenticated.<br><strong>Example: <code>safety auth login</code></strong></td></tr><tr><td></td><td><code>logout</code></td><td>Log out from the current Safety CLI session.<br><strong>Example: <code>safety auth logout</code></strong></td></tr><tr><td></td><td><code>status</code></td><td>Show the current authentication status.<br><strong>Example: <code>safety auth status</code></strong></td></tr><tr><td>Options</td><td><code>--install-completion</code></td><td>Install shell-specific completion scripts.<br><strong>Example: <code>safety auth --install-completion fish</code></strong></td></tr><tr><td></td><td><code>--show-completion</code></td><td>Show shell completion scripts for manual setup.<br><strong>Example: <code>safety auth --show-completion fish</code></strong></td></tr><tr><td></td><td><code>--help</code></td><td>Show detailed help information for commands and options.<br><strong>Example: <code>safety auth --help</code></strong></td></tr></tbody></table>

## Commands

<table><thead><tr><th width="189.33333333333331">safety --help</th><th width="251">Command/Option</th><th>Description</th></tr></thead><tbody><tr><td>Commands</td><td><code>auth</code></td><td>Authenticate Safety CLI to perform scans. Your default browser will automatically open to <a href="https://platform.safetycli.com/">https://platform.safetycli.com</a>.<br><strong>Example: <code>safety auth login</code></strong></td></tr><tr><td></td><td><code>scan</code></td><td>Run vulnerability scans on a Python project directory.<br><strong>Example: <code>safety scan</code></strong></td></tr><tr><td></td><td><code>system-scan</code></td><td>Run a comprehensive scan for packages and vulnerabilities across your entire machine/environment.<br><strong>Example: <code>safety system-scan</code></strong></td></tr><tr><td>Other Commands</td><td><code>alert</code></td><td>[Deprecated] Create GitHub Pull Requests from scan results. Being replaced by newer features.<br><strong>Example: <code>safety alert</code></strong></td></tr><tr><td></td><td><code>check</code></td><td>[Deprecated] Find vulnerabilities in target files/environments. Now replaced by safety scan.<br><strong>Example: <code>safety check /path/to/requirements.txt</code></strong></td></tr><tr><td></td><td><code>check-updates</code></td><td>Check for updates to the Safety CLI.<br><strong>Example: <code>safety check-updates</code></strong></td></tr><tr><td></td><td><code>configure</code></td><td>Set up global configurations for Safety CLI, including proxy settings and organization details.<br><strong>Example: <code>safety configure --proxy-host 192.168.0.1</code></strong></td></tr><tr><td></td><td><code>generate</code></td><td>Generate a standard Safety CLI policy file to establish baseline policies for scans.<br><strong>Example: <code>safety generate policy_file</code></strong></td></tr><tr><td></td><td><code>validate</code></td><td>Check if your local Safety CLI policy file is valid.<br><strong>Example: <code>safety validate /path/to/policy.yml</code></strong></td></tr><tr><td>Options</td><td><code>--stage</code></td><td>Assign a development lifecycle stage to your scan (default: development).<br><strong>Example: <code>safety --stage production scan</code></strong></td></tr><tr><td></td><td><code>--key</code></td><td>Use an API key for scans in CI/CD or Production (default: none).<br>For Development scans, unset the API key and authenticate using safety auth.<br><strong>Example: <code>safety --key 'your_api_key' scan</code></strong></td></tr><tr><td></td><td><code>--proxy-host</code></td><td>Specify a proxy host for network communications.<br><strong>Example: <code>safety configure --proxy-host 'proxy.example.com'</code></strong></td></tr><tr><td></td><td><code>--proxy-port</code></td><td>Set the proxy port (default: 80).<br>Note: proxy details can be set globally in a config file. See safety configure --help.<br><strong>Example: <code>safety configure --proxy-port 8080</code></strong></td></tr><tr><td></td><td><code>--proxy-protocol</code></td><td>Choose the proxy protocol (default: https).<br>Note: proxy details can be set globally in a config file. See safety configure --help.<br><strong>Example: <code>safety configure --proxy-protocol https</code></strong></td></tr><tr><td></td><td><code>--disable-optional-telemetry-data</code></td><td>Opt-out of sending optional telemetry for privacy. Anonymized telemetry data will remain.<br><strong>Example: <code>safety --disable-optional-telemetry-data scan</code></strong></td></tr><tr><td></td><td><code>--debug</code></td><td>Enable debug mode for detailed output in addition to standard output.<br><strong>Example: <code>safety --debug scan</code></strong></td></tr><tr><td></td><td><code>--version</code></td><td>Display the installed version of Safety CLI.<br><strong>Example: <code>safety --version</code></strong></td></tr><tr><td></td><td><code>--help</code></td><td>Show detailed help information for commands and options.<br><strong>Example: <code>safety --help</code></strong></td></tr></tbody></table>

## Safety Scan Options

<table><thead><tr><th width="192.33333333333331">safety scan --help</th><th width="252">Command/Option</th><th>Description</th></tr></thead><tbody><tr><td>Options</td><td><code>--target</code></td><td>Define a specific project path for scanning.<br><strong>Example: <code>safety scan --target /path/to/project</code></strong></td></tr><tr><td></td><td><code>--output</code></td><td>Set the format for scan results (default: screen) using Screen, JSON, HTML, or SPDX.<br><strong>Example: <code>safety scan --output json</code></strong></td></tr><tr><td></td><td><strong>--detailed-output</strong></td><td>Enable a verbose scan report for detailed insights.<br><strong>Example: <code>safety scan --detailed-output</code></strong></td></tr><tr><td></td><td><code>--save-as</code></td><td>Save scan results in different formats, including text, json, html, and spdx.<br><strong>Example: <code>safety scan --save-as json results.json</code></strong></td></tr><tr><td></td><td><code>--policy-file</code></td><td>Use a local policy file for scanning.<br><strong>Example: <code>safety scan --policy-file /path/to/policy.yml</code></strong></td></tr><tr><td></td><td><code>--install-completion</code></td><td>Install command-line completion for easier use.<br><strong>Example: <code>safety --install-completion bash</code></strong></td></tr><tr><td></td><td><code>--show-completion</code></td><td>Display shell completion scripts for customization.<br><strong>Example: <code>safety --show-completion zsh</code></strong></td></tr><tr><td></td><td><code>--apply-fixes</code></td><td>Automatically apply updates to requirements files for identified vulnerabilities in accordance with the parameters set in the config file.<br><strong>Example: <code>safety scan --apply-fixes</code></strong></td></tr></tbody></table>

## Environment Variables

| Env Var                  | Default Value | Description                                                                                                                                                                               |
| ------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SAFETY\_REQUEST\_TIMEOUT | 30 seconds    | Allows setting a custom request timeout for Safety CLI when pulling vulnerability and license JSON data from servers. If set, this value takes priority over the default hardcoded value. |
|                          |               |                                                                                                                                                                                           |
|                          |               |                                                                                                                                                                                           |


# Scanning in CI/CD

## Using Safety as a GitHub Action

Safety can be integrated into your existing GitHub CI pipeline as an Action. Just add the following as a step in your workflow YAML file after setting your `SAFETY_API_KEY` secret on GitHub under Settings -> Secrets -> Actions:

```
      - uses: pyupio/safety-action@v1
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}
```

(Don't have an API Key? You can sign up for one with <https://safetycli.com/resources/plans>.)

This will run Safety scan and will fail your CI pipeline if any vulnerable packages are found.

If you have something more complicated such as a monorepo; or once you're finished testing, read the [Documentation](https://docs.safetycli.com/) for more details on configuring Safety as an action.

Link to GitHub Action: <https://github.com/marketplace/actions/pyupio-safety-action>

For more information, visit the [GitHub Action](https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions) documentation below:

{% content-ref url="../../installation/securing-git-repositories/github/github-actions" %}
[github-actions](https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions)
{% endcontent-ref %}


# Securing Development Environments


# License Scanning

Safety provides a clear overview of the licenses used across all your dependencies.

To display the licenses in use, run the **`safety license`** command instead of the usual **`safety scan`** command used to perform vulnerability scans.

You can run the **`safety license --help`** to see a full list of available options.&#x20;

Running **`safety license`** will scan the current Python environment for all installed dependencies and report on their licenses.

Running **`safety license -r requirements.txt`** will report on the packages in the named requirements file.

## Output Options <a href="#output-options" id="output-options"></a>

The default output option is to the screen.

If you wish to ingest or analyze the resulting license report data you can generate a JSON file from the report by adding the **`--output json`** argument, as in the example below:

**`safety license -r requirements.txt --output json`**

Another output option is **`--output bare`** which will print the unique set of licenses that were present in the packages that were analyzed, as in the example below:

**`safety license -r requirements.txt --output bare`**


# Exit Codes

Safety natively supports improved exit codes. It will return a zero (success) exit code for scans that find no vulnerabilities and non-zero exit codes for scans that find vulnerabilities or have other issues.

If you want to suppress non-zero exit codes for scans that find vulnerabilities, you can set this in your Safety policy file. To read more, please refer to the Safety Policy File documentation.


# Scanning in Production

To run Safety in the production environment, you need to set the stage to production. This ensures that the security scans are aligned with the strict requirements of production environments.

#### Option 1: Run Safety in Production

To run the Safety CLI in production, use the `--stage` flag set to production like this: `safety --stage production scan`

Ensure the `$SAFETY_API_KEY` is set as an environment variable before running the command.

#### Option 2: Run as a Cron Job

If you want to automate this process, you can set up a cron job to periodically run Safety CLI within your Python repository. Here's an example cron job configuration:

```bash
# Run Safety every day at midnight
0 0 * * * cd /path/to/repo && \
safety --stage production scan >> \
/var/log/safety.log 2>&1
```

This will scan your production environment every day at midnight, appending the output to `/var/log/safety.log`.


# Safety Telemetry

By default, Safety receives non-sensitive, anonymized telemetry data when scans are performed. These data are captured solely for the purpose of delivering, maintaining and improving the Safety product.

The data captured include the following:&#x20;

| Name                                                            | Description                                                                                | Essential / Optional |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------- |
| **Safety Version** (safety\_version)                            | The version of Safety that was used, e.g. v3.0.1.                                          | Essential            |
| <p><strong>Safety Source</strong></p><p>(safety\_source)</p>    | The method by which Safety was used, e.g. via the CLI or via code.                         | Essential            |
| <p><strong>Safety Command</strong></p><p>(safety\_command)</p>  | Limited to the command used when running the scan (e.g. `safety scan`, `safety check`)     | Optional             |
| <p><strong>Safety Options</strong></p><p>(safety\_options)</p>  | Limited to the options used and how many times each is used, e.g. `-r`, `--output`, et al. | Optional             |
| <p><strong>Python Version</strong> </p><p>(python\_version)</p> | The version of Python installed.                                                           | Optional             |
| <p><strong>OS Type</strong></p><p>(os\_type)</p>                | The OS type used.                                                                          | Optional             |
| <p><strong>OS Release</strong></p><p>(os\_release)</p>          | The version of the OS used.                                                                | Optional             |
| **OS Description** (os\_description)                            | Description of the OS used.                                                                | Optional             |

## Disabling Non-Essential Telemetry Data

It is possible to disable the non-essential telemetry data by using the following option:

`--disable-optional-telemetry` e.g. `safety scan --disable-optional-telemetry`

When this option is employed, Safety will still collect the anonymized Safety Version and Safety Source. These data are required for us to be able to give our customers security protection, including security protection if Safety itself needs an update. We may also use the safety\_version to alert customers of any vulnerability or risk and recommend the user upgrade.

<br>


# Applying Fixes

When performing a **`safety scan`**,  Safety provides a list of the vulnerabilities detected and, where available, recommended fixes for each.

Safety CLI can automatically update requirements files based on these recommendations by using the **`safety scan --apply-fixes`**  command.

{% hint style="info" %}
**Summary**

* Where possible, updates to requirements files are applied automatically using the closest package version in which the detected vulnerability has been resolved.&#x20;
* Upgrades are performed in accordance with the [Policy File](#policy-file), which limits automatic upgrades to patch, minor, or major updates. Any upgrades beyond the policy-defined threshold will result in a prompt (Y/N/Skip) that must be responded to by the user.
* When no fixes are available, a message is displayed to that effect.
* Safety CLI does not download or install packages. Instead, requirements files are updated.
  {% endhint %}

## 1. Applying Security Updates Automatically

Safety can apply recommended security updates by including the **`--apply-fixes`** command.

#### **Example**

**`safety scan --apply-fixes`**

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FdEvYdTnQOh8guEQ3L9fR%2Fimage.png?alt=media&#x26;token=bf20f4bf-c244-4f9d-8b95-a7ea12e8acd6" alt=""><figcaption></figcaption></figure>

In this example, Safety has automatically updated the package versions in the requirements.txt file.  Our policy file has a threshold limiting automatic upgrades to patches and minor upgrades only. As a result, the user is asked whether or not they wish to upgrade to the new version of the last package.

### Threshold for Applying Fixes Automatically

#### Policy File

The Safety policy file referenced when performing the scan includes the automatic update threshold, beyond which the user will be prompted to confirm whether or not they wish to update packages with known vulnerabilities.

This threshold is necessary to prevent Safety from applying updates that could impact projects, e.g. by upgrading to a new major version with breaking changes.

#### Terminal

To set the maximum version change that Safety will apply without user input, append that limit to the command, e.g. **`safety scan --apply-fixes requirements.txt`` `**<mark style="color:blue;">**`minor`**</mark>. Possible values are: `major, minor, patch`. The default is value `patch`.

{% hint style="info" %}
In both cases, the value used is an upper limit. Using **`major`** is equivalent to automatically applying all the fixes without user input.
{% endhint %}

**Examples:**

```
safety scan --apply-fixes requirements.txt minor
```

This will update the requirements.txt file (and any other requirements files it references) with all the security remediations that are `minor` or `patch` updates. If remediation requires a `major` version update, then Safety will ask for user input if they want to make this change.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fz2xQILFfuWD2TBnwwVjE%2Fimage.png?alt=media&#x26;token=f96687a5-d582-408e-a4fd-16f813058211" alt=""><figcaption><p>Patch and Minor Updates Applied Automatically. Major updates require user input.</p></figcaption></figure>

`safety scan --apply-fixes requirements.txt major`

In this case, as `major` was used, all the remediations will be automatically applied in the file, and any of its recursive include files.

## Skipping Update Prompts

If you want to ensure that Safety will not wait for user input, the `--no-prompt` flag will apply all automatic fix updates that fall within the `--auto-security-updates-limit` limit, and ignore those that require user input.

`safety scan -r requirements.txt --apply-fixes -afl minor --no-prompt`

This will apply all `patch` and `minor` version security updates to `requirements.txt` and ignore any `major` version updates, with no user input prompt.


# Securing Git Repositories

## Securing your git source control management system

The best place to start with scanning your Python codebases for dependency vulnerabilities is in a central place for your team, like your build pipeline or your central source control management system. This allows quick setup and will allow you to know what dependencies are in your systems, and secure them before they get to your production systems, without having to set up each developer's environment.

## A quick intro to transitive dependencies

It's important to scan all the Python dependencies present in your systems, and not just the ones listed in your requirements files (these are called transitive, recursive, and run-time dependencies).

## Scanning *all* of your dependencies in your SCM systems

Luckily, scanning your Python environments is really easy to do using our Safety command-line tool. Its default configuration is to scan the local environment where it is running. See our guides below to integrate Safety CLI into your SCM system:


# GitHub

## GitHub Actions

This is a guide to setting up and configuring Safety to scan your GitHub repositories for dependency security vulnerabilities using Safety as a GitHub Action. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.Safety is available as an action in the [GitHub Marketplace](https://github.com/marketplace/actions/pyupio-safety).

#### Step 1: Get your Safety API Key <a href="#step-1-get-your-safety-api-key" id="step-1-get-your-safety-api-key"></a>

To scan any systems for security vulnerabilities, you first need a Safety API key. You can create a Safety account and get your API key [here](https://safetycli.com/contact-sales).

In your GitHub repository, navigate to **Settings** -> **Secrets** -> **Actions**, and add your Safety API key as a secret that matches the variable name you've used in the workflow YAML file (`SAFETY_API_KEY` in all the examples here). Once added, it should look similar to the screenshot below:​​

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F66efviut0LyscT2xhSHv%2F7cb6184-8886cae-Screen_Shot_2022-02-02_at_5.27.37_PM.png?alt=media&#x26;token=4f66d70d-4b60-44c5-8d3a-57b7d138055b" alt="" width="563"><figcaption></figcaption></figure>

#### Step 2: Set up a GitHub Actions workflow on your repository (If you don't have one already) <a href="#step-2-set-up-a-github-actions-workflow-on-your-repository-if-you-dont-have-one-already" id="step-2-set-up-a-github-actions-workflow-on-your-repository-if-you-dont-have-one-already"></a>

GitHub Actions are an easy and powerful way to run CI/CD processes on your codebases hosted on GitHub. Adding Safety security scans to your repositories is as easy as adding a few lines of code to your Github Action workflow configuration file to run Safety.We've created some full pipeline examples below if you don't have one set up yet. If you need help configuring your Python workflow, you can read more on [getting startup with GitHub workflows in Python](https://docs.github.com/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py).

#### Step 3: Configure your GitHub workflow YAML file to run Safety scans <a href="#step-3-configure-your-github-workflow-yaml-file-to-run-safety-scans" id="step-3-configure-your-github-workflow-yaml-file-to-run-safety-scans"></a>

GitHub Actions are configured using YAML workflow files in a special `.github/workflows/` folder. Here is an example YAML file that runs Safety to scan your project for security vulnerabilities. This will scan in auto-detect mode, which will try and scan the most appropriate thing automatically.You can read more about Safety's scan modes and different options.YAML# This workflow will run Safety security scans on all dependencies that are installed into the environment.# For more information see: <https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions#> Saved to \`.github/workflows/safety.yml\`​name: Safety Security Scan​on:push: # Run on every push to any branchpull\_request: # Run on new pull requests​jobs:safety:runs-on: ubuntu-lateststeps:- uses: safety/safety\@2.3.4with:api-key: ${{secrets.SAFETY\_API\_KEY}}


# GitHub Actions

## Introduction to GitHub Actions

[GitHub Actions](https://github.com/features/actions) is a powerful automation tool that integrates directly with GitHub repositories to allow you to automate your workflow by setting up a series of commands (actions) that execute in response to specific GitHub events like a push or a pull request. These actions can be used for a variety of tasks, such as testing code, deploying applications and, in the case of Safety, scanning for vulnerabilities.

[**The Safety CLI Scanner GitHub Action**](https://github.com/marketplace/actions/pyupio-safety-action) enables automated scanning of your projects for vulnerabilities directly within your GitHub workflow.

Link to Safety GitHub Action: <https://github.com/marketplace/actions/pyupio-safety-action>

## Setting Up the Safety GitHub Action

### **Step 1: Create a Safety Account and Obtain an API Key**

* To utilize the Safety CLI scanner, you first need to [create a Safety account](https://platform.safetycli.com/register/).
* Once your account is set up, you can obtain your API key from your [Safety Dashboard](https://platform.safetycli.com/). This key will be used to authenticate your GitHub Action with Safety's services.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FwAVEJQ8iG3lVIfbSunzS%2FScreenshot%202024-07-15%20at%2012.03.09.png?alt=media&#x26;token=9dcfc131-825a-45ce-8abc-4319c14c470a" alt=""><figcaption><p>Organization and User API Keys are available in Organization->API Keys</p></figcaption></figure>

### **Step 2: Configure the GitHub Secret**

* After obtaining your Safety API key, go to your GitHub repository's settings.
* Navigate to the '[Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)' section and add a new secret.
* Name the secret (e.g., `SAFETY_API_KEY`) and paste your Safety API key as the value.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FjE4NmTUEBcc0gRhQArox%2FScreenshot%202024-07-15%20at%2012.07.00.png?alt=media&#x26;token=d1626338-f245-4bd6-a308-57989521ee43" alt=""><figcaption><p>Add a new Secret to your Repo called SAFETY_API_KEY</p></figcaption></figure>

### **Step 3: Set Up the Workflow File**

* You may need to create a Personal Access Token (PAT) with workflow permissions in order to push a workflow file to your repo. To do so, please [refer to this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
* In your repository, create a new file in the `.github/workflows` directory. You can name this file according to its purpose (e.g., `safety_scan.yml`).
* Add the following content to your workflow file:

```yaml
name: Example workflow for Python using Safety Action
on: push
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: Run Safety CLI to check for vulnerabilities
        uses: pyupio/safety-action@v1
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}

```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F4dJmDKDMdREoEHFsG2Xz%2FScreenshot%202024-07-15%20at%2012.29.26.png?alt=media&#x26;token=6efefe85-a895-4651-8ca4-ec561c4dd05a" alt=""><figcaption></figcaption></figure>

### **Step 4: Activate the Workflow**

* Commit and push the workflow file to your repository.
* The Safety CLI Scanner Action will run automatically on each push, scanning your Python project for any vulnerabilities.

### **Additional Configurations (Optional)**

* You can customize the behaviour of the Safety Action by using various properties.
* You can also add arguments like `--detailed-output` to get more information from the scan:

```yaml
name: Example workflow customizing the Safety Action
on: push
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: Run Safety CLI to check for vulnerabilities
        uses: pyupio/safety-action@v1
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}
          args: --detailed-output # To always see detailed output from this action

```

#### Available Properties

<table><thead><tr><th>Property</th><th width="122.33333333333331">Default</th><th>Description</th></tr></thead><tbody><tr><td>api-key</td><td></td><td>Your Safety API Key</td></tr><tr><td>output-format</td><td>screen</td><td>Options are: screen, json, html, spdx, none</td></tr><tr><td>args</td><td></td><td>Override the default arguments to Safety CLI 3.</td></tr></tbody></table>

For more detailed information about Safety's CLI and its functionalities, please refer to [Safety 3 Documentation](https://docs.safetycli.com/safety-docs) or contact our [Support Team](https://docs.safetycli.com/safety-docs/support/support).


# GitLab

This is a guide to setting up and configuring Safety to scan your Gitlab repositories for dependency security vulnerabilities. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.

You can set up Safety to run security scans on your Python repositories in GitLab using Gitlab Pipelines.

### Step 1: Get your Safety API Key

To scan any systems for security vulnerabilities, you first need a Safety API key. [You can create a Safety account and get your API key here](https://platform.safetycli.com/register/).

### Step 2: Set up a Gitlab Pipeline on your repository (If you don't have one already)

Gitlab pipelines are an easy and powerful way to run CI/CD processes on your codebases managed on Gitlab. Adding Safety security scans to your repositories is as easy as adding a few lines of code to your Gitlab pipeline configuration file to install Safety (our command-line tool) and then run a Safety scan.

We've created some full pipeline examples below if you don't have one set up yet. If you need help configuring your pipeline, you can read more on [getting startup with Gitlab pipelines](https://docs.gitlab.com/ee/ci/pipelines/).

### Step 3: Configure your .gitlab-ci.yml YAML file to run Safety

Gitlab pipelines are configured using a `.gitlab-ci.yml` YAML file at the root of your Gitlab repository. Here is an example YAML file that installs and runs Safety to scan your Python environment for security vulnerabilities.

YAML

```yaml
#  PyUp Security Scans Template

#  This template allows you to run security scans on your Python dependencies.
#  The workflow allows running tests on the default branch.

image: python:latest

# Change pip's cache directory to be inside the project directory since we can
# only cache local items.
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip
    - venv/

before_script:
  - python --version  # For debugging
  - pip install virtualenv
  - virtualenv venv
  - source venv/bin/activate
  - pip install safety

run:
  script:
    # Install your requirements. Alternatively install via Poetry or Pipenv
    - pip install -r requirements.txt
    # Run Safety's environment scan
    - safety --key $SAFETY_API_KEY --stage cicd scan
```

Your pipeline YAML file will likely end up running other tests and actions and deployments. All you have to do to ensure that Safety is scanning your dependencies for security vulnerabilities is to ensure that the following code (script) is in your YAML file amongst your other tests and scripts that are running.

YAML

```yaml
...
  script:
    # Install Safety - PyUp's command-line tool
    - pip install safety
    # Install your Python dependencies as per usual. 
    # This example uses requirements.txt and pip, but you may use Poetry with its Pipfiles, or pipenv with its pyproject.toml file. 
    - pip install -r requirements.txt
    # Run safety to scan the local Python environment. This will scan all installed dependencies, including any transitive dependncies that get installed during your installation
    - safety --key $SAFETY_API_KEY --stage cicd scan
```

### Final Step: Add your Safety API Key as a Gitlab repository variable

Your safety script requires the Safety API key to connect to Safety and get the latest commercial vulnerability database. To link up this API key to the $SAFETY\_API\_KEY variable defined in your pipeline YAML file (example above), you need to add your Safety API key as a Gitlab CI/CD environment variable. To do this, navigate to your repository on Gitlab, go to your project’s **Settings > CI/CD** and expand the **Variables** section.

Once added, the new variable should display like the screenshot below on the Gitlab repository variable page:

![973](https://files.readme.io/94ef9af-Screen_Shot_2022-03-28_at_5.44.40_PM.png)

### You're done!

That's it! You now have a fully working Gitlab CI/CD pipeline that will run and scan your Python dependencies for security vulnerabilities on new pushes and pull requests using Safety's commercial vulnerability database.

If there is a vulnerability found, Safety will return a non-zero exit code and fail the test. You can then see the pipeline's output in Gitlab to see what Safety found and how to patch the vulnerabilities. Here is our example running on a new pull request:

![1072](https://files.readme.io/0febb5b-Screen_Shot_2022-03-28_at_5.52.21_PM.png)

### Next Steps: Configure your Pipeline file, and learn more about Safety

**Gitlab Pipelines**\
There are many more configuration options on Gitlab CI/CD Pipelines. For example, you can set up this Pipeline to only run on certain branches or run when other conditions are met. You can also configure it to run periodically using a cron so that your repository is scanned for security vulnerabilities every hour or every day, not just when new code is committed.

You can read more about Gitlab pipelines on their [documentation page](https://docs.gitlab.com/ee/ci/pipelines/).

**Safety Command-Line Interface (CLI)**\
These scans use Safety's Command-Line tool, which has many options and configurations to meet your needs. Instead of scanning your local environment after you've installed your dependencies, you can also configure it to scan specific requirements files, output different formats, or even scan for license compliance issues.

You can read more about Safety and how to use it on its [Github page](https://github.com/pyupio/safety).


# BitBucket

This is a guide to setting up and configuring Safety to scan your BitBucket repositories for dependency security vulnerabilities. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.

You can set up Safety to run security scans on your Python repositories in BitBucket using BitBucket pipelines.

### Step 1: Get your Safety API Key

To scan any systems for security vulnerabilities, you first need a Safety account. [You can create a Safety account and get your API key here.](https://platform.safetycli.com/register/)

### Step 2: Set up a Bitbucket Pipeline on your repository (If you don't have one already)

BitBucket pipelines are an easy and powerful way to run CI/CD processes on your codebases hosted on BitBucket. Adding Safety security scans to your repositories is as easy as adding a few lines of code to your BitBucket pipeline configuration file to install and run Safety CLI.

We've created some full pipeline examples below if you don't have one set up yet. If you need help configuring your pipeline, you can read more on [getting startup with BitBucket pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/) as well as [setting up BitBucket pipelines in Python projects](https://support.atlassian.com/bitbucket-cloud/docs/python-with-bitbucket-pipelines/).

### Step 3: Configure your bitbucket-pipelines.yml YAML file to run Safety

BitBucket pipelines are configured using a `bitbucket-pipelines.yml` YAML file at the root of your BitBucket repository. Here is an example YAML file that installs and runs Safety to scan your Python environment for security vulnerabilities.

YAML

```yaml
#  Safety Security Scans Template

#  This template allows you to run security scans on your Python dependencies.
#  The workflow allows running tests on the default branch.

image: python:3.12

pipelines:
  default:
    - parallel:
      - step:
          # Run Safety to scan your Python Environment (recommended and best practice)
          name: Safety Security Scan on the Python Environment
          script:
            # Install Safety CLI - Safety's command-line tool
            - pip install safety
            # Install your Python dependencies as per usual. 
            # This example uses requirements.txt and pip, but you may use Poetry with its Pipfiles, or pipenv with its pyproject.toml file. 
            - pip install -r requirements.txt
            # Run safety to scan the local Python environment. This will scan all installed dependencies, including any transitive dependncies that get installed during your installation
            - safety --key $SAFETY_API_KEY --stage cicd scan
```

Your pipeline YAML file will likely end up running other tests and actions and deployments. All you have to do to ensure that Safety is scanning your dependencies for security vulnerabilities is to ensure that the following code (script) is in your YAML file amongst your other tests and scripts that are running.

YAML

```yaml
...
  script:
    # Install Safety - PyUp's command-line tool
    - pip install safety
    # Install your Python dependencies as per usual. 
    # This example uses requirements.txt and pip, but you may use Poetry with its Pipfiles, or pipenv with its pyproject.toml file. 
    - pip install -r requirements.txt
    # Run safety to scan the local Python environment. This will scan all installed dependencies, including any transitive dependncies that get installed during your installation
    - safety --key $SAFETY_API_KEY --stage cicd scan
```

### Final Step: Add your Safety API Key as a BitBucket repository variable

Your safety script requires the Safety API key to connect to Safety and get the latest commercial vulnerability database.

To link up this API key to the $SAFETY\_API\_KEY variable defined in your pipeline YAML file (example above), you need to add your Safety API key as a BitBucket repository variable.&#x20;

To do this, navigate to your repository on BitBucket, then **Repository settings** then the **Repository variables** sub-menu.

Once added, the new variable should display like the screenshot below on the BitBucket repository variable page:

![918](https://files.readme.io/6b80389-Screen_Shot_2022-02-01_at_7.27.19_PM.png)

### You're done!

That's it! You now have a fully working BitBucket pipeline that will run and scan your Python dependencies for security vulnerabilities on new pushes and pull requests using Safety's commercial vulnerability database.

If there is a vulnerability found, Safety will return a non-zero exit code and fail the test. You can then see the pipeline's output in Bitbucket to see what Safety found and how to patch the vulnerabilities. Here is our example running on a new pull request:

<figure><img src="https://files.readme.io/76d8aab-Screen_Shot_2022-02-01_at_7.46.14_PM.png" alt=""><figcaption></figcaption></figure>

### Next Steps: Configure your Pipeline file, and learn more about Safety

**BitBucket Pipelines**\
There are many more configuration options on BitBucket Pipelines. For example, you can set up this Pipeline to only run on certain branches or run when other conditions are met. You can also configure it to run periodically using a cron so that your repository is scanned for security vulnerabilities every hour or every day, not just when new code is committed.

You can read more about BitBucket's pipelines on their [documentation page](https://support.atlassian.com/bitbucket-cloud/docs/configure-bitbucket-pipelinesyml/).


# Azure DevOps

This is a guide to setting up and configuring Safety to scan your Azure DevOps repositories for dependency security vulnerabilities. This enables you to configure security and compliance scans on your repositories on new commits, new branches, pull requests, and more.

You can set up Safety to run security scans on your Python repositories in Azure DevOps using Azure Pipelines.

### Step 1: Get your Safety API Key

To scan any systems for security vulnerabilities, you first need a Safety account. [You can create a Safety account and get your API key here.](https://platform.safetycli.com/organization/apikeys)

### Step 2: Set up an Azure DevOps Pipeline on your Repository

Azure Pipelines are a simple and powerful way to build, test, and deploy your code hosted in Azure DevOps. Integrating Safety into your CI/CD pipeline enables automated security and compliance checks for every commit, pull request, or scheduled run.

If you don’t already have a pipeline configured, follow these Microsoft guides to get started:

* [Get started with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started-yaml?view=azure-devops)
* [Build Python apps with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/languages/python?view=azure-devops)

Once your pipeline is in place, proceed to the next step to configure Safety CLI.

***

### Step 2.5: Set up a Self-Hosted Agent (Optional)

If you prefer to run pipelines on your own infrastructure—such as a local machine or internal server—you can configure a self-hosted agent instead of using Microsoft's hosted runners.

For complete setup instructions, see:

* [Set up a self-hosted agent in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux?view=azure-devops)

Once your agent is configured and running, reference its pool name in your pipeline YAML:

```yaml
pool:
  name: Default
```

This tells Azure DevOps to execute the pipeline on the self-hosted runner you just configured in the `Default` agent pool.

### Step 3: Configure your azure-pipelines.yml YAML file to run Safety

Azure Pipelines are configured using an `azure-pipelines.yml` file at the root of your Azure DevOps repository. Here is an example YAML file that installs and runs Safety to scan your Python environment for security vulnerabilities.

```yaml
# Safety Security Scans Template

# This template allows you to run security scans on your Python dependencies.
# The workflow is configured to run on pushes to the 'main' branch.

trigger:
  - main  # Triggers the pipeline on changes to the 'main' branch

pool:
  name: Default  # Uses the default agent pool defined in Azure DevOps

steps:
  - script: |
      # Upgrade pip to the latest version
      python3 -m pip install --upgrade pip

      # Install Safety CLI – Safety’s command-line tool for dependency scanning
      pip install safety

      # (Optional) Install your project dependencies if you want to scan the active environment.
      # This is not required, Safety can scan your static files directly (e.g., requirements.txt, pyproject.toml)
      # You may also use Poetry or Pipenv instead.
      # pip3 install -r requirements.txt

      # Run Safety to scan the local Python environment
      # This will check all installed packages (including transitive dependencies) for vulnerabilities
      safety --key $(SAFETY_API_KEY) --stage cicd scan
    env:
      SAFETY_API_KEY: $(SAFETY_API_KEY)  # Injects your Safety API key as an environment variable
      SAFETY_CLI_DISABLE_LOCAL_CONFIG: "1"  # Disables any local Safety config to avoid misconfiguration
```

### Final Step: Add your Safety API Key as an Azure DevOps pipeline variable

Your Safety script requires the Safety API key to connect to Safety and retrieve the latest commercial vulnerability database.

There are two ways to securely inject the API key into your pipeline:

**Option 1: Define the variable in a Variable Group (via Library)**

* Navigate to your project in Azure DevOps.
* Go to Pipelines > Library.
* Create a new Variable Group or select an existing one.
* Add a variable named `SAFETY_API_KEY` and paste in your key.
* Check "Keep this value secret" to secure the key.

**Option 2: Define the variable in the pipeline UI**

* Go to your pipeline in Azure DevOps.
* Click Edit, then select the "Variables" tab.
* Add a new variable named `SAFETY_API_KEY`.
* Paste in your key and mark it as secret.

Either method will make the `$(SAFETY_API_KEY)` variable available to your pipeline, allowing the YAML configuration to authenticate successfully with Safety CLI.

### You're done!

That's it! You now have a fully working Azure DevOps pipeline that will run and scan your Python dependencies for security vulnerabilities on new pushes and pull requests using Safety's commercial vulnerability database.

If there is a vulnerability found, Safety will return a non-zero exit code and fail the test. You can then see the pipeline's output in Azure DevOps to view what Safety found and how to patch the vulnerabilities.

### Next Steps: Configure your pipeline file, and learn more about Safety

There are many more configuration options on Azure Pipelines. For example, you can:

* Set up this pipeline to only run on certain branches or run when other conditions are met.
* Configure it to run periodically using a cron so that your repository is scanned for security vulnerabilities every hour or every day, not just when new code is committed.

You can read more about Azure Pipelines on their [documentation page](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops).

And for more on Safety CLI, visit [Safety CLI Documentation](https://docs.safetycli.com).


# Git Post-Commit Hooks

## Scanning your development environments

It's a best practice run your security scans as soon as possible in the development life-cycle - this is called shift left security.

Running PyUp security scans in your development environments is as simple as adding Safety's CLI scan to your git pre-commit hook files. This is a file that is executed before a git commit is run, and a failing command in this process will halt the commit itself, and warn the developer of the issue.

## Adding Safety CLI to your git pre-commit hooks

To add Safety scans to your git pre-commit hooks, first find your git pre-commit hook file, located at `.git/hooks/pre-commit`.

If you haven't already set up a pre-commit hook it may still be named `pre-commit.sample`. In that case, rename it to `pre-commit` and that file will start running before your git commits.

Once you've got the file ready, add the following to the bottom of the file:

Shell

```shell
# Add Safety Scan
exec safety scan
```

And that's it. Now Safety will scan your development machine before any code is pushed to central source control systems.


# Pipenv


# Docker Containers

Safety is available in a Docker container if you'd like to scan across Python versions or use Safety without having to install it, or Python, locally.

To get started, you can run the `ghcr.io/pyupio/safety` image. Any arguments provided will be transparently passed through to Safety:

```shell
docker run --rm -ti ghcr.io/pyupio/safety:latest --version
```

Scanning from a requirements file works as expected. You must, however, make sure to volume mount your project so that Safety can access it inside the container:

```shell
docker run --rm -ti -v /path/to/my/project:/target ghcr.io/pyupio/safety --key <YOUR-API-KEY> --stage cicd scan --target /target
```


# Safety Policy Files

{% hint style="warning" %}
With the introduction of Safety Platform, our web-based Safety experience, local policy files will no longer be applied (even if specified in the CLI arguments). Instead, the Project policy that is defined in Platform will be used. Learn more about [Project Policies.](https://docs.safetycli.com/safety-docs/administration/project-policies)
{% endhint %}

Safety CLI scan settings are configured using Safety policy files. These `.safety-policy.yml` files can be defined for each of your project's or codebases.

{% hint style="info" %}
**Note**: the older **`safety check`** command uses an older policy file format. See [Safety 2's policy file format](https://docs.safetycli.com/safety-2/safety-cli-2-scanner/policy-file) to configure the policies for the `safety check` command.&#x20;
{% endhint %}

### Why use a policy file?

Using a policy file is recommended as a way to standardize your security policy for each project, and allows your development team to centrally share and configure rules, settings, and exceptions for your Safety scans. Some examples are:

* Setting vulnerability severity threshold to only report vulnerabilities above a certain severity threshold
* Ignoring specific vulnerabilities your team knows do not impact your project
* suppressing exit codes in scenarios in which you don't want to stop a build or test

These policy files should be checked into your source control at the root of your Python project alongside other policy files such as `.gitignore`, `requirements.txt`, `setup.py`, etc.

### Generating a Safety CLI policy file

To generate a new policy file, run the following command:

```
safety generate policy_file
```

The resulting policy file will be placed in the current directory with the name **`.safety-policy.yml`**. Please note that the file is hidden when viewing in Windows or Finder, but is visible when connected to a folder using an IDE.

### Safety Policy File Structure

Below is an example of a Safety policy file:

```yaml
version: '3.0'

scanning-settings:
  max-depth: 6
  exclude:
    - "node_modules"
    - "lib/other/**"
    - "**/*.js"
  include-files:
    - path: inside_target_dir/requirements-docs.txt
      file-type: requirements.txt
    - path: inside_target_dir/requirements-dev.txt
      file-type: requirements.txt

report:
  dependency-vulnerabilities:
    enabled: true
    auto-ignore-in-report:
      python:
        environment-results: true
        unpinned-requirements: true
      cvss-severity: []
      vulnerabilities:
        59901:
          reason: We are not impacted by this vulnerability
          expires: '2024-03-15'
        62044:
          reason: No upstream python images provide updated pip yet
          expires: '2024-06-01'

fail-scan-with-exit-code:
  dependency-vulnerabilities:
    enabled: true
    fail-on-any-of:
      cvss-severity:
        - critical
        - high
        - medium

security-updates:
  dependency-vulnerabilities:
    auto-security-updates-limit:
      - patch
```

We will now look at each section of the policy file, the items it controls, and available options.

#### Scanning Settings

The **`scanning-settings`** section of the policy file define where Safety CLI should scan in the target directory. These settings configure the **`safety scan`** command.

* **`max-depth`**: an integer that sets the maximum folder depth Safety CLI should scan to in the target directory.
* **`exclude`**: A list of paths and files that Safety CLI should exclude from the scan. This supports Python's [pathlib glob pattern matching](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob), which are the same as for [fnmatch](https://docs.python.org/3/library/fnmatch.html#module-fnmatch), with the addition of `**` which indicates "this directory and all subdirectories, recursively". This supports Unix shell-style wildcards only, and not general regex patterns.
* **`include-files`**: The `Safety Scan` command does not allow single files to be targeted. If, however, files that you wish to be scanned are not included in the scan (e.g. because of non-standard naming conventions used), it is possible to use the `include-files` option of the policy file to include those files in your scan. See the code block above for an example of how to include such files.

#### Report

The **`report`** section of the policy file defines rules for which types and specific vulnerabilities Safety CLI should report on. This includes:&#x20;

* **`dependency-vulnerabilities`**: true/false value, set to false if you want to completely disable dependency vulnerability reporting.&#x20;
* **`auto-ignore-in-report`**: Everything defined under this key will be automatically ignored by Safety CLI and not included in reports or outputs.&#x20;
  * **`python:environment-results`**: true/false - sets whether Safety should report on the dependencies found in the current Python environment.&#x20;
  * **`python:unpinned-requirements`**: true/false - sets whether results should be returned for unpinned packages in requirements files, i.e. packages without a specified version.
  * **`cvss-severity`**: A list of CVSS severity values to ignore, options include: critical, high, medium,  low, and unknown. Any vulnerabilities found that match any of these severity values will be ignored and not included in Safety's scan report.
  * **`vulnerabilities`**: A list of specific vulnerabilities Safety should ignore, using Safety's vulnerability IDs, and including **`reason`** string and **`expires`** datetime properties for logging and audit purposes.

#### Fail Scan with Exit Code

**`fail-scan-with-exit-code`** section of the policy file defines rules for when Safety CLI should return non-zero (failing) exit codes, for running Safety CLI within build and integration pipelines such as GitHub Actions, Azure Pipelines, GitLab Pipelines, Jenkins, and CircleCI pipelines.

This gives you the flexibility to set different rules for what to report, and when to fail builds or pipelines.

* **`dependency-vulnerabilities`**: enabled/disabled
  * **`enabled`**:  true/false
  * **`fail-on-any-of`**: rules defining when Safety CLI should fail critical, high, meduim, low and unknown.&#x20;
    * **`cvss-severity`**: A list of CVSS severity values, options include: critical, high, medium,  low, and unknown. Any vulnerabilities Safety CLI reports on that match these CVSS severity labels will result in a failing exit code.
    * **`exploitability`**: A list of exploitability labels which should result in a failing exit code. This is a stub for the upcoming vulnerability EPSS score filtering feature.

{% hint style="info" %}
Note that some vulnerabilities do not have a CVSS severity score. To fail a scan when these vulnerabilities are detected, make sure to include a `cvss-severity` match for "unknown".
{% endhint %}

#### Security Updates

* **`auto-security-updates-limit`**: - patch/minor/major to determine the upper threshold for automatic application of fixes when Safety CLI is updating packages in a requirements.txt file. Note that if "major" is used, Safety will automatically apply fixes for all vulnerabilities, even if the next secure version is a major upgrade with breaking changes. \
  Additional information is available in the [Applying Fixes documentation](https://docs.safetycli.com/safety-docs/vulnerability-remediation/applying-fixes).

### Using a Safety CLI policy file&#x20;

Safety CLI will automatically use the `.safety-policy.yml` file in the root of the target directory being scanned by either `safety check` or `safety scan`.

If you want to reference a policy file that is not in your project root or scan target directory, set the policy file's path in the scan command using the `--policy-file` when running a scan.&#x20;

```
safety scan --policy-file path-to-custom-location-and-name.yml
```

You can confirm a local policy file is being found and used by Safety CLI in the top report section of the output.

### Validating a Safety CLI policy file&#x20;

Safety CLI's **`validate`** command can validate the correctness of a Safety CLI policy file.&#x20;

For example:

```
safety validate policy_file --path .safety-policy.yml
```

ensures Safety CLI is parsing your policy file correctly.


# Project Policies

{% hint style="info" %}
Project policies are similar to Safety Policy Files, but take precedence over policy files in cases where a codebase has been onboarded as a Safety Project.
{% endhint %}

## Creating a Project Policy

To create a policy for a project, visit <https://platform.safetycli.com> and complete these steps:

1. Select your project.
2. Click **Project Settings**.
3. Click **Policies**.
4. Select your policy and click **Edit**.
5. Build your policy using the guided policy builder, or alternatively click **Advanced Configuration** to build your policy using JSON.
6. Click **Save**.

## Migrating your Safety Policy File to a Project Policy

{% hint style="info" %}
We plan to introduce a feature that will automatically detect a local policy file during project creation and replicate this in the Project Policy. Until then, please follow these instructions.
{% endhint %}

To migrate a local policy file to a Project Policy, visit [https://platform.safetycli.com](https://platform.safetycli.com/) and complete these steps:

1. Click **Project Settings**.
2. Click **Policies**.
3. Select your policy and click **Edit**.
4. Scroll down and click **Advanced Configuration**.
5. Copy the contents of your local policy file.
6. Paste the policy file contents into the advanced configuration.
7. Click **Update Policy**.

## Modifying your Default Organization Policy

All Organizations in Safety Platform are initialized with a default Project Policy. When a new project is created, this organization policy is applied. You can modify your default organization policy by visiting [https://platform.safetycli.com](https://platform.safetycli.com/) and following these steps:<br>

1. From the top navigation items, click **Organization**.
2. From the left-hand navigation, click **Policies**.
3. Select your policy and click **Edit**.
4. Build your policy using the guided policy builder, or alternatively click **Advanced Configuration** to build your policy using JSON.
5. Click **Save**.<br>

Note that updated organization policies will not apply retrospectively to existing project policies, but instead will apply to any newly created projects.


# Output Options and Recommendations

Safety can output the result of a vulnerability scan to a variety of different output formats.&#x20;

The default output is `screen` output, which prints the scan to the command line screen.

Use the `--output` argument to configure which output format Safety generates. The `--output` command line argument can be set to the following values: `screen`, `json`, `html`, `spdx`, `spdx@2.2`, `spdx@2.3`, `none`.

## Screen and text output

`--output screen` (default) will print the results to the screen

Results can be easily saved to a text file. For example:&#x20;

```
safety scan --output screen > results.txt
```

{% hint style="info" %}
For more detailed output, add the **`--detailed-output`** flag
{% endhint %}

If `--detailed-output`  is specified along with `--output json`  then CVE details will be included in the output. In order to filter the json output to only 1 top-level key, the `--filter`  option can be specified. For example:

`safety scan --detailed-output --output json --filter cve_details`

Other options that can be chosen to filter are: `meta`, `scan_results`

## Additional Output Options

Full details on each output option can be found here:

* [JSON](https://docs.safetycli.com/safety-docs/output/json-output)
* [SBOM](https://docs.safetycli.com/safety-docs/output/sbom-output) (SPDX, SPDX\@2.2, SPDX\@2.3)
* [HTML5](https://docs.safetycli.com/safety-docs/output/html-output)


# JSON Output

Safety can generate JSON output, useful for parsing and analyzing the results of a scan. To do so, run the following command.

```
safety scan --output json
```

The JSON output is displayed in the terminal, as shown below. To save the JSON output to a file, use the following command, replacint `test.json` with your desired file name.

```
safety scan --output json >test.json
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FNZswLatSEzLQwd9qmEn9%2Fimage.png?alt=media&#x26;token=bab4b723-418a-4d9a-9ced-a92e3d1c7d9a" alt=""><figcaption></figcaption></figure>

### JSON structure

The resulting output is a JSON with the following sections:

`meta` contains meta information about the scan, such as timestamps, what was scanned, packages found and vulnerabilities found

`scanned_packages` is an array of packages (and versions) that were found during the scan

`affected_packages` is an array of packages that were found to have relevant vulnerabilities

`vulnerabilities` is an array of vulnerabilities that were found relating to the packages in the scan

`ignored_vulnerabilities` is an array of vulnerabilities that were found but were ignored via a command line argument or the safety policy file.

`remediations` an array of remediation (fix) recommendations for each package with relevant vulnerabilities.

`announcements` an array of announcements (messages) from the Safety team. These are not generally related to the packages of vulnerabilities found, but rather are more general announcements, such as announcing a new version of the Safety scanner.


# SBOM Output


# HTML Output

### HTML5 Output

It will return the primary information about the scan in HTML5 format.

`safety scan --output html`

To save the result into an HTML5 file in your current directory:

`safety scan --output html >output.html`


# Detecting Vulnerabilities and Sharing Results via Email

This guide outlines how to utilize the Safety CLI tool for detecting vulnerabilities within your project dependencies and automatically sending an email notification when vulnerabilities are detected.

This process involves configuring a policy file to define the behavior of the scan and crafting a command to execute the scan and send the email based on the scan results.

Configuring the Policy FileTo begin, generate a policy file that will dictate how the Safety CLI scanner operates. This policy file allows for customization of the scanning process, including setting parameters that prevent the scan from failing with an exit code when vulnerabilities are detected.&#x20;

Follow these steps:

1. **Generate a new policy file by running:**

```
safety generate policy_file
```

2. Open the generated `.safety_policy.yml` file and modify it as follows to prevent the scanner from exiting with a failure code due to detected vulnerabilities:

```
version: '3.0'

scanning-settings:
  max-depth: 8
  exclude: []
  include-files: []
  system:
    targets: []

report:
  dependency-vulnerabilities:
    enabled: true
    auto-ignore-in-report:
      python:
        environment-results: true
        unpinned-requirements: true
      cvss-severity: []

fail-scan-with-exit-code:
  dependency-vulnerabilities:
    enabled: false

security-updates:
  dependency-vulnerabilities:
    auto-security-updates-limit:
      - patch

```

​Place this `.safety_policy.yml` at the root of your project directory. For more detailed information on Safety CLI's policy file and its configurations, refer to the official documentation.

#### Running the Scan and Emailing Results <a href="#running-the-scan-and-emailing-results" id="running-the-scan-and-emailing-results"></a>

{% tabs %}
{% tab title="macOS and Unix" %}
This command performs a vulnerability scan using the Safety CLI tool, checks for any detected vulnerabilities, and sends an email notification if any vulnerabilities are found. It is designed to be executed in Unix and macOS environments.

1. **Scan Execution:** The Safety CLI tool is executed with a specified API key and stage. The results are saved in both JSON and human-readable text formats.
2. **Vulnerability Detection:** The `jq` tool is used to parse the JSON output to check for any known vulnerabilities.
3. **Email Notification:** If vulnerabilities are detected, an email is sent with the contents of the text report.

#### Command

Execute the command below in your terminal:

```
safety --key "API_KEY" –stage cicd scan --save-as json report.json > text_report && jq 'any(.scan_results.projects[].files[].results.dependencies[].specifications[].vulnerabilities.known_vulnerabilities[]; .id != null)' report.json | xargs -I {} test {} = "true" && cat text_report | mail -s "Vulnerabilities found" email@domain.com || true
```

* The `--save-as json report.json > text_report` part saves Safety CLI results in a JSON format to `report.json`, while redirecting the standard output to be saved as human-readable `text_report`.
* The `jq` command checks for the presence of any vulnerabilities by examining the `id` fields within the scan results. If any vulnerabilities are found (`true`), the subsequent command is triggered.
* `xargs -I {} test {} = "true"` uses the result from `jq` to conditionally proceed with sending an email if vulnerabilities are detected.
* The `mail` command constructs an email with the subject "Vulnerabilities found" and the content of `text_report`, sending it to the specified email address.
* The `|| true` ensures that, regardless of the exit codes in the pipe, the command sequence exits with a status code of `0` to prevent interrupting any automated pipelines due to a failure status.
  {% endtab %}

{% tab title="Windows" %}
This command performs a vulnerability scan using the Safety CLI tool, checks for any detected vulnerabilities, and sends an email notification if any vulnerabilities are found. It is designed to be executed in a Windows PowerShell environment.

1. **Scan Execution:** The Safety CLI tool is executed with a specified API key and stage. The results are saved in both JSON and human-readable text formats.
2. **Vulnerability Detection:** The vulnerability detection process involves the script first checking if the report.json file exists. Upon confirming its presence, the script then parses the JSON output to identify any known vulnerabilities.
3. **Email Notification:** If vulnerabilities are detected, an email is sent with the contents of the text report. The email configuration is specified using SMTP server details.

To send an email notification about detected vulnerabilities, you need to configure an SMTP (Simple Mail Transfer Protocol) server. An SMTP server is a critical component for email communication, acting as the mail delivery agent that sends outgoing emails from your system to the recipient’s email server. Configuring the SMTP server involves specifying the server address (e.g., smtp.sendgrid.net), the port number (typically 587 for TLS or 465 for SSL), and authentication credentials, which include the SMTP username and password, usually corresponding to an API key and its value. These credentials ensure secure and authenticated communication between your system and the SMTP server.

#### Command Variables

Before executing the command, you need to set the following variables:

* **API\_KEY**: The API key for the Safety CLI scan.
* **SMTP\_SERVER**: The SMTP server address (e.g., smtp.sendgrid.net).
* **SMTP\_PORT**: The SMTP server port (e.g., 587).
* **SMTP\_USER**: The SMTP username, typically an API key identifier.
* **SMTP\_PASSWORD**: The SMTP password, typically the API key value.
* **RECIPIENT\_EMAIL**: The email address to which the report will be sent.
* **SENDER\_EMAIL**: The email address from which the report will be sent.

#### Command

```powershell
safety scan --key <API_KEY> --stage cicd --save-as json report.json > text_report.txt
if (Test-Path -Path "report.json") {
    $jsonReport = Get-Content report.json | ConvertFrom-Json
    $vulnerabilitiesFound = $false
    foreach ($project in $jsonReport.scan_results.projects) {
        foreach ($file in $project.files) {
            foreach ($dependency in $file.results.dependencies) {
                foreach ($specification in $dependency.specifications) {
                    if ($specification.vulnerabilities.known_vulnerabilities.Count -gt 0) {
                        $vulnerabilitiesFound = $true
                        break
                    }
                }
                if ($vulnerabilitiesFound) { break }
            }
            if ($vulnerabilitiesFound) { break }
        }
        if ($vulnerabilitiesFound) { break }
    }
    if ($vulnerabilitiesFound) {
        $smtpServer = "<SMTP_SERVER>"
        $smtpPort = <SMTP_PORT>
        $smtpUser = "<SMTP_USER>"
        $smtpPassword = "<SMTP_PASSWORD>"
        $emailTo = "<RECIPIENT_EMAIL>"
        $emailFrom = "<SENDER_EMAIL>"
        $subject = "Vulnerabilities found"
        $body = Get-Content text_report.txt -Raw
        $smtpClient = New-Object Net.Mail.SmtpClient($smtpServer, $smtpPort)
        $smtpClient.EnableSsl = $true
        $smtpClient.Credentials = New-Object System.Net.NetworkCredential($smtpUser, $smtpPassword)
        $mailMessage = New-Object System.Net.Mail.MailMessage
        $mailMessage.From = $emailFrom
        $mailMessage.To.Add($emailTo)
        $mailMessage.Subject = $subject
        $mailMessage.Body = $body
        $mailMessage.IsBodyHtml = $true
        try {
            $smtpClient.Send($mailMessage)
            Write-Output "Email sent successfully"
        } catch {
            Write-Output "Failed to send email: $_"
            Write-Output "SMTP Server: $smtpServer"
            Write-Output "SMTP Port: $smtpPort"
            Write-Output "SMTP User: $smtpUser"
            Write-Output "SMTP Password: $smtpPassword"
        }
    } else {
        Write-Output "No vulnerabilities found"
    }
} else {
    Write-Output "report.json was not created, scan might have failed"
}
```

{% endtab %}
{% endtabs %}

#### Alternative Approaches <a href="#alternative-approaches" id="alternative-approaches"></a>

While the above command provides a quick and integrated solution for scanning and alerting, it's possible to incorporate this logic into a script for more complex workflows or to enhance readability and maintainability. This guide aims to facilitate a seamless integration of vulnerability scanning and notification within your CI/CD pipeline, ensuring that your team is promptly informed of any security issues detected in your project dependencies.


# Support

If you require additional support beyond the documentation available here, please reach out to our support team at <support@safetycli.com>.&#x20;


# Special Notes on Windows

### Setting the PYTHONENCODING Variable

In some Windows environments, Safety CLI will return an error when performing scans on files or directories that include special or accented characters, e.g. é, è, à, ç, et al.&#x20;

This issue occurs because the `PYTHONIOENCODING` variable is empty or not set to `utf-8`.

If you are using the Windows CMD, you can set the variable in the following way:

```
set PYTHONIOENCODING=utf-8
safety scan --output screen > results.txt
```

This set command updates the value per terminal session; if you want to do it permanently, you must add `PYTHONIOENCODING` with the value `utf-8` to your environment variables on Windows.&#x20;


# Invalid API Key Error

An invalid API key error means you are not using a valid Safety API key. If this API key was working previously, then the key may have been invalidated (for example, rotated) or your Safety account is no longer active.

#### How to get a Safety API key

If you already have a Safety account, once logged in you can find your API key on the [Teams and API Keys](https://manage.safetycli.com) page.

If you do not have a Safety account, you can obtain a Safety API key by [signing up ](https://manage.safetycli.com/create-account)for a free trial or a paid account.

If your team already has a Safety account and you need an API key assigned to you, please get in touch with your team's Safety admin to add you as a team member.

#### Using the Safety API key in Safety CLI

To access and utilize additional features of Safety, you will need to configure Safety to use an API key. There are two ways to do this:

* append your Safety commands with the command-line argument `--key 'your_api_key'`. For example `safety --key 'your_api_key' scan`
* save your API key as the environment variable `SAFETY_API_KEY`.\
  For example `export SAFETY_API_KEY=YOUR_API_KEY`

If you have any further questions, please don't hesitate to contact us via email at [support@s](mailto:support@pyup.io)[afetycli.com](mailto:support@safetycli.com).


# Headless Authentication

Learn how to authenticate sessions on machines with no browser, by leveraging a second machine with a browser.

For users who wish to perform scans on machines with no browser, e.g. EC2 instances, it is possible to authenticate the scan session by leveraging another machine with a browser installed.&#x20;

1. Start by installing the latest version of Safety:

```
pip install safety==3.4.0
```

2. When installed, start by authenticating the session using the new headless option.

```
safety auth login --headless
```

3. You should see the following: “Running in headless mode. Please copy and open the following URL in a browser. Copy and paste this url into your browser.”&#x20;

* Copy and paste the URL from the Terminal into a browser on another machine that does have one.
* Once authenticated on that browser a code will show on the success screen.
* Click the JSON code on the screen. This will copy the code to the clipboard.
* Paste that JSON code string into the original prompt in your Terminal.
* The Safety session should now be authenticated on the machine without a browser installed.&#x20;


# Implementation Support

## Allow List Requirements

To ensure Safety runs correctly in your environments, the following domains must be added to your allow-lists.

<table><thead><tr><th width="374">Domain</th><th>Purpose</th></tr></thead><tbody><tr><td>https://platform.safetycli.com<a href="https://manage.safetycli.comhttps/data.safetycli.comhttps://platform.safetycli.comhttps://auth.safetycli.com"><br><br></a></td><td>Web-based dashboards, account administration, core platform.</td></tr><tr><td>https://manage.safetycli.com</td><td>Dashboards and administration (being phased out in 2024)</td></tr><tr><td>https://auth.safetycli.com</td><td>Authentication</td></tr><tr><td>https://data.safetycli.com</td><td>Vulnerability Database, changelongs, etc.</td></tr></tbody></table>


# Global proxy and identity configuration

Safety CLI's proxy, authenticated, and other global settings can be configured at the system or user level so that these settings do not have to be repeated.

This configuration is stored in **`config.ini`** at Safety CLI's user or system path, which differs based on the operating system. Safety's **`configure`** command let's you easily set these configurations. Using Safety CLI enter **`safety configure --help`** for more details.


# Using Safety in Conda Environments

## Using Safety CLI with Anaconda Environments

### Overview

Safety CLI is the only dependency scanner powered by Safety's industry-leading vulnerability database. Safety CLI can be used to scan and secure Anaconda projects and environments, with some additional steps required to help make implementation and rollout seamless across your team.\
\
This guide will show you how to use Safety CLI effectively with your Anaconda projects.

### Table of Contents

* [General Process](#general-process)
* [Scanning Unix-based Systems (Linux/macOS)](#unix-based-systems-linux-macos)
* [Scanning Windows-based Systems](#windows-based-systems)
* [Notes](#important-note-1)

### General Process

To scan Anaconda environments with Safety CLI, the following general steps are recommended:

1. Export the Anaconda manifest (list of packages in the Anaconda project):

   ```bash
   conda activate your_environment_name
   conda list -e > requirements.txt
   ```
2. Separate pip-installed packages and conda-installed packages into two separate temporary requirements.txt files (instructions and examples for this below)
3. Scan the separated requirements files using `safety scan`
4. Delete the temporary requirements.txt files that were created

### Unix-based Systems (Linux/macOS)

For a streamlined workflow on Unix-based systems, use the following bash script:

```bash
#!/bin/bash

# Function to clean up temporary files
cleanup() {
    rm -f requirements.txt conda_requirements.txt pip_requirements.txt
}

# Trap to ensure cleanup happens even if the script is interrupted
trap cleanup EXIT

# Generate requirements file
conda list -e > requirements.txt

# Function to separate conda and pip packages
separate_requirements() {
    local input_file=$1
    local conda_output=$2
    local pip_output=$3

    > "$conda_output"
    > "$pip_output"

    while IFS= read -r line
    do
        if [[ $line =~ ^#.*$ ]] || [[ -z $line ]]; then
            echo "$line" >> "$conda_output"
        elif [[ $line == *"=pypi_0"* ]]; then
            package_info=$(echo "$line" | sed 's/=/==/;s/=pypi_0//')
            echo "$package_info" >> "$pip_output"
        else
            package_info=$(echo "$line" | awk -F= '{print $1"=="$2" #"$3}')
            echo "$package_info" >> "$conda_output"
        fi
    done < "$input_file"
}

# Separate requirements
separate_requirements "requirements.txt" "conda_requirements.txt" "pip_requirements.txt"

# Run safety with all arguments passed to this script
safety "$@"

# Cleanup is handled by the trap
```

#### Usage

1. Save the script as `conda_safety.sh`
2. Make it executable: `chmod +x conda_safety.sh`
3. Run the script as a replacement for the `safety` command, using any Safety CLI arguments. For example:

```
conda activate <your_environment_name>
./conda_safety.sh scan
```

or

```
conda activate <your_environment_name>
./conda_safety.sh scan --output json
```

#### Setting Up as a Command using an alias

To use the script as a command:

1. Add an alias in your shell configuration file (`~/.bashrc` or `~/.zshrc`):

   ```
   alias conda-safety='/path/to/your/conda_safety.sh'
   ```
2. Reload your shell configuration:

   ```
   source ~/.bashrc  # or ~/.zshrc for Zsh
   ```

Now you can use `conda-safety` as a drop-in replacement for the `safety` command. Once you've activated your conda environment, use \`conda-safety\`. For example:

```
conda activate <your_environment_name>
conda-safety auth
conda-safety scan
```

### Windows-based Systems

For Windows users, use the following PowerShell script:

```powershell
# Function to clean up temporary files
function Cleanup {
    Remove-Item -ErrorAction SilentlyContinue requirements.txt, conda_requirements.txt, pip_requirements.txt
}

# Ensure cleanup happens even if the script is interrupted
trap { Cleanup; break }

# Generate requirements file
conda list -e > requirements.txt

# Function to separate conda and pip packages
function Separate-Requirements {
    param (
        [string]$InputFile,
        [string]$CondaOutput,
        [string]$PipOutput
    )

    $null > $CondaOutput
    $null > $PipOutput

    Get-Content $InputFile | ForEach-Object {
        if ($_ -match '^#' -or $_ -eq '') {
            $_ >> $CondaOutput
        }
        elseif ($_ -match '=pypi_0') {
            $packageInfo = $_ -replace '=', '==' -replace '=pypi_0', ''
            $packageInfo >> $PipOutput
        }
        else {
            $parts = $_ -split '='
            "$($parts[0])==$($parts[1]) #$($parts[2])" >> $CondaOutput
        }
    }
}

# Separate requirements
Separate-Requirements "requirements.txt" "conda_requirements.txt" "pip_requirements.txt"

# Run safety with all arguments passed to this script
safety $args

# Cleanup
Cleanup
```

#### Usage

1. Save the script as `Conda-Safety.ps1`
2. Open PowerShell and navigate to the script's directory
3. Run the script with Safety CLI arguments:

```
conda activate <your_environment_name>
.\Conda-Safety.ps1 scan
```

or

```
conda activate <your_environment_name>
.\Conda-Safety.ps1 scan --output json
```

#### Setting Up as a Command

To use the script as a command in Windows:

1. Create a directory for the script if it doesn't exist:

   ```
   mkdir C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts
   ```
2. Move the script to this directory:

   ```
   Move-Item Conda-Safety.ps1 C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts
   ```
3. Add the directory to your PATH:
   * Open System Properties
   * Click on Environment Variables
   * Under System Variables, find and edit the PATH variable
   * Add `C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts`
4. Create a PowerShell profile if you don't have one:

   ```
   if (!(Test-Path -Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
   ```
5. Add this line to your PowerShell profile:

   ```
   Set-Alias conda-safety C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts\Conda-Safety.ps1
   ```

Now you can use `conda-safety` as a command in PowerShell as a drop-in replacement for the `safety` command. This requires `safety` and `conda` to already be installed and available in Powershell.

### Important Note

Conda-installed packages may differ from standard PyPI packages. As a result, security findings for conda-installed packages may differ from PyPi equivalent packages. Always verify findings for conda-installed packages against the specific versions in your Anaconda environment.

### Help and Implementation Assistance

Anaconda environments and setups vary. If the instructions above do not work or you encouter any issues, please don't hesitate to reach out to our support team at <support@safetycli.com>. We're here to help you ensure the security of your Python projects, regardless of your environment setup.


# Understanding Vulnerability Scoring Systems: CVSS and EPSS

This guide provides a comprehensive comparison between two major vulnerability scoring systems: the Common Vulnerability Scoring System (CVSS) and the Exploit Prediction Scoring System (EPSS).

## CVSS and EPSS

In today's rapidly evolving cybersecurity landscape, effectively prioritizing vulnerability remediation has become more critical than ever. Security teams face an overwhelming number of vulnerabilities across their systems, making it crucial to have reliable methods for assessing which ones pose the greatest risk and require immediate attention.

For many years, the Common Vulnerability Scoring System (CVSS) has served as the primary framework for evaluating vulnerability severity. However, the emergence of the Exploit Prediction Scoring System (EPSS) represents a significant shift in how we approach vulnerability prioritization. While CVSS focuses on the theoretical severity of vulnerabilities, EPSS takes a data-driven approach to predict the likelihood of actual exploitation in the wild.

This guide explores both scoring systems, their methodologies, and how they complement each other in modern vulnerability management practices. Whether you're a security practitioner, manager, or stakeholder, understanding these systems is essential for making informed decisions about vulnerability prioritization and resource allocation.

{% tabs %}
{% tab title="CVSS" %}

## Common Vulnerability Scoring System (CVSS)

CVSS is a framework for assessing the severity of computer system security vulnerabilities. It aims to provide a standardized method for rating vulnerabilities.

#### Key Components of CVSS

CVSS consists of three metric groups:

1. Base Score Metrics
   * Assess the intrinsic characteristics of a vulnerability
   * Include exploitability metrics (attack vector, complexity, privileges required, user interaction)
   * Consider impact metrics (confidentiality, integrity, availability)
2. Temporal Score Metrics
   * Reflect characteristics that change over time
   * Consider exploit code maturity, remediation level, and report confidence
3. Environmental Score Metrics
   * Allow for context-specific adjustments
   * Account for the security requirements of your implementation

#### CVSS Scoring Scale

* Scores range from 0.0 to 10.0
* Critical: 9.0-10.0
* High: 7.0-8.9
* Medium: 4.0-6.9
* Low: 0.1-3.9
* None: 0.0
  {% endtab %}

{% tab title="EPSS" %}

### Exploit Prediction Scoring System (EPSS)

EPSS is a data-driven effort for estimating the probability that a software vulnerability will be exploited in the wild. Unlike CVSS, which measures severity, EPSS predicts the likelihood of exploitation.

#### Key Features of EPSS

1. Probability-Based Approach
   * Provides a probability score between 0 and 1
   * Based on real-world exploitation data
   * Updated daily to reflect current threat landscape
2. Machine Learning Foundation
   * Uses various data points and features to make predictions
   * Considers factors like vulnerability characteristics, social media mentions, and exploit availability
3. Dynamic Nature
   * Scores change based on new data and observations
   * Reflects real-world exploitation patterns
     {% endtab %}
     {% endtabs %}

### Comparison Table: CVSS vs EPSS

| Aspect                | CVSS                                           | EPSS                                 |
| --------------------- | ---------------------------------------------- | ------------------------------------ |
| Primary Purpose       | Measures vulnerability severity                | Predicts exploitation probability    |
| Score Range           | 0.0 to 10.0                                    | 0 to 1 (probability)                 |
| Update Frequency      | Static (unless manually updated)               | Daily                                |
| Methodology           | Expert-driven framework                        | Data-driven machine learning         |
| Complexity            | Complex (3 metric groups, multiple sub-scores) | Simple (single probability score)    |
| Context Consideration | Through environmental metrics                  | Through real-world exploitation data |
| Industry Maturity     | Well-established (20+ years)                   | Emerging standard                    |
| Primary Use Case      | Vulnerability severity assessment              | Exploitation risk prioritization     |
| Data Source           | Theoretical assessment                         | Real-world exploitation data         |
| Adaptability          | Manual updates needed                          | Automatically adapts to new threats  |


# Release Notes

## Safety 3.4.0


# Breaking Changes in Safety 3

As a major version upgrade, Safety 3.x includes several breaking changes over versions 2.x, which are summarized below. For more information on migrating from Safety CLI 2.x to Safety CLI 3.x, please refer to our [migration guide.](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/migrating-from-safety-cli-2.x-to-safety-cli-3.x)

| Breaking Change Category                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Command Update                                       | `safety check` command is replaced by `safety scan`. The new command is more powerful and configurable, providing recursive search in the target directory, native support for various dependency files, and customizable scan settings.                                                                                                                                                                                                                                                                                     |
| Configuration File                                   | The `.safety-policy.yml` file structure has changed. The new format is incompatible with the old one used by `safety check`. Users need to convert their existing policy files to the new format for compatibility with `safety scan`.                                                                                                                                                                                                                                                                                       |
| Policy File Changes                                  | Specific configurations in the old policy file need to be translated to the new format. Notably, `security:ignore-vulnerabilities` moves to `report:auto-ignore-in-report:vulnerabilities`, `security:ignore-cvss-severity-below` and `security:ignore-cvss-unknown-severity` combine into `report:auto-ignore-in-report:cvss-severity`, and `security:continue-on-vulnerability-error:True` is replaced by `fail-scan-with-exit-code:dependency-vulnerabilities:enabled:False`. The `alert` section is no longer supported. |
| Scan Target Settings                                 | The `-r` flag for specifying `requirements.txt` files in `safety check` is no longer needed in `safety scan` as it finds these files automatically. The `scanning-settings:exclude` property in the new policy file can be used to exclude specific files or folders from scans.                                                                                                                                                                                                                                             |
| JSON Output Format                                   | Safety CLI 3 introduces a new JSON output format for `safety scan` that is substantially different from `safety check`’s JSON output. If upgrading from Safety CLI 2.x and using JSON output, users may face breaking changes in the JSON structure if upgrading from versions earlier than 2.4.0b.                                                                                                                                                                                                                          |
| Using Both `Safety Check` and `Safety Scan` Commands | Safety CLI 3 allows running both `safety check` and `safety scan` commands, each with their separate policy files. To continue using both, the old policy file must be renamed (e.g., `.safety-check-policy.yml`) and specified when using `safety check`.                                                                                                                                                                                                                                                                   |
| Validate Command                                     | When using the `validate` command, Safety CLI 3 will validate a 3.0 policy file by default.                                                                                                                                                                                                                                                                                                                                                                                                                                  |

{% hint style="info" %}
**Targeting Specific Requirements Files**

In Safety CLI 2, it was possible to target specific requirements files. The new Safety Scan command is designed to allow you to scan all files in a project directory (or sub-directory) simultaneously rather than running separate scans targeted on each file.

The [Policy File](https://docs.safetycli.com/safety-docs/administration/safety-policy-files) enables you to control the depth of those scans to detect nested requirements files, e.g. six folders deep within the current directory.

If you wish to specify a target directory for the Safety Scan, you can do so using the **`--target`** option, e.g. `safety scan`` `**`--target /path/to/project`**. Safety Scan does not allow you to target single files, but the include-files section of the Policy File does allow you to include specific files in your scan if these are not detected in a normal scan.&#x20;

Example:

**`include-files:`**

**`- path: inside_target_dir/requirements-docs.txt`**&#x20;

**`file-type: requirements.txt`**

**`- path: inside_target_dir/requirements-dev.txt`**

**`file-type: requirements.txt`**

When running a new Safety Scan, the new CLI output will separate findings and recommendations by requirements file, e.g. requirements.txt will have its own set of recommendations, requirements-dev.txt will have its own, etc. This means that instead of running separate scans for each file, you can now run one simple scan and see all findings and recommendations in one output.
{% endhint %}


