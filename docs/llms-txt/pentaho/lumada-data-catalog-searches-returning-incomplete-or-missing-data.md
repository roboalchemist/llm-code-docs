# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data.md

# Data Catalog searches returning incomplete or missing data

If you have a transformation that contains the **Catalog Input**, **Catalog Output**, **Read Metadata**, or **Write Metadata** steps, there may be instances when a complete search of the records in Data Catalog is not performed. This error can occur if:

The default limit provided to prevent PDI from exceeding memory limits or stop connection timeouts to PDC is too short for your environment.

To resolve this issue:

1. Design your transformation.
2. Right-click on the canvas to open the **Transformation properties** dialog box.
3. In the **Parameters** tab, add the following parameter:

   `catalog-result-limit`
4. In the **Default Value** column, enter a number greater than the default value of `25`, for example `500`.
5. Run your transformation.

**Note:** The behavior of this parameter does not directly control the records received from Data Catalog, but rather it works to limit the sub-queries used to retrieve those records. Therefore, you may need to make additional adjustments to establish the correct limit for your environment.
