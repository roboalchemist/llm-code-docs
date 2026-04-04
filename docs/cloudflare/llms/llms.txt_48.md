# Source: https://developers.cloudflare.com/rules/llms.txt

# Rules

Modify incoming requests, change Cloudflare settings, or trigger actions

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/rules/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Rules llms-full.txt](https://developers.cloudflare.com/rules/llms-full.txt) for the complete Rules documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Rules](https://developers.cloudflare.com/rules/index.md): Use Cloudflare Rules to adjust requests and responses, configure settings, and trigger actions for specific requests.

## Rules examples

- [Rules examples](https://developers.cloudflare.com/rules/examples/index.md)

## Configuration Rules

- [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/index.md)
- [Create a configuration rule via API](https://developers.cloudflare.com/rules/configuration-rules/create-api/index.md)
- [Create a configuration rule in the dashboard](https://developers.cloudflare.com/rules/configuration-rules/create-dashboard/index.md)
- [Configuration Rules examples](https://developers.cloudflare.com/rules/configuration-rules/examples/index.md)
- [Define a single configuration rule using Terraform](https://developers.cloudflare.com/rules/configuration-rules/examples/define-single-configuration-terraform/index.md): Create a configuration rule using Terraform to turn off Email Obfuscation and Browser Integrity Check for API requests in a given zone.
- [Configuration Rules settings](https://developers.cloudflare.com/rules/configuration-rules/settings/index.md)

## Cloudflare Snippets

- [Cloudflare Snippets](https://developers.cloudflare.com/rules/snippets/index.md)
- [Configure Snippets via API](https://developers.cloudflare.com/rules/snippets/create-api/index.md)
- [Create a snippet in the dashboard](https://developers.cloudflare.com/rules/snippets/create-dashboard/index.md)
- [Configure Snippets using Terraform](https://developers.cloudflare.com/rules/snippets/create-terraform/index.md)
- [Troubleshoot Snippets](https://developers.cloudflare.com/rules/snippets/errors/index.md)
- [Snippets examples](https://developers.cloudflare.com/rules/snippets/examples/index.md)
- [A/B testing with same-URL direct access](https://developers.cloudflare.com/rules/snippets/examples/ab-testing-same-url/index.md): Set up an A/B test by controlling what response is served based on cookies.
- [Append dates to cookies to use with A/B testing](https://developers.cloudflare.com/rules/snippets/examples/append-dates-to-cookies/index.md): Dynamically set a cookie expiration and test group.
- [Auth with headers](https://developers.cloudflare.com/rules/snippets/examples/auth-with-headers/index.md): Allow or deny a request based on a known pre-shared key in a header. This is not meant to replace the [WebCrypto API](/workers/runtime-apis/web-crypto/).
- [Send Bot Management information to origin](https://developers.cloudflare.com/rules/snippets/examples/bot-data-to-origin/index.md): Send [Bots](/bots/) information to your origin. Refer to [Bot Management variables](/bots/reference/bot-management-variables/) for a full list of available fields.
- [Send suspect bots to a honeypot](https://developers.cloudflare.com/rules/snippets/examples/bots-to-honeypot/index.md): Use the [bot score field](/workers/runtime-apis/request/#incomingrequestcfproperties) to send bots to a honeypot.
- [Bulk redirect based on a map object](https://developers.cloudflare.com/rules/snippets/examples/bulk-redirect-map/index.md): Redirect requests to certain URLs based on a mapped object to the request's URL.
- [Country code redirect](https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/index.md): Redirect a response based on the country code in the header of a visitor.
- [Custom cache](https://developers.cloudflare.com/rules/snippets/examples/custom-cache/index.md): Store, retrieve, and remove assets from cache programmatically. Use this template to optimize performance and implement custom caching strategies.
- [Debugging logs](https://developers.cloudflare.com/rules/snippets/examples/debugging-logs/index.md): Send debugging information in an errored response to a logging service.
- [Define CORS headers](https://developers.cloudflare.com/rules/snippets/examples/define-cors-headers/index.md): Adjust [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) headers and handle preflight requests.
- [Follow redirects from the origin](https://developers.cloudflare.com/rules/snippets/examples/follow-redirects/index.md): Modify the fetch request to follow redirects from the origin, ensuring the client receives the final response.
- [Add HEX timestamp to a request header](https://developers.cloudflare.com/rules/snippets/examples/hex-timestamp/index.md): Add a custom header to requests sent to the origin server with the current timestamp in hexadecimal format for debugging, tracking, or custom routing purposes.
- [Validate JSON web tokens (JWT)](https://developers.cloudflare.com/rules/snippets/examples/jwt-validation/index.md): Extract the JWT token from a header, decode it, and implement validation checks to verify it.
- [Maintenance page](https://developers.cloudflare.com/rules/snippets/examples/maintenance/index.md): Serve a custom maintenance page instead of fetching content from the origin server or cache. Ideal for downtime notifications, planned maintenance, or emergency messages.
- [Override a Set-Cookie header with a certain value](https://developers.cloudflare.com/rules/snippets/examples/override-set-cookies-value/index.md): Get a specific `Set-Cookie` header and update it with a certain value.
- [Redirect 403 Forbidden to a different page](https://developers.cloudflare.com/rules/snippets/examples/redirect-forbidden-status/index.md): If origin responded with `403 Forbidden` error code, redirect to different page.
- [Redirect from one domain to another](https://developers.cloudflare.com/rules/snippets/examples/redirect-replaced-domain/index.md): Redirect all requests from one domain to another domain.
- [Remove fields from API response](https://developers.cloudflare.com/rules/snippets/examples/remove-fields-api-response/index.md): If origin responds with `JSON`, parse the response and delete fields to return a modified response.
- [Remove query strings before sending request to origin](https://developers.cloudflare.com/rules/snippets/examples/remove-query-strings/index.md): Remove certain query strings from a request before passing to the origin.
- [Remove response headers](https://developers.cloudflare.com/rules/snippets/examples/remove-response-headers/index.md): Remove from response all headers that start with a certain name.
- [Return information about the incoming request](https://developers.cloudflare.com/rules/snippets/examples/return-incoming-request-properties/index.md): Respond with information about the incoming request provided by Cloudflareâs global network.
- [Rewrite links on HTML pages](https://developers.cloudflare.com/rules/snippets/examples/rewrite-site-links/index.md): Dynamically rewrite links in HTML responses. This is useful for site migrations and branding updates.
- [Change origin and modify paths](https://developers.cloudflare.com/rules/snippets/examples/route-and-rewrite/index.md): Route requests to a different origin, prepend a directory to the URL path, and remove specific segments.
- [Set security headers](https://developers.cloudflare.com/rules/snippets/examples/security-headers/index.md): Set common security headers such as X-XSS-Protection, X-Frame-Options, and X-Content-Type-Options.
- [Send timestamp to origin as a custom header](https://developers.cloudflare.com/rules/snippets/examples/send-timestamp-to-origin/index.md): Convert timestamp to hexadecimal format and send it as a custom header to the origin.
- [Route to a different origin based on origin response](https://developers.cloudflare.com/rules/snippets/examples/serve-different-origin/index.md): If response to the original request is not `200 OK` or a redirect, send to another origin.
- [Sign requests](https://developers.cloudflare.com/rules/snippets/examples/signing-requests/index.md): Verify a signed request using the HMAC and SHA-256 algorithms or return a 403.
- [Slow down suspicious requests](https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/index.md): Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score.
- [How Snippets work](https://developers.cloudflare.com/rules/snippets/how-it-works/index.md)
- [When to use Snippets vs Workers](https://developers.cloudflare.com/rules/snippets/when-to-use/index.md): This guide helps you determine when to use Snippets or Workers on Cloudflare's global network.

## Transform Rules

- [Transform Rules](https://developers.cloudflare.com/rules/transform/index.md)
- [Transform Rules examples](https://developers.cloudflare.com/rules/transform/examples/index.md)
- [Add a wildcard CORS response header](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/index.md): Create a CORS response header transform rule to add an `Access-Control-Allow-Origin` HTTP header to the response with wildcard as static value. (`cookiename=value`).
- [Add a request header with the current bot score](https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/index.md): Create a request header transform rule to add a `X-Bot-Score` HTTP header to the request with the current bot score.
- [Add request header with a static value](https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/index.md): Create a request header transform rule to add an `X-Source` HTTP header to the request with a static value (`Cloudflare`).
- [Add a request header for subrequests from other zones](https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/index.md): Create a request header transform rule to add an HTTP header when the Workers subrequest comes from a different zone.
- [Add a response header with a static value](https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/index.md): Create a response header transform rule to add a `set-cookie` HTTP header to the response with a static value (`cookiename=value`).
- [Normalize encoded slashes in URL path](https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/index.md): Create a URL rewrite rule (part of Transform Rules) to normalize encoded forward slashes (`%2F`) in the request path to standard slashes (`/`).
- [Remove a request header](https://developers.cloudflare.com/rules/transform/examples/remove-request-header/index.md): Create a request header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the request.
- [Remove a response header](https://developers.cloudflare.com/rules/transform/examples/remove-response-header/index.md): Create a response header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the response.
- [Rewrite blog archive URLs](https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/index.md): Create a transform rule to rewrite the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`.
- [Rewrite path of moved section of a website](https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/index.md): Create a URL rewrite rule (part of Transform Rules) to rewrite everything under `/blog/<PATH>` to `/marketing/<PATH>`.
- [Rewrite path of archived blog posts](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/index.md): Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/news/2012/...` URI paths to `/archive/news/2012/...`.
- [Rewrite path for object storage bucket](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/index.md): Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/files/...` URI paths to `/...`.
- [Rewrite image paths with several URL segments](https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/index.md): Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/images/<FOLDER1>/<FOLDER2>/<FILENAME>` to `/img/<FILENAME>`.
- [Rewrite URL query string](https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/index.md): Create a transform rule to rewrite the request path from `/blog` to `/blog?sort-by=date`.
- [Rewrite page path for visitors in specific countries](https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/index.md): Create two URL rewrite rules (part of Transform Rules) to rewrite the path of the welcome page for visitors in specific countries.
- [Set a response header with the current bot score](https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/index.md): Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response with the current bot score.
- [Set response header with a static value](https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/index.md): Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response to a static value (`Cloudflare`).
- [Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/index.md)
- [Configure Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/configure/index.md): Learn how to configure Managed Transforms.
- [Available Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/index.md): Learn about Cloudflare's Managed Transforms for modifying HTTP headers, including bot protection, TLS client auth, and leaked credentials checks.
- [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/index.md): Learn how to modify HTTP request headers with Cloudflare's rules.
- [Create a request header transform rule via API](https://developers.cloudflare.com/rules/transform/request-header-modification/create-api/index.md)
- [Create a request header transform rule in the dashboard](https://developers.cloudflare.com/rules/transform/request-header-modification/create-dashboard/index.md)
- [Create a rule using Terraform](https://developers.cloudflare.com/rules/transform/request-header-modification/link-create-terraform/index.md)
- [Available fields and functions](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/index.md)
- [Format of HTTP request header names and values](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/header-format/index.md)
- [API parameter reference](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/parameters/index.md)
- [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/index.md)
- [Create a response header transform rule via API](https://developers.cloudflare.com/rules/transform/response-header-modification/create-api/index.md)
- [Create a response header transform rule in the dashboard](https://developers.cloudflare.com/rules/transform/response-header-modification/create-dashboard/index.md)
- [Create a rule using Terraform](https://developers.cloudflare.com/rules/transform/response-header-modification/link-create-terraform/index.md)
- [Available fields and functions](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/fields-functions/index.md)
- [Format of HTTP response header names and values](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/header-format/index.md)
- [API parameter reference](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/index.md)
- [Troubleshoot Transform Rules](https://developers.cloudflare.com/rules/transform/troubleshooting/index.md)
- [URL Rewrite Rules](https://developers.cloudflare.com/rules/transform/url-rewrite/index.md)
- [Create a URL rewrite rule via API](https://developers.cloudflare.com/rules/transform/url-rewrite/create-api/index.md)
- [Create a URL rewrite rule in the dashboard](https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/index.md)
- [Create a rule using Terraform](https://developers.cloudflare.com/rules/transform/url-rewrite/link-create-terraform/index.md)
- [Available fields and functions](https://developers.cloudflare.com/rules/transform/url-rewrite/reference/fields-functions/index.md)
- [URL rewrite parameters](https://developers.cloudflare.com/rules/transform/url-rewrite/reference/parameters/index.md)

## Redirects

- [Redirects](https://developers.cloudflare.com/rules/url-forwarding/index.md)
- [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/index.md)
- [Bulk Redirects concepts](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/index.md): Bulk Redirects work through a combination of URL redirects, a Bulk Redirect list, and a Bulk Redirect rule.
- [Create Bulk Redirects via API](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-api/index.md): Learn how to create Bulk Redirects using the Cloudflare API.
- [Create Bulk Redirects in the dashboard](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/index.md)
- [Bulk Redirects FAQ](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/faq/index.md)
- [How Bulk Redirects work](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/index.md)
- [CSV file format for Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/index.md)
- [Available fields and functions](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/fields-functions/index.md)
- [Bulk Redirects API JSON objects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/index.md)
- [URL redirect parameters](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/index.md)
- [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/index.md)
- [Configure Bulk Redirects using Terraform](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/terraform-example/index.md)
- [Redirect examples](https://developers.cloudflare.com/rules/url-forwarding/examples/index.md)
- [Perform mobile redirects](https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/index.md): Create a redirect rule to redirect visitors using mobile devices to a different hostname.
- [Redirect admin area requests to HTTPS](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/index.md): Create a redirect rule to redirect requests for the administration area of `store.example.com` to HTTPS, keeping the original path and query string.
- [Redirect requests from one domain to another](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/index.md): Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80).
- [Redirect requests from one country to a domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/index.md): Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths.
- [Redirect requests for a domain to a new domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/index.md): Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.
- [Redirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/index.md): Create a redirect rule to redirect all requests for `smallshop.example.com` to a different hostname using HTTPS, keeping the original path and query string.
- [Redirect local visitors to specific subdomains](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/index.md): Create a redirect rule to redirect United Kingdom and France visitors from the `example.com` website's  root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.
- [Redirect visitors to a new page URL](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/index.md): Create a redirect rule to redirect visitors from `/contact-us/` to the page's new path `/contacts/`.
- [Redirect from root to WWW](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/index.md): Create a redirect rule to forward HTTPS requests from the root (also known as the âapexâ or ânakedâ domain) to the WWW subdomain.
- [Redirect from WWW to root](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/index.md): Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the âapexâ or ânakedâ domain).
- [Remove locale from URL path](https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/index.md): Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.
- [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/index.md)
- [Create a redirect rule via API](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-api/index.md)
- [Create a redirect rule in the dashboard](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-dashboard/index.md)
- [Single Redirects settings](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/index.md)
- [Create a redirect rule using Terraform](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/terraform-example/index.md)

## Origin Rules

- [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/index.md)
- [Create an origin rule via API](https://developers.cloudflare.com/rules/origin-rules/create-api/index.md)
- [Create an origin rule in the dashboard](https://developers.cloudflare.com/rules/origin-rules/create-dashboard/index.md)
- [Origin Rules examples](https://developers.cloudflare.com/rules/origin-rules/examples/index.md)
- [Change the HTTP Host header and DNS record](https://developers.cloudflare.com/rules/origin-rules/examples/change-http-host-header/index.md): Create an origin rule to change the HTTP `Host` header and the resolved DNS record.
- [Change the destination port](https://developers.cloudflare.com/rules/origin-rules/examples/change-port/index.md): Create an origin rule to change the destination port.
- [Define a single origin rule using Terraform](https://developers.cloudflare.com/rules/origin-rules/examples/define-single-origin-terraform/index.md): Create an origin rule using Terraform to override the `Host` header, the resolved hostname, and the destination port of API requests.
- [Origin Rules FAQ](https://developers.cloudflare.com/rules/origin-rules/faq/index.md)
- [Origin Rules settings](https://developers.cloudflare.com/rules/origin-rules/features/index.md)
- [Origin Rules API parameter reference](https://developers.cloudflare.com/rules/origin-rules/parameters/index.md)
- [Origin Rules tutorials](https://developers.cloudflare.com/rules/origin-rules/tutorials/index.md)
- [Change URI path and Host header](https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/index.md): This tutorial shows you how to modify both the URI path and the Host header of incoming requests using Transform Rules and Origin Rules.
- [Point to Pages with a custom domain](https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/index.md): This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain.
- [Point to R2 bucket with a custom domain](https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-r2-bucket-with-custom-domain/index.md): This tutorial will instruct you how to configure an origin rule and a DNS record to point to an R2 bucket configured with a custom domain.

## Cache Rules

- [Cache Rules](https://developers.cloudflare.com/rules/link-cache-rules/index.md)

## Cloud Connector

- [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/index.md)
- [Configure a Cloud Connector rule via API](https://developers.cloudflare.com/rules/cloud-connector/create-api/index.md)
- [Configure a Cloud Connector rule in the dashboard](https://developers.cloudflare.com/rules/cloud-connector/create-dashboard/index.md)
- [Configure Cloud Connector rules using Terraform](https://developers.cloudflare.com/rules/cloud-connector/create-terraform/index.md)
- [Cloud Connector examples](https://developers.cloudflare.com/rules/cloud-connector/examples/index.md)
- [Route /images to an S3 Bucket using Terraform](https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform/index.md): Route requests with a URI path starting with `/images` to a specific AWS S3 bucket with Cloud Connector using Terraform.
- [Route /images to an S3 Bucket](https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-s3/index.md): Route requests with a URI path starting with `/images` to a specific AWS S3 bucket using Cloud Connector.
- [Send EU visitors to a Google Cloud Storage bucket](https://developers.cloudflare.com/rules/cloud-connector/examples/send-eu-visitors-to-gcs/index.md): Route all traffic from EU visitors to a Google Cloud Storage bucket using Cloud Connector.
- [Serve /static-assets from Azure Blob Storage](https://developers.cloudflare.com/rules/cloud-connector/examples/serve-static-assets-from-azure/index.md): Route requests with a URI path starting with `/static-assets` to an Azure Blob Storage container using Cloud Connector.
- [Supported cloud providers in Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/providers/index.md)

## Custom Errors

- [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/index.md)
- [Common API calls for Custom Errors](https://developers.cloudflare.com/rules/custom-errors/api-calls/index.md)
- [Create custom error rules](https://developers.cloudflare.com/rules/custom-errors/create-rules/index.md)
- [Edit Error Pages](https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/index.md)
- [Example custom error rules](https://developers.cloudflare.com/rules/custom-errors/example-rules/index.md)
- [Error page types](https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/index.md)
- [Error tokens](https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/index.md)
- [Custom Errors parameters](https://developers.cloudflare.com/rules/custom-errors/reference/parameters/index.md)
- [Troubleshoot Error Pages issues](https://developers.cloudflare.com/rules/custom-errors/troubleshooting/index.md)

## Compression Rules

- [Compression Rules](https://developers.cloudflare.com/rules/compression-rules/index.md)
- [Create a compression rule via API](https://developers.cloudflare.com/rules/compression-rules/create-api/index.md)
- [Create a compression rule in the dashboard](https://developers.cloudflare.com/rules/compression-rules/create-dashboard/index.md)
- [Compression Rules examples](https://developers.cloudflare.com/rules/compression-rules/examples/index.md)
- [Disable Brotli compression](https://developers.cloudflare.com/rules/compression-rules/examples/disable-all-brotli/index.md): Create a compression rule to turn off Brotli compression for all incoming requests of a given zone.
- [Disable compression for AVIF images](https://developers.cloudflare.com/rules/compression-rules/examples/disable-compression-avif/index.md): Create a compression rule to turn off compression for AVIF images, based on either the content type or the file extension specified in the request.
- [Enable Zstandard compression for default content types](https://developers.cloudflare.com/rules/compression-rules/examples/enable-zstandard/index.md): Create a compression rule to turn on Zstandard compression for response content types where Cloudflare applies compression by default.
- [Use Gzip compression for CSV files](https://developers.cloudflare.com/rules/compression-rules/examples/gzip-for-csv/index.md): Create a compression rule to set Gzip compression as the preferred compression method for CSV files.
- [Use only Brotli compression for a specific path](https://developers.cloudflare.com/rules/compression-rules/examples/only-brotli-url-path/index.md): Create a compression rule to set Brotli as the only supported compression algorithm for a specific URI path.
- [Compression Rules settings](https://developers.cloudflare.com/rules/compression-rules/settings/index.md)

## Page Rules

- [Page Rules](https://developers.cloudflare.com/rules/page-rules/index.md)
- [URL forwarding with Page Rules](https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/index.md)
- [Manage Page Rules](https://developers.cloudflare.com/rules/page-rules/manage/index.md)
- [Additional reference for Page Rules](https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/index.md)
- [Recommended page rules](https://developers.cloudflare.com/rules/page-rules/reference/recommended-rules/index.md)
- [Page Rules settings](https://developers.cloudflare.com/rules/page-rules/reference/settings/index.md)
- [Wildcard matching in Page Rules](https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/index.md)
- [Troubleshoot Page Rules - Billing and subscription](https://developers.cloudflare.com/rules/page-rules/troubleshooting/billing-and-subscription/index.md)
- [Troubleshoot Page Rules - General](https://developers.cloudflare.com/rules/page-rules/troubleshooting/general/index.md)

## URL normalization

- [URL normalization](https://developers.cloudflare.com/rules/normalization/index.md)
- [URL normalization examples](https://developers.cloudflare.com/rules/normalization/examples/index.md): Examples of the impact of different URL normalization settings in the URLs of incoming requests.
- [How URL normalization works](https://developers.cloudflare.com/rules/normalization/how-it-works/index.md)
- [Configure URL normalization in the dashboard](https://developers.cloudflare.com/rules/normalization/manage/index.md): How to configure URL normalization in the Cloudflare dashboard.
- [URL normalization settings](https://developers.cloudflare.com/rules/normalization/settings/index.md)

## Trace a request

- [Trace a request](https://developers.cloudflare.com/rules/trace-request/index.md)
- [Cloudflare Trace changelog](https://developers.cloudflare.com/rules/trace-request/changelog/index.md)
- [Use Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/how-to/index.md): Learn how to use Cloudflare Trace in the dashboard and with the API.
- [Cloudflare Trace limitations](https://developers.cloudflare.com/rules/trace-request/limitations/index.md)

## Rules changelog

- [Rules changelog](https://developers.cloudflare.com/rules/changelog/index.md)

## reference

- [Rules language](https://developers.cloudflare.com/rules/reference/link-rule-language/index.md)
- [Page Rules migration guide](https://developers.cloudflare.com/rules/reference/page-rules-migration/index.md)
- [Troubleshoot Rules](https://developers.cloudflare.com/rules/reference/troubleshooting/index.md): Review common troubleshooting scenarios for Rules features.