# Source: https://www.electronjs.org/docs/latest/api/structures/shared-dictionary-info

# SharedDictionaryInfo Object

- `match` string - The matching path pattern for the dictionary which was declared in \'use-as-dictionary\' response header\'s `match` option.
- `matchDestinations` string\[\] - An array of matching destinations for the dictionary which was declared in \'use-as-dictionary\' response header\'s `match-dest` option.
- `id` string - The Id for the dictionary which was declared in \'use-as-dictionary\' response header\'s `id` option.
- `dictionaryUrl` string - URL of the dictionary.
- `lastFetchTime` Date - The time of when the dictionary was received from the network layer.
- `responseTime` Date - The time of when the dictionary was received from the server. For cached responses, this time could be \"far\" in the past.
- `expirationDuration` number - The expiration time for the dictionary which was declared in \'use-as-dictionary\' response header\'s `expires` option in seconds.
- `lastUsedTime` Date - The time when the dictionary was last used.
- `size` number - The amount of bytes stored for this shared dictionary information object in Chromium\'s internal storage (usually Sqlite).
- `hash` string - The sha256 hash of the dictionary binary.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/shared-dictionary-info.md)