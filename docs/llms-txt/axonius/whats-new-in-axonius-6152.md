# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6152.md

# What's New in Axonius 6.1.52

#### Release Date: February 2nd 2025

These Release Notes contain new features and enhancements added in version 6.1.52.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

The following features were added to all assets pages:

### Enhancement to Data Refinement

When refining data by field value or asset entities, users can now choose whether to include or exclude values or asset entities from selected adapter connections, both on Asset pages, and on the Asset Data Chart.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the Asset Graph:

### Select Next Action when Graph Cannot Load

When a step in an Asset Graph investigation cannot be completed, a message is displayed giving the user the choice to either start a new graph or continue from the last successful step.

<Image alt="Screenshot 2025-01-30 at 22.01.31.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Screenshot%202025-01-30%20at%2022.01.31.png" />

## Adapter and Enforcement Action Updates

### Adapter Updates

The following adapters were updated:

* [**Aruba ClearPass**](/docs/aruba-clearpass) - Added the option to parse the "Full-Username" field as hostname from Aruba ClearPass.
* [**Cyberint Argos Edge**](/docs/argos) - Added the capability to specify the number of days back to fetch modified alerts.
* **[Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#microsoft-entra-id-advanced-settings)** -
  * Added the option to fetch the apps usage report from Microsoft and parse the last activity date as the 'Last Seen from Activities' user-aggregated field.
  * Added the option to fetch a list of pre-defined optional strings as extra Intune device attributes.
* [**Mist**](/docs/mist) - Added the option to fetch WiFi clients.
* [**Palo Alto Networks Prisma Cloud Workload Protection**](/docs/prisma-cloud-compute) - Added the option to remove UUID from hostname.
* [**Panorays**](/docs/panorays) - Added the capability to enter a comma-separated list of specific suppliers to fetch.
* [**VMware Workspace ONE (AirWatch)**](/docs/vmware-airwatch)
  * Added the option to fetch the device group data.

  * Added the capability to specify the number of days back to fetch the device's GPS data.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Active Directory - Enrich Devices with Local Users**](/docs/enrich-device-data-with-local-users) - Fetches local users data from devices and enriches it.
* [**Zscaler - Block URLs**](/docs/zscaler-block-url) - Blocks access to selected URLs.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**ServiceNow - Create Incident per Asset**](/docs/create-servicenow-incident-per-entity) - Creates a master ticket with one sub-ticket for each vulnerability or installation of the software.
* [**Wiz - Add Tags to Assets**](/docs/add-tags-to-assets-in-wiz) -
  * Added the option to select Axonius fields from a specific adapter connection to add as tags
  * Added the capability to enter a list of tag keys to include.