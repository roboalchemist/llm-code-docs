# Source: https://sabnzbd.org/wiki/configuration/4.5/scripts/post-processing-scripts

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

## [Incorrect or missing information?](https://github.com/sabnzbd/sabnzbd.github.io/issues/new?title=Improve%3A+Post-processing+scripts&body=%23%23+URL%3A+%2Fwiki%2Fconfiguration%2F4.5%2Fscripts%2Fpost-processing-scripts.html%0A%0AImprovement:%0A) Post-processing scripts

SABnzbd can run a user-provided post-processing scripts. The scripts can be associated with a job entry when adding the job manually, via [category](/wiki/configuration/4.5/categories) or during downloading. Scripts can also be run as an end-of-queue event. A post-processing script will only run when the job has completed without errors. If you want to always run the script, you need to disable the option [Post-Process Only Verified Jobs](/wiki/configuration/4.5/switches).

Scripts may use any scripting language available on your system; common choices are Python, Unix shell, and Windows batch scripts. All scripts must be located in the Scripts-directory, specified in [Config->Folders](/wiki/configuration/4.5/folders) and must be executable. On Unix-like operating systems (Linux, BSD, etc.) this means the x-bit must be on. On Windows, the requirement is that the script's extension is listed in your system's `PATHEXT` environment variable.

The console output of the script is captured by SABnzbd and is saved in the so called "Script Log" which can be opened from the history details. The output will be added to the (optional) notification email and can be examined in the History page.

The "return" code that your script itself returns should be `0` if all went well or non-zero if errors occurred. If the return code is something else than `0`, SABnzbd's History will show that return code (also known as exit code) as `Exit(...)` in the History. By default the job will not be flagged as failed in case the exit code is non-zero. In [Config->Switches](/wiki/configuration/4.5/switches) there is the option to let a non-zero code mark the job as failed.

Example scripts are included in the `scripts` directory of your SABnzbd installation and are shown at the end of this page.

* * *

## Basic parameters

The script will receive the parameters described below. Use `%1` in Windows scripts and `$1` in Unix scripts. Note that on Windows the input parameters are surrounded by quotes (e.g. `"job name"`).

NOTE **Much more information is available to scripts via environment variables,see below!**

Position | Description  
---|---  
1 | The final directory of the job (full path)  
2 | The original name of the NZB file  
3 | Clean version of the job name (no path info and ".nzb" removed)  
4 | Indexer's report number (if supported)  
5 | User-defined category  
6 | Group that the NZB was posted in e.g. alt.binaries.x  
7 | Status of post processing.

* `0` = OK
* `1` = Failed verification
* `2` = Failed unpack
* `3` = 1+2
* `-1` = Failed post processing

8 | URL to be called when job failed (if provided by the server, it is always sent, so check parameter 7!).  
The URL is provided by some indexers as the X-DNZB-Failure header  
  
* * *

## Environment variables

Your script can get extra information via environment variables:

Variable | Description  
---|---  
`SAB_SCRIPT` | The name of the current script  
`SAB_NZO_ID` | The unique ID assigned to the job  
`SAB_FINAL_NAME` | The name of the job in the queue and of the final folder  
`SAB_FILENAME` | The NZB filename (after grabbing from the URL)  
`SAB_COMPLETE_DIR` | The whole path to the output directory of the job  
`SAB_PP_STATUS` | Was post-processing successfully completed (repair and/or unpack, if enabled by user)  
`SAB_CAT` | What category was assigned  
`SAB_BYTES` | Total number of bytes  
`SAB_BYTES_TRIED` | How many bytes of the total bytes were tried  
`SAB_BYTES_DOWNLOADED` | How many bytes were received (can be more than tried, due to overhead)  
`SAB_DUPLICATE` | Was this a duplicate and what type  
`SAB_DUPLICATE_KEY` | The key used for Smart Duplicate Detection  
`SAB_UNWANTED_EXT` | Were there unwanted extensions  
`SAB_OVERSIZED` | Was the job over the user's size limit  
`SAB_PASSWORD` | What was the password supplied by the NZB or the user  
`SAB_CORRECT_PASSWORD` | The password that was detected as being the correct password for this job (added in 3.4.0)  
`SAB_ENCRYPTED` | Was the job detected as encrypted  
`SAB_STATUS` | Current status (completed/failed/running)  
`SAB_FAIL_MSG` | If job failed, why did it fail  
`SAB_AGE` | Average age of the articles in the post  
`SAB_URL` | URL from which the NZB was retrieved  
`SAB_AVG_BPS` | Average bytes/second speed during active downloading  
`SAB_DOWNLOAD_TIME` | How many seconds did we download  
`SAB_PP` | What post-processing was activated (download/repair/unpack/delete)  
`SAB_REPAIR` | Was repair selected by user  
`SAB_UNPACK` | Was unpack selected by user  
`SAB_FAILURE_URL` | Provided by some indexers as alternative NZB if download fails  
`SAB_PRIORITY` | Priority set by user  
`SAB_GROUP` | Newsgroup where (most of) the job's articles came from  
`SAB_ORIG_NZB_GZ` | Path to the original NZB-file of the job. The NZB-file is compressed with gzip (`.gz`)  
`SAB_VERSION` | The version of SABnzbd used  
`SAB_PROGRAM_DIR` | The directory where the current SABnzbd instance is located  
`SAB_API_KEY` | The API-key that you can use to communicate with the SABnzbd [API](/wiki/configuration/4.5/api).  
`SAB_API_URL` |  The URL to the SABnzbd [API](/wiki/configuration/4.5/api), for example `http://127.0.0.1:8080/api`.  
It does not include the required `apikey` parameter, use `SAB_API_KEY`.  
`SAB_PAR2_COMMAND` | The path to the `par2` command on the system that SABnzbd uses  
`SAB_MULTIPAR_COMMAND` | Windows-only (empty on other systems). The path to the MultiPar command on the system that SABnzbd uses  
`SAB_RAR_COMMAND` | The path to the `unrar` command on the system that SABnzbd uses  
`SAB_ZIP_COMMAND` | The path to the `unzip` command on the system that SABnzbd uses  
`SAB_7ZIP_COMMAND` | The path to the `7z` command on the system that SABnzbd uses. Not all systems have 7zip installed (it's optional for SABnzbd), so this can also be empty  
`PYTHONUNBUFFERED` | This variable is set to 1 when running a Python script (`.py`), in order to force Python to write output to SABnzbd directly instead of buffering it  
  
* * *

## Example Python script using basic parameters

The get the parameters in python, you can do this:
  
    import sys
    try:
        (scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url) = sys.argv
    except:
        print("No commandline parameters found")
        sys.exit(1)
  
    # continue script
  
    # Your code goes here
  
    # Success code
    sys.exit(0)

* * *

## Example Python script using environment variables
  
    import os
  
    print("SABnzbd version:", os.environ['SAB_VERSION'])
    print("Job location:", os.environ['SAB_COMPLETE_DIR'])
    print("Fail msg:", os.environ['SAB_FAIL_MSG'])
  
    # Your code
  
    # Success code
    sys.exit(0)

* * *

[![Special Newshosting offer for SABnzbd users](/images/specials/nh_horizontal.png)](https://www.newshosting.com/partners/exclusive-usenet-offer/?a_aid=sabnzbd&chan=mb2)  

SABnzbd is (C) [the SABnzbd-Team](/wiki/contact) [![SABnzbd on Twitter](/images/twitter-logo.svg)](https://twitter.com/sabnzbd "SABnzbd on Twitter")  
Unless stated otherwise, text content of this page is licensed under [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).  
