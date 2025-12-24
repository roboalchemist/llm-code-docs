# Source: https://headscale.net/stable/setup/install/source/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/setup/install/source.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/setup/install/source.md "View source of this page")

# Build from source[¶](#build-from-source "Permanent link")

Community documentation

This page is not actively maintained by the headscale authors and is written by community members. It is *not* verified by headscale developers.

**It might be outdated and it might miss necessary steps**.

Headscale can be built from source using the latest version of [Go](https://golang.org) and [Buf](https://buf.build) (Protobuf generator). See the [Contributing section in the GitHub README](https://github.com/juanfont/headscale#contributing) for more information.

## OpenBSD[¶](#openbsd "Permanent link")

### Install from source[¶](#install-from-source "Permanent link")

    # Install prerequisites
    pkg_add go git

    git clone https://github.com/juanfont/headscale.git

    cd headscale

    # optionally checkout a release
    # option a. you can find official release at https://github.com/juanfont/headscale/releases/latest
    # option b. get latest tag, this may be a beta release
    latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)

    git checkout $latestTag

    go build -ldflags="-s -w -X github.com/juanfont/headscale/hscontrol/types.Version=$latestTag" -X github.com/juanfont/headscale/hscontrol/types.GitCommitHash=HASH" github.com/juanfont/headscale

    # make it executable
    chmod a+x headscale

    # copy it to /usr/local/sbin
    cp headscale /usr/local/sbin

### Install from source via cross compile[¶](#install-from-source-via-cross-compile "Permanent link")

    # Install prerequisites
    # 1. go v1.20+: headscale newer than 0.21 needs go 1.20+ to compile
    # 2. gmake: Makefile in the headscale repo is written in GNU make syntax

    git clone https://github.com/juanfont/headscale.git

    cd headscale

    # optionally checkout a release
    # option a. you can find official release at https://github.com/juanfont/headscale/releases/latest
    # option b. get latest tag, this may be a beta release
    latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)

    git checkout $latestTag

    make build GOOS=openbsd

    # copy headscale to openbsd machine and put it in /usr/local/sbin