# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6145.md

# What's New in Axonius 6.1.45

#### Release Date: December 15th 2024

These Release Notes contain new features and enhancements added in version 6.1.45.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

## SaaS Management New Features and Enhancements

### New SaaS Applications Fields: Owner and Associated Owner

The SaaS Applications module includes [two new fields](/docs/saas-applications#enrichment-fields):

* **Owner** - The application's owner, that is the person who is responsible for the application  in your organization.

* **Associated Owner** - Displays the value of the 'Username', 'Email, and 'User Department' fields from the Axonius User associated with the SaaS Application Owner.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Creating a New  Adapter

It is now possible to [create new adapters](/docs/create-new-adapter) (CSV/JSON only), each with its own unique pages and the same standard features that can be found in all adapters. Users can also upload their own logo for each custom adapter they create (note that only SVG files are supported). Custom adapters are displayed in the 'Custom Adapter' category.

<Image alt="CreateNewADapter3(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewADapter3(1).png" />

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Exporting Roles and Permissions to CSV

It is now possible to export a list of all existing [roles](/docs/manage-roles) and their permissions, to a CSV file. Exporting to a CSV file aids in compliance, as the date-stamped file indicates the roles and permissions granted at a specific date and time.

### New Information Added to Email Notifications

Email [notifications](/docs/configuring-notification-settings) for low disk space now include the following details:

* **Machine Name or IP Address** - To identify the exact machine with low disk space.
* **Partition Details** - Disk partition names and total sizes.
* **Operating System and Version** - For contextual insight into the system environment.
* **Timestamp of Warning** - To accurately time the alerts for our records.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Additional Schedules for Enforcement Sets

More schedule plans and capabilities were added to the **Select Schedule** tab of the **Create Enforcement Set** drawer. These expanded capabilities enable users to schedule runs on specific days, within defined time ranges, and at custom intervals, such as every X hours, days, weeks, or months. This allows for custom, more precise and adaptable automation of Enforcement Set runs.
To learn more about the new scheduling capabilities, see [Scheduling Enforcement Set Runs](/docs/scheduling-ec-set-runs).

<Image alt="CustomSchedulePlan" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule8(1).png" />

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### filter\_by\_key function

The new **filter\_by\_key** function allows users to filter data within complex fields and extract a specific field value based on a match between another field value and a specified value.
This function checks each object in the complex field for a match between the value of a specified field and a specified value. If there is a match in an object, it adds the value from another specified field to a comma-separated list. This list is returned by the function.
**Syntax**: **filter\_by\_key** (\[**adapter\_complex\_field\_path**], **field\_to\_compare**, **by\_value**, **field\_to\_pick**)
Where

* **adapter\_complex\_field\_path** - The path to the complex field being filtered.

* **field\_to\_compare** - The field in the object to compare with by\_value.

* **by\_value**- The value to match against the field\_to\_compare.

* **field\_to\_pick** - The field whose values are added to the resulting list for all matched objects.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Infoblox IPAM and DHCP**](/docs/infoblox-ipam)
  * Infoblox IPAM and DHCP is a platform that provides automated IP address management and Dynamic Host Configuration Protocol services. (Fetches: Devices)
* [**KnowBe4 PhishER**](/docs/knowb4-phisher)
  * KnowBe4 PhishER is a security awareness tool that helps train users to identify and mitigate phishing threats. (Fetches: Alerts/Incidents)
* [**ManageEngine Applications Manager**](/docs/manage-engine-application-manager)
  * ManageEngine Applications Manager offers full-stack visibility across cloud and on-premise apps, optimizing performance and simplifying IT and DevOps processes. (Fetches: Devices, Business Applications)
* [**Ruckus Virtual SmartZone**](/docs/ruckus)
  * Ruckus vSZ is a virtualized network management system that offers centralized control and monitoring of Wi-Fi networks. (Fetches: Users)
* **[ServiceNow](/docs/servicenow#advanced-settings)** - Added the option to enter device class names to locate for fetching devices as Network Device assets.
* [**STIG**](/docs/stig)
  * STIG is a framework that defines standardized security configurations and compliance requirements for IT systems and software. It retrieves compliance data for security controls to assess adherence to defined requirements. (Fetches: Devices)
* [**ZPE Cloud**](/docs/zpe-systems)
  * ZPE Cloud is a platform that provides secure remote access and management for critical network infrastructure. (Fetches: Devices)

### Adapter Updates

The following adapters were enhanced:

* [**Arista CloudVision**](/docs/arista-cloudvision) - Added the option to fetch vulnerabilities and bug IDs.
* **CrowdStrike Falcon** - Added the option to enrich configuration assessments with Rule Name.
* [**DMARCLY**](/docs/dmarcly) - This adapter now fetches domains and URLs.
* [**GoDaddy**](/docs/godaddy)
  * This adapter now fetches domains and URLs.
  * Added the option to keep fetching devices as URLs as well as devices.
* [**HaloITSM**](/docs/haloitsm) - Added support for OAuth2 authentication.
* [**Hyperview DCIM**](/docs/hyperview-dcim)
  * Token was replaced with Client ID and Client Secret in connection parameters.
  * Added the capability to select asset types to fetch.
  * Added the option to not enrich the assets endpoint with the component asset endpoint.
  * Added the option to not enrich the assets endpoint with the software endpoint.
* [**Jira Service Management (Service Desk)**](/docs/atlassian-jira-service-desk) - This adapter now fetches networks.
* [**Microsoft Azure**](/docs/microsoft-azure) - A page detailing all Azure entity types (services) that can be fetched as Axonius assets by the Microsoft Azure adapter was added to the documentation site. See [Microsoft Azure Services Fetched as Assets](/docs/microsoft-azure-services-fetched-as-assets).
* [**Microsoft Defender for Endpoint for GCC**](/docs/defender-gcc) - It is now possible to provide a custom scope to be used when requesting data from the Microsoft API.
* **[Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#general1)**
  * This adapter now fetches account information for legal holds.
  * Added the option to fetch claims policy for enterprise applications.
  * Added the option to fetch the full Bitlocker information, including the Bitlocker Key.
* [**Sectigo**](/docs/sectigo) - Added the option to not fetch users.
* **ServiceNow** - Added the option to specify table names to parse as Network assets.
* [**Venafi**](/docs/venafi) - Added the option to filter self-signed certificates.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Axonius Network Discovery - Scan**](/docs/network-scanner-scan) - Scans Devices' IP addresses.
* [**Cloudflare Zero Trust - Revoke User Session**](/docs/cloudflare-zero-trust-revoke-user-session) - Revokes the session of Cloudflare Zero Trust compromised users.
* [**GCP - Send Object To Bucket**](/docs/send-object-to-gce) - Sends objects to the selected bucket in Google Cloud Platform.
* [**Okta - Read Group (Refetch)**](/docs/okta-ec-read-group-refetch)

### Updated Enforcement Actions

* [**Cisco Identity Services Engine (ISE) - Apply Policy to Devices**](/docs/cisco-ise) - It is now possible to use this action to also clear policies from devices.
* [**Assign Active Directory Group to Users**](/docs/assign-active-directory-group-to-user) - Added the ability to [test the adapter connection](/docs/create-ec-set#selecting-the-enforcement-set-action).
* [**Microsoft Entra ID (formerly Azure AD) - Assign Group to Users**](/docs/assign-azure-ad-group-to-user) - Groups can now be selected from a list of fetched groups.