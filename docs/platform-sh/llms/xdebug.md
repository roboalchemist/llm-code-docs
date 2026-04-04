# Source: https://docs.upsun.com/languages/php/xdebug.md

# Using Xdebug


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

[Xdebug](https://xdebug.org/) is a real-time debugger extension for PHP.
While usually used for local development, it can also be helpful for debugging aberrant behavior on the server.

As configured on Upsun, it avoids any runtime overhead for non-debug requests, even in production, and only allows connections via SSH tunnels to avoid any security issues.

Note that Xdebug runs only on your app containers.
So you can't use it for [worker containers](https://docs.upsun.com../../create-apps/workers.md).

Also, note that if you use a [custom start command](https://docs.upsun.com/languages/php.md#alternate-start-commands),
Xdebug is automatically disabled.

## Before you begin

The following table shows the PHP versions where Xdebug is available:

| 5.4 | 5.5 | 5.6 | 7.0 | 7.1 | 7.2 | 7.3 | 7.4 | 8.0 | 8.1 | 8.2 | 8.3 | 8.4 | 8.5 |
| 

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

You also need:

- The Upsun [CLI](https://docs.upsun.com../../administration/cli.md)
- A Xdebug-compatible IDE installed on your machine.
    For setup instructions, consult your IDE's Xdebug documentation, such as that for [PHPStorm](https://www.jetbrains.com/help/phpstorm/configuring-xdebug.md).

## 1. Set up Xdebug

Xdebug runs as a second PHP-FPM process used only for debugging requests, leaving the normal process unaffected.

To enable Xdebug, add the following to your [app configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md):

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    runtime:
      xdebug:
        idekey: <YOUR_KEY>
```
<YOUR_KEY> can be any arbitrary alphanumeric string.

When that key is defined, Upsun starts a second PHP-FPM process on the container that's identically configured but also has Xdebug enabled.
Only incoming requests that have an Xdebug cookie or query parameter set are forwarded to the debug PHP-FPM process.
All other requests are directed to the normal PHP-FPM process and thus have no performance impact.

If you have enabled the [router cache](https://docs.upsun.com../../define-routes/cache.md),
you need to explicitly add the Xdebug cookie (`XDEBUG_SESSION`) to the cookie allowlist.
Depending on the cookies already listed, the result should look similar to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'php:8.5'
    runtime:
      xdebug:
        idekey: <YOUR_KEY>

routes:
  "https://{default}/":
    # ...
    cache:
      enabled: true
      cookies: ['/^SS?ESS/', 'XDEBUG_SESSION']
```
Xdebug has several configuration options available.
They can be set the same way as any other [PHP setting](https://docs.upsun.com/languages/php.md#php-settings).
For a full list of available options, consult the [Xdebug documentation](https://xdebug.org/docs/).

## 2. Use Xdebug

### Open a tunnel

To open an SSH tunnel to the server from a local checkout of your app, run the following [CLI command](https://docs.upsun.com../../administration/cli.md) :

```bash
upsun environment:xdebug
```

That SSH tunnel allows your IDE and the server to communicate debug information securely.

By default, Xdebug operates on port `9003`.
Generally, it's best to configure your IDE to use that port.
To use an alternate port, use the `--port` flag.

To close the tunnel and terminate the debug connection, press Ctrl + C.

### Install an Xdebug helper

While Xdebug can be triggered from the browser by adding a special query parameter, the preferred way is to use a browser plugin helper.
Helpers are available for [Firefox](https://addons.mozilla.org/en-US/firefox/addon/xdebug-helper-for-firefox/)
and [Chrome](https://chrome.google.com/webstore/detail/xdebug-helper/eadndfjplgieldjbigjakmdgkmoaaaoc).
Their respective plugin pages document how to trigger them when needed.

## 3. Configure your IDE

Follow the instructions for your IDE, such as those for [PHPStorm](https://www.jetbrains.com/help/phpstorm/configuring-xdebug.md).

The common steps for setup usually include:

1. Configuring the Xdebug debug port and making sure it's set to the expected value (`9003` as default or the value you chose with `--port` when opening the tunnel).
2. Making sure that external connections are allowed.
3. Adding a new server for your Upsun environment.
    The Host should be the hostname of the environment on Upsun you are debugging.
    The Port should always be `443` and the Debugger set to `Xdebug`.
4. Ensuring path mappings is enabled.
    This lets you define what remote paths on the server correspond to what path on your local machine.
    In the majority of cases you can just define [your app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory)
    to map to `myapp`.
5. Listening for connections.
6. Starting debugging. While in listen mode, start the `upsun xdebug` tunnel.
    Use the Xdebug helper plugin for your browser to enable debugging.
    Set a break point in your app, then load a page in your browser.
    The request should pause at the break point and allow you to examine the running app.

