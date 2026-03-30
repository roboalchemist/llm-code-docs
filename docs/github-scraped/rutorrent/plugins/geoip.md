# GeoIP Plugin Documentation

The GeoIP plugin shows geolocation of peers for the selected torrent.

## Features

- Display peer locations on a world map
- Show country flags for peers
- Country-based peer statistics

## Requirements

- PHP GeoIP extension installed
- GeoIP database (country or city level)

## Installation

### Install PHP GeoIP Extension

```bash
# Debian/Ubuntu
apt-get install php-geoip

# CentOS/RHEL
yum install php-pecl-geoip
```

### Download GeoIP Database

```bash
# Create database directory
mkdir -p /usr/share/GeoIP

# Download country database
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz
tar -xzf GeoLite2-Country.tar.gz
mv GeoLite2-Country*/GeoLite2-Country.mmdb /usr/share/GeoIP/

# Or city database for more detail
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
tar -xzf GeoLite2-City.tar.gz
mv GeoLite2-City*/GeoLite2-City.mmdb /usr/share/GeoIP/
```

## Configuration

Edit `plugins/geoip/conf.php`:

```php
<?php
// GeoIP database path
$geoip_db_path = '/usr/share/GeoIP';

// Database type: GEOIP_COUNTRY_EDITION or GEOIP_CITY_EDITION
$geoip_db_type = GEOIP_CITY_EDITION;
?>
```

## Usage

1. Select a torrent
2. Go to the Peers tab
3. GeoIP displays:
   - Country flags next to peer IPs
   - Country column with location
   - Map view (if supported)

## Troubleshooting

### "GeoIP extension not installed"

Install the PHP GeoIP extension (see Installation above).

### Incorrect Locations

- Update GeoIP database regularly
- Use city database for better accuracy
- Check database file permissions

### Map Not Displaying

- Ensure JavaScript is enabled
- Check browser console for errors
- Verify map library is loaded
