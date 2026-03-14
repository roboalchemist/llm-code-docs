# Source: https://help.aikido.dev/zen-firewall/zen-installation-instructions/zen-firewall-for-node.js-javascript-and-typescript/restify.md

# Node.js (Restify)

This guide will walk you through installing and setting up Zen Firewall by Aikido for your application. Follow the steps below to protect your application.

If you encounter any issues or problems, don't hesitate reach out on support chat or Github issues

<https://github.com/AikidoSec/firewall-node>

## Requirements

* Node.js 16+.
* Restify 8.x to 11.x.
* [Aikido account](https://help.aikido.dev/getting-started/setting-up-your-account) & [Zen Firewall token](https://help.aikido.dev/zen-firewall/zen-installation-instructions/creating-an-aikido-zen-firewall-token)

## Installation & Configuration

{% stepper %}
{% step %}

#### Install Zen Firewall by Aikido

Install Zen in your project:

{% tabs %}
{% tab title="npm" %}

```bash
npm install --save-exact @aikidosec/firewall
```

{% endtab %}

{% tab title="Yarn" %}

```bash
yarn add --exact @aikidosec/firewall
```

{% endtab %}

{% tab title="pnpm" %}

```bash
pnpm add --save-exact @aikidosec/firewall
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="require Syntax" %}
Load Zen **before** any other imports:

{% @aikido-custom-code/code-highlight language="javascript" content="+require("@aikidosec/firewall");

const restify = require("restify");
const server = restify.createServer();" %}
{% endtab %}

{% tab title="import Syntax" %}
Import Zen **before** any other library:

{% @aikido-custom-code/code-highlight language="typescript" content="+import "@aikidosec/firewall";

import restify from "restify";
const server = restify.createServer();" %}

{% hint style="warning" %}
Many TypeScript projects use `import` syntax but still compile to CommonJS — in that case, the setup above works as-is. If your app runs as **native ESM** (e.g. `"type": "module"` in package.json), see [**ESM setup**](https://help.aikido.dev/zen-firewall/zen-installation-instructions/zen-firewall-for-node.js-javascript-and-typescript/node.js-esm) for additional steps.
{% endhint %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}

#### Enable Rate limiting and User blocking

{% @aikido-custom-code/code-highlight language="javascript" content="+const Zen = require("@aikidosec/firewall");
\+
+// Optional middleware to set user for rate limiting or blocking specific users
+server.use((req, res, next) => {

* Zen.setUser({ id: "123", name: "John Doe" });
* return next();
  +});
*

+// Call this after auth middleware, as early as possible in the middleware stack
+Zen.addRestifyMiddleware(server);" %}
{% endstep %}

{% step %}

#### Start Zen Firewall in dry / detection-only mode

```bash
AIKIDO_BLOCK=false AIKIDO_TOKEN=AIK_RUNTIME_ node app.js
```

Set the token as an environment variable so the Aikido Zen agent can pick it up. If you don't have a token yet, follow [instructions here](https://help.aikido.dev/zen-firewall/zen-installation-instructions/creating-an-aikido-zen-firewall-token).

```bash
AIKIDO_TOKEN=AIK_RUNTIME_
```

We recommend to start your app in dry mode  to ensure it works as expected without blocking any requests. We advise running Zen Firewall in staging for two weeks to avoid false positives.

```bash
AIKIDO_BLOCK=false
```

{% hint style="info" %}
You can use `AIKIDO_DEBUG=true` to enable debug mode for more detailed information about what the agent is doing. For more information about your environment variables: [configuration-via-environment-variables](https://help.aikido.dev/zen-firewall/zen-installation-instructions/configuration-via-environment-variables "mention")
{% endhint %}
{% endstep %}

{% step %}

#### Test your app

Browse to your application and perform a couple of actions or open a couple of pages. Zen will automatically discover the routes in your application.&#x20;

{% hint style="info" %}
Zen sends data back to Aikido every 10 minutes
{% endhint %}

You can verify a working agent by looking at the following pages of your Zen application:

* **Events**: Should show an "Application started" event.
* **Routes**: After some time your application routes will start showing here with the method, route and requests.
* **Instances**: Should show the number of active instances for your application where Zen is installed.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FcBVQ6hPTYOWgbnRaVIZI%2FScreenshot%202025-06-23%20at%2010.08.35.png?alt=media&#x26;token=eae8f436-01b9-478e-872e-b3813232196b" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Setup rate limiting in the dashboard

When you've added the Zen Firewall middleware you can test protecting a route from brute force attacks, you do this by setting up rate limit in the Aikido Dashboard:

1. Click on the created app.
2. Go to the **Routes** tab.
3. Find the route you would like to limit and click **Setup rate limiting**.
4. Follow the instructions to configure the rate limit (e.g., 5 requests per minute).

![API route management interface showing authentication routes with protection and rate limiting options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuLKgJLpyKEIZhfq0dEEi%2FScreenshot%202025-10-30%20at%2010.38.17.png?alt=media\&token=db7263f6-b9ec-4da2-94ac-180a295eb535)

![Set rate limiting for POST /auth/login to 5 requests per minute.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2633dcea71b485b0257ecf6b607323a9646dae06%2Fsetup-and-installation-of-zen-firewall-for-java_f0ecf04a-31ae-4057-b23d-8c8b18d2f353.png?alt=media)

**Verify Rate Limiting**

Start your app and try to access the route you've rate limited 5 times within a minute. After the fifth attempt, you should receive a rate limit error:

```
You are rate limited by Aikido firewall. (Your IP: 1.2.3.4)
```

{% endstep %}

{% step %}

#### Next steps

Congrats you've successfully installed Zen Firewall. If you encountered any problems, have concerns or feature requests, don't hesitate to reach out to support.

You can now go and explore the many features that Zen Firewall provides:

* [blocking-bot-traffic-with-zen-firewall](https://help.aikido.dev/zen-firewall/zen-features/blocking-bot-traffic-with-zen-firewall "mention")
* [blocking-tor-traffic-with-zen-firewall](https://help.aikido.dev/zen-firewall/zen-features/blocking-tor-traffic-with-zen-firewall "mention")
* [blocking-users-with-zen-firewall](https://help.aikido.dev/zen-firewall/zen-features/blocking-users-with-zen-firewall "mention")
* [blocking-known-threat-actors-with-zen-firewall](https://help.aikido.dev/zen-firewall/zen-features/blocking-known-threat-actors-with-zen-firewall "mention")
* [blocking-traffic-by-country-with-zen-firewall](https://help.aikido.dev/zen-firewall/zen-features/blocking-traffic-by-country-with-zen-firewall "mention")
* [setting-up-rate-limiting-for-routes](https://help.aikido.dev/zen-firewall/zen-features/setting-up-rate-limiting-for-routes "mention")
* [monitor-outbound-domains](https://help.aikido.dev/zen-firewall/zen-features/monitor-outbound-domains "mention")

Additional information:

* [how-zen-works-performance-reliability](https://help.aikido.dev/zen-firewall/miscellaneous/how-zen-works-performance-reliability "mention")
* [blocking-vs-detection-mode-in-zen-firewall](https://help.aikido.dev/zen-firewall/zen-features/blocking-vs-detection-mode-in-zen-firewall "mention")
* [understanding-your-zen-statistics](https://help.aikido.dev/zen-firewall/zen-features/understanding-your-zen-statistics "mention")
  {% endstep %}
  {% endstepper %}
