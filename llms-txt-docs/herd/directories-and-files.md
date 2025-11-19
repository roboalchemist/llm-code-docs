# Source: https://herd.laravel.com/docs/macos/advanced-usage/directories-and-files.md

# Directories and Files

# Herd Directories and Files

You may find the following files and directories helpful while you are troubleshooting issues with Herd.

## Main directory

The main directory contains all the following config files and directories and is a good start when troubleshooting issues with Herd. You may delete this folder if you plan to re-install Herd from scratch.

```bash  theme={null}
~/Library/Application Support/Herd/
```

## Binaries

You can find all binaries of Herd in this directory. This includes binaries like composer or expose that ship with Herd as well as downloaded binaries like the latest PHP versions.

```bash  theme={null}
~/Library/Application Support/Herd/bin
```

## Config

All config files for all Herd services live in this directory.

```bash  theme={null}
~/Library/Application Support/Herd/config
```

### nginx

The nginx directory contains a `herd.conf` and the `nginx.conf`. Herd uses both to decide which sites it serves and what happens to files. In case you see a `Bad Gateway` error, there could be an issue in one of these files.

```bash  theme={null}
~/Library/Application Support/Herd/config/nginx
```

Site-specific Nginx configuration files are located in the following directory:

```bash  theme={null}
~/Library/Application Support/Herd/config/valet/Nginx
```

### php

This directory contains all `php.ini` files for all PHP versions on your machine. If you use Herd Pro, it also contains `debug.ini` files that Xdebug uses when you enable it for a request. If you're in debug mode, Herd loads the normal `php.ini` and applies the `debug.ini` on top.

```bash  theme={null}
~/Library/Application Support/Herd/config/php
```

### Log

Herd stores all logs of nginx and php-fpm in this directory. It may also contain mail logs if you use Herd Pro.

```bash  theme={null}
~/Library/Application Support/Herd/Log
```
