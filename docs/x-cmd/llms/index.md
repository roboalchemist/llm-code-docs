# Source: https://www.x-cmd.com/start/index.md

---
url: /start/index.md
---

# Installation Guide

This guide outlines how to install, update, and uninstall x-cmd on various shell environments and operating systems.

x-cmd is a command-line library/toolbox developed using Posix Shell compatible syntax, prioritizing flexibility and lightweight design. To minimize system impact, x-cmd core operations only rely on pre-installed system commands and operate solely within the user directory. Therefore, installation and most usage scenarios do not require root privileges.

Differences exist between different systems and shells. Thanks to user feedback and support, x-cmd has provided corresponding solutions for these differences. This document summarizes these solutions and provides links to relevant documentation.

After successful installation, welcome to read our [Getting Started Guide](/start/get-started.md) ~ This guide will help you quickly master the core functions of x-cmd, including auto-completion, theme customization, module management, and package management, to help you get started quickly.

## Installation using Posix Shell Script

The most convenient installation method is to use the installation script provided by x-cmd, which is hosted at [https://get.x-cmd.com](https://github.com/x-cmd/get/blob/main/index.html).

This script is written using Posix Shell compatible syntax. Users can download it using `curl` or `wget` and run it directly in **bash, zsh, dash, ash**.

::::ul
:::li Using `curl` command
```sh
eval "$(curl https://get.x-cmd.com)"
```
:::
:::li Using `wget` command
```sh
eval "$(wget -O- https://get.x-cmd.com)"
```
:::
::::

<Terminal
   demo="/start/install-cmd-curl.en.json,/start/install-cmd-wget.en.json"
   btn="curl,wget"
   name="curl,wget"
   desc="curl command installation, wget command installation"
   size="large"
/>

## Installing x-cmd in Fish, Elvish, Nushell, xonsh, tcsh

Because the installation script is written using POSIX shell syntax, it cannot be run directly in non-POSIX shell environments (such as fish, elvish, nushell, xonsh, tcsh). Therefore, please use the following command:

```bash
curl https://get.x-cmd.com | sh
```

Or

```bash
wget -O- https://get.x-cmd.com | sh
```

After installation, to automatically load x-cmd when the shell starts, we provide a quick configuration command like `x <shell-name> --setup`.

For example, with [fish](/start/fish.md):

```bash
~/.x-cmd.root/bin/x-cmd fish --setup
```

We have prepared special documentation for users of the following shells to further improve the onboarding experience:

- [fish](/start/fish.md)
- [elvish](/start/elvish.md)
- [nushell](/start/nushell.md)
- [xonsh](/start/xonsh.md)
- [tcsh](/start/tcsh.md)

## Installing x-cmd on Windows and Powershell

We provide a [x-cmd.bat](https://get.x-cmd.com/x-cmd.bat) batch script for download. Users only need to double-click to open it to trigger the installation.

At the same time, x-cmd also provides an installation script written in Powershell. Users can call the following command in powershell to download the script and trigger the installation.

```powershell
[System.Text.Encoding]::GetEncoding("utf-8").GetString($(Invoke-WebRequest -Uri "https://get.x-cmd.com/x-cmd.ps1").RawContentStream.ToArray()) | Invoke-Expression
```

Please go to [Windows Installation](/start/windows.md), this document provides a detailed introduction, precautions, and principle explanation for Windows systems.

Powershell users can also directly access the [Powershell dedicated document](/start/powershell.md)

## Install via System Package Managers

### Homebrew

[![Homebrew Version](https://img.shields.io/homebrew/v/x-cmd?logo=homebrew&style=flat&colorA=18181B&colorB=107fbc&label=Homebrew)](https://formulae.brew.sh/formula/x-cmd)

::::ol
:::li Run the command to install
```sh
brew install x-cmd
```
:::
:::li After the installation, we need to activate it within your current user environment. <sup><Link href="/start/system-installation#currently-supported-system-package-managers"><i class="i-carbon:information-filled" /></Link></sup>
```sh
x-cmd
```
:::
::::

### AUR

[![Arch AUR Version](https://img.shields.io/aur/version/x-cmd?logo=archlinux&style=flat&colorA=18181B&colorB=107fbc&label=AUR)](https://aur.archlinux.org/packages/x-cmd)

::::ol
:::li Run the command to install
```sh
sudo yay -S x-cmd
# or
sudo paru -S x-cmd
```
:::
:::li After the installation, we need to activate it within your current user environment. <sup><Link href="/start/system-installation#currently-supported-system-package-managers"><i class="i-carbon:information-filled" /></Link></sup>
```sh
x-cmd
```
:::
::::

### apt

Currently awaiting community review.

Related discussions: [Debian](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1099644), [Kali](https://bugs.kali.org/view.php?id=9101)

### apk

Currently awaiting community review.

Related discussion: [Alpine MR #80866](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/80866)

### pacman

Currently awaiting community review.

Related page: [Arch AUR](https://aur.archlinux.org/packages/x-cmd)

### dnf

Currently awaiting community review.

Related discussion: [Red Hat Bugzilla #2351807](https://bugzilla.redhat.com/show_bug.cgi?id=2351807)

## Other Installation Methods: Docker Container, SSH Remote Installation

### Package Manager (Planned)

We have submitted x-cmd to system package managers like `brew`, `apt`, `apk`; it is estimated to be available soon.

### Docker Container

In a minimalist Linux container environment without pre-installed `curl` or `wget`, you can use the following command to quickly install x-cmd:

```bash
x docker run -x -it <container name or id>
```

```bash
x docker setup <container name or id>
```

- For the `x docker` command, please refer to the [`x-cmd` Docker module documentation](/mod/docker.md).

### Installing x-cmd on a remote host via SSH

The basic principle is to use scp to transfer the x-cmd all-in-one installation package to the user directory of the remote server and trigger decompression and automatic configuration.

## Updating x-cmd: `x upgrade`

Updating x-cmd is very simple; just run the `x upgrade` command.

Or run the installation script again:

```bash
eval "$(curl https://get.x-cmd.com)"
```

:::info Note:
- The upgrade process will not delete older versions of x-cmd, nor will it affect other open shell environments.
- For a more detailed explanation and principle analysis, please refer to the [relevant documentation](/start/upgrade.md).
:::

## Uninstalling x-cmd

Uninstalling x-cmd is very simple; just run the following command:

```bash
x uninstall self
```

This will delete the `~/.x-cmd.root` directory and clear the x-cmd loading command from the shell configuration file (such as `~/.bashrc`).

:::info Note:
- Before uninstalling, ensure that no active processes are calling x-cmd.
- For a more detailed explanation and principle analysis, please refer to the [relevant documentation](/start/uninstall.md).
:::
