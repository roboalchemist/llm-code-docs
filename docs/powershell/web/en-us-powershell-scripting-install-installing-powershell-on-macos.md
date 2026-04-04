# Source: https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-macos

Title: Install PowerShell 7 on macOS - PowerShell

URL Source: https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-macos

Markdown Content:
There are multiple package versions of PowerShell 7 that can be installed. This article focuses on installing the latest stable release package. For more information about the package versions, see the [PowerShell Support Lifecycle](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle?view=powershell-7.5) article.

Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7. Preview versions of PowerShell can be installed side-by-side with other versions of PowerShell. Newer preview versions replace existing previous preview versions. If you need to run PowerShell 7.5 side-by-side with a previous version, reinstall the previous version using the binary archive method.

There are several ways to install PowerShell on macOS. Homebrew is the preferred installation method.

Homebrew is the preferred package manager for macOS. If the `brew` command isn't found, you need to install Homebrew following [their instructions](https://brew.sh/).

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once `brew` is installed, install PowerShell.

The following command installs the latest stable release of PowerShell:

```
brew install --cask powershell
```

If you want the LTS or Preview version of PowerShell, you can install it using Homebrew's tap method. Select tap version you want to install:

*   `powershell/tap/powershell-lts`
*   `powershell/tap/powershell-preview`

For example, use the following command to install the Preview release:

```
brew install powershell/tap/powershell-preview
```

