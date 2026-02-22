# Source: https://sabnzbd.org/wiki/configuration/4.5/scheduling

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

##  [ Incorrect or missing information? ](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Scheduling&body=%23%23+URL%3A+%2Fwiki%2Fconfiguration%2F4.5%2Fscheduling.html%0A%0AImprovement:%0A) Scheduling 

You can use the scheduler to set up tasks to be performed at specific days and times. Each schedule block is repeated one per week or every day.

Action | Description  
---|---  
**Resume** | Continue downloading, Watched Folder scanning and RSS feed readouts.  
**Pause** |  Stop downloading  
NOTE Will pause at startup if not combined with a scheduled **Resume**.   
**Pause-all** | Stop downloading, [Watched Folder](/wiki/configuration/4.5/folders) scanning and RSS feeds, stops all disk activity.  
**Shutdown** | Exit SABnzbd.  
**Restart** | Restart SABnzbd.  
**Speedlimit** | Set the speedlimiter to the given `%` value. This can also be in `K/M/G` notation, for example `4.5M` will set the speedlimit to 4.5MB/s.  
**Pause post processing** | Halt post-processing (except active job), while downloading continues.  
**Resume post processing** | Will resume post-processing, while downloading continues.  
**Scan watched folder** | Read watched folder (this will disable the interval in [Folders](/wiki/configuration/4.5/folders)).  
**Create backup** | Create a scheduled backup of the configuration file and databases in the Complete Download Folder.  
**Read RSS feeds** |  Read all RSS feeds (this will disable the interval in [RSS](/wiki/configuration/4.5/rss)).  
**Remove failed jobs** |  Remove all jobs in history that have failed to complete, including their files.  
**Remove completed jobs** |  Remove all jobs in history that have completed successfully.  
**Pause low/normal/high priority jobs** |  All jobs with a low/normal/high priority will set to paused mode.  
**Resume low/normal/high priority jobs** |  All jobs with a low/normal/high priority will be resumed.  
**Enable/Disable quota management** |  See [Quota](/wiki/configuration/4.5/switches).  
**Enable/Disable`server-name`** |  Enable or disable a server on the given time.  
**Pause/Resume`category-name`**| All jobs within the selected category will be paused/unpaused.  
  
NOTE On startup, SABnzbd will evaluate all schedules and determine the current pause/resume state and speedlimit. The `-pause` [command-line parameter](/wiki/advanced/command-line-parameters) will override this evaluation.

NOTE On each schedule change, the schedule will be re-evaluated and the speedlimit will be set. If SABnzbd happened to be paused, it will NOT be resumed by the schedule evaluation. This is to prevent spontaneous resumption during schedule changes. 

* * *

## Example

Suppose you only want to download on weekdays between 1:00AM and 5:30PM and in the weekend between 1:00 AM and 11:00AM.  
You set this up using four schedule blocks. 

Resume downloading every day at 1:00AM:  
`01:00 Daily Resume`

Pause downloading every day at 5:30PM (= 17:30 military time):  
`17:30 Daily Pause`

Pause downloading on Saturday 11:00AM:  
`11:00 Saturday Pause`

Pause downloading on Sunday 11:00AM:  
`11:00 Sunday Pause`

Enable server on Monday 6:00AM:  
`06:00 my.usenet.com:119 1`

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)   

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")   
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
