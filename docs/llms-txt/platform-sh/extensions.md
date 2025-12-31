# Source: https://docs.upsun.com/languages/php/extensions.md

# Extensions

**Note**: 

You can now use the [Upsun composable image (BETA)](https://docs.upsun.com/create-apps/app-reference/composable-image.md) to install runtimes and tools in your application container.
When using the composable image, see how you can:

 - [Manage PHP extensions](https://docs.upsun.com/create-apps/app-reference/composable-image.md#php-extensions-and-python-packages)
 - [Modify your PHP runtime](https://docs.upsun.com/languages/php.md#modify-your-php-runtime-when-using-the-composable-image)

PHP has a number of [extensions](https://pecl.php.net/) developed by members of the community.
Some of them are available for Upsun containers.

You can define the PHP extensions you want to enable or disable:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    runtime:
      extensions:
        - raphf
        - http
        - igbinary
        - redis
      disabled_extensions:
        - sqlite3
```
You can also [include configuration options](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#extensions) for specific extensions.

The following table shows all extensions that are available (Avail) and on by default (Def).
You can turn on the available ones with the `extensions` key
and turn off those on by default with the `disabled_extensions` key.
(Extensions marked with `*` are built in and can't be turned off.)

| Extension | 5.4 | 5.5 | 5.6 | 7.0 | 7.1 | 7.2 | 7.3 | 7.4 | 8.0 | 8.1 | 8.2 | 8.3 | 8.4 | 8.5 |
| ``amqp`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``apc`` |

              Avail

| ``apcu`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``apcu_bc`` |

              Avail

              Avail

              Avail

              Avail

              Avail

| ``applepay`` |

              Avail

              Avail

              Avail

              Avail

| ``bcmath`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``blackfire`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``bz2`` |

              Avail

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``calendar`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``ctype`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``curl`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``datadog`` |

              Avail

              Avail

| ``datadog-profiling`` |

              Avail

              Avail

| ``dba`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``dom`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``enchant`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``event`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``exif`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``ffi`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``fileinfo`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``ftp`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``gd`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``gearman`` |

              Avail

              Avail

              Avail

| ``geoip`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``gettext`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``gmp`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``gnupg`` |

              Avail

              Avail

              Avail

| ``http`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``iconv`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``igbinary`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``imagick`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail with``webp``

              Avail with``webp``

              Avail with``webp``

              Avail with``webp``

              Avail

| ``imap`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``interbase`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``intl`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``ioncube`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``json`` |

              Def

              Def

              Def

              Def

              Def

              Def

              *

              *

              *

              *

              *

              *

| ``ldap`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``mailparse`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``mbstring`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``mcrypt`` |

              Def

              Def

              Def

              Avail

              Avail

| ``memcache`` |

              Avail

              Avail

              Avail

| ``memcached`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``mongo`` |

              Avail

              Avail

              Avail

| ``mongodb`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``msgpack`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``mssql`` |

              Avail

              Avail

              Avail

| ``mysql`` |

              Def

              Def

              Def

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``mysqli`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``mysqlnd`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``newrelic`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``oauth`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``odbc`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``opcache`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``openswoole`` |

              Avail

              Avail

              Avail

| ``opentelemetry`` |

              Avail

              Avail

              Avail

| ``pdo`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``pdo_dblib`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``pdo_firebird`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``pdo_mysql`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``pdo_odbc`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``pdo_pgsql`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``pdo_sqlite`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``pdo_sqlsrv`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``pecl-http`` |

              Avail

| ``pgsql`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``phar`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``phpdbg`` |

              Avail

| ``pinba`` |

              Avail

              Avail

              Avail

| ``posix`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``propro`` |

              Avail

| ``protobuf`` |

              Avail

              Avail

| ``pspell`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``pthreads`` |

              Avail

              Avail

| ``raphf`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``rdkafka`` |

              Avail

              Avail

              Avail

              Avail

| ``readline`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``recode`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``redis`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``shmop`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``simplexml`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``snmp`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``soap`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``sockets`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``sodium`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``sourceguardian`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``spplus`` |

              Avail

              Avail

| ``sqlite3`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``sqlsrv`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``ssh2`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``swoole`` |

              Avail

              Avail

              Avail

| ``sybase`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``sysvmsg`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``sysvsem`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``sysvshm`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``tideways`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``tideways_xhprof`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``tidy`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``tokenizer`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``uuid`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``uv`` |

              Avail

              Avail

| ``wddx`` |

              Avail

              Avail

              Avail

              Avail

              Avail

| ``xcache`` |

              Avail

              Avail

| ``xdebug`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``xhprof`` |

              Avail

              Avail

              Avail

| ``xml`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``xmlreader`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``xmlrpc`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``xmlwriter`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

| ``xsl`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``yaml`` |

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

              Avail

| ``zbarcode`` |

              Avail

              Avail

              Avail

              Avail

| ``zendopcache`` |

              Def

              *

              *

              *

              *

              *

              *

              *

              *

              *

              *

              *

              *

              *

| ``zip`` |

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Def

              Avail

              Def

Some built-in modules are always on:

- `date`
- `filter`
- `hash`
- `json` (from 8.0)
- `libxml`
- `openssl`
- `pcntl`
- `pcre`
- `Reflection`
- `session`
- `SPL`
- `standard`
- `Zend OPcache` (from 5.5)
- `zlib`

To see a complete list of the compiled PHP extensions, run the following [CLI command](https://docs.upsun.com../../administration/cli/_index.md):

```bash
upsun ssh "php -m"
```

## Custom PHP extensions

It's possible to use an extension not listed here,
but it takes slightly more work:

1. Download the `.so` file for the extension as part of your build hook using `curl` or similar.
   It can also be added to your Git repository if the file isn't publicly downloadable,
   but committing large binary blobs to Git is generally not recommended.

2. Load the extension using an absolute path by [customizing the PHP settings](https://docs.upsun.com/languages/php.md#customize-php-settings)
   For example, if the extension is named `spiffy.so` and is in your [app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory),
   your configuration looks like the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    variables:
      php:
        extension: /app/spiffy.so
```

