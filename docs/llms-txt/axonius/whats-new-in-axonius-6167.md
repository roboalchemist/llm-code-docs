# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6167.md

# What's New in Axonius Asset Cloud 6.1.67

#### Release Date: May 18th 2025

These Release Notes contain new features and enhancements added in version 6.1.67.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

  ## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### New, Dedicated Risk Score Page

[**Axonius Risk Score**](/docs/risk-score-settings) settings page is now available and accessible from the Vulnerability Instances page. This page offers a robust solution to assess threat levels and prioritize remediation efforts. Users can calculate the risk scores of different asset types by creating custom conditions and parameters, based on account risk, business impact, and exploitability considerations.
To ensure the calculation is accurate and fits the organization's security needs, users can assign alternative values to fields to normalize data, manipulate the normalized values using operators, or assign numeric values to non-numeric fields. Users can also define fallback conditions.

![RiskScoreReady](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-C3OAA6MB.png)

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Creating a New  Adapter

The number of custom adapters that can be created for SQL Server adapters was raised to 30.

### Adapters Page

#### Bulk Set Advanced Settings Additional Options

Added support for the following options in the **Bulk Set Advanced Settings**:

* Delete devices and other assets that were not returned from the source by a successful fetch in the last X hours

* Delete users that were not returned from the source by a successful fetch in the last X hours

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Appspace**](/docs/appspace)
  * Appspace is a collaboration platform that provides digital signage and workplace experience solutions. (Fetches: Devices, Users)
* [**Bastazo**](/docs/bastazo)
  * Bastazo is a security platform that offers comprehensive attack surface management solutions. (Fetches: Devices)
* [**Harbor**](/docs/harbor)
  * Harbor is an open-source container image registry that provides vulnerability scanning and role-based access control. (Fetches: Vulnerabilities, SaaS Applications, Compute Images)
* [**IBM Guardium Data Security Center**](/docs/ibm-guardium-data-security-center)
  * IBM Guardium Data Security Center is a platform that offers comprehensive data protection and security management solutions. (Fetches: Devices, Users, Databases)
* [**Ironclad Contract Lifecycle Management**](/docs/ironclad-contract-lifecycle-management)
  * Ironclad is a contract lifecycle management platform that offers automated contract creation and management. (Fetches: Users)
* [**ManageEngine ADManager Plus**](/docs/manage-engine-admanager-plus)
  * ManageEngine ADManager Plus is an IT management software suite that offers solutions for IT operations and service management. (Fetches: Devices, Users, Groups)
* [**Xensam Xupervisor**](/docs/xensam-xupervisor)
  * Xensam Xupervisor is a software asset management tool that provides real-time visibility and control over software usage and licenses. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Citrix ShareFile**](/docs/citrix-sharefile) - Added the option to not fetch user permissions and access controls.
* [**Cymulate**](/docs/cymulate-recon) - Added the option to fetch ASM history based on a specified number of latest days instead of the latest ASM endpoint.
* [**GitHub**](/docs/github) - Added the option to fetch issues.
* [**GLPI**](/docs/glpi)
  * This adapter now fetches software and SaaS applications as assets.
  * Added the option to enrich Computers with installed software.
* [**Guardicore**](/docs/guardicore) - Added the option to not fetch users.
* [**Infoblox BloxOne**](/docs/bloxone) - Added the option to fetch Infra Appliances as devices.
* [**Infoblox DDI**](/docs/infoblox) - Added the option to fetch data from WAPI/member:dns.
* [**Microsoft Azure**](/docs/microsoft-azure) - This adapter now fetches Web Application Firewall Policy Rules as Firewalls.
* [**Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM)**](/docs/microsoft-sccm) - Added the option to fetch only active devices where Active0 = 1.
* [**Palo Alto Networks Panorama**](/docs/palo-alto-networks-panorama) - Added the option to ignore all generic host devices.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - The **User Name** and **Password** parameters are no longer mandatory for this adapter, as a new, alternative **OpenID Token** parameter was added. Customers can either provide a user name and a password **or** the OpenID token.
* [**Rapid7 Nexpose and InsightVM**](/docs/rapid7-nexpose) - Added the option to not parse the Host Name field if its value is a valid IP.
* [**SailPoint IdentityIQ**](/docs/sailpoint-iq)
  * Added the option to only fetch users seen within a specified number of days.
  * The filter in the connection now only works for Users assets and not for other asset types.
* [**Trend Micro Deep Security**](/docs/trend-micro-deep-security)
  * This adapter now fetches networks as assets.
  * Added the option to fetch network assets.