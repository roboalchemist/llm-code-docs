# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6138.md

# What's New in Axonius 6.1.38

#### Release Date: October 27th 2024

These Release Notes contain new features and enhancements added in version 6.1.38.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Responsive Dashboards Provide Enhanced User Experience and Added Capabilities

Axonius Responsive Dashboards provide:

**Flexible Chart Sizing and Configuration**
More variety of options to create custom chart sizes, and the ability to configure the number of items included in each chart. This allows users to display significantly more content, maximizing the available space.

**Drag and Drop Grid Positioning**
Users can drag and drop charts from the top-left corner to change their position on the grid. Charts can be [dynamically resized](/docs/chart-actions#resizing-dashboard-charts) by dragging from the bottom-right corner.

**Consistent Chart Order**
The new grid system ensures that charts maintain their respective order regardless of screen resolution, providing a seamless viewing experience across different screen sizes, devices, and reports shared by email.

**Pin Charts in Grid Position**
Users can [pin specific charts to a fixed location](/docs/chart-actions#pin), ensuring a consistent order even when dragging and dropping charts, or making other changes.

**Chart Links**
Each chart is given a permalink, enabling users to [bookmark and share](/docs/chart-actions#copy-link) specific charts within the Dashboard space. Only users with the necessary permissions can access the charts from a link.

**Export Charts**
Users can [export selected charts](/docs/chart-actions#export) as PNG files, for quick data sharing and integration with additional reporting documents.

**Values Display for Zero/No Data Found**
All charts have been updated to display zeros when query results return zero assets for Count, Count True, and Count False functions. For Sum and Average functions, the text 'No data found' is displayed when no valid data exists. This improves the clarity of data presentations, ensuring stakeholders understand when data is absent versus when the result actually equals zero.

![ChartActions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartActions.jpg)

![Resize(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Resize\(1\).gif)

### New and Updated Dashboard Templates

New SaaS Management Overview Dashboard template was added.

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

Added a 'starts' operator to the Query Wizard for IP Address fields.

## Vulnerability Management Module New Features and Enhancements

### New CVSS Rating Versions Supported

The CVSS field now supports v4.0, in addition to v2.0 and v3.0.

## SaaS Management New Features and Enhancements

### Preferred Category Field Displays a Single Value for SaaS Application Category

You can use the new ['Preferred Category' SaaS Application field](/docs/saas-applications#static-fields) to display a single application category for applications with multiple category values. This is particularly beneficial for avoiding duplicate values when segmenting reports or Dashboard charts by application category.

### New Complex SaaS Application Field: Bitsight Security Rating

The New complex field,[Bitsight Security Rating](/docs/saas-applications#static-fields) includes the following data fetched by the adapter for each relevant SaaS Application:

* **Security Rating** - Bitsight's numeric rating for the application from 250 - 900

* **Risk** - The corresponding risk assigned to the application based on the security rating. Values include High (250-630), Medium (640-730), and Low (740-900).
  For more information, see [What is a Bitsight Security Rating?](https://help.bitsighttech.com/hc/en-us/articles/231352528-What-is-a-Bitsight-Security-Rating)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Data Scope - Improved Configuration for Restricted Fields

Users now have an improved way to configure restricted fields for data scopes. They can now select an adapter directly, and then choose the fields from that specific adapter to exclude or include. It is then possible to select additional adapters with their specific fields as required

### Gateway Support Added to Beyond Trust Password Safe Vault

Added the capability to select the Gateway through which to connect to the [BeyondTrust Password Safe Password Manager](/docs/managing-external-passwords#beyondtrust-password-safe) under **Enterprise Password Management** Settings.

## Case Management New Features and Enhancements

The [Case drawer](viewing-and-editing-case-details)(opens by clicking a Case row in the Case Management table) has a new **Case Assets** tab, which includes:

* A list of the assets on which the Case opened, showing for each asset the Adapter Connections column and the first column from the asset's default view.
* A link to the Assets page filtered to show all Case assets.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Dynamic Value Statement Wizard Enhancement

The Dynamic Value Statement Wizard now supports the [**concat** function](/docs/using-the-dynamic-value-statement-wizard#using-the-concat-function-in-the-wizard) in All and Switch/Case statements. This function assigns to the action field the concatenation of one or more of either or both of the following:

* Custom input - User-entered string
* Adapter field - Value from a selected adapter field

#### Enhancement to set\_value Operator

[Dynamic Value statements](/docs/enforcement-action-condition-syntax-table) now support **set\_value** for Boolean fields:

```
device all then form.field_on set_value true
device all then form.field_on set_value false
```

### Enhancements to Axonius Actions

### Manage Custom Enrichment - Enrich assets with CSV file

In the [Manage Custom Enrichment - Enrich assets with CSV file enforcement action](/docs/add-enrichment), under **Additional Fields**, the new **Interpret a value with semicolons as a list of values** option enables defining a field in the CSV file as a multiple value list field with semicolon delimiters.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Eagle Eye Networks (V3)**](/docs/eagle-eye-networks-v3)
  * Eagle Eye Networks provides cloud-based video surveillance products for physical security and business operations applications. (Fetches: Devices)

* [**Hyperview DCIM**](/docs/hyperview-dcim)
  * Hyperview DCIM is a data center infrastructure management solution that provides real-time monitoring, asset management, and capacity planning for data centers. (Fetches: Devices)

* [**IAVM Enrichment**](/docs/iavm-enrichment)
  * IAVM is a DoD process for identifying and managing security vulnerabilities in critical systems, ensuring timely protection through alerts, bulletins, and advisories.

* [**Microsoft Hyper-V (PSRemote)**](/docs/microsoft-hyper-v-psremote)
  * Microsoft Hyper-V is a native hypervisor. It can create virtual machines on x86-64 systems running Windows. This adapter uses PSRemoting over WinRM, with JEA capabilities. *(Fetches: Devices)*

* [**Mosyle Manager**](/docs/mosyle-manager)
  * Mosyle Manager is a MDM solution designed to manage, configure, and secure Apple devices in educational and enterprise environments. (Fetches: Devices, Users)

* [**NeuShield Data Sentinel**](/docs/neushield-data-sentinel)
  * NeuShield Data Sentinel is a data protection tool that offers ransomware defense and data recovery capabilities. (Fetches: Devices, Accounts/Tenants)

* [**Pharos Beacon**](/docs/pharos-beacon)
  * Pharos Beacon is a cloud print management tool that provides centralized control of organizational print operations. (Fetches: Devices)

* [**Ubiquiti Networks UniFi Cloud Controller**](/docs/ubiquiti-networks-unify-cloud-controller)
  * The UniFi Cloud Controller is a wireless network management software solution for managing multiple wireless networks using a web browser via the Cloud. (Fetches: Devices)

### Adapter Updates

The following adapters were enhanced:

* [**Akamai EEA**](/docs/akamai-eaa#advanced-settings) -       Added option to ignore specific app names and to only fetch apps that are associated with directories.
* [**EfficientIP SOLIDserver DDI**](/docs/efficientip-solidserver) - Added scope options to the list of options to fetch as devices.
* **Flexera SVM** - Added the option to fetch vulnerabilities.
* [**Infoblox DDI**](/docs/infoblox) - Added the capability to not skip records without both a Hostname and a MAC Address.
* [**LeanIX**](/docs/leanix) - This adapter now fetches Application Services.
* **[Microsoft Azure](/docs/microsoft-azure)** -Added the option to enrich Advisor Recommendations in virtual machines with assessment information.
* **Microsoft Defender External Attack Surface Management (Defender EASM)** - This adapter now fetches Domains and URLs. There is an option to set whether to create Device or Domains and URL assets.
* **Microsoft Defender for Endpoint (Microsoft Defender ATP)**  - The Fetch Missing KBs setting now has two options: "Extract from Vulnerabilities API" or "Fetch from Get Missing KBs API"
* **[Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad)** - Added app roles to the fetch when the `Fetch user extensions (service principal)` advanced setting is enabled.
* [**Opal**](/docs/opal) - Added the capability to enrich Opal groups with Opal apps.
* [**Securonix SNYPR**](/docs/securonix-snypr) - Added the option to use API Key authentication.
* [**Schneider Electric EcoStruxure IT  Expert & Data Center Expert**](/docs/schneider-electric-ecostruxure-it) - The name of the 'Schneider Electric EcoStruxure IT' adapter was changed to **Schneider Electric EcoStruxure IT Expert & Data Center Expert**.
* [**Symantec Endpoint Protection 14.x**](/docs/symantec-endpoint-protection)
  * Added the capability to connect the SEMP database and fetch data from it.
  * Added the option to query device definitions from the agent\_def\_cache table in the SEMP database.
* **[Tenable.sc](/docs/tenablesc-formerly-securitycenter)** - Added the option to fetch vulnerabilities with accepted risk.
* **[Tripwire Enterprise](/docs/tripwrie-enterprise)**
  * Added the capability to select the node types to fetch from.
  * Now fetches DBI devices  as Databases
* [**Vectra AI**](/docs/vectra-ai) - Deployment, Client ID, and Client Secret were added to connection parameters.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Okta - Read User (Refetch)**](/docs/refetch-okta-user)
* [**Microsoft MECM - Deploy Package to Devices**](/docs/deploy-package-in-sccm)

### Updated Enforcement Actions

The following Enforcement Actions were updated:

**Slack  - Assign Resource to User**  - Updates were made to this action.