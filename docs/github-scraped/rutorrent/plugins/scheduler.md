# Scheduler Plugin Documentation

The Scheduler plugin enables you to define six different rtorrent behavior types for each hour of the 168-hour week.

## Behavior Modes

| Mode | Description |
|------|-------------|
| **Unlimited** | Uses predefined upload/download limits |
| **Turn off** | Stops all torrents |
| **Seeding only** | Stops all torrents, then restarts only those stopped by the plugin |
| **Limited1** | Apply custom speed limits configured in settings |
| **Limited2** | Apply custom speed limits configured in settings |
| **Limited3** | Apply custom speed limits configured in settings |

## How It Works

When ruTorrent starts with the Scheduler plugin installed:
1. It sends a command to rtorrent's scheduler
2. The scheduler periodically calls a dedicated script
3. Behavior changes based on the current time slot

**Note:** The poll only begins after the first ruTorrent startup.

## Configuration

Edit `plugins/scheduler/conf.php`:

```php
<?php
// Default download speed limit (KB/s)
$sch_def_dl = 0;  // 0 = unlimited

// Default upload speed limit (KB/s)
$sch_def_ul = 0;  // 0 = unlimited

// Script call interval in minutes
$updateInterval = 60;
?>
```

## Time Slot Configuration

### Web Interface

Access via Settings > Scheduler in ruTorrent:
1. Click hour blocks to cycle through modes
2. Drag to select multiple hours
3. Configure speed limits for Limited modes

### Direct Configuration

Edit time slots in the scheduler settings:

```
Hour: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Mode: U U U U U U U U L1 L1 L1 L1 U U U L2 L2 L2 L3 L3 U U U U
```

Where:
- `U` = Unlimited
- `T` = Turn off
- `S` = Seeding only
- `L1` = Limited1
- `L2` = Limited2
- `L3` = Limited3

## Speed Limits for Limited Modes

Configure limits in conf.php:

```php
// Limited1 settings (KB/s)
$SCH_L1_DL = 1000;  // Download
$SCH_L1_UL = 100;    // Upload

// Limited2 settings (KB/s)
$SCH_L2_DL = 500;
$SCH_L2_UL = 50;

// Limited3 settings (KB/s)
$SCH_L3_DL = 100;
$SCH_L3_UL = 10;
```

## PHP Timezone Setup

PHP defaults to UTC. Configure in php.ini:

```ini
date.timezone = "America/New_York"
```

Check both CLI and FPM php.ini files (typically in `/etc/php/`).

## Use Cases

### Night Time Throttling

Reduce bandwidth usage during night hours:
```
22:00 - 06:00: Limited (100 KB/s down, 20 KB/s up)
06:00 - 22:00: Unlimited
```

### Seeding During Off-Peak

Seed only during specific hours:
```
00:00 - 08:00: Seeding only
08:00 - 00:00: Turn off
```

### Day/Night Schedule

```
Weekdays:
00:00 - 08:00: Limited1
08:00 - 18:00: Turn off
18:00 - 00:00: Unlimited

Weekends:
00:00 - 24:00: Unlimited
```

## Troubleshooting

### Scheduler Not Working

1. Ensure rtorrent is running
2. Check PHP has write access to scheduler script
3. Verify time slot configuration
4. Check rtorrent log for errors

### Wrong Time Being Applied

1. Verify system timezone
2. Check PHP timezone setting
3. Ensure NTP is running on server
