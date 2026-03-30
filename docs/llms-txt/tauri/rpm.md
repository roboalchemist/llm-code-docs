# RPM

import ShowSolution from '@components/ShowSolution.astro';
import CommandTabs from '@components/CommandTabs.astro';
import { Steps } from '@astrojs/starlight/components';

:::note
Some sections in this guide are optional. This includes configuring scripts and certain other steps. Feel free to adapt the instructions based on your specific needs and requirements.
:::

This guide covers how to distribute and manage RPM packages, including retrieving package information, configuring scripts, setting dependencies, and signing packages.

:::note

GUI apps on macOS and Linux do not inherit the `$PATH` from your shell dotfiles (`.bashrc`, `.bash_profile`, `.zshrc`, etc). Check out Tauri's [fix-path-env-rs](https://github.com/tauri-apps/fix-path-env-rs) crate to fix this issue.

:::

## Limitations

Core libraries such as glibc frequently break compatibility with older systems. For this reason, you must build your Tauri application using the oldest base system you intend to support. A relatively old system such as Ubuntu 18.04 is more suited than Ubuntu 22.04, as the binary compiled on Ubuntu 22.04 will have a higher requirement of the glibc version, so when running on an older system, you will face a runtime error like `/usr/lib/libc.so.6: version 'GLIBC_2.33' not found`. We recommend using a Docker container or GitHub Actions to build your Tauri application for Linux.

See the issues [tauri-apps/tauri#1355](https://github.com/tauri-apps/tauri/issues/1355) and [rust-lang/rust#57497](https://github.com/rust-lang/rust/issues/57497), in addition to the [AppImage guide](https://docs.appimage.org/reference/best-practices.html#binaries-compiled-on-old-enough-base-system) for more information.

## Configuring the RPM package

Tauri allows you to configure the RPM package by adding scripts, setting dependencies, adding a license, including custom files, and more.
For detailed information about configurable options, please refer to: [RpmConfig](https://v2.tauri.app/reference/config/#rpmconfig).

### Add post, pre-install/remove script to the package

The RPM package manager allows you to run scripts before or after the installation or removal of the package. For example, you can use these scripts to start a service after the package is installed.

Here's an example of how to add these scripts:

1. Create a folder named `scripts` in the `src-tauri` directory in your project.

```bash
mkdir src-tauri/scripts
```

2. Create the script files in the folder.

```bash
touch src-tauri/scripts/postinstall.sh \
touch src-tauri/scripts/preinstall.sh \
touch src-tauri/scripts/preremove.sh \
touch src-tauri/scripts/postremove.sh
```

Now if we look inside `/src-tauri/scripts` we will see:

```bash
ls src-tauri/scripts/
postinstall.sh  postremove.sh  preinstall.sh  preremove.sh
```

3. Add some content to the scripts

```bash title="preinstall.sh"
echo "-------------"
echo "This is pre"
echo "Install Value: $1"
echo "Upgrade Value: $1"
echo "Uninstall Value: $1"
echo "-------------"
```

```bash title="postinstall.sh"
echo "-------------"
echo "This is post"
echo "Install Value: $1"
echo "Upgrade Value: $1"
echo "Uninstall Value: $1"
echo "-------------"
```

```bash title="preremove.sh"
echo "-------------"
echo "This is preun"
echo "Install Value: $1"
echo "Upgrade Value: $1"
echo "Uninstall Value: $1"
echo "-------------"
```

```bash title="postremove.sh"
echo "-------------"
echo "This is postun"
echo "Install Value: $1"
echo "Upgrade Value: $1"
echo "Uninstall Value: $1"
echo "-------------"
```

4. Add the scripts to the`tauri.conf.json` file

```json title="tauri.conf.json"
{
  "bundle": {
    "linux": {
      "rpm": {
        "epoch": 0,
        "files": {},
        "release": "1",
        // add the script here
        "preInstallScript": "/path/to/your/project/src-tauri/scripts/prescript.sh",
        "postInstallScript": "/path/to/your/project/src-tauri/scripts/postscript.sh",
        "preRemoveScript": "/path/to/your/project/src-tauri/scripts/prescript.sh",
        "postRemoveScript": "/path/to/your/project/src-tauri/scripts/postscript.sh"
      }
    }
  }
}
```

### Setting the Conflict, Provides, Depends, Files, Obsoletes, DesktopTemplate, and Epoch

- **conflict**: Prevents the installation of the package if it conflicts with another package.
  For example, if you update an RPM package that your app depends on and the new version is incompatible with your app.

- **provides**: Lists the RPM dependencies that your application provides.

- **depends**: Lists the RPM dependencies that your application needs to run.

- **files**: Specifies which files to include in the package.

- **obsoletes**: Lists the RPM dependencies that your application obsoletes.

:::note
If this package is installed, packages listed as "obsoletes" will be automatically removed if present.
:::

- **desktopTemplate**: Adds a custom desktop file to the package.

- **epoch**: Defines weighted dependencies based on version numbers.

:::caution
It is not recommended to use epoch unless necessary, as it alters how the package manager compares package versions.
For more information about epoch, please check: [RPM Packaging Guide](https://rpm-packaging-guide.github.io/#epoch-scriptlets-and-triggers).
:::

To use these options, add the following to your `tauri.conf.json` :

```json title="tauri.conf.json"
{
  "bundle": {
    "linux": {
      "rpm": {
        "postRemoveScript": "/path/to/your/project/src-tauri/scripts/postscript.sh",
        "conflicts": ["oldLib.rpm"],
        "depends": ["newLib.rpm"],
        "obsoletes": ["veryoldLib.rpm"],
        "provides": ["coolLib.rpm"],
        "desktopTemplate": "/path/to/your/project/src-tauri/desktop-template.desktop"
      }
    }
  }
}
```

### Add a license to the package

To add a license to the package, add the following to the `src-tauri/cargo.toml` or in the `src-tauri/tauri.conf.json` file:

```toml title="src-tauri/cargo.toml"
[package]
name = "tauri-app"
version = "0.0.0"
description = "A Tauri App"
authors = ["you"]
edition = "2021"
license = "MIT" # add the license here