# Source: https://render.com/docs/static-site-headers.md

# HTTP Headers for Static Sites

Because static sites don't have a server-side component that can inject custom [HTTP response headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header), you can define response headers for your static sites in the [Render Dashboard](https://dashboard.render.com).

## Header syntax

The *header path* must be a relative path without the domain. It will be matched with all custom domains attached to your site.

You can use *wildcards* to match arbitrary request paths.

| Path        | Effect                                                                       |
| ----------- | ---------------------------------------------------------------------------- |
| `/*`        | Matches all request paths.                                                   |
| `/blog/*`   | Matches `/blog/`, `/blog/latest-post/`, and all other paths under `/blog/`   |
| `/**/*`     | Matches `/blog/`, `/assets/`, and all other paths with at least two slashes. |
| `/*.css`    | Matches `/tokens.css` and `/mode.css`, but not `/assets/theme.css`           |
| `/**/*.css` | Matches `/assets/theme.css` but not `/tokens.css`                            |

The *name* is the *case-insensitive* name for the header. Examples include:

- `Cache-Control`
- `X-Frame-Options`
- `Referrer-Policy`

The *value* of the header is sent as-is in the response. Examples include:

- `public, max-age=86400`
- `DENY`
- `same-origin`

The header key is normalized and the value is appended to it to form the response:

- `cache-control: public, max-age=86400`
- `x-frame-options: DENY`
- `referrer-policy: same-origin`

---

##### Appendix: Glossary definitions

###### static site

Deploy this *service type* to host a static website (HTML/CSS/JS) over a global CDN at a public URL.

Related article: https://render.com/docs/static-sites.md