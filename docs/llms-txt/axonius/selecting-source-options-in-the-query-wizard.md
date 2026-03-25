# Source: https://docs.axonius.com/docs/selecting-source-options-in-the-query-wizard.md

# Selecting Source Options in the Query Wizard

Use Different Source Options to create sophisticated query options:

The source dropdown contains the following options:

## Aggregated Data (ALL)

Use **Aggregated Data** to query on all asset common fields fetched from any of the adapter connections.

* **Aggregated Data** is selected by default.

## Complex Field (OBJ)

Use **Complex Field** to query on assets with a specific complex field that meets the specified criteria.

* Example: query on all devices that have installed software that meets the following criteria:
  * **Installed Software:Software Name** contains 'chrome'.
  * **Installed Software:Software Version** NOT later than 86.

![ComplexEG.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ComplexEG.png)

## Asset Entity (ENT)

Use **Asset Entity** to make a query on a specific asset entity, that is, an asset entity fetched from a specific adapter connection.

* **Asset Entity** is useful if assets in your Axonius environment have been correlated by several different asset entities from the same adapter connection, for example: **Amazon Web Services (AWS)**, **Microsoft Entra ID (Azure AD)**, **SolarWinds Network Performance Monitor** and **Tanium**.

  * Example 1: query on all users that were fetched from **Amazon Web Services (AWS)** with a specific **Adapter Connection Label** and the **Device Type** is **EC2**.

![EntEG1.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntEG1.png)

* Example 2: You can also create queries on Complex Fields.

The 'Complex Field’ is available as an option for the second row onwards. You can choose complex fields according to the adapter type selected. For example, you can find devices with an asset entity that has a specific software name and version and that were last seen in the last 7 days.

![EntittQueryEx2.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntittQueryEx2.png)

## Field Comparison (CMP)

Use Field Comparison to compare between adapter field values, and only return assets which match the comparison.

* The following field types are supported: Enum, Boolean, Numeric, Date, and List.
* For String, Enum, and Boolean fields - Equals operand is supported (String comparison is case-sensitive)
* For Numeric fields - Equals, `<`, and `>` operands are supported
* For Date fields - `Equals`, `<`, `>`, `<days`, `>days`, `<hours`, `>hours`, `duration until (days)` and  `duration until (hours)` operands are supported.
* When comparing date fields by days, the time is ignored and only the date is compared.
* The  `>days` and `>hours`  operands let you query if the first date field is later than the second date field by more than the number of days or the number of hours specified.
* The  `<days` and `<hours` operands let you query if the first date field is sooner than the second date field by more than the number of days or the number of hours specified.
  * **Example:** query all devices whose last seen by the **Amazon Web Services (AWS)** adapter is more than 3 days after their last seen by the **Microsoft Active Directory (AD)** adapter.

![FieldCmp1.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldCmp1.png)

* The `duration until (days)` and  `duration until (hours)` operands let you compare the time difference between two date or timestamp fields: view assets where the gap between Field A and Field B is shorter or longer than the specified number of hours or minutes.

  <Callout icon="📘" theme="info">
    **Note**

    These operands only support date or timestamp fields.
  </Callout>

  * **Example:** query all users where the time passed between their First Seen date and Last Seen date is less than 3 days. This is useful for identifying ephemeral (short-lived) assets.

  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/DurationQuery.png)

  * **Additional use cases for running time-duration comparison queries:**
    * Find users whose admin rights were granted and revoked within 1 day, which indicates possible abuse.
    * Find assets that remained unpatched for more than 7 days after a known CVE appeared.

### Field Comparison by Aggregated Values

When you select **Field Comparison**, and then select **Aggregated**, the **Field** dropdown allows you to select by a preferred value, a Common Enrichment field, or by **Latest Used User Email**,  **Last Used Users AD Display Name**, **Total CVE Count** (high, low, etc.), **First Seen**, or **Last Seen**.

![PreferredFields2](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PreferredFields2.png)

### Field Comparison by List Fields

You can compare a list of values to receive an exact or partial match. For example, if you want to compare an Asset Name between devices or compare lists of IP addresses.

Use either the ‘in’, ‘contains’, or ‘equals’ operator to obtain the desired result.

#### Using the 'in' operator

When you select **Field Comparison** by adapter and compare between the list of values in the top and lower rows of the query using the *in* operator, the results show assets where all values from the top row are found within the values of the bottom row.

