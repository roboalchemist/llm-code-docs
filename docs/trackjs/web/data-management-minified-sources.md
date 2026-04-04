# Source: https://docs.trackjs.com/data-management/minified-sources/

Title: Dealing with Minified Sources

URL Source: https://docs.trackjs.com/data-management/minified-sources/

Markdown Content:
Debugging production problems will often involve understanding minified JavaScript. TrackJS helps you see through minification with full support for Source Maps as well as beautifying your other source code.

[Source Maps](https://docs.trackjs.com/data-management/minified-sources/#source-maps "Permalink Here")
------------------------------------------------------------------------------------------------------

Source maps enable TrackJS to show you the original function names and source code associated with an error’s stack trace. It’s amazingly helpful in understanding the running code at the time of an error.

Source maps are intermediary files that connect your final minified source code with the original source files that produced it, even if the original files are in a different language such as TypeScript or JSX. Source maps can be produced automatically from many build tools such as WebPack and Rollup.

**TIP** Unsure how to enable source maps for your toolchain? [Check out this article](https://github.com/ryanseddon/source-map/wiki/Source-maps%3A-languages,-tools-and-other-info).

Once you’ve configured source maps for your build, you’ll see `.map` files being generated alongside your minified scripts. Your minified files should also have the an annotation on the last line similar to `//# sourceMappingUrl=scripts.js.map`.

When you view an error where the stack trace has this annotation, TrackJS will attempt to retrieve the `map` file and apply it. For this to succeed:

*   The error must have a stack trace.
*   The JavaScript file(s) in the stack frames must be accessible.
*   There must be a single source map directive in the file.
*   The source map file itself must be accessible.

Assuming these criteria are met, you’ll see a little green toggle in the stack trace pane, and you’ll now have real file, lines and columns to look at. If you’ve optionally included the original source in your map, we will include that and beautify it as well.

[Securing Source Maps](https://docs.trackjs.com/data-management/minified-sources/#securing-source-maps "Permalink Here")
------------------------------------------------------------------------------------------------------------------------

If you do not want to expose your source maps publicly, you can secure access to them by validating that the request came from TrackJS. We will make the request from known IP Addresses and include an authentication header that you can use to validate.

### [Securing by IP Address](https://docs.trackjs.com/data-management/minified-sources/#securing-by-ip-address "Permalink Here")

Alternatively, you can validate the request by checking the requesting IP Addresses are from TrackJS. We will make the request from these static IP Addresses:

*   `142.4.218.95`
*   `167.114.172.73`

You can secure access to the `map` files with some configuration to your webservers to only allow access from these addresses. Here are examples on how to make this configuration for **Apache**:

<Files ~ "\.map$"> Require all denied Require ip 142.4.218.95 Require ip 167.114.172.73 </Files>

[Secure source maps by IP on Apache](https://docs.trackjs.com/data-management/minified-sources/#code-secure-source-maps-by-ip-on-apache)

And for **Nginx**:

server { location ~ \.map$ { allow 142.4.218.95; allow 167.114.172.73; deny all; }}

[Secure source maps by IP on Nginx](https://docs.trackjs.com/data-management/minified-sources/#code-secure-source-maps-by-ip-on-nginx)

We will include a custom `X-TrackJS-Sourcemap-Key` header with every source map request our servers make.

**TIP** You can find your secret source map key in the [**Account**](https://my.trackjs.com/account/organization) section of the TrackJS UI.

You can secure access to the `map` files with some configuration to your webservers to only allow access with this header. Here are examples on how to make this configuration for **Apache**:

And for **Nginx**:

### [Securing with Cloudfront](https://docs.trackjs.com/data-management/minified-sources/#securing-with-cloudfront "Permalink Here")

Many users choose to host their scripts and sourcemaps on Cloudfront. The following function can be used as a template to secure these sourcemaps so that only TrackJS can access them.

/** * !!! IMPORTANT !!!: Keep EMPTY until copied into cloudfront functions and replace with secret value * * @type {string} * @see https://my.trackjs.com/account/organization * @see https://docs.trackjs.com/data-management/minified-sources/#securing-by-header */var TRACKJS_SOURCEMAP_KEY = '';var unauthorizedResponse = { statusCode: 401, statusDescription: 'Unauthorized'};/** * Only allow TrackJS to access sourcemap files * * @param event * @returns {boolean} Whether the request can continue */function sourceMapGuard(event) { var isSourceMapRegex = /.+\.map$/; if (!isSourceMapRegex.test(event.request.uri)) { // not a sourcemap return true; } if (event.request.headers && event.request.headers['x-trackjs-sourcemap-key'] && event.request.headers['x-trackjs-sourcemap-key'].value && event.request.headers['x-trackjs-sourcemap-key'].value === TRACKJS_SOURCEMAP_KEY) { console.log(`Allowed TrackJS access to sourcemap (${event.request.uri}) from: ${event.viewer.ip}`); return true; } console.log(`Denied access to sourcemap (${event.request.uri}) from: ${event.viewer.ip}`); return false;}/** * Function Cloudfront calls to handle the 'Viewer Request' */function handler(event) { var hasAccess = sourceMapGuard(event); if (!hasAccess) { return unauthorizedResponse; } // Add more request guards here as needed. // Allow access by returning the original request. return event.request;}

[Secure source maps Cloudfront function](https://docs.trackjs.com/data-management/minified-sources/#code-secure-source-maps-cloudfront-function)

We will include a custom `X-Requested-By` header with every source map request our servers make.

**NOTE** We continue to support this method but recommend using the source map key option above for new installations, as it is more secure.

You can secure access to the `map` files with some configuration to your webservers to only allow access with this header.

### [Manual Source Maps](https://docs.trackjs.com/data-management/minified-sources/#manual-source-maps "Permalink Here")

If you’re developing an internal application, or on a development environment, your source maps may not be exposed. We also support the option of drag-and-dropping a source map right on the stack trace in the UI. This works exactly like the automatic retrieval, except you’re in full control. Your source map file is _never_ sent to our servers, and is processed on the client.

[Beautify Sources](https://docs.trackjs.com/data-management/minified-sources/#beautify-sources "Permalink Here")
----------------------------------------------------------------------------------------------------------------

TrackJS automatically beautifies minified files, even without producing source maps. Expanding any stack trace frame will attempt to retrieve the file referenced, and beautify the sources.
