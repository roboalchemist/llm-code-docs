# Source: https://docs.snowflake.com/en/user-guide/classify-results.md

# Working with the results of sensitive data classification

This topic describes the ways that you can view the results of sensitive data classification and how you can track classification tags to
monitor sensitive data.

## Use the Trust Center to view results

To view results of sensitive data classification in the Trust Center, complete the following steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md) as a user with the [required privileges](classify-ui-trust-center.md).
2. In the navigation menu, select Governance & security » Trust Center.
3. Select the Data Security tab.
4. Do one of the following:

   * If you want to gain high-level insights into the security of your sensitive data, select the Dashboard tab. For more information,
     see Dashboard page.
   * If you want to list all of the tables and views that have been classified as containing sensitive data, select the
     Sensitive objects tab.

     When the page opens, select a table to see which columns have sensitive data, the
     [semantic category](classify-intro.md) of those columns, and whether tags were applied to the columns.

### Dashboard page

The Dashboard page provides high-level insights into the security of your sensitive data by providing information such as how many
databases and tables have been classified. The page contains the following tiles.

| Tile | Description |
| --- | --- |
| Objects by compliance category | Identifies the number of objects that contain data that might be subject to a regulation or other compliance standard, based on the type of information in the object.  **Note:** The mapping between a compliance category and semantic categories is not exhaustive. Only native semantic categories supported by Snowflake are mapped to a compliance category. For the complete mapping, see Compliance category mappings.  You are solely responsible for determining which regulations or laws apply to your data and ensuring your compliance with the applicable regulations or laws. |
| Objects by semantic category | Identifies the most common semantic categories, and the number of objects that contain data that belong to those categories. |
| Databases monitored by auto-classification | Identifies which databases are currently monitored by sensitive data classification. A database is partially monitored if someone used SQL to set a classification profile directly on a schema in the database rather than setting the profile at the database level. |
| Classification status | Identifies whether all databases currently being monitored for sensitive data have been classified. |
| Sensitive data masking status | Identifies whether sensitive data is protected by a [masking policy](security-column-ddm-intro.md). The masking policy can be a tag-based policy or one that was manually applied to the column.  A table is *fully masked* if every column that contains sensitive data has a masking policy associated with it. A table is *partially masked* if only some columns containing sensitive data are associated with a masking policy. |

### Compliance category mappings

> **Note:**
>
> You are solely responsible for determining which regulations or laws apply to your data and ensuring your compliance with the applicable
> regulations or laws. The compliance categories within sensitive data classification are designed to give you an out-of-the-box toolkit to
> aid your efforts, but are not exhaustive. Only [native semantic categories](classify-native.md) supported by Snowflake are
> mapped to a compliance category.

Use the following table to understand the Objects by compliance category tile on the Dashboard page.

