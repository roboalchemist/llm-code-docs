# Source: https://linuxcontainers.org/lxc/manpages/man5/lxc-usernet.5.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man5/lxc-usernet.5.html)
    -   [Deutsch](/de/lxc/manpages//man5/lxc-usernet.5.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man5/lxc-usernet.5.html)
    -   [Indonesia](/id/lxc/manpages//man5/lxc-usernet.5.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man5/lxc-usernet.5.html)

-   LXC
-   Manpages
-   lxc-usernet.5

Man page of lxc-usernet

# lxc-usernet

Section: (5)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-usernet - unprivileged user network administration file. [Â ]

## DESCRIPTION

*/etc/lxc/lxc-usernet* controls the limits which the program **lxc-user-nic** places on network interfaces which an unprivileged user may create. [Â ]

### CONFIGURATION

This file consists of multiple entries, one per line, of the form:

**user** **type** **bridge** **number**

or

**\@group** **type** **bridge** **number**

Where

**user**
:   is the username to whom this entry applies.

**\@group**
:   is the groupname to which this entry applies.

**type**
:   is the type of network interface being allowed. Only veth is currently supported.

**bridge**
:   is the bridge to which the network interfaces may be attached, for instance *lxcbr0*.

**number**
:   is the number or quota of network interfaces of the given type which the given user or group may attach to the given bridge, for instance *2*.

Since a user can be specified both by username as well as one or more usergroups, it is possible that several configuration lines enable that user to create network interfaces. In such cases, any interfaces create are counted towards the quotas of the user or group in the order in which they appear in the file. If the quota of one line is full, the rest will be parsed until one is found or the end of the file. [Â ]

## SEE ALSO

**lxc**(1), **[lxc-user-nic](../man1/lxc-user-nic.1.html)**(1) [Â ]

## AUTHOR

Daniel Lezcano \<<daniel.lezcano@free.fr>\>

------------------------------------------------------------------------

[Â ]

## Index

[NAME](#lbAB)

:   

[DESCRIPTION](#lbAC)

:   

    [CONFIGURATION](#lbAD)

    :   

[SEE ALSO](#lbAE)

:   

[AUTHOR](#lbAF)

:   

------------------------------------------------------------------------

This document was created by man2html, using the manual pages.\
Time: 13:50:10 GMT, December 20, 2025

Project infrastructure sponsored by [Zabbly](https://zabbly.com).

-   [Improve this website](https://github.com/lxc/linuxcontainers.org)
-   [Back to top](#)
-   [Content under Creative Commons CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)