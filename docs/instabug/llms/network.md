# Source: https://docs.instabug.com/references/application-performance-monitoring/network.md

# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-application-performance-monitoring/network.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-application-performance-monitoring/network.md

# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/application-performance-monitoring/network.md

# Network

**Here are a few examples:**

| URL pattern example          | Matches with                         | Doesn't match with                                                                                        |
| ---------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `sample.com/part1/part2`     | `sample.com/part1/part2`             | `sample.com/part1`                                                                                        |
| `sample.com/part1/*`         | `sample.com/part1/part2`             | `sample.com/part1/part2/part3`                                                                            |
| `sample.com/part1/*/part3`   | `sample.com/part1/part2/part3`       | <p><code>sample.com/part1/part3/part4</code><br><code>sample.com/part1/part2/part3/part4</code></p>       |
| `sample.com/part1/*/*/part4` | `sample.com/part1/part2/part3/part4` | <p><code>sample.com/part1/part2/part4</code><br><code>sample.com/part1/part2/part3/part4/part5</code></p> |
| `sample.com/part1/*/*/*`     | `sample.com/part1/part2/part3/part4` | <p><code>sample.com/part1/part2/part3/part4/part5</code><br><code>sample.com/part1/part2/part3</code></p> |

**Some notes to consider while creating your URL patterns:**

* Custom URL patterns that you define have higher precedence than the auto-generated ones. If the same call matches with a custom and an auto pattern, it gets grouped with the custom.
* At any point, you can delete a pattern to prevent grouping new calls with it.
* URL patterns shouldn't overlap. Each incoming network call gets grouped with only one pattern. In case of conflict, it gets merged with the newest pattern.

{% hint style="info" %}
📘 Creating or deleting patterns doesn’t affect your old data that has already been grouped. It only affects the upcoming network requests.
{% endhint %}

***

### Network Calls Apdex

Luciq calculates an Apdex score for every network request (URL pattern) in your app. Apdex score ranges between 0 and 1. The higher the value, the closer you are to satisfying a user experience:

* Apdex score ≥ 0.94 equates to **Excellent** performance.
* Apdex score ≥ 0.85 and < 0.94 equates to **Good** performance.
* Apdex score ≥ 0.7 and < 0.85 equates to **Fair** performance.
* Apdex score ≥ 0.5 and < 0.7 equates to **Poor** performance.
* Apdex score < 0.5 is considered **Unacceptable**.

#### How Is the Network Calls Apdex Calculated?

When a network call occurrence is collected, it is flagged based on a pre-defined target (T). A network call occurrence is considered:

* **Satisfying:** if its duration ≤ T
* **Tolerable:** if its duration > T and ≤ 4T
* **Frustrating:** if its duration > 4T or if it fails due to a server-side or client-side error.

Then, based on the bucketing explained above, the Apdex is calculated:

* `Total occurrences = Satisfying occurrences + Tolerable occurrences + Frustrating occurrences`
* `Apdex score = (Satisfying occurrences + 0.5 * Tolerable occurrences) / Total occurrences`

#### How Can You Control a Specific Network Call's Target?

By default, it is set to **0.5 seconds**; however, you can easily change this number from your dashboard by clicking on the action highlighted in the screenshots below.

<figure><img src="https://files.readme.io/e89764232733ce5387e6c323c6ac8f8a4f09027183a6a036bc8d23bf4a4092fe-image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://files.readme.io/907d773144802847b60c2e99f48e4523a2a0483b0809cb8f62067b050dec7626-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
📘 Please note that updating your response time target does **not** affect the already stored occurrences; only future occurrences will be flagged using the new target.
{% endhint %}

### Network Latency Breakdown

You can see the P50s, P95s, and the frequency of each stage/operation that occurred inside a network group. These are the stages/operations that were made to send the network request and receive its response from the server.

The feature works out of the box without any instrumentation, and the stages are shown inside the Spans table inside the Network metric.

The spans table contains the following stages:

* DNS Lookup
* Connection Handshake
* TLS Connection
* Uploading Request
* Downloading Response
* Server Processing

<figure><img src="https://files.readme.io/17631abeb5264f4e35785b67fabcbee2814b85a1b2e6c71594e3fada1e02b7c8-ios-apm-network-1.png" alt=""><figcaption></figcaption></figure>

You can also see the breakdown and visualize the stages' timeline on an occurrence level inside the occurrences page.

<figure><img src="https://files.readme.io/ce4899c575bf561ff4ea8ea8c2543406c194852a263aea0715b7f3fc4cfca2aa-ios-apm-network-2.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}

#### 📘 Minimum SDK Version

The minimum required SDK version for this feature is v12.1.0.
{% endhint %}
