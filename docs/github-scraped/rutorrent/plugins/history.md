# History Plugin Documentation

The History plugin logs a history of torrents, tracking their lifecycle from addition to completion.

## Features

- Track when torrents were added
- Record completion times
- Log torrent removals and their cause
- View historical data for all torrents
- Filter and search history

## What is Logged

| Event | Details |
|-------|---------|
| Added | Timestamp, source URL, initial path |
| Completed | Timestamp, final path, size |
| Removed | Timestamp, reason (manual, seed limit, etc.) |
| Changed | Label changes, path changes |

## Usage

1. Access History tab in ruTorrent
2. View chronological list of torrent events
3. Filter by date range, event type, or torrent name
4. Export history if needed

## Configuration

Edit `plugins/history/conf.php`:

```php
<?php
// Enable/disable
$enabled = true;

// Maximum history entries (0 = unlimited)
$max_entries = 10000;

// Log file path (optional)
$log_file = '/var/www/rutorrent/share/logs/history.log';
?>
```

## Data Retention

Configure how long to keep history:

```php
// Days to keep history (0 = forever)
$retention_days = 90;

// Auto-cleanup on startup
$auto_cleanup = true;
```

## Export

### View Raw Data

```bash
cat /var/www/rutorrent/share/settings/history.dat
```

### JSON Export

History can be exported for external analysis or backup.
