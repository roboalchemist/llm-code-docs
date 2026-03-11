# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6161.md

# What's New in Axonius Asset Cloud 6.1.61

#### Release Date: April 6th 2025

These Release Notes contain new features and enhancements added in version 6.1.61.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Customize the Text Displayed When an Item has No Value in the Field Segmentation Chart

Users can edit the text shown in the [Field Segmentation chart](/docs/field-segmentation-chart) when an item has no value to display. By default, the text is 'No Value,' now users can change the text to something else, for example, 'None' or 'N/A.'

## Cases  New Features and Enhancements

The [Case Management table](/docs/case-management-page) can now be filtered to show Cases managed by specific Assignees.

\###[Adapters Fetch History](/docs/adapters-fetch-history) Page Enhancements

* The 'Total Devices' and 'Total Users' columns were added to the default view.

## Adapter and Enforcement Action Updates

### Adapter Updates

The following adapters were updated:

* [**Aruba ClearPass**](/docs/aruba-clearpass) - Added the option to enter a JSON configuration to pre-parse the raw data before parsing the actual device data.
* [**Flexera IT Asset Management**](/docs/flexera-it-asset-management) - Added the capability to enter the table name for software when using the FNMP database.
* [**HPE Aruba Networking Central**](/docs/aruba-central) - The name of the 'Aruba Central' adapter was changed to **HPE Aruba Networking Central**.
* [**JFrog Xray**](/docs/jfrog-xray) - Added the capability to specify how many of the latest versions of each artifact to fetch.
* [**Nexthink Query Language (NQL)**](/docs/nexthink-infinity-nql)
  * The Query ID connection parameter was changed to Device Query ID.
  * User Query ID was added to connection parameters.
  * Added the option to fetch users based on the User Query ID.
* [**Phosphorus**](/docs/phosphorus) - Added the option to fetch excluded devices.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added the capability to fetch Confirmed or Potential detection types.
* [**VMWare ESXi and vSphere**](/docs/vmware-esxi) - Added the capability to enter a list of hostnames to be replaced by the asset name.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Delete Bandura threatER User**](/docs/threater-delete-user) - Deletes users from Bandura threatER.
* **[Illumio - Create Workload](/docs/illumio-create-workload)** - Creates a workload in Illumio.