# Source: https://docs.axonius.com/docs/whats-new-in-axonius-506.md

# What's New in Axonius 5.0.6

These Release Notes contain new features and enhancements added in version 5.0.6.

* Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Axonius 5.0 Ongoing Adapter and Enforcement Action Updates](/docs/axonius-50-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Enhancements

#### Query Comparison Chart

* Query Comparison chart now supports charts based on Vulnerabilities and Software queries.

### New Dashboard Templates

The following new dashboard templates were added:

* [ServiceNow Reconciliation](/docs/servicenow-reconciliation)

* [CISA Known Exploited Vulnerabilities](/docs/cisa-known-exploited-vulnerabilities).

## Devices and Users Page New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

### Asset Investigation

The [Asset Investigation Advanced page](/docs/advanced-asset-investigation) can now be filtered by an existing saved query, so that  **Asset Investigation** will only run on entities that match the results of the saved query.

![AdAssetInvestigatoinScreenNewUp](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdAssetInvestigatoinScreenNewUp.png)

### Query Wizard Enhancements

**Field Comparison Queries**
The **Total CVE Count**   field  can now be be used in **Field Comparison** Queries.

**Associated Devices: Devices Serial**
Associated Devices: Devices Serial can now be queried using count operators.

### Autocomplete Suggestions for Equals Values for Software and Vulnerabilities

In addition to existing autocomplete suggestions on Devices and Users queries, autocomplete suggestions are now supported  for software and vulnerabilities  queries. For the following fields, when the operator is set to equals the value dropdown box displays all of the values that exist in the system, so that the user will easily be able to formulate a valid query, without having to guess the exact name of the component in the system.
**Software**

* Installed Software -  Vendor
* Installed Software - Name

**Vulnerabilities**

* Software vendor

* Software name

* Severity

## Software Management Module New Features and Enhancements

**Added Fields**
The following fields were added to the Software page as optional fields:

* Software description

* Installed software: publisher

* Source

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

**Linux Verify Fingerprint**

On the **UI** page under **[GUI](/docs/configuring-user-interface-settings)**, added an option to make the 'Verify Fingerprint' field a required field on the [Linux SSH](/docs/linux-ssh) adapter and [Axonius - Run Linux SSH Scan](/docs/run-linux-ssh-scan) Enforcement Action.

**HashiCorp Vault**
Added support for [AppRole Authentication](/docs/managing-external-passwords#hashicorp-vault) in **HashiCorp Vault** Enterprise Password Integration.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Filter for Enforcement Set Name

New **Enforcement Name** filter added on the Enforcement Center and Enforcement Center> Run History pages to filter enforcement sets by name.

### Predefined Enforcement Sets

New [predefined enforcement sets](/docs/using-predefined-enforcement-sets) were added that can be easily and quickly used as a basis for new enforcement sets. These view-only enforcement sets are located in the Enforcement Center under the **Predefined Enforcements sets** folder.

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

**Support for Key-pair in a Complex Field**

It is now possible to [write statements ](/docs/using-functions-and-keywords) that assign values from complex fields in assets.

**Support for common enrichment fields**

Common Enrichment fields, i.e., custom enrichment fields based on Aggregated fields, are now supported in dynamic value statements.

### Enhancements to Axonius Actions

**Axonius - Calculate Risk Score Fields Under Custom Data**
The **Risk Score - Axonius calculated field per device** and **Risk Score - Axonius calculated field per vulnerability** fields are also found under Custom Data.