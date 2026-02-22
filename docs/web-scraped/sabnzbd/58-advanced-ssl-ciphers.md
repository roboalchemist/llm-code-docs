# Source: https://sabnzbd.org/wiki/advanced/ssl-ciphers

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

### [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+SSL+Ciphers&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fssl-ciphers.html%0A%0AImprovement:%0A) SSL Ciphers

## Summary

Setting SSL Ciphers to the following value will lower encryption strength, increase performance (download speed) and is supported by virtually all news servers:

    AES128

NOTE Setting the SSL Cipher with news servers that support TLS 1.3 connections is not (yet) supported by Python and thus SABnzbd. Setting custom ciphers forces the maximum TLS version to 1.2.

Increases in download speed are most notable on systems where CPU power is the limiting factor. Note that some older CPU's might lack AES hardware acceleration and `CHACHA20` might be faster than `AES128`.

## What are SSL ciphers?

When you connect to a news server using SSL/TLS, the firsts step in the connection process is for SABnzbd and the server to agree how the connection will be secured. The SSL/TLS specifications, such as TLSv1.2, define which protocols can and should be used. These protocols define how the security keys will be exchanged and how the actual data will be encrypted. As you can imagine, stronger encryption requires more CPU power to decode.

During the initial stage of the connection, the handshake, SABnzbd and the server will let each other know which protocols they support and then use the strongest available on both. By modifying the SSL Ciphers setting, you can specify what SABnzbd should report as available protocols.

When there are active connections, you can see which protocol is being used for each server in the Status and Interface settings (, Connections). For example: `TLSv1.2 (DHE-RSA-AES128-SHA)`.

## What are the options?

SABnzbd will use the OpenSSL library that's available on your system or that's part of Python.

You can see which ciphers are available on your system by executing `openssl ciphers -v` on the command line. All the strings on the left of the table can be used as an SSL Ciphers setting.

It is also possible to specify multiple single cipher settings or a family of ciphers by specifying it in OpenSSL Cipher format. More information can be found here: <https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html>.

## What are the risks?

Setting your SSL Ciphers to `AES128` will not suddenly expose your traffic to the world. There is evidence that this and similar protocols can be decrypted, but it seems to require a large amount of resources.

It's up to you to decide how valuable your usenet data is. It should also be noted that your internet service provider will always be able to see to which IP-address you are connecting, with or without SSL. Enabling SSL only shields the contents of the connection, not the target.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
