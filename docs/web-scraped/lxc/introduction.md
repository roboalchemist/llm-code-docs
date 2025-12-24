# Source: https://linuxcontainers.org/lxc/introduction/

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
    -   [æ---¥æœ¬èªž](/ja/lxc/introduction/)
    -   [Deutsch](/de/lxc/introduction/)
    -   [ç®€ä½"ä¸­æ--‡](/zh-cn/lxc/introduction/)
    -   [Indonesia](/id/lxc/introduction/)
    -   [FranÃ§ais](/fr/lxc/introduction/)

-   LXC
-   Introduction

# What\'s LXC?[¶](#whats-lxc "Permanent link")

LXC is a userspace interface for the Linux kernel containment features. Through a powerful API and simple tools, it lets Linux users easily create and manage system or application containers.

# Features[¶](#features "Permanent link")

Current LXC uses the following kernel features to contain processes:

-   Kernel namespaces (ipc, uts, mount, pid, network and user)
-   Apparmor and SELinux profiles
-   Seccomp policies
-   Chroots (using pivot_root)
-   Kernel capabilities
-   CGroups (control groups)

LXC containers are often considered as something in the middle between a chroot and a full fledged virtual machine. The goal of LXC is to create an environment as close as possible to a standard Linux installation but without the need for a separate kernel.

# Components[¶](#components "Permanent link")

LXC is currently made of a few separate components:

-   The liblxc library
-   Several language bindings for the API:
    -   [python3](https://github.com/lxc/python3-lxc)
    -   [lua](https://github.com/lxc/lua-lxc)
    -   [Go](https://github.com/lxc/go-lxc)
    -   [ruby](https://github.com/lxc/ruby-lxc)
    -   [Haskell](https://github.com/fizruk/lxc)
-   A set of standard tools to control the containers
-   Distribution container templates

# Licensing[¶](#licensing "Permanent link")

LXC is free software, most of the code is released under the terms of the GNU LGPLv2.1+ license, some Android compatibility bits are released under a standard 2-clause BSD license and some binaries and templates are released under the GNU GPLv2 license.

The default license for the project is the GNU LGPLv2.1+.

# Support[¶](#support "Permanent link")

LXC\'s stable release support relies on the Linux distributions and their own commitment to pushing stable fixes and security updates.

Based on the needs and available resources from the various distributions, specific versions of LXC can enjoy long term support with frequent bugfix updates.

Other releases will typically be maintained on a best effort basis which typically means until the next stable release is out.

## Extended support[¶](#extended-support "Permanent link")

LXC 6.0 and 5.0 are long term support releases:

-   LXC 6.0 will be supported until June 1st 2029
-   LXC 5.0 will be supported until June 1st 2027

Project infrastructure sponsored by [Zabbly](https://zabbly.com).

-   [Improve this website](https://github.com/lxc/linuxcontainers.org)
-   [Back to top](#)
-   [Content under Creative Commons CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)