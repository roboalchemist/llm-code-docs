# Source: https://crawlee.dev/js/api/playwright-crawler/function/launchPlaywright.md

# launchPlaywright<!-- -->

### Callable

* ****launchPlaywright**(launchContext, config): Promise\<Browser>

***

* Launches headless browsers using Playwright pre-configured to work within the Apify platform. The function has the same return value as `browserType.launch()`. See [Playwright documentation](https://playwright.dev/docs/api/class-browsertype) for more details.

  The `launchPlaywright()` function alters the following Playwright options:

  * Passes the setting from the `CRAWLEE_HEADLESS` environment variable to the `headless` option, unless it was already defined by the caller or `CRAWLEE_XVFB` environment variable is set to `1`. Note that Apify Actor cloud platform automatically sets `CRAWLEE_HEADLESS=1` to all running actors.
  * Takes the `proxyUrl` option, validates it and adds it to `launchOptions` in a proper format. The proxy URL must define a port number and have one of the following schemes: `http://`, `https://`, `socks4://` or `socks5://`. If the proxy is HTTP (i.e. has the `http://` scheme) and contains username or password, the `launchPlaywright` functions sets up an anonymous proxy HTTP to make the proxy work with headless Chrome. For more information, read the [blog post about proxy-chain library](https://blog.apify.com/how-to-make-headless-chrome-and-puppeteer-use-a-proxy-server-with-authentication-249a21a79212).

  To use this function, you need to have the [Playwright](https://www.npmjs.com/package/playwright) NPM package installed in your project. When running on the Apify Platform, you can achieve that simply by using the `apify/actor-node-playwright-*` base Docker image for your actor - see [Apify Actor documentation](https://docs.apify.com/actor/build#base-images) for details.

  ***

  #### Parameters

  * ##### optionallaunchContext: [PlaywrightLaunchContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightLaunchContext.md)

    Optional settings passed to `browserType.launch()`. In addition to [Playwright's options](https://playwright.dev/docs/api/class-browsertype?_highlight=launch#browsertypelaunchoptions) the object may contain our own [PlaywrightLaunchContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightLaunchContext.md) that enable additional features.

  * ##### optionalconfig: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns Promise\<Browser>

  Promise that resolves to Playwright's `Browser` instance.
