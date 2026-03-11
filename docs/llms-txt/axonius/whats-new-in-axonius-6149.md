# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6149.md

# What's New in Axonius 6.1.49

#### Release Date: January  12th 2025

These Release Notes contain new features and enhancements added in version 6.1.49.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Set the Start of the Week to Sunday or Monday for Line Charts

You can now  set 'Sunday' or 'Monday' as the [start of the week](/docs/configuring-user-interface-settings) for dashboard charts of all widget types that are displayed as line charts.

#### More Specific Options for Displaying Past Data in Line Charts

More options have been added to the '[Show results from the last](/docs/historical-query-results)' drop-down for line charts. Complete periods of time show data only for time periods that are a full unit.

For example, the last 2 'complete weeks',  displays data from the past 2 full weeks. The last 2 'complete weeks to date'  displays data for the past 2 full weeks, plus the days that have elapsed in the current week so far.

The new options include displaying data for the last:

* Complete weeks

* Complete months

* Complete quarters

* Complete years

* Complete weeks to date

* Complete months to date

* Complete quarters to date

* Complete years to date

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

#### New Date Field Operators

Two new operators were added to each Date field: **Last Calendar Days** and **Next Calendar Days**. They represent a defined range of calendar days (full days) to filter results by, as opposed to the **Last Days** and **Next Days** operators, which count cycles of 24 hours from the moment you run the query.

## Users Page New Features and Enhancements

The following new Preferred Fields were added to the **Users** page:

* **Preferred User Name**

* **Preferred Mail**

## Activity Log New Features and Enhancements

### New "Latest" Option Added to the Discovery Cycle Filter

Users can now filter Activity Logs by the 'latest' Discovery Cycle.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Dynamic Value Statement Wizard Enhancements

The Dynamic Value Statement wizard now supports nesting the *relation* function inside the *concat* function. This allows users to easily include data fetched from related assets in emails, tickets, and more.

### Enhancements to Axonius Actions

#### Axonius - Calculate Risk Score

* The **Axonius - Calculate Risk Score** Enforcement Action is now supported for all asset types, instead of only for Devices and Vulnerabilities. The available **Score Calculation** fields change according to the asset selected.

## Adapter and Enforcement Action Updates

### Adapter Updates

The following adapters were enhanced:

* [**Black Duck**](/docs/blackduck) - Added the capability to enter the format in which to download a report (JSON or CSV).
* [**Cisco Catalyst Center (formerly Cisco DNA Center)**](/docs/cisco-dna-center) - The name of the 'Cisco DNA Center' adapter was changed to **Cisco Catalyst Center (formerly Cisco DNA Center)**.
* [**Druva Cloud Platform**](/docs/druva-cloud-platform)
  * Organization ID was added to connection parameters.
  * Added the option to fetch servers.
* [**CSV**](/docs/csv)
  * Added the option to upload a file from the following source: **Microsoft SharePoint On Premise**.
  * It is now possible to upload CSV files as Accounts/Tenant assets.
* [**Forcepoint Web Security Endpoint CSV File**](/docs/forcepoint-web-security-endpoint) - Added the option to parse "Version" as Agent Version.
* [**Have I Been Pwned**](/docs/have-i-been-pwned) - The **Use Async Fetch** option was removed from the adapter's connection configuration.
* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch the 'Is Interactive' field for the Users asset.
* [**Microsoft Defender for Endpoint (Microsoft Defender ATP)**](/docs/microsoft-defender-atp) - Added the option to fetch Sensors as Devices.
* **Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune** - Fetch Users Last Sign-In - How to fetch now includes options to fetch login errors for 'Enabled in Normal Fetch' and 'Enabled in Background'.
* [**Red Hat Insights**](/docs/red-hat-insights) - Client ID and Client Secret were added to connection parameters.
* [**SecurityScorecard**](/docs/securityscorecard) - Added the option to fetch domains from parent domains.
* [**Tenable.io**](/docs/tenableio) - Added the option to remove the Domain text from the value of the Axonius aggregated field **Local Admins - Groups**.
* **[Workday](/docs/workday#parameters)**
  * Added the option to select whether the custom report applies to Users or Devices.
  * This adapter now fetches devices.
* [**Zscaler Web Security**](/docs/zscaler-web-security) - A dropdown in Advanced Settings (Advanced Configuration section) was added that allows the user to select one or more asset types. Once the asset types are selected, the relevant advanced configurations are displayed. Advanced Configuration is divided into subcategories to make finding of relevant settings easier.  In addition, advanced configurations now have a description in a tooltip which provides information such as asset types, permissions, description, and more.