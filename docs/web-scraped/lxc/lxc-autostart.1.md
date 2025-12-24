# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-autostart.1.html

[![Linux containers logo](/static/img/containers.small.png)](/)

[Menu](#navigation "menu") [Close menu](#navigation-closed "close menu")

[ [Jump to main content](#main-content) ]

-   [[Home](#Home-menu)]
    -   [Home Page](/)
    -   [Jobs](https://discuss.linuxcontainers.org/c/jobs/17)
-   [[Incus](#Incus-menu)]
    -   [Introduction](/incus/introduction/)

    -   [Announcement](/incus/announcement/)

    -   [Try it online](/incus/try-it/)

    -   [News](/incus/news/)

    -   [Documentation](https://linuxcontainers.org/incus/docs/main/)

    -   [Downloads](/incus/downloads/)

    -   

        ------------------------------------------------------------------------

    -   [GitHub](https://github.com/lxc/incus)

    -   [Forum](https://discuss.linuxcontainers.org)

    -   [Image server](https://images.linuxcontainers.org)
-   [[IncusOS](#IncusOS-menu)]
    -   [Introduction](/incus-os/introduction/)

    -   [Documentation](/incus-os/docs/main/)

    -   [Download](https://incusos-customizer.linuxcontainers.org)

    -   

        ------------------------------------------------------------------------

    -   [GitHub](https://github.com/lxc/incus-os)

    -   [Forum](https://discuss.linuxcontainers.org)
-   [[LXC](#LXC-menu)]
    -   [Introduction](/lxc/introduction/)

    -   [News](/lxc/news/)

    -   [Getting started](/lxc/getting-started/)

    -   [Documentation](/lxc/documentation/)

    -   [Manpages](/lxc/manpages/)

    -   [Contribute](/lxc/contribute/)

    -   [Security](/lxc/security/)

    -   [Downloads](/lxc/downloads/)

    -   

        ------------------------------------------------------------------------

    -   [GitHub](https://github.com/lxc/lxc)

    -   [Forum](https://discuss.linuxcontainers.org)

    -   [Image server](https://images.linuxcontainers.org)
-   [[LXCFS](#LXCFS-menu)]
    -   [Introduction](/lxcfs/introduction/)

    -   [News](/lxcfs/news/)

    -   [Getting started](/lxcfs/getting-started/)

    -   [Manpages](/lxcfs/manpages/)

    -   [Contribute](/lxcfs/contribute/)

    -   [Downloads](/lxcfs/downloads/)

    -   

        ------------------------------------------------------------------------

    -   [GitHub](https://github.com/lxc/lxcfs)

    -   [Forum](https://discuss.linuxcontainers.org)
-   [[distrobuilder](#distrobuilder-menu)]
    -   [Introduction](/distrobuilder/introduction/)

    -   [News](/distrobuilder/news/)

    -   [Documentation](/distrobuilder/docs/latest/)

    -   [Contribute](/distrobuilder/contribute/)

    -   [Downloads](/distrobuilder/downloads/)

    -   

        ------------------------------------------------------------------------

    -   [GitHub](https://github.com/lxc/distrobuilder)

    -   [Forum](https://discuss.linuxcontainers.org)

```
<!-- -->
```
-   [Language](#languages)
    -   [English](#)
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-autostart.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-autostart.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-autostart.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-autostart.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-autostart.1.html)

-   LXC
-   Manpages
-   lxc-autostart.1

Man page of lxc-autostart

# lxc-autostart

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-autostart - start/stop/kill auto-started containers [Â ]

## SYNOPSIS

**lxc-autostart** \[-k\] \[-L\] \[-r\] \[-s\] \[-a\] \[-A\] \[-g *groups*\] \[-t *timeout*\] [Â ]

## DESCRIPTION

**lxc-autostart** processes containers with lxc.start.auto set. It lets the user start, shutdown, kill, restart containers in the right order, waiting the right time. Supports filtering by lxc.group or just run against all defined containers. It can also be used by external tools in list mode where no action will be performed and the list of affected containers (and if relevant, delays) will be shown.

The \[-r\], \[-s\] and \[-k\] options specify the action to perform. If none is specified, then the containers will be started. \[-a\] and \[-g\] are used to specify which containers will be affected. By default only containers without a lxc.group set will be affected. \[-t TIMEOUT\] specifies the maximum amount of time to wait for the container to complete the shutdown or reboot. [Â ]

## OPTIONS

**-r,\--reboot**
:   Request a reboot of the container.

**-s,\--shutdown**
:   Request a clean shutdown. If a \[-t timeout\] greater than 0 is given and the container has not shut down within this period, it will be killed as with the \[-k kill\] option.

**-k,\--kill**
:   Rather than requesting a clean shutdown of the container, explicitly kill all tasks in the container.

**-L,\--list**
:   Rather than performing the action, just print the container name and wait delays until starting the next container.

**-t,\--timeout** *TIMEOUT*
:   Wait TIMEOUT seconds before hard-stopping the container.

**-g,\--group** *GROUP*
:   Comma separated list of groups to select (defaults to those without a lxc.group - the NULL group). This option may be specified multiple times and the arguments concatenated. The NULL or empty group may be specified as a leading comma, trailing comma, embedded double comma, or empty argument where the NULL group should be processed. Groups are processed in the order specified on the command line. Multiple invocations of the -g option may be freely intermixed with the comma separated lists and will be combined in specified order.

**-a,\--all**
:   Ignore lxc.group and select all auto-started containers.

**-A,\--ignore-auto**
:   Ignore the lxc.start.auto flag. Combined with -a, will select all containers on the system.

[Â ]

## AUTOSTART AND SYSTEM BOOT

The **lxc-autostart** command is used as part of the LXC system service, when enabled to run on host system at bootup and at shutdown. It\'s used to select which containers to start in what order and how much to delay between each startup when the host system boots.

Each container can be part of any number of groups or no group at all. Two groups are special. One is the NULL group, i.e. the container does not belong to any group. The other group is the \"onboot\" group.

When the system boots with the LXC service enabled, it will first attempt to boot any containers with lxc.start.auto == 1 that is a member of the \"onboot\" group. The startup will be in order of lxc.start.order. If an lxc.start.delay has been specified, that delay will be honored before attempting to start the next container to give the current container time to begin initialization and reduce overloading the host system. After starting the members of the \"onboot\" group, the LXC system will proceed to boot containers with lxc.start.auto == 1 which are not members of any group (the NULL group) and proceed as with the onboot group. [Â ]

## STARTUP GROUP EXAMPLES

**-g \"onboot,\"**

:   Start the \"onboot\" group first then the NULL group.

    This is the equivalent of: **-g onboot -g \"\"**.

**-g \"dns,web,,onboot\"**

:   Starts the \"dns\" group first, the \"web\" group second, then the NULL group followed by the \"onboot\" group.

    This is the equivalent of: **-g dns,web -g ,onboot** or **-g dns -g web -g \"\" -g onboot**.

[Â ]

## SEE ALSO

**[lxc](../man7/lxc.7.html)**(7), **[lxc-create](../man1/lxc-create.1.html)**(1), **[lxc-copy](../man1/lxc-copy.1.html)**(1), **[lxc-destroy](../man1/lxc-destroy.1.html)**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-stop](../man1/lxc-stop.1.html)**(1), **[lxc-execute](../man1/lxc-execute.1.html)**(1), **[lxc-console](../man1/lxc-console.1.html)**(1), **[lxc-monitor](../man1/lxc-monitor.1.html)**(1), **[lxc-wait](../man1/lxc-wait.1.html)**(1), **[lxc-cgroup](../man1/lxc-cgroup.1.html)**(1), **[lxc-ls](../man1/lxc-ls.1.html)**(1), **[lxc-info](../man1/lxc-info.1.html)**(1), **[lxc-freeze](../man1/lxc-freeze.1.html)**(1), **[lxc-unfreeze](../man1/lxc-unfreeze.1.html)**(1), **[lxc-attach](../man1/lxc-attach.1.html)**(1), **[lxc.conf](../man5/lxc.conf.5.html)**(5) [Â ]

## AUTHOR

StÃ©phane Graber \<<stgraber@ubuntu.com>\>

------------------------------------------------------------------------

[Â ]

## Index

[NAME](#lbAB)

:   

[SYNOPSIS](#lbAC)

:   

[DESCRIPTION](#lbAD)

:   

[OPTIONS](#lbAE)

:   

[AUTOSTART AND SYSTEM BOOT](#lbAF)

:   

[STARTUP GROUP EXAMPLES](#lbAG)

:   

[SEE ALSO](#lbAH)

:   

[AUTHOR](#lbAI)

:   

------------------------------------------------------------------------

This document was created by man2html, using the manual pages.\
Time: 13:50:10 GMT, December 20, 2025

Project infrastructure sponsored by [Zabbly](https://zabbly.com).

-   [Improve this website](https://github.com/lxc/linuxcontainers.org)
-   [Back to top](#)
-   [Content under Creative Commons CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)