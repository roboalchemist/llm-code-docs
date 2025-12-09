# Source: https://rustdesk.com/docs/en/client/linux/

# Linux

## Installation

### Ubuntu (â¥ 18)

```
# please ignore the wrong disk usage report
sudo apt install -fy ./rustdesk-<version>.deb
```

For Ubuntu 18.04, please do below first for pipewire.

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:pipewire-debian/pipewire-upstream
sudo apt update
```

### CentOS/Fedora (â¥ 28)

```
sudo yum localinstall ./rustdesk-<version>.rpm
```

### Arch Linux/Manjaro

```
sudo pacman -U ./rustdesk-<version>.pkg.tar.zst
```

### openSUSE (â¥ Leap 15.0)

```
sudo zypper install --allow-unsigned-rpm ./rustdesk-<version>-suse.rpm
```

### AppImage

```
# For Fedora
sudo yum install libnsl
./rustdesk-<version>.AppImage
```

```
# For Ubuntu
sudo yum install libfuse2
./rustdesk-<version>.AppImage
```

### Flatpak

```
flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak --user install ./rustdesk-<version>.flatpak
flatpak run com.rustdesk.RustDesk
```

## X11 Required

RustDesk does not support Wayland yet; you need switch to X11 manually.

RustDesk now has experimental Wayland support since version 1.2.0.

### Display Server

Ubuntu |
Fedora |
[Arch Linux](https://bbs.archlinux.org/viewtopic.php?id=218319)

### Login Screen

Login screen using Wayland is not supported yet. If you wanna access login screen after reboot or logout with RustDesk, you need to change login screen to X11, please modify below line to `WaylandEnable=false` in `/etc/gdm/custom.conf` or `/etc/gdm3/custom.conf`:

```
#WaylandEnable=false
```

Note

Please **reboot** to make above changes taking effect.

### Permissions Issue

If SELinux is enabled, RustDesk will not work properly in either X11 or Wayland environments, related [issues](https://github.com/search?q=repo%3Arustdesk%2Frustdesk+SElinux&type=issues).

You can run:

```
$ sudo grep 'comm=&#34;rustdesk&#34;' /var/log/audit/audit.log | tail -1
type=AVC msg=audit(1697902459.165:707): avc:  denied  { name_connect } for  pid=31346 comm=&#34;rustdesk&#34; dest=53330 scontext=system_u:system_r:init_t:s0 tcontext=system_u:object_r:ephemeral_port_t:s0 tclass=tcp_socket permissive=0
```

Note

The number in parentheses after `audit` is timestamp.

If the output contains `avc: denied`, you need to add SELinux policies, please refer to SELinux.