# Gazelle - What.CD Web Framework for Private BitTorrent Trackers

Gazelle is an open-source PHP web framework designed for private BitTorrent trackers. Originally developed by [What.CD](https://whatcd.github.io/Gazelle/) to power one of the largest music-focused private trackers, it is written in PHP, JavaScript, and MySQL. Although it focuses on music by default, it can be adapted for most private tracker use cases.

**Repository:** [WhatCD/Gazelle](https://github.com/whatcd/gazelle) | **GitHub Pages:** [whatcd.github.io/Gazelle](https://whatcd.github.io/Gazelle/)

## Features

Gazelle ships with a comprehensive feature set for running a private BitTorrent tracker:

- **User account management** -- registration, authentication, permissions, user classes, and staff roles
- **Torrent upload and download handling** -- torrent file processing, announce/scrape endpoints, peer management
- **Ratio tracking** -- per-user seeding/leeching stats, ratio enforcement, bonus points
- **Seeding bonuses** -- configurable bonus point system rewarding long-term seeders
- **Community features** -- forums, collage system, request system, staff blog, bookmarks, comments
- **Artist database** -- music artist pages with discographies, similar artists, tags
- **Search** -- Sphinx-powered full-text search across torrents, artists, requests, and forums
- **Notifications** -- in-site messaging, torrent comments, quote notifications, staff PMs
- **Staff tools** -- reports system, user toolbox, site history, site-wide options
- **Bitcoin donations** -- integrated donation processing with rank perks
- **API** -- REST API for third-party integrations and OAuth-based application access
- **GeoIP** -- MaxMind GeoIP-based user country tracking
- **Push notifications** -- Pushbullet integration for staff alerts
- **IRC integration** -- IRC announce, !trich command support
- **OpenSearch** -- Browser search plugin support
- **Captcha** -- built-in captcha system

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | PHP 5.4+ |
| Frontend | JavaScript (vanilla + jQuery-era libraries) |
| Database | MySQL |
| Search | Sphinx Search 2.0.6+ |
| Caching | Memcached |
| Web server | Nginx (recommended) |
| Tracker daemon | Ocelot (custom compiled, included as `ocelot-0.8.tar.gz` / `ocelot-1.0.tar.gz`) |

### Project Structure

```text
gazelle/
├── ajax.php               # AJAX request dispatcher
├── announce.php           # BitTorrent announce endpoint (tracker)
├── api.php                # REST API entry point
├── gazelle.sql            # Full database schema
├── sphinx.conf            # Sphinx search index configuration
├── classes/               # PHP class files (70+ classes)
│   ├── users.class.php
│   ├── torrents.class.php
│   ├── torrentsearch.class.php
│   ├── sphinxql.class.php
│   ├── notificationsmanager.class.php
│   ├── forums.class.php
│   ├── requests.class.php
│   ├── collages.class.php
│   ├── donations.class.php
│   └── ...
├── sections/             # Page sections (MVC sections pattern)
│   ├── torrents/
│   ├── artist/
│   ├── requests/
│   ├── collages/
│   ├── forums/
│   ├── user/
│   ├── upload/
│   └── ...
├── design/               # Static assets (CSS, images)
├── static/               # JavaScript and other static files
├── templates/            # HTML template files
├── docs/
│   ├── INSTALL.txt       # Detailed installation guide
│   ├── CodingStandards.txt  # Code style guide
│   └── CHANGES.txt      # Daily-generated changelog
└── ocelot-*.tar.gz       # Pre-built Ocelot tracker daemon
```

## Dependencies

### Runtime Dependencies

| Dependency | Version | Required | Notes |
|------------|---------|----------|-------|
| Nginx | any | Recommended | Apache also works |
| PHP | 5.4+ | Yes | Familiarity with PHP assumed for modifications |
| Memcached | any | Yes | Used for caching layer |
| Sphinx Search | 2.0.6+ | Yes | Full-text search engine |
| procps-ng | any | Recommended | Process utilities |

### Compile-Time Dependencies (for Ocelot/Gazelle-Ocelot)

| Dependency | Version | Notes |
|------------|---------|-------|
| Git | any | Source checkout |
| GCC/G++ | 4.7+ (4.8.1+ recommended) | Compilation |
| Boost | 1.55.0+ | Required by Ocelot tracker daemon |

## Installation

### Prerequisites

Gazelle requires a running MySQL database, Memcached daemon, and Sphinx search installation before beginning.

### Step 1: Database Setup

Run the provided SQL schema to initialize all tables:

```sql
SET FOREIGN_KEY_CHECKS = 0;
CREATE DATABASE gazelle CHARACTER SET utf8 COLLATE utf8_swedish_ci;
USE gazelle;
-- (run gazelle.sql here)
SET FOREIGN_KEY_CHECKS = 1;
```

Key tables include: `users`, `torrents`, `torrents_group`, `artists_group`, `forums`, `forum_posts`, `requests`, `collages`, `comments`, `bookmarks_*`, `donations`, `invite_tree`, `sphinx_*`, and more.

### Step 2: Sphinx Search Configuration

Copy `sphinx.conf` to your Sphinx installation directory:

```bash
cp sphinx.conf /etc/sphinx/sphinx.conf
mkdir -p /var/lib/sphinx/
/usr/bin/indexer -c /etc/sphinx/sphinx.conf --all
```

The configuration defines multiple indexes:

- `torrents` -- main torrent search index (with artist names via joined fields)
- `requests` -- request search index
- `log` -- site log index

Indexes use delta indexing strategy with a `delta` index rotated every minute and a full `main` index rotated twice daily.

### Step 3: Application Configuration

Copy the configuration template and customize:

```bash
cp classes/config.php.template classes/config.php
# Edit classes/config.php with your site settings:
# - Database credentials
# - Memcached socket path
# - Sphinx connection settings
# - Site name, announcements
# - API keys
```

### Step 4: Memcached

Start memcached with a Unix socket:

```bash
memcached -d -m 5120 -s /var/run/memcached.sock -a 0777 -t 4 -C -u nobody
```

### Step 5: Web Server

Configure your web server (Nginx example):

```nginx
server {
    listen 80;
    server_name tracker.example.com;
    root /var/www/gazelle;
    index index.php;

    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
}
```

### Step 6: First User (SysOp)

Register the first user account through the web interface. The first registered user is automatically granted SysOp privileges.

### Step 7: Cron Jobs

Four scheduled tasks are required:

```bash
# Schedule processing (every 15 minutes)
*/15 * * * * /usr/bin/php /var/www/vhosts/what/schedule.php SCHEDULE_KEY

# Peer update (every 15 minutes, offset by 10 minutes)
*/15 * * * * sleep 10; /usr/bin/php /var/www/vhosts/what/peerupdate.php SCHEDULE_KEY

# Delta index rotation (every minute)
* * * * * /usr/bin/indexer -c /etc/sphinx/sphinx.conf --rotate delta requests_delta log_delta

# Full index rotation (twice daily at midnight and noon)
0 */12 * * * /usr/bin/indexer -c /etc/sphinx/sphinx.conf --rotate --all
```

### Step 8: GeoIP Data

Populate country data by visiting `/tools.php?action=update_geoip`, then run the provided SQL migration to map existing users to their geographic distribution.

### Development with Vagrant

[VagrantGazelle](https://github.com/dr4g0nnn/VagrantGazelle) provides a pre-configured Vagrant environment for local development. Source files are shared from `src/` on the host to `/var/www/` on the guest. Port 80 on the guest forwards to port 8080 on the host.

## Configuration Reference

### Key Configuration Options (classes/config.php)

| Option | Description |
|--------|-------------|
| `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME` | MySQL connection settings |
| `MEMCACHED_HOST`, `MEMCACHED_PORT` | Memcached server |
| `SITE_NAME` | Tracker name displayed in templates |
| `ANNOUNCE_URL` | Torrent announce URL |
| `SCHEDULE_KEY` | Secret key for cron job authentication |
| `SITE_URL` | Base URL of the tracker |
| `SPHINX_HOST`, `SPHINX_PORT` | Sphinx search server |
| `ENABLE_IPV4`, `ENABLE_IPV6` | Protocol toggle flags |

### Site Options (Database)

Site-wide options are stored in the `site_options` table rather than hardcoded, allowing staff to toggle features without code changes.

### User Classes

Gazelle defines user classes with different permission levels:

| Class | Description |
|-------|-------------|
| Guest | Unregistered visitor |
| User | Registered member |
| Power User | Elevated privileges |
| Elite | Higher trust level |
| Donor | Paid supporter with bonus perks |
| Moderator | Can edit content, warn users |
| SysOp | Full site administrator |

Permissions are enforced via the `permissions` class and `permissions_form.php`.

## Coding Standards

All pull requests must adhere to Gazelle's coding standards defined in `docs/CodingStandards.txt`.

### File Naming

- PHP, CSS, and JavaScript files use lowercase with underscores: `torrent_search.class.php`
- No mixed-case or camelCase in file names

### Formatting

| Rule | PHP/JavaScript | CSS |
|------|----------------|-----|
| Indentation | Tabs | Tabs |
| Line endings | LF (Unix) | LF (Unix) |
| Encoding | ASCII | ASCII |
| Braces | K&R (same line) | N/A |

### PHP/JavaScript Style

- Opening braces on the same line as the statement (K&R style)
- Spaces before control structure parentheses: `if (...)`
- Spaces around conditional and ternary operators: `$a ? $b : $c`
- Use `elseif` not `else if`
- Always include braces for single statements
- Use `<?` short tags for PHP
- JavaScript variables use `var` (ES5 era)
- No whitespace between cast operators

### SQL Style

- SQL keywords in uppercase: `SELECT`, `JOIN`, `WHERE`
- Use aliases for multi-table joins
- Use `!=` for not equal comparisons
- Proper indentation with JOINs indented from SELECT

### Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| PHP functions | lowercase_with_underscores | `get_user_stats()` |
| JavaScript functions | camelCase | `formatBytes()` |
| PHP variables | CamelCase | `$UserID`, `$CacheDir` |
| JavaScript globals | camelCase | `totalSize` |
| JavaScript locals | lowercase_with_underscores | `file_count` |
| Classes | CamelCase | `TorrentsClass` |
| Constants | ALL_CAPS | `MAX_UPLOAD_SIZE` |
| SQL tables | lowercase_with_underscores | `torrents_group` |
| SQL columns | CamelCase | `GroupID`, `UserID` |
| ID columns | `ID` or descriptive | `RequestID` |

### Comments

- Multi-line: `/* */` (C89-style)
- Single-line: `//` (C99-style)

## API

Gazelle exposes a REST API via `api.php` with OAuth-based application authorization.

### API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api.php?action=torrent&id=<id>` | Get torrent details |
| `GET /api.php?action=user&id=<id>` | Get user profile and stats |
| `GET /api.php?action=collage&id=<id>` | Get collage details |
| `GET /api.php?action=recent` | Get recently uploaded torrents |
| `POST /api.php?action=upload` | Upload a new torrent (authenticated) |

### OAuth Applications

Users can register OAuth applications to access the API on behalf of other users:

```sql
-- Applications table
CREATE TABLE api_applications (
  ID int(10) NOT NULL AUTO_INCREMENT,
  UserID int(10) NOT NULL,
  Token char(32) NOT NULL,
  Name varchar(50) NOT NULL,
  PRIMARY KEY (ID)
);

-- Authorized users per application
CREATE TABLE api_users (
  UserID int(10) NOT NULL,
  AppID int(10) NOT NULL,
  Token char(32) NOT NULL,
  State enum('0','1','2') NOT NULL DEFAULT '0',
  Time datetime NOT NULL,
  Access text,
  PRIMARY KEY (UserID, AppID)
);
```

## Sphinx Search Configuration

Gazelle uses Sphinx for full-text search across multiple content types. The `sphinx.conf` defines multiple data sources and indexes.

### Torrent Index Source

The `torrents` source inherits from `torrents_base` and aggregates data from three normalized tables (`sphinx_tg`, `sphinx_t`, `sphinx_a`) via `sql_query_pre` statements:

```sql
-- Group table (sphinx_tg)
INSERT INTO sphinx_tg (id, name, taglist, year, ...)
SELECT id, name, taglist, year, ... FROM torrents_group

-- Torrent table (sphinx_t)
INSERT INTO sphinx_t (id, gid, size, snatched, seeders, ...)
SELECT ID, GroupID, Size, Snatched, Seeders, ...
FROM torrents

-- Artist name joined field (sphinx_a)
INSERT INTO sphinx_a (gid, aname)
SELECT GroupID, GROUP_CONCAT(aa.Name SEPARATOR ' ')
FROM torrents_artists JOIN artists_alias USING(AliasID)
WHERE Importance IN ('1','3','4','5','6')
GROUP BY groupid
```

### Indexed Torrent Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| groupid | uint | Torrent group ID |
| time | uint | Upload timestamp |
| categoryid | uint | Category (Music, Anime, etc.) |
| releasetype | uint | Album type |
| size | bigint | Total size in bytes |
| snatched | uint | Total snatch count |
| seeders | uint | Current seeder count |
| leechers | uint | Current leecher count |
| logscore | uint | Log check score (0-100) |
| year | uint | Release year |
| scene | bool | Scene release flag |
| haslog | bool | Has log file |
| hascue | bool | Has CUE sheet |
| freetorrent | bool | Free torrent flag |

## Key Database Tables

| Table | Purpose |
|-------|---------|
| `users` | User accounts and authentication |
| `torrents_group` | Album/release-level grouping of torrents |
| `torrents` | Individual torrent files within a group |
| `torrents_artists` | Artist-to-torrent mappings with role |
| `artists_group` | Artist names and metadata |
| `artists_alias` | Artist alias names |
| `requests` | User-submitted requests for specific content |
| `requests_votes` | Votes on requests |
| `collages` | User-curated collections of torrents/artists |
| `forums`, `forum_posts` | Forum categories and posts |
| `comments` | Threaded comments on torrents/artists/etc. |
| `sphinx_*` | Sphinx denormalized data tables |
| `sphinx_index_last_pos` | Delta indexing position tracking |
| `sphinx_delta` | Delta index entries |
| `donations` | Donation history |
| `users_notificationsettings` | Per-user notification preferences |
| `push_notifications` | Pushbullet queue |
| `permissions` | User class permission matrix |
| `locked_accounts` | Locked (suspended) account statuses |

## Notable Classes

| Class | Purpose |
|-------|---------|
| `users.class.php` | User data, stats, permissions |
| `torrents.class.php` | Torrent operations, peer tracking |
| `torrentsearch.class.php` | Sphinx-backed search queries |
| `sphinxql.class.php` | SphinxQL query builder |
| `sphinxqlquery.class.php` | SphinxQL query execution |
| `sphinxqlresult.class.php` | SphinxQL result parsing |
| `forums.class.php` | Forum operations |
| `requests.class.php` | Request system logic |
| `collages.class.php` | Collage management |
| `notificationsmanager.class.php` | Notification dispatch |
| `donations.class.php` | Donation processing and rank |
| `permissions.class.php` | Permission checking |
| `cache.class.php` | Memcached wrapper |
| `userrank.class.php` | User rank/privilege calculation |
| `torrent_form.class.php` | Torrent upload/edit form handling |
| `reports.class.php` | Torrent/user report handling |
| `text.class.php` | BBCode parsing and text utilities |
| `image.class.php` | Image processing and thumbnails |
| `bitcoinrpc.class.php` | Bitcoin donation via bitcoind RPC |

## Security Notes

- XSS and SQL injection vulnerabilities have been addressed in recent versions
- `locked_accounts` provides an intermediate suspension state (full disabled vs. active)
- Passwords follow MySQL's `PASSWORD()` hashing (legacy, pre-bcrypt)
- The `bad_passwords` table stores common weak passwords to prevent their use
- Proxy and VPN detection via `proxies.class.php`
- User agent tracking and validation via `useragent.class.php`

## Support

- **IRC:** `#gazelle` on `irc.what-network.net` -- for bug reports, questions, and codebase discussion
- **GitHub Issues:** Report bugs on the [GitHub issue tracker](https://github.com/whatcd/gazelle/issues)
- **Changelog:** Generated daily at `https://raw.githubusercontent.com/WhatCD/Gazelle/master/docs/CHANGES.txt`

## License

Gazelle is licensed under the [GNU General Public License v3](https://raw.githubusercontent.com/WhatCD/Gazelle/master/docs/COPYING.txt).
