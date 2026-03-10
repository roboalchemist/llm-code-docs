# Source: https://screenshotone.com/docs/guides/fail-if-content-contains/

# Fail rendering if the content contains a string

There is a set of use cases when you want to fail screenshot rendering and retry it if the content of the page contains a string.

For example, if you use residential rotating proxies and a site blocks you with some specific test, you might want to retry the request instead of getting the successful screenshot of the page with the CAPTCHA or an error.

:::tip[Did you know?]
You don't pay for failed and cached screenshots with ScreenshotOne.
:::

That's exactly what you need the option `fail_if_content_contains` for.

Let's quickly see how it works and how you can use it. Let's first render the example.com page:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://example.com
```

The result is:

![The example.com website](example.com.png)

Now, let's try to fail it:

```
https://api.screenshotone.com/take?fail_if_content_contains=Illustrative+Examples+In+Documents&access_key=<your access key>&url=https://example.com
```

The result is:

```json
{
    "is_successful": false,
    "error_message": "The page content contains the specified string by the `fail_if_content_contains` option. If it seems to be a mistake or not what you expected, please, reach out to `support@screenshotone.com` as quickly as possible, and will assist and try to resolve your problem.",
    "error_code": "content_contains_specified_string",
    "documentation_url": "https://screenshotone.com/docs/errors/content-contains-specified-string/"
}
```

As you might notice, the match is case insensitive, it is done for simplicity.

You can also specify multiple strings to fail if any of them is matched on the page content:

```
https://api.screenshotone.com/take?fail_if_content_contains=Prior&fail_if_content_contains=Example&access_key=<your access key>&url=https://example.com
```

## A few more similar options

Check out the other similar options:

- [Fail rendering if the content is missing a string](/docs/options/#fail_if_content_missing)
- [Fail rendering if the request fails](/docs/options/#fail_if_request_failed)

## Support

If you have any questions or need help, please, reach out to `support@screenshotone.com` as quickly as possible, and we will assist and try to resolve your problem.