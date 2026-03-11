# Source: https://docs.axonius.com/docs/brinqa.md

# Brinqa

Brinqa is a cyber risk management platform that helps businesses identify and remediate vulnerabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Brinqa server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Brinqa connection parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4DA96PC4.png" />

## APIs

Axonius uses the [Brinqa Platform API](https://docs.brinqa.com/docs/brinqa-api/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

You must have the following permissions (user roles):

* **Data exporter** -  To download data from list views and access the GraphQL Explorer.
* **Remediation owner** - To access remediation data.
* **Risk Analyst** - Grants read-only access to specific datasets through clusters. Risk analysts can also participate in remediation requests as a requester or a reviewer.

To manage roles, in Brinqa Platform, go to **Administration** `>` **Security**, the select **Roles**. The **Roles** page displays a list view of the existing roles in the Brinqa Platform.

See the [Brinqa documentation](https://docs.brinqa.com/docs/roles/#default-roles) for more information on managing, creating and assigning user roles.

## Supported From Version

Supported from Axonius version 6.1