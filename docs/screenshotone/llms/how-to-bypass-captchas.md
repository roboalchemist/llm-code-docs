# Source: https://screenshotone.com/docs/guides/how-to-bypass-captchas/

# How to bypass CAPTCHAs

:::note
If you screenshot your websites or websites of your customers, follow our guide on [how to unblock ScreenshotOne in Cloudflare](/docs/guides/unblock-cloudflare-challenges/) (if relevant).
:::

Since the the launch of ScreenshotOne API, it was designed to perform ethical screenshotting, hence the ScreenshotOne API doesn't support bypassing CAPTCHAs, by default.

However, if you need to do that, and you know what you are doing within the legal boundaries, you can use a third-party services as a proxy with ScreenshotOne API.

For, example [Web Unlocker by Bright Data](https://brightdata.com/products/web-unlocker) is a service that can be used to bypass CAPTCHAs as a proxy.


## Web Unlocker by Bright Data

:::danger

**Use it only as the last resort and if you are ready to pay for the increased usage of Web Unlocker.**

You will see increased usage of your requests for in your Web Unlocker account. One ScreenshotOne API request might be equal to 100-500 requests (sometimes even more) for the Web Unlocker proxy.

The Web Unlocker solution is not designed to work well with browser automation tools like the ScreenshotOne API uses. Cause every browser request is counted as a separate request for the Web Unlocker: loading images, CSS files, scripts and similar.

Prefer using the residential [proxies](/docs/guides/how-to-use-proxies/) if you need to bypass CAPTCHAs.
:::

The Web Unlocker by Bright Data is a great way to bypass CAPTCHAs if you need to. However, be aware that the API response time might be slower than the normal one, and sometimes the requests even might fail. It relates to how proxies operate and depends on the stability of the proxy provider.

[Brigh Data Web Unlocker](https://brightdata.com/products/web-unlocker) solution has `pay-as-you-go` pricing model, and it is a great way to bypass CAPTCHAs if you need to.

However, be aware that the API response time might be slower than the normal one, and sometimes the requests even might fail. It relates to how proxies operate and depends on the stability of the proxy provider.

### 1. Create the Web Unlocker proxy

To create the Web Unlocker proxy, sign up to [Bright Data](https://brightdata.com/), and once you log in, choose `Web Unlocker` from the "Add" menu:

![The Bright Data Dashboard](dashboard.png)

Make sure to enable the CAPTCHA solver and premium domains if needed:

![The Web Unlocker creation screen](create.png)

Once created, you can choose the Node.js code example and copy the proxy URL:

![The Web Unlocker code example](proxy_url.png)

### 2. Use the Web Unlocker proxy with the ScreenshotOne API

In this example, the proxy URL is:

```
http://brd-customer-hl_99a0bd97-zone-your_unlocker_name:can1v3iuf18x@brd.superproxy.io:22225

```

Now, you can use this proxy URL in the ScreenshotOne API request:

```
https://api.screenshotone.com/take?key=<YOUR API KEY>&url=https://example.com&proxy=http://brd-customer-hl_99a0bd97-zone-your_unlocker_name:can1v3iuf18x@brd.superproxy.io:22225
```

## Residential proxies

It is worth to mention, that using residential proxies might also prevent CAPTCHAs from even showing up. Check out our guide on [how to use proxies](/docs/guides/how-to-use-proxies) to learn more.

It happens because with the residential IP addresses, usually there is no need to even show CAPTCHAs, since it looks like that the requests are coming from real users, not bots.

## Cost optimizations

To save money on proxies, you can try to use the option [fail_if_content_contains](/docs/options/#fail_if_content_contains) to fail the request if the content contains a certain string that might hint you that there is a CAPTCHA on the page.

The option returns a specific error code like: 
```
{
    "is_successful": false,
    "error_code": "content_contains_specified_string",
    "error_message": "The page content contains the specified string by the `fail_if_content_contains` option. If it seems to be a mistake or not what you expected, please, reach out to `support@screenshotone.com` as quickly as possible, and we will assist and try to resolve your problem.",
    "documentation_url": "https://screenshotone.com/docs/errors/content-contains-specified-string/"
}
```

Since you don't pay for the failed requests, you can only then retry the request with the same parameters, but with the proxy that bypasses CAPTCHAs.

## Any questions?

Read more about [how to use proxies](/docs/guides/how-to-use-proxies) in the ScreenshotOne API and if you have any questions, feel free to reach out to us at [support@screenshotone.com](mailto:support@screenshotone.com).