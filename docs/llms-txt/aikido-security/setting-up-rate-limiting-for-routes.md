# Source: https://help.aikido.dev/zen-firewall/zen-features/setting-up-rate-limiting-for-routes.md

# Setting Up Rate Limiting for Routes

### Introduction <a href="#introduction" id="introduction"></a>

Zen Firewall by Aikido allows you to **set up rate limiting on routes** to protect your application from abuse, such as preventing excessive password reset requests. You can rate limit, webpages, REST API routes as well as GraphQL APIs.

> Check the [functionality support matrix](https://help.aikido.dev/doc/getting-started-with-zen/doccLOR8KzO0#functionality-support-matrix) to see if your framework supports rate limiting.

### Supported Functionality <a href="#supported-functionality" id="supported-functionality"></a>

* Set rate limiting on specific routes
* Set rate limiting on multiple routes by adding a wildcard\* route
* Set rate limiting on IP address or [user ID](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1#how-to-identify-and-block-users), or a [custom group ID](#how-it-works) (e.g. company ID for B2B SaaS)
* Disable protection for a specific route instead disabling protection for your entire app.
* [Localhost](http://localhost) or 127.0.0.1 is never rate limited

> Rate limiting is based on individual IP addresses or [user identification](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1#how-to-identify-and-block-users).\
> For example, if the limit is 10 requests per minute:
>
> * ❌ **Blocked**: A single IP making 11 requests will be
> * ✅ **Allowed:** 11 different IPs making one request each
>
> This helps prevent abuse while allowing normal traffic from multiple users.

### How to set up rate limiting <a href="#how-to-set-up-rate-limiting" id="how-to-set-up-rate-limiting"></a>

Step 1: Navigate to a specific app and open the Routes tab

Step 2: Open Action Menu of the specific route you wish to apply rate limiting to. Clicking Setup rate limiting will open a modal.

![API routes management interface showing method, route, app name, rate limiting, and status.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdFXeFgXFLqe6CPvyBzP9%2FScreenshot%202025-10-30%20at%2010.38.17.png?alt=media\&token=7b396c10-eddb-4f93-acfc-062af8de82b8)

**Step 3**: **Enable Rate Limiting** and specify the number of requests allowed per timeframe. Save by updating the routes.

![Enable and configure rate limiting for PATCH requests to /api/v2/posts/:number.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F2SOgwvs5MTnTh1SwT0G6%2FScreenshot%202025-10-30%20at%2012.06.25.png?alt=media\&token=dd220d77-8a84-425f-86b6-2a4a9bade2e2)

> Config changes take up to 1 minute to take effect.

### Setting up rate limiting for multiple routes at once <a href="#setting-up-rate-limiting-for-multiple-endpoints-at-once" id="setting-up-rate-limiting-for-multiple-endpoints-at-once"></a>

You can set up rate limiting for multiple routes at once by adding a wildcard route.

**Step 1.** On the routes page, click **Add Route.**

![API routes table showing route, app name, rate limiting, and protected status.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeEcaIhW5bnyRaHhGrj4F%2FScreenshot%202025-10-30%20at%2012.06.53.png?alt=media\&token=6cbc1f91-feb1-41fb-b71d-08917369809b)

**Step 2.** Add a wildcard route by adding an `*` in the route.

![Add an API route with rate limiting in Aikido Firewall settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FwP2qpLAsPPeSciEx9pEQ%2FScreenshot%202025-10-30%20at%2012.06.59.png?alt=media\&token=45c31655-c851-417d-abca-f15f79f0cc4e)

**Step 3.** The wildcard will appear now in the list. Proceed to set up rate limiting the same way as above.

![POST /auth/\* route: Demo app, 10 requests/min, Protected status.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJx87XTOnONwyuSV3hhtd%2FScreenshot%202025-10-30%20at%2012.07.54.png?alt=media\&token=051e2152-9a71-4ed4-b274-f47a86e95e3d)

## How it works <a href="#how-it-works" id="how-it-works"></a>

### **Order of operations**

Aikido Zen enforces rate limits in the following order of priority:

1. Group level
2. User level
3. IP level

Once a request is rate limited at a higher level (e.g., group), the lower levels (user or IP) are not evaluated.

### **Sliding window**

Tracks events using a moving time frame that continuously slides forward. Unlike fixed windows that reset at specific times, sliding windows maintain a rolling count of the most recent period (e.g., last 60 seconds). This prevents edge cases where brief traffic spikes could bypass limits at window boundaries.

### **Route selection (wildcards)**

Zen will first select the exact route match (without wildcards) to apply a rate limit. If no exact route is found wildcard matches are applied based on the lowest limit. Only one limit is applied at any given time, a single requests will never hit multiple limits.

### **Group-based rate limiting**

To limit the number of requests for a group of users, you can use the `setRateLimitGroup` function. This is useful if you want to limit the number of requests per team or company. Please note that if a rate limit group is set, the configured rate limits are only applied to the group and not to individual users or IP addresses.

Available for:

* [Node.js](https://github.com/AikidoSec/firewall-node/blob/main/docs/user.md#rate-limiting-groups)
* [Python](https://github.com/AikidoSec/firewall-python/blob/main/docs/user.md#rate-limiting-groups)
* [Java](https://github.com/AikidoSec/firewall-java/blob/main/docs/user.md#rate-limiting-groups)
* Other agents will follow soon
