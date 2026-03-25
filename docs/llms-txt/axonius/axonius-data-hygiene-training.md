# Source: https://docs.axonius.com/docs/axonius-data-hygiene-training.md

# Axonius Data Hygiene

<HTMLBlock>
  {`
  <iframe src="https://fast.wistia.net/embed/iframe/t4yjk3eosj?web_component=true&amp;seo=false&amp;videoFoam=false" frameborder="0" allowfullscreen="true" allow="autoplay; fullscreen" title="Data Hygiene Video" style="display:flex;margin-right:auto;width:640px;height:360px;" width="640" height="360" allowtransparency="true" scrolling="no" class="wistia_embed" name="wistia_embed" dataalign="left" datadisplay="flex"></iframe>
  `}
</HTMLBlock>

## **Introduction**

Axonius Data Hygiene can help organizations find inconsistencies and erroneous data in their security, management, and CMDB systems

**Audience:** Axonius Administrators & End-Users

**Difficulty:** Intermediate to Advanced

**Execution Time:** 1 week, ongoing refinement

**Duration of Use Case:** Perpetual

**Value:** Improved Data Trust & Refinement of Compliance Findings

**What is this use case?**

The primary objective of Data Hygiene is to ensure an accurate representation of any dataset. Within the realm of the Axonius platform, this is an accurate reflection of an organization’s environment and a comprehensive asset inventory for all infrastructure. Data brought into Axonius may be incomplete, inconsistent, out-of-scope, or duplicative, all of which may cause erroneous insights to be generated and may also cause undercorrelation or overcorrelation. Axonius Data Hygiene underpins all use cases within the Axonius Platform and should be considered a foundational practice for all organizations leveraging Axonius.

**Use Case in Action:**

In this presentation, we will focus upon several facets of Data Hygiene, including data completeness, under-correlation and over-correlation. We will use data from various adaptors to explore the more common causes of under and overcorrelation in addition to exploring the key fields which drive correlation. Some examples of adapters prone to data hygiene issues include adapters with humans in the loop (e.g. CMDBs like ServiceNow), and, adapters with sparse data such as Cisco Meraki.

**Why is it Relevant?**

* **Downstream Use Case Accuracy:** Erroneous data coming in from adapters can affect the accuracy of other use cases, such as agent coverage or CMDB reconciliation.
* **Asset Count:** Undercorrelation can inflate asset counts
* **Accuracy of Source Tools:** Erroneous data can indicate a problem with a source tool

## Scope

**How do I build this use case?**

Queries built for Axonius Data Hygiene should focus on the presence of under-correlation, over-correlation, and missing key fields.

1. **Under Correlation Queries**

   1. Undercorrelation Queries should focus on Devices with Distinct Adapter Connections Count = 1 Additionally, focus on specific adapters (such as adapters known to be volatile or that are newly integrated). ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfJ7lbAfvo28w7pUN7B8C5D3DhJWua-h03PsRV7BrtbQMugd7aU8D7GztupjTWdj1ra1oWVRCr4OtuF2eCXemguj3xvCWd6dhXqDSfJUWwpF5Sos2uuJaPUyuLXeHaxo-IEDDfgK-EE2LyefgTKmwric8QretOs2ALRLBUxkit9NQ=nw?key=EWTX9mGFmeKIjpHR0E_qvA)

**Over Correlation Queries**

1. Find systems with multiple values for key fields (such as Serial Number, Host Name, Asset Name, Cloud ID, and MAC address) ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUc2LwLnvv5wmbPFDm_Kao0mZNOsJS65Luoq6Vjhw-8QMWZgoXEg40khUszak_XHUa9KSG6CzaRfRHk67zfFqL23Uz-ACC8xgA87dt7Jq1cC9epQEqFRgSnAyH_4uk6czB4LXY5K2hdOmFK3EuSFQsJUaiUYpfNDtO0i6LglLrTYpQ=nw?key=EWTX9mGFmeKIjpHR0E_qvA)

**Key Field Views**

