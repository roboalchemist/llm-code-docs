# Snapcraft

## Prerequisites

import { Tabs, TabItem, Card } from '@astrojs/starlight/components';

**1. Install `snap`**

{/* prettier-ignore */}
<Tabs syncKey="distro">
  <TabItem label="Debian">
    ```shell
    sudo apt install snapd
    ```
  </TabItem>
  <TabItem label="Arch">
    ```shell
    sudo pacman -S --needed git base-devel
    git clone https://aur.archlinux.org/snapd.git
    cd snapd
    makepkg -si
    sudo systemctl enable --now snapd.socket
    sudo systemctl start snapd.socket
    sudo systemctl enable --now snapd.apparmor.service
    ```
  </TabItem>
  <TabItem label="Fedora">
    ```shell
    sudo dnf install snapd
    # Enable classic snap support
    sudo ln -s /var/lib/snapd/snap /snap
    ```

    Reboot your system afterwards.

  </TabItem>
</Tabs>

**2. Install a base snap**

```shell
sudo snap install core22
```

**3. Install `snapcraft`**

```shell
sudo snap install snapcraft --classic
```

## Configuration

1. Create an UbuntuOne account.
2. Go to the [Snapcraft](https://snapcraft.io) website and register an App name.
3. Create a snapcraft.yaml file in your projects root.
4. Adjust the names in the snapcraft.yaml file.

```yaml
name: appname
base: core22
version: '0.1.0'
summary: Your summary # 79 char long summary
description: |
  Your description

grade: stable
confinement: strict

layout:
  /usr/lib/$SNAPCRAFT_ARCH_TRIPLET/webkit2gtk-4.1:
    bind: $SNAP/usr/lib/$SNAPCRAFT_ARCH_TRIPLET/webkit2gtk-4.1

apps:
  appname:
    command: usr/bin/appname
    desktop: usr/share/applications/appname.desktop
    extensions: [gnome]
    #plugs:
    #  - network
    # Add whatever plugs you need here, see https://snapcraft.io/docs/snapcraft-interfaces for more info.
    # The gnome extension already includes [ desktop, desktop-legacy, gsettings, opengl, wayland, x11, mount-observe, calendar-service ]
    #  - single-instance-plug # add this if you're using the single-instance plugin
    #slots:
    # Add the slots you need to expose to other snaps
    #  - single-instance-plug # add this if you're using the single-instance plugin