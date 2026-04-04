# Source: https://render.com/docs/quotaguard.md

# QuotaGuard Static IP

[QuotaGuard Static IP](https://www.quotaguard.com/quotaguard-static-ip-pricing/#QGstatic) Static IPs allow your services on Render to send outbound traffic through a load balanced pair of static IP addresses. Once set up, you can use QuotaGuard's IPs to connect to IP-restricted environments outside your Render network.

> You do not need QuotaGuard to connect to your databases or private services on Render.

## Getting Started

After [creating a QuotaGuard account](https://www.quotaguard.com/quotaguard-static-ip-pricing/#QGstatic), you will be redirected to a setup page with all the information needed to proxy your traffic through QuotaGuard's static IPs. Make note of the HTTP/S URLs and your static outbound IPs.

[image: QuotaGuard Configuration Page]

## Configuring Your Application

You can configure QuotaGuard the same way you would configure your app to use any HTTP proxy. [QuotaGuard provides examples](https://support.quotaguard.com/support/home) for common languages:

- [QuotaGuard for Go](https://www.quotaguard.com/docs/language-platform/go/)
- [QuotaGuard for Node.js](https://www.quotaguard.com/docs/language-platform/node-js/)
- [QuotaGuard for PHP](https://www.quotaguard.com/docs/language-platform/php/)
- [QuotaGuard for Python](https://www.quotaguard.com/docs/language-platform/python/)
- [QuotaGuard for Ruby](https://www.quotaguard.com/docs/language-platform/ruby/)

Most of these examples involve adding the `QUOTAGUARDSTATIC_URL` environment variable to your service in the Render Dashboard. Set the value to the *_HTTP/HTTPS URL_* from your QuotaGuard Outbound Proxy Setup page. Any requests your application makes using QuotaGuard's proxy URL will be routed through one of the IPs displayed in your QuotaGuard configuration.

> Using QuotaGuard Static IPs will add an additional hop to your network requests and can affect response times for your application. Make sure to test application response times before and after enabling QuotaGuard.

## Testing Your Implementation

Requests to `ip.quotaguard.com` always return the request client's IP address. Requests made to this address with your QuotaGuard proxy configuration will return one of the static IPs listed in your configuration.

```shell{outputLines:2}
curl -x QUOTAGUARDSTATIC_URL ip.quotaguard.com
=> {"ip":"52.34.188.175"}
```