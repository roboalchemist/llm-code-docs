# Source: https://developer.1password.com/docs/events-api/get-started

On this page

# Get started with the 1Password Events API

You can use the 1Password Events API to set up an integration between your 1Password Business account and your security information and event management (SIEM) system.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Before you get started, you\'ll need to [sign up for a 1Password Business account](https://1password.com/pricing/password-manager).

If you already have a business account, you\'ll need to be an [owner](https://support.1password.com/1password-glossary#owner) or [administrator](https://support.1password.com/1password-glossary#administrator) to set up an Events Reporting integration.

## Step 1: Set up an Events Reporting integration[â€‹](#step-1-set-up-an-events-reporting-integration "Direct link to Step 1: Set up an Events Reporting integration") 

You can set up an Events Reporting integration in your 1Password Business account:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Integrations**](https://start.1password.com/integrations/directory) in the sidebar. If you\'ve set up other integrations in your account, you\'ll also need to select **Directory** on the Integrations page.
3.  In the Events Reporting section, choose your SIEM from the list. If your SIEM isn\'t listed, select **Other**.
4.  Enter a name for the integration, then select **Add Integration**.
5.  Set up a bearer token:
    - **Token Name**: Enter a name for the token.
    - **Expires After**: (Optional) Choose when the token will expire: 30 days, 90 days, or 180 days. The default setting is Never.
    - **Events to Report**: Choose which events the token can access. The default scope includes all events: sign-in attempts, item usages, and audit events.
6.  Select **Issue Token**.
7.  On the \"Save your token\" page, select **Save in 1Password**. Choose the vault where you want to save your token, then select **Save**.\
    [Your bearer token will be saved as an [API Credential item](https://support.1password.com/item-categories#api-credential) in 1Password.]
8.  Select **View Integration Details**.

You can issue or revoke bearer tokens for your Events Reporting integration at any time. Learn more about [how to manage bearer tokens](/docs/events-api/authorization#manage-bearer-tokens).

## Step 2: Test the integration[â€‹](#step-2-test-the-integration "Direct link to Step 2: Test the integration") 

Before you connect your 1Password account with your SIEM, you can send a test request to the Events API using [curl ](https://curl.se/) on the command line. Specify the [endpoint](/docs/events-api/endpoints/) along with any required [request headers](/docs/events-api/request-headers/) and data.

### 1. Create a curl request[â€‹](#1-create-a-curl-request "Direct link to 1. Create a curl request") 

In your terminal, format your curl request using the following structure:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[The `Content-Type` header and the `--data` flag with [pagination](/docs/events-api/pagination/) content are only used in `POST` requests to the Events API.]

Replace the highlighted content with your preferred values:

[\<METHOD\>] The [HTTP request method](/docs/events-api/request-methods/) you want to use for your request. For example: `POST`.

[\<base_url\>] The [base URL](/docs/events-api/servers/) of the server used for events in your 1Password account. For example: `https://events.1password.com`.

[\<path\>] The path of the [endpoint](/docs/events-api/endpoints/) you want to use. For example: `/api/v2/signinattempts`.

[\<YOUR_BEARER_TOKEN\>]: The bearer token you generated in [step 1](#step-1-set-up-an-events-reporting-integration). You can use one of the following options:

- Option 1: Copy the credential field from the bearer token you saved in 1Password, then paste it in the authorization header. For example:

  :::::: container_wh0u
  ::::: wrapper_Ok5U
  ::: 
  :::

  ::: 
  [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
  :::
  :::::
  ::::::

  [The `...` at the end of the bearer token here indicates it\'s been truncated for the example. You\'ll need to include the full credential string for your token.]

- Option 2: [Use an environment variable to load your API token](/docs/events-api/generic-scripts#usage) to avoid revealing your bearer token in plaintext. You\'ll need to use double quotes for the authorization header to allow for variable expansion. For example:

  :::::: container_wh0u
  ::::: wrapper_Ok5U
  ::: 
  :::

  ::: 
  [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
  :::
  :::::
  ::::::

[\<number_of_records\>] The optional [pagination limit](/docs/events-api/pagination/) for the maximum number of event records you want returned per page. (POST requests only.) Choose a value from `1` to `1000`.

[\<YYYY-MM-DDTHH:MM:SSZ\>] The optional [RFC 3339-formatted ](https://datatracker.ietf.org/doc/html/rfc3339) date and time (UTC) for when you want to start and stop retrieving events. (POST requests only.) For example: `2025-10-31T09:00:00Z`.

The pagination limit, start time, and end time data is all optional. If you don\'t want to include them in your POST request, use an empty request body for the `--data` flag:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### 2. Send a curl request[â€‹](#2-send-a-curl-request "Direct link to 2. Send a curl request") 

Send your formatted curl request from the terminal.

The following example sends a POST request to the [`signinattempts` endpoint](/docs/events-api/reference#post-apiv2signinattempts), using the curl command structure from the example above.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

See result\...

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### 3. Review the response[â€‹](#3-review-the-response "Direct link to 3. Review the response") 

Review the response that was returned to check that the request was successful.

The example request above shows a successful `200` response, with JSON objects detailing the sign-in attempt event(s) and a cursor for continued calling of the API. See the [response schema for the `signinattempts` endpoint](/docs/events-api/reference#responses-3) for more information.

If the request was successful but your 1Password account didn\'t contain any events within the parameters of your request, the response will still return an object with a [cursor string](/docs/events-api/pagination#cursor). For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If you made a call to a different endpoint, check the [Events API reference](/docs/events-api/reference/) for the appropriate response object schema.

If you see an error, learn more about [HTTP status codes and recommended actions for error messages](/docs/events-api/status-codes).

## Step 3: Connect your 1Password account to your SIEM[â€‹](#step-3-connect-your-1password-account-to-your-siem "Direct link to Step 3: Connect your 1Password account to your SIEM") 

### Use a pre-built connector[â€‹](#use-a-pre-built-connector "Direct link to Use a pre-built connector") 

Many SIEMs already support connecting with 1Password. To use a pre-built connector, [check if your SIEM is in the list of supported applications or services](https://support.1password.com/events-reporting#step-2-connect-your-1password-account-to-your-siem). If it is, you can follow the provided link for documentation on how to connect your 1Password account.

If your SIEM isn\'t listed, you can also check the documentation for that service for any information they might have about connecting to a 1Password account.

### Build your own integration[â€‹](#build-your-own-integration "Direct link to Build your own integration") 

If your SIEM doesn\'t have a pre-built connector, you can build your own client to send your 1Password account activity to your SIEM. Use the [Events API reference](/docs/events-api/reference/) and documentation to learn more about how the API works.

To help you get started, you can refer to the [example scripts in our GitHub repository ](https://github.com/1Password/events-api-generic/) for JavaScript, Python, Ruby, Go, and PHP. Learn more about [how to use the example scripts](/docs/events-api/generic-scripts/).

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [1Password Events API reference](/docs/events-api/reference/)
- [About the 1Password Events API](/docs/events-api/introduction/)
- [1Password Events API generic scripts](/docs/events-api/generic-scripts/)
- [GitHub repository of example scripts ](https://github.com/1Password/events-api-generic/)