1. Include columns showing key fields (such as Serial Number, Host Name, Asset Name, Cloud ID, and MAC address) to find systems where key fields are missing, inaccurate, or mismatched. ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUf46WIJ9Yyyn5NrTMziw0jaiI4ELL46UZ3Ug9M9cC2svgY53CI7BpbLxHD0mwtqINzT7OqA6kIBZ_7JIoynlVRjnWKlcH9qBDn7fvYiwhpdZI2j63m4Z9a495KzFaHXKFXrcLH64XHyKO0ZGsxhMdVj3_e8VpM91TAogx6BSQfUJQ=nw?key=EWTX9mGFmeKIjpHR0E_qvA)

## Visibility

**How do I visually explain this use case?**

Initial visualization may be imported using the Data Hygiene dashboard template. Additionally, ask your TAM for additional dashboards available.

There are several types of charts indicating potential data issues:

* **Bad Data Reason Charts**

  * Identify missing or erroneous data within the key fields highlighted earliest (indicating an erroneous data issue) ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdYM3k_zKVvNEWC3eX-J0fXcIAYBihqrkiv3mwqSKGlvYKJ5WbsWXNISkPs0xpI22bQhmqLranSLJhmZ4cWVe3Rox64vTXwzrsRSX-4v9bmkOzSuikYK2bSi9JZjDkFvXVedpgS13IXdJ27n0SzZBkE7J0Xqhe1Dfe5uuAHQPtT6g=nw?key=EWTX9mGFmeKIjpHR0E_qvA)

**Duplicate Charts**

* Highlight Assets where their key field is found on other assets (indicating undercorrelation) ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUe9I3_ca3eh2bzdTt1fREVSuKyI767IJmLhC4OBY_DUNRVF1sOPbDj8WgE1d1fFeGn2e2T4rwL0-F1Ln1zoQczfbqGsTSmx2NkoayIuW5giLzdDeq9bkcSYUspMfbCA25XeXkitLf_olHywJw04kkryv6kAnvi-un6QkfoWtjQP=nw?key=EWTX9mGFmeKIjpHR0E_qvA)

**Over-Correlation Key Fields Charts**

* Identifies devices where more than one entry is contained for key fields (such as Serial Number) ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcAJQulMMIKsZF7KpcLrWcRO6FWTfJnxquxc0b6hJ2wLD1ecF-tEzYkboPzAC-mtPmZrl_0HJRRWTETb3b-2NcOqUhOQjt1VBdShL7tq70JETanzTp0MI4wgyCvMbXle8I7wNditTEZJgQ80PBvVebl0wQvxl5NfrBaShN2Fv1E=nw?key=EWTX9mGFmeKIjpHR0E_qvA)

**Recommended Visualizations**

There are several key visualizations we recommend when starting this use case which attempt to answer key questions by leadership/executives.

* Potential Undercorrelation Issues

  * Count of unique assets with overlapping values on key fields (Field segmentation charts)

Potential Overcorrelation Issues

* Counts of systems with multiple key fields (field summary chart)

Asset Count Over Time

* Track changes to asset count as you resolve data issues (query timeline chart)

## Actionability

**How do I automate this use case?** Automation is a key component for the Axonius Data Hygiene use case, allowing us to immediately take action to resolve the issues we identify. We can break this down into several categories of automation, in increasing order of complexity.

**Monitoring**

* Use Findings to alert on:

  * Large changes in device count that could indicate correlation issues
  * Additions of Adapters/connections

**Add Tags**

* Leverage “Tag Reimaged Devices” to help reduce false-positive data hygiene issues, identifying when a device has been re-imaged
* Leverage Manual and Enforcement-based tagging to reflect findings from Data Hygiene discussions (Such as In-Scope, Out-of-Scope, To be Decommissioned, etc)

**Remediate Source System Data**

* Leverage CMDB reconciliation to correct erroneous CMDB Data
* Utilize Remove Asset enforcements for stale data (such as Old Active Directory entries that are no longer active devices).
* File tickets to integrate the remediation of data hygiene directly into existing workflows.