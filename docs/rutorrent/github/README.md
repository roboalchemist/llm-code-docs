# ruTorrent - Web Frontend for rtorrent

ruTorrent is a front-end for the popular Bittorrent client [rtorrent](http://rakshasa.github.io/rtorrent). It provides a web-based interface for managing torrents with features similar to uTorrent.

## Features

- **Lightweight server side** - Can run on old/low-end servers and some SOHO routers
- **Extensible** - Many plugins available with easy custom plugin creation
- **Web-based** - Access from any browser, including mobile devices
- **Multi-user support** - User access levels and permissions
- **RSS support** - Built-in RSS feed fetching with automatic downloads
- **Plugin ecosystem** - 50+ official plugins for additional functionality

## Quick Start

1. **Install rtorrent** (requires xmlrpc-c support)
2. **Configure web server** (Apache, Nginx, Lighttpd, or Cherokee)
3. **Set up ruTorrent** - Clone to web server document root
4. **Configure access** - Set up `config.php` and permissions

See [Installation Guide](docs/installation.md) for detailed setup instructions.

## Documentation Sections

| Section | Description |
|---------|-------------|
| [Installation](docs/installation.md) | Detailed installation for rtorrent and ruTorrent |
| [Web Server Configuration](docs/webserver.md) | Apache, Nginx, Lighttpd, Cherokee setup |
| [Configuration Reference](docs/configuration.md) | All config.php parameters |
| [Usage Guide](docs/usage.md) | Interface and controls |
| [Troubleshooting](docs/troubleshooting.md) | Error messages and solutions |
| [Version History](docs/versions.md) | Release notes and changelog |
| [Plugins](plugins/README.md) | Plugin documentation |

## Core Plugins

| Plugin | Description |
|--------|-------------|
| [_cloudflare](plugins/cloudflare.md) | CloudFlare support |
| [_getdir](plugins/getdir.md) | Directory browser |
| [_task](plugins/task.md) | Task management framework |
| [_noty](plugins/noty.md) | Notification system (v1) |
| [_noty2](plugins/noty2.md) | Notification system (v2) |

## Download Management Plugins

| Plugin | Description |
|--------|-------------|
| [Data](plugins/data.md) | File management |
| [Diskspace](plugins/diskspace.md) | Disk space monitoring |
| [Erasedata](plugins/erasedata.md) | Secure data deletion |

## RSS and Search Plugins

| Plugin | Description |
|--------|-------------|
| [RSS](plugins/rss.md) | RSS feed management with filters |
| [RSSURLRewrite](plugins/rssurlrewrite.md) | RSS URL rewriting |
| [ExtSearch](plugins/extsearch.md) | Multi-site torrent searching |
| [Rutracker_check](plugins/rutracker_check.md) | Rutracker status checking |

## Upload and Sharing Plugins

| Plugin | Description |
|--------|-------------|
| [Create](plugins/create.md) | Create .torrent files |
| [Unpack](plugins/unpack.md) | Automatic archive extraction |
| [FileDrop](plugins/filedrop.md) | Drag-and-drop file upload |

## Ratio and Seeding Plugins

| Plugin | Description |
|--------|-------------|
| [Ratio](plugins/ratio.md) | Ratio group management |
| [ExtRatio](plugins/extratio.md) | Extended ratio features |
| [Scheduler](plugins/scheduler.md) | Time-based behavior scheduling |
| [SeedingTime](plugins/seedingtime.md) | Seeding time tracking |
| [Throttle](plugins/throttle.md) | Channel-based speed limits |

## Monitoring and Statistics Plugins

| Plugin | Description |
|--------|-------------|
| [GeoIP](plugins/geoip.md) | Peer geolocation |
| [History](plugins/history.md) | Torrent history logging |
| [Traffic](plugins/traffic.md) | Traffic statistics |
| [cpuload](plugins/cpuload.md) | CPU load display |
| [LookAt](plugins/lookat.md) | Process monitoring |
| [Mediainfo](plugins/mediainfo.md) | Media file information |

## Interface Enhancement Plugins

| Plugin | Description |
|--------|-------------|
| [Theme](plugins/theme.md) | Custom theming |
| [AutoTools](plugins/autotools.md) | Automated labeling and file operations |
| [IPad](plugins/ipad.md) | iPad optimization |
| [LoginMgr](plugins/loginmgr.md) | Tracker authentication management |

## Requirements

- **rtorrent** 0.8.5+ with xmlrpc-c support
- **Web server** (Apache, Nginx, Lighttpd, Cherokee)
- **PHP** 5.1+ with:
  - mbstring extension
  - curl extension (for some plugins)
  - PCRE support

## Screenshots

![ruTorrent Interface](https://github.com/Novik/ruTorrent/wiki/images/scr1_small.jpg)
![Torrent Details](https://github.com/Novik/ruTorrent/wiki/images/scr2_small.jpg)
![Multi-torrent View](https://github.com/Novik/ruTorrent/wiki/images/scr3_small.jpg)

## License

ruTorrent is released under the [GPLv3 license](LICENSE.md).

## Download

- **Development version**: [tarball](https://github.com/Novik/ruTorrent/tarball/master)
- **Stable releases**: [GitHub Releases](https://github.com/Novik/ruTorrent/releases)

## Links

- [Official GitHub Repository](https://github.com/Novik/ruTorrent)
- [GitHub Wiki](https://github.com/Novik/ruTorrent/wiki)
- [rtorrent Documentation](https://github.com/rakshasa/rtorrent/wiki)
