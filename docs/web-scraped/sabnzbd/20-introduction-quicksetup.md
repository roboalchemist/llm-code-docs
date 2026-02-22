# Source: https://sabnzbd.org/wiki/introduction/quick-setup

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

## [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Getting+started&body=%23%23+URL%3A+%2Fwiki%2Fintroduction%2Fquick-setup.html%0A%0AImprovement:%0A) Getting started

## Usenet basics

If you're a beginner with Usenet, you should first find a website explaining the concepts (for example, this [English](http://www.binaries4all.com/beginners/) and [Dutch](http://www.binaries4all.nl) website explains everything in great detail). You should especially find out about how to obtain NZB files that define your downloads. On this Wiki you can find all the information you'll need to setup SABnzbd and customize it. If you experience trouble, please post on our [Forum](https://forums.sabnzbd.org/).

* * *

## Windows & macOS

Download the latest build listed on [our download page](/downloads). For Windows we suggest the installer exe, for macOS we suggest the dmg.

## Ubuntu/Debian via PPA

[Installation guide](/wiki/installation/install-ubuntu-repo).

## Other Unix/Linux distributions

Get the latest Python Source Zip listed on [our download page](/downloads).

* * *

## Installing SABnzbd

## Windows

Run the installer, follow the prompts. When prompted for installation options, decide if you want SABnzbd to launch in the background when you log in, if you want it to be associated with `.nzb` files, and if you want a desktop icon created.

## macOS

Double-click the `.dmg`, drag the `.app` to Applications. You're done!

## Ubuntu Linux

You already installed it via apt. After installing, edit `/etc/default/sabnzbdplus` if you want SABnzbd to run at startup.

* * *

## Upgrading SABnzbd

For all operating systems, to upgrade SABnzbd simply shut down SABnzbd and re-install. In it's a major release (e.g. from 0.7.20 to 1.1.0), it's always better to finish the queue first before updating.

* * *

## The Wizard

After launching SABnzbd for the first time, you'll be presented with our quick-start wizard which will hopefully get you up and running as soon as possible. All settings can be changed later in the various Configuration pages.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)  

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")  
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
