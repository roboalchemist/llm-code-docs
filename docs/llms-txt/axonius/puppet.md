# Source: https://docs.axonius.com/docs/puppet.md

# Puppet

Puppet is an open-source software configuration management tool.

## Asset Types Fetched

* Devices, Software, SaaS Applications

## Before You Begin

### Required Ports

* Port 8081

### Creating a Certificate

It is highly recommended to create a dedicated certificate for the Puppet adapter.  The name used for the certificate (“axonius" in this example) must be unique and not currently in use.
Follow these steps to generate a certificate in Puppet and upload the required files to Axonius:

1. Connect to the Puppet Master instance with SSH.

2. Run the following command to remove any previous instances of the certificate:

   `sudo /opt/puppetlabs/bin/puppet cert clean axonius_`

3. Run the following command to create the certificate:

   `sudo /opt/puppetlabs/bin/puppet cert generate axonius`

4. Copy the following files to your workstation:

* CA cert: */etc/puppetlabs/puppet/ssl/certs/ca.pem*
* Public key cert: */etc/puppetlabs/puppet/ssl/certs/axonius.pem*
* Private key file: */etc/puppetlabs/puppet/ssl/private\_keys/axonius.pem* (you will need to chmod the private key file to copy it)

5. Upload the respective files to the Axonius adapter configuration page and click **Save**.

### Certificate Permissions

This part is relevant when there are certificate permission issues that require generating a new CA.
On Puppet v.6 and above, use the following commands:

1. Clear old certificate

   `puppetserver ca clear axonius`

2. Generate new certificate

   `puppetserver ca generate --certname axonius`

3. Copy over the files (as described in step 4 in [Creating a Certificate](https://docs.axonius.com/docs/puppet#creating-a-certificate))

4. Make sure that the certificate name is in the PuppetDB certificate-allowlist (by default, in /etc/puppetlabs/puppetdb/certificate-allowlist )

<Callout icon="📘" theme="info">
  **Note**

  Depending on your Puppet version, it may be either "certificate-allowlist" or "certificate-whitelist".
</Callout>

5. Reload the PuppetDB to save the change to the certificate-allowlist:

   `[sudo] puppetdb reload`

## Connecting the Adapter in Axonius

1. **Server Port** - The port used for the connection.
2. **Server Name** - The hostname or IP address of the Puppet server along with port 8081.
3. **CA File** - The Certificate Authority certificate for the Puppet Master instance.
4. **Authentication Method** - Select an authentication method, either **Certificate Based Authentication** (default) or **User Based Authentication**.

   <Tabs>
     <Tab title="Certificate Based Authentication">
       * **Certificate File** - The certificate file containing the public key for the keypair being used to authenticate.  Please see instructions below for generating the certificate in Puppet.
       * **Private Key File** - The private key file for the certificate being used to authenticate.
     </Tab>

     <Tab title="User Based Authentication">
       * **RBAC Token** - A user-based authentication token. For more information, see [Configure security settings](https://www.puppet.com/docs/pe/2023.8/configuring_security_settings#configuring_rbac).
     </Tab>
   </Tabs>

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/PuppetConfig.png)

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  **Note**

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Exclude IPv6 addresses** - Select whether to fetch IPv6 addresses.
   * If enabled, all connections for this adapter will fetch only IPv4 addresses.
   * If disabled, all connections for this adapter will fetch both IPv4 and IPv6 addresses.
2. **Exclude Loopback addresses** - Select whether to exclude any loopback addresses from fetching devices.
3. **Enter prefix to fetch dynamic Puppet fields** - Enter a prefix used on your system for dynamic Puppet fields. Axonius will then fetch all Puppet fields with this prefix and add them to the devices.
4. **Facts Fields to Include** - Specify which Puppet facts should be fetched and displayed as dynamic fields in Axonius. Enter a comma-separated list of fields.

   **Fact Fields Format**

   Each field you enter should be the exact field name (or path) as it appears in the Puppet facts data.

   * **For top-level facts:** Enter the field name directly. For example: `sitecode`, `hypervisors`
   * **For nested or hierarchical facts:** Use a forward slash (/) as the delimiter between levels. For example: `networking/ip`, `os/family`, `processors/models/0`

     Therefore, if the Puppet facts are as follows:

     ```
     {
       "sitecode": "NYC01",
       "hypervisors": "vmware",
       "networking": {
         "ip": "192.168.1.100",
         "mac": "00:11:22:33:44:55"
       },
       "os": {
         "family": "RedHat",
         "release": {
           "major": "8"
         }
       }
     }
     ```

     Enter the following fields for **Facts Fields to Include**:  `sitecode`, `hypervisors`, `networking/ip`, `os/family`, `os/release/major`

     <Callout icon="📘" theme="info">
       **Notes**

       * Field names are case-sensitive and must match exactly their format in the Puppet facts.
       * If a field doesn't exist for a particular device, it is either empty or hidden.
       * After adding new fields, you might need to run a new discovery cycle to see the data.
     </Callout>

   **Field Naming in Axonius**

   The fields are created as dynamic objects in the Devices page, which means that for nested paths, Axonius creates inner fields for each nesting level, thus preserving the hierarchical structure. This allows you to expand and view nested facts in their original structure.

   For example, if you add the `networking/ip` field, Axonius creates a a parent field called `networking` with a nested called `ip` field inside it.

<Callout icon="📘" theme="info">
  **Note**

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>