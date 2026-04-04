# Source: https://crawlee.dev/js/docs/deployment/apify-platform.md

# Apify Platform

Copy for LLM

Apify is a [platform](https://apify.com) built to serve large-scale and high-performance web scraping and automation needs. It provides easy access to [compute instances (Actors)](#what-is-an-actor), convenient [request](https://crawlee.dev/js/docs/guides/request-storage.md) and [result](https://crawlee.dev/js/docs/guides/result-storage.md) storages, [proxies](https://crawlee.dev/js/docs/guides/proxy-management.md), [scheduling](https://docs.apify.com/scheduler), [webhooks](https://docs.apify.com/webhooks) and [more](https://docs.apify.com/), accessible through a [web interface](https://console.apify.com) or an [API](https://docs.apify.com/api).

While we think that the Apify platform is super cool, and it's definitely worth signing up for a [free account](https://console.apify.com/sign-up), **Crawlee is and will always be open source**, runnable locally or on any cloud infrastructure.

note

We do not test Crawlee in other cloud environments such as Lambda or on specific architectures such as Raspberry PI. We strive to make it work, but there are no guarantees.

## Logging into Apify platform from Crawlee[​](#logging-into-apify-platform-from-crawlee "Direct link to Logging into Apify platform from Crawlee")

To access your [Apify account](https://console.apify.com/sign-up) from Crawlee, you must provide credentials - your [API token](https://console.apify.com/account?tab=integrations). You can do that either by utilizing [Apify CLI](https://github.com/apify/apify-cli) or with environment variables.

Once you provide credentials to your scraper, you will be able to use all the Apify platform features, such as calling actors, saving to cloud storages, using Apify proxies, setting up webhooks and so on.

### Log in with CLI[​](#log-in-with-cli "Direct link to Log in with CLI")

Apify CLI allows you to log in to your Apify account on your computer. If you then run your scraper using the CLI, your credentials will automatically be added.

```
npm install -g apify-cli
apify login -t YOUR_API_TOKEN
```

### Log in with environment variables[​](#log-in-with-environment-variables "Direct link to Log in with environment variables")

Alternatively, you can always provide credentials to your scraper by setting the [`APIFY_TOKEN`](#apify_token) environment variable to your API token.

> There's also the [`APIFY_PROXY_PASSWORD`](#apify_proxy_password) environment variable. Actor automatically infers that from your token, but it can be useful when you need to access proxies from a different account than your token represents.

### Log in with Configuration[​](#log-in-with-configuration "Direct link to Log in with Configuration")

Another option is to use the [`Configuration`](https://docs.apify.com/sdk/js/reference/class/Configuration) instance and set your api token there.

```
import { Actor } from 'apify';

const sdk = new Actor({ token: 'your_api_token' });
```

## What is an actor[​](#what-is-an-actor "Direct link to What is an actor")

When you deploy your script to the Apify platform, it becomes an [actor](https://apify.com/actors). An actor is a serverless microservice that accepts an input and produces an output. It can run for a few seconds, hours or even infinitely. An actor can perform anything from a simple action such as filling out a web form or sending an email, to complex operations such as crawling an entire website and removing duplicates from a large dataset.

Actors can be shared in the [Apify Store](https://apify.com/store) so that other people can use them. But don't worry, if you share your actor in the store and somebody uses it, it runs under their account, not yours.

**Related links**

* [Store of existing actors](https://apify.com/store)
* [Documentation](https://docs.apify.com/actors)
* [View actors in Apify Console](https://console.apify.com/actors)
* [API reference](https://apify.com/docs/api/v2#/reference/actors)

## Running an actor locally[​](#running-an-actor-locally "Direct link to Running an actor locally")

First let's create a boilerplate of the new actor. You could use Apify CLI and just run:

```
apify create my-hello-world
```

The CLI will prompt you to select a project boilerplate template - let's pick "Hello world". The tool will create a directory called `my-hello-world` with a Node.js project files. You can run the actor as follows:

```
cd my-hello-world
apify run
```

## Running Crawlee code as an actor[​](#running-crawlee-code-as-an-actor "Direct link to Running Crawlee code as an actor")

For running Crawlee code as an actor on [Apify platform](https://apify.com/actors) you should either:

* use a combination of [`Actor.init()`](https://docs.apify.com/sdk/js/reference/class/Actor#init) and [`Actor.exit()`](https://docs.apify.com/sdk/js/reference/class/Actor#exit) functions;
* or wrap it into [`Actor.main()`](https://docs.apify.com/sdk/js/reference/class/Actor#main) function.

NOTE

* Adding [`Actor.init()`](https://docs.apify.com/sdk/js/reference/class/Actor#init) and [`Actor.exit()`](https://docs.apify.com/sdk/js/reference/class/Actor#exit) to your code are the only two important things needed to run it on Apify platform as an actor. `Actor.init()` is needed to initialize your actor (e.g. to set the correct storage implementation), while without `Actor.exit()` the process will simply never stop.
* [`Actor.main()`](https://docs.apify.com/sdk/js/reference/class/Actor#main) is an alternative to `Actor.init()` and `Actor.exit()` as it calls both behind the scenes.

Let's look at the `CheerioCrawler` example from the [Quick Start](https://crawlee.dev/js/docs/quick-start.md) guide:

* Using Actor.main()
* Using Actor.init() and Actor.exit()

```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.main(async () => {
    const crawler = new CheerioCrawler({
        async requestHandler({ request, $, enqueueLinks }) {
            const { url } = request;

            // Extract HTML title of the page.
            const title = $('title').text();
            console.log(`Title of ${url}: ${title}`);

            // Add URLs that match the provided pattern.
            await enqueueLinks({
                globs: ['https://www.iana.org/*'],
            });

            // Save extracted data to dataset.
            await Actor.pushData({ url, title });
        },
    });

    // Enqueue the initial request and run the crawler
    await crawler.run(['https://www.iana.org/']);
});
```

```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.init();

const crawler = new CheerioCrawler({
    async requestHandler({ request, $, enqueueLinks }) {
        const { url } = request;

        // Extract HTML title of the page.
        const title = $('title').text();
        console.log(`Title of ${url}: ${title}`);

        // Add URLs that match the provided pattern.
        await enqueueLinks({
            globs: ['https://www.iana.org/*'],
        });

        // Save extracted data to dataset.
        await Actor.pushData({ url, title });
    },
});

// Enqueue the initial request and run the crawler
await crawler.run(['https://www.iana.org/']);

await Actor.exit();
```

Note that you could also run your actor (that is using Crawlee) locally with Apify CLI. You could start it via the following command in your project folder:

```
apify run
```

## Deploying an actor to Apify platform[​](#deploying-an-actor-to-apify-platform "Direct link to Deploying an actor to Apify platform")

Now (assuming you are already logged in to your Apify account) you can easily deploy your code to the Apify platform by running:

```
apify push
```

Your script will be uploaded to and built on the Apify platform so that it can be run there. For more information, view the [Apify Actor](https://docs.apify.com/cli) documentation.

## Usage on Apify platform[​](#usage-on-apify-platform "Direct link to Usage on Apify platform")

You can also develop your actor in an online code editor directly on the platform (you'll need an Apify Account). Let's go to the [Actors](https://console.apify.com/actors) page in the app, click *Create new* and then go to the *Source* tab and start writing the code or paste one of the examples from the [Examples](https://crawlee.dev/js/docs/examples.md) section.

## Storages[​](#storages "Direct link to Storages")

There are several things worth mentioning here.

### Helper functions for default Key-Value Store and Dataset[​](#helper-functions-for-default-key-value-store-and-dataset "Direct link to Helper functions for default Key-Value Store and Dataset")

To simplify access to the *default* storages, instead of using the helper functions of respective storage classes, you could use:

* [`Actor.setValue()`](https://docs.apify.com/sdk/js/reference/class/Actor#setValue), [`Actor.getValue()`](https://docs.apify.com/sdk/js/reference/class/Actor#getValue), [`Actor.getInput()`](https://docs.apify.com/sdk/js/reference/class/Actor#getInput) for `Key-Value Store`
* [`Actor.pushData()`](https://docs.apify.com/sdk/js/reference/class/Actor#pushData) for `Dataset`

### Using platform storage in a local actor[​](#using-platform-storage-in-a-local-actor "Direct link to Using platform storage in a local actor")

When you plan to use the platform storage while developing and running your actor locally, you should use [`Actor.openKeyValueStore()`](https://docs.apify.com/sdk/js/reference/class/Actor#openKeyValueStore), [`Actor.openDataset()`](https://docs.apify.com/sdk/js/reference/class/Actor#openDataset) and [`Actor.openRequestQueue()`](https://docs.apify.com/sdk/js/reference/class/Actor#openRequestQueue) to open the respective storage.

Using each of these methods allows to pass the [`OpenStorageOptions`](https://docs.apify.com/sdk/js/reference/interface/OpenStorageOptions) as a second argument, which has only one optional property: [`forceCloud`](https://docs.apify.com/sdk/js/reference/interface/OpenStorageOptions#forceCloud). If set to `true` - cloud storage will be used instead of the folder on the local disk.

note

If you don't plan to force usage of the platform storages when running the actor locally, there is no need to use the [`Actor`](https://docs.apify.com/sdk/js/reference/class/Actor) class for it. The Crawlee variants [`KeyValueStore.open()`](https://crawlee.dev/js/api/core/class/KeyValueStore.md#open), [`Dataset.open()`](https://crawlee.dev/js/api/core/class/Dataset.md#open) and [`RequestQueue.open()`](https://crawlee.dev/js/api/core/class/RequestQueue.md#open) will work the same.

### Getting public url of an item in the platform storage[​](#getting-public-url-of-an-item-in-the-platform-storage "Direct link to Getting public url of an item in the platform storage")

If you need to share a link to some file stored in a Key-Value Store on Apify Platform, you can use [`getPublicUrl()`](https://docs.apify.com/sdk/js/reference/class/KeyValueStore#getPublicUrl) method. It accepts only one parameter: `key` - the key of the item you want to share.

```
import { KeyValueStore } from 'apify';

const store = await KeyValueStore.open();
await store.setValue('your-file', { foo: 'bar' });
const url = store.getPublicUrl('your-file');
// https://api.apify.com/v2/key-value-stores/<your-store-id>/records/your-file
```

### Exporting dataset data[​](#exporting-dataset-data "Direct link to Exporting dataset data")

When the [`Dataset`](https://crawlee.dev/js/api/core/class/Dataset.md) is stored on the [Apify platform](https://apify.com/actors), you can export its data to the following formats: HTML, JSON, CSV, Excel, XML and RSS. The datasets are displayed on the actor run details page and in the [Storage](https://console.apify.com/storage) section in the Apify Console. The actual data is exported using the [Get dataset items](https://apify.com/docs/api/v2#/reference/datasets/item-collection/get-items) Apify API endpoint. This way you can easily share the crawling results.

**Related links**

* [Apify platform storage documentation](https://docs.apify.com/storage)
* [View storage in Apify Console](https://console.apify.com/storage)
* [Key-value stores API reference](https://apify.com/docs/api/v2#/reference/key-value-stores)
* [Datasets API reference](https://docs.apify.com/api/v2#/reference/datasets)
* [Request queues API reference](https://docs.apify.com/api/v2#/reference/request-queues)

## Environment variables[​](#environment-variables "Direct link to Environment variables")

The following are some additional environment variables specific to Apify platform. More Crawlee specific environment variables could be found in the [Environment Variables](https://crawlee.dev/js/docs/guides/configuration.md#environment-variables) guide.

note

It's important to notice that `CRAWLEE_` environment variables don't need to be replaced with equivalent `APIFY_` ones. Likewise, Crawlee understands `APIFY_` environment variables after calling `Actor.init()` or when using `Actor.main()`.

### `APIFY_TOKEN`[​](#apify_token "Direct link to apify_token")

The API token for your Apify account. It is used to access the Apify API, e.g. to access cloud storage or to run an actor on the Apify platform. You can find your API token on the [Account Settings / Integrations](https://console.apify.com/account?tab=integrations) page.

### Combinations of `APIFY_TOKEN` and `CRAWLEE_STORAGE_DIR`[​](#combinations-of-apify_token-and-crawlee_storage_dir "Direct link to combinations-of-apify_token-and-crawlee_storage_dir")

> `CRAWLEE_STORAGE_DIR` env variable description could be found in [Environment Variables](https://crawlee.dev/js/docs/guides/configuration.md#crawlee_storage_dir) guide.

By combining the env vars in various ways, you can greatly influence the actor's behavior.

| Env Vars                                | API | Storages         |
| --------------------------------------- | --- | ---------------- |
| none OR `CRAWLEE_STORAGE_DIR`           | no  | local            |
| `APIFY_TOKEN`                           | yes | Apify platform   |
| `APIFY_TOKEN` AND `CRAWLEE_STORAGE_DIR` | yes | local + platform |

When using both `APIFY_TOKEN` and `CRAWLEE_STORAGE_DIR`, you can use all the Apify platform features and your data will be stored locally by default. If you want to access platform storages, you can use the `{ forceCloud: true }` option in their respective functions.

```
import { Actor } from 'apify';
import { Dataset } from 'crawlee';

// or Dataset.open('my-local-data')
const localDataset = await Actor.openDataset('my-local-data');
// but here we need the `Actor` class
const remoteDataset = await Actor.openDataset('my-dataset', { forceCloud: true });
```

### `APIFY_PROXY_PASSWORD`[​](#apify_proxy_password "Direct link to apify_proxy_password")

Optional password to [Apify Proxy](https://docs.apify.com/proxy) for IP address rotation. Assuming Apify Account was already created, you can find the password on the [Proxy page](https://console.apify.com/proxy) in the Apify Console. The password is automatically inferred using the `APIFY_TOKEN` env var, so in most cases, you don't need to touch it. You should use it when, for some reason, you need access to Apify Proxy, but not access to Apify API, or when you need access to proxy from a different account than your token represents.

## Proxy management[​](#proxy-management "Direct link to Proxy management")

In addition to your own proxy servers and proxy servers acquired from third-party providers used together with Crawlee, you can also rely on [Apify Proxy](https://apify.com/proxy) for your scraping needs.

### Apify Proxy[​](#apify-proxy "Direct link to Apify Proxy")

If you are already subscribed to Apify Proxy, you can start using them immediately in only a few lines of code (for local usage you first should be [logged in](#logging-into-apify-platform-from-crawlee) to your Apify account.

```
import { Actor } from 'apify';

const proxyConfiguration = await Actor.createProxyConfiguration();
const proxyUrl = await proxyConfiguration.newUrl();
```

Note that unlike using your own proxies in Crawlee, you shouldn't use the constructor to create [`ProxyConfiguration`](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) instance. For using Apify Proxy you should create an instance using the [`Actor.createProxyConfiguration()`](https://docs.apify.com/sdk/js/reference/class/Actor#createProxyConfiguration) function instead.

### Apify Proxy Configuration[​](#apify-proxy-configuration "Direct link to Apify Proxy Configuration")

With Apify Proxy, you can select specific proxy groups to use, or countries to connect from. This allows you to get better proxy performance after some initial research.

```
import { Actor } from 'apify';

const proxyConfiguration = await Actor.createProxyConfiguration({
    groups: ['RESIDENTIAL'],
    countryCode: 'US',
});
const proxyUrl = await proxyConfiguration.newUrl();
```

Now your crawlers will use only Residential proxies from the US. Note that you must first get access to a proxy group before you are able to use it. You can check proxy groups available to you in the [proxy dashboard](https://console.apify.com/proxy).

### Apify Proxy vs. Own proxies[​](#apify-proxy-vs-own-proxies "Direct link to Apify Proxy vs. Own proxies")

The `ProxyConfiguration` class covers both Apify Proxy and custom proxy URLs so that you can easily switch between proxy providers. However, some features of the class are available only to Apify Proxy users, mainly because Apify Proxy is what one would call a super-proxy. It's not a single proxy server, but an API endpoint that allows connection through millions of different IP addresses. So the class essentially has two modes: Apify Proxy or Own (third party) proxy.

The difference is easy to remember.

* If you're using your own proxies - you should create an instance with the ProxyConfiguration [`constructor`](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md#constructor) function based on the provided [`ProxyConfigurationOptions`](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md).
* If you are planning to use Apify Proxy - you should create an instance using the [`Actor.createProxyConfiguration()`](https://docs.apify.com/sdk/js/reference/class/Actor#createProxyConfiguration) function. [`ProxyConfigurationOptions.proxyUrls`](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md#proxyUrls) and [`ProxyConfigurationOptions.newUrlFunction`](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md#newUrlFunction) enable use of your custom proxy URLs, whereas all the other options are there to configure Apify Proxy.

**Related links**

* [Apify Proxy docs](https://docs.apify.com/proxy)
