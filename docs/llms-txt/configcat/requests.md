# Source: https://configcat.com/docs/requests.md

# What is a config JSON download?

Copy page

A config JSON download is counted every time your application downloads a configuration file from the ConfigCat CDN. The frequency of these downloads is totally under your control. Between downloads, you can evaluate your feature flags as many times as you like, it still counts as one config JSON download.

See an [overview of the ConfigCat architecture](https://configcat.com/architecture/).

Use the [Plan Calculator](https://configcat.com/calculator/) to calculate your estimated config JSON downloads.

Keep track of the number of config JSON downloads your apps are making on the [Usage & Quota page.](https://app.configcat.com/product/usage)

![ConfigCat Statistics](/docs/assets/stats.png)

## Current config JSON download limits[​](#current-config-json-download-limits "Direct link to Current config JSON download limits")

### Shared infrastructure[​](#shared-infrastructure "Direct link to Shared infrastructure")

The following plans run on shared infrastructure. So all customers use the same API nodes and Config Delivery Network (CDN).

| Plan           | total req/month | avg. req/sec | max. spike req/s |
| -------------- | --------------- | ------------ | ---------------- |
| **Free**       | 5,000,000       | \~2          | \~4              |
| **Pro**        | 25,000,000      | \~10         | \~20             |
| **Smart**      | 250,000,000     | \~100        | \~200            |
| **Enterprise** | 1,000,000,000   | \~400        | \~800            |

Use the [Plan Calculator](https://configcat.com/calculator/) to get your estimated config JSON downloads.

info

If you reach this limit, we will keep your application up and running. However, you can expect us to contact you on how we can meet your needs.

### Dedicated infrastructure[​](#dedicated-infrastructure "Direct link to Dedicated infrastructure")

The following plans include dedicated API and CDN nodes.

#### Hosted[​](#hosted "Direct link to Hosted")

Runs on dedicated infrastructure provided by ConfigCat. The basic package includes:

* 1x API node
* 6x CDN nodes

|                               | total req/month | avg. req/sec | max. spike req/s |
| ----------------------------- | --------------- | ------------ | ---------------- |
| **Basic package**             | 6,000,000,000   | \~2400       | \~4800           |
| **Every additional CDN node** | + 1,000,000,000 | \~400        | \~800            |

#### On-Premise (Self-hosted)[​](#on-premise-self-hosted "Direct link to On-Premise (Self-hosted)")

Runs on the customer's own infrastructure. We suggest [contacting ConfigCat's engineering](https://configcat.com/support/) team for exact requirements and performance characteristics.

## config JSON downloads[​](#config-json-downloads "Direct link to config JSON downloads")

The ConfigCat SDK, which you import into your applications, downloads your feature flags and settings in the form of a config JSON file from the ConfigCat CDN and caches it locally.

## `GetValue()` call is NOT a config JSON download[​](#getvalue-call-is-not-a-config-json-download "Direct link to getvalue-call-is-not-a-config-json-download")

Reading feature flag and setting values from cache with `GetValue()` is not considered as a config JSON download. If the cache is empty (e.g., upon application launch) or expired, a config JSON will be downloaded, and all subsequent `GetValue()` calls will then be served from the cache.

## Example use cases[​](#example-use-cases "Direct link to Example use cases")

### Frontend/mobile/desktop applications[​](#frontendmobiledesktop-applications "Direct link to Frontend/mobile/desktop applications")

Typically, you have a high number of frontend/mobile/desktop application instances. Your user count determines this number.

#### Example: A standard web application with 15k active users[​](#example-a-standard-web-application-with-15k-active-users "Direct link to Example: A standard web application with 15k active users")

Web apps run in the browser, so for each user, there will be a different ConfigCat SDK instance running. In this example, we have 15,000 active users who usually spend 5 hours on your web application per month. The ConfigCat SDK runs in Auto polling mode with the default 60 seconds polling interval.

> **18,000** *(5 hours in seconds)* / **60** *polling interval* = **300 config JSON downloads/user/month**<br />**15,000** *(users)* × **300** *(config JSON downloads/user/month)* = **4,500,000 config JSON downloads / month**

#### Example: A mobile application running on 5k devices 24/7[​](#example-a-mobile-application-running-on-5k-devices-247 "Direct link to Example: A mobile application running on 5k devices 24/7")

Having a mobile app that runs on the devices as a background process. The ConfigCat SDK runs in Auto polling mode with 1 hour polling interval. Your application runs on 5,000 devices.

> **5,000** *(devices)* × **730** *(hours in a month)* = **3,650,000 config JSON downloads / month**

### Backend applications[​](#backend-applications "Direct link to Backend applications")

Backend applications typically have fewer instances than frontend applications.

#### Example: Average frequency polling in 4 instances[​](#example-average-frequency-polling-in-4-instances "Direct link to Example: Average frequency polling in 4 instances")

Let's say you have an API for your frontend application, and you have 4 instances of it behind a load balancer. All these 4 instances use the ConfigCat SDK in Auto Polling mode with a 1-minute polling interval.

> **4** *(instances)* × **43,800** *(minutes in a month)* = **175,200 config JSON downloads / month**

#### Example: High frequency polling in 10 instances[​](#example-high-frequency-polling-in-10-instances "Direct link to Example: High frequency polling in 10 instances")

Suppose you want your system to react faster after changing a feature flag in ConfigCat. You can decrease the default polling interval all the way down to 1 second. In this case, we are calculating with 10 running instances.

> **10** *(instances)* × **2,592,000** *(seconds in a month)* = **25,920,000 config JSON downloads / month**

## How to lower the monthly config JSON download count?[​](#how-to-lower-the-monthly-config-json-download-count "Direct link to How to lower the monthly config JSON download count?")

### Use the ConfigCat Client as a Singleton[​](#use-the-configcat-client-as-a-singleton "Direct link to Use the ConfigCat Client as a Singleton")

Make sure that you use the *ConfigCat Client* as a Singleton object in your application code. If you want to use multiple SDK Keys in the same application, create only one *ConfigCat Client* per SDK Key.

### Increase the polling interval[​](#increase-the-polling-interval "Direct link to Increase the polling interval")

You can lower the frequency your application downloads the `config JSON` by setting larger polling intervals or using a different [polling mode](https://configcat.com/docs/advanced/caching.md) other than the default auto polling. See the [SDK References for more.](https://configcat.com/docs/sdk-reference/overview.md)

### Use webhooks[​](#use-webhooks "Direct link to Use webhooks")

In a backend application, you may want to consider using [Webhooks.](https://configcat.com/docs/advanced/notifications-webhooks.md) This way your application receives notifications about changes and downloads the `config JSON` only when needed.

### Call your backend instead of the ConfigCat CDN[​](#call-your-backend-instead-of-the-configcat-cdn "Direct link to Call your backend instead of the ConfigCat CDN")

In the case of a frontend application, you can reduce the number of calls made towards the ConfigCat CDN by moving the evaluation logic from the frontend application to your backend.

### Use the ConfigCat Proxy to cache/proxy config JSON downloads[​](#use-the-configcat-proxy-to-cacheproxy-config-json-downloads "Direct link to Use the ConfigCat Proxy to cache/proxy config JSON downloads")

The [ConfigCat Proxy](https://configcat.com/docs/advanced/proxy/proxy-overview.md) allows you to host a feature flag evaluation and config JSON proxy/cache service within your own infrastructure.<br /><!-- -->The [CDN proxy](https://configcat.com/docs/advanced/proxy/endpoints.md#cdn-proxy) feature allows you to proxy/cache config JSON downloads, and the ConfigCat SDKs can be routed to the ConfigCat Proxy running in your own infrastructure, greatly reducing the number of config JSON downloads.

### Purchase additional config JSON downloads[​](#purchase-additional-config-json-downloads "Direct link to Purchase additional config JSON downloads")

You can purchase an add-on for your subscription to increase your limits. [Contact us](https://configcat.com/support/) for more information.

| Plan           | Price             | Additional config JSON downloads | Additional network traffic |
| -------------- | ----------------- | -------------------------------- | -------------------------- |
| **Smart**      | $250 or €229 / mo | +250 million                     | +1TB                       |
| **Enterprise** | $700 or €649 / mo | +1 billion                       | +4TB                       |