For example, if the top row lists public IPs and the bottom row lists a device's Network Interface IPs, the results will be devices with network interfaces that include all those public IPs.

![Device\_FieldComparison](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Device_FieldComparison.png)

If  **NOT** is selected, and if the top row contains a device with list values of 10.0.0.1, 10.0.0.2, and 10.0.0.3 and the lower row contains a device with list values of 10.0.0.1, 10.0.0.2, 10.0.0.3, and 10.0.0.4  the resulting devices displayed are all devices with values that aren't mutual between the top row and lower row. For example, 10.0.0.4 is returned.

The fields in the lower row are available by the top row's field type and operator. For example, comparing a single value with another single value by using the *equals* operator won't offer lists to compare. If you use the *in* operator, the list fields are available to compare.

<Callout icon="📘" theme="info">
  Note

  List field values using ‘in’ or ‘equals’ are case-sensitive.
</Callout>

#### Using the 'contains' operator

Use **Field Comparison** with the Contains operator for case-insensitive comparisons of mutual values, like email addresses or partial IP matches. This query returns assets where the top row contains all the values from the bottom row of the query.

![PreferredContains](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PreferredContains.png)

#### Using the 'equals' operator

Use **Field Comparison** with the Equals operator to find assets with exact, case-sensitive matches between lists of values. This query returns assets that contain all values present in both the top and bottom rows of the query.

## Relationship (RLT)

Use **Relationship** to query on assets that are connected to each other, i.e. that have a relationship between them, for instance Users that are connected to Devices.

You can build a relationship query from a certain Asset page by selecting other asset type fields from the query wizard.

**To create a query based on relationship**

1. Open the Assets page relevant to the asset type you are creating the query from and open the **Query Wizard**.
2. From the **Source** dropdown, select **Relationship**.

![SourceDropDown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-28WIOOSP.png)

3.The **Asset Type** dropdown is displayed. The list shows all the asset types which can be related to the asset type that you selected. Only asset types that you have permission to see are displayed in the Asset type dropdown.

<Image align="center" alt="RelationshipAssetType" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-XQ6S9L9Z.png" />

4. Select the asset type that you want to use in the relationship query. In this example, we will assume we are on the **Devices** page and select **Security Findings**.

The following example shows how to query for devices that have critical CVEs, based on the relationship between Devices and Security Findings.

5. The **Select Relationship** field opens. Assets are related by values in specific fields, for instance, Devices and Security Findings may be related by the CVE ID.
   The default field that creates the relationship is displayed and selected. If someone on your system has already created a custom relationship using a different field, then those fields are displayed too.
6. The ‘exists’ function appears by default.

   ![SourceRLT](https://files.readme.io/d6659d0fa9faa0f1e537d382531a10dd8b9ce73757c3872d9390014a1b4a00a3-image.png)

   <br />

<Callout icon="📘" theme="info">
  Note

  The 'count' function is also available for selection in specific cases. This function counts how many relationships exist for an asset - for example, the number of groups associated with a device. If you need to configure a 'count' relationship, contact Axonius support
</Callout>

7. A second row appears. Select the appropriate parameters to complete the query, as demonstrated below.

   ![RLTQuery](https://files.readme.io/f868ec420482096d75f5f2c9deb3c852265dc7a9b2760c8c00507fda78f30afc-image.png)

<Callout icon="📘" theme="info">
  Note

  From the second row on, you can select any source except for Relationship, meaning, You cannot build a relationship query based on another relationship.
</Callout>

8. You can add more conditions (rows) to the query by clicking +. The suggested fields depend on the selected asset type. For example, you can show devices that have critical Security Findings that were first seen in the last 7 days:

   ![RLTQueryAdditionalRows](https://files.readme.io/d19f43599e80b81f14f66a33acd0ca917e8830af7dca6df6fc8628f8ca2d61dd-image.png)

   You can save the relationship query as any other saved query.

<Callout icon="📘" theme="info">
  Note

  When building a relationship query that runs on Security Findings, you cannot use two levels of query (Security Findings and Devices) - you can only add parameters from one level.
</Callout>

### Examples for Relationship Queries

Use Relationship queries to find:

* All users whose last login date was 3 days ago.
* All devices of the enterprise's full time job employees.
* All users who used Unsecured devices in the last 7 days.
* All users who used Unmanaged applications.
* All licenses of Inactive users.