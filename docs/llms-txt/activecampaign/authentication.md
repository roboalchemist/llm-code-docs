# Source: https://developers.activecampaign.com/reference/authentication.md

# Authentication

All requests to the API are authenticated by providing your API key. The API key should be provided as an HTTP header named `Api-Token`.

**Example:**\
Account name: `123456demo.activehosted.com`\
API Token: `123abc-def-ghi`

```text Header
curl -H "Api-Token: 123abc-def-ghi" https://123456demo.api-us1.com/api/3/users/me
```

<Image title="findYourKey.jpg" alt={2859} align="center" src="https://files.readme.io/640e39b-findYourKey.jpg">
  Your API key can be found in your account on the Settings page under the "Developer" tab. Each user in your ActiveCampaign account has their own unique API key.
</Image>

> ❗️
>
> Remember to keep your API key secret. Do not share it and take care not to expose it publicly in client-side code.