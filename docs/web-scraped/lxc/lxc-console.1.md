# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-console.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-console.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-console.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-console.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-console.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-console.1.html)

-   LXC
-   Manpages
-   lxc-console.1

Man page of lxc-console

# lxc-console

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-console - Launch a console for the specified container [Â ]

## SYNOPSIS

**lxc-console**  \[-e *escape character*\] \[-t *ttynum*\] [Â ]

## DESCRIPTION

If the tty service has been configured and is available for the container specified as parameter, this command will launch a console allowing to log on the container.

The available tty are free slots taken by this command. That means if the container has four ttys available and the command has been launched four times each taking a different tty, the fifth command will fail because no console will be available.

The command will connect to a tty. If the connection is lost or broken, the command can be launched again and regain the tty at the state it was before the disconnection.

A *ttynum* of 0 may be given to attach to the container\'s /dev/console instead of its dev/tty\<*ttynum*\>.

A keyboard escape sequence may be used to disconnect from the tty and quit lxc-console. The default escape sequence is \<Ctrl+a q\>. [Â ]

## OPTIONS

**-e, \--escape** *escape character*
:   Specify the escape sequence prefix to use instead of \<Ctrl a\>. This may be given as \'\^letter\' or just \'letter\'. For example to use \<Ctrl+b q\> as the escape sequence use -e \'\^b\'.

**-t, \--tty** *ttynum*
:   Specify the tty number to connect to or 0 for the console. If not specified the next available tty number will be automatically chosen by the container.

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

tty service denied
:   No tty is available or there is not enough privilege to use the console. For example, the container belongs to user \"foo\" and \"bar\" is trying to open a console to it.

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