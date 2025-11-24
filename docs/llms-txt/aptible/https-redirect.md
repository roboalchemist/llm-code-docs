# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-redirect.md

# HTTPS Redirect

<Tip> Your app can detect which protocol is being used by examining a request's `X-Forwarded-Proto` header. See [HTTP Request Headers](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/http-request-headers) for more information.</Tip>

By default, [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) accept traffic over both HTTP and HTTPS.

To disallow HTTP and redirect traffic to HTTPS at the Endpoint level, you can set the `FORCE_SSL` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable to `true` (it must be set to the string `true`, not just any value).

# `FORCE_SSL` in detail

Setting `FORCE_SSL=true` on an app causes 2 things to happen:

* Your HTTP(S) Endpoints will redirect all HTTP requests to HTTPS.
* Your HTTP(S) Endpoints will set the `Strict-Transport-Security` header on responses with a max-age of 1 year.

Make sure you understand the implications of setting the `Strict-Transport-Security` header before using this feature.

In particular, by design, clients that connect to your site and receive this header will refuse to reconnect via HTTP for up to a year after they receive the `Strict-Transport-Security` header.

# Enabling `FORCE_SSL`

To set `FORCE_SSL`, you'll need to use the [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) command.

The value must be set to the string `true` (e.g., setting to `1` won't work).

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        "FORCE_SSL=true"
```
