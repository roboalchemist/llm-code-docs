# Crontab

These are the cron jobs. Adjust PATH according to where the repository is checked out on the filesystem.

```cron
PATH=$PATH:/var/www/bin

# Background task scheduler — runs every 15 minutes
0,15,30,45  *   * * * scheduler >> /tmp/schedule.log

# Sphinx delta indexer — runs every minute
*           *   * * * /usr/bin/indexer -c /etc/sphinx/sphinx.conf --rotate delta log_delta > /dev/null

# Sphinx full reindex — runs every 2 hours
5           */2 * * * /usr/bin/indexer -c /etc/sphinx/sphinx.conf --rotate --all >> /tmp/sphinx-indexer.log
```

## Adjusting PATH

Replace `/var/www/bin` with the actual path to the Gazelle `bin/` directory on your server.
