# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-create.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-create.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-create.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-create.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-create.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-create.1.html)

-   LXC
-   Manpages
-   lxc-create.1

Man page of lxc-create

# lxc-create

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-create - creates a container [Â ]

## SYNOPSIS

**lxc-create**  \[-f *config_file*\]  \[-B *backingstore*\] \[\-- *template-options*\] [Â ]

## DESCRIPTION

**lxc-create** creates a system object where is stored the configuration information and where can be stored user information. The identifier *name* is used to specify the container to be used with the different lxc commands.

The object is a directory created in */var/lib/lxc* and identified by its name.

The object is the definition of the different resources an application can use or can see. The more the configuration file contains information, the more the container is isolated and the more the application is jailed.

If the configuration file *config_file* is not specified, the container will be created with the default isolation: processes, sysv ipc and mount points. [Â ]

## OPTIONS

**-f, \--config** *config_file*
:   Specify the configuration file to configure the virtualization and isolation functionalities for the container.

**-t, \--template** *template*
:   \'template\' is the short name of an existing \'lxc-template\' script that is called by lxc-create, eg. busybox, debian, fedora, ubuntu or sshd. Refer to the examples in */usr/share/lxc/templates* for details of the expected script structure. Alternatively, the full path to an executable template script can also be passed as a parameter. \"none\" can be used to force lxc-create to skip rootfs creation.

**-B, \--bdev** *backingstore*

:   \'backingstore\' is one of \'dir\', \'lvm\', \'loop\', \'btrfs\', \'zfs\', \'rbd\', or \'best\'. The default is \'dir\', meaning that the container root filesystem will be a directory under */var/lib/lxc/container/rootfs*. This backing store type allows the optional *\--dir ROOTFS* to be specified, meaning that the container rootfs should be placed under the specified path, rather than the default. (The \'none\' backingstore type is an alias for \'dir\'.) If \'btrfs\' is specified, then the target filesystem must be btrfs, and the container rootfs will be created as a new subvolume. This allows snapshotted clones to be created, but also causes rsync \--one-filesystem to treat it as a separate filesystem. If backingstore is \'lvm\', then an lvm block device will be used and the following further options are available: *\--lvname lvname1* will create an LV named *lvname1* rather than the default, which is the container name. *\--vgname vgname1* will create the LV in volume group *vgname1* rather than the default, *lxc*. *\--thinpool thinpool1* will create the LV as a thin-provisioned volume in the pool named *thinpool1* rather than the default, *lxc*. *\--fstype FSTYPE* will create an FSTYPE filesystem on the LV, rather than the default, which is ext4. *\--fssize SIZE* will create a LV (and filesystem) of size SIZE rather than the default, which is 1G.

    If backingstore is \'loop\', you can use *\--fstype FSTYPE* and *\--fssize SIZE* as \'lvm\'. The default values for these options are the same as \'lvm\'.

    If backingstore is \'rbd\', then you will need to have a valid configuration in *ceph.conf* and a *ceph.client.admin.keyring* defined. You can specify the following options : *\--rbdname RBDNAME* will create a blockdevice named RBDNAME rather than the default, which is the container name. *\--rbdpool POOL* will create the blockdevice in the pool named POOL, rather than the default, which is \'lxc\'.

    If backingstore is \'best\', then lxc will try, in order, btrfs, zfs, lvm, and finally a directory backing store.

**\--** *template-options*
:   This will pass *template-options* to the template as arguments. To see the list of options supported by the template, you can run **lxc-create -t TEMPLATE -h**.

[Â ]

## COMMON OPTIONS

These options are common to most of lxc commands.

**-?, -h, \--help**
:   Print a longer usage message than normal.

**\--usage**
:   Give the usage message

**-q, \--quiet**
:   mute on

**-P, \--lxcpath=***PATH*
:   Use an alternate container path. The default is /var/lib/lxc.

**-o, \--logfile=***FILE*
:   Output to an alternate log *FILE*. The default is no log.

**-l, \--logpriority=***LEVEL*

:   Set log priority to *LEVEL*. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG.

    Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.

**-n, \--name=***NAME*
:   Use container identifier *NAME*. The container identifier format is an alphanumeric string.

**\--rcfile=***FILE*

:   Specify the configuration file to configure the virtualization and isolation functionalities for the container.

    This configuration file if present will be used even if there is already a configuration file present in the previously created container (via lxc-create).

**\--version**
:   Show the version number.

[Â ]

## DIAGNOSTIC

The container already exists
:   As the message mention it, you try to create a container but there is a container with the same name. You can use the **lxc-ls** command to list the available containers on the system.

[Â ]

## SEE ALSO

**[lxc](../man7/lxc.7.html)**(7), **[lxc-create](../man1/lxc-create.1.html)**(1), **[lxc-copy](../man1/lxc-copy.1.html)**(1), **[lxc-destroy](../man1/lxc-destroy.1.html)**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-stop](../man1/lxc-stop.1.html)**(1), **[lxc-execute](../man1/lxc-execute.1.html)**(1), **[lxc-console](../man1/lxc-console.1.html)**(1), **[lxc-monitor](../man1/lxc-monitor.1.html)**(1), **[lxc-wait](../man1/lxc-wait.1.html)**(1), **[lxc-cgroup](../man1/lxc-cgroup.1.html)**(1), **[lxc-ls](../man1/lxc-ls.1.html)**(1), **[lxc-info](../man1/lxc-info.1.html)**(1), **[lxc-freeze](../man1/lxc-freeze.1.html)**(1), **[lxc-unfreeze](../man1/lxc-unfreeze.1.html)**(1), **[lxc-attach](../man1/lxc-attach.1.html)**(1), **[lxc.conf](../man5/lxc.conf.5.html)**(5) [Â ]

## AUTHOR

Daniel Lezcano \<<daniel.lezcano@free.fr>\>

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

[COMMON OPTIONS](#lbAF)

:   

[DIAGNOSTIC](#lbAG)

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