# Ratio Plugin Documentation

The Ratio plugin enables convenient management of ratio limits for torrent groups in ruTorrent.

## Features

- Configure ratio groups with customizable parameters
- Automatic torrent management based on ratio
- Integration with rtorrent 0.8.5+ native ratio groups
- GUI for defining seed termination rules

## Parameters

| Parameter | Description |
|-----------|-------------|
| Min % | Minimum ratio before action triggers |
| Max % | Maximum ratio to maintain |
| UL (Mb) | Upload threshold in megabytes |
| Time (h) | Time threshold in hours |

## Actions

When a ratio group's conditions are met:

| Action | Description |
|--------|-------------|
| Stop | Stop the torrent |
| Remove | Remove the torrent |
| Stop+Cleanup | Stop and delete data files |

## Configuration

Edit `plugins/ratio/conf.php`:

```php
<?php
// Maximum ratio (0-100)
define('MAX_RATIO', 100);

// Default ratio group settings
$ratioGroupDefault = [
    'name' => 'Default',
    'min_ratio' => 100,      // Minimum ratio (%)
    'max_ratio' => 150,      // Maximum ratio (%)
    'min_upload' => 0,        // Minimum upload (MB), 0 = disabled
    'min_time' => 72,        // Minimum seeding time (hours), 0 = disabled
    'action' => 'stop'       // stop, remove, or stop_cleanup
];
?>
```

## Usage

### Creating Ratio Groups

1. Go to Settings > Ratio
2. Create new ratio group
3. Set parameters:
   - **Min ratio**: Start monitoring at this ratio
   - **Max ratio**: Stop at this ratio
   - **Upload threshold**: Trigger after uploading X MB
   - **Time threshold**: Trigger after seeding X hours

### Assigning Torrents

1. Right-click on torrent
2. Select "Ratio Group"
3. Choose appropriate group

## Requirements

- rtorrent 0.8.5 or later
- seedingtime plugin for time-based ratio features

## Setup Note

- Groups are created on first ruTorrent startup
- rtorrent config may need manual setup for immediate operation:

```bash
# In .rtorrent.rc
method.set = group.seeding.ratio.command, d.stop
```
