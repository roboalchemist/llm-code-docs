# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6133.md

# What's New in Axonius 6.1.33

#### Release Date: September 22nd 2024

These Release Notes contain new features and enhancements added in version 6.1.33.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

## Devices and Users Pages New Features and Enhancements

The following new features and enhancements were added to the **Devices**  page.

### OS Is 'End of Life' and 'Is End of Support' Fields Added

The following fields were added to the Devices Page:

* OS: Is End of Life
* OS: Is End of Support
* Preferred OS: Is End of Life
* Preferred OS: Is End of Support

These fields rely on the data in the 'OS: End of Life' and 'OS: End of Support' and 'Preferred OS: End of Life/End of Support'  fields. This allows users to better track information about operating systems that reached or are about to reach end-of-life or end-of-support, and take appropriate action if required.

![IsEOLField](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IsEOLField.png)

### Sort the Installed Software Table by Version

Users can now sort the Installed Software data in the Device Asset Profile by the value in the Software Version column.
![SWVersion\_Sort](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SWVersion_Sort.png)

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

### Accessing Device Breakdown from the Software Page

When clicking on the Device Count field in the Software page, users are redirected to a predefined view in the Devices page displaying all devices that have the selected software installed on them. This view is expanded by default by the Installed Software complex field and includes its following nested fields: Software Name, Software Vendor, Software Version, End-of-Life, and End-of-Support Date, in addition to other fields.

### Querying Software EOL/EOS Data from the Devices Page

When users enable the predefined Software Versions View in the Devices page, they can use the query wizard to query data according to End-of-Life and End-of-Support dates.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Field Mapping and Data Transformations

[Field Mapping](/docs/managing-field-mapping) and [Data Transformations](/docs/managing-data-transformations) are now configurable under **System Settings> Data**.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

In the [Axonius - Send Email to Assets](/docs/send-email-to-entities) Enforcement Action, it is now possible to do the following:

* Upload the custom company logo so that it appears in the header of emails sent by the Enforcement Center.
* Send the email as plain text with all formatting removed.