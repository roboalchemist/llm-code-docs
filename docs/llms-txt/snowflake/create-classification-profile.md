# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/commands/create-classification-profile.md

# CREATE CLASSIFICATION_PROFILE

*Fully qualified name:* SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE

Creates a new instance of the CLASSIFICATION_PROFILE class or replaces an existing instance of the CLASSIFICATION_PROFILE class in the
current or specified schema.

> **Important:**
>
> If you execute a CREATE OR REPLACE command, the classification profile is removed from all databases and schemas, which turns off
> automatic classification.

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  [ IF NOT EXISTS ] <classification_profile_name> (  <config_object> )
```

## Parameters

`classification_profile_name`
:   Specifies the identifier (name) for the instance of the CLASSIFICATION_PROFILE class; must be unique for the schema in which the object
    is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../../../identifiers-syntax.md).

## Constructor arguments

`config_object`
:   An [OBJECT](../../../data-types-semistructured.md) containing key-value pairs used to configure sensitive data classification.

    | Key | Type | Default | Description |
    | --- | --- | --- | --- |
    | `minimum_object_age_for_` `classification_days` | INTEGER |  | Required: Specifies the minimum number of days an object must exist in order to be classified.  To classify objects immediately, specify `0`. |
    | `maximum_classification_` `validity_days` | INTEGER |  | Optional: Specifies the number of days since the last classification event before a table is classified again using automatic classification.  Specify this value to ensure that tables are reclassified. If you omit this key, objects are never reclassified.  The value must be greater than or equal to `1`. |
    | `snowflake_semantic_` `categories` | ARRAY |  | Optional: Specifies a list of Snowflake [native semantic categories](../../../../user-guide/classify-native.md) (types of data) and optional countries to use for classification. Snowflake identifies data as sensitive only if the data is classified as belonging to the specified categories (and countries, if provided). The array can contain the following keys:   * `category` — Required string that specifies a native semantic category. * `country_codes` — Optional array that specifies two-letter country codes. Snowflake identifies data as belonging to a category   only if a semantic subcategory exists for the specified country.  To determine if a semantic subcategory exists for a country and obtain the two-letter code for a country, see   [native semantic categories](../../../../user-guide/classify-native.md).   See [Classify data using a subset of native semantic categories](../../../../user-guide/classify-auto.md). |
    | `auto_tag` | BOOLEAN | TRUE | Optional: When `TRUE`, sets the recommended classification system tags on the columns in the specified object when the classification process is complete.  When `FALSE`, automatic tagging does not occur. |
    | `tag_map` | OBJECT |  | Optional: Maps one or more user-defined tags to the SEMANTIC_CATEGORY system tag.  See Tag map. |
    | `custom_classifiers` | OBJECT |  | Optional: Specifies [custom classifiers](../../../../user-guide/classify-custom.md) that are used when automatically classifying data.  Each key in the object specifies the name of an instance of the [CUSTOM_CLASSIFIER class](../../custom_classifier.md).  The value of each key specifies the [custom_classifier!LIST](../../custom_classifier/methods/list.md) method of the custom classifier instance. |
    | `enable_tag_based_` `sensitive_data_exclusion` | BOOLEAN | FALSE | Optional: When `TRUE`, objects tagged with the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION system tag are excluded from sensitive data classification.  When `FALSE`, tag-based sensitive data exclusion is disabled and all objects are classified regardless of system tags.  For more information, see [Excluding data from sensitive data classification](../../../../user-guide/classify-auto-exclude.md). |
    | `classify_views` | BOOLEAN | FALSE | Optional: When `FALSE`, views are excluded from sensitive data classification. When `TRUE`, views are automatically classified along with tables. |

### Tag map

An [OBJECT](../../../data-types-semistructured.md) that maps one or more user-defined tags to the SEMANTIC_CATEGORY system tag.

`'column_tag_map': [ ... ]`
:   An array of objects that have the following key-value pairs:

    `'tag_name': 'string'`
    :   The fully qualified name of the tag.

        For more information, see [Identifier requirements](../../../identifiers-syntax.md).

    `'tag_value':'string'`
    :   The string value of the tag.

        Optional: If not specified, you must also omit the `semantic_categories` key. If omitted, the `tag_name` tag is applied to
        every column to which the SEMANTIC_CATEGORY system tag is applied, and the value of the user-defined tag will match the value of the
        SEMANTIC_CATEGORY tag.

    `'semantic_categories': [ 'category' [ , 'category' ... ] ]`
    :   A comma-separated list of [native categories](../../../../user-guide/classify-native.md). The `tag_name` user-defined tag is mapped to
        instances where the value of the SEMANTIC_CATEGORY tag is one of the specified native categories.

        Optional: If not specified, you must also omit the `tag_value` key. If omitted, the `tag_name` tag is applied to every
        column to which the system SEMANTIC_CATEGORY tag is applied, and the value of the user-defined tag will match the value of the
        SEMANTIC_CATEGORY tag.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege/role | Object |
| --- | --- |
| CLASSIFICATION_ADMIN database role | n/a |
| CREATE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE privilege | Schema |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Methods

You can call the following methods on the instance of the CLASSIFICATION_PROFILE class that you create:

* [<classification_profile_name>!DESCRIBE](../methods/describe.md)
* [<classification_profile_name>!SET_AUTO_TAG](../methods/set_auto_tag.md)
* [<classification_profile_name>!SET_CLASSIFY_VIEWS](../methods/set_classify_views.md)
* [<classification_profile_name>!SET_CUSTOM_CLASSIFIERS](../methods/set_custom_classifiers.md)
* [<classification_profile_name>!SET_ENABLE_TAG_BASED_SENSITIVE_DATA_EXCLUSION](../methods/set_enable_tag_based_sensitive_data_exclusion.md)
* [<classification_profile_name>!SET_MAXIMUM_CLASSIFICATION_VALIDITY_DAYS](../methods/set_maximum_classification_validity_days.md)
* [<classification_profile_name>!SET_MINIMUM_OBJECT_AGE_FOR_CLASSIFICATION_DAYS](../methods/set_minimum_object_age_for_classification_days.md)
* [<classification_profile_name>!SET_SNOWFLAKE_SEMANTIC_CATEGORIES](../methods/set_snowflake_semantic_categories.md)
* [<classification_profile_name>!SET_TAG_MAP](../methods/set_tag_map.md)
* [<classification_profile_name>!UNSET_CUSTOM_CLASSIFIERS](../methods/unset_custom_classifiers.md)
* [<classification_profile_name>!UNSET_MAXIMUM_CLASSIFICATION_VALIDITY_DAYS](../methods/unset_maximum_classification_validity_days.md)
* [<classification_profile_name>!UNSET_SNOWFLAKE_SEMANTIC_CATEGORIES](../methods/unset_snowflake_semantic_categories.md)
* [<classification_profile_name>!UNSET_TAG_MAP](../methods/unset_tag_map.md)

## Usage notes

* Executing a CREATE OR REPLACE command removes the classification profile from all databases and schemas, which turns off automatic
  classification.
* To refer to this class by its unqualified name, include the database and schema of the class in your
  [search path](../../../snowflake-db-classes.md).
* If the same tag and semantic category is mapped to two different values, then the order of the objects in the `column_tag_map`
  determines the tag and string value to set on a column. Order the `column_tag_map` arrays from highest preference to lowest
  preference.

## Examples

Create an instance and specify basic criteria to automatically classify tables in a database:

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

Create an instance and specify the tag mapping to a single tag:

```sqlexample
CREATE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE my_classification_profile(
  {
    'minimum_object_age_for_classification_days':0,
    'auto_tag':true,
    'tag_map':{
      'column_tag_map':[
        {
          'tag_name':'tag_db.sch.pii'
        }
      ]
    }
  }
);
```

Create an instance and specify the tag mapping to different tag values:

```sqlexample
CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  my_classification_profile(
    {
      'minimum_object_age_for_classification_days':0,
      'auto_tag':true,
      'tag_map': {
        'column_tag_map':[
          {
            'tag_name':'test_ac_db.test_ac_schema.pii',
            'tag_value':'important',
            'semantic_categories':['NAME']
          },
          {
            'tag_name':'test_ac_db.test_ac_schema.pii',
            'tag_value':'pii',
            'semantic_categories':['EMAIL','NATIONAL_IDENTIFIER']
          }
        ]
      }
    }
  );
```

Create an instance and specify custom classifiers for the sensitive data classification process:

```sqlexample
CREATE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE my_classification_profile(
  {
    'minimum_object_age_for_classification_days':0,
    'auto_tag':true,
    'custom_classifiers': {
      'medical_codes': medical_codes!list(),
      'finance_codes': finance_codes!list()
    }
  }
);
```
