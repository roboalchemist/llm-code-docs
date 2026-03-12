# Source: https://docs.snowflake.com/en/user-guide/classify-auto.md

# Use SQL to set up sensitive data classification

The following sections describe how to use SQL to set up the automatic classification of sensitive data within a database. If you want to
use a web interface to set up sensitive data classification, see [Use the Trust Center to set up sensitive data classification](classify-ui-trust-center.md).

The basic workflow for using SQL to classify sensitive data consists of the following steps:

1. Create a *classification profile* that controls what happens during sensitive data classification.
2. Set the classification profile on a database or schema to automatically classify tables in the entity.

For end-to-end examples of this workflow, see Examples.

## About classification profiles

A classification profile defines the criteria that are used to automatically classify tables in a database. This
criteria includes:

* How long a table should exist before automatically classifying it.
* How long before previously classified tables should be reclassified.
* Whether system and custom tags are automatically set on columns after the classification. You can decide whether you want Snowflake
  to automatically apply suggested tags or prefer to review proposed tag assignments, then apply them yourself.
* A mapping between system classification tags and user-defined object tags so the user-defined tags
  can be applied automatically.
* Whether [custom classifiers](classify-custom.md) are used to classify data.

When a data engineer assigns the classification profile to a database, sensitive data in the tables that belong to the database is
automatically classified on the schedule defined by the profile. A data engineer can assign the same classification profile to multiple
databases, or create multiple classification profiles to set different classification criteria for different databases.

To use SQL to create a classification profile, run the [CREATE CLASSIFICATION_PROFILE](../sql-reference/classes/classification_profile/commands/create-classification-profile.md)
command to create an instance of the CLASSIFICATION_PROFILE
[class](../sql-reference/snowflake-db-classes.md).

For an example of using the CREATE CLASSIFICATION_PROFILE command to create a classification profile, see Examples.

## About tag mapping

You can use the classification profile to map [SEMANTIC_CATEGORY system tags](classify-intro.md) to one or more
[object tags](object-tagging/introduction.md). With this tag mapping, a column with sensitive data can be automatically
assigned a user-defined tag based on its classification. The tag map can be added while creating the classification profile or later by
calling the [<classification_profile_name>!SET_TAG_MAP](../sql-reference/classes/classification_profile/methods/set_tag_map.md) method.

Regardless of whether you are defining the tag map while creating the classification profile or after, the contents of the map are specified
as a JSON object. This JSON object contains the `'column_tag_map'` key, which is an array of objects that specify a user-defined tag,
the string value of that tag, and the semantic categories to which the tag is being mapped.

The following is an example of a tag map:

```javascript
'tag_map': {
  'column_tag_map': [
    {
      'tag_name':'tag_db.sch.pii',
      'tag_value':'Highly Confidential',
      'semantic_categories':[
        'NAME',
        'NATIONAL_IDENTIFIER'
      ]
    },
    {
      'tag_name': 'tag_db.sch.pii',
      'tag_value':'Confidential',
      'semantic_categories': [
        'EMAIL'
      ]
    }
  ]
}
```

Based on this mapping, if you have a column of email addresses and the classification process determines that the column contains these
addresses, the `tag_db.sch.pii = 'Confidential'` tag is set on the column containing the email addresses.

If your tag map includes multiple JSON objects that map tags, tag values, and category values, the order of the JSON objects determines
which tag and value to set on the column if there is a conflict. Specify the JSON objects in the desired assignment order from left to
right, or top to bottom if you are formatting JSON.

> **Tip:**
>
> Each object in the `column_tag_map` field has only has one required key: `tag_name`. If you omit the `tag_value` and
> `semantic_categories` keys, the user-defined tag gets applied to every column to which the SEMANTIC_CATEGORY system tag is applied,
> and the value of the user-defined tag will match the value of the SEMANTIC_CATEGORY tag for a given column.

If there is a conflict with a manually assigned tag and a tag applied by automatic classification, an error occurs. For information about
tracking these errors, see [Troubleshooting sensitive data classification](classify-troubleshooting.md).

## Classify data using a subset of native semantic categories

By default, Snowflake classifies data into its [native semantic categories](classify-native.md) whenever it identifies
sensitive data. A semantic category represents a type of data, such as email addresses, credit card numbers, or social security numbers.

