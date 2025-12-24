# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-top.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-top.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-top.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-top.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-top.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-top.1.html)

-   LXC
-   Manpages
-   lxc-top.1

Man page of lxc-top

# lxc-top

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-top - monitor container statistics [Â ]

## SYNOPSIS

**lxc-top** \[\--help\] \[\--delay *delay*\] \[\--sort *sortby*\] \[\--reverse\] [Â ]

## DESCRIPTION

**lxc-top** displays container statistics. The output is updated every *delay* seconds, and is ordered according to the *sortby* value given. **lxc-top** will display as many containers as can fit in your terminal. Press \'q\' to quit. Press one of the sort key letters to sort by that statistic. Pressing a sort key letter a second time reverses the sort order. [Â ]

## OPTIONS

**-d, \--delay** *delay*
:   Amount of time in seconds to delay between screen updates. The default is 3 seconds.

**-s, \--sort** *sortby*
:   Sort the containers by name, cpu use, or memory use. The *sortby* argument should be one of the letters n,c,b,m,k to sort by name, cpu use, block I/O, memory, or kernel memory use respectively. The default is \'n\'.

**-r, \--reverse**
:   Reverse the default sort order. By default, names sort in ascending alphabetical order and values sort in descending amounts (ie. largest value first).

[Â ]

## EXAMPLE

lxc-top \--delay 1 \--sort m
:   Display containers, updating every second, sorted by memory use.

[Â ]

## NOTES

For performance reasons the kernel does not account kernel memory use unless a kernel memory limit is set. If a limit is not set, **lxc-top** will display kernel memory use as 0. If no containers are being accounted, the KMem column will not be displayed. A limit can be set by specifying

          lxc.cgroup.memory.kmem.limit_in_bytes = number
          

in your container configuration file, see **[lxc.conf](../man5/lxc.conf.5.html)**(5). [Â ]

## SEE ALSO

**[lxc](../man7/lxc.7.html)**(7), **[lxc-create](../man1/lxc-create.1.html)**(1), **[lxc-copy](../man1/lxc-copy.1.html)**(1), **[lxc-destroy](../man1/lxc-destroy.1.html)**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-stop](../man1/lxc-stop.1.html)**(1), **[lxc-execute](../man1/lxc-execute.1.html)**(1), **[lxc-console](../man1/lxc-console.1.html)**(1), **[lxc-monitor](../man1/lxc-monitor.1.html)**(1), **[lxc-wait](../man1/lxc-wait.1.html)**(1), **[lxc-cgroup](../man1/lxc-cgroup.1.html)**(1), **[lxc-ls](../man1/lxc-ls.1.html)**(1), **[lxc-info](../man1/lxc-info.1.html)**(1), **[lxc-freeze](../man1/lxc-freeze.1.html)**(1), **[lxc-unfreeze](../man1/lxc-unfreeze.1.html)**(1), **[lxc-attach](../man1/lxc-attach.1.html)**(1), **[lxc.conf](../man5/lxc.conf.5.html)**(5) [Â ]

## AUTHOR

Dwight Engen \<<dwight.engen@oracle.com>\>

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

[EXAMPLE](#lbAF)

:   

[NOTES](#lbAG)

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