# Source: https://help.aikido.dev/dast-surface-monitoring/api-scanning/add-additional-headers-in-api-scanning.md

# Add Additional Headers in API Scanning

Add custom headers that Aikido will include in every request during an API scan. This is useful for auth tokens, tenant IDs or any header your service needs before it accepts traffic.

Aikido sends each header you define with all scan requests. The scanner does not try to detect missing headers on its own, so make sure you include everything your API requires. Unlike our [Authentication](https://help.aikido.dev/dast-surface-monitoring/api-scanning/authenticated-api-scanning-for-rest-graphql) these headers are included during the scan.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FcXGsUgwAcWWiz8aWI20d%2FScreenshot%202025-12-01%20at%2016.00.21.png?alt=media&#x26;token=9134d434-1ea5-433f-875c-bca886d854bd" alt=""><figcaption></figcaption></figure>

### Typical use cases

* Static auth tokens for staging or test environments
* X API Key headers
* Version or tenant selectors
* Headers needed to bypass a gateway or WAF in front of your API

## Add a header

1. Click Edit headers in the API Settings page.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F9OQNJ7ZwUoxSabbwjzzs%2FScreenshot%202025-12-01%20at%2016.04.33.png?alt=media&#x26;token=1e2f4c0b-f321-4d2a-af02-ba4df8985c7d" alt=""><figcaption></figcaption></figure>

1. Enter the header name.
2. Enter its value.
3. Add more headers if needed.
4. Save changes.
