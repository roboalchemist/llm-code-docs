# Source: https://docs.upsun.com/languages/php/swoole.md

# Swoole


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

Swoole is a PHP extension that extends PHP core with a coroutine based asynchronous network application framework designed for building large scale concurrent systems.

Unlike PHP-FPM’s stateless operating, Swoole relies on establishing persistent connections with every user, sending and receiving data in real-time.

[Swoole](https://github.com/swoole/swoole-src) and [Open Swoole](https://openswoole.com/) are two forked libraries pursuing that goal.

**Note**: 

The ``swoole`` and ``openswoole`` extensions are [available by default](https://docs.upsun.com/languages/php/extensions.md) on Upsun PHP 8.2 Upsun containers.

For other versions of PHP, you can install both extensions manually by following the instructions on this page. 
You need:

- PHP 7.3+ for Swoole
- PHP 7.4.0+ for Open Swoole
- The [Swoole installation script](https://raw.githubusercontent.com/platformsh/snippets/main/src/install_swoole.sh).
  **Note**: 

Currently, the installation script is compatible with PHP <=8.0. It is **not** compatible with PHP 8.3,
and the ``swoole`` and ``openswoole`` extensions are **not** available on Upsun PHP 8.3 containers yet.

## Install

Install the PHP extension for Swoole or Open Swoole during the build.

Take advantage of an [installation script](https://raw.githubusercontent.com/platformsh/snippets/main/src/install_swoole.sh).
You need to pass 2 parameters:

* Which Swoole project to use: `openswoole` or `swoole`
* Which version to install

```yaml  {location=".upsun/config.yaml"}
applications:
    app:
        type: 'php:<VERSION>'
        hooks:
            build: |
                set -e
                ...
                curl -fsS https://raw.githubusercontent.com/platformsh/snippets/main/src/install_swoole.sh | { bash /dev/fd/3 openswoole 4.11.0 ; } 3<&0
```

## Use

Override the default web server with a [custom start command](https://docs.upsun.com/languages/php.md#alternate-start-commands).
Octane should listen on a TCP socket.

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    web:
      upstream:
        socket_family: tcp
        protocol: http
      commands:
        start: php <PATH_TO_SWOOLE_START_COMMAND> --port=$PORT
      locations:
        "/":
          passthru: true
          scripts: false
          allow: false
```

