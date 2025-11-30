# Source: https://www.electronjs.org/docs/latest/api/structures/cookie

# Cookie Object

- `name` string - The name of the cookie.
- `value` string - The value of the cookie.
- `domain` string (optional) - The domain of the cookie; this will be normalized with a preceding dot so that it\'s also valid for subdomains.
- `hostOnly` boolean (optional) - Whether the cookie is a host-only cookie; this will only be `true` if no domain was passed.
- `path` string (optional) - The path of the cookie.
- `secure` boolean (optional) - Whether the cookie is marked as secure.
- `httpOnly` boolean (optional) - Whether the cookie is marked as HTTP only.
- `session` boolean (optional) - Whether the cookie is a session cookie or a persistent cookie with an expiration date.
- `expirationDate` Double (optional) - The expiration date of the cookie as the number of seconds since the UNIX epoch. Not provided for session cookies.
- `sameSite` string - The [Same Site](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#SameSite_cookies) policy applied to this cookie. Can be `unspecified`, `no_restriction`, `lax` or `strict`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/cookie.md)