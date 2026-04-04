# Source: https://docs.zapier.com/platform/manage/auth-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Change authentication field keys

## Change scenario

You want to change the key of one or more [authentication input fields](/platform/build/basicauth#1-build-an-input-form) required when a user authenticates your app to Zapier.

## Impact to users

This is a **breaking change**.

Modifying the key of an existing authentication field constitutes a breaking change. Without adequate precautions, existing app connections may break as [migration](/platform/manage/migrate) is not possible. Users will need to establish a new connection to your integration and manually refresh each of their Zaps.

## Best practices

We strongly encourage you to **avoid changing authentication field keys** whenever possible.

### Workaround

If your API endpoint requires a different property for authentication, think about adjusting the property key rather than amending the form field input's key. This modification must be made in each trigger, action, search request, as well as in the authentication.

> NOTE: Form field input keys do not need to match directly with the properties your API expects.

For example, let's say you have a form field input with the key `API-KEY`and are sending the field's value to your API using the same property name of `API-KEY`.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=129a0860b6aeb5862331af556cf50d9f" data-og-width="1149" width="1149" data-og-height="211" height="211" data-path="images/daef0487a89a2cbb17ec719cbbd50577.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=da45571ca1e498a0eb6c0c41b34f73a8 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=18394c29c1dd9618cab3719f6acbaa25 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b29ffa808763979e03dc777f32926967 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=61d77861eeb3034bda25b6b813c9aa42 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b61513c96d65abf64357a1337b97dc93 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/daef0487a89a2cbb17ec719cbbd50577.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=e555644c48b3ca8296c2d268d65daa58 2500w" />
</Frame>

```bash  theme={null}
headers: {
  "API-KEY": bundle.authData.api_key; // original
}
```

Next, your API changes and expects the request property to be `X-API-KEY` instead. You can change the request property key (left) as needed. But still refer to the original form field input (right).

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b92ffe70c46b27082fe3b1f3649c8f00" data-og-width="1150" width="1150" data-og-height="207" height="207" data-path="images/bf4cdfe3183752e0e57707001260e9e3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=34477804eac8165fd12bb0a319d87dd8 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3ec0cb4d593ca92b9f2c1ca1c5ee0b45 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=21dc5c320a794cc3ecc071c4f609af1f 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=06a1132fc59e1e5cfb2a866f43f17a94 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=97fe8d0611e360f464a7df99cf409cc4 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/bf4cdfe3183752e0e57707001260e9e3.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=91f9bd80353162beb9322780406008f7 2500w" />
</Frame>

```bash  theme={null}
headers: {
  "X-API-KEY": bundle.authData.api_key; // new - request key and field key can differ
}
```

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
