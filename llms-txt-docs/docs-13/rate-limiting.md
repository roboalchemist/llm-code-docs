# Source: https://docs.solidfi.com/v2/api-reference/getting-started/rate-limiting.md

# Rate Limiting

> Solid Platform enforces rate limiting

Rate limiting protects APIs from excessive use and thereby limits their availability. To ensure all your programs can reliably use the Solid APIs and other services, we rate-limit access to those services to ensure no program, its end users, or malicious hackers abuse access. When a program's traffic exceeds its allocated rate limit, an HTTP 429 status code (Too Many Requests) is returned.

There are two rate-limiting points affecting the Solid platform:

1. Solid's AWS CloudFront rate limits
   Solid's cloud infrastructure limits all incoming traffic, including a Program's incoming Solid API HTTP traffic, on a per-client-IP-address basis to 1000 HTTP requests per rolling 5-minute window.
2. Solid API backend rate limits
   In the Sandbox environment, Solid default rate limits a program's traffic (across all client IP addresses) to:

* 50 read operations per second
* 50 write operations per second

In the Prod environment, Solid default rate limits a program's traffic (across all client IP addresses) to:

* 100 read operations per second
* 100 write operations per second

As a developer, when your application hits the rate limits, it will receive a 429 response. However, you must take a proactive approach by throttling your traffic before hitting the rate limits in the first place.

Solid may reduce limits or increase limits to enable high-traffic FinTech apps.

If you need a different limit, could be lower or higher, please let your account manager know, and the Solid team will review the request.

<Note>IPs whose traffic persistently exceeds this limit by a large margin may be throttled further.</Note>