You can configure the classification profile to limit which types of data (semantic categories) to classify as sensitive.
Snowflake classifies data only if it belongs to the subset of semantic categories that you specify in the profile.

The `snowflake_semantic_categories` key in a classification profile’s configuration object defines the list of semantic categories
that you want classified. You can specify which data to classify in two ways:

* **Classify by semantic category**: Specify categories like NAME or EMAIL to classify all data of that type, regardless of location.
* **Classify by semantic category and country**: For categories with country-specific subcategories (like TAX_IDENTIFIER or PASSPORT),
  you can use the `country_codes` key to classify only data from specific countries. For a list of two-letter country codes and
  supported semantic subcategories, see [Native semantic categories of sensitive data classification](classify-native.md).

You can mix both approaches in the same classification profile. The following examples demonstrate each variation:

### Example 1: Classify specific semantic categories

This example configures a classification profile so data is classified only if Snowflake identifies it as belonging to the semantic
categories NAME and NATIONAL_IDENTIFIER. All other types of data are not classified.

```sqlexample
CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  my_classification_profile(
    {
      'minimum_object_age_for_classification_days': 0,
      'snowflake_semantic_categories':
        [
          {'category': 'NAME'},
          {'category': 'NATIONAL_IDENTIFIER'}
        ]
    });
```

### Example 2: Classify a category with specific country codes

For semantic categories that have country-specific subcategories, you can use the `country_codes` key to limit classification to
specific countries. The `country_codes` value is a two-letter country code.

This example classifies data only if Snowflake identifies that it is a tax identifier in Italy (IT) or France (FR):

```sqlexample
CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  my_classification_profile(
    {
      'minimum_object_age_for_classification_days': 0,
      'snowflake_semantic_categories':
        [
          {
            'category': 'TAX_IDENTIFIER',
            'country_codes': ['IT', 'FR']
          }
        ]
    });
```

### Example 3: Combine global and country-specific categories

You can combine semantic categories that do not have country-specific subcategories with categories that do. This example specifies that
Snowflake always classify data belonging to the NAME category and classify the PASSPORT category if the data pertains to United States
passports:

```sqlexample
CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  my_classification_profile(
    {
      'minimum_object_age_for_classification_days': 0,
      'snowflake_semantic_categories':
        [
          {
            'category': 'NAME'
          },
          {
            'category': 'PASSPORT',
            'country_codes': ['US']
          }
        ]
    });
```

## Set a classification profile on a database

Implement sensitive data classification by setting a classification profile on a database. After you set the
classification profile on the database, all tables and views within that database are automatically monitored by sensitive data
classification.

You can also set a classification on a schema. If you set a classification profile on a schema that exists within a database that is also
associated with a classification profile, the profile set on the schema overrides the profile set on the database.

To set a classification profile, use an [ALTER DATABASE](../sql-reference/sql/alter-database.md) or [ALTER SCHEMA](../sql-reference/sql/alter-schema.md) command to set
the CLASSIFICATION_PROFILE parameter. For example, to set a classification profile `my_profile` so all tables and views in the `my_db`
database are monitored by sensitive data classification, run the following command:

```sqlexample
ALTER DATABASE my_db
  SET CLASSIFICATION_PROFILE = 'governance_db.classify_sch.my_profile';
```

## Access control

Here are the privileges and roles that let you work with classification profiles and enable sensitive data
classification.

| Task | Required privileges/roles | Notes |
| --- | --- | --- |
| Create a classification profile | SNOWFLAKE.CLASSIFICATION_ADMIN database role | For information about granting this database role to other roles, see [Using SNOWFLAKE database roles](../sql-reference/snowflake-db-roles.md). |
|  | CREATE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE on schema | You need this privilege on the schema where you want to create the classification profile instance. |
|  | USAGE on database and schema | You need privileges on the schema where you want to create the classification profile instance. |
| Set the classification profile on a database/schema | One of the following:   *EXECUTE AUTO CLASSIFICATION on account* EXECUTE AUTO CLASSIFICATION on database/schema | By default, the owner of the database/schema has the EXECUTE AUTO CLASSIFICATION privilege on it. |
|  | Any privilege on schema’s database | If setting a classification profile on a schema, you need at least one privilege on the database that contains that schema. |
|  | Any privilege on database/schema | You need at least one privilege on the database/schema that contains the table that you want to automatically classify. The EXECUTE AUTO CLASSIFICATION privilege meets this requirement. |
|  | One of the following:   *OWNERSHIP on classification profile instance.* <classification_profile>!PRIVACY_USER instance role on the classification profile. | For information about granting the PRIVACY_USER instance role to other roles, see [Instance roles](../sql-reference/snowflake-db-classes.md). |
|  | APPLY TAG on Account |  |
| Call [methods](../sql-reference/classes/classification_profile.md) on a classification profile instance | <classification_profile>!PRIVACY_USER instance role | For information about granting this instance role to other roles, see [Instance roles](../sql-reference/snowflake-db-classes.md). |
| List classification profiles | <classification_profile>!PRIVACY_USER instance role |  |
| Drop classification profiles | OWNERSHIP on classification profile instance |  |

