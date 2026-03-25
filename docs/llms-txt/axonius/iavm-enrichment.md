# Source: https://docs.axonius.com/docs/iavm-enrichment.md

# IAVM Enrichment

IAVM is a DoD process for identifying and managing security vulnerabilities in critical systems, ensuring timely protection through alerts, bulletins, and advisories.

## Types of Assets Fetched

This adapter does not fetch any assets but enriches data on Aggregated Security Findings and Security Finding Instances, according to the principles of Information Assurance Vulnerability Management (IAVM).

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IAVM Enrichment server that Axonius can communicate with via the [Required Ports](/docs/iavm-enrichment#required-ports).
2. **Certificate File** *(required)* - A local certificate store in PEM format containing a certificate and key that has been provisioned into the system.
3. **Client Key File** *(optional)* - Upload a client key file.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="iavm" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-0UAR88CS.png" />

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1