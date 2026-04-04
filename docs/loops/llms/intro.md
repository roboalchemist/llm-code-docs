# Source: https://loops.so/docs/guides/intro.md

# Source: https://loops.so/docs/api-reference/intro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Introduction

> The Loops REST API lets you manage your contacts, send events and send transactional email.

## Authentication

<Warning>
  Your Loops API key should never be used client side or exposed to your end
  users.
</Warning>

Start here if you want to use the Loops API to add contacts to your Loops audience,
update their attributes, and send events to Loops.

<Accordion title="Authentication Steps">
  To get started, you'll need an API key. Go to [Settings -> API](https://app.loops.so/settings?page=api) in Loops and click **Generate key**.

  <img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d1f3115197ec809cb8713e2ea57ef03f" alt="" data-og-width="1430" width="1430" data-og-height="359" height="359" data-path="images/authentication-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b9f12e1e414172597193b11ef978216a 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=949bf24692620558e45aa77b3f5622fb 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=3709da7aedda70097b7a1015da70b5d7 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=bb27f1cf6104c3eae2ef0c7a290ad29e 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=dbcb6fca36c6ba75c1a91ca35fdeb2e8 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-1.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d46212c3c28f69666e52dc90faf36f9e 2500w" />
  This creates an API key. You can assign it a human-readable name:
  <img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7bdd41a72e81e88aecc6c242049e5bd0" alt="" data-og-width="1430" width="1430" data-og-height="242" height="242" data-path="images/authentication-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f8ddddea42c7a1620f1bf83180f0c22d 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7afc921f8ac32166a4de84ecba86dda2 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=cdf71e2417587c5c13ab01e6dc796e68 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=713c9a1ce7ddd841d27361b75ede9d27 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=421a9420ce25aa7e63a2c6de58554487 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-2.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=656e0cb701d99210a670e9e1df976f12 2500w" />
  We suggest using a different API key for different purposes. You can revoke an API key at any time with the trash icon.

  When making an API call, add an Authorization header and set the API key as a Bearer token:
  <img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=89b339ef97fd1f1d54a11f4be52e4455" alt="" data-og-width="1430" width="1430" data-og-height="148" height="148" data-path="images/authentication-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a4f4efcb2cdfd86e2f39aad94cdf7bc5 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6155aa3b71bec86a48953724232d8e61 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5c99f5e829f1f6559d88782cf7577f1e 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d2aa615e26a41c59db4e1c33dbc31b4f 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c49732b9252db0f9c3adbfb52e6a45e6 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/authentication-3.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=869f9e89e53b74b5ba62b247150b0219 2500w" />

  You can test your API key by making a `GET` request to

  ```
  https://app.loops.so/api/v1/api-key
  ```

  If successful, you will receive the following response:

  ```
  {
    "success": true
  }
  ```

  Here's an example Curl request (replace `d2d561f5ff80136f69b4b5a31b9fb3c9` with your own API key):

  ```bash  theme={"dark"}
  curl https://app.loops.so/api/v1/api-key -H "Accept: application/json" -H "Authorization: Bearer d2d561f5ff80136f69b4b5a31b9fb3c9"
  ```
</Accordion>

## Rate Limiting

To ensure the quality of service for all users, our API is rate limited. This means there's a limit to the number of requests your application can make to our API in a certain time frame. The baseline rate limit is **10 requests per second per team**.

<Accordion title="Rate Limiting Details">
  To see your current usage, we provide the following response headers in every API response:

  * `x-ratelimit-limit`: The maximum number of requests you can make per second.
  * `x-ratelimit-remaining`: The number of requests remaining in the current rate limit window.

  Here is an example of a successful response with rate limit headers:

    <img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e5a91eaa1ae89d9938439b0ec9fa2c19" alt="" data-og-width="705" width="705" data-og-height="175" height="175" data-path="images/api-successful-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=371214bda7bf4ade93c48f4072887a1d 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=89ff68bbe88ebe1fc9f147975f8d79bd 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=92e92c82b68049494273b9697b4d0b1a 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c7fa4c8255de81dab213bb6a333e6efc 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=92ef6994e652c11130b307be1a6a7eeb 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-successful-response.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=10bb665f9ae21cfd02b9066030b2bb96 2500w" />

  If you exceed this limit, you'll receive a response with HTTP status `429 Too Many Requests`. Here is an example of a failed response with rate limit headers:

    <img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=9008b344cb25eab08a74e1df468b72e4" alt="" data-og-width="699" width="699" data-og-height="171" height="171" data-path="images/api-rate-limited.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5091956297ec524b2c4ec40d749b6f74 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b88a91db05eb2c57cc891534b9203b2e 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2278b37b7db0ffa4bac98319d5267aa5 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=3c5d8e9e42c0c6ac1b063cf6b1f7e9ba 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=accbbe22ad4f2d7b0114713bcb8c63f9 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/api-rate-limited.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6c336e2e909b0fc1b2c4544bee821561 2500w" />

  It's important to handle these 429 responses in your application. We recommend implementing retries with an exponential backoff strategy.

  If your use case requires a higher limit, please [contact us](mailto:help@loops.so) and we'll be happy to discuss your needs.
