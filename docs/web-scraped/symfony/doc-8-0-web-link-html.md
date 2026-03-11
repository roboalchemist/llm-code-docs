# Source: https://symfony.com/doc/8.0/web_link.html

Title: Asset Preloading and Resource Hints with WebLink (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/web_link.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/web_link.rst)

Symfony provides native support (via the [WebLink](https://github.com/symfony/web-link) component) for managing `Link` HTTP headers, which are the key to improve the application performance when using preloading capabilities of modern web browsers.

`Link` headers are used to hint resources (e.g. CSS and JavaScript files) to clients before they even know that they need them. WebLink enables several optimizations:

* Telling the browser to preload resources that will be needed for the current page;
* Sending [103 Early Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/103) responses so the browser starts downloading assets before the full response is ready (see [Asset Preloading and Resource Hints with WebLink](https://symfony.com/doc/current/web_link.html#early-hints));
* Making early DNS lookups, TCP handshakes or TLS negotiations.

Note

Some of these features (like Early Hints or resource hints) work best over a secure HTTPS connection. The main web servers (Apache, nginx, Caddy, etc.) support this, and you can also use the [Docker installer and runtime for Symfony](https://github.com/dunglas/symfony-docker) created by Kévin Dunglas, from the Symfony community.

[Installation](https://symfony.com/doc/8.0/web_link.html#installation "Permalink to this headline")
---------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex), run the following command to install the WebLink feature before using it:

[Preloading Assets](https://symfony.com/doc/8.0/web_link.html#preloading-assets "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------

Imagine that your application includes a web page like this:

In a traditional HTTP workflow, when this page is loaded, browsers make one request for the HTML document and another for the linked CSS file. With the `Link` HTTP header, your application can hint the browser to preload the CSS file while processing the HTML.

This is useful for resources that are not directly linked in the HTML but are needed early (e.g. a font file referenced inside a CSS stylesheet).

To preload a resource, use the `preload()` Twig function provided by WebLink. The ["as" attribute](https://w3c.github.io/preload/#as-attribute) is required, as browsers use it to prioritize resources correctly and comply with the content security policy:

The `preload()` function adds a `Link` HTTP header to the response (e.g. `Link: </fonts/myfont.woff2>; rel="preload"; as="font"`). This tells the browser (or an HTTP/2 compatible server or CDN) to start fetching the resource as early as possible. You can also combine it with the `asset()` function:

If you reload the page, the perceived performance will improve because the browser starts downloading the CSS file as soon as it receives the `Link` header, without waiting for the full HTML to be parsed.

Tip

When using the [AssetMapper component](https://symfony.com/doc/current/frontend/asset_mapper.html) (e.g. `importmap('app')`), there's no need to add the `<link rel="preload">` tag. The `importmap()` Twig function automatically adds the `Link` HTTP header for you when the WebLink component is available.

Additionally, according to [the Priority Hints specification](https://wicg.github.io/priority-hints/), you can signal the priority of the resource to download using the `importance` attribute:

### [How does it work?](https://symfony.com/doc/8.0/web_link.html#how-does-it-work "Permalink to this headline")

The WebLink component manages the `Link` HTTP headers added to the response. When using the `preload()` function, a header like this is added to the response: `Link </fonts/myfont.woff2>; rel="preload"; as="font"`

When the browser receives this header, it starts downloading the resource right away, before it encounters the corresponding tag in the HTML.

Popular proxy services and CDNs including [Cloudflare](https://blog.cloudflare.com/announcing-support-for-http-2-server-push-2/), [Fastly](https://docs.fastly.com/en/guides/http2-server-push) and [Akamai](https://http2.akamai.com/) also leverage `Link` headers to optimize resource delivery and improve performance of your applications in production.

[Sending Early Hints](https://symfony.com/doc/8.0/web_link.html#sending-early-hints "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

By default, `Link` headers are sent along with the final response. However, you can further improve performance by sending these headers _before_ the full response is ready, using [103 Early Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/103) responses. This tells the browser to start downloading assets while the server is still preparing the page.

Note

In order to work, the [SAPI](https://www.php.net/manual/en/function.header.php) you're using must support this feature, like [FrankenPHP](https://frankenphp.dev/).

The simplest way to send early hints is by using the `preload()` Twig function. When early hints are supported by your web server, the `Link` headers added via `preload()` are automatically sent as `103` responses:

For more control, you can send early hints explicitly from your controller action thanks to the [sendEarlyHints()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20sendEarlyHints "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::sendEarlyHints()") method:

Technically, Early Hints are an informational HTTP response with the status code `103`. The `sendEarlyHints()` method creates a `Response` object with that status code and sends its headers immediately.

This way, browsers can start downloading the assets immediately; like the `style.css` and `script.js` files in the above example. The `sendEarlyHints()` method also returns the `Response` object, which you must use to create the full response sent from the controller action.

Tip

When using the [AssetMapper component](https://symfony.com/doc/current/frontend/asset_mapper.html), asset file names contain a version hash (e.g. `styles-3c16d9220694c0e56d8648f25e6035e9.css`). To reference the correct versioned URL in early hints, use the [AssetMapperInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/AssetMapper/AssetMapperInterface.php "Symfony\Component\AssetMapper\AssetMapperInterface") service:

[Resource Hints](https://symfony.com/doc/8.0/web_link.html#resource-hints "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

[Resource Hints](https://www.w3.org/TR/resource-hints/) are used by applications to help browsers when deciding which resources should be downloaded, preprocessed or connected to first.

The WebLink component provides the following Twig functions to send those hints:

* `dns_prefetch()`: "indicates an origin (e.g. `https://foo.cloudfront.net`) that will be used to fetch required resources, and that the user agent should resolve as early as possible".
* `preconnect()`: "indicates an origin (e.g. `https://www.google-analytics.com`) that will be used to fetch required resources. Initiating an early connection, which includes the DNS lookup, TCP handshake, and optional TLS negotiation, allows the user agent to mask the high latency costs of establishing a connection".
* `prefetch()`: "identifies a resource that might be required by the next navigation, and that the user agent _should_ fetch, such that the user agent can deliver a faster response once the resource is requested in the future".
* `prerender()`: " **deprecated** and superseded by the [Speculation Rules API](https://developer.mozilla.org/docs/Web/API/Speculation_Rules_API), identifies a resource that might be required by the next navigation, and that the user agent _should_ fetch and execute, such that the user agent can deliver a faster response once the resource is requested later".

The component also supports sending HTTP links not related to performance and any link implementing the [PSR-13](https://www.php-fig.org/psr/psr-13/) standard. For instance, any [link defined in the HTML specification](https://html.spec.whatwg.org/dev/links.html#linkTypes):

The previous snippet will result in this HTTP header being sent to the client: `Link: </index.jsonld>; rel="alternate",</app.css>; rel="preload"; nopush`

You can also add links to the HTTP response directly from controllers and services:

Tip

The possible values of link relations (`'preload'`, `'preconnect'`, etc.) are also defined as constants in the [Link](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/WebLink/Link.php "Symfony\Component\WebLink\Link") class (e.g. `Link::REL_PRELOAD`, `Link::REL_PRECONNECT`, etc.).

Some third-party APIs provide resources such as pagination URLs using the `Link` HTTP header. The WebLink component provides the [HttpHeaderParser](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/WebLink/HttpHeaderParser.php "Symfony\Component\WebLink\HttpHeaderParser") utility class to parse those headers and transform them into [Link](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/WebLink/Link.php "Symfony\Component\WebLink\Link") instances:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
