# Source: https://headscale.net/stable/setup/install/community/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/setup/install/community.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/setup/install/community.md "View source of this page")

# Community packages[¶](#community-packages "Permanent link")

Several Linux distributions and community members provide packages for headscale. Those packages may be used instead of the [official releases](../official/) provided by the headscale maintainers. Such packages offer improved integration for their targeted operating system and usually:

- setup a dedicated local user account to run headscale
- provide a default configuration
- install headscale as system service

Community packages might be outdated

The packages mentioned on this page might be outdated or unmaintained. Use the [official releases](../official/) to get the current stable version or to test pre-releases.

[![Packaging status](https://repology.org/badge/vertical-allrepos/headscale.svg)](https://repology.org/project/headscale/versions)

## Arch Linux[¶](#arch-linux "Permanent link")

Arch Linux offers a package for headscale, install via:

    pacman -S headscale

The [AUR package `headscale-git`](https://aur.archlinux.org/packages/headscale-git) can be used to build the current development version.

## Fedora, RHEL, CentOS[¶](#fedora-rhel-centos "Permanent link")

A third-party repository for various RPM based distributions is available at: <https://copr.fedorainfracloud.org/coprs/jonathanspw/headscale/>. The site provides detailed setup and installation instructions.

## Nix, NixOS[¶](#nix-nixos "Permanent link")

A Nix package is available as: `headscale`. See the [NixOS package site for installation details](https://search.nixos.org/packages?show=headscale).

## Gentoo[¶](#gentoo "Permanent link")

    emerge --ask net-vpn/headscale

Gentoo specific documentation is available [here](https://wiki.gentoo.org/wiki/User:Maffblaster/Drafts/Headscale).

## OpenBSD[¶](#openbsd "Permanent link")

Headscale is available in ports. The port installs headscale as system service with `rc.d` and provides usage instructions upon installation.

    pkg_add headscale