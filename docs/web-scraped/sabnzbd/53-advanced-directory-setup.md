# Source: https://sabnzbd.org/wiki/advanced/directory-setup

Toggle navigation [![SABnzbd](/images/logo-full.svg)](/)

* [Home](/)
* [Downloads](/downloads)
* Documentation
* [Wiki](/wiki/)
*     * [FAQ](/wiki/faq)
*     * [Quick Setup](/wiki/introduction/quick-setup)
* [Configuration](/wiki/configuration/4.5/configure)
* [Post-processing scripts](/wiki/configuration/4.5/scripts/post-processing-scripts)
* [Extensions](/wiki/extensions-for-sabnzbd)
* [API reference](/wiki/configuration/4.5/api)
* [Forum](https://forums.sabnzbd.org/)
* [Live Chat](/live-chat.html)
* [Donate](/donate)
* [GitHub](https://github.com/sabnzbd/sabnzbd)

![SABnzbd](/images/logo-full.svg)

## Wiki menu  Wiki

[User Manual](/wiki/) [FAQ](/wiki/faq) [Contact](/wiki/contact)

Introduction

* [Quick Setup](/wiki/introduction/quick-setup)
* [Using SABnzbd](/wiki/introduction/usage)
* [NZB Sources](/wiki/introduction/nzb-sources)
* [How To's](/wiki/introduction/howto)
* [Known issues](/wiki/introduction/known-issues)

Installation

* [Windows](/wiki/installation/install-windows)
* [macOS](/wiki/installation/install-macos)
* [Unix](/wiki/installation/install-unix)
* [NAS](/wiki/installation/install-nas)
* [From source](/wiki/installation/install-off-modules)

Configuration

* [Configure](/wiki/configuration/4.5/configure)
* [General](/wiki/configuration/4.5/general)
* [Folders](/wiki/configuration/4.5/folders)
* [Servers](/wiki/configuration/4.5/servers)
* [Categories](/wiki/configuration/4.5/categories)
* [Switches](/wiki/configuration/4.5/switches)
* [Sorting](/wiki/configuration/4.5/sorting)
* [Notifications](/wiki/configuration/4.5/notifications)
* [Scheduling](/wiki/configuration/4.5/scheduling)
* [RSS](/wiki/configuration/4.5/rss)
* [Special Settings](/wiki/configuration/4.5/special)
* [API Reference](/wiki/configuration/4.5/api)

Scripts

* [Pre-queue scripts](/wiki/configuration/4.5/scripts/pre-queue-scripts)
* [Post-processing scripts](/wiki/configuration/4.5/scripts/post-processing-scripts)
* [Notification scripts](/wiki/configuration/4.5/scripts/notification-scripts)

Advanced Topics

* [High-Speed Tweaks](/wiki/advanced/highspeed-downloading)
* [HTTPS for the Web UI](/wiki/advanced/https)
* [Command line options](/wiki/advanced/command-line-parameters)
* [Folder setup](/wiki/advanced/directory-setup)
* [Unix permissions](/wiki/advanced/unix-permissions)
* [RAR with password](/wiki/advanced/password-protected-rars)
* [IPv6](/wiki/advanced/ipv6)
* [SSL/TLS security](/wiki/advanced/certificate-errors)
* [SSL Ciphers](/wiki/advanced/ssl-ciphers)
* [Windows Service](/wiki/advanced/sabnzbd-as-a-windows-service)
* [Android](/wiki/advanced/android)

[Extensions for SABnzbd](/wiki/extensions-for-sabnzbd)

[Special Newshosting offer for SABnzbd users: 70% Off + 3 FREE MONTHS!](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=wt)

### [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Folder+Setup&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fdirectory-setup.html%0A%0AImprovement:%0A) Folder Setup

SABnzbd uses a number of folders for different purposes, some are just for internal administration. Given that some folders can become very large, you may want to relocate them. The following table explains the purpose of each folder, its default location and its keyword in the INI file. All folders can also be changed through the Web-GUI.

The expression `%userprofile%` is for Windows your personal folder in `C:\Users\` which can be directly entered in Run (`WindowsKey+R`). For Posix (Linux) `~` means your home folder.

NOTE The paths of the `log_dir`, `admin_dir` will be relative to the location of the `sabnzbd.ini` file unless a fixed path is set.
The `download_dir`, `complete_dir`, `dirscan_dir` are relative from the current users home directory.

NOTE You can set fixed paths such as `D:\Downloads`, or `/Volumes/nameofdrive/Downloads`. However, the path must be accessible to SABnzbd **when it is launched** otherwise it will be reset to the default path.

* * *

### Configuration file `sabnzbd.ini`

Operating System | Path
---|---
Windows | `%userprofile%\AppData\Local\sabnzbd\sabnzbd.ini`
Posix | `~/.sabnzbd/sabnzbd.ini`
macOS | `~/Library/Application Support/SABnzbd/sabnzbd.ini`

* * *

### Temporary Download Folder `download_dir`

Here SABnzbd collects the data for each download and error correction (par2) is done. When complete, the data is moved to the `complete_dir`. There should be enough space to contain the largest complete job + 10% for error correction data.

Operating System | Path
---|---
Windows | `%userprofile%\Downloads\incomplete
Posix | `~/Downloads/incomplete
macOS | `~/Downloads/incomplete

* * *

### Complete Download Folder `complete_dir`

Here all completed download jobs are stored. Each job is placed in a separate folder, named after the NZB file that started it. You want to put this on a volume with plenty of room.

Operating System | Path
---|---
Windows | `%userprofile%\Downloads\complete`
Posix | `~/Downloads/complete`
macOS | `~/Downloads/complete`

* * *

### Administrative directory `admin_dir`

Used for the internal administration of the job-queue and history.

Operating System | Path
---|---
Windows | `%userprofile%\AppData\Local\sabnzbd\admin`
Posix | `~/.sabnzbd/admin`
macOS | `~/Library/Application Support/SABnzbd/admin`

* * *

### Log directory `log_dir`

Here SABnzbd's logging is stored. Although only needed for troubleshooting, you must have this folder. Growth of this folder is normally limited to 5 MB.

Operating System | Path
---|---
Windows | `%userprofile%\AppData\Local\sabnzbd\logs`
Posix | `~/.sabnzbd/logs`
macOS | `~/Library/Application Support/SABnzbd/logs`

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
