# Install desktop app on Linux

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

This page describes how to install the Mattermost desktop app on Linux.

::::::: {.tab parse-titles=""}
Ubuntu/Debian

Both a `.deb` package (Beta), and an official APT repository is
available for Debian 9 and for Ubuntu releases 20.04 LTS or later.
Automatic app updates are supported and enabled. When a new version of
the desktop app is released, your app updates automatically.

:::: important
::: title
Important
:::

The GPG public key has changed. If you had previously set up the
repository on your system, you\'ll need to [download the new
key](https://deb.packages.mattermost.com/pubkey.gpg). You can set the
`UPDATE_GPG_KEY=yes` environment variable when running the setup script
to configure it to overwrite the previous key on your system with the
new one. The first step of installation then becomes:
`curl -fsS -o- https://deb.packages.mattermost.com/setup-repo.sh | sudo UPDATE_GPG_KEY=yes bash`.
Depending on your setup, additional steps may also be required,
particularly for installations that don\'t rely on the repository setup
script.
::::

1. At the command line, set up the Mattermost repository on your
    system:

> ``` sh
> curl -fsS -o- https://deb.packages.mattermost.com/setup-repo.sh | sudo bash
> ```

1. Install the Mattermost desktop app:

> ``` sh
> sudo apt install mattermost-desktop
> ```

1. Update the Mattermost desktop app:

> ``` sh
> sudo apt upgrade mattermost-desktop
> ```

## Snapcraft Package

A snap is available for systems that have Snapcraft installed. Snapcraft
is installed by default on Ubuntu 16.04 and later, but for most other
Linux distributions you can install it manually. To install Snapcraft,
see [Install snapd](https://snapcraft.io/docs/installing-snapd) on the
Snapcraft website for details.

1. At the command line, execute the following command:

> ``` sh
> sudo snap install mattermost-desktop --beta
> ```

1. Run Mattermost as a desktop app.

:::: tip
::: title
Tip
:::

You can review the current version of your desktop app by selecting the
**More** [\|more-icon-vertical\|](##SUBST##|more-icon-vertical|) icon
located in the top left corner of the desktop app, then selecting **Help
\> Version\...**.
::::
:::::::

::::: {.tab parse-titles=""}
CentOS/RHEL

Beta `.rpm` packages are available for CentOS and RHEL 7 and 8.
Automatic app updates aren\'t supported. You must update your app
manually.

## Install the Mattermost desktop app

1. Download the latest version of the Mattermost desktop app for 64-bit
    systems:
    [mattermost-desktop-6.0.4-linux-x86_64.rpm](https://releases.mattermost.com/desktop/6.0.4/mattermost-desktop-6.0.4-linux-x86_64.rpm)
2. At the command line, execute the following command:

> ``` sh
> sudo rpm -i mattermost-desktop-6.0.4-linux-x86_64.rpm
> ```

1. Run Mattermost as a desktop app.

To manually update the desktop app, run the following command:

> ``` sh
> sudo rpm -u mattermost-desktop-6.0.4-linux-x86_64.rpm
> ```

:::: tip
::: title
Tip
:::

You can review the current version of your desktop app by selecting the
**More** [\|more-icon-vertical\|](##SUBST##|more-icon-vertical|) icon
located in the top left corner of the desktop app, then selecting **Help
\> Version\...**.
::::
:::::

::: {.tab parse-titles=""}
Generic Linux

The Desktop app is available in two formats which are usable on most
Linux distributions: a compressed tarball, and an AppImage binary. Both
can be downloaded from the [Desktop App\'s Github releases
page](https://github.com/mattermost/desktop/releases). Automatic app
updates are supported and enabled on AppImage binary builds. When a new
version of the desktop app is released, your app updates automatically.

For instructions on how to use the AppImage binary, please refer to the
[AppImage Quickstart documentation
page](https://docs.appimage.org/introduction/quickstart.html).

## Install the Desktop App\'s compressed tarball

1. Download the latest version of the Mattermost desktop app for 64-bit
    systems:
    [mattermost-desktop-6.0.4-linux-x64.tar.gz](https://releases.mattermost.com/desktop/6.0.4/mattermost-desktop-6.0.4-linux-x64.tar.gz)
2. Extract the archive to a convenient location, then give
    `chrome-sandbox` in the extracted directory the required ownership
    and permissions:
    `sudo chown root:root chrome-sandbox && sudo chmod 4755 chrome-sandbox`
3. Execute `mattermost-desktop` located inside the extracted directory.
4. To create a Desktop launcher, open the file `README.md`, and follow
    the instructions in the **Desktop launcher** section.
:::
