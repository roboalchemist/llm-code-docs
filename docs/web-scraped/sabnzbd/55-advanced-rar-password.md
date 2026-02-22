# Source: https://sabnzbd.org/wiki/advanced/password-protected-rars

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Password-protected+RARs&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fpassword-protected-rars.html%0A%0AImprovement:%0A) Password-protected RARs 

Sometimes you encounter encrypted (or password-protected) RARs. It's only useful to download a password protected post when you know the password upfront. Trying to get a password afterwards is probably a waste of your time and/or money.

SABnzbd will try all available passwords when it detects an encrypted job during the downloading. If none of the passwords work you can set to automatically [Pause or Abort](/wiki/configuration/4.5/switches) the download. 

* * *

## Password per NZB

Supposing you know the required password, you can give it to SABnzbd before the download starts post-processing.  
You can do this like this: 

  * In the NZB file name you can embed the password like this: `My Job {{PW}}.nzb` or `My Job password=PW.nzb`  
This will set the job name to `My Job` and the password to `PW`. 
  * When the job is in the queue, hover over the job and click the    icon.   
At the top of the files list you can set the password.
  * You can also rename the job in the queue.  
`My Job / PASSWORD` will set the password. The `/` is used as a separator because it cannot be part of a folder name.  
The folder name will be `My Job` and `PASSWORD` will be used as the decryption password when unpacking. 

The password can be changed until the job enters the post-processing queue.

## Inside the NZB

Indexers and NZB suppliers can include the password inside the NZB `head` section (see [NZB specification](/wiki/extra/nzb-spec)):
    
    <meta type="password">secret</meta>

Or as the `x-dnzb-password` header when SABnzbd fetches the URL. 

* * *

## Password file

If you don't set a password per job, you can create a text file containing all passwords to be tried.  
It's a simple ASCII text file (created with Notepad, VI or TextEdit) and should contain one password per line. Specify where the file is in [Config->Folders](/wiki/configuration/4.5/folders). 

NOTE Checking passwords is not very fast, the more passwords you list in the file the longer it will take and the more CPU power is lost. Do not list more than ~20 passwords in this file.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
