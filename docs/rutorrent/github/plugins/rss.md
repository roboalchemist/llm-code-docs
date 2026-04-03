# RSS Plugin Documentation

The RSS Plugin fetches torrents via RSS download links, featuring two main functions: entering feeds and setting up filters.

## Features

- Add and manage RSS feeds from torrent sites
- Automatic downloading based on filters
- Multi-feed support with individual settings
- Custom filter rules with regex support
- Cookie-based authentication support

## Adding a Feed

1. Right-click the RSS icon in the toolbar
2. Select **"Add RSS Feed"**
3. Enter the feed URL and a custom alias
4. Click OK

**Important:** Use a **download feed**, not a web feed. Some feeds require cookies (use the Cookies plugin).

## Manual Downloading

- Right-click an item and select **"Load"**
- Opens "Add Torrent" window
- Option to add torrent in "Stopped" mode

## RSS Manager

Access via right-click on RSS icon > **"RSS Manager"**

### Filter Configuration

| Option | Purpose |
|--------|---------|
| Add | Create new filter rule |
| Filter | Match regex pattern |
| Exclude | Exclusion regex |
| Check Fields | Match title, description, or link |
| Directory | Save path for downloads |
| Match Interval | Download frequency |
| Label | Assign label to downloaded torrents |
| RatioGroup | Set ratio group |
| Channel | Organize feeds by channel |

### Filter Examples

**Basic filter for TV episodes:**

```text
/Lost.S06E.*/i
```

**Exclude certain releases:**

```text
/(DVDR|Complete|DVDRip|BDrip|Bluray)/i
```

**Note:** Regex filters must be enclosed in `/ /i` tags for case-insensitive matching.

## Authentication Methods

### HTTP Basic Auth

```text
http://username:password@site.com/rss.php
```

### Cookie Authentication

```text
http://site.com/rss.php:COOKIE:name1=value1;name2=value2;
```

### Using the Cookies Plugin

Configure cookies in the Cookies plugin settings, then reference them in the feed URL.

## Feed Management

- **Edit Feed:** Right-click > "Edit Feed"
- **Delete Feed:** Right-click > "Remove Feed"
- **Refresh:** Right-click > "Refresh Feed"
- **Rename:** Right-click > "Rename Feed"

## Auto-Start Behavior

- Torrents auto-start when added through filters
- For server reboots, ensure rtorrent starts automatically
- ruTorrent remembers filter state on reload

## Configuration

### conf.php Settings

```php
// Enable/disable plugin
$enabled = true;

// Refresh interval (minutes)
$refreshInterval = 30;

// Maximum concurrent downloads from RSS
$maxConcurrent = 5;
```

### Command Line Usage

```bash
# Force refresh all feeds
php plugins/rss/refresh.php
```
