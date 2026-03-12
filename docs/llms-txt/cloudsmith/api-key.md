# Source: https://help.cloudsmith.io/docs/api-key.md

# API Key

<HTMLBlock>
  {`
  <div class="cs-headline">
    In order to use the <a href="https://help.cloudsmith.io/reference">Cloudsmith API</a>, or any other integrations or tools that make use of the Cloudsmith API, you will first need to get your API Key.
  </div>
  `}
</HTMLBlock>

An API Key provides Read and Write access. If you want Read-only access, please use an [Entitlement Token](https://help.cloudsmith.io/docs/entitlements). API Keys and Entitlement Tokens should be treated as secrets to prevent unwarranted access.

## Getting your API Key

There are two ways to retrieve your API Key:

* Via the Cloudsmith web app
* Via the Cloudsmith CLI

### Via the Cloudsmith web app

On the top right corner, click on your user icon, then click on [Personal API Keys](https://docs-staging.cloudsmith.com/getting-started/api-key#:~:text=then%20click%20on-,Personal%20API%20Keys,-and%20click%20Refresh) and click Refresh to view the API Key. Refreshing the API key will permanently disable the current API key. Make sure you store it in a proper secret management tool to access it later.

<Image title="API-Key-Website.png" alt={1367} align="center" src="https://files.readme.io/09519ee2e11428df4ff044a9ab263a299528854a66fec1ac67b67c31216ba2c7-api-key-1.png">
  API-Key via Cloudsmith web app
</Image>

### Via the Cloudsmith CLI

You can retrieve your API key using the cloudsmith login command:

```
cloudsmith login
Login: you@example.com
Password: PASSWORD
Repeat for confirmation: PASSWORD
```

**NOTE**: Please ensure you use your email for the 'Login' prompt.

## Adding IP-Based restrictions to your API-Key

By default, you can use your API-Key from anywhere.

If you wish to restrict the use of your API-Key to a specific IP address or range, you can add the CIDR address/mask to the Allow List:

<Image title="api-IP-restrictions.png" alt={1186} align="center" src="https://files.readme.io/22ae1e116d92758718494a4b11391efb8452889f72711cc83cf6f28b14cd5709-api-ip-restrictions.png">
  API-Key Allow List
</Image>

One you have added your CIDR address/mask, just click the green "Update" button to apply your restriction.