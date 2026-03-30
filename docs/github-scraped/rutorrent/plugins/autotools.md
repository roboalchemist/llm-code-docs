# AutoTools Plugin Documentation

The AutoTools plugin provides automation capabilities for ruTorrent with three main functions.

## Features

### Auto Label

Automatically creates labels when adding new torrents through the web interface.

**Template Variables:**

| Variable | Description |
|----------|-------------|
| `{DIR}` | Directory path relative to rtorrent.rc |
| `{TRACKER}` | Tracker name |
| `{NOW}` | Current date |
| `{NOW:format}` | Date with strftime format (e.g., `{NOW:%Y-%m-%d}`) |

**Configuration:**

- Labels are generated from templates set in plugin options
- Created automatically if label field is empty

### Auto Move

Transfers completed torrent data files to a configured directory.

**Behavior:**

- Preserves original directory structure
- After transfer, searches for `.mailto` file
- Sends optional email notifications about completed downloads

**Requirements:**

- `_getdir` plugin for convenient directory selection
- External move program (mv command)

### Auto Watch

Monitors nested subdirectories for new .torrent files.

**Behavior:**

- Automatically adds torrents to rtorrent
- Downloads to corresponding directories based on rtorrent.rc configuration
- Supports nested subdirectory monitoring

## Additional Features

- Handles multiple torrents sharing a data directory correctly
- Existing files with matching names in destination are overwritten
- Integration with rtorrent occurs at web interface loading
- Recommended: reinstall `_getdir` plugin for convenient directory navigation

## Configuration

Edit `plugins/_autotools/conf.php`:

```php
<?php
// Auto Label settings
$autolabel.enable = true;
$autolabel.default = '';

// Auto Move settings
$automove.enable = false;
$automove.directory = '/path/to/completed';
$automove.notifications = true;

// Auto Watch settings
$autowatch.enable = false;
$autowatch.directory = '/path/to/watch';
$autowatch.start = true;
?>
```

## Email Notifications

Auto Move can send email notifications after file transfer:

1. Create `.mailto` file in destination directory:

```text
user@example.com
```

2. Configure SMTP settings in conf.php (if available)
