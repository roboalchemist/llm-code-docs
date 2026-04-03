# Rutracker_check Plugin Documentation

The Rutracker_check plugin checks torrent availability on Rutracker tracker.

## Features

- Check if torrents are still available on Rutracker
- Automatic re-check on interval
- Visual status indicator in torrent list
- Error notifications when torrent is not available

## Requirements

- Valid Rutracker account with cookies configured
- LoginMgr plugin enabled with Rutracker credentials

## Usage

1. Enable Rutracker_check plugin
2. Configure cookies in LoginMgr
3. Torrents from Rutracker will be automatically checked

## Configuration

Edit `plugins/rutracker_check/conf.php`:

```php
<?php
// Check interval (minutes)
$checkInterval = 60;

// Enable auto-check on startup
$checkOnStart = true;
?>
```

## Status Indicators

| Status | Meaning |
|--------|---------|
| Green | Torrent available |
| Yellow | Checking... |
| Red | Not available |
| Gray | Not a Rutracker torrent |
