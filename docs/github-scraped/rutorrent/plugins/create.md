# Create Plugin Documentation

The Create plugin enables creation of new .torrent files from files or directories.

## Usage

1. Click the **"Create Torrent..."** icon in the toolbar
2. Opens "Create New Torrent" window
3. Add a file or directory source
4. Fill in tracker information (announce URL)
5. Optionally select a piece size
6. Check "Start seeding" to add immediately
7. Check "Private Torrent" for private trackers
8. Click **"Create..."**
9. Monitor progress in Console window
10. Download the finished .torrent by clicking **"Save"**

## Features

- Create torrents from single files or entire directories
- Multiple tracker support
- Configurable piece size
- Private torrent flag
- Automatic seeding option
- Recent tracker history

## Configuration

Edit `plugins/create/conf.php`:

### $useExternal

Set to desired external program or `false` to use internal implementation:

```php
$useExternal = false;  // Use built-in creator
$useExternal = 'mktorrent';  // Use external program
```

### Supported External Programs

| Program | Notes |
|---------|-------|
| `mktorrent` | Recommended for 64-bit systems |
| `createtorrent` | Part of ktorrent |
| `transmissioncli` | Part of Transmission |
| `transmissioncreate` | Part of Transmission CLI |
| `buildtorrent` | Alternative option |

### $pathToCreatetorrent

Path to external program. If empty, searches PATH:

```php
$pathToCreatetorrent = '/usr/local/bin/mktorrent';
```

### $recentTrackersMaxCount

Controls how many recent trackers are remembered:

```php
$recentTrackersMaxCount = 15;
```

## External Program Installation

### mktorrent (Recommended)

```bash
# Debian/Ubuntu
apt-get install mktorrent

# Compile from source
wget https://github.com/Rudde/mktorrent/releases
tar -xzf mktorrent-*.tar.gz
cd mktorrent-*
make
sudo make install
```

### buildtorrent

```bash
# Compile
git clone https://github.com/mgduda/buildtorrent.git
cd buildtorrent
make
sudo make install
```

## Piece Size Guidelines

| Data Size | Recommended Piece Size |
|-----------|----------------------|
| < 512 MB | 32 KB |
| 512 MB - 1 GB | 64 KB |
| 1 GB - 4 GB | 128 KB |
| 4 GB - 8 GB | 256 KB |
| > 8 GB | 512 KB |

## Private Torrents

Enable the "Private Torrent" checkbox for:

- Private trackers requiring passkey
- Private trackers that don't allow DHT
- Trackers that verify peer sources

## Troubleshooting

### "External program not found"

1. Install the external program
2. Set full path in configuration
3. Ensure web server user can execute it

### Large Torrent Creation Fails

- Use external program on 64-bit systems
- Increase PHP memory limit
- Use larger piece sizes

### Permissions Error

```bash
chmod +x /usr/local/bin/mktorrent
chown www-data:www-data /usr/local/bin/mktorrent
```
