Source: https://docs.slack.dev/changelog/2019-07-deprecate-early-tls-versions

# Deprecate early TLS versions

July 1, 2019

When your app, custom integration, or bot communicates with Slack via HTTP, it uses [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) to ensure data privacy and integrity.

There are multiple major versions of TLS, including `v1.0`, `1.1`, `1.2`, and `1.3`. Versions `1.0` and `1.1` are deprecated and should no longer be used.

On **March 4, 2020**, we'll require all communications with Slack to use TLS version `1.2` or greater.

All TLS connections must use the [SNI extension](https://en.wikipedia.org/wiki/Server_Name_Indication). Lastly, TLS connections must support at least one of the following supported cipher suites:

* `ECDHE-RSA-AES128-GCM-SHA256`
* `ECDHE-RSA-AES256-GCM-SHA384`
* `ECDHE-RSA-AES128-SHA`
* `ECDHE-RSA-AES256-SHA`
* `AES128-GCM-SHA256`
* `AES256-GCM-SHA384`

Using TLS version `1.2` or greater makes Slack safer for everyone.

## What's changing {#what}

On March 4, 2020, we'll require all apps, custom integrations, bots, and users communicating with Slack to use TLS version `1.2` or greater.

All TLS connections must use the [SNI extension](https://en.wikipedia.org/wiki/Server_Name_Indication). Lastly, TLS connections must support at least one of the following supported cipher suites:

* `ECDHE-RSA-AES128-GCM-SHA256`
* `ECDHE-RSA-AES256-GCM-SHA384`
* `ECDHE-RSA-AES128-SHA`
* `ECDHE-RSA-AES256-SHA`
* `AES128-GCM-SHA256`
* `AES256-GCM-SHA384`

## How do I prepare? {#how}

Preparing for a new TLS version involves two steps. First, check which version of TLS your app uses. Second, if you're not already using TLS `1.2` or greater, update your TLS version.

Good news: ​​if your app is built using modern versions of your programming language, HTTP libraries, and frameworks, you likely don’t need to make any changes.

Check [this list of affected apps](https://api.slack.com/unsafe-tls-deprecation) to see if your app needs any changes.

You can also use several different online, third-party tools to check which TLS version you're using. For example, check your app's TLS version by pinging the following URL with the same HTTP client or infrastructure that you use in your app, integration, or bot.

```text
https://www.howsmyssl.com/a/check
```text

For language-specific instructions, read on.

### Python {#python}

Use the following command to identify which version of TLS your app is using:

```text
python3 -c "import json, urllib.request; print(json.loads(urllib.request.urlopen('https://www.howsmyssl.com/a/check').read().decode('UTF-8'))['tls_version'])"
```text

While we recommend using Python 3 if possible, we know that some developers still use Python 2. In that case, use the following command instead:

```text
 python -c "import json, urllib2; print json.load(urllib2.urlopen('https://www.howsmyssl.com/a/check'))['tls_version']"
```text

​​If your TLS version is less than `1.2`, first ensure that you are using a version of Python which supports TLS `1.2` and higher: Python `3.3.0+` or Python `2.7.8+`. ​​ ​​Then, check dependencies for available upgrades. For example, to update to the latest version of requests​, use `pip install requests --upgrade​`.

### Node.js {#node}

Check your Node installation using the following command:

```text
node -e "var https = require('https'); https.get('https://www.ssllabs.com/ssltest/viewMyClient.html', function(res){ console.log(res.statusCode) });"
```text

​​A `200` status code means your app is using TLS version `1.2` or greater. If your TLS version is less than `1.2`, ensure that you are using a supported version of Node. Node versions follow a support schedule called the [LTS support schedule](https://nodejs.org/en/about/releases/). If you haven’t already, you should make plans to adopt [Node v12 LTS](https://nodejs.org/download/release/latest-v12.x/) before March 4, 2020. `v12` guarantees a TLS version `1.2` or greater. In advance of this, we'll implement a 24-hour test deprecation on February 19, 2020.

### Java {#java}

​​If you are using Java `8`, TLS `1.2` is enabled by default and you do not need to make any changes. ​​ ​​If you are using Java `7`, TLS `1.2` will need to be enabled manually. Depending on the specific API or framework your code uses, you will enable it differently. [This site](https://www.baeldung.com/java-7-tls-v12) provides steps for the most popular ways to enable TLS 1.2. ​​ ​​If you are using Java `6` or below: sadly, you'll need to upgrade to a later version. TLS 1.2 is not supported on these versions.

### Other languages {#other}

​​**Go**

​​All versions of Go support TLS 1.2 by default. There’s no need to make any changes.

​​**Ruby**

​​Check your Ruby installation using the following command:

```text
 ruby -r'net/http' -e 'puts Net::HTTP.get(URI("https://www.howsmyssl.com/a/check"))'
```text

If you're not at TLS version `1.2` or greater, upgrade your version of Ruby. TLS `1.2` is supported on Ruby version `2.0.0` and higher.

​​\*\*.NET / C#\*\*

​​If you are using the .NET Framework, you should use v4.5 or higher. A more detailed guide for TLS 1.2 support across the various versions of .NET is available at [Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/tls).

## What if I do nothing? {#nothing}

If you do nothing and your app uses TLS version `1.0` or `1.1`, Slack will refuse your app's HTTP requests beginning March 4, 2020. In advance of this, Slack will also refuse your app's HTTP requests on February 19, 2020. We encourage you to update your app before then so your users don't experience any problems.

## When does this happen? {#when}

TLS version `1.2` or greater will be required on March 4, 2020. As always, [let us know](https://slack.com/help/requests/new) if you have concerns or questions. We're here for you.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
* [Deprecation](/changelog/tags/deprecation)