Download the install package from the [releases](https://aka.ms/powershell-release?tag=stable) page. Select the package version you want to install.

*   PowerShell 7.5 
    *   Arm64 processors - [powershell-7.5.4-arm64.pkg](https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/powershell-7.5.4-osx-arm64.pkg)
    *   x64 processors - [powershell-7.5.4-osx-x64.pkg](https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/powershell-7.5.4-osx-x64.pkg)

*   PowerShell 7.4 (LTS) 
    *   Arm64 processors - [powershell-7.4.13-osx-arm64.pkg](https://github.com/PowerShell/PowerShell/releases/download/v7.4.13/powershell-7.4.13-osx-arm64.pkg)
    *   x64 processors - [powershell-7.4.13-osx-x64.pkg](https://github.com/PowerShell/PowerShell/releases/download/v7.4.13/powershell-7.4.13-osx-x64.pkg)

*   PowerShell 7.6-preview 
    *   Arm64 processors - [powershell-7.6.0-rc1-osx-arm64.pkg](https://github.com/PowerShell/PowerShell/releases/download/v7.6.0-rc1/powershell-7.6.0-rc1-osx-arm64.pkg)
    *   x64 processors - [powershell-7.6.0-rc1-osx-x64.pkg](https://github.com/PowerShell/PowerShell/releases/download/v7.6.0-rc1/powershell-7.6.0-rc1-osx-x64.pkg)

There are two ways to install PowerShell using the downloaded package.

Install PowerShell using Finder:

1.   Open **Finder**

2.   Locate the downloaded package

3.   Double-click the file

You will receive the following error message when installing the package:

> "powershell-7.5.4-osx-arm64.pkg" Not Opened
> 
> 
> Apple could not verify "powershell-7.5.4-osx-arm64.pkg" is free from malware that may harm your Mac or compromise your privacy.

4.   Select the **Done** button to close the prompt.

This error message comes from the Gatekeeper feature of macOS. For more information, see [Safely open apps on your Mac - Apple Support](https://support.apple.com/102445).

After you've tried to open the package, follow these steps:

1.   Open **System Settings**.
2.   Select **Privacy & Security** and scroll down to the **Security** section.
3.   Select the **Open Anyway** button to confirm your intent to install PowerShell.
4.   When the warning prompt reappears, select **Open Anyway**.
5.   Enter username and password to allow the installation to proceed.

To install the PowerShell package from the command line, you must bypass the Gatekeeper checks. Use one of the following methods to install the package:

*   Run the `installer` command with the **allowUntrusted** flag:

```
sudo installer -allowUntrusted -pkg ./Downloads/powershell-7.5.4-osx-arm64.pkg -target /
```
*   Or install the package as you normally would after running one of the following commands:

    *   Run `sudo xattr -rd com.apple.quarantine ./Downloads/powershell-7.5.4-osx-arm64.pkg`.
    *   Use the `Unblock-File` cmdlet if you're using PowerShell. Include the full path to the `.pkg` file.

If you already have the [.NET Core SDK](https://learn.microsoft.com/en-us/dotnet/core/sdk) installed, you can use the [.NET Global tool](https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools) to install PowerShell 7.

```
dotnet tool install --global PowerShell
```

The dotnet tool installer adds `~/.dotnet/tools` to your `PATH` environment variable. However, the currently running shell doesn't have the updated `PATH`. Start PowerShell from a new shell by typing `pwsh`.

PowerShell binary `tar.gz` archives are provided for the macOS platform to enable advanced deployment scenarios. When you install using this method, you must also manually install any dependencies.

Download the install package from the [releases](https://aka.ms/powershell-release?tag=stable) page onto your Mac. Select the archive version you want to install.

*   PowerShell 7.4 (LTS) 
    *   Arm64 processors - [powershell-7.4.13-osx-arm64.tar.gz](https://github.com/PowerShell/PowerShell/releases/download/v7.4.13/powershell-7.4.13-osx-arm64.tar.gz)
    *   x64 processors - [powershell-7.4.13-osx-x64.tar.gz](https://github.com/PowerShell/PowerShell/releases/download/v7.4.13/powershell-7.4.13-osx-x64.tar.gz)

*   PowerShell 7.5 
    *   Arm64 processors - [powershell-7.5.4-osx-arm64.tar.gz](https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/powershell-7.5.4-osx-arm64.tar.gz)
    *   x64 processors - [powershell-7.5.4-osx-x64.tar.gz](https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/powershell-7.5.4-osx-x64.tar.gz)

*   PowerShell 7.6-preview 
    *   Arm64 processors - [powershell-7.6.0-rc1-osx-arm64.tar.gz](https://github.com/PowerShell/PowerShell/releases/download/v7.6.0-rc1/powershell-7.6.0-rc1-osx-arm64.tar.gz)
    *   x64 processors - [powershell-7.6.0-rc1-osx-x64.tar.gz](https://github.com/PowerShell/PowerShell/releases/download/v7.6.0-rc1/powershell-7.6.0-rc1-osx-x64.tar.gz)

Use the following commands to install PowerShell from the binary archive. Change the download URL to match the version you want to install.

```
# Download the powershell '.tar.gz' archive
curl -L -o /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/powershell-7.5.4-osx-arm64.tar.gz

# Create the target folder where powershell is placed
sudo mkdir -p /usr/local/microsoft/powershell/7

# Expand powershell to the target folder
sudo tar zxf /tmp/powershell.tar.gz -C /usr/local/microsoft/powershell/7

# Set execute permissions
sudo chmod +x /usr/local/microsoft/powershell/7/pwsh

# Create the symbolic link that points to pwsh
sudo ln -s /usr/local/microsoft/powershell/7/pwsh /usr/local/bin/pwsh
```

After the package is installed, run `pwsh` from a terminal. If you have installed a Preview package, run `pwsh-preview`.

*   The location of `$PSHOME` varies based on the package you installed. 
    *   For Stable and LTS packages: `/usr/local/microsoft/powershell/7/`
    *   For Preview packages: `/usr/local/microsoft/powershell/7-preview/`
    *   The macOS install package creates a symbolic link, `/usr/local/bin/pwsh` that points to `pwsh` in the `$PSHOME` location.

*   User profiles are read from `~/.config/powershell/profile.ps1`
*   Default profiles are read from `$PSHOME/profile.ps1`
*   User modules are read from `~/.local/share/powershell/Modules`
*   Shared modules are read from `/usr/local/share/powershell/Modules`
*   Default modules are read from `$PSHOME/Modules`
*   PSReadLine history is recorded to `~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt`

PowerShell respects the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/latest/) on macOS.

Run the following commands to update the installed version of PowerShell to the latest release.

```
brew update
brew upgrade powershell
```

Note

When updating to a newer version of PowerShell, use the same method, cask or the tap, that you used to perform the initial install. If you use a different method, opening a new pwsh session continues to use the older version of PowerShell.

If you decide to use different methods, there are ways to correct the issue using the [Homebrew link method](https://docs.brew.sh/Manpage#link-ln-options-formula).

If you installed PowerShell with Homebrew, use the following command to uninstall:

```
brew uninstall --cask powershell
```

If you manually installed PowerShell 7, you must manually remove it. The following command removes the symbolic link and PowerShell files.

```
sudo rm -rf /usr/local/bin/pwsh /usr/local/microsoft/powershell
```

Use `sudo rm` to remove any other remaining PowerShell files and folders.

Microsoft supports PowerShell until [PowerShell reaches end-of-support](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle) or the version of macOS reaches end-of-support.

The following versions of macOS are supported:

*   macOS 26 (Tahoe) x64 and Arm64
*   macOS 15 (Sequoia) x64 and Arm64
*   macOS 14 (Sonoma) x64 and Arm64

Apple determines the support lifecycle of macOS. For more information, see the following:

*   [macOS release notes](https://developer.apple.com/documentation/macos-release-notes)
*   [Apple Security Updates](https://support.apple.com/HT201222)

Microsoft supports the installation methods in this document. There may be other third-party methods of installation available from other sources. While those tools and methods may work, Microsoft can't support those methods.

*   [Homebrew Web](https://brew.sh/)
*   [Homebrew GitHub Repository](https://github.com/Homebrew)
*   [Homebrew-Cask](https://github.com/Homebrew/homebrew-cask)
