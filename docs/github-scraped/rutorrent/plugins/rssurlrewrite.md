# RSSURLRewrite Plugin Documentation

The RSSURLRewrite plugin allows rewriting of RSS feed URLs, useful for proxying or redirecting feeds.

## Use Cases

- Access blocked trackers through a proxy
- Rewrite URLs to point to alternative mirrors
- Convert HTTP to HTTPS or vice versa
- Custom URL transformations

## Configuration

Edit `plugins/rssurlrewrite/conf.php`:

```php
<?php
// URL rewriting rules
// Format: 'original_url' => 'rewritten_url'
$rewriteRules = [
    'http://tracker1.example.com' => 'https://proxy.example.com/tracker1',
    'http://oldtracker.com' => 'http://newtracker.com',
];
?>
```

## Rule Format

| Pattern | Result |
|---------|--------|
| Exact match | `http://site.com` -> `http://newsite.com` |
| Wildcard | `http://*.tracker.com/*` -> `http://mirror.tracker.com/` |

## Examples

### Proxy All Traffic

```php
$rewriteRules = [
    'http://blocked-tracker.net' => 'http://my-proxy.com/http/blocked-tracker.net',
];
```

### Mirror Switching

```php
$rewriteRules = [
    'http://tracker.example.com' => 'http://mirror1.example.com',
    'http://backup.example.com' => 'http://mirror2.example.com',
];
```

### Protocol Change

```php
$rewriteRules = [
    'http://tracker.example.com' => 'https://tracker.example.com',
];
```

## Usage

1. Configure rewrite rules in conf.php
2. Enable RSSURLRewrite plugin
3. RSS feeds matching rules will be automatically rewritten