</Accordion>

## Debugging

Sometimes things go wrong. Here are some tips to help you debug your API requests.

<Accordion title="Debugging Steps">
  If you are having trouble with the API, we recommend using a tool like [Postman](https://www.postman.com/) to test your requests.

  ### Handling CORS errors

  The Loops API does not support cross-origin requests made from client-side JavaScript. To avoid CORS errors, make sure to issue your requests from a server-side application.

  ### Dealing with `401 Unauthorized` "Invalid API key" errors

  Make sure you have generated an API key from [Settings -> API](https://app.loops.so/settings?page=api) and that you are including it in your requests.

  Your API key should be included in the "Authorization" header of your request, following the format `Authorization: Bearer YOUR_API_KEY`.

  ### Handling rate limiting (`429` Responses)

  The Loops API allows a maximum of 10 requests per second per team. If you receive a `429 Too Many Requests` response, this means you have exceeded this limit.

  The `x-ratelimit-limit` and `x-ratelimit-remaining` headers in the response can provide information about your current rate limit usage.

  ### Handling other `400`-level Responses

  `400`-level responses typically indicate that there was a problem with the request. The response body will contain more information about what went wrong, so be sure to check it for details.

  Check on your request type (GET, POST, PUT, DELETE) and ensure that you are using the correct one for the endpoint you are trying to access.

  ### "Some body key or value is longer than allowable"

  If you receive this error, it means that a value in the request body is too long. We support a maximum of 500 characters for each value, including the opening and closing quotes. Please reduce the length of the values in your request and try again.

  ***

  If you have followed these steps and are still experiencing issues, don't hesitate to [reach out to the Loops team](https://app.loops.so/settings?page=support) for further assistance.
</Accordion>

## OpenAPI spec

Get started quickly with the Loops API using our OpenAPI documents.

You can import these documents into an API client like Postman or Insomnia to see and use all of our endpoints, with example requests and expected responses.

* **YAML:** [app.loops.so/openapi.yaml](https://app.loops.so/openapi.yaml)
* **JSON:** [app.loops.so/openapi.json](https://app.loops.so/openapi.json)

## SDKs

SDKs are software packages built on top of the API, making it easier to integrate into your project.

<CardGroup>
  <Card title="JavaScript" icon="js" href="/sdks/javascript">
    The official JavaScript/TypeScript SDK for Loops.
  </Card>

  <Card title="Nuxt" icon={<svg viewBox="0 0 61 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M33.9971 39.539H56.5247C57.2402 39.539 57.9432 39.3564 58.5628 39.0093C59.1825 38.6623 59.697 38.1631 60.0546 37.5619C60.4122 36.9608 60.6003 36.2789 60.6 35.5849C60.5997 34.8908 60.411 34.2091 60.0528 33.6083L44.9239 8.1904C44.5663 7.5894 44.0519 7.09032 43.4324 6.74332C42.8129 6.39632 42.1101 6.21363 41.3947 6.21363C40.6793 6.21363 39.9766 6.39632 39.357 6.74332C38.7375 7.09032 38.2231 7.5894 37.8655 8.1904L33.9971 14.6939L26.4338 1.97648C26.0759 1.37553 25.5613 0.876518 24.9416 0.52958C24.3219 0.182643 23.619 0 22.9035 0C22.188 0 21.4851 0.182643 20.8654 0.52958C20.2457 0.876518 19.7311 1.37553 19.3732 1.97648L0.547184 33.6083C0.189033 34.2091 0.00031171 34.8908 3.85805e-07 35.5849C-0.000310938 36.2789 0.187799 36.9608 0.54541 37.5619C0.903021 38.1631 1.41752 38.6623 2.03717 39.0093C2.65681 39.3564 3.35975 39.539 4.07528 39.539H18.2162C23.819 39.539 27.9509 37.1518 30.794 32.4945L37.6965 20.8993L41.3936 14.6939L52.4895 33.3335H37.6965L33.9971 39.539ZM17.9857 33.3272L8.11711 33.325L22.9101 8.47362L30.2912 20.8993L25.3492 29.2044C23.4611 32.2262 21.3162 33.3272 17.9857 33.3272Z" fill="#FF4A00"/></svg>} href="/sdks/nuxt">
    The official Nuxt module for Loops.
  </Card>

  <Card title="PHP" icon="php" href="/sdks/php">
    The official PHP SDK for Loops.
  </Card>

  <Card title="Ruby" icon={<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50" fill="#FF4A00"><path d="M 3.125 23.160156 L 8.183594 14.480469 C 8.230469 14.394531 8.292969 14.316406 8.363281 14.253906 L 17.441406 5.792969 C 17.539063 5.703125 17.65625 5.632813 17.78125 5.585938 L 25.578125 2.722656 L 32.152344 7.316406 L 28.878906 17.722656 L 16.597656 29.132813 L 6.582031 31.378906 Z M 7.296875 33.269531 L 11.96875 46.628906 L 15.8125 31.355469 Z M 42.484375 2.875 L 35.074219 6.992188 L 47.355469 15.910156 C 47.613281 14.761719 47.914063 13.195313 47.984375 11.863281 C 47.980469 11.847656 47.980469 11.828125 47.980469 11.808594 C 48.019531 9.910156 47.707031 7.925781 46.675781 6.210938 C 45.75 4.667969 44.359375 3.539063 42.535156 2.828125 C 42.519531 2.84375 42.507813 2.863281 42.484375 2.875 Z M 34.375 35.578125 L 29.296875 20.058594 L 18.988281 29.644531 Z M 31.144531 19.269531 L 36.1875 34.679688 C 40.132813 30.386719 44.171875 25.246094 46.476563 18.925781 Z M 45.382813 16.949219 L 33.851563 8.578125 L 31.117188 17.269531 Z M 5.761719 34.9375 L 2.335938 40.816406 C 3.507813 46.242188 7.566406 47.457031 10.242188 47.753906 Z M 4.878906 32.484375 L 2 25.644531 L 2 37.421875 Z M 39.921875 2.011719 C 39.90625 2.007813 39.890625 2 39.871094 2 L 28.039063 2 L 33.3125 5.6875 Z M 17.875 31.355469 L 13.777344 47.632813 C 22.109375 46.40625 28.359375 41.929688 33.425781 37.355469 Z M 44.546875 45.648438 C 44.3125 45.648438 44.074219 45.566406 43.882813 45.398438 L 35.617188 38.058594 C 31.984375 41.429688 27.742188 44.855469 22.519531 47.164063 L 44.5625 45.667969 C 44.691406 45.660156 44.8125 45.621094 44.925781 45.570313 C 44.804688 45.621094 44.675781 45.648438 44.546875 45.648438 Z M 37.0625 36.667969 L 45.210938 43.902344 C 45.382813 44.054688 45.472656 44.253906 45.511719 44.460938 L 47.195313 22.414063 C 44.582031 28.078125 40.742188 32.730469 37.0625 36.667969 Z"></path></svg>} href="/sdks/ruby">
    The official Ruby SDK for Loops.
  </Card>
</CardGroup>

### Unofficial SDKs

The following SDKs are community-submitted and have not been officially reviewed or endorsed by Loops. We recommend thoroughly testing and reviewing the code before integrating it into your project.

* [Laravel](https://github.com/plutolinks/laravel-loops) by PlutoLinks
* [PHP](https://github.com/plutolinks/loops-php) by PlutoLinks
* [Ruby on Rails](https://github.com/danielfriis/loops_rails) by Daniel Friis

[Submit an SDK](mailto:dan@loops.so)

## API Reference

The base URL for the API is `https://app.loops.so/api`

### Contacts

Manage contacts.

<CardGroup cols={2}>
  <Card title="Create contact" icon="user-plus" href="/api-reference/create-contact" />

  <Card title="Update contact" icon="user-pen" href="/api-reference/update-contact" />

  <Card title="Find contact" icon="user-magnifying-glass" href="/api-reference/find-contact" />

  <Card title="Delete contact" icon="user-xmark" href="/api-reference/delete-contact" />
</CardGroup>

### Contact properties

Manage contact properties.

<CardGroup cols={2}>
  <Card title="Create contact property" icon="address-book" href="/api-reference/create-contact-property" />

  <Card title="List contact properties" icon="square-list" href="/api-reference/list-contact-properties" />
</CardGroup>

### Mailing lists

View your mailing lists.

<CardGroup cols={2}>
  <Card title="List mailing lists" icon="list" href="/api-reference/list-mailing-lists" />
</CardGroup>

### Events

Send events to trigger emails in loops.

<CardGroup cols={2}>
  <Card title="Send event" icon="bolt" href="/api-reference/send-event" />
</CardGroup>

### Transactional email

Send a transactional email.

<CardGroup cols={2}>
  <Card title="Send transactional email" icon="envelope" href="/api-reference/send-transactional-email" />

  <Card title="List transactional emails" icon="envelopes" href="/api-reference/list-transactional-emails" />
</CardGroup>

### Custom fields

View your account's custom contact properties.

<Warning>
  This endpoint is now deprecated in favor of [List contact properties](/api-reference/list-contact-properties).
</Warning>

<CardGroup cols={2}>
  <Card title="List custom fields" icon="square-list" href="/api-reference/list-custom-fields" />
</CardGroup>

### API key

Test your API key.

<CardGroup cols={2}>
  <Card title="Test API key" icon="square-terminal" href="/api-reference/api-key" />
</CardGroup>
