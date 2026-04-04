# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/unexpected-requests-app-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unexpected Requests in App Logs

When you expose an app to the Internet using [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) with [External Placement](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#endpoint-placement) will likely receive traffic from sources other than your intended users.

Some of this traffic may make requests for non-existent or non-sensical resources.

## Cause

This is normal on the Internet, and there are various reasons it might happen:

* An attacker is [fingerprinting you](http://security.stackexchange.com/questions/37839/strange-get-requests-to-my-apache-web-server)

* An attacker is [probing you for vulnerabilities](http://serverfault.com/questions/215074/strange-stuff-in-apache-log)

* A spammer is trying to get you to visit their site

* Someone is mistakenly sending traffic to you

## Resolution

This traffic is usually harmless as long as your app does not expose major unpatched vulnerabilities.

So, the best thing you can do is to take a proactive security posture that includes secure code development practices, regular security assessment of your apps, and regular patching.