| Compliance category | Native semantic category | Locale |
| --- | --- | --- |
| Digital Personal Data Protection Act (DPDPA) | DATE_OF_BIRTH | n/a |
|  | DRIVERS_LICENSE | India (IN) |
|  | EMAIL | n/a |
|  | NAME | n/a |
|  | NATIONAL_IDENTIFIER | India (IN) |
|  | PHONE_NUMBER | n/a |
|  | STREET_ADDRESS | n/a |
|  | TAX_IDENTIFIER | India (IN) |
| General Data Protection Regulation (GDPR) | AGE | n/a |
|  | DRIVERS_LICENSE | Austria (AT), Belgium (BE), Bulgaria (BG), Croatia (HR), Cyprus (CY), Czech Republic (CZ), Denmark (DK), Estonia (EE), Finland (FI), France (FR), Germany (DE), Greece (GR), Hungary (HU), Ireland (IE), Italy (IT), Latvia (LV), Lithuania (LT), Luxembourg (LU), Malta (MT), Netherlands (NL), Poland (PL), Portugal (PT), Romania (RO), Slovakia (SK), Slovenia (SI), Spain (ES), Sweden (SE) |
|  | EMAIL | n/a |
|  | ETHNICITY | n/a |
|  | GENDER | n/a |
|  | IBAN | n/a |
|  | IMEI | n/a |
|  | IP_ADDRESS | n/a |
|  | NAME | n/a |
|  | NATIONAL_IDENTIFIER | Austria (AT), Belgium (BE), Bulgaria (BG), Croatia (HR), Cyprus (CY), Czech Republic (CZ), Denmark (DK), Estonia (EE), Finland (FI), France (FR), Germany (DE), Greece (GR), Hungary (HU), Ireland (IE), Latvia (LV), Lithuania (LT), Luxembourg (LU), Malta (MT), Netherlands (NL), Poland (PL), Portugal (PT), Romania (RO), Slovakia (SK), Slovenia (SI), Spain (ES), Sweden (SE), United Kingdom (UK) |
|  | PASSPORT | Austria (AT), Belgium (BE), Bulgaria (BG), Croatia (HR), Cyprus (CY), Czech Republic (CZ), Denmark (DK), Estonia (EE), Finland (FI), France (FR), Germany (DE), Greece (GR), Hungary (HU), Ireland (IE), Italy (IT), Latvia (LV), Lithuania (LT), Luxembourg (LU), Malta (MT), Netherlands (NL), Poland (PL), Portugal (PT), Romania (RO), Slovakia (SK), Slovenia (SI), Spain (ES), Sweden (SE) |
|  | PAYMENT_CARD | n/a |
|  | PHONE_NUMBER | n/a |
|  | SALARY | n/a |
|  | TAX_IDENTIFIER | Austria (AT), Cyprus (CY), France (FR), Germany (DE), Greece (GR), Hungary (HU), Italy (IT), Malta (MT), Netherlands (NL), Poland (PL), Portugal (PT), Slovenia (SI), Spain (ES), Sweden (SE) |
|  | VIN | n/a |
| Gramm-Leach-Bliley Act (GLBA) | BANK_ACCOUNT | United States (US) |
|  | DRIVERS_LICENSE | United States (US) |
|  | NAME | United States (US) |
|  | NATIONAL_IDENTIFIER | United States (US) |
|  | PASSPORT | United States (US) |
|  | PAYMENT_CARD | n/a |
|  | STREET_ADDRESS | United States (US) |
|  | TAX_IDENTIFIER | United States (US) |
| Health Insurance Portability and Accountability Act (HIPAA) | ADMINISTRATIVE_AREA_1 | United States (US) |
|  | ADMINISTRATIVE_AREA_2 | United States (US) |
|  | AGE | n/a |
|  | CITY | United States (US) |
|  | DATE_OF_BIRTH | n/a |
|  | EMAIL | n/a |
|  | ETHNICITY | n/a |
|  | IMEI | n/a |
|  | IP_ADDRESS | n/a |
|  | NAME | n/a |
|  | NATIONAL_IDENTIFIER | United States (US) |
|  | PHONE_NUMBER | United States (US) |
|  | POSTAL_CODE | United States (US) |
|  | STREET_ADDRESS | United States (US) |
|  | URL | n/a |
|  | VIN | n/a |
| Payment Card Industry (PCI) | PAYMENT_CARD | n/a |
| Personally identifiable information (PII) | DATE_OF_BIRTH | n/a |
|  | DRIVERS_LICENSE | n/a |
|  | EMAIL | n/a |
|  | NAME | n/a |
|  | NATIONAL_IDENTIFIER | n/a |
|  | PHONE_NUMBER | n/a |
|  | STREET_ADDRESS | n/a |
|  | TAX_IDENTIFIER | n/a |

## Use SQL to view results

You can use SQL to view the results of automatic classification in the following ways:

* Call the [SYSTEM$GET_CLASSIFICATION_RESULT](../sql-reference/functions/system_get_classification_result.md) function. For example:

  ```sqlexample
  CALL SYSTEM$GET_CLASSIFICATION_RESULT('mydb.sch.t1');
  ```

  You cannot return results until the classification process completes. The automatic classification process does not start until one hour
  after setting the classification profile on the database.
* Use a role that is granted the SNOWFLAKE.GOVERNANCE_VIEWER database role to query the
  [DATA_CLASSIFICATION_LATEST](../sql-reference/account-usage/data_classification_latest.md) view. For example:

  ```sqlexample
  SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.DATA_CLASSIFICATION_LATEST;
  ```

  Results might not appear until three hours after classification completes.

