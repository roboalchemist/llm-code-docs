# Source: https://docs.axonius.com/docs/cyberhaven.md

# Cyberhaven

Cyberhaven provides a data detection and response (DDR) solution, based on big data graph analytics of all user interactions with data over time and across the enterprise.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cyberhaven server.

2. **API Key** *(required)* - An API token associated with a user account that has permissions to fetch assets.
   To obtain an API Key, see [APIs](/docs/cyberhaven#apis).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **API Version** - The version number of the Cyberhaven API. Select either **Version 1** (default) or **Version 2**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cyberhaven](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cyberhaven.png)

## APIs

Axonius uses the following APIs:

* [Cyberhaven Public API](https://storage.googleapis.com/cyberhaven-docs/redoc-static.html#/paths/~1api~1rest~1v1~1endpoints~1list/post)
* Cyberhaven API v2.0

**Obtain a token**

```
REFRESH_TOKEN=#tokenfromui
DEPLOYMENT=domain.cyberhaven.io

TOKEN=$(echo $REFRESH_TOKEN | base64 -Dd | xargs -0 -I{} curl -H 'content-type: application/json' https://$DEPLOYMENT/user-management/auth/token -k --data '{}')

```

**Check API**

```
curl -H 'content-type: application/json' -H "Authorization: Bearer $TOKEN" https://$DEPLOYMENT/api/rest/v1/endpoints/list -k --data '{}'

```

**Full Test Script**

```
#!/bin/bash

REFRESH_TOKEN="get your token from /api-tokens"
DEPLOYMENT=your_deployment.cyberhaven.io

TOKEN=$(echo $REFRESH_TOKEN | base64 -Dd | xargs -0 -I{} curl -H 'content-type: application/json' https://$DEPLOYMENT/user-management/auth/token -k --data '{}')

curl -H 'content-type: application/json' -H "Authorization: Bearer $TOKEN" https://$DEPLOYMENT/api/rest/v1/endpoints/list -k --data '{}'
```

## Supported From Version

Supported from Axonius version 4.7