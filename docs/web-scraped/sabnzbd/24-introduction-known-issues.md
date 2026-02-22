# Source: https://sabnzbd.org/wiki/introduction/known-issues

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

[ ![Special Newshosting offer for SABnzbd users](/images/specials/nh_corner.png) ](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=wc1)

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Known+issues&body=%23%23+URL%3A+%2Fwiki%2Fintroduction%2Fknown-issues.html%0A%0AImprovement:%0A) Known issues 

These are known issues regarding the working of SABnzbd in its environment.  
They are not registered as bugs of SABnzbd, because we cannot solve them.  
It's more an incompatibility with other systems or outright bugs in these other systems. 

  * Size limit
  * Hangup of post-processing
  * Unreliable Usenet servers
  * macOS and foreign characters
  * Linux and foreign characters
  * Files remain in Watched Folder
  * Blocked email
  * Mounting external drives and network shares

## Size limit

To prevent unexpectedly large NZBs from eating your quotum you can set the option "size_limit" in ["Config->Special"](/wiki/configuration/4.5/special).  
Any NZB larger than this size will be set to paused and get a low priority. 

## Hangup of post-processing

When PAR2 or UNRAR hang up, you should never just stop SABnzbd.  
Instead use your operating system's task manager to stop the Par2 or UNRAR program.  
Forcing SABnzbd to quit may damage your queues.  

## Unreliable Usenet servers

Some Usenet servers have intermittent login (or other) problems.  
For these, the server blocking method is not very favorable.  
There is an ["Special" option](/wiki/configuration/4.5/special) "no_penalties" which, when set to 1, will limit blocks to 1 minute  
(No, 2 doesn't mean 2 minutes). 

## macOS and foreign characters

On macOS you may encounter downloaded files with foreign characters (e.g. é and ä).  
The par2 repair may fail when the files were created on a Windows system.  
The problem is caused by the PAR2 utility and we cannot fix this now.  
This does not apply to files inside RAR files. 

## Linux and foreign characters

On Linux when you download files they may have the wrong character encoding.  
You will see this only when downloaded files contain accented characters.  
You need to fix it yourself by running the **convmv** utility (available for most Linux platforms). 

## Files remain in Watched Folder

The "Watched Folder" sometimes fails to delete the NZB files it has processed.  
This happens when other software still accesses these files.  
Some third-party utilities supporting SABnzbd are known to do this.  
We cannot solve this problem, because the Operating System (read Windows) prevents the removal.  
SABnzbd does try about 10 times with 5 second intervals, but after that it gives up.  
The NZB will not be processed again, unless changed or overwritten. 

## Blocked email

When SABnzbd cannot send notification emails, check your virus scanner, firewall or security suite.  
It may be blocking outgoing email. 

## Mounting external drives and network shares

When you are using external drives or network shares on macOS or Linux make sure that the drives are mounted.  
The operating system will simply redirect your files to alternative locations.  
You may have trouble finding the files when mounting the drive later. 

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
