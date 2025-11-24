# Source: https://herd.laravel.com/docs/macos/sites/nginx-configuration.md

# Nginx Configuration

# Advanced Nginx Configuration

Herd ships with a default Nginx configurations that is suitable for most projects. However, you can customize the
Nginx settings to fit your specific needs. You can do this in multiple ways and depending on your requirements. Some
settings can (and **must**) be configured via the Herd UI, while others require you to edit the Nginx configuration files directly.

## Via Herd

The most common configurations that usually require changes in your Nginx configuration are the maximum file upload size and the memory limit.
You can change these settings via the Herd UI within the PHP settings section. You can either configure them for all
PHP versions or set specific values per PHP version.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ae85e28aa0c761497d5f08c59dba198b" data-og-width="1460" width="1460" data-og-height="1300" height="1300" data-path="images/docs/nginx-php-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f815b3454614663d7dd74d9117419766 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b2b55c50bbdaae3e42c8644867854e92 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9006f0c3e98d4b76a1f1625c67654ba8 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=383fcfb8f83b62c0f7efe9d780d09ef8 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dc2c263831bd081462e525cb93739918 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=399463c5e0c19f51904e66c6e9292e58 2500w" />
</Frame>

You can also change the PHP version for a specific site via the Herd UI. You can either do that in the sites settings or
via the command line by running `herd isolate 8.3` (or any other version you want to use). This creates a dedicated nginx
configuration file for the specified PHP version and use this version for all web request of the current site.

To use the same version via the command line, you can run `herd php artisan ...` or `herd composer ...` instead of just using `php artisan ...` or `composer ...`.
This will ensure that the correct PHP version is used for the command.

If you secure a site with a TLS/SSL certificate, this creates a dedicated Nginx configuration file for the site and you
can make further changes to the Nginx configuration for this site in this file (see below).

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=30612f7cbdc58b29c6e35d6caa4449c6" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/nginx-php-versions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8488ec9029dd12b00bfa25ed75ee6d8f 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0766ca141417d11f864cd79ceec0206e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f82f5f735b085314d12c7c6713889e33 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e29c37369a1a5e34e7875a53a5140c6e 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=00d2b87b958053d69d9eeefa618656c3 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1b119b300c3b3e2355648a35ca39cfb3 2500w" />
</Frame>

## Customizing the global nginx configuration

Herd comes with default configuration files that are in your Herd configuration directory a `~/Library/Application Support/Herd/config/nginx`.
This directory contains the files `nginx.conf` and `herd.conf` that Herd loads on every request. You can edit these files
to make global changes to all projects – but we recommend only changing site-specific files because we might rewrite these files in future updates.

## Customizing the site-specific nginx configuration

If you isolate the PHP version for a site or secure it with a TLS/SSL certificate, Herd creates a dedicated Nginx
configuration file for this site. This file is located at `~/Library/Application Support/Herd/config/valet/Nginx` and named
after the site domain. For example, if your site is `herd.laravel.com.test`, the file will be named `herd.laravel.com.test`.

You can edit this file to make site-specific changes to the Nginx configuration but make sure to keep Herd specific elements like the
isolated PHP version or references to the TLS/SSL certificate intact.

## CORS

Herd does not ship with a specific CORS configuration because we believe that your local environment should match your
standard production environment as closely as possible. If you need to configure CORS for your project, you can do that similar to
how you would do it in production and either create a global CORS configuration for all sites or add the required header in your site-specific file.

```
# CORS Rules
add_header Access-Control-Allow-Origin *;
# END of CORS Rules #
```

### CORS in Laravel

For the Laravel framework, you publish the CORS middleware as described
in the [Laravel documentation](https://laravel.com/docs/12.x/routing#cors).
