# Source: https://screenshotone.com/docs/guides/authenticated-pages/

# Screenshot authenticated pages

:::note
If you screenshot your websites or websites of your customers and you have a problem with Cloudflare challenges, follow our guide on [how to unblock ScreenshotOne in Cloudflare](/docs/guides/unblock-cloudflare-challenges/) (if relevant).
:::

There is a few methods to screenshot authenticated pages:

1. [If the website is yours or it allows to send a custom HTTP header with the authentication token when rendering the page.](#1-custom-http-header)
2. [If the website is yours, allow to bypass authentication for ScreenshotOne servers.](#2-allow-bypassing-authentication-for-screenshotone-servers)
3. [Using cookies.](#3-using-cookies)

## 1. Custom HTTP header

If the website is yours or it allows to send a custom HTTP header with the authentication token when rendering the page, you can use the following method:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://example.com&headers=Authorization: Bearer <your authentication token>
```

Or:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://example.com&authorization=Bearer <your authentication token>
```

Support the header name is different, e.g. `X-API-Key`, you can use the following syntax:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://example.com&headers=X-API-Key: <your authentication token>
```

## 2. Allow bypassing authentication for ScreenshotOne servers

This method is complicated and requires for you to configure your firewall to [allow the ScreenshotOne servers](/docs/ip-ranges/) to access the website.

## 3. Using Cookies

If the website you are trying to screenshot uses cookies to authenticate users and doesn't block automation or it is yours, you can use cookies with the ScreenshotOne API to render pages behind authentication.

I will use [ScreenshotOne's Dashboard](https://dash.screenshotone.com/) as an example. Suppose, I want screenshot the dashboard page (`https://dash.screenshotone.com/dashboard`):

![ScreenshotOne's Dashboard](./dashboard.png)

If I screenshot it straight away like:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://dash.screenshotone.com/dashboard
```

I will get the following result:

![Unauthenticated](./unauthenticated.jpeg)

It is an authenticated form.

Let's check cookies for the page, after I logged in:

![Cookies](./cookies.png)

Make sure to copy all the cookie parameters, including the `domain`, `path` and other parameters:

```
__Secure-better-auth.session_token=ZFmIsN7BVPU0Fzzd9aJ7lZU4TLSvu2L2.buMSGkHDIxhT%2B7YIl6tS82eGGLAAeRzk7FMp1YiTtK8%3D
domain=dash.screenshotone.com
path=/
HttpOnly
Secure
Lax
```

Then format it as required by the ScreenshotOne API:

```
__Secure-better-auth.session_token=ZFmIsN7BVPU0Fzzd9aJ7lZU4TLSvu2L2.buMSGkHDIxhT%2B7YIl6tS82eGGLAAeRzk7FMp1YiTtK8%3D; domain=dash.screenshotone.com; path=/; HttpOnly; Secure; Lax
```

And then try to screenshot the page again but with the cookies now:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://dash.screenshotone.com/dashboard&cookies=__Secure-better-auth.session_token=ZFmIsN7BVPU0Fzzd9aJ7lZU4TLSvu2L2.buMSGkHDIxhT%2B7YIl6tS82eGGLAAeRzk7FMp1YiTtK8%3D; domain=dash.screenshotone.com; path=/; HttpOnly; Secure; Lax
```

The result will be as expected:

![Authenticated](./authenticated.jpeg)

One pitfall is that likely you will need to write your own code to sign in to the website and get the cookies.

## Support

If you need help with screenshotting authenticated pages and any of the above methods does not work for you, please, contact us at `support@screenshotone.com`.