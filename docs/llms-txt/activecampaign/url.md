# Source: https://developers.activecampaign.com/reference/url.md

# Base URL

The API is accessed using a base URL that is specific to your account. In the examples provided in this documentation, we use the URL `youraccountname.api-us1.com` as a stand-in for your real account API URL. Your API URL can be found in your account on the My Settings page under the "Developer" tab. In addition, URL paths should begin with `/api/3` to specify version 3 of the API. Generally, the URL will be in the form `https://<your-account>.api-us1.com/api/3/<resource>`. All API calls should be made over HTTPS.

> 🚧 Base URL Usage for 3rd Party Developers
>
> If you are building an app or integration that requires the user to input their Base URL and API key it is important to **always use the API URL found in the User's "Developer" tab**. It is explicitly not a guarantee that `api-us1.com` is always a supported API Base URL for all current and future users. The Base URL in the "Developer" tab will always be the source of truth for that user. Allowing users to input just an account name instead of the full URL may result in invalid API URLs for some users, particularly users located outside of the United States.