# Source: https://sabnzbd.org/wiki/installation/install-macos

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Install+SABnzbd+for+macOS&body=%23%23+URL%3A+%2Fwiki%2Finstallation%2Finstall-macos.html%0A%0AImprovement:%0A) Install SABnzbd for macOS 

## The official App

If you just want to use SABnzbd, we provide a packaged application (64bit-only) available [here](/downloads).   
Pick the right folder for your macOS version and drag SABnzbd to the Applications folder.

* * *

## How to run from sources on macOS

Running the source python (.py) files on a macOS system is not recommended unless you want to try the latest GitHub copy, or make changes yourself. 

  1. Get a local copy (clone) of the SABnzbd source by running in the Terminal: 
         
         git clone -b master https://github.com/sabnzbd/sabnzbd.git
         cd sabnzbd

  2. Install the dependencies by running (might require Xcode):  

         python3 -m pip install -U -r requirements.txt

  3. Start SABnzbd by running:  

         python3 SABnzbd.py

Your default web browser should now start and show the user interface of SABnzbd.

To update the source files to the latest version, open Terminal and run: 
    
    cd sabnzbd
    git pull

* * *

## Running from Terminal

Since the "-d" option of SABnzbd is not working under Leopard, we need to create a daemon environment. This can easily be done by running the command in _screen_. This also adds running at a low priority so that it will affect system performance less. The final command looks like this (provided that SABnzbd is still on your desktop):
    
    cd SABnzbd/
    /usr/bin/screen -m -d /usr/bin/nice -n 20 ~/SABnzbd/SABnzbd.py -b 0

Explanation:

  * screen -m -d: starts the command in a detached screen.
  * nice -n 20: starts the command with the lowest processor priority.
  * SABnzbd.py -b 0: starts the SABnzbd without autostarting your browser.

Start SABnzbd at boottime  
Run this script in crontab periodically, so that SABnzb+ is started at boottime and will be kept running. 
    
    #!/bin/bash
    active=$(/bin/ps aux | grep -v grep | grep SABnzbd.py)
    if [ "$active" = "" ]
    then
        /usr/bin/screen -m -d /usr/bin/nice -n 20 ~/SABnzbd/SABnzbd.py -b 0
    fi

Should you ever need to run the compiled app from Terminal, this is the way:
    
    /Applications/SABnzbd.app/Contents/MacOS/SABnzbd

If you need to see the logging output directly tro the console:
    
    /Applications/SABnzbd.app/Contents/MacOS/SABnzbd --console

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
