# Source: https://docs.beefree.io/beefree-sdk/apis/html-importer-api/authentication.md

# Source: https://docs.beefree.io/beefree-sdk/apis/template-catalog-api/authentication.md

# Source: https://docs.beefree.io/beefree-sdk/apis/content-services-api/authentication.md

# Authentication

## Bearer Token Authentication

Beefree SDK's Content Services API uses bearer tokens to authenticate requests. You can create, view, and manage your bearer token in the [Beefree SDK Developer Console](https://developers.beefree.io). All requests must be made over HTTPS and contain the following HTTP Header:

```http
Authorization: Bearer {token}
```

## Create a Bearer Token

To use the Content Services API you will first need to obtain a your API Key—the bearer token you will use to authenticate to make API calls—from the Beefree SDK Developer Console.

To obtain an API Key, take the following steps:

1. Log in to the [Beefree SDK Developer Console](https://developers.beefree.io/).
2. Navigate to the application you'd like to activate the Content Services API for.
3. Click on the corresponding **Details** button.
4. Navigate to the Content Services API section of the **Details** page.
5. Click **Create New API Key**.

   A pop up will appear asking you to confirm that you understand [usage-based fees](https://devportal.beefree.io/hc/en-us/articles/4403095825042-Usage-based-fees) may apply.
6. Click **Create Key**.

Your API key will appear under the **Content services API** section of your application details.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F6o1tCK3iLvxHISxaIqy8%2FCleanShot%202025-05-01%20at%2018.53.41.png?alt=media&#x26;token=09c5e077-696f-4486-af44-e8d537fe0963" alt=""><figcaption><p>Screenshot of the Details page in the Developer Console with the CSAPI section highlighted</p></figcaption></figure>
