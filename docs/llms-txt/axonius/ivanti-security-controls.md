# Source: https://docs.axonius.com/docs/ivanti-security-controls.md

# Ivanti Security Controls

Ivanti Security Controls is a unified IT management platform used for managing and protecting Windows-based machines, Red Hat Enterprise and CentOS Linux machines, and VMware ESXi Hypervisors.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Before You Begin

### APIs

Axonius uses the [Ivanti Security Controls REST API](https://help.ivanti.com/iv/help/en_US/isec/API/Topics/Welcome.htm).

**To configure the REST API:**

1. From Microsoft Management Console (MMC), go to **Certificates - Local Computer** `>` **Trusted Root Certification Authorities** `>` **Certificates** folder.
2. Right-click **ST Root Authority** and then select **All Tasks** `>` **Export**.
3. Convert the ST Root certificate with OpenSSL by exporting as a DER by using:

```
 openssl x509 -inform der -in certificate.cer -out certificate.pem
```

4. Verify the ST Root certificate by using:

```
openssl x509 -in certificate.crt -text -noout
```

5. Enable UAC remote restrictions.
6. Upload the certificate in Axonius using the [**Certificate Settings**](/docs/certificate-settings#ssl-trust-ca-settings) tab under **General Settings**.

* For additional requirements, see [Ivanti Security Controls REST API - Requirements](https://help.ivanti.com/iv/help/en_US/isec/API/Topics/Requirements.htm).

### Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* Port 3121

### Required Permissions

The value supplied in [User Name](#parameters):

* Must have read access to devices.
* Must be a local or domain admin.

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Ivanti Security Controls server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Port** - Use the default value.
3. **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image border={false} src="https://files.readme.io/6eb0ceb0e0d1784ab2284006277ce10d6f7f40d510a5ab431cbfccd383b846f5-image.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of threads to open for installed software fetch** *(required, default: 15)* - Set the number of threads to open when fetching the installed software.

2. **Fetch installed software and OS Patches** - Select whether to fetch information about installed software and OS installed security patches for connected devices.

3. **Fetch machine last seen** - Select whether to perform a fetch of all of the patches in the last number of days defined.

4. **Only fetch patch scans with a minimum of x machines** *(required, default: 10)* - Select whether to fetch patch scans that apply to at least the number of machines set here. This setting also fetches installed software.

5. **Fetch all the patches from the last x days** *(required, default: 90)* - Set the number of days back to fetch information about software that was patched in the last X days. This setting also fetches installed software.

6. **Fetch machines** - Clear this option if there is an error fetching machines.

7. **Fetch patch vulnerabilities** - Select this option to fetch CVEs related to the machine security patches.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />