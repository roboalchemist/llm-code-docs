# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/introduction/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> How to authenticate with the Zinc API

To use the Zinc API, you must authenticate every request with your API key.

<Info>
  You can find your API key in your <a href="https://app.zinc.com" target="_blank">Zinc dashboard</a> after creating an account.
</Info>

## Example Authentication Request

```bash  theme={null}
curl https://api.zinc.com/orders \
  -H "Authorization: Bearer <your_api_key>"
```

Authentication is performed using **Bearer token authentication**.

* Include your API key in the `Authorization` header
* Format: `Authorization: Bearer <your_api_key>`

<Warning>
  Never share your API key or expose it in public repositories, client-side code, or other insecure locations. Your API key is tied to your account, and you are responsible for all requests made with it.
</Warning>

If you believe your API key has been compromised, please contact [support@zinc.com](mailto:support@zinc.com) immediately.


Built with [Mintlify](https://mintlify.com).