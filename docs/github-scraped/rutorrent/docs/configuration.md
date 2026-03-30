# ruTorrent Configuration Reference

Complete reference for ruTorrent configuration files: `config.php`, `access.ini`, and `plugins.ini`.

## config.php

The main configuration file controlling ruTorrent's core functionality.

### HTTP/Snoopy Client Settings

| Parameter | Type | Description |
|-----------|------|-------------|
| `$httpUserAgent` | string | Browser user agent string for HTTP requests |
| `$httpTimeOut` | integer | Request timeout in seconds |
| `$httpUseGzip` | boolean | Enable gzip compression for HTTP responses |
| `$httpIP` | string | Specific IP for external HTTP/HTTPS resource access |
| `$httpProxy` | array | Proxy configuration: protocol, host, and port |

### XMLRPC Communication

| Parameter | Type | Description |
|-----------|------|-------------|
| `$rpcTimeOut` | integer | XMLRPC request timeout in seconds |
| `$rpcLogCalls` | boolean | Enable logging of RPC method calls |
| `$rpcLogFaults` | boolean | Log RPC faults and errors |

### PHP Processing

| Parameter | Type | Description |
|-----------|------|-------------|
| `$phpUseGzip` | boolean | Use external gzip binary for page compression |
| `$phpGzipLevel` | integer | Compression level for gzip output (0-9) |

### SCGI Connection

| Parameter | Type | Description |
|-----------|------|-------------|
| `$scgi_host` | string | SCGI host address (127.0.0.1 for localhost) |
| `$scgi_port` | integer | SCGI port number |
| `$XMLRPCMountPoint` | string | Mount point path for XMLRPC communication |

**Example:**

```php
$scgi_host = "127.0.0.1";
$scgi_port = 5000;
$XMLRPCMountPoint = "/RPC2";
```

### Diagnostic & Logging

| Parameter | Type | Description |
|-----------|------|-------------|
| `$do_diagnostic` | boolean | Enable ruTorrent diagnostic checks |
| `$al_diagnostic` | boolean | Auto-loader diagnostic mode |
| `$log_file` | string | File path for error logging |

### Upload & Directory Settings

| Parameter | Type | Description |
|-----------|------|-------------|
| `$saveUploadedTorrents` | boolean | Persist uploaded .torrent files |
| `$overwriteUploadedTorrents` | boolean | Replace existing torrent files |
| `$topDirectory` | string | Root directory users can access |
| `$tempDirectory` | string | Temporary file storage location |

### Plugin Configuration

| Parameter | Type | Description |
|-----------|------|-------------|
| `$cachedPluginLoading` | boolean | Enable cached plugin loading for performance |
| `$pluginMinification` | boolean | Minify JavaScript for faster loading |

### Security Settings

| Parameter | Type | Description |
|-----------|------|-------------|
| `$enableCSRFCheck` | boolean | Validate Origin and Referer headers |
| `$enabledOrigins` | array | Allowed domains for CSRF validation |
| `$forbidUserSettings` | boolean | Restrict user configuration access |

### Path & Profile Settings

| Parameter | Type | Description |
|-----------|------|-------------|
| `$pathToExternals` | array | Paths to external binaries (PHP, curl, gzip) |
| `$profilePath` | string | User profile directory location |
| `$profileMask` | string | File permission mask for profiles |
| `$localhosts` | array | Recognized localhost addresses |

**Example:**

```php
$pathToExternals = [
    "php"  => '/usr/bin/php',
    "curl" => '/usr/bin/curl',
    "gzip" => '/bin/gzip'
];
```

### Performance Options

| Parameter | Type | Description |
|-----------|------|-------------|
| `$canUseXSendFile` | boolean | Enable X-Sendfile for file serving |
| `$localHostedMode` | boolean | rTorrent runs on same machine |
| `$throttleMaxSpeed` | integer | Maximum upload speed limit |
| `$locale` | string | Character encoding setting |

---

## access.ini

Interface control flags using `yes`/`no` values.

### Page Visibility

| Setting | Default | Description |
|---------|---------|-------------|
| `showDownloadsPage` | yes | Display downloads tab |
| `showConnectionPage` | yes | Display connection settings tab |
| `showBittorentPage` | yes | Display BitTorrent settings tab |
| `showAdvancedPage` | yes | Display advanced options tab |
| `showPluginsTab` | yes | Display plugins tab |

### Rate Control

| Setting | Default | Description |
|---------|---------|-------------|
| `canChangeULRate` | yes | Modify upload speed limit |
| `canChangeDLRate` | yes | Modify download speed limit |

### Torrent Management

| Setting | Default | Description |
|---------|---------|-------------|
| `canChangeTorrentProperties` | yes | Edit torrent properties |
| `canAddTorrentsWithoutPath` | yes | Add torrents without download path |
| `canAddTorrentsWithoutStarting` | yes | Add torrents without auto-starting |
| `canAddTorrentsWithResume` | yes | Resume torrent after adding |
| `canAddTorrentsWithRandomizeHash` | no | Randomize info hash |

---

## plugins.ini

Plugin control flags with values: `yes`, `no`, or user-defined strings.

### Standard Plugin Flags

| Flag | Description |
|------|-------------|
| `enabled` | Plugin activation status |
| `canChangeToolbar` | Modify main toolbar |
| `canChangeMenu` | Modify context menus |
| `canChangeOptions` | Change plugin options |
| `canChangeTabs` | Add new interface tabs |
| `canChangeColumns` | Modify table structures |
| `canChangeStatusBar` | Alter status bar content |
| `canChangeCategory` | Modify category labels |
| `canBeShutdowned` | Allow plugin unloading |

### Example plugins.ini Entry

```ini
[_task]
enabled = yes
canChangeToolbar = yes
canChangeMenu = yes
canChangeOptions = yes
canChangeTabs = no
canChangeColumns = yes
canChangeStatusBar = no
canChangeCategory = yes
canBeShutdowned = yes

[throttle]
enabled = yes
canChangeToolbar = no
canChangeMenu = yes
canChangeOptions = yes
canChangeTabs = no
canChangeColumns = no
canChangeStatusBar = yes
canChangeCategory = no
canBeShutdowned = yes
```

---

## Example config.php

```php
<?php
// SCGI Connection
$scgi_host = "127.0.0.1";
$scgi_port = 5000;
$XMLRPCMountPoint = "/RPC2";

// HTTP Settings
$httpUserAgent = '';
$httpTimeOut = 30;
$httpUseGzip = true;

// Directory Settings
$topDirectory = '/home/user/downloads';
$tempDirectory = '/home/user/rutorrent/share/temp';

// Logging
$log_file = '/home/user/rutorrent/share/logs/errors.log';

// Security
$enableCSRFCheck = true;
$enabledOrigins = ['https://torrents.example.com'];

// Performance
$phpUseGzip = false;
$canUseXSendFile = false;

// Paths to external binaries
$pathToExternals = [
    "php"  => '/usr/bin/php',
    "curl" => '/usr/bin/curl',
    "gzip" => '/bin/gzip',
    "tar"  => '/bin/tar',
];
?>
```

---

## Multi-User Configuration

ruTorrent supports multiple users with individual settings:

1. Create user directories in `share/`
2. Configure per-user `config.php` in `conf/users/<username>/`
3. Set appropriate permissions

```bash
share/
  users/
    user1/
      settings/
      torrents/
    user2/
      settings/
      torrents/
```
