# Source: https://sabnzbd.org/wiki/advanced/ipv6

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

### [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+IPv6&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fipv6.html%0A%0AImprovement:%0A) IPv6

SABnzbd is fully IPv6 enabled: it can download from IPv6 enabled news servers, and you can access SABnzbd's web-interface over IPv6.

### Download from IPv6 enabled news servers

SABnzbd will automatically use IPv6 if available when connecting to news servers. Based on HappyEyeballs, SABnzbd will choose the quickest connection to a newsserver: via IPv4 or via IPv6

### Access SABnzbd's web-interface over IPv6

To access SABnzbd's web-interface over IPv6, you need to fill out `::` in [General](/wiki/configuration/4.5/general) at the field "SABnzbd Host". Press Save Changes, and then restart SABnzbd.
As a first test, you should be able to access SABnzbd via `http://[::1]:8080/`. If that works you can fill out the public IPv6 address of your system running SABnzbd, so something like `http://[2001:dead:beef:cafe:123:4567:b055]:8080/`

### Access SABnzbd over IPv6 from your LAN without login

To access SABnzbd over IPv6 from your LAN without login, you can fill out your IPv6 network prefix in Config -> Special -> local_range, so something like `2001:dead:beef:cafe:` (replace with your actual prefix).

### Access SABnzbd over IPv6 from the outside world

To access SABnzbd over IPv6 from the outside world, you need to configure your router to allow incoming connections on the SABnzbd port (default is 8080) for the local IPv6 addresses.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
