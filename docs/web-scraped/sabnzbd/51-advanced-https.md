# Source: https://sabnzbd.org/wiki/advanced/https

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

### [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Webserver+using+HTTPS&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fhttps.html%0A%0AImprovement:%0A) Webserver using HTTPS

To make the communication between SABnzbd and your web browser private, you can enable HTTPS (secured HTTP). The purpose of a certificate is two-fold; one is to give you encrypted communication, the other is to authenticate the server. The certificate authority guarantees that you are actually talking to the website of your bank or similar service. Web browsers are very fussy about the authentication part, and by default will complain unless you buy your own certificate.

By default SABnzbd will create self signed certificates for you to use. These however will give browser warnings when you try to connect however it is usually easy to make an exception for these certificates.

The default key and certs are located inside your admin folder of the folder where your sabnzbd.ini is. For example:

    Windows:
    %localappdata%/sabnzbd/admin/server.cert
    %localappdata%/sabnzbd/admin/server.key
    Linux:
    ~/.sabnzbd/admin/server.cert
    ~/.sabnzbd/admin/server.key

You can change the location of these files by entering the full path to both in [Config->General](/wiki/configuration/4.5/general).

If you want trouble-free communication you need to buy a certificate from one of the many Certificate Authorities, for example from Verisign or Let’s Encrypt (see below).
Be warned that certificates come with different capabilities and hence, different prices. You probably only need a basic certificate, but even these are expensive not worth the price for just accessing SABnzbd.

To turn on access using HTTPS, you need enable HTTPS in [Config->General](/wiki/configuration/4.5/general#toc1). This will enable HTTPS on the main listening port. If you want it to listen on a different port specific for HTTPS, you can specify this by clicking on Advanced.

NOTE If you upgraded from an older version of SABnzbd, the HTTPS port (under Advanced) might be set to `9090`. Set it to empty to enable HTTPS on the main port.

If you expose SABnzbd to the Internet you can use `443` as port number, as this is the official number for HTTPS and allows you to not specify the port when accessing. Please note using a port number below 1024 requires running as root under linux.

## Creating a valid certificate using Let’s Encrypt

If you run SABnzbd behind an Apache proxy, you can create free valid certificates using Let's Encrypt.
[A guide is available on the forums.](https://forums.sabnzbd.org/viewtopic.php?f=1&t=19684)

## Create a self-signed certificate with OpenSSL

From a command prompt type:

    openssl genrsa 1024 > host.key
    openssl req -new -x509 -nodes -sha1 -days 365 -key host.key > host.cert

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
