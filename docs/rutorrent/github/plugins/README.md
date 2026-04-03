# ruTorrent Plugin Documentation

Complete documentation for ruTorrent's official and third-party plugins.

## Plugin Categories

### Core Framework Plugins

Plugins that provide infrastructure for other plugins.

| Plugin | Description |
|--------|-------------|
| [_cloudflare](cloudflare.md) | CloudFlare support |
| [_getdir](getdir.md) | Directory browser |
| [_noty](noty.md) | Notification system (v1) |
| [_noty2](noty2.md) | Notification system (v2) |
| [_task](task.md) | Task management framework |

### Download Management Plugins

| Plugin | Description |
|--------|-------------|
| [Data](data.md) | File management |
| [DataDir](datadir.md) | Directory management |
| [Diskspace](diskspace.md) | Disk space monitoring |
| [Erasedata](erasedata.md) | Secure data deletion |

### Search and Discovery Plugins

| Plugin | Description |
|--------|-------------|
| [ExtSearch](extsearch.md) | Multi-site torrent searching |
| [RSS](rss.md) | RSS feed management |
| [RSSURLRewrite](rssurlrewrite.md) | RSS URL rewriting |
| [Rutracker_check](rutracker_check.md) | Rutracker status checking |

### Upload and Sharing Plugins

| Plugin | Description |
|--------|-------------|
| [Create](create.md) | Create .torrent files |
| [Unpack](unpack.md) | Automatic archive extraction |
| [FileDrop](filedrop.md) | Drag-and-drop file upload |
| [UploadETA](uploadeta.md) | ETA for uploads |

### Ratio and Seeding Plugins

| Plugin | Description |
|--------|-------------|
| [Ratio](ratio.md) | Ratio group management |
| [ExtRatio](extratio.md) | Extended ratio features |
| [Scheduler](scheduler.md) | Time-based behavior scheduling |
| [SeedingTime](seedingtime.md) | Seeding time tracking |

### Monitoring and Statistics Plugins

| Plugin | Description |
|--------|-------------|
| [GeoIP](geoip.md) | Peer geolocation |
| [History](history.md) | Torrent history logging |
| [Traffic](traffic.md) | Traffic statistics |
| [Chunks](chunks.md) | Chunk visualization |
| [cpuload](cpuload.md) | CPU load display |
| [LookAt](lookat.md) | Process monitoring |

### Interface Enhancement Plugins

| Plugin | Description |
|--------|-------------|
| [Theme](theme.md) | Custom theming |
| [IPad](ipad.md) | iPad optimization |
| [Show Peers Like Wtorrent](show_peers_like_wtorrent.md) | Peer display style |

---

## Plugin Installation

### Official Plugins

Most plugins are included in the ruTorrent package under `plugins/`. Enable in `conf/plugins.ini`:

```ini
[plugin_name]
enabled = yes
```

### Third-Party Plugins

Install third-party plugins by cloning to the `plugins/` directory:

```bash
cd /var/www/rutorrent/plugins
git clone https://github.com/user/plugin-name.git
chown -R www-data:www-data plugin-name
```

---

## Plugin Configuration

Each plugin may have a `conf.php` file for settings:

```php
// Example plugin configuration
<?php
$useExternal = true;
$pathToExternal = '/usr/bin/program';
$maxConnections = 10;
?>
```

---

## Plugin Development

### Basic Plugin Structure

```text
plugins/
  myplugin/
    conf.php        # Configuration
    init.php        # Initialization
    plugin.php      # Main plugin code
    lang/           # Language files
    images/         # Icons and images
```

### Plugin Hooks

Plugins can hook into various events:

| Hook | Description |
|------|-------------|
| `view.phtml` | Modify view display |
| `system.index` | Add to index page |
| `rpc.callback` | Handle RPC calls |
| `torrent.added` | Torrent added event |

---

## Third-Party Plugins Overview

### Popular Third-Party Plugins

| Plugin | Repository |
|--------|------------|
| NFO Viewer | Micdu70/plugin-nfo-ruTorrent |
| Mobile UI | xombiemp/rutorrentMobile |
| File Manager | nelu/rutorrent-filemanager |
| Media Player | nelu/rutorrent-filemanager-media |
| File Upload | nelu/rutorrent-thirdparty-plugins |
| File Share | nelu/rutorrent-filemanager-share |
| Sync | ArthurJam/ruTorrent-plugin-sync |
| AutoDL-irssi | plugin-autodl-irssi |
