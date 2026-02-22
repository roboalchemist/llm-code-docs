# Source: https://sabnzbd.org/wiki/installation/install-off-modules

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Install+from+source&body=%23%23+URL%3A+%2Fwiki%2Finstallation%2Finstall-off-modules.html%0A%0AImprovement:%0A) Install from source 

## Guides for Windows and macOS

Specific guides to install from source are available for:

  * [Windows](/wiki/installation/install-from-source-windows)
  * [Apple macOS](/wiki/installation/install-macos)

* * *

## Linux platforms

### Source

Get a local copy (clone) of the SABnzbd source from github or via git with: 
    
    git clone -b master https://github.com/sabnzbd/sabnzbd.git 

### Python

SABnzbd 3.7.2 and higher requires [Python 3.8 or higher](http://www.python.org).  
Check python version with `python3 --version`. 

### Must-have Python modules

Python comes included with a Python Packages Manager (`pip`) on many platforms.  
Which may be required to be updated to handle building/installing newer packages for your system.  
  
Upgrade the python package manager and build modules: 
    
    python3 -m pip install --upgrade pip wheel
    
Install the Python module requirements from the SABnzbd source directory: 
    
    pip3 install --upgrade -r requirements.txt
    
If you plan to do development work, you might need the following OS packages: 
    
    pip3 install --upgrade -r builder/requirements.txt
    pip3 install --upgrade -r tests/requirements.txt
    
On **non-x86** linux platforms you may need to install: 
    
    python3-dev python3-setuptools python3-pip libffi-dev libssl-dev openssl-dev musl-dev cargo
    
If the `sabctools` (formerly called `sabyenc`) installation fails, read [here](/sabctools).

Start SABnzbd by running: 
    
    ./SABnzbd.py

### Multi-language support

To enable multi-language support (and fix mistakes in English texts) you will need to run this command once before starting SABnzbd for the first time and after each major update: 
    
    python3 tools/make_mo.py

### Must-have utilities

#### `unrar`

We recommend release 5.5 or higher your package manager or the [official website](http://www.rarlab.com/rar_add.htm). 

#### `par2`

Available through package managers as `par2`, `par2cmdline` or via [GitHub](https://github.com/Parchive/par2cmdline/releases).  
Optimized versions of `par2` can also be installed, read more [here](/wiki/installation/multicore-par2). 

### Optional utilities

#### `unzip`

Any `unzip` command that supports passwords (via `-P` option) will function.  
Can usually be installed via package managers, alternatively InfoZip's unzip program can be obtained [here](http://gnuwin32.sourceforge.net/packages/unzip.htm). 

#### `7zip`

7zip can be obtained via package managers, the command that SABnzbd looks for is `7za` or `7z`.  
The package is called `7zip` or can be obtained from the [official website](http://www.7-zip.org/).  
`p7zip` was a modification of 7zip to provide linux support which has been abanonded. 

#### `nice`

To adjust the **CPU priority** of external tools that SABnzbd runs (ex: par / unrar)

#### `ionice`

To adjust the **disk priority** of external tools that SABnzbd runs (ex: par / unrar)

#### `notify-osd`

NotifyOSD provides desktop pop-up notifications. Available through package managers as `notify-osd`.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
