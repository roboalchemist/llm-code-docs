# Source: https://sabnzbd.org/wiki/advanced/command-line-parameters

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

### [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Command+Line+Parameters&body=%23%23+URL%3A+%2Fwiki%2Fadvanced%2Fcommand-line-parameters.html%0A%0AImprovement:%0A) Command Line Parameters

You can start SABnzbd with options. You normally do this from a command prompt (Windows) or a shell (Unix).
An option is a combination of the option name and one parameter. For parameters that contain spaces, you must surround the parameter with double quotes (e.g. `--config-file "/my very long path/SABnzbd.ini"`).

Short | Long command | Description
---|---|---
`-f` | `--config-file <path-to-ini>` | The name of the configuration file.
|  |  If you specify an INI file, all relative folders in Config->Folders will be relative to the location of the INI file. If you do not specify an INI file, SABnzbd will first check the [Default Locations](/wiki/advanced/directory-setup).
`-s` |  `--server <host:port>` |  Specify IP address and port that SABnzbd should listen on. Value will be stored in the INI file. See [General - Host and Port](/wiki/configuration/4.5/general) section for supported notations
`-t` |  `--templates <template>` |  Select another set of user interface templates. Use a name of a set in the `interfaces` folder.
The name of a standard interface ("Glitter", "Plush" or "smpl")
`-l` |  `--logging <-1..2>` |  `-1` = Disable all logging
`0` = Only show errors and warnings
`1` = Also show info messages
`2` = Also show debug messages (use only when analyzing problems)
`-w` |  `--weblogging` |  Logging of the webserver framework on (use only when analyzing problems)
`-b` |  `--browser <0|1>` |  `0` = Do not show the browser (recommended for servers).
`1` = SABnzbd will start the system's default browser, showing the GUI of SABnznd (default).
`-d` |  `--daemon` |  Start in daemon mode. Run without a terminal window and do not start the browser. Do NOT assume that the user profile can be used. You must use the `-f <path-to-ini>` option.
|  `--pid <path-file>` |  Create a file with the PID (process number) of the SABnznbd process. The file will exists as long as the instance of SABnzbd lives (unless it crashes). A full directory path is required. The file name will be `sabnzbd-port.pid` where `port` is the port number used for the web server. [Only Unix/macOS]
|  `--pidfile <path-file>` |  Use this to set a file (full path required) where SABnzbd can store its PID. The content of the file will be the process number (PID). [Only Unix/macOS]
`-h` |  `--help` |  Show short explanation of the commandline options and exit program (won't work with Win32 binary)
`-v` |  `--version` |  Show SABnzbd's version and exit program (won't work with Win32 binary)
`-c` |  `--clean` |  Clear the cache and log directories. All queued downloads will be removed. The `download_dir` is **not** cleared.
`-p` |  `--pause` | Start in paused mode
| `--repair` |  Add orphaned jobs from the incomplete folder to the queue. Can also be performed from the GUI.
| `--repair-all` |  Try to reconstruct the queue from the incomplete folder with full data reconstruction. Can also be performed from the GUI.
|  `--https <port>` |  Set the HTTPS port number and enable HTTPS for the user interface
|  `--ipv6_hosting <0|1>` |  Use `0` when your system cannot handle `::1` (the IPv6 value of `localhost`). The setting will be stored in the `sabnzbd.ini` file.
|  `--inet_exposure <0..5>` |  Set the `External internet access`. See [General - External internet access](/wiki/configuration/4.5/general) section for supported levels, starting at `0` for `No access` (the default).
|  `--no-login` |  Start SABnzbd and reset username and password.
|  `--log-all` |  Log all article handling and enable other excessive logging (for developers).
|  `--disable-file-log` |  Logging is only written to console, useful if `stdout` is redirected to another logging system.
|  `--new` |  Normally SABnzbd checks if an instance of SABnzbd is already running. If so and the versions match, the second instance will just activate the web interface of the first instance or send an NZB to the first instance. If you really want to run multiple instances, you will need to use the `--new` parameter.
|  `--console` |  Force console logging.

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
