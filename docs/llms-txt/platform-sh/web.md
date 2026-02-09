# Source: https://docs.upsun.com/administration/web.md

# Source: https://docs.upsun.com/create-apps/web.md

# Source: https://docs.upsun.com/create-apps/image-properties/web.md

# web


A web instance that defines how the web application is served.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images.

Use the `web` key to configure the web server running in front of your app.

For **single-runtime images**, default values might vary based on the image [`type`](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types), which defines the base container used to run the application.

| Name        | Type                                       | Required                      | Description                                          |
|-------------|--------------------------------------------|-------------------------------|------------------------------------------------------|
| `commands`  | A [web commands dictionary](#web-commands) | See [`start`](#start) | The command to launch your app.                      |
| `upstream`  | An [upstream dictionary](#upstream)        |                               | How the front server connects to your app.           |
| `locations` | A [locations dictionary](#locations)       |                               | How the app container responds to incoming requests. |

See some [examples of how to configure what's served](https://docs.upsun.com../web.md).

### Web commands

| Name         | Type     | Required                      | Description                                                                                         |
|--------------|----------|-------------------------------|-----------------------------------------------------------------------------------------------------|
| [`pre_start`](#pre_start)  | `string` |                               | Command run just prior to `start`, which can be useful when you need to run _per-instance_ actions. Non-blocking. |
| [`start`](#start)      | `string` | Typically, except for PHP; see [`start`](#start). | The command to launch your app. If it terminates, it's restarted immediately.                       |
| [`post_start`](#post_start) | `string` |                               | Command runs **after** the `start` command and **before** adding the container to the router. Can be used to ensure app is active before routing traffic to it.       |

### `pre_start` command {#pre_start}
The `pre_start` command is **not blocking**, which means the `deploy` hook may start running **before** the `pre_start` command finishes. This can lead to unexpected behavior if `pre_start` performs setup tasks that `deploy` depends on.
To avoid issues, make sure any critical initialization in `pre_start` can complete quickly or is safe to run concurrently with `deploy`.

### `start` command {#start}
On all containers other than PHP, it's a best practice to include a `start` command. This command runs every time your app is restarted, regardless of whether new code is deployed.

On PHP containers, `start` is optional and defaults to starting PHP-FPM (`/usr/bin/start-php-app`).
You can set it explicitly on a PHP container to run a dedicated process,
such as [React PHP](https://github.com/platformsh-examples/platformsh-example-reactphp)
or [Amp](https://github.com/platformsh-examples/platformsh-example-amphp).
See [Alternate start commands](https://docs.upsun.com/languages/php.md#alternate-start-commands) in the PHP topic.

**Note**: 

Do not run a ``start`` process in the background by using ``&`` syntax.
The Upsun supervisor interprets that syntax as the command terminating and starts another copy, creating a loop that continues until the container crashes.
Run the command as usual and allow the Upsun supervisor to manage it.

### `post_start` command {#post_start}
You can use the `post_start` command to ensure your app is fully active before traffic is routed to it. This command can perform checks or wait until your application starts listening on the expected port. 

For example, if your framework needs several seconds to initialize (for example, to build caches or establish database connections), `post_start` can help coordinate the handover to ensure that the app receives traffic only after it is initialized.

#### Example:

This example contains two web commands:

- A `start` command that starts the application every time, whether or not new code is deployed. 
- A `post_start` command that repeatedly checks whether a service on `localhost` is responding.

```yaml {}
applications:
  <APP_NAME>:
    type: "python:3.14"
    source:
      root: "/"
    web:
      commands:
        start: 'uwsgi --ini conf/server.ini'
        post_start: |
        date
        curl -sS --retry 20 --retry-delay 1 --retry-connrefused localhost -o /dev/null        
```

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    type: "composable:25.11"
    source:
      root: "/"
    stack: 
      runtimes: [ "python@3.14" ]
    web:
      commands:
        start: 'uwsgi --ini conf/server.ini'
        post_start: |
        date
        curl -sS --retry 20 --retry-delay 1 --retry-connrefused localhost -o /dev/null        
```

### `upstream` {#upstream}

```yaml {}
applications:
  myapp:
    type: 'python:3.14'
    source:
      root: "/"
    web:
      upstream:
        socket_family: tcp
        protocol: http
```

| Name | Type | Required | Description | Default |
| ``socket_family`` | ``tcp`` or ``unix`` |  | Whether your app listens on a Unix or TCP socket. | Defaults to ``tcp`` for all [primary runtimes](https://docs.upsun.com/create-apps/app-reference/composable-image.md#multiple-runtimes-primary-runtime) except PHP; for PHP the default is ``unix``. |
| ``protocol`` | ``http`` or ``fastcgi`` |  | Whether your app receives incoming requests over HTTP or FastCGI. | Default varies based on the [primary runtimes](https://docs.upsun.com/create-apps/app-reference/composable-image.md#multiple-runtimes-primary-runtime). |
For PHP, the defaults are configured for PHP-FPM and shouldn’t need adjustment.
For all other containers, the default for ``protocol`` is ``http``.
The following example is the default on non-PHP containers:

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    type: "composable:25.11"
    source:
      root: "/"
    stack: 
      runtimes: [ "python@3.14" ]
    web:
      upstream:
        socket_family: tcp
        protocol: http
```

#### Where to listen

Where to listen depends on your setting for `web.upstream.socket_family` (defaults to `tcp`).

| `socket_family` | Where to listen                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `tcp`           | The port specified by the [`PORT` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables)               |
| `unix`          | The Unix socket file specified by the [`SOCKET` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables) |

If your application isn't listening at the same place that the runtime is sending requests,
you see `502 Bad Gateway` errors when you try to connect to your website.

### `locations` {#locations}

Each key in the `locations` dictionary is a path on your site with a leading `/`.
For `example.com`, a `/` matches `example.com/` and `/admin` matches `example.com/admin`.
When multiple keys match an incoming request, the most-specific applies.

The following table presents possible properties for each location:

| Name | Type | Default | Description |
| ``root`` | ``string`` |  | The directory to serve static assets for this location relative to the app’s root directory ([see ](https://docs.upsun.com/create-apps/image-properties/source.md)). Must be an actual directory inside the root directory. |
| ``passthru`` | ``boolean`` or  ``string`` | ``false`` | Whether to forward disallowed and missing resources from this location to the app. A string is a path with a leading ``/`` to the controller, such as ``/index.php``. <BR> <BR> If your app is in PHP, when setting ``passthru`` to ``true``, you might want to set ``scripts`` to ``false`` for enhanced security. This prevents PHP scripts from being executed from the specified location. You might also want to set ``allow`` to ``false`` so that not only PHP scripts can’t be executed, but their source code also can’t be delivered. |
| ``index`` | ``string`` array or ``null`` |  | Files to consider when serving a request for a directory. When set, requires access to the files through the ``allow`` or ``rules`` keys. |
| ``expires`` | ``string`` | ``-1`` | How long static assets are cached. The default means no caching. Setting it to a value enables the ``Cache-Control`` and ``Expires`` headers. Times can be suffixed with ``ms`` = milliseconds, ``s`` = seconds, ``m`` = minutes, ``h`` = hours, ``d`` = days, ``w`` = weeks, ``M`` = months/30d, or ``y`` = years/365d. |
| ``allow`` | ``boolean`` | ``true`` | Whether to allow serving files which don’t match a rule. |
| ``scripts`` | ``boolean`` |  | Whether to allow scripts to run. Doesn’t apply to paths specified in ``passthru``. Meaningful only on PHP containers. |
| ``headers`` | A headers dictionary |  | Any additional headers to apply to static assets, mapping header names to values (see [Set custom headers on static content](https://docs.upsun.com/create-apps/web/custom-headers.md)). Responses from the app aren’t affected. |
| ``request_buffering`` | A [request buffering dictionary](#request-buffering) | See below | Handling for chunked requests. |
| ``rules`` | A [rules dictionary](#rules) |  | Specific overrides for specific locations. |

#### Rules

The rules dictionary can override most other keys according to a regular expression.
The key of each item is a regular expression to match paths exactly.
If an incoming request matches the rule, it's handled by the properties under the rule,
overriding any conflicting rules from the rest of the `locations` dictionary.

Under `rules`, you can set all the other possible [`locations` properties](#locations)
except `root`, `index`, `rules` and `request_buffering`.

In the following example, the `allow` key disallows requests for static files anywhere in the site.
This is overridden by a rule that explicitly allows common image file formats.

```yaml {}
applications:
  myapp:
    type: 'python:3.14'
    source:
      root: "/"
    web:
      locations:
        '/':
          # Handle dynamic requests
          root: 'public'
          passthru: '/index.php'
          # Disallow static files
          allow: false
          rules:
            # Allow common image files only.
            '\.(jpe?g|png|gif|svgz?|css|js|map|ico|bmp|eot|woff2?|otf|ttf)$':
              allow: true
```

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    type: "composable:25.11"
    source:
      root: "/"
    stack: 
      runtimes: [ "python@3.14" ]
    web:
      locations:
        '/':
          # Handle dynamic requests
          root: 'public'
          passthru: '/index.php'
          # Disallow static files
          allow: false
          rules:
            # Allow common image files only.
            '\.(jpe?g|png|gif|svgz?|css|js|map|ico|bmp|eot|woff2?|otf|ttf)$':
              allow: true
```

#### Request buffering

Request buffering is enabled by default to handle chunked requests as most app servers don't support them.
The following table shows the keys in the `request_buffering` dictionary:

| Name               | Type      | Required | Default | Description                               |
|--------------------|-----------|----------|---------|-------------------------------------------|
| `enabled`          | `boolean` | Yes      | `true`  | Whether request buffering is enabled.     |
| `max_request_size` | `string`  |          | `250m`  | The maximum size to allow in one request. |

The default configuration would look like this:

```yaml {}
applications:
  myapp:
    type: 'python:3.14'
    source:
      root: "/"
    web:
      locations:
        '/':
          passthru: true
          request_buffering:
            enabled: true
            max_request_size: 250m
```

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    type: "composable:25.11"
    source:
      root: "/"
    stack: 
      runtimes: [ "python@3.14" ]
    web:
      locations:
        '/':
          passthru: true
          request_buffering:
            enabled: true
            max_request_size: 250m
```