## Results for JSON columns

Snowflake can classify columns of type ARRAY, VARIANT, or OBJECT when the semi-structured data is in JSON format. The result of this
classification has the following characteristics:

* The results object contains a `object_path_results` field. This field lists objects, where each object corresponds to
  a field in the semi-structured data that was classified into a native semantic category.
* If there is sensitive data in a field of the semi-structured data, then the semantic category of the *column* is `MULTIPLE`. To obtain
  the semantic category of fields in the semi-structured data, use the `object_path_results` field in the results.

As an example, suppose Snowflake classifies the following table:

```output
+-----------------------------------------------------------+---------------+-----------------------------------------------------+
| ARRAY_COL                                                 | FIRST_NAME    | OBJECT_COL                                          |
+-----------------------------------------------------------+---------------+-----------------------------------------------------+
| [ { "email": "alice@example.com" }, { "email": "b..." } ] | "Joe"         | { "email": "jane@domain.com", "phone": "206-..." }  |
+-----------------------------------------------------------+---------------+-----------------------------------------------------+
```

The classification result might look like the following:

```JSON
{
  "ARRAY_COL": {
    "object_path_results": {
      "ARRAY_COL:[$$].email": {
        "alternates": [],
        "recommendation": {
          "confidence": "HIGH",
          "coverage": 1,
          "details": [],
          "privacy_category": "IDENTIFIER",
          "semantic_category": "EMAIL"
        }
      }
    },
    "recommendation": {
      "confidence": "HIGH",
      "details": [],
      "privacy_category": "IDENTIFIER",
      "semantic_category": "MULTIPLE"
    },
    "valid_value_ratio": 1
  },
  "FIRST_NAME": {
    "alternates": [],
    "recommendation": {
      "confidence": "HIGH",
      "coverage": 1,
      "details": [],
      "privacy_category": "IDENTIFIER",
      "semantic_category": "NAME"
    },
    "valid_value_ratio": 1
  },
  "OBJECT_COL": {
    "object_path_results": {
      "OBJECT_COL:email": {
        "alternates": [],
        "recommendation": {
          "confidence": "HIGH",
          "coverage": 1,
          "details": [],
          "privacy_category": "IDENTIFIER",
          "semantic_category": "EMAIL"
        }
      },
      "OBJECT_COL:phone": {
        "alternates": [],
        "recommendation": {
          "confidence": "HIGH",
          "coverage": 1,
          "details": [
            {
              "coverage": 1,
              "semantic_category": "US_PHONE_NUMBER"
            },
            {
              "coverage": 1,
              "semantic_category": "JP_PHONE_NUMBER"
            }
          ],
          "privacy_category": "IDENTIFIER",
          "semantic_category": "PHONE_NUMBER"
        }
      }
    },
    "recommendation": {
      "confidence": "HIGH",
      "details": [],
      "privacy_category": "IDENTIFIER",
      "semantic_category": "MULTIPLE"
    },
    "valid_value_ratio": 1
  }
}
```

## Use tags to track sensitive data

When Snowflake classifies sensitive data, it suggests or automatically applies system-defined and user-defined tags to the columns that
contain sensitive data. Because columns with sensitive data are assigned these tags, you can monitor the sensitive data by running queries
and calling functions to track the tags.

For example, to list all of the columns that were classified and assigned a semantic category, you can run the following query:

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TAG_REFERENCES
  WHERE TAG_NAME = 'SEMANTIC_CATEGORY'
  ORDER BY object_database, object_schema, object_name, column_name;
```

If you want to determine which semantic category was assigned to the `fname` column of the `hr_data` table, you can run the following
query to obtain the value of the SEMANTIC_CATEGORY tag:

```sqlexample
SELECT SYSTEM$GET_TAG(
  'SNOWFLAKE.CORE.SEMANTIC_CATEGORY',
  'hr_data.fname',
  'COLUMN');
```

For information about the different ways that you can track tags, see [Monitor object tags](object-tagging/monitor.md).
