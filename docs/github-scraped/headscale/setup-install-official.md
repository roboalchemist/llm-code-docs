# Source: https://headscale.net/stable/setup/install/official/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/setup/install/official.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/setup/install/official.md "View source of this page")

# Official releases[¶](#official-releases "Permanent link")

Official releases for headscale are available as binaries for various platforms and DEB packages for Debian and Ubuntu. Both are available on the [GitHub releases page](https://github.com/juanfont/headscale/releases).

## Using packages for Debian/Ubuntu (recommended)[¶](#using-packages-for-debianubuntu-recommended "Permanent link")

It is recommended to use our DEB packages to install headscale on a Debian based system as those packages configure a local user to run headscale, provide a default configuration and ship with a systemd service file. Supported distributions are Ubuntu 22.04 or newer, Debian 12 or newer.

1.  Download the [latest headscale package](https://github.com/juanfont/headscale/releases/latest) for your platform (`.deb` for Ubuntu and Debian).

    ::: 
        HEADSCALE_VERSION="" # See above URL for latest version, e.g. "X.Y.Z" (NOTE: do not add the "v" prefix!)
        HEADSCALE_ARCH="" # Your system architecture, e.g. "amd64"
        wget --output-document=headscale.deb \
         "https://github.com/juanfont/headscale/releases/download/v$/headscale_$_linux_$.deb"
    :::

2.  Install headscale:

    ::: 
        sudo apt install ./headscale.deb
    :::

3.  [Configure headscale by editing the configuration file](../../../ref/configuration/):

    ::: 
        sudo nano /etc/headscale/config.yaml
    :::

4.  Enable and start the headscale service:

    ::: 
        sudo systemctl enable --now headscale
    :::

5.  Verify that headscale is running as intended:

    ::: 
        sudo systemctl status headscale
    :::

## Using standalone binaries (advanced)[¶](#using-standalone-binaries-advanced "Permanent link")

Advanced

This installation method is considered advanced as one needs to take care of the local user and the systemd service themselves. If possible, use the [DEB packages](#using-packages-for-debianubuntu-recommended) or a [community package](../community/) instead.

This section describes the installation of headscale according to the [Requirements and assumptions](../../requirements/#assumptions). Headscale is run by a dedicated local user and the service itself is managed by systemd.

1.  Download the latest [`headscale` binary from GitHub\'s release page](https://github.com/juanfont/headscale/releases):

    ::: 
        sudo wget --output-document=/usr/bin/headscale \
        https://github.com/juanfont/headscale/releases/download/v<HEADSCALE VERSION>/headscale_<HEADSCALE VERSION>_linux_<ARCH>
    :::

2.  Make `headscale` executable:

    ::: 
        sudo chmod +x /usr/bin/headscale
    :::

3.  Add a dedicated local user to run headscale:

    ::: 
        sudo useradd \
         --create-home \
         --home-dir /var/lib/headscale/ \
         --system \
         --user-group \
         --shell /usr/sbin/nologin \
         headscale
    :::

4.  Download the example configuration for your chosen version and save it as: `/etc/headscale/config.yaml`. Adjust the configuration to suit your local environment. See [Configuration](../../../ref/configuration/) for details.

    ::: 
        sudo mkdir -p /etc/headscale
        sudo nano /etc/headscale/config.yaml
    :::

5.  Copy [headscale\'s systemd service file](https://github.com/juanfont/headscale/blob/main/packaging/systemd/headscale.service) to `/etc/systemd/system/headscale.service` and adjust it to suit your local setup. The following parameters likely need to be modified: `ExecStart`, `WorkingDirectory`, `ReadWritePaths`.

6.  In `/etc/headscale/config.yaml`, override the default `headscale` unix socket with a path that is writable by the `headscale` user or group:

    ::: 
    [config.yaml]
        unix_socket: /var/run/headscale/headscale.sock
    :::

7.  Reload systemd to load the new configuration file:

    ::: 
        systemctl daemon-reload
    :::

8.  Enable and start the new headscale service:

    ::: 
        systemctl enable --now headscale
    :::

9.  Verify that headscale is running as intended:

    ::: 
        systemctl status headscale
    :::