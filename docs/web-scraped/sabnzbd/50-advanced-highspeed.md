# Diagnosing speed limitations

Source: https://sabnzbd.org/wiki/advanced/highspeed-downloading

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

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_corner.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=wc1)

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

### [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+High+speed+Downloading&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fhighspeed-downloading.html%0A%0AImprovement:%0A) High speed Downloading

If you have a fast Internet connection (60MB/s aka 500 Mbps, and over) and are not getting the full speeds you require, there are a few steps that you can take to diagnose what is causing the limitation.

Open the Status window (  ), run the tests (  ) and check the following:

![Diagnostics](/images/wiki/highspeed-downloading.png)

  1. Is the speed listed as **Internet Bandwidth** near your expected bandwidth?
If not, make sure the network connection to your device is working correctly.
Test your device’s speed via [fast.com](https://fast.com/).
  2. Is the **Pystone** score at least 100.000 or above?
If the score is lower than this, the CPU in your device is either too slow or something else is preventing SABnzbd from using its power.
  3. Is the **Folder Speed** at least 150MB/s?
Both Incomplete and Complete should be on a SSD/M.2/NVMe disk.
  4. Download the **10GB test download** , is the speed higher than on regular downloads?
  5. After this, do you see **Download speed limited by** Disk Speed in the Status Window?
If so, either your disk are too slow or something is preventing SABnzbd from writing fast to your disks.

NOTE When you seek support on our forums/Discord/Reddit, please make sure that you have used the diagnostics above and report the results.

## Optimizations

* Make sure `Maximum line speed` in [Config->General](/wiki/configuration/4.5/general) is set to the correct value for your connection.
* Try different connection numbers for your servers. Start with 8 and increase from there. A higher number will increase the overhead so more connections might actually reduce your speed.
* Increase `Articles per request` in [Config->Servers](/wiki/configuration/4.5/servers) (Advanced settings). The default is `1` (disabled), but increasing to `2-10` can improve speed if your server supports it. See [NNTP Pipelining](/wiki/advanced/nntp-pipelining) for more information.
* Turn Off `Direct Unpack` in [Config->Switches](/wiki/configuration/4.5/switches) to reduce disk load.
* Turn On `Pause Downloading During Post-Processing` in [Config->Switches](/wiki/configuration/4.5/switches). This will reduce disk load, as downloading and post-processing are not performed simultaneously.
* Change [SSL Ciphers](/wiki/advanced/ssl-ciphers) to `AES128` or `CHACHA20` in [Config->Servers](/wiki/configuration/4.5/servers). This can slightly reduce CPU load.
* Turn off `Unwanted Extensions` and `Action when encrypted RAR is downloaded`, as these use a substantial amount of disk and CPU power.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
