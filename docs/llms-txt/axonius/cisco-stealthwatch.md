# Source: https://docs.axonius.com/docs/cisco-stealthwatch.md

# Cisco Stealthwatch

Cisco Stealthwatch is an agentless malware detection solution that provides visibility and network traffic security analytics across the extended network, including endpoints, branch, data center, and cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Cisco SMC Hostname** *(required)* - The hostname or IP address of the Cisco SMC server.

2. **Tenant identifier** *(required)* - Specify the Tenant ID. Tenant ID is the suffix of domain\_\[TENANT\_ID] that can be found when you run the following command on the Cisco SMC server:
   ```

   ls -lsa /lancope/var/smc/config/ | grep domain
   ```
   Note: Only the tenant identifier numbers themselves need to be entered into the field.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cisco Stealthwatch](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20Stealthwatch.png)

## APIs

Axonius uses [Stealthwatch Enterprise REST API Documentation](https://developer.cisco.com/docs/stealthwatch/#!why-use-these-apis).

## Required Ports

HTTPS communication is required between Axonius and the Cisco SMC server.

## Required Permissions

The value supplied in [User Name](#parameters) must be a read-only user. The user should have access to Cisco Stealthwatch SMC (Management Center) with permissions to view exporters.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                            | Supported | Notes |
| ---------------------------------- | --------- | ----- |
| Cisco Stealthwatch 6.10 and higher | Yes       |       |
| Cisco Stealthwatch 6.9  and lower  | No        |       |