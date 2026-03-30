# Source: https://help.aikido.dev/zen-firewall/zen-installation-instructions/zen-firewall-for-java-kotlin-and-groovy/spring-webflux.md

# Java (Spring WebFlux)

This guide will walk you through installing and setting up Zen Firewall by Aikido for your application. Follow the steps below to protect your application.

If you encounter any issues or problems, don't hesitate reach out on support chat or Github issues

<https://github.com/AikidoSec/firewall-java>

{% hint style="warning" %}
Spring WebFlux support is still evolving because of thread/context behavior in reactive pipelines.
{% endhint %}

## Requirements

* Java 17+ (tested up to Java 21; also supports Kotlin/Groovy with same agent).
* Spring WebFlux 3.x.
* [Aikido account](https://help.aikido.dev/getting-started/setting-up-your-account) & [Zen Firewall token](https://help.aikido.dev/zen-firewall/zen-installation-instructions/creating-an-aikido-zen-firewall-token)

## Installation & Configuration

{% stepper %}
{% step %}
**Install Zen Firewall by Aikido**

Download and extract the latest Java agent bundle:

{% tabs %}
{% tab title="zip" %}

```bash
curl -L https://github.com/AikidoSec/firewall-java/releases/latest/download/zen.zip -o zen.zip
unzip zen.zip
```

{% endtab %}

{% tab title="tar.gz" %}

```bash
curl -L https://github.com/AikidoSec/firewall-java/releases/latest/download/zen.tar.gz -o zen.tar.gz
tar -xzf zen.tar.gz
```

{% endtab %}
{% endtabs %}

Keep the extracted folder structure intact (for example `/opt/zen`) and make sure your process can read and write it.

Add the Java agent to your runtime:

```bash
-javaagent:/opt/zen/agent.jar
```

For rate limiting and user blocking features, add `agent_api.jar` to your project.

Gradle:

```gradle
dependencies {
    implementation files('/opt/zen/agent_api.jar')
}
```

Maven:

```xml
<dependency>
  <groupId>dev.aikido</groupId>
  <artifactId>agent_api</artifactId>
  <version>1.0</version>
  <systemPath>/opt/zen/agent_api.jar</systemPath>
</dependency>
```

{% endstep %}

{% step %}

#### Enable Request Blocking and User Identification

Use this middleware to enable rate limiting, user identification, and blocking features.

Zen Firewall does not require this middleware to block attacks. Core attack protection works without it. The middleware provides additional request context that Zen uses for protections such as [rate limiting](https://help.aikido.dev/zen-firewall/zen-features/setting-up-rate-limiting-for-routes), [user blocking](https://help.aikido.dev/zen-firewall/zen-features/blocking-users-with-zen-firewall), [bot blocking](https://help.aikido.dev/zen-firewall/zen-features/blocking-bot-traffic-with-zen-firewall), [country blocking](https://help.aikido.dev/zen-firewall/zen-features/blocking-traffic-by-country-with-zen-firewall), and [threat actor](https://help.aikido.dev/zen-firewall/zen-features/blocking-known-threat-actors-with-zen-firewall) blocking.

Adapt the example to fit how your application identifies users and handles requests.

Use a WebFilter that checks `ShouldBlockRequest`:

{% @aikido-custom-code/code-highlight language="java" content="+\@Component
+public class RatelimitingFilter implements WebFilter {

* @Override
* public Mono<Void> filter(ServerWebExchange exchange, WebFilterChain chain) {
* ```
     ShouldBlockRequest.ShouldBlockRequestResult result = ShouldBlockRequest.shouldBlockRequest();
  ```
*
* ```
     if (result.block()) {
  ```
* ```
         byte[] response = "You are blocked by Zen.".getBytes(StandardCharsets.UTF_8);
  ```
* ```
         exchange.getResponse().setStatusCode(HttpStatus.FORBIDDEN);
  ```
*
* ```
         if (result.data().type().equals("ratelimited")) {
  ```
* ```
             String message = "You are rate limited by Zen.";
  ```
* ```
             if (result.data().trigger().equals("ip")) {
  ```
* ```
                 message = message + " (Your IP: " + result.data().ip() + ")";
  ```
* ```
             }
  ```
* ```
             response = message.getBytes(StandardCharsets.UTF_8);
  ```
* ```
             exchange.getResponse().setStatusCode(HttpStatus.TOO_MANY_REQUESTS);
  ```
* ```
         }
  ```
*
* ```
         DataBuffer dataBuffer = exchange.getResponse().bufferFactory().wrap(response);
  ```
* ```
         return exchange.getResponse().writeWith(Mono.just(dataBuffer));
  ```
* ```
     }
  ```
*
* ```
     return chain.filter(exchange);
  ```
* }
  +}" %}

Set users in a filter that executes before the rate-limit filter:

{% @aikido-custom-code/code-highlight language="java" content="+import dev.aikido.agent\_api.SetUser;

+\@Component
+\@Order(1)
+public class SetUserFilter implements WebFilter {

* @Override
* public Mono<Void> filter(ServerWebExchange exchange, WebFilterChain chain) {
* ```
    SetUser.setUser(new SetUser.UserObject("123", "John Doe"));
  ```
* ```
    return chain.filter(exchange);
  ```
* }
  +}" %}
  {% endstep %}

{% step %}
**Start Zen Firewall in dry / detection-only mode**

```bash
AIKIDO_TOKEN=AIK_RUNTIME_... AIKIDO_BLOCK=false java -javaagent:/opt/zen/agent.jar -jar build/myapp.jar
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
**Test your app**

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
**Setup rate limiting in the dashboard**

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
**Next steps**

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
