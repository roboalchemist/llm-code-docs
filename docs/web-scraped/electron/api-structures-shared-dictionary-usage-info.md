# Source: https://www.electronjs.org/docs/latest/api/structures/shared-dictionary-usage-info

# SharedDictionaryUsageInfo Object

- `frameOrigin` string - The origin of the frame where the request originates. Itâ€™s specific to the individual frame making the request and is defined by its scheme, host, and port. In practice, will look like a URL.
- `topFrameSite` string - The site of the top-level browsing context (the main frame or tab that contains the request). Itâ€™s less granular than `frameOrigin` and focuses on the broader \"site\" scope. In practice, will look like a URL.
- `totalSizeBytes` number - The amount of bytes stored for this shared dictionary information object in Chromium\'s internal storage (usually Sqlite).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/shared-dictionary-usage-info.md)