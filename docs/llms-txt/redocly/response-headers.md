# Source: https://redocly.com/docs/realm/config/response-headers.md

# `responseHeaders`


Custom headers are added to the response header object if requested resource matches a configured pattern.

## Options

### Patterns map

| Option | Type | Description |
|  --- | --- | --- |
| *{glob pattern}* | [[Header object](#header-object)] | **REQUIRED.** A glob pattern used to match requested resource.
It can match any assets, routes, or both. |


### Header object

| Option | Type | Description |
|  --- | --- | --- |
| name | string | Response header name |
| value | string | Response header value |


## Examples

The following is an example of custom headers for CSS, JS files, and a /my-markdown/ route:


```yaml
responseHeaders:
  '**/*.js':
    - name: X-Content-Type-Options
      value: nosniff
    - name: Cache-Control
      value: no-cache

  '**/*.css':
    - name: X-XSS-Protection
      value: 1; mode=block

  /my-markdown/:
    - name: X-Frame-Options
      value: DENY
```

## Resources

- **[Block search indexing](/docs/realm/config/seo#block-indexing-with-response-headers)** - Use responseHeaders to control search engine indexing and SEO optimization strategies