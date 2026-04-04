# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/geo-sessions-stickier-location-based-sessions.md

# Geo-sessions: stickier, location-based sessions

In the past, businesses used sticky sessions to run multi-step procedures or mimic user behavior. At Nimble, we saw significant room to improve session quality, longevity, and accuracy.

Geo-sessions are our end-to-end upgrade to traditional sticky sessions that provide substantial upgrades across the board.

### How Geo-sessions work

Geo-sessions improve session stability, longevity, and quality by an order of magnitude. This is achieved through several pioneering methodologies:

* [x] **highly-durable residential IPs:** Nimble tests proxies for their stability and durability, and only the most reliable residential proxies are used in Geo-sessions.
* [x] **Minimum rotation:** by relaxing rotation-trigger sensitivity, Nimble minimizes proxy rotation unless it's absolutely necessary.
* [x] **ASN consistency:** Once a Geo-session starts, any time a proxy is rotated the newly selected proxy must use the same ASN as the initial proxy.
* [x] **Prioritizing proximity:** Beyond maintaining the same ASN, Nimble will also rotate a proxy with the physically closest available proxy.
* [x] **Geographical zone retention:** Beyond prioritizing proximity, Nimble defines a strict geographical radius of 15km around the initially selected proxy, and any new proxy rotated in must originate from within this zone.

These parameters work together to create highly consistent sessions. Even when IP rotation inevitably occurs, the new IP is highly-likely to replace the previous IP so well that it resembles **normal IP reassignment**, and the session continues normally.

{% hint style="success" %}
Geo-session peers are selected from within a 175 kilometer radius of the current peer.
{% endhint %}

### Why use Geo-sessions

Geo-sessions provide a reliable and effective solution to several key needs:

* [x] **Long, multi-step processes:** if your scraping needs require sessions that go through multiple steps, Geo-sessions can ensure session stability.
* [x] **Fully mimic user behavior:** by extending sessions to days and weeks, mimicking user behavior with data that persists continuously throughout the Geo-session becomes easier and substantially more effective.
* [x] **Multi-organizational and 3rd party sharing**: Because Geo-sessions are global, they can be shared across Nimble accounts, allowing for secure and compartmentalized collaboration with other organizations.

### Geo-sessions vs. sticky sessions

Both Geo-sessions and sticky sessions have their unique advantages. Geo-sessions offer substantially longer duration, highly-precise and consistent geotargeting, and minimum rotation. On the other hand, sticky sessions rotate unresponsive IPs faster, and may provide faster download speeds due to using a wider range of proxies.

<table><thead><tr><th width="226.66666666666663"> </th><th>Sticky Session</th><th>Geo-session</th></tr></thead><tbody><tr><td><strong>Rotation sensitivity</strong></td><td>Medium: unresponsive IPs are quickly replaced</td><td>Low: unresponsive IPs are given time to return</td></tr><tr><td><strong>Geotargeting during IP Rotation</strong></td><td>Medium: City targeting is the highest precision.</td><td>High: maintains 15km geographic zone.</td></tr><tr><td><strong>Performance</strong></td><td>high: uses many IPs and rotates unresponsive IPs.</td><td>Medium: algorithmically selects most stable IPs.</td></tr></tbody></table>

{% hint style="info" %}
Geo-sessions are currently only supported within the US. Support for additional countries is coming soon.
{% endhint %}

### Creating a new Geo-session

To create a new Geo-session, simply use the `geosession` flag with a random string that will serve as the new Geo-session ID:

{% hint style="info" %}
Geosession IDs are limited to between 16 to 32 alphanumeric characters (16 characters minimum).
{% endhint %}

{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}

{% hint style="warning" %}
For Geo-sessions to work properly, please extend your request timeout to at least 40 seconds on your http client (e.g Chrome/Puppeteer/Selenium/Curl/http code library, etc.).
{% endhint %}

### Geo-session IDs are Global

Traditional sticky session IDs are limited to your account, meaning:

* [x] Only you can access your sticky sessions.
* [x] Sticky session IDs need to be unique only within your account.

However, Geo-sessions are global across Nimble's platform. This means:

* [x] Geo-sessions can be securely shared with 3rd parties on Nimble's platform by sharing the session ID.
* [x] Geo-session IDs need to be unique across the Nimble platform.

To help ensure your custom Geo-session ID is unique, Nimble considers additional parameters when identifying a Geo-session. For example, the following request initiates a Geo-session in London, England:

{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-country-GB-city-london-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}

If another Geo-session with the same ID is started that targets a different location, this will be considered a separate session, and will receive a different proxy.

{% hint style="warning" %}
Be sure to use the same parameters across requests that share the same Geo-session. If the location targeting is changed, but the Geo-session ID remains the same, a new session will still be initiated.
{% endhint %}
