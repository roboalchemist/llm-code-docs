# Source: https://sabnzbd.org/wiki/advanced/android

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Android&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fandroid.html%0A%0AImprovement:%0A) Android 

# Running SABnzbd on Android

Note: Experimental and advanced  
  
## Basic SABnzbd 2.x

It is possible to run SABnzbd on a plain, standard Android.  
  
  1. On your Android device, install the app UserLAnd from <https://play.google.com/store/apps/details?id=tech.ula>
  2. While setting up UserLAnd, choose Ubuntu, and ssh
  3. Start UserLAnd. On the command line, type "sudo apt-get install sabnzbdplus"
  4. Start sabnzbd with "sabnzbdplus" 
  5. On your Android, now access SABnzbd via <http://127.0.0.1:8080>[  
](http://127.0.0.1:8080)
  6. You can fill out the wizard  

The above will give (at the time of this writing) Ubuntu 18.04 with the older version SABnzbd 2.3.2.   
  
## Update to SABnzbd 3.x

With some extra work, you can update to the current version of SABnzbd:  
  
On the command line of Ubuntu-on-Android, do this:  
  
    sudo apt update -y
    
    sudo apt-get install software-properties-common -y
    
    sudo add-apt-repository ppa:jcfp/ppa -y
    
    sudo apt-get install sabnzbdplus -y

You can start SABnzbd with  
  
    sabnzbdplus

You can access SABnzbd via [http://127.0.0.1:8080](http://127.0.0.1:8080/)  
  
## Share downloads to Android  

There are shared directories between UserLAnd and Android:  
  
For Internal storage:  
UserLAnd: /storage/internal/  
Android app "Files" "internal storage": /Android/data/tech.ula/files/storage  
  
For SDcard (if any)  
UserLAnd: /storage/sdcard/  
Android app "Files" -> "SD Card" -> /Android/data/tech.ula/files/storage  
  
So, in SABnzbd set Complete to /storage/internal/  
  
## Remote access to Ubuntu-on-Android

You can access Ubunt-on-Android via SSH like this:  
  
ssh <ip address of Android device> -p 2022  
  
* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
