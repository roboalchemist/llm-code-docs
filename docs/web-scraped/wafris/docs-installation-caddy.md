# Source: https://wafris.org/docs/installation/caddy/

Title: Caddy

URL Source: https://wafris.org/docs/installation/caddy/

Markdown Content:
[](https://wafris.org/docs/installation/caddy/#wafris-caddy-installation) Wafris Caddy Installation
---------------------------------------------------------------------------------------------------

[](https://wafris.org/docs/installation/caddy/#build-caddy-with-wafris) Build Caddy with Wafris
-----------------------------------------------------------------------------------------------

The Wafris client for Caddy needs to be compiled into your Caddy runtime. Generate a custom Caddy build that includes Wafris from [https://caddyserver.com/download](https://caddyserver.com/download), or use the xcaddy utility to build from source:

```
xcaddy build --with github.com/Wafris/wafris-caddy
```

[](https://wafris.org/docs/installation/caddy/#setup) Setup
-----------------------------------------------------------

### [](https://wafris.org/docs/installation/caddy/#1-connect-to-wafris-hub) 1. Connect to Wafris Hub

Go to [https://wafris.org/hub](https://wafris.org/hub) to create a new account and follow the instructions. Wafris Hub will provide you with a fully pre-configured setup you can use for testing.

### [](https://wafris.org/docs/installation/caddy/#2-install-the-wafris-caddy-module) 2. Install the Wafris Caddy module

Either generate a custom Caddy build that includes Wafris from [https://caddyserver.com/download](https://caddyserver.com/download), or use the `xcaddy` utility to build from source:

```
xcaddy build --with github.com/Wafris/wafris-caddy
```

Download xcaddy at [https://github.com/caddyserver/xcaddy](https://github.com/caddyserver/xcaddy)

### [](https://wafris.org/docs/installation/caddy/#3-set-your-redis-connection-in-your-caddyfile) 3. Set your Redis connection in your Caddyfile

Add the `wafris` directive to your Caddyfile. The directive takes a single argument, which is the Redis URL you received in Step 1.

```
route {
  # this redis url assumes you are running redis on your local machine for testing purposes
  wafris "redis://localhost:6379?protocol=3"
}
```

These routes are usually nesting in a siteblock such as:

```
localhost {
  route {
    wafris "redis://localhost:6379?protocol=3"
  }
}
```

or

```
example.com {
  reverse_proxy :4000 {
  }

  route {
    wafris "redis://localhost:6379?protocol=3"
  }
}
```

* * *