For an example of granting these privileges and database roles to the role of a data engineer, see Basic example: Automatically classifying tables in a database.

## Examples

* Basic example: Automatically classifying tables in a database
* Example: Using a tag map and custom classifiers
* Example: Testing a classification profile before enabling automatic classification

### Basic example: Automatically classifying tables in a database

Complete these steps to automatically classify a table in the database:

1. As an administrator, give the data engineer the roles and privileges they need to
   automatically classify tables in a database.

   ```sqlexample
   USE ROLE ACCOUNTADMIN;

   GRANT USAGE ON DATABASE mydb TO ROLE data_engineer;
   GRANT EXECUTE AUTO CLASSIFICATION ON DATABASE mydb TO ROLE data_engineer;

   GRANT DATABASE ROLE SNOWFLAKE.CLASSIFICATION_ADMIN TO ROLE data_engineer;
   GRANT CREATE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE ON SCHEMA mydb.sch TO ROLE data_engineer;

   GRANT APPLY TAG ON ACCOUNT TO ROLE data_engineer;
   ```

2. Switch to the data engineer role:

   ```sqlexample
   USE ROLE data_engineer;
   ```

3. [Create the classification profile](../sql-reference/classes/classification_profile/commands/create-classification-profile.md) as an
   instance of the CLASSIFICATION_PROFILE class:

   ```sqlexample
   CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
     my_classification_profile(
       {
         'minimum_object_age_for_classification_days': 0,
         'maximum_classification_validity_days': 30,
         'auto_tag': true,
         'classify_views': false
       });
   ```

4. Call the [DESCRIBE](../sql-reference/classes/classification_profile/methods/describe.md) method on the instance to confirm its properties:

   ```sqlexample
   SELECT my_classification_profile!DESCRIBE();
   ```

5. Set the classification profile instance on the schema, which starts the background process of monitoring tables in the schema and
   automatically classifying them for sensitive data.

   ```sqlexample
   ALTER DATABASE mydb
    SET CLASSIFICATION_PROFILE = 'mydb.sch.my_classification_profile';
   ```

   > **Note:**
   >
   > There is a one-hour delay between setting the classification profile on the schema and Snowflake beginning to classify the schema.
6. After waiting one hour, call the [SYSTEM$GET_CLASSIFICATION_RESULT](../sql-reference/functions/system_get_classification_result.md) stored procedure to obtain the results
   of the automatic classification.

   ```sqlexample
   CALL SYSTEM$GET_CLASSIFICATION_RESULT('mydb.sch.t1');
   ```

### Example: Using a tag map and custom classifiers

1. As an administrator, give the data engineer the roles and privileges they need to
   automatically classify tables in a database and set tags on columns.
2. Create the classification profile.

   ```sqlexample
   CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
     my_classification_profile(
       {
         'minimum_object_age_for_classification_days': 0,
         'maximum_classification_validity_days': 30,
         'auto_tag': true,
         'classify_views': false
       });
   ```

3. Call the [SET_TAG_MAP](../sql-reference/classes/classification_profile/methods/set_tag_map.md) method on the instance to add a
   tag map to the classification profile. This allows custom tags to be automatically applied on
   columns that contain sensitive data.

   ```sqlexample
   CALL my_classification_profile!SET_TAG_MAP(
     {'column_tag_map':[
       {
         'tag_name':'my_db.sch1.pii',
         'tag_value':'sensitive',
         'semantic_categories':['NAME']
       }]});
   ```

   Alternatively, you could have added this tag map when you created the classification profile.
