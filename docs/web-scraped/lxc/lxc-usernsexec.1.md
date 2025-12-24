# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-usernsexec.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-usernsexec.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-usernsexec.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-usernsexec.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-usernsexec.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-usernsexec.1.html)

-   LXC
-   Manpages
-   lxc-usernsexec.1

Man page of lxc-usernsexec

# lxc-usernsexec

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-usernsexec - Run a task as root in a new user namespace. [Â ]

## SYNOPSIS

**lxc-usernsexec** \[-m *uid-map*\]  [Â ]

## DESCRIPTION

**lxc-usernsexec** can be used to run a task as root in a new user namespace. [Â ]

## OPTIONS

**-m** *uid-map*

:   The uid map to use in the user namespace. Each map consists of four colon-separate values. First a character \'u\', \'g\' or \'b\' to specify whether this map pertains to user ids, group ids, or both; next the first userid in the user namespace; next the first userid as seen on the host; and finally the number of ids to be mapped.

    More than one map can be specified. If no map is specified, then by default the full uid and gid ranges granted by /etc/subuid and /etc/subgid will be mapped to the uids and gids starting at 0 in the container.

    Note that *lxc-usernsexec* always tries to setuid and setgid to 0 in the namespace. Therefore uid 0 in the namespace must be mapped.

[Â ]

## EXAMPLES

To spawn a shell with the full allotted subuids mapped into the container, use

              lxc-usernsexec
            

To run a different shell than */bin/sh*, use

              lxc-usernsexec -- /bin/bash
            

If your user id is 1000, root in a container is mapped to 190000, and you wish to chown a file you own to root in the container, you can use:

              lxc-usernsexec -m b:0:1000:1 -m b:1:190000:1 -- /bin/chown 1:1 $file
            

This maps your userid to root in the user namespace, and 190000 to uid 1. Since root in the user namespace is privileged over all userids mapped into the namespace, you are allowed to change the file ownership, which you could not do on the host using a simple chown. [Â ]

## SEE ALSO

**[lxc](../man7/lxc.7.html)**(7), **[lxc-create](../man1/lxc-create.1.html)**(1), **[lxc-copy](../man1/lxc-copy.1.html)**(1), **[lxc-destroy](../man1/lxc-destroy.1.html)**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-stop](../man1/lxc-stop.1.html)**(1), **[lxc-execute](../man1/lxc-execute.1.html)**(1), **[lxc-console](../man1/lxc-console.1.html)**(1), **[lxc-monitor](../man1/lxc-monitor.1.html)**(1), **[lxc-wait](../man1/lxc-wait.1.html)**(1), **[lxc-cgroup](../man1/lxc-cgroup.1.html)**(1), **[lxc-ls](../man1/lxc-ls.1.html)**(1), **[lxc-info](../man1/lxc-info.1.html)**(1), **[lxc-freeze](../man1/lxc-freeze.1.html)**(1), **[lxc-unfreeze](../man1/lxc-unfreeze.1.html)**(1), **[lxc-attach](../man1/lxc-attach.1.html)**(1), **[lxc.conf](../man5/lxc.conf.5.html)**(5) [Â ]

## AUTHOR

Serge Hallyn \<<serge.hallyn@ubuntu.com>\>

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

[EXAMPLES](#lbAF)

:   

[SEE ALSO](#lbAG)

:   

[AUTHOR](#lbAH)

:   

------------------------------------------------------------------------

This document was created by man2html, using the manual pages.\
Time: 13:50:10 GMT, December 20, 2025

Project infrastructure sponsored by [Zabbly](https://zabbly.com).

-   [Improve this website](https://github.com/lxc/linuxcontainers.org)
-   [Back to top](#)
-   [Content under Creative Commons CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)