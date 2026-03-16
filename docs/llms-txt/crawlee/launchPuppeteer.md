# Source: https://crawlee.dev/js/api/puppeteer-crawler/function/launchPuppeteer.md

# launchPuppeteer<!-- -->

### Callable

* ****launchPuppeteer**(launchContext, config): Promise\<Browser>

***

* Launches headless Chrome using Puppeteer pre-configured to work within the Apify platform. The function has the same argument and the return value as `puppeteer.launch()`. See [Puppeteer documentation](https://pptr.dev/api/puppeteer.launchoptions) for more details.

  The `launchPuppeteer()` function alters the following Puppeteer options:

  * Passes the setting from the `CRAWLEE_HEADLESS` environment variable to the `headless` option, unless it was already defined by the caller or `CRAWLEE_XVFB` environment variable is set to `1`. Note that Apify Actor cloud platform automatically sets `CRAWLEE_HEADLESS=1` to all running actors.
  * Takes the `proxyUrl` option, validates it and adds it to `args` as `--proxy-server=XXX`. The proxy URL must define a port number and have one of the following schemes: `http://`, `https://`, `socks4://` or `socks5://`. If the proxy is HTTP (i.e. has the `http://` scheme) and contains username or password, the `launchPuppeteer` functions sets up an anonymous proxy HTTP to make the proxy work with headless Chrome. For more information, read the [blog post about proxy-chain library](https://blog.apify.com/how-to-make-headless-chrome-and-puppeteer-use-a-proxy-server-with-authentication-249a21a79212).

  To use this function, you need to have the [puppeteer](https://www.npmjs.com/package/puppeteer) NPM package installed in your project. When running on the Apify cloud, you can achieve that simply by using the `apify/actor-node-chrome` base Docker image for your actor - see [Apify Actor documentation](https://docs.apify.com/actor/build#base-images) for details.

  ***

  #### Parameters

  * ##### optionallaunchContext: [PuppeteerLaunchContext](https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerLaunchContext.md)

    All `PuppeteerLauncher` parameters are passed via an launchContext object. If you want to pass custom `puppeteer.launch(options)` options you can use the `PuppeteerLaunchContext.launchOptions` property.

  * ##### optionalconfig: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns Promise\<Browser>

  Promise that resolves to Puppeteer's `Browser` instance.
