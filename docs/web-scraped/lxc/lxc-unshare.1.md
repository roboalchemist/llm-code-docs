# Source: https://linuxcontainers.org/lxc/manpages/man1/lxc-unshare.1.html

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
    -   [æ---¥æœ¬èªž](/ja/lxc/manpages//man1/lxc-unshare.1.html)
    -   [Deutsch](/de/lxc/manpages//man1/lxc-unshare.1.html)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/manpages//man1/lxc-unshare.1.html)
    -   [Indonesia](/id/lxc/manpages//man1/lxc-unshare.1.html)
    -   [FranÃ§ais](/fr/lxc/manpages//man1/lxc-unshare.1.html)

-   LXC
-   Manpages
-   lxc-unshare.1

Man page of lxc-unshare

# lxc-unshare

Section: (1)\
Updated: 2021-06-03\
[Index](#index) [Return to Main Contents](../index.html)

------------------------------------------------------------------------

[Â ]

## NAME

lxc-unshare - Run a task in a new set of namespaces. [Â ]

## SYNOPSIS

**lxc-unshare**  \[-u, \--user *user*\] \[-H, \--hostname *hostname*\] \[-i, \--ifname *ifname*\] \[-d, \--daemon\] \[-M, \--remount\]  [Â ]

## DESCRIPTION

**lxc-unshare** can be used to run a task in a cloned set of namespaces. This command is mainly provided for testing purposes. Despite its name, it always uses clone rather than unshare to create the new task with fresh namespaces. Apart from testing kernel regressions this should make no difference. [Â ]

## OPTIONS

**-s, \--namespaces** *namespaces*
:   Specify the namespaces to attach to, as a pipe-separated list, e.g. *NETWORK\|IPC*. Allowed values are *MOUNT*, *PID*, *UTSNAME*, *IPC*, *USER* and *NETWORK*. This allows one to change the context of the process to e.g. the network namespace of the container while retaining the other namespaces as those of the host. (The pipe symbol needs to be escaped, e.g. *MOUNT\\\|PID* or quoted, e.g. *\"MOUNT\|PID\"*.)

**-u, \--user** *user*
:   Specify a userid which the new task should become.

**-H, \--hostname** *hostname*
:   Set the hostname in the new container. Only allowed if the UTSNAME namespace is set.

**-i, \--ifname** *interfacename*
:   Move the named interface into the container. Only allowed if the NETWORK namespace is set. You may specify this argument multiple times to move multiple interfaces into container.

**-d, \--daemon**
:   Daemonize (do not wait for the container to exit before exiting)

**-M, \--remount**
:   Mount default filesystems (/proc /dev/shm and /dev/mqueue) in the container. Only allowed if MOUNT namespace is set.

[Â ]

## EXAMPLES

To spawn a new shell with its own UTS (hostname) namespace,

              lxc-unshare -s UTSNAME /bin/bash
            

If the hostname is changed in that shell, the change will not be reflected on the host.

To spawn a shell in a new network, pid, and mount namespace,

              lxc-unshare -s "NETWORK|PID|MOUNT" /bin/bash
            

The resulting shell will have pid 1 and will see no network interfaces. After re-mounting /proc in that shell,

              mount -t proc proc /proc
            

ps output will show there are no other processes in the namespace.

To spawn a shell in a new network, pid, mount, and hostname namespace.

              lxc-unshare -s "NETWORK|PID|MOUNT|UTSNAME" -M -H myhostname -i veth1 /bin/bash
            

The resulting shell will have pid 1 and will see two network interfaces (lo and veth1). The hostname will be \"myhostname\" and /proc will have been remounted. ps output will show there are no other processes in the namespace. [Â ]

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