4. Call the [SET_CUSTOM_CLASSIFIERS](../sql-reference/classes/classification_profile/methods/set_custom_classifiers.md) method to add
   [custom classifiers](classify-custom.md) to the classification profile. This allows sensitive data to be automatically
   classified with user-defined semantic and privacy categories.

   ```sqlexample
   CALL my_classification_profile!set_custom_classifiers(
     {
       'medical_codes': medical_codes!list(),
       'finance_codes': finance_codes!list()
     });
   ```

   Alternatively, you could have added the custom classifiers when you created the classification profile.
5. Call the [DESCRIBE](../sql-reference/classes/classification_profile/methods/describe.md) method on the instance to confirm that the
   tag map and custom classifiers have been added to the classification profile.

   ```sqlexample
   SELECT my_classification_profile!DESCRIBE();
   ```

6. Set the classification profile instance on the database.

   ```sqlexample
   ALTER DATABASE mydb
    SET CLASSIFICATION_PROFILE = 'mydb.sch.my_classification_profile';
   ```

7. Attach a masking policy to the `tag_db.sch.pii` tag to enable tag-based masking.

   ```sqlexample
   ALTER TAG tag_db.sch.pii SET MASKING POLICY pii_mask;
   ```

### Example: Testing a classification profile before enabling automatic classification

1. As an administrator, give the data engineer the roles and privileges they need to
   automatically classify tables in a schema and set tags on columns.
2. Create the classification profile with a tag map and custom classifiers:

   ```sqlexample
   CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE my_classification_profile(
     {
       'minimum_object_age_for_classification_days':0,
       'auto_tag':true,
       'tag_map': {
         'column_tag_map':[
           {
             'tag_name':'tag_db.sch.pii',
             'tag_value':'highly sensitive',
             'semantic_categories':['NAME','NATIONAL_IDENTIFIER']
           },
           {
             'tag_name':'tag_db.sch.pii',
             'tag_value':'sensitive',
             'semantic_categories':['EMAIL','MEDICAL_CODE']
           }
         ]
       },
       'classify_views': false,
       'custom_classifiers': {
         'medical_codes': medical_codes!list(),
         'finance_codes': finance_codes!list()
       }
     }
   );
   ```

3. Call the [SYSTEM$CLASSIFY](../sql-reference/stored-procedures/system_classify.md) stored procedure to test the tag mappings on the `table1` table before
   enabling automatic classification.

   ```sqlexample
   CALL SYSTEM$CLASSIFY(
    'db.sch.table1',
    'db.sch.my_classification_profile'
   );
   ```

   The `tags` key in the output contains the details about whether the tag was set (`true` if set, `false` otherwise),
   the name of the tag that was set, and the value of the tag:

   ```output
   {
     "classification_profile_config": {
       "classification_profile_name": "db.schema.my_classification_profile"
     },
     "classification_result": {
       "EMAIL": {
         "alternates": [],
         "recommendation": {
           "confidence": "HIGH",
           "coverage": 1,
           "details": [],
           "privacy_category": "IDENTIFIER",
           "semantic_category": "EMAIL",
           "tags": [
             {
               "tag_applied": true,
               "tag_name": "snowflake.core.semantic_category",
               "tag_value": "EMAIL"
             },
             {
               "tag_applied": true,
               "tag_name": "snowflake.core.privacy_category",
               "tag_value": "IDENTIFIER"
             },
             {
               "tag_applied": true,
               "tag_name": "tag_db.sch.pii",
               "tag_value": "sensitive"
             }
           ]
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
           "semantic_category": "NAME",
           "tags": [
             {
               "tag_applied": true,
               "tag_name": "snowflake.core.semantic_category",
               "tag_value": "NAME"
             },
             {
               "tag_applied": true,
               "tag_name": "snowflake.core.privacy_category",
               "tag_value": "IDENTIFIER"
             },
             {
               "tag_applied": true,
               "tag_name": "tag_db.sch.pii",
               "tag_value": "highly sensitive"
             }
           ]
         },
         "valid_value_ratio": 1
       }
     }
   }
   ```

4. Having verified that automatic classification based on the classification profile will have the desired result, set the classification
   profile instance on the database.

   ```sqlexample
   ALTER DATABASE mydb
    SET CLASSIFICATION_PROFILE = 'mydb.sch.my_classification_profile';
   ```
