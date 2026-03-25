# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6166.md

# What's New in Axonius Asset Cloud 6.1.66

#### Release Date: May 11th 2025

These Release Notes contain new features and enhancements added in version 6.1.66.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Infinite Blue**](/docs/infinite-blue)
  * Infinite Blue is a business continuity and disaster recovery platform that offers planning and management solutions. (Fetches: Devices, Users)
* [**Mend.io**](/docs/mend-io)
  * Mend.io is a software tool that provides automated open-source security and compliance management. (Fetches: Devices, Vulnerabilities, SaaS Applications)
* [**Windows Print Management**](/docs/windows-print-management)
  * Windows Print Management is a tool that offers centralized management and control of print services within a network. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Azure Defender for IoT**](/docs/azure-defender-for-iot) - Added the option to classify Azure IoT Defender assets as Axonius assets. Assets can be fetched as Network Devices, Network Services, or Databases.

* [**BloodHound**](/docs/bloodhound) - Added the option to fetch Tier Zero devices.

* [**CSV**](/docs/csv),[**CSV Legacy Remote File Configuration**](/docs/legacy-remote-file-configuration-csv) and [**Custom Files**](/docs/custom-files) - Added two optional connection parameters under Amazon S3 Bucket: External Role ARN and Entry Point External ID.

* [**CSV - Applications**](/docs/applications-csv) - Added the option to use Axonius-generated setting IDs as hash of application name and setting name.

* [**Eagle Eye Networks (v3)**](/docs/eagle-eye-networks-v3)
  * This adapter now fetches users as assets.
  * Added the option to fetch users from the Users endpoint.

* [**Forescout Switch Plugin**](/docs/forescout-switch-plugin)
  * Added the capability to enter the field and path from the raw JSON to use for the Host Name/Asset Name.
  * Added the capability to enter a list of possible prefixes that need to be removed from the Asset Name and Host Name fields.

* [**Hibob**](/docs/hibob) - Added the option to use a user name and password for authentication.

* [**HPE Aruba Networking**](/docs/aruba) - The name of the 'Aruba' adapter was changed to **HPE Aruba Networking**.

* [**HPE Aruba Networking Management Software (AirWave)**](/docs/aruba-airwave) - The name of the 'Aruba AirWave' adapter was changed to **HPE Aruba Networking Management Software (AirWave)**.

* [**Jamf Pro**](/docs/jamf-pro) - Added the capability to enter a comma-separated list of device IDs for specific devices that you want to fetch.

* [**Microsoft Azure**](/docs/microsoft-azure) - Added the option to filter Policy Definitions and Policy Set Definitions by Policy Assignment IDs.

* [**Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune**](/docs/microsoft-azure-active-directory-ad)
  * Added an option to fetch Enterprise Application Provisioning status.
  * Added an option to fetch data from user extension attributes.

* [**SailPoint IdentityNow**](/docs/sailpoint-identity-now)
  * By default, the system fetches accounts. Added the option to not fetch accounts.
  * By default, the system fetches sources. Added the option to not fetch sources.

* [**Sunflower**](/docs/sunflower)
  * Profile Description, Operation, Interface Type, and Asset Identifier Key were added to connection parameters.
  * Added the capability to enter custom attributes for request.

* [**Tenable.asm**](/docs/tenable-asm) - Added the option to specify ports and record types to fetch.

* [**Trellix Endpoint Security (HX)**](/docs/fireeye-endpoint-security-formerly-hx)
  * This adapter now fetches networks as assets.
  * Added the option to fetch network assets.

* [**WhatsUp Gold**](/docs/whatsup-gold) - Added support for authentication with Access Token.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**GitHub - Create issue**](/docs/en/github-create-issue) - Opens an issue on GitHub based on an Axonius query.
* [**Tenable.io - Overwrite ACR**](/docs/en/tenable-io-overwrite-acr) - Updates the ACR score of assets and sends the assets' UUID and updated score to Tenable.io.
* [**Admin By Request - Delete Computer**](/docs/admin-by-request-delete-computer) - Deletes a computer from Admin By Request.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Halcyon - Set Device Policy**](/docs/set-halcyon-device-mode) - The name of the 'Halcyon - Set Device Mode' enforcement action was changed to **Halcyon - Set Device Policy**.
* [**HTTP Server - Send to Webhook**](/docs/en/send-to-webhook) - Added the option to retry running the Enforcement Action a specified number of times before reporting a failure.