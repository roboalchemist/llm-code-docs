# Source: https://www.electronjs.org/docs/latest/api/structures/custom-scheme

# CustomScheme Object

- `scheme` string - Custom schemes to be registered with options.
- `privileges` Object (optional)
  - `standard` boolean (optional) - Default false.
  - `secure` boolean (optional) - Default false.
  - `bypassCSP` boolean (optional) - Default false.
  - `allowServiceWorkers` boolean (optional) - Default false.
  - `supportFetchAPI` boolean (optional) - Default false.
  - `corsEnabled` boolean (optional) - Default false.
  - `stream` boolean (optional) - Default false.
  - `codeCache` boolean (optional) - Enable V8 code cache for the scheme, only works when `standard` is also set to true. Default false.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/custom-scheme.md)