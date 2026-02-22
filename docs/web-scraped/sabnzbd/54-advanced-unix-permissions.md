# Source: https://sabnzbd.org/wiki/advanced/unix-permissions

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

#  Wiki menu  Wiki 

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Unix+Permissions&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Funix-permissions.html%0A%0AImprovement:%0A) Unix Permissions 

_Linux, Unix, macOS only_

When SABnzbd runs on a Unix-like server, the download result must often be made available for other users.  
Normally files that are created by a user account are private. This is also true for the files created by SABnzbd.  
This is OK for the internal administration files, but not always for the downloaded files. 

In [Config->Folders](/wiki/configuration/4.5/folders) you can specify which access rights SABnzbd should give the end result.  
This parameter is passed to the [chmod](http://en.wikipedia.org/wiki/Chmod) command. It uses the octal notation supported by `chmod`.  
You need to specify the settings for _folders_ , so with the X bits set, SABnzbd will automatically remove any X bits for all files. 

Typical values:  
`0777` | full access for everyone  
---|---  
`0700` | only private access  
`0755` | private read/write access, others only read access  
`0750` | private read/write access, group read access, others no access  
  
You can set the permissions in [Config->Folders](/wiki/configuration/4.5/folders).

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
