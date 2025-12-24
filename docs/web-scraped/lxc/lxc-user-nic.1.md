# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-user-nic.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-user-nic.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-user-nic.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-user-nic.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-user-nic.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-user-nic.1.html)

-   LXC
-   Manpages
-   lxc-user-nic.1

Man page of lxc-user-nic

# lxc-user-nic

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-user-nic - Manage nics in another network namespace [Â ]

## SYNOPSIS

**lxc-user-nic** **create**       **lxc-user-nic** **delete**       [Â ]

## DESCRIPTION

**lxc-user-nic** is a setuid-root program with which unprivileged users may manage network interfaces for use by a lxc container.

It will consult the configuration file */etc/lxc/lxc-usernet* to determine the number of interfaces which the calling user is allowed to create, and which bridge he may attach them to. It tracks the number of interfaces each user has created using the file */run/lxc/nics*. It ensures that the calling user is privileged over the network namespace to which the interface will be attached. **lxc-user-nic** also allows one to delete network devices. Currently only ovs ports can be deleted. [Â ]

## OPTIONS

*lxcpath*
:   The path of the container. This is currently not used.

*name*
:   The name of the container. This is currently not used.

*pid*
:   The process id for the task to whose network namespace the interface should be attached.

*type*
:   The network interface type to attach. Currently only veth is supported. With this type, two interfaces representing each tunnel endpoint are created. One endpoint will be attached to the specified bridge, while the other will be passed into the container.

*bridge*
:   The bridge to which to attach the network interface, for instance *lxcbr0*.

*container nicname*
:   The desired interface name in the container. This will be *eth0* if unspecified.

*path to network namespace*
:   A path to open to get a file descriptor for the target network namespace. This is only relevant when an veth device is deleted.

[Â ]

## SEE ALSO

**lxc**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-usernet](../man5/lxc-usernet.5.html)**(5) [Â ]

## AUTHOR

Christian Brauner \<<christian@brauner.io>\>

Serge Hallyn \<<serge@hallyn.com>\>

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

[SEE ALSO](#lbAF)

:   

[AUTHOR](#lbAG)

:   

------------------------------------------------------------------------

This document was created by man2html, using the manual pages.\
Time: 13:50:10 GMT, December 20, 2025

Project infrastructure sponsored by [Zabbly](https://zabbly.com).

-   [Improve this website](https://github.com/lxc/linuxcontainers.org)
-   [Back to top](#)
-   [Content under Creative Commons CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)