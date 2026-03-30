# ruTorrent Installation Guide

## Overview

This guide covers installing rtorrent (the backend Bittorrent client) and ruTorrent (the web frontend).

## Part 1: Install rtorrent

### Quick Installation (Package Manager)

For most distributions, rtorrent is available via package manager:

```bash
# Debian/Ubuntu
apt-get update
apt-cache show rtorrent | grep Version  # Check available version
apt-get install rtorrent

# FreeBSD
cd /usr/ports/net-p2p/rtorrent/ && make install clean
```

**Requirements:** rtorrent 0.8.5+ with xmlrpc-c support (most distro packages include this since 0.7.8)

### Compile from Source (Advanced)

Only for users needing the latest version or custom compilation.

#### Dependencies

```bash
# Install build dependencies
# - gcc
# - ncurses
# - libsigc++-2.0
# - libssl
# - xmlrpc-c (with i8 support, version >= 1.11)
```

#### Build xmlrpc-c

```bash
svn co http://svn.code.sf.net/p/xmlrpc-c/code/stable xmlrpc-c
cd xmlrpc-c
./configure
make
make install
```

#### Build libtorrent

```bash
cd ~
wget http://rtorrent.net/downloads/libtorrent-0.13.8.tar.gz
tar -zxvf libtorrent-0.13.8.tar.gz
cd libtorrent-0.13.8
bash autogen.sh
./configure
make
make install
```

#### Build rtorrent

```bash
cd ~
wget http://rtorrent.net/downloads/rtorrent-0.9.8.tar.gz
tar -zxvf rtorrent-0.9.8.tar.gz
cd rtorrent-0.9.8
bash autogen.sh
./configure --with-xmlrpc-c
make
make install
```

## Part 2: Configure rtorrent

### Create Configuration File

Download the official template:

```bash
curl -Ls "https://raw.githubusercontent.com/wiki/rakshasa/rtorrent/CONFIG-Template.md" \
    | sed -ne "/^######/,/^### END/p" \
    | sed -re "s:/home/USERNAME:$HOME:" >~/.rtorrent.rc
mkdir -p ~/rtorrent/
```

**Important:** Do not run rtorrent as root. Create a dedicated user.

### Enable RPC Socket

Add these lines to `.rtorrent.rc` to enable the RPC socket:

```ini
system.daemon.set = false
network.scgi.open_local = (cat,(session.path),rpc.socket)
execute.nothrow = chmod,770,(cat,(session.path),rpc.socket)
```

The RPC socket will be at `~/rtorrent/.session/rpc.socket`

### Alternative: SCGI Port

For older configurations using a port instead of socket:

```ini
network.scgi.open_port = 127.0.0.1:5000
```

## Part 3: Install ruTorrent

### Download

```bash
# Development version
wget https://github.com/Novik/ruTorrent/tarball/master -O rutorrent.tar.gz
tar -xzf rutorrent.tar.gz
mv Novik-ruTorrent-* /var/www/rutorrent

# Or clone stable release
wget https://github.com/Novik/ruTorrent/releases -O rutorrent.tar.gz
```

### Set Permissions

```bash
# Web server user ownership (adjust for your setup)
chown -R www-data:www-data /var/www/rutorrent

# Session directory
mkdir -p /var/www/rutorrent/share/.session
chown -R www-data:www-data /var/www/rutorrent/share
chmod -R 755 /var/www/rutorrent
```

### Configure ruTorrent

1. Copy the configuration template:

   ```bash
   cd /var/www/rutorrent
   cp conf/access.ini -p conf/access.ini.bak
   ```

2. Edit `conf/config.php` with your settings (see [Configuration Reference](configuration.md))

3. Set up web server authentication if needed

## Part 4: Running rtorrent

### Test Mode (Interactive)

```bash
rtorrent
```

### Daemon Mode (Background)

Set `system.daemon.set = true` in `.rtorrent.rc`, then:

```bash
daemonize $(which rtorrent)
```

### Systemd Service (Recommended)

Create `/etc/systemd/system/rtorrent@.service`:

```ini
[Unit]
Description=rtorrent (bt) client
After=network.target

[Service]
Type=forking
User=%I
KillMode=none
ExecStart=/usr/bin/daemonize /usr/bin/rtorrent
ExecStop=/usr/bin/killall rtorrent
WorkingDirectory=%h

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
systemctl enable rtorrent@<username>
systemctl start rtorrent@<username>
```

## Next Steps

- [Configure Web Server](webserver.md) - Set up Apache, Nginx, Lighttpd, or Cherokee
- [Configure ruTorrent](configuration.md) - Edit config.php settings
- [Set Up Plugins](plugins/) - Install and configure plugins
