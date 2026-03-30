# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started/installation.md

# Installation

Install Tabnine CLI on your system.

### Prerequisites

* **Node.js** version **22** or higher
* Access to a tabnine host
* Tabnine Agents enabled for your team

### Download and Install

Run the appropriate command for your platform. Replace `<YOUR TABNINE HOST>` with the URL of your tabnine console (For example: <https://console.tabnine.com>):

#### macOS, Linux, WSL

```bash
export TABNINE_HOST="<YOUR TABNINE HOST>"
curl $TABNINE_HOST/update/cli/installer.mjs | node --input-type=module - $TABNINE_HOST
```

#### Windows PowerShell

```powershell
$env:TABNINE_HOST = "<YOUR TABNINE HOST>"
irm $env:TABNINE_HOST/update/cli/installer.mjs | node --input-type=module - $env:TABNINE_HOST
```

#### Windows CMD

```cmd
set TABNINE_HOST="<YOUR TABNINE HOST>"
curl %TABNINE_HOST%/update/cli/installer.mjs | node --input-type=module - %TABNINE_HOST%
```

### Add to PATH

After installation, add Tabnine CLI to your PATH.

#### macOS, Linux, WSL

The default installation location is:

```
~/.local/bin/tabnine
```

**Note**: `~/.local/` is different than `/local/`. If you don't have a `~/.local/` folder, create it first:

```bash
mkdir -p ~/.local/bin
```

Add to your PATH by adding this line to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload your shell configuration:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### Windows

The installer should add Tabnine CLI to your PATH automatically. If not, add the installation directory manually:

{% stepper %}
{% step %}
**Open System Properties**

Open **System Properties** → **Environment Variables**.
{% endstep %}

{% step %}
**Edit User Path**

Under **User variables**, select **Path** and click **Edit**.
{% endstep %}

{% step %}
**Add Directory**

Add the Tabnine CLI installation directory.
{% endstep %}

{% step %}
**Save**

Click **OK** to save.
{% endstep %}
{% endstepper %}

### Verify Installation

Check that Tabnine CLI is correctly installed:

```bash
tabnine --version
```

You should see the version number displayed.

### First Run

Start Tabnine CLI:

```bash
tabnine
```

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2F4MrGR8xawkOov9vOrdhS%2Ftabnine%20CLI%20open.gif?alt=media&#x26;token=4fb24c4b-5824-4434-b610-26b9f3ff268d" alt=""><figcaption></figcaption></figure>

#### Authentication

On first run, you'll be prompted to sign in to Tabnine:

{% stepper %}
{% step %}
Press **OK** when prompted for authentication.
{% endstep %}

{% step %}
Your browser will open to `tabnine.com`.
{% endstep %}

{% step %}
If you're already signed in, authentication will be automatic.
{% endstep %}

{% step %}
If not, log in with your Tabnine credentials.
{% endstep %}

{% step %}
Return to the terminal - you're ready to use Tabnine CLI!
{% endstep %}
{% endstepper %}

### Troubleshooting

<details>

<summary>"Command not found: tabnine"</summary>

Solution: Ensure Tabnine CLI is in your PATH:

```bash
# Check if the binary exists
ls ~/.local/bin/tabnine

# Verify PATH includes the directory
echo $PATH | grep ".local/bin"

# If not in PATH, add it (see "Add to PATH" section above)
```

</details>

<details>

<summary>"Node.js not found"</summary>

Solution: Install Node.js version 20 or higher from [nodejs.org](https://nodejs.org/)

</details>

<details>

<summary>Installation Fails</summary>

Common causes:

* No access to tabnine host
* Node.js version too old
* Insufficient permissions

Solutions:

* Check network connection
* Update Node.js: `node --version` (should be 20+)
* On Unix systems, ensure `~/.local/bin` has write permissions

</details>

<details>

<summary>Authentication Fails</summary>

Solution: See the [Troubleshooting](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting) section.

</details>

### Updating Tabnine CLI

Tabnine CLI checks for updates automatically. To manually update, re-run the installer according to the [installation instructions](#download-and-install).

Sometimes, you will be prompted to restart Tabnine CLI following an update. This will typically happen at the beginning of a session, as seen here:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FZJvHY1XPKRRFmNqpzIVA%2FUpdate%20rerun%20tabnine.png?alt=media&#x26;token=9c4fbcf2-0517-46c2-afe2-4cb213fffcce" alt=""><figcaption><p>You may be asked to re-run Tabnine after an update</p></figcaption></figure>

### Uninstall

To remove Tabnine CLI:

#### macOS, Linux, WSL

```bash
rm -rf ~/.tabnine/agent
rm ~/.local/bin/tabnine
```

#### Windows

```powershell
Remove-Item -Recurse -Force $env:USERPROFILE\.tabnine\agent

# Remove tabnine.exe from installation directory
```

Then remove the installation directory from your PATH.
