# Source: https://configcat.com/docs/network-traffic.md

# Network Traffic

Copy page

Network Traffic refers to the data transmitted between your applications and ConfigCat CDN. It includes the requests made to fetch feature flags and settings.

Generally speaking, the Network Traffic is proportional to:

* the size of the `config JSON`,
* the number of clients connecting to ConfigCat,
* and the frequency of changes in the `config JSON`.

Here are a few examples of config JSON file sizes:

| Config JSON complexity |                 | Network Traffic     |                                     |
| ---------------------- | --------------- | ------------------- | ----------------------------------- |
| # of feature flags     | Targeting Rules | first download size | no change<br />`304 - Not Modified` |
| 11                     | none            | 0.5 kB              | 65 B                                |
| 17                     | few             | 1.6 kB              | 65 B                                |
| 370                    | many            | 159 kB              | 65 B                                |

#### Size of the `config JSON`[​](#size-of-the-config-json "Direct link to size-of-the-config-json")

It is affected by the number of feature flags, settings, targeting rules, segments, and the length of their values.

#### Number of clients connecting to ConfigCat[​](#number-of-clients-connecting-to-configcat "Direct link to Number of clients connecting to ConfigCat")

Every time a client downloads the config JSON, it contributes to the overall Network Traffic.

#### Frequency of changes in the `config JSON`[​](#frequency-of-changes-in-the-config-json "Direct link to frequency-of-changes-in-the-config-json")

The `config JSON` is cached on the ConfigCat CDN. If there is no change, the ConfigCat CDN will respond with `304 Not Modified`. If there is a change, the ConfigCat CDN will respond with `200 OK` and the new `config JSON` content in the response body.

### Shared infrastructure[​](#shared-infrastructure "Direct link to Shared infrastructure")

The following plans run on shared infrastructure. So all customers use the same API nodes and Config Delivery Network (CDN).

| Plan           | Data / month |
| -------------- | ------------ |
| **Free**       | 20 GB        |
| **Pro**        | 100 GB       |
| **Smart**      | 1 TB         |
| **Enterprise** | 4 TB         |

info

If you hit this limit, we will keep your application up and running. However, you can expect us to contact you on how we can meet your needs.

### Dedicated infrastructure[​](#dedicated-infrastructure "Direct link to Dedicated infrastructure")

The following plans include dedicated API and CDN nodes.

#### Hosted[​](#hosted "Direct link to Hosted")

Runs on dedicated servers provided by ConfigCat.

|                   | Data / month |
| ----------------- | ------------ |
| **Basic package** | 24 TB        |

#### On-Premise (Self-hosted)[​](#on-premise-self-hosted "Direct link to On-Premise (Self-hosted)")

Runs on the customer's own servers. We suggest [contacting ConfigCat's engineering](https://configcat.com/support/) team on exact requirements and performance.

## How to reduce the monthly Network Traffic?[​](#how-to-reduce-the-monthly-network-traffic "Direct link to How to reduce the monthly Network Traffic?")

### Delete the old feature flags and unused Targeting Rules[​](#delete-the-old-feature-flags-and-unused-targeting-rules "Direct link to Delete the old feature flags and unused Targeting Rules")

If you have a large number of feature flags and Targeting Rules in a config, you can reduce the size of the `config JSON` by deleting the old ones. The [Zombie Flags](https://configcat.com/docs/zombie-flags.md) feature can help you finding stale feature flags.

### Avoid keeping lots of data in the comparison value of Targeting Rules or segments[​](#avoid-keeping-lots-of-data-in-the-comparison-value-of-targeting-rules-or-segments "Direct link to Avoid keeping lots of data in the comparison value of Targeting Rules or segments")

The comparison value of a Targeting Rule or segment is stored in the `config JSON` and downloaded by the SDKs. If you have a lot of Targeting Rules or segments with lengthy comparison values, you can reduce the size of the `config JSON` by shortening them.

### Consider the amount of text you keep in a text setting's value[​](#consider-the-amount-of-text-you-keep-in-a-text-settings-value "Direct link to Consider the amount of text you keep in a text setting's value")

Similarly to the comparison value of Targeting Rules or segments, the value of a text setting is stored in the `config JSON` and downloaded by the SDKs. If you have a lot of text settings with lengthy values, you can reduce the size of the `config JSON` by shortening them.

### Separate your feature flags into multiple configs[​](#separate-your-feature-flags-into-multiple-configs "Direct link to Separate your feature flags into multiple configs")

If you have a large number of feature flags, you can reduce the size of the `config JSON` by separating them into multiple configs. This way, the payload of each download will be smaller.

### Use the ConfigCat Proxy to cache/proxy config JSON downloads[​](#use-the-configcat-proxy-to-cacheproxy-config-json-downloads "Direct link to Use the ConfigCat Proxy to cache/proxy config JSON downloads")

The [ConfigCat Proxy](https://configcat.com/docs/advanced/proxy/proxy-overview.md) allows you to host a feature flag evaluation and config JSON proxy/cache service within your own infrastructure.<br /><!-- -->The [CDN proxy](https://configcat.com/docs/advanced/proxy/endpoints.md#cdn-proxy) feature allows you to proxy/cache config JSON downloads, and the ConfigCat SDKs can be routed to the ConfigCat Proxy running in your own infrastructure greatly reducing network traffic.

### Purchase additional network traffic[​](#purchase-additional-network-traffic "Direct link to Purchase additional network traffic")

You can purchase an add-on for your subscription to increase your limits. [Contact us](https://configcat.com/support/) for more information.

| Plan           | Price             | Additional config JSON downloads | Additional network traffic |
| -------------- | ----------------- | -------------------------------- | -------------------------- |
| **Smart**      | $250 or €229 / mo | +250 million                     | +1TB                       |
| **Enterprise** | $700 or €649 / mo | +1 billion                       | +4TB                       |
