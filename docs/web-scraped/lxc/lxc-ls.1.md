# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-ls.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-ls.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-ls.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-ls.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-ls.1.html)

-   LXC
-   Manpages
-   lxc-ls.1

Man page of lxc-ls

# lxc-ls

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-ls - list the containers existing on the system [Â ]

## SYNOPSIS

**lxc-ls** \[-1\] \[\--active\] \[\--frozen\] \[\--running\] \[\--stopped\] \[\--defined\] \[-f\] \[-F *format*\] \[-g *groups*\] \[\--nesting=*NUM*\] \[\--filter=*regex*\] [Â ]

## DESCRIPTION

**lxc-ls** list the containers existing on the system. [Â ]

## OPTIONS

**-1**
:   Show one entry per line. (default when /dev/stdout isn\'t a tty)

**\--active**
:   List only active containers (same as \--frozen \--running).

**\--frozen**
:   List only frozen containers.

**\--running**
:   List only running containers.

**\--stopped**
:   List only stopped containers.

**\--defined**
:   List only defined containers.

**-f,\--fancy**
:   Use a fancy, column-based output.

**-F,\--fancy-format** *format*
:   Comma separated list of columns to show in the fancy output. The list of accepted and default fields is listed in \--help.

**-g,\--groups** *groups*
:   Comma separated list of groups the container must have to be displayed. The parameter may be passed multiple times.

**\--nesting=***NUM*
:   Show nested containers. The number of nesting levels to be shown can be specified by passing a number as argument.

**\--filter=***regex*
:   The regular expression passed to **lxc-ls** will be applied to the container name. The format is a POSIX extended regular expression. It can also be given as additional argument without explicitly using **\--filter**.

[Â ]

## EXAMPLES

lxc-ls \--fancy
:   list all the containers, listing one per line along with its name, state, ipv4 and ipv6 addresses.

lxc-ls \--active -1
:   list active containers and display the list in one column.

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

## SEE ALSO

**[lxc](../man7/lxc.7.html)**(7), **[lxc-create](../man1/lxc-create.1.html)**(1), **[lxc-copy](../man1/lxc-copy.1.html)**(1), **[lxc-destroy](../man1/lxc-destroy.1.html)**(1), **[lxc-start](../man1/lxc-start.1.html)**(1), **[lxc-stop](../man1/lxc-stop.1.html)**(1), **[lxc-execute](../man1/lxc-execute.1.html)**(1), **[lxc-console](../man1/lxc-console.1.html)**(1), **[lxc-monitor](../man1/lxc-monitor.1.html)**(1), **[lxc-wait](../man1/lxc-wait.1.html)**(1), **[lxc-cgroup](../man1/lxc-cgroup.1.html)**(1), **[lxc-ls](../man1/lxc-ls.1.html)**(1), **[lxc-info](../man1/lxc-info.1.html)**(1), **[lxc-freeze](../man1/lxc-freeze.1.html)**(1), **[lxc-unfreeze](../man1/lxc-unfreeze.1.html)**(1), **[lxc-attach](../man1/lxc-attach.1.html)**(1), **[lxc.conf](../man5/lxc.conf.5.html)**(5) [Â ]

## HISTORY

Written originally as a shell script by Daniel Lezcano and Serge Hallyn. Later reimplemented and extended in Python by StÃ©phane Graber and then reimplemented and extended in C by Christian Brauner. [Â ]

## AUTHOR

Christian Brauner \<<christian.brauner@mailbox.org>\>, StÃ©phane Graber \<<stgraber@ubuntu.com>\>

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

[COMMON OPTIONS](#lbAG)

:   

[SEE ALSO](#lbAH)

:   

[HISTORY](#lbAI)

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