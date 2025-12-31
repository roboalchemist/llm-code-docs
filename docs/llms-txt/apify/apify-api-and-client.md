# Source: https://docs.apify.com/academy/expert-scraping-with-apify/apify-api-and-client.md

# IV - Apify API & client

**Gain an in-depth understanding of the two main ways of programmatically interacting with the Apify platform - through the API, and through a client.**

***

You can use one of the two main ways to programmatically interact with the Apify platform: by directly using https://docs.apify.com/api/v2.md, or by using the https://docs.apify.com/api/client/js and https://docs.apify.com/api/client/python API clients. In the next two lessons, we'll be focusing on the first two.

> Apify's API and JavaScript API client allow us to do anything a regular user can do when interacting with the platform's web interface, only programmatically.

## Learning 🧠

* Scroll through the https://docs.apify.com/api/v2.md (there's a whole lot there, so you're not expected to memorize everything).
* Read about the Apify client in https://docs.apify.com/api/client/js. It can also be seen on https://github.com/apify/apify-client-js and https://www.npmjs.com/package/apify-client.
* Learn about the https://docs.apify.com/sdk/js/reference/class/Actor#newClient function in the Apify SDK.
* Skim through https://help.apify.com/en/articles/2868670-how-to-pass-data-from-web-scraper-to-another-actor about API integration (this article is old; however, still relevant).

## Knowledge check 📝

1. What is the relationship between the Apify API and the Apify client? Are there any significant differences?
2. How do you pass input when running an Actor or task via API?
3. Do you need to install the `apify-client` npm package when already using the `apify` package?

## Our task

We'll be creating another new Actor, which will have two jobs:

1. Programmatically call the task for the Amazon Actor.
2. Export its results into CSV format under a new key called **OUTPUT.csv** in the default key-value store.

Though it's a bit unintuitive, this is a perfect activity for learning how to use both the Apify API and the Apify JavaScript client.

The new Actor should take the following input values, which be mapped to parameters in the API calls:


```
{
    // How much memory to allocate to the Amazon Actor
    // Must be a power of 2
    "memory": 4096,

    // Whether to use the JavaScript client to make the
    // call, or to use the API
    "useClient": false,

    // The fields in each item to return back. All other
    // fields should be ommitted
    "fields": ["title", "itemUrl", "offer"],

    // The maximum number of items to return back
    "maxItems": 10
}
```


https://docs.apify.com/academy/expert-scraping-with-apify/solutions/using-api-and-client.md

## Next up

https://docs.apify.com/academy/expert-scraping-with-apify/migrations-maintaining-state.md will teach us everything we need to know about migrations and how to handle them properly to avoid losing any state; therefore, increasing the reliability of our `demo-actor` Amazon scraper.
