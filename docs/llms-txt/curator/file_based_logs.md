# Source: https://docs.curator.interworks.com/site_administration/logging/file_based_logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Logs

> File-based logs on the Curator server including the System Log, PHP error log, and Apache error log.

Server logs are stored as files on the Curator server and require direct server or file system access to view.
These logs are typically used for deeper troubleshooting, especially when database connectivity issues prevent
backend access or when investigating web server configuration problems.

## System Log

The System Log is Curator's primary application log, recording system events, errors, warnings, and debug
information. This log mirrors much of the same information found in the
[Event Log](/site_administration/logging/database_logs#event-log), but writes directly to disk rather than
the database.

<Note>
  The System Log can be particularly useful when the Event Log is unavailable (such as during database
  connectivity issues) or when troubleshooting errors that may not appear in the Event Log. In some cases,
  database transaction rollbacks can prevent Event Log entries from being saved, but the corresponding
  System Log entries will still be present.
</Note>

### Log File Location

The default System Log locations are:

| Operating System | Default Path                                 |
| ---------------- | -------------------------------------------- |
| Linux            | `/var/www/html/storage/logs/`                |
| Windows          | `C:\InterWorks\Curator\htdocs\storage\logs\` |

<Note>
  These paths may vary based on your installation. Central Dispatch installations, custom installation
  directories, or different Windows drive letters will affect the actual location. The log files are
  always located in the `storage/logs/` directory relative to your Curator installation root.
</Note>

### Log File Format

By default, Curator uses daily log rotation, creating files named `system-YYYY-MM-DD.log`. For example:

* `system-2025-01-15.log`
* `system-2025-01-14.log`

### Log Rotation Configuration

File-based log retention is configured separately from the database log retention settings. The number of
log files retained and other logging behavior is controlled by the `config/logging.php` configuration file.

If your log files are consuming excessive disk space or not rotating properly, refer to the
[Updating Curator Logging](/server_management/system_administration/updating_curator_logging) guide for
configuration instructions.

## PHP Error Log

The PHP error log captures PHP runtime errors, warnings, and notices that occur outside of Curator's
application logging. This can include syntax errors, memory issues, and extension-related problems that
may prevent Curator from starting properly.

### Log File Location

The PHP error log location depends on your server configuration:

| Operating System | Default Path                                                 |
| ---------------- | ------------------------------------------------------------ |
| Linux            | `/var/log/php-fpm/www-error.log` or `/var/log/php/error.log` |
| Windows          | `C:\InterWorks\Curator\php_error.log`                        |

<Note>
  The actual location may vary based on your PHP and web server configuration. Check your `php.ini` file
  for the `error_log` directive to find the exact path.
</Note>

### Common PHP Errors

| Error Type  | Description                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------ |
| Fatal Error | Critical errors that halt script execution (e.g., missing required files, syntax errors)         |
| Warning     | Non-fatal issues that may indicate problems (e.g., missing optional files, deprecated functions) |
| Notice      | Minor issues that don't affect functionality (e.g., undefined variables)                         |

### Viewing PHP Configuration

To find your PHP error log location and other settings:

```bash  theme={null}
# Linux
php -i | grep error_log

# Or check the loaded php.ini file
php --ini
```

## Apache Error Log

The Apache error log records web server errors, including failed requests, configuration issues, and
module errors. This log is essential for diagnosing issues with SSL certificates, URL rewrites, and
server connectivity.

### Log File Location

| Operating System | Default Path                                               |
| ---------------- | ---------------------------------------------------------- |
| Linux            | `/var/log/httpd/error_log` or `/var/log/apache2/error.log` |
| Windows          | `C:\InterWorks\Curator\libs\apache\logs\error.log`         |

<Note>
  The location varies based on your Linux distribution. RHEL/CentOS typically use `/var/log/httpd/`,
  while Debian/Ubuntu use `/var/log/apache2/`.
</Note>

### Apache Access Log

In addition to the error log, Apache maintains an access log that records all HTTP requests to the server.
This can be useful for:

* Tracking request patterns
* Identifying slow requests
* Debugging authentication issues
* Monitoring for suspicious activity

| Operating System | Default Path                                                 |
| ---------------- | ------------------------------------------------------------ |
| Linux            | `/var/log/httpd/access_log` or `/var/log/apache2/access.log` |
| Windows          | `C:\InterWorks\Curator\libs\apache\logs\access.log`          |

### Common Apache Errors

| Error                     | Description                                  |
| ------------------------- | -------------------------------------------- |
| 403 Forbidden             | Permission denied to access a resource       |
| 404 Not Found             | Requested file or page does not exist        |
| 500 Internal Server Error | Server-side error, often a PHP fatal error   |
| 502 Bad Gateway           | PHP-FPM or backend service not responding    |
| 503 Service Unavailable   | Server temporarily unable to handle requests |

## Troubleshooting Workflow

When troubleshooting issues with Curator, check logs in this order:

1. **Event Log** - Start with the backend Event Log for application-level errors
2. **System Log** - Check for entries that may not have been saved to the Event Log
3. **PHP Error Log** - Look for PHP runtime errors that prevent Curator from functioning
4. **Apache Error Log** - Check for web server configuration or connectivity issues

<Tip>
  When reporting issues to InterWorks Support, providing relevant excerpts from all applicable logs
  can significantly speed up diagnosis and resolution.
</Tip>
