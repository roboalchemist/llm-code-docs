# Throttle Plugin Documentation

The Throttle plugin provides control over speed limits for groups of torrents in rtorrent 0.8.5+.

## Features

- Configure speed limits for multiple channels (default: 10)
- Assign channels to individual torrents or groups via contextual menu
- "0" value means no limits
- Minimum limit is 1 Kbps

## Requirements

- rtorrent 0.8.5 or later
- Channels are created on first ruTorrent start after rtorrent initialization

## Usage

### Assigning a Channel

1. Right-click on a torrent or multiple torrents
2. Select **"Throttle"** from the context menu
3. Choose a channel (1-10)

### Channel Settings

Access via Settings > Channels:

| Channel | Download (KB/s) | Upload (KB/s) |
|---------|-----------------|---------------|
| 1 | 0 (unlimited) | 0 (unlimited) |
| 2 | 0 | 0 |
| ... | ... | ... |
| 10 | 0 | 0 |

### Quick Assignment

Right-click torrent > Throttle > Channel Number

## Configuration

Edit `plugins/throttle/conf.php`:

```php
<?php
// Maximum number of channels
$max_throttle = 10;

// Default download speed per channel (KB/s)
$default_dl = 0;

// Default upload speed per channel (KB/s)
$default_ul = 0;
?>
```

## Important Notes

1. **Speed limits only function when global system limits are set** in rtorrent config
2. ruTorrent automatically adjusts zero values to ensure functionality
3. **Channel assignment requires the torrent to be stopped first**
4. Changing channels does not affect torrent state

## Use Cases

### Priority Torrents

- Channel 1: Unlimited (priority downloads)
- Channels 2-5: Limited (secondary downloads)
- Channel 10: Very slow (background seeding)

### ISP Data Caps

Create channels with reduced speeds to manage bandwidth usage:

```php
// Channel 1: Peak hours (conservative)
$dl = 500;  // KB/s
$ul = 50;

// Channel 2: Off-peak (faster)
$dl = 2000;
$ul = 200;
```

### Ratio Management

Use throttling to control upload speeds for ratio requirements:

```php
// Maintain ratio while throttling
$dl = 0;    // No download limit
$ul = 20;   // Slow upload for ratio
```

## Troubleshooting

### "Throttle not available"

- Verify rtorrent version >= 0.8.5
- Restart ruTorrent to create channels

### Speed Limits Not Working

- Ensure global limits are set in rtorrent config:

  ```text
  throttle.global_down.max_rate.set_kb = 0
  throttle.global_up.max_rate.set_kb = 0
  ```

- Check torrent is assigned to a channel
- Verify torrent is not in "unlimited" state
