# Source: https://docs.socket.dev/docs/socket-firewall-enterprise-wrapper-mode.md

# Enterprise Wrapper Mode

Socket Firewall's wrapper mode runs locally on developer machines, intercepting package manager commands and enforcing security policies before packages are downloaded.

## Installation

Download the latest `sfw` binary from the [releases page](https://github.com/SocketDev/firewall-release/releases).

1. Download the appropriate binary for your platform
2. Rename it to `sfw` (or `sfw.exe` on Windows)
3. Make it executable (Linux/macOS): `chmod +x sfw`
4. Add it to your `PATH`

**macOS Note:** You may need to allow execution by running:

```bash
xattr -dr com.apple.quarantine ./path/to/sfw
```

## Basic Usage

Prefix any package manager command with `sfw`:

```bash
sfw npm install lodash
sfw pip install requests
sfw cargo add serde
```

The wrapper automatically handles proxy initialization, certificate generation, environment setup, command execution, and cleanup.

## Configuration

### API Token

Set your Socket API token via environment variable:

```bash
export SOCKET_API_KEY=sktsec_your_api_key_here
sfw npm install lodash
```

Or create a `.sfw.config` file in your project or home directory:

```
SOCKET_API_KEY=sktsec_your_api_key_here
```

Using configuration files allows different API tokens per repository, enabling distinct Socket organizations and security policies on a per-project basis.

The API token requires scopes: `packages` and `entitlements:list`.

For additional configuration options, see [Enterprise Configuration](./socket-firewall-enterprise-configuration).

***

## Shell Configuration for Transparent Usage

Instead of typing `sfw npm install`, you can configure your shell so that `npm install` automatically routes through Socket Firewall.

### Supported Commands

| Ecosystem             | Commands              |
| --------------------- | --------------------- |
| JavaScript/TypeScript | `npm`, `yarn`, `pnpm` |
| Python                | `pip`, `pip3`, `uv`   |
| Rust                  | `cargo`               |
| Go                    | `go`                  |
| Java/Scala/Kotlin     | `mvn`, `gradle`       |
| Ruby                  | `gem`, `bundle`       |
| .NET                  | `dotnet`              |

***

### macOS / Linux Setup

#### Zsh (\~/.zshrc)

Add to your `~/.zshrc`:

```bash
# Socket Firewall Aliases
# JavaScript/TypeScript
alias npm="sfw npm"
alias yarn="sfw yarn"
alias pnpm="sfw pnpm"

# Python
alias pip="sfw pip"
alias pip3="sfw pip3"
alias uv="sfw uv"

# Rust
alias cargo="sfw cargo"

# Go
alias go="sfw go"

# Java/Scala/Kotlin
alias mvn="sfw mvn"
alias gradle="sfw gradle"

# Ruby
alias gem="sfw gem"
alias bundle="sfw bundle"

# .NET
alias dotnet="sfw dotnet"
```

Apply changes:

```bash
source ~/.zshrc
```

#### Bash (\~/.bashrc)

Add to your `~/.bashrc`:

```bash
# Socket Firewall Aliases
# JavaScript/TypeScript
alias npm="sfw npm"
alias yarn="sfw yarn"
alias pnpm="sfw pnpm"

# Python
alias pip="sfw pip"
alias pip3="sfw pip3"
alias uv="sfw uv"

# Rust
alias cargo="sfw cargo"

# Go
alias go="sfw go"

# Java/Scala/Kotlin
alias mvn="sfw mvn"
alias gradle="sfw gradle"

# Ruby
alias gem="sfw gem"
alias bundle="sfw bundle"

# .NET
alias dotnet="sfw dotnet"
```

Apply changes:

```bash
source ~/.bashrc
```

#### Alternative: Shell Functions

If aliases conflict with existing configuration, use functions instead:

```bash
# Add to ~/.zshrc or ~/.bashrc
npm() { sfw npm "$@"; }
yarn() { sfw yarn "$@"; }
pnpm() { sfw pnpm "$@"; }
pip() { sfw pip "$@"; }
pip3() { sfw pip3 "$@"; }
uv() { sfw uv "$@"; }
cargo() { sfw cargo "$@"; }
go() { sfw go "$@"; }
mvn() { sfw mvn "$@"; }
gradle() { sfw gradle "$@"; }
gem() { sfw gem "$@"; }
bundle() { sfw bundle "$@"; }
dotnet() { sfw dotnet "$@"; }
```

***

### Windows Setup (PowerShell)

#### Locate Your Profile

Check if your profile exists:

```powershell
Test-Path $PROFILE
```

If it returns `False`, create it:

```powershell
New-Item -Path $PROFILE -ItemType File -Force
```

Open for editing:

```powershell
notepad $PROFILE
```

#### Add Function Wrappers

Add to your `$PROFILE`:

```powershell
# Socket Firewall Function Wrappers

# JavaScript/TypeScript
function npm { sfw npm @args }
function yarn { sfw yarn @args }
function pnpm { sfw pnpm @args }

# Python
function pip { sfw pip @args }
function pip3 { sfw pip3 @args }
function uv { sfw uv @args }

# Rust
function cargo { sfw cargo @args }

# Go
function go { sfw go @args }

# Java/Scala/Kotlin
function mvn { sfw mvn @args }
function gradle { sfw gradle @args }

# Ruby
function gem { sfw gem @args }
function bundle { sfw bundle @args }

# .NET
function dotnet { sfw dotnet @args }
```

Apply changes:

```powershell
. $PROFILE
```

#### Alternative: Set-Alias with Functions

For cleaner separation:

```powershell
function Invoke-SfwNpm { sfw npm @args }
Set-Alias -Name npm -Value Invoke-SfwNpm -Option AllScope -Force

function Invoke-SfwYarn { sfw yarn @args }
Set-Alias -Name yarn -Value Invoke-SfwYarn -Option AllScope -Force

function Invoke-SfwPnpm { sfw pnpm @args }
Set-Alias -Name pnpm -Value Invoke-SfwPnpm -Option AllScope -Force

# Add similar patterns for other commands as needed
```

***

### Verification

#### macOS / Linux

```bash
# Check alias definition
type npm
# Expected: npm is an alias for sfw npm

# Or for functions
type npm
# Expected: npm is a shell function

# Test execution
npm --version
```

#### Windows (PowerShell)

```powershell
# Check function definition
Get-Command npm
# Expected: CommandType shows Function

# View definition
(Get-Command npm).Definition
# Expected: sfw npm @args

# Test execution
npm --version
```

***

### Bypassing the Wrapper

To run the original command without Socket Firewall:

#### macOS / Linux

```bash
# Use command builtin
command npm install lodash

# Or use full path
/usr/local/bin/npm install lodash
```

#### Windows (PowerShell)

```powershell
# Use full path
& "C:\Program Files\nodejs\npm.cmd" install lodash

# Or temporarily remove the function
Remove-Item Function:\npm
npm install lodash
```

***

### Selective Ecosystem Protection

Add only the aliases for ecosystems you need. Example for JavaScript only:

**macOS/Linux:**

```bash
# Socket Firewall - JavaScript only
alias npm="sfw npm"
alias yarn="sfw yarn"
alias pnpm="sfw pnpm"
```

**Windows:**

```powershell
# Socket Firewall - JavaScript only
function npm { sfw npm @args }
function yarn { sfw yarn @args }
function pnpm { sfw pnpm @args }
```

***

### Troubleshooting

| Issue                               | Solution                                                         |
| ----------------------------------- | ---------------------------------------------------------------- |
| `sfw: command not found`            | Ensure `sfw` is installed and in your `PATH`                     |
| Alias not working after restart     | Verify changes are in the correct rc file and it's being sourced |
| PowerShell execution policy error   | Run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`        |
| Alias conflicts with existing alias | Use shell functions instead of aliases                           |
| Arguments not passed correctly      | Ensure `"$@"` (bash/zsh) or `@args` (PowerShell) is used         |

<br />