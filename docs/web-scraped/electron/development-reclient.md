# Source: https://www.electronjs.org/docs/latest/development/reclient

On this page

# Reclient

> Reclient integrates with an existing build system to enable remote execution and caching of build actions.

Electron has a deployment of a [reclient](https://github.com/bazelbuild/reclient) compatible RBE Backend that is available to all Electron Maintainers. See the [Access](#access) section below for details on authentication. Non-maintainers will not have access to the cluster, but can sign in to receive a `Cache Only` token that gives access to the cache-only CAS backend. Using this should result in significantly faster build times .

## Enabling Reclient[â€‹](#enabling-reclient "Direct link to Enabling Reclient") 

Currently the only supported way to use Reclient is to use our [Build Tools](https://github.com/electron/build-tools). Reclient configuration is automatically included when you set up `build-tools`.

If you have an existing config, you can just set `"reclient": "remote_exec"` in your config file.

## Building with Reclient[â€‹](#building-with-reclient "Direct link to Building with Reclient") 

When you are using Reclient, you can run `autoninja` with a substantially higher `j` value than would normally be supported by your machine.

Please do not set a value higher than **200**. The RBE system is monitored. Users found to be abusing it with unreasonable concurrency will be deactivated.

``` 
autoninja -C out/Testing electron -j 200
```

If you\'re using `build-tools`, appropriate `-j` values will automatically be used for you.

## Access[â€‹](#access "Direct link to Access") 

For security and cost reasons, access to Electron\'s RBE backend is currently restricted to Electron Maintainers. If you want access, please head to `#access-requests` in Slack and ping `@infra-wg` to ask for it. Please be aware that being a maintainer does not *automatically* grant access. Access is determined on a case-by-case basis.

## Support[â€‹](#support "Direct link to Support") 

We do not provide support for usage of Reclient. Issues raised asking for help / having issues will *probably* be closed without much reason. We do not have the capacity to handle that kind of support.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/reclient.md)