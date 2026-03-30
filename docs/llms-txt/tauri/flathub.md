# Flathub

import { Tabs, TabItem, Card } from '@astrojs/starlight/components';

For detailed information on how Flatpak works, you can read [Building your first Flatpak](https://docs.flatpak.org/en/latest/first-build.html)

This guide assumes you want to distribute your Flatpak via [Flathub](https://flathub.org/), the most commonly used platform for Flatpak distribution. If you plan on using other platforms, please consult their documentation instead.

## Prerequisites

To test your app inside the Flatpak runtime you can build the Flatpak locally first before uploading your app to Flathub. This can also be helpful if you want to quickly share development builds.

**1. Install `flatpak` and `flatpak-builder`**

To build Flatpaks locally you need the `flatpak` and `flatpak-builder` tools. For example on Ubuntu you can run this command:

<Tabs syncKey="distro">
  <TabItem label="Debian">

```sh
sudo apt install flatpak flatpak-builder
```

  </TabItem>
  <TabItem label="Arch">

```sh
sudo pacman -S --needed flatpak flatpak-builder
```

  </TabItem>
  <TabItem label="Fedora">

```sh
sudo dnf install flatpak flatpak-builder
```

  </TabItem>
  <TabItem label="Gentoo">

```sh
sudo emerge --ask \
sys-apps/flatpak \
dev-util/flatpak-builder
```

  </TabItem>
</Tabs>

**2. Install the Flatpak Runtime**

```shell
flatpak install flathub org.gnome.Platform//46 org.gnome.Sdk//46
```

**3. [Build the .deb of your tauri-app](https://v2.tauri.app/reference/config/#bundleconfig)**

**4. [Create an AppStream MetaInfo file](https://www.freedesktop.org/software/appstream/metainfocreator/#/guiapp)**

**5. Create the flatpak manifest**

```yaml