# LoginMgr Plugin Documentation

The LoginMgr plugin handles authentication with third-party torrent sites. It's a support plugin primarily used by the RSS and ExtSearch plugins for logging into trackers.

## Features

- Store multiple tracker credentials
- Automatic login to protected trackers
- Cookie-based authentication support
- Fallback to direct login when cookies expire

## Configuration

Access through the WebUI Settings menu, then select **"Accounts"** from the left sidebar.

### Available Options

| Option | Description |
|--------|-------------|
| Login | Username for the site |
| Password | Password for authentication |
| Enabled | Checkbox to activate/deactivate for individual sites |

## Security Note

**Warning:** This plugin stores passwords in plain text format. Consider the security implications before storing credentials.

## Usage

### With RSS Plugin

1. Configure LoginMgr with tracker credentials
2. Set up RSS feed in RSS plugin
3. Plugin automatically logs in when fetching feed

### With ExtSearch Plugin

1. Configure LoginMgr with tracker credentials
2. Use ExtSearch to search tracker
3. Plugin handles authentication automatically

## Configuration File

Edit `plugins/loginmgr/conf.php`:

```php
<?php
// Enable auto-login
$autologin = true;

// Session timeout (seconds)
$session_timeout = 3600;
?>
```

## Troubleshooting

### Login Fails

1. Verify credentials in LoginMgr settings
2. Check if tracker is operational
3. Look for captcha requirements (not supported)
4. Check browser console for error messages

### Cookies Not Working

1. Ensure Cookies plugin is enabled
2. Verify cookie format in feed URL
3. Check cookie expiration settings
