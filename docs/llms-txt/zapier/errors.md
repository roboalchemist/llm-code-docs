# Source: https://docs.zapier.com/powered-by-zapier/api-reference/common-types/errors.md

# Source: https://docs.zapier.com/platform/build/errors.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/common-types/errors.md

# Source: https://docs.zapier.com/platform/build/errors.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/common-types/errors.md

# Source: https://docs.zapier.com/platform/build/errors.md

# Add error response handling

> If your API returns responses with a status code above 400 that should not automatically throw an error then Zapier recommends enabling skipThrowForStatus.

This feature allows you to create custom error handling script for status codes above 400. Note that 401 status codes will throw a `RefreshAuthError` [regardless](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#user-content-error-response-handling).

To enable `skipThrowForStatus`:

## 1. Enable skipThrowForStatus

* Log into the [Platform UI](https://zapier.com/app/developer).
* Select your **integration**.
* In the *Build* section in the left sidebar, click **Advanced**.
* Click the **Settings** tab.
* Click the **On** toggle next to *Enable skipThrowForStatus*.
* Click **Save**.

## 2. Use Code Mode to add error handling script

You'll need to add error handling script to your authentication, triggers, actions that could encounter the error using [Code Mode](/platform/build/code-mode).

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b285f7641f30a2f81d132c906407fcd2" data-og-width="1028" width="1028" data-og-height="169" height="169" data-path="images/9553266cb5a5ab7804d3f9ac1a9eed60.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=ab42d5913795cfa392418016121225eb 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=8ba9c4f4f1f960550960258a3a7aa5b9 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b2721e95ec64372b32be8b6352353a06 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=17ab4af6f3cac8ea0121753f248dc3b4 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=784b41a2901df8e27e91c2ab21763825 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=963e0c05bd4e8aed027069e050be5964 2500w" />
</Frame>

```js  theme={null}
return z.request(options).then((response) => {
  if (response.status === 404) {
    throw new z.errors.Error(
      "Insert error message to user here",
      "InvalidData",
      404,
    );
  }
  return response.json;
});
```

Learn more about [general error handling in Zapier](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#general-errors).

## Video Tutorial

You can refer to this video on implementing error handling:

<video controls src="https://cdn.zappy.app/dc5abf26e1f5b3e64d85361bb0d498b1.mp4" />

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
