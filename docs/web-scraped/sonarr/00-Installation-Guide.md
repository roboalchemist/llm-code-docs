Toggle navigation ![Image](img/logo.png)Sonarr

* __HOME
* __FEATURES
* __DOWNLOAD
* __SUPPORT
* [__DONATE](/donate)
* [__GITHUB](https://github.com/Sonarr/Sonarr)

![Image](img/slider/seriesdetails.png)

## Sonarr is an internet PVR for Usenet and Torrents.

## Notifications and fully customizable quality profiles.

![Image](img/slider/qualityprofile.png) ![Image](img/slider/notifications.png)
![Image](img/slider/posters.png) ![Image](img/slider/table.png)
![Image](img/slider/overview.png)

## Multiple Series views.

![Image](img/slider/updates2.png) ![Image](img/slider/updates.png)

## Built-in updater. See what's new without leaving the comfort of the app.

Sonarr is an internet PVR for Usenet and Torrents.

### Features

![Image](img/features/calendar.png)

### __Calendar

See all your upcoming episodes in one convenient location.

![Image](img/features/manualsearch.png)

### __Manual Search

Find all the releases, choose the one you want and send it right to your
download client.

![Image](img/features/blocklist.png)

### __Automatic Failed Download Handling

Sonarr makes failed downloads a thing of the past. Password protected
releases, missing repair blocks or virtually any other reason? no worries.
Sonarr will automatically block the release and try another one until it finds
one that works.

### Download Sonarr

* __Windows
* __Linux
* __macOS
* __NAS
* __Docker
* __   Others

Package maintainers: [Team Sonarr](https://github.com/sonarr/sonarr)

Introduction

Sonarr is supported natively on Windows. Sonarr can be installed as Windows
Service or System Tray Application.

A Windows Service runs even when the user is not logged in, but special care
must be taken since Windows Services cannot access network drives (`X:\`
mapped drives or `\\server\share` UNC paths) without special configuration
steps.
Additionally the Windows Service runs under the **Local Service** account, by
default this account does not have permissions to access your user's home
directory unless permissions have been assigned manually. This is particularly
relevant when using download clients that are configured to download to your
home directory.
It's therefore advisable to install Sonarr as a System Tray Application if the
user can remain logged in. The option to do so is provided during the
installer.

Sonarr is supported on Windows 8.1 and Server 2012 or later. Pre-release or
earlier versions of Windows are not supported.

#### Updating Sonarr v3 to v4 (macOS)

Sonarr will automatically convert an existing Sonarr installation. It's
advisable to make a backup of the v3 data first.

1Install Sonarr

Download the Windows Installer with the following link and execute it.

[Download Windows (x64)
Installer](//services.sonarr.tv/v1/download/main/latest?version=4&os=windows&arch=x64&installer=true)

[Download Windows (x86)
Installer](//services.sonarr.tv/v1/download/main/latest?version=4&os=windows&arch=x86&installer=true)

2View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Alternatives for advanced users

##### Manual Install (macOS)

It is possible to install Sonarr manually using the [Windows
x64](//services.sonarr.tv/v1/download/main/latest?version=4&os=windows&arch=x64)
or [Windows
x86](//services.sonarr.tv/v1/download/main/latest?version=4&os=windows&arch=x86)
.zip downloads. However in that case you must manually deal with dependencies,
installation and permissions.

* ![Image](logo/debian.svg) Debian
* __  Ubuntu
* ![Image](logo/archlinux.svg) ArchLinux
* ![Image](logo/gentoo.svg) Gentoo
* __  FreeBSD
* __   Others

Package maintainers: [Team Sonarr](https://github.com/sonarr/sonarr)

Introduction

The installation process described here utilizes an installation shell script.
The script will configure the required systemd unit to auto-start Sonarr.
It'll deploy the binaries in `/opt/Sonarr` and the configuation data will be
stored in `/var/lib/sonarr`.

#### Updating Sonarr v3 to v4 (Debian/Ubuntu)

The Sonarr v4 package overwrites v3's systemd unit if present. It's advisable
to make a backup of the v3 data first and uninstall the previous `sonarr`
package.

1Install Sonarr

Run one of the below commands as **root**.

During the installation, you will be asked which user and group Sonarr must
run as. It's important to choose these correctly to avoid permission issues
with your media files. We suggest you keep at least the group name identical
between your download client(s) and Sonarr.
If you need to correct these after installation, please re-run the
installation script.

##### curl (Debian/Ubuntu)

    curl -o install-sonarr.sh https://raw.githubusercontent.com/Sonarr/Sonarr/develop/distribution/debian/install.sh
    sudo bash install-sonarr.sh

##### wget (Debian/Ubuntu)

    wget -qO install-sonarr.sh https://raw.githubusercontent.com/Sonarr/Sonarr/develop/distribution/debian/install.sh
    sudo bash install-sonarr.sh

2View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Replace 'localhost' with your server IP if you're connecting remotely

Alternatives for advanced users

##### Manual Install (Debian/Ubuntu)

It is possible to install Sonarr manally using a `.tar.gz` download. However
in that case you must manually deal with dependencies, installation and
permissions. You will need to download the correct package for your system.

ARM (ARM, armf, and armhf)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=arm

ARM64 (arm64)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=arm64

AMD64 (x64) (amd64)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=x64

##### Docker container (Debian/Ubuntu)

You can follow the Docker guide to install Sonarr as a Docker container
instead.

Package maintainers: [Team Sonarr](https://github.com/sonarr/sonarr)

Introduction

The installation process described here utilizes an installation shell script.
The script will configure the required systemd unit to auto-start Sonarr.
It'll deploy the binaries in `/opt/Sonarr` and the configuation data will be
stored in `/var/lib/sonarr`.

#### Updating Sonarr v3 to v4 (Docker)

The Sonarr v4 package overwrites v3's systemd unit if present. It's advisable
to make a backup of the v3 data first and uninstall the previous `sonarr`
package.

1Install Sonarr

Run one of the below commands as **root**.

During the installation, you will be asked which user and group Sonarr must
run as. It's important to choose these correctly to avoid permission issues
with your media files. We suggest you keep at least the group name identical
between your download client(s) and Sonarr.
If you need to correct these after installation, please re-run the
installation script.

##### curl

    curl -o install-sonarr.sh https://raw.githubusercontent.com/Sonarr/Sonarr/develop/distribution/debian/install.sh
    sudo bash install-sonarr.sh

##### wget

    wget -qO install-sonarr.sh https://raw.githubusercontent.com/Sonarr/Sonarr/develop/distribution/debian/install.sh
    sudo bash install-sonarr.sh

2View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Replace 'localhost' with your server IP if you're connecting remotely

Alternatives for advanced users

##### Manual Install (Docker)

It is possible to install Sonarr manally using a `.tar.gz` download. However
in that case you must manually deal with dependencies, installation and
permissions. You will need to download the correct package for your system.

ARM (ARM, armf, and armhf)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=arm

ARM64 (arm64)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=arm64

AMD64 (x64) (amd64)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=x64

##### Docker container

You can follow the Docker guide to install Sonarr as a Docker container
instead.

Package maintainers: [fryfrog,
txtsd](https://aur.archlinux.org/packages/sonarr-bin/)

Introduction

The Arch Linux User Repository offers [sonarr-
bin](https://aur.archlinux.org/packages/sonarr-bin/) package that can be
installed manually or using your favorite [AUR
helper](https://wiki.archlinux.org/index.php/AUR_helpers).

#### Updating Sonarr v3 to v4 (Docker) (2)

Sonarr will convert an existing Sonarr database if found during startup. Of
course, it is always advisable to make a backup first.

1Install Sonarr

An AUR helper can install Sonarr and its dependencies easily, or follow the
[AUR Installing
Packages](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages)
wiki for manual installation.

For example, to use [paru](https://aur.archlinux.org/packages/paru) to install
the Sonarr package:

    paru -S sonarr-bin

2Start Sonarr

    sudo systemctl daemon-reload
    sudo systemctl enable --now sonarr

3View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Replace 'localhost' with your server IP if you're connecting remotely

Alternatives for advanced users

##### Manual Install (Docker) (2)

It is possible to install Sonarr manually from upstream using the [.tar.gz
download](//services.sonarr.tv/v1/download/main/latest?version=4&os=linux).
However in that case you must manually deal with dependencies, installation
and permissions.

##### Docker container (2)

You can follow the Docker guide to install Sonarr as a Docker container
instead.

Package maintainers: [xartin](https://github.com/xartin),
[candrews](https://github.com/candrews)

Introduction

[Gentoo Linux includes sonarr](https://packages.gentoo.org/packages/www-
apps/sonarr) so it can be installed using Gentoo portage.

1Install Sonarr

    emerge www-apps/sonarr

2Start Sonarr

    systemctl daemon-reload
    systemctl enable --now sonarr

3View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Replace 'localhost' with your server IP if you're connecting remotely

Alternatives for advanced users

##### Manual Install (Docker) (3)

It is possible to install Sonarr manually from upstream using the [.tar.gz
download](//services.sonarr.tv/v1/download/main/latest?version=4&os=linux).
However in that case you must manually deal with dependencies, installation
and permissions.

##### Docker container (3)

You can follow the Docker guide to install Sonarr as a Docker container
instead.

Package maintainers:
[mvanbaak](https://cgit.freebsd.org/ports/tree/net-p2p/sonarr)

Introduction

Sonarr can be installed using the FreeBSD Sonarr
[Port](https://cgit.freebsd.org/ports/tree/net-p2p/sonarr).

1Install Sonarr

Install the port with:

    pkg install sonarr

2Start Sonarr

Start the service:

    sysrc sonarr_enable=YES
    service sonarr start

3View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Replace 'localhost' with your server IP if you're connecting remotely

Alternatives for advanced users

##### Manual Install (Docker) (4)

It is possible to install Sonarr manually from upstream using the [.tar.gz
download](//services.sonarr.tv/v1/download/main/latest?version=4&os=linux).
However in that case you must manually deal with dependencies, installation
and permissions.

##### Docker container (4)

You can follow the Docker guide to install Sonarr as a Docker container
instead.

Please contact us if you wish to port Sonarr v4 for any other distribution
that the ones already listed.

A generic download is available for linux, but dependencies, installation and
permissions will need to be done manually.

ARM (ARM, armf, and armhf)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=arm

ARM64 (arm64)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=arm64

AMD64 (x64) (amd64)

    https://services.sonarr.tv/v1/download/main/latest?version=4&os;=linux&arch;=x64

Package maintainers: [Team Sonarr](https://github.com/sonarr/sonarr)

Introduction

The easiest way to install Sonarr on macOS is to use the App archive with the
steps described below.

#### Updating Sonarr v3 to v4 (Docker) (3)

Sonarr will convert an existing Sonarr database if found during startup. Of
course, it is always advisable to make a backup first.

1Download App package

[Download macOS App
(ARM)](//services.sonarr.tv/v1/download/main/latest?version=4&os=macos&arch=arm64&installer=true)

[Download macOS App
(Intel)](//services.sonarr.tv/v1/download/main/latest?version=4&os=macos&arch=x64&installer=true)

2Install App

Open the archive and drag the Sonarr icon to your Application folder.

In macOS 10.12+ Gatekeeper App Translocation will prevent Sonarr from updating
if it's being run directly from the download location. Therefore it MUST be
moved to the Application folder.

3Self-sign Sonarr

Open Terminal and run

    codesign --force --deep -s - /Applications/Sonarr.app && xattr -rd com.apple.quarantine /Applications/Sonarr.app

4Start Sonarr

Open Sonarr.app in your Application folder.

5View Sonarr

Browse to `http://localhost:8989` to start using Sonarr.

Alternatives for advanced users

##### Manual Install (Docker) (5)

It is possible to install Sonarr manually using the [macOS
ARM](//services.sonarr.tv/v1/download/main/latest?version=4&os=macos&arch=arm64)
or [macOS
Intel](//services.sonarr.tv/v1/download/main/latest?version=4&os=macos&arch=x64)
.tar.gz downloads. However in that case you must manually deal with
dependencies, installation and permissions.

##### Docker container (5)

You can follow the Docker guide to install Sonarr as a Docker container
instead.

* Synology
* QNAP
* __   Others

A Sonarr package is maintained by [SynoCommunity](https://synocommunity.com/)
Please contact us if you wish to include the appropriate install instructions
on this page.

The Sonarr Qnap port is being maintained by the qnap forum community.
Please contact us if you wish to include the appropriate install instructions
on this page.

Please contact us if you wish to port Sonarr for any other NAS that the ones
already listed.

A generic download is available for linux, but dependencies, installation and
permissions will need to be done manually.

[Download Linux
.tar.gz](//services.sonarr.tv/v1/download/main/latest?version=4&os=linux)

Package maintainers: [linuxserver](https://www.linuxserver.io),
[hotio](https://hotio.dev)

Introduction

The Sonarr team does not offer an official Docker image. However, a number of
third parties have created and maintain their own.
These instructions provide generic guidance that should apply to any Sonarr
Docker image.

#### Updating Sonarr v3 to v4 (Docker) (4)

Most docker containers use `/config` volume to mount the data directory and
supply that path to Sonarr as parameter. Sonarr will convert the given
directory on startup if an existing database is found. Of course, it is always
advisable to make a backup first.

1Avoid common pitfalls

##### Volumes and Paths

There are two common problems with Docker volumes: Paths that differ between
the Sonarr and download client container and paths that prevent fast moves and
hard links.
The first is a problem because the download client will report a download's
path as `/torrents/My.Show.S01E01/`, but in the Sonarr container that might be
at `/downloads/My.Show.S01E01/`. The second is a performance issue and causes
problems for seeding torrents. Both problems can be solved with well planned,
consistent paths.

Most Docker images suggest paths like `/tv` and `/downloads`. This causes slow
moves and doesn't allow hard links because they are considered two different
file systems _inside_ the container. Some also recommend paths for the
download client container that are different from the Sonarr container, like
`/torrents`.
The best solution is to use a single, common volume _inside_ the containers,
such as `/data`. Your Series would be in `/data/tv`, torrents in
`/data/downloads/torrents` and/or usenet downloads in
`/data/downloads/usenet`.

If this advice is not followed, you may have to configure a Remote Path
Mapping in the Sonarr web UI (Settings › Download Clients).

##### Ownership and Permissions

Permissions and ownership of files is one of the most common problems for
Sonarr users, both inside and outside Docker. Most images have environment
variables that can be used to override the default user, group and umask, you
should decide this before setting up all of your containers. The
recommendation is to use a common group for all related containers so that
each container can use the shared group permissions to read and write files on
the mounted volumes.
Keep in mind that Sonarr will need read and write to the download folders as
well as the final folders.

_For a more detailed explanation of these issues, see[The Best Docker Setup
and Docker Guide](https://wiki.servarr.com/docker-guide) wiki article._

2Install Sonarr

To install and use these Docker images, you'll need to keep the above in mind
while following their documentation. There are many ways to manage Docker
images and containers too, so installation and maintenance of them will depend
on the route you choose.

* ##### [ghcr.io/hotio/sonarr:release](https://ghcr.io/hotio/sonarr:latest)

[hotio](https://hotio.dev) doesn't specify any default volumes, besides
`/config`. Images are automatically updated multiple times per hour if
upstream changes are found. Read the
[instructions](https://hotio.dev/containers/sonarr) on how to install the
image.

* ##### [ghcr.io/linuxserver/sonarr:latest](https://ghcr.io/linuxserver/sonarr:latest)

[linuxserver.io](https://www.linuxserver.io) is one of the most prolific and
popular Docker image maintainers. They also maintain images for most of the
popular download clients as well. LinuxServer specifies a couple of optional
default volumes such as `/tv` and `/downloads`. The default volumes are not
optimal nor recommended. Our recommendation is to use a single volume for the
data, as mentioned above.

Please contact us if you wish to port Sonarr for any other platform than the
ones already listed.

### Support

[__Forums Talk to Sonarr developers and other users, we are here to help.](https://forums.sonarr.tv) [__Wiki Check out the FAQ, API documentation and
other guides](https://wiki.sonarr.tv) [__IRC Channel Join our IRC channel
for a chat. irc.libera.chat #sonarr](https://web.libera.chat/?channels=#sonarr) [__Discord Join our Discord
server for a chat.](https://discord.sonarr.tv)

[__GitHub Issues Track bugs and features for the things that matter to you.](https://github.com/Sonarr/Sonarr/issues) [__Follow us on Twitter News,
updates and anything else that might come up.](https://twitter.com/sonarrtv)
[__Sonarr subreddit Discuss Sonarr and talk to other users.](https://www.reddit.com/r/sonarr)

©  Sonarr. All rights reserved.
