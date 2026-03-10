# Source: https://render.com/docs/uptime-best-practices.md

# Best Practices for Maximizing Uptime

To help keep your Render services healthy and responsive, we recommend the following best practices. Many of these apply to services on _any_ deployment platform—not just Render!

## Run more than one instance

Server hardware isn't perfect, and neither are the data centers that orchestrate that hardware. When you [scale your service to multiple instances](scaling), Render runs those instances on different nodes. This means that if a particular instance (or an entire node) goes down, at least one instance of your service stays up and running.

[diagram]

When issues like these occur, Render also _automatically_ moves affected services to new instances, but this can take a few minutes. By running multiple instances, your service remains up during the automatic transition.

## Enable health checks

Sometimes a service instance gets into an unresponsive state and needs a quick restart. Render can detect this situation with [*health checks*](/deploys#health-checks).

You define an HTTP endpoint path in your service that always returns a `2xx` response (if the service is functioning normally), and Render sends periodic requests to that path. If those requests fail several times in a row for a particular instance, Render restarts it.

Health checks also protect you from bad deploys: if a new deploy fails its health check, Render keeps the previous deploy running.

[Learn more about health checks.](/deploys#health-checks)

## Log the `CF-Ray` ID of each request

All inbound requests to Render web services pass through Cloudflare for [DDoS protection](ddos-protection):

[diagram]

Cloudflare assigns a unique ID to each request and sets it as the value of the `CF-Ray` HTTP header. Render includes this header in the request it sends along to your service.

Whenever your web service receives an incoming request, it should include the value of the `CF-Ray` header in all logs generated for that request, including logging as soon as the request is received.

Tracking the `CF-Ray` ID for each request helps you trace the execution of your individual requests, and it also helps Render's support team diagnose any issues that might occur earlier in this request flow.

## Set up an external monitoring probe

An external monitoring probe is similar to a [health check](#enable-health-checks), but it sends periodic HTTP requests to your web service from _outside_ Render. This more closely simulates traffic from your service's users.

We recommend creating your probe with a third-party monitoring provider, such as [HeyOnCall](https://heyoncall.com/guides/monitoring-your-render-app-with-heyoncall) or [Better Stack](https://betterstack.com/docs/uptime/monitoring-start/). In case of an incident, your provider will send a notification that includes the `CF-Ray` ID returned by Cloudflare. This is handy for debugging in combination with your [service's logs](#log-the-cf-ray-id-of-each-request), or for sharing with Render support.

## Add retry logic to clients

If you maintain long-lived connections to your service (such as over WebSocket), make sure to implement retry logic for those connections. Render routes each connection to a _particular instance_ of your service running on a _particular machine_, and Render might replace an instance at any time as part of a deploy or standard maintenance.

Replacing an instance this way is a [zero-downtime](/deploys#zero-downtime-deploys) event, but terminating the old instance does by necessity terminate all connections to it. By implementing retry logic, you can quickly restore your long-lived connection to a running instance.

## Test your data backups

Database hiccups happen, and you can resolve them much faster when you've prepared ahead of time. Make sure you've thoroughly tested your data backup and [recovery procedure](postgresql-backups#perform-a-recovery), so you can fix your service as quickly as possible whenever the time comes.