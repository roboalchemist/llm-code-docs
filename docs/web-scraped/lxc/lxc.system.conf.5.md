# Source: https://linuxcontainers.org/lxc/manpages/man5/lxc.system.conf.5.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man5/lxc.system.conf.5.html)
    -   [Deutsch](/de/lxc/manpages//man5/lxc.system.conf.5.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man5/lxc.system.conf.5.html)
    -   [Indonesia](/id/lxc/manpages//man5/lxc.system.conf.5.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man5/lxc.system.conf.5.html)

-   LXC
-   Manpages
-   lxc.system.conf.5

Man page of lxc.system.conf

# lxc.system.conf

Section: (5)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc.system.conf - LXC system configuration file [Â ]

## DESCRIPTION

The system configuration is located at */etc/lxc/lxc.conf* or *\~/.config/lxc/lxc.conf* for unprivileged containers.

This configuration file is used to set values such as default lookup paths and storage backend settings for LXC. [Â ]

### CONFIGURATION PATHS

**lxc.lxcpath**
:   The location in which all containers are stored.

**lxc.default_config**
:   The path to the default container configuration.

[Â ]

### CONTROL GROUPS

**lxc.cgroup.use**
:   Comma separated list of cgroup controllers to setup. If none is specified, all available controllers will be used.

**lxc.cgroup.pattern**
:   Format string used to generate the cgroup path (e.g. lxc/%n).

[Â ]

### LVM

**lxc.bdev.lvm.vg**
:   Default LVM volume group name.

**lxc.bdev.lvm.thin_pool**
:   Default LVM thin pool name.

[Â ]

### ZFS

**lxc.bdev.zfs.root**
:   Default ZFS root name.

[Â ]

## **lxc**(1),

**[lxc.container.conf](../man5/lxc.container.conf.5.html)**(5), **[lxc.system.conf](../man5/lxc.system.conf.5.html)**(5), **[lxc-usernet](../man5/lxc-usernet.5.html)**(5) [Â ]

## SEE ALSO

**[lxc](../man7/lxc.7.html)**(7), **[lxc-create](../man1/lxc-create.1.html)**(1), **[lxc-copy](../man1/lxc-copy.1.html)**(1), **[lxc-destroy](../man1/lxc-destroy.1.html)**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-stop](../man1/lxc-stop.1.html)**(1), **[lxc-execute](../man1/lxc-execute.1.html)**(1), **[lxc-console](../man1/lxc-console.1.html)**(1), **[lxc-monitor](../man1/lxc-monitor.1.html)**(1), **[lxc-wait](../man1/lxc-wait.1.html)**(1), **[lxc-cgroup](../man1/lxc-cgroup.1.html)**(1), **[lxc-ls](../man1/lxc-ls.1.html)**(1), **[lxc-info](../man1/lxc-info.1.html)**(1), **[lxc-freeze](../man1/lxc-freeze.1.html)**(1), **[lxc-unfreeze](../man1/lxc-unfreeze.1.html)**(1), **[lxc-attach](../man1/lxc-attach.1.html)**(1), **[lxc.conf](../man5/lxc.conf.5.html)**(5) [Â ]

## AUTHOR

StÃ©phane Graber \<<stgraber@ubuntu.com>\>

------------------------------------------------------------------------

[Â ]

## Index

[NAME](#lbAB)

:   

[DESCRIPTION](#lbAC)

:   

    [CONFIGURATION PATHS](#lbAD)

    :   

    [CONTROL GROUPS](#lbAE)

    :   

    [LVM](#lbAF)

    :   

    [ZFS](#lbAG)

    :   

[**lxc**(1),](#lbAH)

:   

[SEE ALSO](#lbAI)

:   

[AUTHOR](#lbAJ)

:   

------------------------------------------------------------------------

This document was created by man2html, using the manual pages.\
Time: 13:50:10 GMT, December 20, 2025

Project infrastructure sponsored by [Zabbly](https://zabbly.com).

-   [Improve this website](https://github.com/lxc/linuxcontainers.org)
-   [Back to top](#)
-   [Content under Creative Commons CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)