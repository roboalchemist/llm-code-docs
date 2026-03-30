# Source: https://docs.axonius.com/docs/adyen.md

# Adyen

## Overview

Adyen is a financial‑technology platform that provides end‑to‑end payment processing, risk management, and global acquiring for online, mobile, and point‑of‑sale transactions.

This adapter integrates with Adyen's Management API to retrieve  device and user inventory information for inventory and identity visibility in Axonius.

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users

## Before you begin

### &#x20;Ports

* TCP port 80/443

### APIs

* [Adyen Management API v3 ](https://docs.adyen.com/api-explorer/Management/3/overview)
* [https://docs.adyen.com/api-explorer/Management/3/get/terminals](https://docs.adyen.com/api-explorer/Management/3/get/terminals)
* [https://docs.adyen.com/api-explorer/Management/3/get/companies](https://docs.adyen.com/api-explorer/Management/3/get/companies)
* [https://docs.adyen.com/api-explorer/Management/3/get/companies/(companyId)/users](https://docs.adyen.com/api-explorer/Management/3/get/companies/\(companyId\)/users)

### Required Permissions

* To fetch devices, the API credential must have the Management API - Terminal actions read role.
* To fetch users, the API credential must have the Management API - Account read and Management API - Users read and write roles.

#### Supported From Version

Supported from Axonius version 8.0.9

### Configuring the Adyen credentials

## Deploying the Adyen Adapter

* Navigate to the Adapters page, search for `adyen_adapter`, and click on the adapter tile.
* Click on **Add Connection**.

### Required Parameters

1. **Domain** - The base domain for the Adyen Management API.  This must include the URL scheme (https\://). Do not append path segments (the adapter will add /v3/...).
2. **API Key** - Adyen Management API key with the permissions listed under 'Required Permissions'. Refer to [Generate an API Key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) for instructions on how to create the key.
3. **Connection Label** - A user-friendly name for this connection

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Adyen.png" />

### Optional Fields

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.
   <br />