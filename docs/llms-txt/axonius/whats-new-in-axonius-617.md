# Source: https://docs.axonius.com/docs/whats-new-in-axonius-617.md

# What's New in Axonius 6.1.7

#### Release Date: March 24th 2024

These Release Notes contain new features and enhancements added in version 6.1.7.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Pivot Chart - Set Measure Color

You can now [specify a color for each measure](/docs/adv-pivot-chart#5-metrics) displayed in the Pivot chart. Measure colors are supported in Bar, Stacked Bar, and Matrix chart visualizations.
![MeasureColor](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MeasureColor.png)

## Assets Pages

### Asset Investigation

Support for the following fields was added to [**Asset Investigation**](/docs/advanced-asset-investigation):

* Organizational Unit

* AD Is Domain Controller (DC)

* AD DHCP Server

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

**Detected Field on Vulnerabilities Repositories Page**
A new 'Detected' field was added to the **[Vulnerabilities Repository](/docs/vulnerabilities-repository)** page. This field indicates whether the Vulnerability was detected on Axonius or not.

![VulnDetectedRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VulnDetectedRN.png)

## Findings Center New Features and Enhancements

From the [**Alert** drawer](/docs/viewing-alert-information#viewing-a-findings-center-alert), it is now possible to pivot to the asset list related to the triggered alert exactly as it was at the time of the alert. This asset list is based on historical snapshots from the time of the alert.

![FreezeAlertResults](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FreezeAlertResults.png)

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

* New [regex\_replace](/docs/using-functions-and-keywords#using-the-regexreplace-function) function

  * The new regex\_replace function checks if a specified
    field's string value matches the pattern in regex\_expression, and if it does, replaces it with the string (or function that returns a string) in replace\_value.
    Its syntax is:
    ```
       regex_replace ([field], regex_expression, replace_value)
    ```