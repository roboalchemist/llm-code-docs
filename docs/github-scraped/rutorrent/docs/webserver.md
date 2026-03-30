# Web Server Configuration Guide

ruTorrent communicates with rtorrent via SCGI. This guide covers configuration for Apache, Nginx, Lighttpd, and Cherokee.

## Basic Requirements

- PHP with mbstring extension
- SCGI module for rtorrent communication
- Authentication on SCGI mount if directory is password-protected

## Lighttpd

### Install PHP

```bash
apt install php-cgi php-fpm
```

### Enable mod_fastcgi

In `lighttpd.conf`:

```bash
server.modules = (
    "mod_access",
    "mod_alias",
    "mod_compress",
    "mod_redirect",
    "mod_fastcgi",
)

# PHP FastCGI configuration
fastcgi.server = ( ".php" => ((
    "bin-path" => "/usr/bin/php-cgi",
    "socket" => "/tmp/php.socket"
)))
```

### SCGI Configuration (RPC Socket)

```bash
# Add mod_scgi to server.modules
server.modules += ( "mod_scgi" )

# SCGI mount configuration
scgi.server = (
    "/RPC2" => (
        "127.0.0.1" => (
            "host" => "127.0.0.1",
            "port" => 5000,
            "check-local" => "disable"
        )
    )
)
```

## Apache

### Install mod_scgi

```bash
# Ubuntu/Debian
apt-get install libapache2-mod-scgi

# FreeBSD
cd /usr/ports/www/mod_scgi && make install clean
```

### Configure SCGI

Add to your Apache config:

```
SCGIMount /RPC2 127.0.0.1:5000
```

Or use location block:

```apache
<Location /rutorrent>
    Require all granted
</Location>

<Location /RPC2>
    SCGIMount /RPC2 127.0.0.1:5000
    Require all granted
</Location>
```

### Alternative: mod_proxy_scgi

```apache
# Enable required modules
a2enmod proxy proxy_scgi

# Proxy configuration
ProxyPass /RPC2 scgi://localhost:5000/
# or with Unix socket:
ProxyPass /RPC2 unix:/path/to/unix.socket|scgi://127.0.0.1
```

### htpasswd Authentication

```bash
# Create password file
htpasswd -c /etc/apache2/.htpasswd username

# Add to Apache config
<Location /rutorrent>
    AuthType Basic
    AuthName "ruTorrent"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Location>
```

## Nginx

### SCGI Configuration

```nginx
location /RPC2 {
    include scgi_params;
    scgi_pass localhost:5000;
}
```

**Note:** SCGI module is built-in and enabled by default since nginx 0.8.42.

### Complete ruTorrent Configuration

```nginx
server {
    listen 80;
    server_name torrents.example.com;
    root /var/www/rutorrent;
    index index.html;

    # PHP processing
    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass unix:/var/run/php/php-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    # ruTorrent SCGI
    location /RPC2 {
        include scgi_params;
        scgi_pass 127.0.0.1:5000;
    }

    # ruTorrent files
    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Authentication

```nginx
auth_basic "ruTorrent";
auth_basic_user_file /etc/nginx/.htpasswd;
```

Generate password file:

```bash
htpasswd -c /etc/nginx/.htpasswd username
```

### SSL Configuration

```nginx
server {
    listen 443 ssl http2;
    server_name torrents.example.com;

    ssl_certificate /etc/ssl/certs/torrents.crt;
    ssl_certificate_key /etc/ssl/private/torrents.key;

    # ... rest of configuration
}
```

## Cherokee

### Using rtorrent Wizard

1. Open `cherokee-admin`
2. Select virtual server
3. Go to "Behavior" tab
4. Choose "wizards" -> "misc"
5. Select rtorrent wizard and configure

### Manual Configuration

```
vserver!20!rule!500!handler = scgi
vserver!20!rule!500!handler!balancer = round_robin
vserver!20!rule!500!handler!balancer!source!1 = 11
vserver!20!rule!500!match = request
vserver!20!rule!500!match!request = ^/RPC1
```

## Firewall Considerations

Ensure your firewall allows:

- Web server port (80/443)
- rtorrent listening ports (typically 6881-6889)

```bash
# UFW example
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 5000/tcp  # SCGI port
```

## Testing the Setup

1. Start rtorrent in the background
2. Access ruTorrent in browser
3. Check browser console for errors
4. Verify rtorrent is responding:

```bash
# Test SCGI connection
curl -s http://localhost/RPC2
```

## Common Issues

| Error | Cause | Solution |
|-------|-------|----------|
| "Bad link to rTorrent" | rtorrent not running or wrong SCGI config | Verify rtorrent is running; check config.php settings |
| 502 Bad Gateway | SCGI not configured | Ensure SCGI mount point matches config.php |
| 403 Forbidden | Wrong permissions | Check file ownership and .htaccess settings |
