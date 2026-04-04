# Source: https://docs.ghost.org/themes/helpers/data/readable_url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# readable_url

> Usage: `{{readable_url URL}}`

***

The `readable_url` helper outputs a human-readable URL by stripping out its protocol, www, query paramters, and hash fragments. It doesn’t strip out any subdomains or pathnames. This helper pairs well with the [`recommendations` helper](/themes/helpers/data/recommendations) to output more readable URLs.

See the examples below to understand the helper’s expected output:

```handlebars  theme={"dark"}
{{readable_url "https://google.com"}}
<!-- removes the "https://" protocol. Outputs: "google.com" -->

{{readable_url "www.google.com"}}
<!-- removes "www". Outputs: "google.com" -->

{{readable_url "https://google.com?foo=bar&dog=love"}}
<!-- removes query parameters. Outputs: "google.com" -->

{{readable_url "https://google.com#section-1"}}
<!-- removes hash fragments. Outputs: "google.com" -->

{{readable_url "https://ghost.org/about"}}
<!-- pathnames are not removed. Outputs: "ghost.org/about" -->

{{readable_url "https://account.ghost.org"}}
<!-- subdomains are not removed. Outputs: "account.ghost.org" -->
```


Built with [Mintlify](https://mintlify.com).