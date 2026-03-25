# Source: https://docs.safetycli.com/safety-docs/firewall/installation-and-configuration/installing-safety-cli-via-binary.md

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
