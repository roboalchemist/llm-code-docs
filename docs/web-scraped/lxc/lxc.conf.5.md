# Source: https://linuxcontainers.org/lxc/manpages/man5/lxc.conf.5.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man5/lxc.conf.5.html)
    -   [Deutsch](/de/lxc/manpages//man5/lxc.conf.5.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man5/lxc.conf.5.html)
    -   [Indonesia](/id/lxc/manpages//man5/lxc.conf.5.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man5/lxc.conf.5.html)

-   LXC
-   Manpages
-   lxc.conf.5

Man page of lxc.conf

# lxc.conf

Section: (5)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc.conf - Configuration files for LXC. [Â ]

## DESCRIPTION

LXC configuration is split in two parts. Container configuration and system configuration. [Â ]

### CONTAINER CONFIGURATION

The container configuration is held in the *config* stored in the container\'s directory.

A basic configuration is generated at container creation time with the default\'s recommended for the chosen template as well as extra default keys coming from the *default.conf* file.

That *default.conf* file is either located at */etc/lxc/default.conf* or for unprivileged containers at *\~/.config/lxc/default.conf*.

Details about the syntax of this file can be found in: **[lxc.container.conf](../man5/lxc.container.conf.5.html)**(5) [Â ]

### SYSTEM CONFIGURATION

The system configuration is located at */etc/lxc/lxc.conf* or *\~/.config/lxc/lxc.conf* for unprivileged containers.

This configuration file is used to set values such as default lookup paths and storage backend settings for LXC.

Details about the syntax of this file can be found in: **[lxc.system.conf](../man5/lxc.system.conf.5.html)**(5) [Â ]

## SEE ALSO

**lxc**(1), **[lxc.container.conf](../man5/lxc.container.conf.5.html)**(5), **[lxc.system.conf](../man5/lxc.system.conf.5.html)**(5), **[lxc-usernet](../man5/lxc-usernet.5.html)**(5) [Â ]

## AUTHOR

StÃ©phane Graber \<<stgraber@ubuntu.com>\>

------------------------------------------------------------------------

[Â ]

## Index

[NAME](#lbAB)

:   

[DESCRIPTION](#lbAC)

:   

    [CONTAINER CONFIGURATION](#lbAD)

    :   

    [SYSTEM CONFIGURATION](#lbAE)

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