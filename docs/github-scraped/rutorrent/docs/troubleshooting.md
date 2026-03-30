# ruTorrent Troubleshooting Guide

## Common Error Messages

### "torrent doesn't passed to rTorrent"

**Cause:** The torrent tracker requires authorization, or the torrent file was corrupted during download.

**Solution:**

- Verify tracker authentication credentials
- Re-download the torrent file
- Check if tracker is operational

---

### "PHP module PCRE is not installed"

**Cause:** Missing PCRE module on BSD-based systems.

**Solution:**

```bash
# Debian/Ubuntu
apt-get install php-pcre

# FreeBSD
pkg install php*pcRE
```

---

### "Web server can't access rTorrent's session directory"

**Cause:** Insufficient rights or restricted PHP instructions (`open_basedir`).

**Solution:**

- Move the session directory to the rtorrent installation directory
- Adjust `open_basedir` in php.ini:

  ```ini
  open_basedir = /var/www/rutorrent:/home/user/rtorrent:/tmp
  ```

- Set proper permissions:

  ```bash
  chmod -R 0777 ~/rtorrent/.session
  ```

---

### "Permission Errors (Settings, Torrents, test.sh)"

**Cause:** Incorrect ruTorrent installation; archive was not unpacked under the web-server user account.

**Solution:**
```bash
# Fix ownership (adjust user/group for your setup)
chown -R www-data:www-data /var/www/rutorrent

# Fix permissions
find /var/www/rutorrent -type d -exec chmod 755 {} \;
find /var/www/rutorrent -type f -exec chmod 644 {} \;

# Directories needing write access
chmod 777 /var/www/rutorrent/share
chmod 777 /var/www/rutorrent/share/settings
chmod 777 /var/www/rutorrent/share/torrents
```

---

### "Bad link to rTorrent"

**Cause:** rtorrent is not running or misconfigured SCGI settings.

**Diagnosis:**
```bash
# Check if rtorrent is running
ps aux | grep rtorrent

# Test SCGI port
curl -s http://localhost/RPC2
```

**Solution:**
1. Verify rtorrent is running
2. Check `config.php` settings:
   ```php
   $scgi_host = "127.0.0.1";
   $scgi_port = 5000;
   ```
3. Match with rtorrent configuration
4. Restart services:
   ```bash
   systemctl restart rtorrent
   systemctl restart apache2  # or nginx
   ```

---

### "xmlrpc-c library version incorrect"

**Cause:** rtorrent compiled with xmlrpc-c < 1.11, lacking i8 support.

**Solution:**
1. Check xmlrpc-c version:
   ```bash
   xmlrpc-c-config --version
   ```
2. If version < 1.11, recompile rtorrent with newer xmlrpc-c:
   ```bash
   svn co http://svn.code.sf.net/p/xmlrpc-c/code/stable xmlrpc-c
   cd xmlrpc-c
   ./configure
   make
   make install
   ```

---

### "Plugin cannot access external program"

**Cause:** Required program is unavailable to the web-server user, not in PATH, or running in chroot.

**Solution:**
- Install the required program
- Configure plugin to use full path:
  ```php
  // In plugin conf.php
  $pathToCreatetorrent = '/usr/local/bin/mktorrent';
  ```
- Check PATH for web server user:
  ```bash
  sudo -u www-data env | grep PATH
  ```

---

### "rTorrent user can't access PHP interpreter"

**Cause:** PHP interpreter unavailable to rtorrent user (system uses php-fcgi without cli).

**Solution:**
```bash
# Install PHP CLI
apt-get install php-cli
# or
yum install php-cli
```

---

### "rTorrent user can't access external program"

**Cause:** PHP files in plugins directory may lack execute permissions, or DOS line endings present.

**Solution:**
```bash
# Check permissions
sudo -u <rtorrent_user> sh <ruTorrent_install_dir>/php/test.sh

# Fix DOS line endings
dos2unix php/test.sh
find . -name "*.php" -exec dos2unix {} \;

# Set execute permissions
chmod +x php/test.sh
```

---

## Diagnostic Tools

### Built-in Diagnostic

Enable in `config.php`:
```php
$do_diagnostic = true;
$al_diagnostic = true;
$log_file = '/path/to/logfile.log';
```

### test.sh Script

```bash
cd /var/www/rutorrent
php test.sh
```

This checks:
- PHP extensions (curl, zip, etc.)
- File permissions
- External program availability
- Session directory access

## Performance Issues

### Slow Page Loads

**Causes:**
- Large number of torrents
- Insufficient PHP memory
- Slow external program calls

**Solutions:**
```php
// Increase PHP memory limit in php.ini
memory_limit = 256M

// Enable caching in config.php
$cachedPluginLoading = true;
$pluginMinification = true;
```

### High CPU Usage

**Causes:**
- Many peers connected
- Disk I/O bottlenecks
- Too many concurrent operations

**Solutions:**
- Limit max connections in rtorrent config
- Use bandwidth throttling
- Consider SSD for session directory

## Connection Issues

### Cannot Connect from External Network

**Check:**
1. Firewall rules:
   ```bash
   iptables -L -n | grep 5000
   ufw status
   ```
2. Web server binding:
   ```nginx
   # Nginx - bind to all interfaces
   listen 80;  # instead of localhost
   ```
3. SCGI host in config.php:
   ```php
   $scgi_host = "0.0.0.0";  # or specific IP
   ```

### SSL Certificate Errors

**For self-signed certificates:**
```php
// In config.php
$httpIP = "your.ip.here";
$httpProxy = [
    "protocol" => "https",
    "host"     => "your.host.com",
    "port"     => 443
];
```

## Log Analysis

### Enable Logging

```php
// In config.php
$log_file = '/var/www/rutorrent/share/logs/rutorrent.log';
```

### Read Logs

```bash
tail -f /var/www/rutorrent/share/logs/rutorrent.log
```

### Common Log Entries

| Entry | Meaning |
|-------|---------|
| `XMLRPC connection failed` | SCGI misconfiguration |
| `Permission denied` | File/directory permissions issue |
| `RPC timeout` | rtorrent unresponsive |
| `CSRF check failed` | Session mismatch |

## Getting Help

- [GitHub Issues](https://github.com/Novik/ruTorrent/issues)
- [GitHub Wiki](https://github.com/Novik/ruTorrent/wiki)
- [Forum](https://forums.rutorrent.net/)
