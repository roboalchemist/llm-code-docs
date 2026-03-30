# ruTorrent Version History

Complete changelog for ruTorrent releases.

## Version 3.6

**Release Date:** October 16, 2013 (r2450)

- Added **LookAt** plugin
- Added **_noty** plugin (notification system)
- Fixed numerous bugs
- Majority of plugin code rewritten

## Version 3.5

**Release Date:** December 7, 2012 (r2254)

- Added support for rtorrent 0.9.2
- Added **filedrop** plugin
- Multi-file torrent addition for modern browsers

## Version 3.4

**Release Date:** February 29, 2012 (r2014)

- Added support for rtorrent 0.9.0
- Added six new plugins:
  - Screenshots
  - Rutracker_check
  - History
  - And others

## Version 3.3

**Release Date:** July 30, 2011 (r1731)

- Added support for rtorrent 0.8.8/0.8.9
- Added browser support:
  - IE 9.0
  - Opera 11.0
  - Firefox 5.0
- Added iPad support
- User profile storage flexibility

## Version 3.2

**Release Date:** November 16, 2010 (r1552)

- Added new plugins:
  - Theme
  - RSS URL Rewrite
  - LoginMgr
  - Feeds
  - ExtSearch
- API rewritten to support plugins

## Version 3.1

**Release Date:** May 25, 2010 (r1167)

- Added single user mode directive
- Added gzip compression support
- Added cpuload plugin
- Added HTTPRPC plugin
- Added magnet-link support

## Version 3.0

**Release Date:** March 10, 2010 (r844)

- Major rewrite for improved performance
- Added multi-user support
- Added user access levels
- Added torrent search functionality

## Version 2.9

**Release Date:** March 10, 2010 (r844)

- Bug-fix release
- End of the 2.x branch

## Versions 2.6-2.8

**Release Period:** 2009

- Early releases with plugin additions
- Added plugins: geoip, ratio, tracklabels
- Various bug fixes
- Interface improvements

---

## Current Status

The ruTorrent project continues to be maintained with regular updates and bug fixes. Check the [GitHub releases page](https://github.com/Novik/ruTorrent/releases) for the latest version.

## Updating ruTorrent

To update to a newer version:

```bash
# Navigate to ruTorrent directory
cd /var/www/rutorrent

# Backup current installation
tar -czf rutorrent-backup-$(date +%Y%m%d).tar.gz ./

# Download new version
wget https://github.com/Novik/ruTorrent/archive/refs/heads/master.tar.gz
tar -xzf master.tar.gz

# Merge files (preserve conf/ directory)
cp -r ruTorrent-master/* .
rm -rf ruTorrent-master

# Restore permissions
chown -R www-data:www-data .
```
